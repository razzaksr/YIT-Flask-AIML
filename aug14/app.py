from flask import *
from forms import TransactionForm
app = Flask(__name__)
# csrf token
app.config["SECRET_KEY"] = "yitaimlflask"
# in memory
transactionHistory = []
@app.route("/")
def view(): return render_template("index.html",history = transactionHistory)
@app.route("/send", methods = ['GET','POST'])
def fund():
    transaction = TransactionForm()
    # if submit post happened
    if transaction.validate_on_submit():
        current = {
            transaction.fromAccount.name:transaction.fromAccount.data,
            transaction.toAccount.name:transaction.toAccount.data,
            transaction.ifsc.name:transaction.ifsc.data,
            transaction.amount.name:transaction.amount.data,
            transaction.type.name:transaction.type.data
        }
        transactionHistory.append(current)
        return redirect("/")
    return render_template('transfer.html',pay = transaction)

if __name__ == "__main__": app.run('localhost',8877)