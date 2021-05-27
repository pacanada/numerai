from pathlib import Path
import pandas as pd

class NumeraiAgent:
    """Class for helping out with the process of downloading data from numerai,
    training, computing metrics and submitting predictions """
    def __init__(
        self,
        path_data: Path,
        public_key: str,
        private_key: str,
        model_id: str,
        url_training_data: str,
        url_tournament_data: str,
        model,
    ):
        self.path_data = path_data
        self.public_key = public_key
        self.private_key = private_key
        self.model_id = model_id
        self.url_training_data = url_training_data
        self.url_tournament_data = url_tournament_data
        self.model = model

    def save_last_data(self,):
        try:
            print("Downloading training data")
            training_data = pd.read_csv(self.url_training_data)
            training_data.to_feather(self.path_data / "training.feather")
            print(f"Training data saved in {self.path_data} as training.feather")
        except Exception as e:
            print(e)

        try:
            print("Downloading tournament data")
            training_data = pd.read_csv(self.url_training_data)
            training_data.to_feather(self.path_data / "tournament.feather")
            print(f"Tournament data saved in {self.path_data} as tournament.feather")
        except Exception as e:
            print(e)
    def load_training_data(self,):
        self.df_training = pd.read_feather(self.path_data / "training.feather")
    def load_tournament_data(self,):
        self.df_tournament = pd.read_feather(self.path_data / "tournament.feather")   
    def fit_model(self):
        self.feature_columns = [c for c in self.df_training.columns if c.startswith("feature")]
        self.target_column = "target"
        self.fitted_model = self.model.fit(
            X=self.df_training[self.feature_columns],
            y=self.df_training[self.target_column])
        
    def compute_metrics(self,):
        pass
    def submit_predictions(self,):
        pass