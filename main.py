from flask import Flask, render_template, request, flash, redirect, url_for
from generator import Generate_password

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return render_template("index.html")

@app.route("/result", methods=["POST", "GET"])
def result():
    letters_value = False 
    digits_value = False
    special_characters_value = False
    
    output = request.form.to_dict()
    
    
    if 'letters_value' in output:
        letters_value = output["letters_value"]
    if 'digits_value' in output:
        digits_value = output["digits_value"]
    if 'special_characters_value' in output:
        special_characters_value = output["special_characters_value"]
    
    
    return render_template("index.html", 
                           letters_value = letters_value,
                           digits_value = digits_value,
                           special_characters_value = special_characters_value
                           )
    
    
if __name__ == '__main__':
    app.run(debug=True, port=5001)