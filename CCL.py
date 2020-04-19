from bs4 import BeautifulSoup
import requests
from pymongo import MongoClient
from flask import Flask, escape, request,render_template,flash, redirect,url_for,session,logging

app = Flask(__name__)
client = MongoClient("mongodb+srv://Rahul:Rahul@cluster0-lfcqx.mongodb.net/test?retryWrites=true&w=majority")
db = client.Miniproject
colfm = db.fifamen
colfw = db.fifawomen
coliodi = db.iccodi
colitest = db.icctest
colit20i = db.icct20i

colfm.delete_many({})
colfw.delete_many({})
coliodi.delete_many({})
colitest.delete_many({})
colit20i.delete_many({})
#--------------------------
c = 1
url = 'https://www.fifa.com/fifa-world-ranking/ranking-table/men/'

data = requests.get(url)
html = BeautifulSoup(data.text, 'html.parser')
x = html.find_all(class_='fi-t__nText')    
for i in x:
    title = i.text
    colfm.insert_one({'Rank':c,'Name':title})    
    c += 1
c = 1
url = 'https://www.fifa.com/fifa-world-ranking/ranking-table/women/'
data = requests.get(url)
html = BeautifulSoup(data.text, 'html.parser')
x = html.find_all(class_='fi-t__nText')    
for i in x:
    title = i.text
    colfw.insert_one({'Rank':c,'Name':title})    
    c += 1
c = 1
url = 'https://www.icc-cricket.com/rankings/mens/team-rankings/odi'
data = requests.get(url)
html = BeautifulSoup(data.text, 'html.parser')
x = html.find_all("td", {"class": "table-body__cell rankings-table__team u-text-left"})
    
for i in x:
    title = i.text
    coliodi.insert_one({'Rank':c,'Name':title})
    c += 1
c = 1
url = 'https://www.icc-cricket.com/rankings/mens/team-rankings/test'
data = requests.get(url)
html = BeautifulSoup(data.text, 'html.parser')
x = html.find_all("td", {"class": "table-body__cell rankings-table__team u-text-left"})
    
for i in x:
    title = i.text
    colitest.insert_one({'Rank':c,'Name':title})
    c += 1
c = 1
url = 'https://www.icc-cricket.com/rankings/mens/team-rankings/t20i'
data = requests.get(url)
html = BeautifulSoup(data.text, 'html.parser')
x = html.find_all("td", {"class": "table-body__cell rankings-table__team u-text-left"})
    
for i in x:
    title = i.text
    colit20i.insert_one({'Rank':c,'Name':title})
    c += 1
@app.route('/fifam')
def scrapefm():
	cursor = colfm.find()
	return render_template('fifa.html',posts=cursor)

@app.route('/fifaw')
def scrapefw():
    cursor = colfw.find()
    return render_template('fifa.html',posts=cursor)

@app.route('/iccodi')
def scrapeiccodi():
	cursor = coliodi.find()
	return render_template('fifa.html',posts=cursor)

@app.route('/icctest')
def scrapecicctest():
	cursor = colitest.find()
	return render_template('fifa.html',posts=cursor)

@app.route('/icct20i')
def scrapecicct20i():
	cursor = colit20i.find()
	return render_template('fifa.html',posts=cursor)

@app.route('/')
def default():
	return render_template('CCLhome.html')

if __name__ == "__main__":
    
    app.run(host='0.0.0.0')
