from pymongo import MongoClient
import webbrowser
import smtplib
from string import Template

print "Calories Tracker"

print "****************"

weight = raw_input("Please enter weight: ")

height = raw_input("Please enter height: ")


client = MongoClient()

db = client['db']

collection = db['Diamond1']

count = db.Diamond1.find().count()

calories = count*0.000398*45

bmi = float(weight)/float(height)*float(height)


print "Weight: %s  kgs"% weight
print "Height: %s metres"% height

print "Calories Burnt: %s calories"% calories

print "BMI: %s "% bmi





sender = 'bist.saurabh@yahoo.com'

receivers = ['smnaik@ncsu.edu', 'sanskruti.naik29@gmail.com']



message = """From: Sanskruti Naik<sanskruti.naik29@gmail.com>

To: Sanskruti Naik <to@todomain.com>

Subject: Calories Counter



Your Calorie status for the day 

"""
smtpObj = smtplib.SMTP('localhost',25)

smtpObj.sendmail(sender, receivers, message)
print "Successfully sent email"

html = '''<html>
<head>
<title> Calorie Count </title>
</head>

<body background="CalorieCutting.jpg" text="blue">
<center><i>
<hr><hr>
<font size="+4">Calorie Count</font>
<br><hr><hr></center>
<br>
<br>
 <head><title>Calorie Count</title></head>
 <body background="CalorieCutting.jpg", width = "100%", height = "75px", background-size = "50%">
 <p><br>
<br><br><h1 color = "blue" align = "center">Height: $code1</h1><br>
<br><br><h1 color = "blue" align = "center">Weight: $code2</h1><br>
<br><br><h1 color = "blue" align = "center">Calorie Count: $code3</h1><br>
<br><br><h1 color = "blue" align = "center">BMI: $code4</h1><br>
</p>
</body>
</html>
'''
s = Template(html).safe_substitute(code1=height, code2=weight, code3=calories, code4=bmi )
f = open("yourpage.html","w")
f.write(s)
f.close()

webbrowser.open("file:///home/vsnarvek/yourpage.html");

