import firebase
from firebase import Firebase
from firebase import firebase as f
from stdiomask import getpass 
import sys

config = {
  "apiKey": "AIzaSyBlLq7LECUeC0Et_UZi3KMIYzdTYyeSbNI",
  "authDomain": "information-agreegator.firebaseapp.com",
  "projectId": "information-agreegator",
  "storageBucket": "information-agreegator.appspot.com",
  "messagingSenderId": "149901859275",
  "databaseURL": "https://information-agreegator-default-rtdb.firebaseio.com/",
  "appId": "1:149901859275:web:69de34d55096a98f09be4e",
  "serviceAccount": (r"\Downloads\info-agree-firebase-adminsdk.json")
}

firebase = Firebase(config)
auth = firebase.auth()

#enter the details
name = input("Enter your name : \n")
email = input("Please Enter Your Email Address : \n").strip()
password = getpass("Please Enter Your Password : \n",mask="*")

#create user
auth.create_user_with_email_and_password(email, password)

#user sign in 
user = auth.sign_in_with_email_and_password(email, password)
print("login successful")

#verification mail
auth.send_email_verification(user['idToken'])
print("verification mail send")

#database entry
data={name:email}
fire = f.FirebaseApplication("https://information-agreegator-default-rtdb.firebaseio.com/",None)
result = fire.post('/information-agreegator-default-rtdb/',data)
print(result)
