from flask import Flask, jsonify, render_template, request, redirect

app = Flask(__name__)

# in memory records
laptops = [
    {"model":"hp pavilion","ram":16,"ssd":512,"cost":56900.3},
    {"model":"lenevo thinkpad","ram":32,"ssd":1024,"cost":87000.56},
    {"model":"acer aspire","ram":32,"ssd":256,"cost":58900.78},
    {"model":"dell latitude","ram":8,"ssd":256,"cost":32999.6}
]

# routers

@app.route("/delete/<mod>")
def removeStock(mod):
    global laptops
    laptops = [each for each in laptops if each["model"]!=mod]
    return redirect("/stocks")

@app.route("/new", methods=["GET","POST"])
def addStock():
    if request.method == "GET": return render_template('new.html')
    else:
        newModel = request.form["model"]
        newRam = int(request.form["ram"])
        newSsd = int(request.form["ssd"])
        newCost = float(request.form["cost"])
        newLaptop = {"model":newModel,"ram":newRam,"ssd":newSsd,"cost":newCost}
        laptops.append(newLaptop)
        return redirect("/stocks")

@app.route("/stocks")
def viewStocks(): return render_template('main.html', stocks = laptops)

@app.route("/")
def viewJson(): return jsonify(laptops)

if __name__ == "__main__": app.run('localhost',4444)