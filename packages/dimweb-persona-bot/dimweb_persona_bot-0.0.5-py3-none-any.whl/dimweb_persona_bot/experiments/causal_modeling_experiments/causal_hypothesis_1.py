from dimweb_persona_bot.dataloaders.persona_chat_dataloaders import PersonaChatDatasetV1
from dimweb_persona_bot.dataloaders.causal_samplers.causal_samplers_hypothesis_1 import (
    H1CausalTrainPersonaSampleV1,
    H1CausalValidPersonaSampleV1,
    H1CausalTrainPersonaSampleV2,
    H1CausalValidPersonaSampleV2,
)
from dimweb_persona_bot.dataloaders.lighting import LightningDataModuleV1
from dimweb_persona_bot.hyperparameters.causal_modeling_hyperparameters import (
    H1PersonaChatHyperparametersV1,
)
from dimweb_persona_bot.lighting_models.causal_lighting_models import (
    LightingCausalModelV1,
)
from dimweb_persona_bot.hyperparameters.lighting import H1LightingHyperparametersV1
from dimweb_persona_bot.utils import (
    ExperimentArgumentParserV1,
    TrainArgumentsV1,
    WandbLoggerV1,
    WandbLoggerV2,
)

from transformers import AutoTokenizer, AutoModelForCausalLM


from pytorch_lightning import Trainer
from pytorch_lightning.callbacks import ModelCheckpoint


def h1_experiment_1():
    """
    модели у которых сдвиг токенов происходит внутри модели
    - gpt2
    - microsoft/DialoGPT-medium
    - RUCAIBox/mvp - не работает
    - roberta-base - не работает
    """
    parser = ExperimentArgumentParserV1()
    args: TrainArgumentsV1 = parser.args

    max_epochs = 4
    if args.debug_status == 1:
        max_epochs = 2

    lighting_hyperparameters = H1LightingHyperparametersV1(
        precision=16,
        # accumulate_grad_batches=3,
        max_epochs=max_epochs,
    ).__dict__

    hyperparameters = H1PersonaChatHyperparametersV1(
        train_batch_size=8 * 2,
        valid_batch_size=16,
        model_name="gpt2",
        predicted_texts_folder="/home/dimweb/Desktop/deeppavlov/persona_bot/predicted_texts",
        debug_status=args.debug_status,
    )

    tokenizer = AutoTokenizer.from_pretrained(hyperparameters.model_name)
    # так надо. https://github.com/huggingface/transformers/issues/2630#issuecomment-684512764
    tokenizer.pad_token_id = tokenizer.eos_token_id

    accelerator = "gpu"
    if args.debug_status == 1:
        accelerator = "cpu"

    device = "cuda" if accelerator == "gpu" else "cpu"

    notes = """
    дефолтная AutoModelForCausalLM.
    контекст=вся персона+последний вопрос от пользователя
    таргет=ответ от пользователя
    """
    wandb_logger = WandbLoggerV2(
        hyperparameters=hyperparameters,
        tags=["causal_modeling", "experiment_1"],
        notes=notes,
    )

    data_module = LightningDataModuleV1(
        train_path_dataset="./datasets/persona_chat/train.json",
        valid_path_dataset="./datasets/persona_chat/valid.json",
        hyperparameters=hyperparameters,
        tokenizer=tokenizer,
        base_train_dataset_class=PersonaChatDatasetV1,
        base_valid_dataset_class=PersonaChatDatasetV1,
        base_train_sample_class=H1CausalTrainPersonaSampleV1,
        base_valid_sample_class=H1CausalValidPersonaSampleV1,
        debug_status=args.debug_status,
        device=device,
    )

    base_model = AutoModelForCausalLM.from_pretrained(hyperparameters.model_name)

    model = LightingCausalModelV1(
        hyperparameters=hyperparameters,
        tokenizer=tokenizer,
        base_model=base_model,
    )

    checkpoint_callback = ModelCheckpoint(
        save_top_k=1,
        monitor="valid_loss_epoch",
        mode="min",
        filename=f"{hyperparameters.model_name}"
        + "-{epoch:02d}-{valid_loss_epoch:.2f}",
    )

    trainer = Trainer(
        accelerator=accelerator,
        logger=wandb_logger.logger,
        callbacks=[checkpoint_callback],
        **lighting_hyperparameters,
    )
    if args.debug_status != 1:
        trainer.validate(model=model, dataloaders=data_module)

    trainer.fit(
        model,
        datamodule=data_module,
    )


def h1_experiment_2():
    """
    модели у которых сдвиг токенов не происходит внутри модели
    небходимо самому сдвигать токены и подавать их в модель
    - facebook/blenderbot_small-90M
    - facebook/bart-base
    - google/bigbird-pegasus-large-arxiv
    - facebook/blenderbot-400M-distill
    - roberta-base - не работает
    - RUCAIBox/mvp - не работает
    """
    parser = ExperimentArgumentParserV1()
    args: TrainArgumentsV1 = parser.args

    max_epochs = 4
    if args.debug_status == 1:
        max_epochs = 1

    lighting_hyperparameters = H1LightingHyperparametersV1(
        precision=16,
        # accumulate_grad_batches=3,
        max_epochs=max_epochs,
    ).__dict__

    hyperparameters = H1PersonaChatHyperparametersV1(
        train_batch_size=8,
        valid_batch_size=16,
        model_name="RUCAIBox/mvp",
        predicted_texts_folder="/home/dimweb/Desktop/deeppavlov/persona_bot/predicted_texts",
    )

    tokenizer = AutoTokenizer.from_pretrained(hyperparameters.model_name)
    # так надо. https://github.com/huggingface/transformers/issues/2630#issuecomment-684512764
    tokenizer.pad_token_id = tokenizer.eos_token_id

    data_module = LightningDataModuleV1(
        train_path_dataset="./datasets/persona_chat/train.json",
        valid_path_dataset="./datasets/persona_chat/valid.json",
        hyperparameters=hyperparameters,
        tokenizer=tokenizer,
        base_train_dataset_class=PersonaChatDatasetV1,
        base_valid_dataset_class=PersonaChatDatasetV1,
        base_train_sample_class=H1CausalTrainPersonaSampleV2,
        base_valid_sample_class=H1CausalValidPersonaSampleV2,
        debug_status=args.debug_status,
    )

    base_model = AutoModelForCausalLM.from_pretrained(hyperparameters.model_name)

    model = LightingCausalModelV1(
        hyperparameters=hyperparameters,
        tokenizer=tokenizer,
        base_model=base_model,
    )

    checkpoint_callback = ModelCheckpoint(
        save_top_k=1,
        monitor="valid_loss_epoch",
        mode="min",
        filename=f"{hyperparameters.model_name}"
        + "-{epoch:02d}-{valid_loss_epoch:.2f}",
    )

    accelerator = "gpu"
    if args.debug_status == 1:
        accelerator = "cpu"

    wandb_logger = WandbLoggerV1(
        hyperparameters=hyperparameters,
    )

    trainer = Trainer(
        accelerator=accelerator,
        logger=wandb_logger.logger,
        callbacks=[checkpoint_callback],
        **lighting_hyperparameters,
    )
    if args.debug_status != 1:
        trainer.validate(model=model, dataloaders=data_module)

    trainer.fit(
        model,
        datamodule=data_module,
    )
