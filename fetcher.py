import requests
import os.path
import urllib2
import sched, time
from time import gmtime, strftime
from apimodule import auctionhouse as ah

timeout = 60*5
apiKey = "YOUR-API-KEY-HERE"
s = sched.scheduler(time.time, time.sleep)

def fetchDataFile():
    currentTime = strftime("%H:%M:%S", gmtime())
    fileData = ah.getDumpFile(apiKey)
    if fileData != None:
        url = fileData["url"]
        lastModified = fileData["lastModified"]
        filename = "../auctions_"+str(lastModified)+".json"
        if not os.path.isfile(filename) :
            response = urllib2.urlopen(url)
            data = response.read()
            dataFile = open(filename, 'w+')
            dataFile.write(data)
            dataFile.close()
            print currentTime + ": creating file: ", filename
        else:
            print currentTime + ": File already exists"
    else:
        print currentTime + ": Failed to extract data from: ", jsonData

    s.enter(timeout, 1, fetchDataFile, ())

s.enter(timeout, 1, fetchDataFile, ())
s.run()
