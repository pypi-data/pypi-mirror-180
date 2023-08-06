import argparse
import os
from pprint import pprint
from typing import Union, Optional

import timm
import torch
import torch.nn as nn
import torchvision.transforms as transforms
from PIL import Image
from pytorch_lightning import LightningModule, LightningDataModule, Trainer
from pytorch_lightning.callbacks import ModelCheckpoint, LearningRateMonitor
from pytorch_lightning.utilities.seed import seed_everything
from torch.utils.data import DataLoader
from torchmetrics import Accuracy
from torchvision.datasets import ImageFolder
from .randaug import RandAugment
from timm.data.transforms_factory import create_transform  



# solver settings
OPT = 'adam'  # adam, sgd
WEIGHT_DECAY = 0.0001
MOMENTUM = 0.9  # only when OPT is sgd
LR_SCHEDULER = 'step'  # step, multistep, reduce_on_plateau
LR_DECAY_RATE = 0.1
LR_STEP_SIZE = 5  # only when LR_SCHEDULER is step
LR_STEP_MILESTONES = [10, 15]  # only when LR_SCHEDULER is multistep


def get_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description='Train classifier.')
    parser.add_argument('--dataset', '-d', type=str, required=True, help='Root directory of dataset')
    parser.add_argument('--outdir', '-o', type=str, default='results', help='Output directory')
    parser.add_argument('--model-name', '-m', type=str, default='resnet18', help='Model name (timm)')
    parser.add_argument('--img-size', '-i', type=int, default=224, help='Input size of image')
    parser.add_argument('--epochs', '-e', type=int, default=100, help='Number of training epochs')
    parser.add_argument('--save-interval', '-s', type=int, default=10, help='Save interval (epoch)')
    parser.add_argument('--batch-size', '-b', type=int, default=8, help='Batch size')
    parser.add_argument('--num-workers', '-w', type=int, default=12, help='Number of workers')
    group = parser.add_mutually_exclusive_group()
    group.add_argument('--gpu-ids', type=int, default=None, nargs='+', help='GPU IDs to use')
    group.add_argument('--n-gpu', type=int, default=None, help='Number of GPUs')
    parser.add_argument('--seed', type=int, default=42, help='Seed')
    args = parser.parse_args()
    return args




def get_optimizer(parameters, base_lr) -> torch.optim.Optimizer:
    if OPT == 'adam':
        optimizer = torch.optim.Adam(parameters,
                                     lr=base_lr,
                                     weight_decay=WEIGHT_DECAY)
    elif OPT == 'sgd':
        optimizer = torch.optim.SGD(parameters,
                                    lr=base_lr,
                                    weight_decay=WEIGHT_DECAY,
                                    momentum=MOMENTUM)
    else:
        raise NotImplementedError()

    return optimizer


def get_lr_scheduler_config(optimizer: torch.optim.Optimizer) -> dict:
    if LR_SCHEDULER == 'step':
        scheduler = torch.optim.lr_scheduler.StepLR(
            optimizer,
            step_size=LR_STEP_SIZE,
            gamma=LR_DECAY_RATE)
        lr_scheduler_config = {
            'scheduler': scheduler,
            'interval': 'epoch',
            'frequency': 1,
        }
    elif LR_SCHEDULER == 'multistep':
        scheduler = torch.optim.lr_scheduler.MultiStepLR(
            optimizer,
            milestones=LR_STEP_MILESTONES,
            gamma=LR_DECAY_RATE)
        lr_scheduler_config = {
            'scheduler': scheduler,
            'interval': 'epoch',
            'frequency': 1,
        }
    elif LR_SCHEDULER == 'reduce_on_plateau':
        scheduler = torch.optim.lr_scheduler.ReduceLROnPlateau(
            optimizer,
            mode='max',
            factor=0.1,
            patience=10,
            threshold=0.0001)
        lr_scheduler_config = {
            'scheduler': scheduler,
            'monitor': 'val/loss',
            'interval': 'epoch',
            'frequency': 1,
        }
    else:
        raise NotImplementedError

    return lr_scheduler_config


class ImageTransform:
    def __init__(self, is_train: bool, img_size: Union[int, tuple] = (224,224)):
        if type(img_size) == int:
            img_size = (img_size, img_size)
        if is_train:
            self.transform = create_transform(224, is_training=True,auto_augment="rand-m9-n3-mstd0.5")
            """
            self.transform = transforms.Compose([
                #transforms.RandomHorizontalFlip(p=0.5),
                RandAugment(2, 9), 
                transforms.Resize(img_size),
                transforms.ToTensor(),
                transforms.Normalize(mean=[0.485, 0.456, 0.406],
                                     std=[0.229, 0.224, 0.225])
            ])
            """
        else:
            self.transform = create_transform(224,)
            """
            self.transform = transforms.Compose([
                transforms.Resize(img_size),
                transforms.ToTensor(),
                transforms.Normalize(mean=[0.485, 0.456, 0.406],
                                     std=[0.229, 0.224, 0.225])
            ])
            """

    def __call__(self, img: Image.Image) -> torch.Tensor:
        return self.transform(img)


class SimpleData(LightningDataModule):
    def __init__(self, root_dir: str, img_size: int = 224, batch_size: int = 8, num_workers: int = 16):
        super().__init__()
        self.root_dir = root_dir
        self.img_size = img_size
        self.batch_size = batch_size
        self.num_workers = num_workers

        self.train_dataset = ImageFolder(root=os.path.join(root_dir, 'train'),
                                         transform=ImageTransform(is_train=True, img_size=self.img_size))
        self.val_dataset = ImageFolder(root=os.path.join(root_dir, 'val'),
                                       transform=ImageTransform(is_train=False, img_size=self.img_size))
        self.classes = self.train_dataset.classes
        self.class_to_idx = self.train_dataset.class_to_idx

    def train_dataloader(self) -> DataLoader:
        dataloader = DataLoader(self.train_dataset,
                                batch_size=self.batch_size,
                                shuffle=True,
                                drop_last=True,
                                num_workers=self.num_workers)
        return dataloader

    def val_dataloader(self) -> DataLoader:
        dataloader = DataLoader(self.val_dataset,
                                batch_size=self.batch_size,
                                shuffle=False,
                                drop_last=False,
                                num_workers=self.num_workers)
        return dataloader


class SimpleModel(LightningModule):
    def __init__(self, model_name: str = 'resnet18',
                 pretrained: bool = False, num_classes: Optional[int] = None, class_to_index=None, img_size=224,base_lr=0.01):
        super().__init__()
        self.save_hyperparameters()
        self.model = timm.create_model(model_name=model_name,
                                       pretrained=pretrained,
                                       num_classes=num_classes)
        self.train_loss = nn.CrossEntropyLoss()
        self.train_acc = Accuracy()
        self.val_loss = nn.CrossEntropyLoss()
        self.val_acc = Accuracy()
        self.base_lr = base_lr

    def forward(self, x):
        return self.model(x)

    def training_step(self, batch, batch_idx):
        x, target = batch

        out = self(x)
        _, pred = out.max(1)

        loss = self.train_loss(out, target)
        acc = self.train_acc(pred, target)
        self.log_dict({'train/loss': loss, 'train/acc': acc}, prog_bar=True)

        return loss

    def validation_step(self, batch, batch_idx):
        x, target = batch

        out = self(x)
        _, pred = out.max(1)

        loss = self.val_loss(out, target)
        acc = self.val_acc(pred, target)
        self.log_dict({'val/loss': loss, 'val/acc': acc})

    def configure_optimizers(self):
        optimizer = get_optimizer(self.parameters(),self.base_lr)
        lr_scheduler_config = get_lr_scheduler_config(optimizer)
        return {"optimizer": optimizer, "lr_scheduler": lr_scheduler_config}


def get_basic_callbacks(checkpoint_interval: int = 1) -> list:
    lr_callback = LearningRateMonitor(logging_interval='epoch')
    ckpt_callback = ModelCheckpoint(filename='{epoch}-{val/loss:.2f}',
                                    auto_insert_metric_name=False,
                                    save_top_k=2,
                                    monitor="val/acc",
                                    save_last=True,
                                    mode="max",
                                    every_n_epochs=checkpoint_interval)
    return [ckpt_callback, lr_callback]


def get_gpu_settings(gpu_ids) -> tuple:
    if gpu_ids is not None:
        # list
        gpus = gpu_ids
        strategy = "ddp" if len(gpus) > 1 else None   
    else:
        gpus = 1
        strategy = None
    gpus = gpus if torch.cuda.is_available() else None
    strategy = None if gpus is None else strategy
    return gpus, strategy


def get_trainer(epochs, outdir, save_interval, gpu_ids) -> Trainer:
    callbacks = get_basic_callbacks(checkpoint_interval=save_interval)
    gpus, strategy = get_gpu_settings(gpu_ids)
    trainer = Trainer(
        max_epochs=epochs,
        callbacks=callbacks,
        default_root_dir=outdir,
        gpus=gpus,
        strategy=strategy,
        logger=True,
    )
    return trainer

def run_train(dataset_path, model_name="resnet18", outdir="results", img_size=224, epochs=100, save_interval=10, batch_size=8, num_workers=12, gpu_ids=[0], seed=42, base_lr=0.01):
    seed_everything(seed)
    data = SimpleData(root_dir=dataset_path, img_size=img_size,
                      batch_size=batch_size, num_workers=num_workers)
    model = SimpleModel(model_name=model_name,
                        pretrained=True,
                        num_classes=len(data.classes), class_to_index=data.class_to_idx, img_size=img_size,base_lr=base_lr)
    trainer = get_trainer(epochs, outdir, save_interval, gpu_ids)
    trainer.fit(model, data)

