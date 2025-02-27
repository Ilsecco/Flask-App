from flask import Flask
import random
import os

app = Flask(__name__)

@app.route("/")
def index():
    return "<h1>hello world</h1>"



@app.route("/password")
def password():
    a = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!#$%&'()*+,-./:;<=>?@[c]^_`{|}~"
    t = ""
    for i in range(50):
        t += random.choice(a)

    return f"<h1>{t}</h1>"



@app.route("/moneta")
def moneta():
    
    y = random.randint(0, 1)
    if y == 0:
        g = "A"
    elif y == 1:
        g ="B"

    if g == "A":
        return "<h1>è uscito testa</h1>"
    elif g == "B":
        return "<h1>è uscito croce</h1>"
    




@app.route("/foto")
def foto():
    s=os.listdir("images")
    h=random.choice(s)
    t = f'<img src="images/{h}" alt="Immagine Random">'
    return t     

app.run(debug=True)
