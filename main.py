from flask import Flask, render_template, request, redirect
from .travelapi import *

app = Flask(__name__)
class Trip:
    def __init__(self):
        self.start = ""
        self.location = ""
        self.length = ""
        self.budget = ""
        self.stay = []

trip = Trip()


@app.route("/")
@app.route("/home", methods =["GET", "POST"])
def home():
    if request.method == "POST":
        trip.start = request.form.get("city_name_from")
        trip.location = request.form.get("city_name_to")
        trip.length = request.form.get("trip_length")
        trip.budget = request.form.get("budget_total")
        print("TRIP INFO", trip.start, trip.location, trip.length, trip.budget)
        return redirect('/planatrip')
    return render_template('home.html')


@app.route("/planatrip", methods =["GET", "POST"])
def transport():
    print("TRIP INFO", trip.start, trip.location, trip.length, trip.budget)
    return render_template('transport.html')


@app.route("/hotels", methods =["GET", "POST"])
def hotels():
    # return "hotels"+ str(hotels_lst)
    return render_template('hotel.html', hotels = str(hotels(100)))


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