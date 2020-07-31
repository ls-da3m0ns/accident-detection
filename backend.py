# -*- coding: utf-8 -*-


import pyrebase
global config, firebase, storage

config = config = {
  "apiKey": "AIzaSyAIUVNFg8SoM5nc_0BX2Pw4uL5nbIFyN_E",
  "authDomain": "hackjaipur-44104.firebaseapp.com",
  "databaseURL": "https://hackjaipur-44104.firebaseio.com/",
  "storageBucket": "hackjaipur-44104.appspot.com",
  "serviceAccount": "firebase.json?token=ALA5BOGXIIV7GM7MR2FMAGS664R4U"
}

firebase = pyrebase.initialize_app(config)
storage = firebase.storage()
def videoFromFirebase(video):
    path_on_cloud = "out_video/"+video
    path_local = "./out_video/"+video
    storage.child(path_on_cloud).download(path_local)
    print("Video : " + video + " successfully downloaded from firebase!")

def imgFromFirebase(image):
    path_on_cloud = "out_images/"+image
    path_local = "./out_images/"+image
    storage.child(path_on_cloud).download(path_local)
    print("Image : " + image+ " successfully downloaded from firebase!")

import sqlite3 

def download_db():
  storage.child("database/accidents.db").download("database/accidents.db")

def veiw():
    download_db()
    conn=sqlite3.connect("database/accidents.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM accident")
    rows=cur.fetchall()
    conn.close()
    return rows

ou = veiw()[-2:]
lis = list()
for i in range(2):
  imgFromFirebase(str(ou[i][-1])+'.jpg')
  videoFromFirebase(str(ou[i][-1])+'.mp4')

new = ou[-3:]



