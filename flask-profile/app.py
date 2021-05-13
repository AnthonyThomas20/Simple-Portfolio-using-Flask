import gspread
from flask import Flask, render_template

gc = gspread.service_account(filename='flask-profile.json')
sh = gc.open('flask-profile')

shProfile = sh.get_worksheet(0)
shContacts = sh.get_worksheet(1)
shContacts.append_row('John Doe', 'johndoe@gmail.com', 'Hello')

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')
