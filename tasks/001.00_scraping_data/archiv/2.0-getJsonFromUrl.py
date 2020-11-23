import urllib, json

import time
import datetime as dt

import os
os.chdir( os.path.dirname(__file__) )

'''
targetUrl = "https://www.lotto.de/bin/6aus49_archiv?drawday="

url = "https://www.lotto.de/bin/6aus49_archiv?drawday=2017-03-11"
response = urllib.urlopen(url)
data = json.loads(response.read())
print data["2017-03-11"]["lotto"]["superzahl"]
print data["2017-03-11"]["lotto"]["gewinnzahlen"]
'''

'''
with open('filename') as f:
    lines = f.readlines()
'''
#COM: Get list of files
data_dir ="./url_captures/"
listFiles = os.listdir( data_dir )

#print listFiles #1956.urls.txt

target_dir ="./data_captures/"

container = { }

for idFile, nameFile in enumerate( listFiles ):

    keyYear = str( nameFile.split(".")[0] )
    print keyYear
    container[ keyYear ] = { }
    #COM: Get Lines in File
    with open( data_dir + nameFile) as f:
        lines = f.readlines()

    #print lines

    for idLine , urlLine in enumerate( lines ):

        ##COM: Get content of Url
        url = urlLine
        urlDate = url.split("=")[1].translate(None, '\n') #'https://www.lotto.de/bin/6aus49_archiv?drawday=1955-12-25\n'
        response = urllib.urlopen(url)
        data = json.loads(response.read())

        container[ keyYear ][ urlDate ] = { }

        dayWeek = dt.datetime.strptime(urlDate, '%Y-%m-%d').weekday()

        container[ keyYear ][ urlDate ]["superzahl"] = data[ urlDate ]["lotto"]["superzahl"]
        container[ keyYear ][ urlDate ]["zusatzzahl"] = data[ urlDate ]["lotto"]["zusatzzahl"]
        container[ keyYear ][ urlDate ]["gewinnzahlen"] = data[ urlDate ]["lotto"]["gewinnzahlen"]
        container[ keyYear ][ urlDate ]["dayWeek"] = dayWeek
        container[ keyYear ][ urlDate ]["date"] = urlDate
        container[ keyYear ][ urlDate ]["urlopen"] = urlLine.translate(None, '\n')

    with open(target_dir + keyYear + ".data.json", 'a') as outfile:
        json.dump( container[ keyYear ] , outfile)
