from flask import Flask, render_template, redirect, request, session
import random
app = Flask(__name__)
app.secret_key = "whatEverYouWantToCallIt"

@app.route('/')
def index():
	if "gold" not in session:
		session["gold"] = 0 
	if "result" not in session:
		session["result"] = " "	
	return render_template('index.html')

@app.route('/process_money', methods=["POST"])
def process_money():
	if request.form["building"] == "farm": 
		addgold = random.randrange(10,20)
		session["gold"] += addgold 
		session["result"] += "You earned" + str(session["gold"]) + " from the farm"
	if request.form["building"] == "cave":
		addgold = random.randrange(5,10)
		session["gold"] += addgold
		session["result"] += str("You earned" + str(session["gold"]) + " from the cave")
	if request.form["building"] == "house":
		addgold = random.randrange(2,5)
		session["gold"] += addgold
		session["result"] += str("You earned" + str(session["gold"]) + " from the house")
	if request.form["building"] == "casino":
		addgold = random.randrange(-50,50)
		session["gold"] += addgold
		session["result"] += str("You earned" + str(session["gold"]) + " from the casino")
	return redirect('/')

app.run(debug=True)