from flask import Flask,jsonify
import requests
import os
from dotenv import load_dotenv



load_dotenv()
bebida = os.getenv('BEBIDA')

app = Flask(__name__)

@app.route("/")
def home():
    return "<p>Hello, World!</p>"

@app.route("/bebidas")
def endpoint():

    print(bebida)

    data = requests.get("https://www.thecocktaildb.com/api/json/v1/1/search.php?s=margarita")
    data = data.json()
    print (data)

    _str = ""
    _list = []
    for drink in data["drinks"]:
        _list.append(
            {
                "name" :  drink["strDrink"]
            }
        )
        # _str = _str + "<p>" + drink["strDrink"] + "</p>"

    return jsonify(_list)

if __name__ == '__main__':
    # run app in debug mode on port 5000
    app.run(debug=True, port=8080)