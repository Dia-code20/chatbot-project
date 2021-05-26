from chatterbot import ChatBot
from flask import Flask, render_template, request
 
from chatterbot import ChatBot
import chatterbot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer

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


app = Flask(__name__)
app.static_folder = 'static'

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chatbot")
def bot():
    return render_template("chatbot.html")

@app.route("/get")
def get_bot_response():
    userText = request.args.get("msg")
    return str(chatbot.get_response(userText))

if __name__ == "__main__":
    app.run(debug=True)