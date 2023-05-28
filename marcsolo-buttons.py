#buttons and such
# made this a separate file to cross-examine everything
# definitely errors somewhere, it's like 3 am
from flask import Flask, redirect, request, render_template

app = Flask(__name__, static_folder = 'assests')

#routes
@app.route("/")
def home():
    return redirect("/home")

@app.route("/home")
def homeTemp():
    return render_template("home.html")

@app.route("/startTrip")
def startTripTemp():
    return render_template("startTrip.html")

@app.route("/transport")
def transportTemp():
    render_template("transport.html")

@app.route("/hotel")
def hotelTemp():
    render_template("hotel.html")

@app.route("/food")
def foodTemp():
    render_template("food.html")

@app.route("/summary")
def summaryTemp():
    render_template("summary.html")

#buttons on home
@app.route("/home", methods = ['POST', 'GET'])
def buttonStartPlanning():
    if request.method == "POST":
        travelTo = request.form["Travel-To"]
        travelFrom = request.form["Travel-From"]
        tripLength = request.form["Trip-Length"]
        budget = request.form["Desired-Budget"]
        #ARRAY NAME userInput generic - MUST EDIT
        userInput.append(travelTo)
        userInput.append(travelFrom)
        userInput.append(tripLength)
        userInput.append(budget)
    return AITransport()

#buttons on transport
#starting off the display
@app.route("/transport")
def AITransport():
    #ARRAY NAME AITransportArr generic - MUST EDIT
    #Map???
    if (AITransportArr.len() > 0):
        currShowTransport = 0
        return render_template("transport.html", AI-Transport-Response=AITransportArr[0])
    else:
        currShowTransport = 0
        return transportTemp()

@app.route("/transport", methods = ['POST', 'GET'])
def buttonPrevTransport():
    #currShowTransport generic - EDIT
    if request.method == "POST":
        if (currShowTransport > 0):
            currShowTransport -= 1
            return render_template("transport.html", AI-Transport-Response=AITransportArr[currShowTransport])
        else:
            return AITransport()

@app.route("/transport", methods = ['POST', 'GET'])
def buttonNextTransport():
    if request.method == "POST":
        if ((currShowTransport < AITransportArr.len()):
            currShowTransport += 1
            return render_template("transport.html", AI-Transport-Response=AITransportArr[currShowTransport])
        else:
            return render_template("transport.html", AITransportArr[currShowTransport])

@app.route("/transport", methods = ['POST', 'GET'])
def buttonSelectTransport():
    if request.method == "POST":
        if (transportSelected == false):
            #summaryArr generic - EDIT
            summaryArr.insert(0, AITransportArr[currShowTransport])
            #transportSelected intially false
            transportSelected = true
        return render_template("transport.html", AI-Transport-Response=(AITransportArr[currShowTransport]+"\nSELECTED!!"))
    else:
        return render_template("transport.html", AI-Transport-Response=(AITransportArr[currShowTransport]+"\nALREADY SELECTED A TRAVEL METHOD!!"))

@app.route("/transport", methods = ['POST', 'GET'])
def buttonHotelPlan():
    if request.method == "POST":
        return AIHotel()

#buttons on hotel
@app.route("/hotel")
def AIHotel():
    #ARRAY NAME AITransportArr generic - MUST EDIT
    #Map???
    if (AIHotelArr.len() > 0):
        currShowHotel = 0
        return render_template("hotel.html", AI-Hotel-Response=AIHotelArr[0])
    else:
        currShowHotel = 0
        return hotelTemp()

@app.route("/hotel", methods = ['POST', 'GET'])
def buttonPrevHotel():
    #currShowTransport generic - EDIT
    if request.method == "POST":
        if (currShowHotel > 0):
            currShowHotel -= 1
            return render_template("hotel.html", AI-Hotel-Response=AIHotelArr[currShowHotel])
        else:
            return AIHotel()

@app.route("/hotel", methods = ['POST', 'GET'])
def buttonNextHotel():
    if request.method == "POST":
        if ((currShowHotel < AIHotelArr.len()):
            currShowHotel += 1
            return render_template("hotel.html", AI-Hotel-Response=AIHotelArr[currShowHotel])
        else:
            return render_template("hotel.html", AIHotelArr[currShowHotel])

@app.route("/hotel", methods = ['POST', 'GET'])
def buttonSelectHotel():
    if request.method == "POST":
        if (hotelSelected == false):
            hotelSelected = true
            #summaryArr generic - EDIT
            summaryArr.insert(1, AIHotelArr[currShowHotel])
        return render_template("hotel.html", AI-Hotel-Response=(AIHotelArr[currShowHotel]+"\nSELECTED!!"))
    else:
        return render_template("hotel.html", AI-Hotel-Response=(AIHotelArr[currShowHotel]+"\nALREADY SELECTED A HOTEL TO STAY AT!!"))

@app.route("/hotel", methods = ['POST', 'GET'])
def buttonFoodPlan():
    if request.method == "POST":
        return AIFood()
    
#buttons on food
@app.route("/food")
def AIFood():
    #ARRAY NAME AITransportArr generic - MUST EDIT
    #Map???
    if (AIFoodArr.len() > 0):
        currShowFood = 0
        return render_template("food.html", AI-Food-Response=AIFoodArr[0])
    else:
        currShowFood = 0
        return foodTemp()

@app.route("/food", methods = ['POST', 'GET'])
def buttonPrevFood():
    #currShowTransport generic - EDIT
    if request.method == "POST":
        if (currShowFood > 0):
            currShowFood -= 1
            return render_template("food.html", AI-Food-Response=AIFoodArr[currShowFood])
        else:
            return AIFood()

@app.route("/food", methods = ['POST', 'GET'])
def buttonNextFood():
    if request.method == "POST":
        if ((currShowFood < AIFoodArr.len()):
            currShowFood += 1
            return render_template("food.html", AI-Food-Response=AIFoodArr[currShowFood])
        else:
            return render_template("food.html", AIFoodArr[currShowFood])

@app.route("/food", methods = ['POST', 'GET'])
def buttonSelectTransport():
    if request.method == "POST":
        #summaryArr generic - EDIT
        summaryArr.append([AIFoodArr[currShowFood]])
    return render_template("food.html", AI-Food-Response=(AIFoodArr[currShowFood]+"\nSELECTED!!"))

@app.route("/transport", methods = ['POST', 'GET'])
def buttonSummary():
    if request.method == "POST":
        return AISummary()
    
#buttons on summary
@app.route("/summary")
def AISummary():
    transportPrint = "Travel Method: " + summaryArr[0], " (" + transportMath + "%)\n"
    hotelPrint = "Hotel Location: " + summaryArr[1], " (" + hotelMath + "%)\n"
    foodPrint = "Food Spots: \n"
    sumArrPOS = 2
    while (sumArrPOS < summaryArr.len()):
        foodPrint += ("\t" + summaryArr[2] + " (" + math + "\n")
        sumArrPOS += 1
    completePrint = transportPrint + hotelPrint + foodPrint
    return render_template("summary.html", AI-Summary-Response=completePrint)

@app.route("/summary", methods = ['POST','GET'])
def buttonEditTransport():
    if method == "POST":
        summaryArr.pop(0)
        transportSelected = false
        return AITransport()
        
@app.route("/summary", methods = ['POST','GET'])
def buttonEditHotel():
    if method == "POST":
        summaryArr.pop(1)
        hotelSelected = false
        return AIHotel()

@app.route("/summary", methods = ['POST','GET'])
def buttonEditFood():
    if method == "POST":
        keepTransport = summaryArr[0]
        keepHotel = summaryArr[1]
        summaryArr.clear()
        summaryArr.append(keepTransport)
        summaryArr.append(keepHotel)
        return AIFood()

@app.route("/summary", methods = ['POST','GET'])
def buttonSaveTrip():
    if method == "POST":
        return redirect("/startTrip")
