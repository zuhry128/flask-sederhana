from flask import Flask, render_template
from flask import request
import models as mods

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/', methods=['POST'])
def calculation():
        first = request.form.get("firstNumber", type=int)
        second = request.form.get("secondNumber", type=int)
        operation = request.form.get("aritmatika")

        if(operation == 'Penjumlahan'):
            result = mods.add(first, second)
        elif(operation == 'Pengurangan'):
            result = mods.substract(first, second)
        elif(operation == 'Perkalian'):
            result = mods.multiply(first, second)
        elif(operation == 'Pembagian'):
            result = mods.divide(first, second)
        else:
            result = "invalid choice"
        final = result
        return render_template('index.html', final=final)


if __name__ == "__main__":
    app.run(debug=True)

