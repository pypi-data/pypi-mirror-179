from typing import List


from dimweb_persona_bot.lighting_models.causal_lighting_models import (
    LightingCausalModelV1,
)
from dimweb_persona_bot.database_logger.logger import DatabaseLoggerV1

import wandb
import os


class LightingSeq2SeqModelV1(LightingCausalModelV1):
    def validation_step(
        self,
        batch,
        batch_idx: int,
    ):
        self.create_database_logger()

        predicts = self.model(
            input_ids=batch["input_ids"],
            attention_mask=batch["attention_mask"],
            labels=batch["labels"],
        )

        generated_tokens = self.model.generate(
            input_ids=batch["input_ids"],
            attention_mask=batch["attention_mask"],
            max_length=self.hyperparameters.max_response_length,
        )

        generated_tokens = self.tokenizer.batch_decode(
            generated_tokens,
            skip_special_tokens=True,
        )

        input_tokens = self.tokenizer.batch_decode(
            batch["input_ids"],
            skip_special_tokens=True,
        )

        decoded_labels = self.tokenizer.batch_decode(
            batch["custom_labels"],
            skip_special_tokens=True,
        )

        # compute text metrics
        text_metrics = self.text_evaluator.evaluate(
            generated_texts=generated_tokens,
            original_texts=decoded_labels,
        )

        # save texts for later analysis
        self.save_generation_predicts(
            prediction_ids=batch["sample_id"],
            decoded_labels=decoded_labels,
            generated_tokens=generated_tokens,
            input_tokens=input_tokens,
            persona=batch["persona"],
        )

        loss = predicts.loss

        self.log_dict(
            {
                "valid_loss": loss.detach().item(),
                "valid_blue_score": text_metrics["blue_score"],
                "valid_rougeL_score": text_metrics["rougeL_score"],
                "valid_chrf_score": text_metrics["chrf_score"],
            },
            on_step=True,
            on_epoch=True,
        )

    def save_generation_predicts(
        self,
        prediction_ids: List[str],
        persona: List[str],
        decoded_labels: List[str],
        generated_tokens: List[str],
        input_tokens: List[str],
    ):
        if not self.trainer.sanity_checking:
            run_id = wandb.run.id
            epoch = self.custom_current_epoch
            paired_texts = []
            for label, generated_text, input_token, prediction_id, persona_item in zip(
                decoded_labels,
                generated_tokens,
                input_tokens,
                prediction_ids,
                persona,
            ):
                true_texts = f"{input_token}@@@{label}"
                predicted_texts = f"{input_token}@@@{generated_text}"

                true_texts = true_texts.replace("\n", " ")
                predicted_texts = predicted_texts.replace("\n", " ")

                pair = "\n".join([true_texts, predicted_texts])
                paired_texts.append(pair)
                persona_item = " ".join(persona_item)

                # log to database
                if self.database_logger is not None:
                    self.database_logger.save_prediction(
                        actual_response=label,
                        context=input_token,
                        epoch=epoch,
                        model_prediction=generated_text,
                        persona=persona_item,
                        prediction_id=prediction_id,
                    )

            paired_texts = "\n\n".join(paired_texts)

            save_folder_path = f"{self.hyperparameters.predicted_texts_folder}/{run_id}"
            # create folder if not exists
            if not os.path.exists(save_folder_path):
                os.makedirs(save_folder_path)

            # append to file
            with open(f"{save_folder_path}/{epoch}.txt", "a") as f:
                f.write(paired_texts)

    def create_database_logger(self):
        if wandb.run is not None:
            self.database_logger = DatabaseLoggerV1(
                wandb_run_id=wandb.run.id,
                hyperparameters=self.hyperparameters,
                host=self.hyperparameters.host,
                port=self.hyperparameters.port,
            )
