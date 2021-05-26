
from chatterbot import ChatBot
import chatterbot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer

#création d'une instance de chatbot

chatbot = ChatBot(
    'Chatty',
    storage_adapter= 'chatterbot.storage.SQLStorageAdapter',
    logic_adapter = [
        'chatterbot.logic.TimeLogicAdapter',
        'chatterbot.logic.BestMatch',
        {
            'import_path':'chatterbot.logic.BestMatch',
            'default_reponse':'Je suis désolé, mais je ne comprends pas, japprends encore',
            'maximum_similarity_threshold': 0.65
        }
    ],
    preprocessors=[
        'chatterbot.preprocessors.unescape_html'
    ],
    database_uri='sqlite:///database.sqlite3'
)

trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train("data/data.yml")
