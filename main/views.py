from django.shortcuts import render
import firebase_admin
from firebase_admin import credentials
import pyrebase

config = {
    "apiKey": "AIzaSyDSSbFTuyMaxlkSW3fRHUaP12Xm8-Wd0j0",
    "authDomain": "test1-388cc.firebaseapp.com",
    "databaseURL": "https://test1-388cc-default-rtdb.firebaseio.com",
    "projectId": "test1-388cc",
    "storageBucket": "test1-388cc.appspot.com",
    "messagingSenderId": "816583744157",
    "appId": "1:816583744157:web:2cec192ca15ff09a639274",
    "measurementId": "G-4X812QEH4X"
}

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
database = firebase.database()

if not firebase_admin._apps:
    cred = credentials.Certificate('/Users/via1100302047/Documents/YagouOnlineMarket/worksapce/test1-388cc-firebase-adminsdk-80be7-84faee8d62.json')
    default_app = firebase_admin.initialize_app(cred)

def main(request):
    '''
    Render the main page
    '''
    product_name = database.child("data").child("name").get().val()
    product_price = database.child("data").child("price").get().val()
    product_category = database.child("data").child("category").get().val()

    context = {
        "product_name": product_name,
        "product_price":product_price,
        "product_category":product_category
    }
    return render(request, 'main/main.html', context)


def about(request):
    """
    Render the about page
    """
    return render(request, 'main/about.html')
