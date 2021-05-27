from pathlib import Path
class NumeraiAgent:
    """Class for helping out with the process of downloading data from numerai,
    training, computing metrics and submitting predictions """
    def __init__(
        self,
        path_data: Path,
        public_key: str,
        private_key: str,
        model_id: str,
    ):
        self.path_data = path_data
        self.public_key = public_key
        self.private_key = private_key
        self.model_id = model_id
        
    def save_last_data(self,):
        pass
    def fit_model(self,):
        pass
    def compute_metrics(self,):
        pass
    def submit_predictions(self,):
        pass