from numerai import NumeraiAgent
from config import Config

config = Config()

def main():
    numerai_agent = NumeraiAgent(
        path_data=config.path_data,
        private_key=config.private_key,
        public_key=config.public_key,
        model_id=config.model_id,
        url_tournament_data=config.url_tournament_data,
        url_training_data=config.url_training_data,
        model = config.model
        )
    #numerai_agent.save_last_data()
    numerai_agent.load_training_data()
    numerai_agent.load_tournament_data()
    numerai_agent.fit_model()


    print("Success")

if __name__=="__main__":
    main()