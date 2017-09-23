from flask import Flask, request
from caesar import rotate_character

app = Flask(__name__)
app.config['DEBUG'] = True

form ="""
<!DOCTYPE html>
<html>
    <head>
        <style>
            form {
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }
            textarea {
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }
        </style>
    </head>
    <body>
        <form action="/" method='post'>
            <span>Rotate by:
            <input type="text" name="rot" /></span>
            <textarea name="text"></textarea>
            <input type="submit" />
        </form>
    </body>
</html>
"""

@app.route("/")
def index():
    return form

@app.route("/", methods=['post'])
def encrypt():
    rot = request.form["rot"]
    text = request.form["text"]
    sentence = ''
    for char in text:
        new_val = rotate_character(char, rot)
        sentence = sentence + new_val
    return "<h1>" + sentence + "</h1>"


app.run()