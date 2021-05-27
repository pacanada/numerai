import os
from pathlib import Path
from os.path import join, dirname
from dotenv import load_dotenv
from models import LinearRegressionCustom
from sklearn.linear_model import LinearRegression

dotenv_path = join(Path(__file__), '.env')
parent_dir = Path(__file__).parent.parent # one level up src, fix
dotenv_path = join(parent_dir, '.env')
load_dotenv(dotenv_path)



class Config():
    def __init__(self):
        self.path_data = parent_dir / "data"
        self.private_key = os.environ.get("NUM_PRIVATE_KEY")
        self.public_key = os.environ.get("NUM_PUBLIC_KEY")
        self.model_id = os.environ.get("MODEL_ID")
        self.url_training_data = "https://numerai-public-datasets.s3-us-west-2.amazonaws.com/latest_numerai_training_data.csv.xz"
        self.url_tournament_data = "https://numerai-public-datasets.s3-us-west-2.amazonaws.com/latest_numerai_tournament_data.csv.xz"
        self.model = LinearRegressionCustom()