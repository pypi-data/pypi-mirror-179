from typing import Optional
import os

from dimweb_persona_bot.dataloaders.datasets import BaseInitialDatasetV1
from dimweb_persona_bot.dataloaders.causal_samplers.causal_samplers_hypothesis_1 import (
    BaseDatasetSampleV1,
)
from dimweb_persona_bot.hyperparameters.causal_modeling_hyperparameters import (
    BaseHyperparametersV1,
)

from pytorch_lightning import LightningDataModule

import torch
from torch.utils.data import DataLoader, Dataset

from transformers import AutoTokenizer


class PytorchDatasetV1(Dataset):
    def __init__(
        self,
        dataset: BaseInitialDatasetV1,
        tokenizer: AutoTokenizer,
        dataset_sample_class: BaseDatasetSampleV1,
        hyperparameters: BaseHyperparametersV1,
        *args,
        **kwargs,
    ) -> None:
        super().__init__(*args, **kwargs)
        self.dataset = dataset
        self.tokenizer = tokenizer
        self.dataset_sample_class = dataset_sample_class
        self.hyperparameters = hyperparameters

    def __len__(self) -> int:
        return len(self.dataset)

    def __getitem__(self, idx: int) -> BaseDatasetSampleV1:
        return self.dataset_sample_class(
            self.dataset[idx],
            self.tokenizer,
            self.hyperparameters,
        ).get_sample()


class LightningDataModuleV1(LightningDataModule):
    def __init__(
        self,
        train_path_dataset: str,
        valid_path_dataset: str,
        hyperparameters: BaseHyperparametersV1,
        tokenizer: AutoTokenizer,
        base_train_dataset_class: BaseInitialDatasetV1 = None,
        base_valid_dataset_class: BaseInitialDatasetV1 = None,
        base_train_sample_class: BaseDatasetSampleV1 = None,
        base_valid_sample_class: BaseDatasetSampleV1 = None,
        debug_status: int = 0,
        device: str = "cpu",
    ) -> None:
        assert debug_status in [0, 1]
        assert base_train_dataset_class is not None
        assert base_valid_dataset_class is not None
        assert base_train_sample_class is not None
        assert base_valid_sample_class is not None

        super().__init__()

        self.train_path_dataset = train_path_dataset
        self.valid_path_dataset = valid_path_dataset

        self.hyperparameters = hyperparameters
        self.tokenizer = tokenizer

        self.base_train_dataset_class = base_train_dataset_class
        self.base_valid_dataset_class = base_valid_dataset_class
        self.base_train_sample_class = base_train_sample_class
        self.base_valid_sample_class = base_valid_sample_class

        self.debug_status = debug_status
        self.device = device

    def setup(self, stage: Optional[str] = None):
        train_dataset = self.base_train_dataset_class(
            input_dataset_path=self.train_path_dataset,
        )
        valid_dataset = self.base_valid_dataset_class(
            input_dataset_path=self.valid_path_dataset,
        )

        if self.debug_status == 1:
            train_dataset = train_dataset[:2]
            valid_dataset = valid_dataset[:2]

        self.train_dataset = PytorchDatasetV1(
            dataset=train_dataset,
            tokenizer=self.tokenizer,
            hyperparameters=self.hyperparameters,
            dataset_sample_class=self.base_train_sample_class,
        )

        self.valid_dataset = PytorchDatasetV1(
            dataset=valid_dataset,
            tokenizer=self.tokenizer,
            hyperparameters=self.hyperparameters,
            dataset_sample_class=self.base_valid_sample_class,
        )

    def train_dataloader(self) -> DataLoader:
        return DataLoader(
            self.train_dataset,  # type: ignore
            batch_size=self.hyperparameters.train_batch_size,
            shuffle=True,
            num_workers=os.cpu_count(),  # type: ignore
            collate_fn=self.train_collate_fn,
            pin_memory=True,
        )

    def val_dataloader(self) -> DataLoader:
        return DataLoader(
            self.valid_dataset,  # type: ignore
            batch_size=self.hyperparameters.valid_batch_size,
            shuffle=False,
            num_workers=os.cpu_count(),  # type: ignore
            collate_fn=self.valid_collate_fn,
        )

    def train_collate_fn(self, batch):
        # TODO: remove repetitions
        collated_batch = {}

        for key in batch[0].keys():
            batch_items = []
            max_len = 0
            for item in batch:
                item = item[key]
                if isinstance(item, list):
                    max_len = max(max_len, len(item))
                batch_items.append(item)
            if key in ["input_ids", "custom_labels"]:
                batch_items = self._padding(
                    batch_items,
                    self.tokenizer.pad_token_id,
                    max_len,
                )
                collated_batch[key] = torch.tensor(
                    batch_items,
                )
            elif key == "attention_mask":
                batch_items = self._padding(
                    batch_items,
                    0,
                    max_len,
                )
                collated_batch[key] = torch.tensor(
                    batch_items,
                )
            elif key in ["labels"]:
                batch_items = self._padding(
                    batch_items,
                    self.hyperparameters.pad_token_id,
                    max_len,
                )
                collated_batch[key] = torch.tensor(
                    batch_items,
                )
            else:
                collated_batch[key] = batch_items

        return collated_batch

    def valid_collate_fn(self, batch):
        return self.train_collate_fn(batch)

    def _padding(self, list_of_tokens: list, pad_id: int, max_len: int) -> list:
        return [
            tokens + [pad_id] * (max_len - len(tokens)) for tokens in list_of_tokens
        ]

    def _get_max_len(self, list_of_tokens: list) -> int:
        return max([len(tokens) for tokens in list_of_tokens])
