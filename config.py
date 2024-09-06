import os

from dotenv import load_dotenv

load_dotenv()

BS_KEY = os.getenv("BS_KEY")
DS_KEY = os.getenv("DS_KEY")
DB_CONFIG = {
    "apiKey": os.getenv("DB_KEY"),
    "authDomain": f"{os.getenv("PROJECTID")}.firebaseapp.com",
    "databaseURL": os.getenv("DB_URL"),
    "projectId": os.getenv("PROJECTID"),
    "storageBucket": f"{os.getenv("PROJECTID")}.appspot.com",
    "messagingSenderId": os.getenv("MSG_SNDR_ID"),
    "appId": os.getenv("APPID"),
    "measurementId": os.getenv("MSRMTID"),
}
