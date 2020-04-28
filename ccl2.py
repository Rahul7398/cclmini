from bs4 import BeautifulSoup
import requests
from pymongo import MongoClient
from flask import Flask, escape, request,render_template,flash, redirect,url_for,session,logging

app = Flask(__name__)
client = MongoClient("mongodb+srv://Rahul:Rahul@cluster0-lfcqx.mongodb.net/test?retryWrites=true&w=majority")
db = client.ccldatabase
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
    if(c==15):
        break#1
    c += 1
c = 1
url = 'https://www.fifa.com/fifa-world-ranking/ranking-table/women/'
data = requests.get(url)
html = BeautifulSoup(data.text, 'html.parser')
x = html.find_all(class_='fi-t__nText')    
for i in x:
    title = i.text
    colfw.insert_one({'Rank':c,'Name':title})
    if(c == 15):
        break;
    c += 1
c = 1
url = 'https://www.icc-cricket.com/rankings/mens/team-rankings/odi'
data = requests.get(url)
html = BeautifulSoup(data.text, 'html.parser')
#x = html.find_all("td", {"class": "table-body__cell rankings-table__team u-text-left"})
x1 = html.find("td", {"class": "rankings-block__banner--team-name"})
y = x1.find("span",{"class":"u-hide-phablet"})
c = 1
coliodi.insert_one({'Rank':c,'Name':y.text})
c++
x = html.find_all("td", {"class": "table-body__cell rankings-table__team"})
    
for i in x:
    j = i.find("span",{"class":"u-hide-phablet"})
    title = j.text
    coliodi.insert_one({'Rank':c,'Name':title})
    if(c==15):
        break #3
    c += 1
c = 1
url = 'https://www.icc-cricket.com/rankings/mens/team-rankings/test'
data = requests.get(url)
html = BeautifulSoup(data.text, 'html.parser')

#x = html.find_all("td", {"class": "table-body__cell rankings-table__team u-text-left"})
x1 = html.find("td", {"class": "rankings-block__banner--team-name"})
y = x1.find("span",{"class":"u-hide-phablet"})
c = 1
coliodi.insert_one({'Rank':c,'Name':y.text})
c++
x = html.find_all("td", {"class": "table-body__cell rankings-table__team"})
    
for i in x:
    j = i.find("span",{"class":"u-hide-phablet"})
    title = j.text
    colitest.insert_one({'Rank':c,'Name':title})
    if(c==15):
        break #4
    c += 1
c = 1
url = 'https://www.icc-cricket.com/rankings/mens/team-rankings/t20i'
data = requests.get(url)
html = BeautifulSoup(data.text, 'html.parser')
#x = html.find_all("td", {"class": "table-body__cell rankings-table__team u-text-left"})
x1 = html.find("td", {"class": "rankings-block__banner--team-name"})
y = x1.find("span",{"class":"u-hide-phablet"})
c = 1
coliodi.insert_one({'Rank':c,'Name':y.text})
c++
x = html.find_all("td", {"class": "table-body__cell rankings-table__team"})
    
for i in x:
    j = i.find("span",{"class":"u-hide-phablet"})
    title = j.text
    colit20i.insert_one({'Rank':c,'Name':title})
    if(c==15):
        break #5
    c += 1
@app.route('/fifam')
def scrapefm():
    cursor = colfm.find()
    l=[]
    x = 0
    for i in cursor:
        if x%2==0:
            l.append(i)
        x +=1
    return render_template('fifa.html',posts=l)

@app.route('/fifaw')
def scrapefw():
    cursor = colfw.find()
    l=[]
    x = 0
    for i in cursor:
        if x%2 ==0:
            l.append(i)
        x +=1
    return render_template('fifa.html',posts=l)

@app.route('/iccodi')
def scrapeiccodi():
    cursor = coliodi.find()
    l=[]
    x = 0
    for i in cursor:
        if x%2 ==0:
            l.append(i)
        x +=1
    return render_template('fifa.html',posts=l)

@app.route('/icctest')
def scrapecicctest():
    cursor = colitest.find()
    l=[]
    x = 0
    for i in cursor:
        if x%2 ==0:
            l.append(i)
        x +=1
    return render_template('fifa.html',posts=l)

@app.route('/icct20i')
def scrapecicct20i():
    cursor = colit20i.find()
    l=[]
    x = 0
    for i in cursor:
        if x%2 ==0:
            l.append(i)
        x +=1
    return render_template('fifa.html',posts=l)

@app.route('/')
def default():
	return render_template('CCLhome.html')

if __name__ == "__main__":
    
    app.run()
