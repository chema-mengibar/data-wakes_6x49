import time
import datetime as dt
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import os
os.chdir( os.path.dirname(__file__) )

#strDate = '23.12.2017'
#newDate = dt.datetime.strptime(strDate, '%d.%m.%Y')
#print dt.datetime.strftime(newDate, '%Y-%m-%d')


browser = webdriver.Chrome(executable_path=r".\common\chromedriver.exe")

url = 'https://www.lotto.de/de/ergebnisse/lotto-6aus49/lottozahlen.html'

targetUrl = "https://www.lotto.de/bin/6aus49_archiv?drawday="

browser.get(url)
time.sleep(1)


elem = browser.find_elements(By.XPATH, '//select')
options = elem[1].find_elements_by_tag_name('option')

listUrls = ''

for i, opt in enumerate(options):
    lotoDay =  opt.get_attribute('innerHTML').split(" ")[0]
    lotoDate =  opt.get_attribute('innerHTML').split(" ")[1]

    lotoDateDt = dt.datetime.strptime(lotoDate, '%d.%m.%Y')
    newLotoDate = dt.datetime.strftime( lotoDateDt, '%Y-%m-%d')

    #transform date     04.01.2017 >> 2017-01-04
    print str(i) + " " + lotoDay + " " + newLotoDate
    print targetUrl + newLotoDate
    listUrls += targetUrl + newLotoDate + '\n'




browser.close()

data_dir ="./captures/"
filename = '2017.urls.txt'

file_ = open(data_dir + filename, 'w')
file_.write( listUrls) #.encode('utf-8')
file_.close()
