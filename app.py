from flask import Flask, request, jsonify, render_template, redirect, url_for
from dotenv import load_dotenv 

#crear instancia
app =  Flask(__name__)

#endpoit hola mundo
@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
