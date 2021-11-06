from jina import Document , DocumentArray
import pandas as pd
import logging
from telegram import Update
from telegram.ext import Updater,  MessageHandler, Filters , CallbackContext

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

path = "D:\Python\Main_Project_Jina\Dictionary.csv"
df = pd.read_csv(path)
df = df.drop(columns=['POS' , 'Count'])
df = df.drop_duplicates().dropna()

Document(text = 'something')
docs = DocumentArray()
for ind in range(df.shape[0]):
    word = df.iloc[ind,0]
    defn = df.iloc[ind,1]
    doc = Document(text= word)
    doc.tags['Definition'] = defn
    docs.append(doc)


def String_Cutter(index):
    string = str(docs[index].tags)
    string= string[17 : ]
    string = string[ :-3]
    return string

def Semantic_Search(string):
    Search = string[0].upper() + string[1:].lower()
    for index in range(0,175761):
        if Search == docs[index].text:
            return String_Cutter(index)
    return "Word not found"

def Reply(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(Semantic_Search(update.message.text))


def main() -> None:
    updater = Updater("1431795622:AAHocJ5AKOzBBQ58cFfZZVvaSvua0qsmZHk")
    dispatcher = updater.dispatcher

    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, Reply))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()