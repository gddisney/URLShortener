from flask import Flask, request, redirect
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from wtforms.validators import InputRequired
from keystore import KeyStore
import string
import random
import json

def HTMLindex(url,submit):
    rand = ''.join(random.choices(string.ascii_letters + string.digits, k=4))
    index = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>URL Shortner</title>
</head>
<body>
    <center>
    <form action="{ rand }" method="post">
    <h3>{ url }</h3>
    <h3>{ submit }</h3>
    </form>
    </center>
</body>
</html>"""
    return index

app = Flask(__name__)
Bootstrap(app)
app.config['SECRET_KEY'] = ''.join(random.choices(string.ascii_letters + string.digits, k=16))
keystore = KeyStore().read('url.db')

class URLForm(FlaskForm):
    url = StringField("URL",validators=[InputRequired()])
    submit = SubmitField('Submit')

@app.route('/')
def index():
    if request.method == 'GET':
        form = URLForm()
        _template = HTMLindex(form.url,form.submit)
        return _template

@app.route('/<rand>',methods = ['GET','POST'])
def short(rand): 
    if request.method == 'POST':
        path = request.path[1:]
        url = str(request.form.get('url'))
        print(url)
        KeyStore(id=path,url=url)
        KeyStore().write(id=path,database="url.db")
        return f"<html><body><iframe src={url} frameBorder='0' height=100% width=100%>"
    if request.method == 'GET':
        path = request.path[1:]
        data = KeyStore().get(id=path,database="url.db")
        url = data['url']
        return f"<html><body><iframe src={url} frameBorder='0' height=100% width=100%>"
    
app.run(host='0.0.0.0', port=8080)
