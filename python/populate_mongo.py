import time
from random import randint
from datetime import datetime
from pymongo import MongoClient

def populate():
    client = MongoClient()
    db = client.fer
    faces = db.faces

    fields = ['Id', 'Age', 'Gender', 'Emotion', 'DateTime']
    emotions = ["Anger", "Contempt", "Disgust", "Fear", "Happiness", "Neutral", "Sadness", "Surprise"]
    genders = ["male", "female"]

    i = 0
    while True:
        id = "random" + str(i)
        age = randint(10, 80)
        gender = genders[randint(0,1)]
        emotion = emotions[randint(0,7)]
        dt = datetime.now()
        #dt = datetime.now().isoformat(timespec="seconds")

        face = {
            "Id": id,
            "Age": age,
            "Gender": gender,
            "Emotion": emotion,
            "DateTime": dt
        }

        faces.insert_one(face)
        time.sleep(0.3)
        i += 1

populate()