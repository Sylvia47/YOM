import pyrebase

config = {
    'apiKey': "AIzaSyDSSbFTuyMaxlkSW3fRHUaP12Xm8-Wd0j0",
    'authDomain': "test1-388cc.firebaseapp.com",
    'databaseURL': "https://test1-388cc-default-rtdb.firebaseio.com",
    'projectId': "test1-388cc",
    'storageBucket': "test1-388cc.appspot.com",
    'messagingSenderId': "816583744157",
    'appId': "1:816583744157:web:2cec192ca15ff09a639274",
    'measurementId': "G-4X812QEH4X"
}

# initialize app with config
firebase = pyrebase.initialize_app(config)

# authenticate a user
auth = firebase.auth()
user = auth.sign_in_with_email_and_password("via1100302047@gmail.com", "songweijun1234")


db = firebase.database()
