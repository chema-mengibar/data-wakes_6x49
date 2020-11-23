import os
import sys

DIR_TASK = os.path.basename(os.getcwd())
DIR_LIB = os.path.abspath(os.path.join(os.path.dirname(__file__),"../"))
DIR_TASK = os.path.dirname(os.path.abspath(__file__))

import json, csv, time, string, itertools, copy, yaml
import numpy as np
import pandas as pd
import datetime as dt

from datetime import date

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

os.chdir( os.path.dirname(__file__))

CONFIG_FILE_NAME = '001.00_config'
config = yaml.load( stream = file( DIR_TASK + '\\' + CONFIG_FILE_NAME + '.yml', 'r'), Loader=yaml.FullLoader)
yaml.dump( config, file( DIR_TASK + '\\config.yml', 'w') )

sys.path.append( DIR_LIB )

from lib.router import Router
router = Router( )
print '>> Walk, Don`t Run'

# --------------------------------------------------------------------------



browser = webdriver.Chrome(executable_path=r"..\\lib\\selenium\\chromedriver_1.exe")

url = 'https://www.lotto.de/de/ergebnisse/lotto-6aus49/lottozahlen.html'
targetUrl = "https://www.lotto.de/bin/6aus49_archiv?drawday="

browser.get(url)
time.sleep(1)


#STEP: output-file

outputPath =  router.getRoute( config['target']['route'] ) + config['target']['dir']

#com: create output folder
if not os.path.exists( outputPath ):
  os.makedirs( outputPath )


#STEP: Selenium

#com: Close cookies modal
time.sleep(1)
elem = browser.find_element_by_id('ppms_cm_agree-to-all')
elem.click()
time.sleep(0.2)

# elem = browser.find_elements(By.XPATH, '//select') # selectedYear, daySelect
itemSelectYears = browser.find_element_by_id('selectedYear')
listYears = itemSelectYears.find_elements_by_tag_name('option')


def getSeletedYear( pos ):
  return listYears[ pos ].get_attribute('value')

def selectYear( pos ):
  listYears[ pos ].click( )

def getDaysOfSelectedYear():
  targetUrl = "https://www.lotto.de/api/stats/entities.lotto/draws/"
  listUrls = ''
  yearDaysOptions = browser.find_element_by_id('daySelect').find_elements_by_tag_name('option')
  for i, opt in enumerate(yearDaysOptions):
    lotoDate =  opt.get_attribute('value') + '__00:00:00'
    lotoDateDt = dt.datetime.strptime(lotoDate, '%Y-%m-%d__%H:%M:%S')
     #help: newLotoDate = dt.datetime.strftime( lotoDateDt, '%Y-%m-%d')
    #com: miliseconds timestamp
    timestamp = int(round(time.mktime(lotoDateDt.timetuple()))) * 1000 
    listUrls += targetUrl + str(timestamp) + '\n'
  return listUrls
  

# Set the selected option in Year dropdown
yearIdx = 0

selectYear( yearIdx )
yearInt = getSeletedYear( yearIdx )
time.sleep(0.2)
listUrls = getDaysOfSelectedYear()

outputFilePath = outputPath + config['target']['file'].replace("$ID$", str( yearInt ) )
file_ = open( outputFilePath, 'w')
file_.write( listUrls) #.encode('utf-8')
file_.close()

browser.close()