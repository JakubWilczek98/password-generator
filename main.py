from flask import Flask, render_template, request, flash, redirect, url_for
from generator import Generate_password


app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return render_template("index.html")

@app.route("/result", methods=["POST", "GET"])
def result():
    
    output = request.form.to_dict()
    letters_value = False 
    digits_value = False
    special_characters_value = False
    pass_length = output["pass_length"]
    if pass_length == "":
        pass_length = 0
    else: 
        pass_length = round(float(output["pass_length"]))
    
    if 'letters_value' in output:
        letters_value = output["letters_value"]
    if 'digits_value' in output:
        digits_value = output["digits_value"]
    if 'special_characters_value' in output:
        special_characters_value = output["special_characters_value"]
    
    password = Generate_password(letters_value, digits_value, special_characters_value, pass_length)
    new_password = password.generate()
    
    
    return render_template("results.html", 
                           new_password = new_password
                           )


if __name__ == '__main__':
    app.run(debug=True, port=5001)