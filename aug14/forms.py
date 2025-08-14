from flask_wtf import FlaskForm
from wtforms import *
from wtforms.validators import *

class TransactionForm(FlaskForm):
    fromAccount = StringField("Enter the Sender Account Number ", validators=[
        DataRequired(message="Sender account is mandate"),
        Regexp(r"^[0-9]{12}$", message="Invalid sender account")
    ])
    toAccount = StringField("Enter the receiver account number ",validators=[
        DataRequired(message="Receiver account is mandate"),
        Regexp(r"^[0-9]{12}$", message="Invalid receiver account")
    ])
    confirmAccount = PasswordField("Confirm receiver account number",validators=[
        DataRequired(message="Confiming receiver account is mandate"),
        Regexp(r"^[0-9]{12}$", message="Invalid receiver account"),
        EqualTo("toAccount",message="Receiver and confirm shoud be same")
    ])
    ifsc = StringField("Enter the IFSC Code", validators=[
        DataRequired(message="ifsc code required"),
        Regexp(r"^[A-Z]{4}[0-9]{5}$", message="invalid ifscode")
    ])
    amount = StringField("Enter the amount to transfer",validators=[
        DataRequired(message="Amount is mandate"),
        Regexp(r"^[0-9]{1,}$", message="Invalid amount")
    ])
    type = SelectField("Select Type of Transaction ",choices=[
        # (actual,presentable)
        ('neft','NEFT'),
        ('rtgs',"RTGS"),
        ('imps',"IMPS")
    ])
    submit = SubmitField("Transfer")