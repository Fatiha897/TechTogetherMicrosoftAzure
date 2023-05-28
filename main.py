from flask import Flask, render_template, request
from .travelapi import *

app = Flask(__name__)
class Trip:
    def __init__(self):
        self.name = ""
        self.location = ""
        self.budget = ""
        self.stay = ""

trip = Trip()


@app.route("/")
@app.route("/home", methods =["GET", "POST"])
def home():
    if request.method == "POST":
        name = request.form.get("NamE")
        trip.name = name
        print("HERE", trip.name)
    return render_template('home.html')


@app.route("/planatrip", methods =["GET", "POST"])
def transport():
    # return "hotels"+ str(hotels_lst)
    return render_template('transport.html')


@app.route("/hotels", methods =["GET", "POST"])
def hotels():
    # return "hotels"+ str(hotels_lst)
    return render_template('hotel.html') # hotels = str(foodnearby(100)))


@app.route("/food", methods =["GET", "POST"])
def food():
    # return "hotels"+ str(hotels_lst)
    return render_template('food.html')


@app.route("/summary", methods =["GET", "POST"])
def summary():
    # return "hotels"+ str(hotels_lst)
    return render_template('summary.html')


@app.route("/startTrip", methods =["GET", "POST"])
def end():
    # return "hotels"+ str(hotels_lst)
    return render_template('startTrip.html')