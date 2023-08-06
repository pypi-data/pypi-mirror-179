from dimweb_persona_bot.database_logger.models import ModelMetricsV1, ModelPredictionV1
from dimweb_persona_bot.hyperparameters.causal_modeling_hyperparameters import (
    BaseHyperparametersV1,
)
import peewee as pw


class DatabaseLoggerV1:
    def __init__(
        self,
        wandb_run_id: str,
        hyperparameters: BaseHyperparametersV1,
        host: str,
        port: int,
    ):
        self.host = host
        self.port = port

        self.__test_connection()
        self.hyperparameters = hyperparameters
        self.model_name = hyperparameters.model_name
        self.model_architecture = hyperparameters.model_architecture
        self.wandb_run_id = wandb_run_id

    def __test_connection(self):
        db = pw.PostgresqlDatabase(
            "nlp_database",
            user="postgres",
            password="postgres",
            host=self.host,
            port=self.port,
            autorollback=True,
        )
        db.connect()
        db.close()

    def save_metrics(
        self,
        epoch: int,
        valid_loss_epoch: float,
        blue_score_epoch: float,
        rougel_score_epoch: float,
        charf_score_epoch: float,
    ):
        ModelMetricsV1.create(
            epoch=epoch,
            model_name=self.model_name,
            model_architecture=self.model_architecture,
            wandb_run_id=self.wandb_run_id,
            valid_loss_epoch=valid_loss_epoch,
            blue_score_epoch=blue_score_epoch,
            rougel_score_epoch=rougel_score_epoch,
            charf_score_epoch=charf_score_epoch,
            debug_status=self.hyperparameters.debug_status,
        )

    def save_prediction(
        self,
        prediction_id: str,
        epoch: int,
        persona: str,
        context: str,
        model_prediction: str,
        actual_response: str,
    ):
        ModelPredictionV1.create(
            prediction_id=prediction_id,
            epoch=epoch,
            model_name=self.model_name,
            model_architecture=self.model_architecture,
            wandb_run_id=self.wandb_run_id,
            persona=persona,
            context=context,
            model_prediction=model_prediction,
            actual_response=actual_response,
            debug_status=self.hyperparameters.debug_status,
        )


class DatabaseAnalaizerV1:
    def __init__(
        self,
        host: str,
        port: int,
    ):
        self.host = host
        self.port = port
        self.db = None
        self.__connect_database()

    def __connect_database(self):
        db = pw.PostgresqlDatabase(
            "nlp_database",
            user="postgres",
            password="postgres",
            host=self.host,
            port=self.port,
            autorollback=True,
        )
        db.connect()
        self.db = db

    def execute_sql(self, query: str):
        cursor = self.db.execute_sql(query)
        return cursor.fetchall()
