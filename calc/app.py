# Put your app in here.
from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)

@app.route('/')
def calcForm():
    html = """
        <form method=post>
            <input type=text name=function placeholder=Operation?></input>
            <input type=text name=num_one placeholder=Num1></input>
            <input type=text name=num_two placeholder=Num2></input>
            <button>Submit!</button>
        </form>
    """
    return html


@app.route('/', methods=["POST"])
def math():  #can i make this a variable url param? 
    a = request.form["num_one"]
    b = request.form["num_two"]
    function = request.form["function"]
    print(a , b)
    function = function.lower()
    if function == 'add':
        added = add(a, b)
        return f"<p>{a} + {b} = {added}"
    elif function == 'subtract':
        subtracted = sub(a, b)
        return f"{a} - {b} = {subtracted}"
    elif function == 'multiply':
        multiplied = mult(a, b)
        return f"{a} * {b} = {multiplied}"
    elif function == 'divide':
        divided = div(a, b)
        return f"{a} / {b} = {divided}"
    else:
        return """
        <h1>Not found, please enter correct information</h1>
        <p>add, subtract, multiple and divide must be fully typed out and spelled correctly</p>
        <p>Num1 and Num2 must be integers</p>
        """
