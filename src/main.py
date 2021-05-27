from numerai import NumeraiAgent
from config import Config

config = Config()

def main():
    numerai_agent = NumeraiAgent(
        path_data=config.path_data,
        private_key=config.private_key,
        public_key=config.public_key,
        model_id=config.model_id
        )


    print("Success")

if __name__=="__main__":
    main()