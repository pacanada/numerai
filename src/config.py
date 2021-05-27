import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
parent_dir = dirname(__file__)
load_dotenv(dotenv_path)



class Config():
    def __init__(self):
        self.path_data = parent_dir + "data/"
        self.private_key = os.environ.get("NUM_PRIVATE_KEY")
        self.public_key = os.environ.get("NUM_PUBLIC_KEY")
        self.model_id = os.environ.get("MODEL_ID")
