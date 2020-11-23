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

listYears = elem[0].find_elements_by_tag_name('option')

for y, year in enumerate( listYears ):
    optionYear = elem[0].find_elements_by_tag_name('option')[y].click( )
    yearInt = elem[0].find_elements_by_tag_name('option')[y].get_attribute('value')
    time.sleep(0.5)

    listUrls = ''
    options = elem[1].find_elements_by_tag_name('option')

    for i, opt in enumerate(options):
        lotoDay =  opt.get_attribute('innerHTML').split(" ")[0]
        lotoDate =  opt.get_attribute('innerHTML').split(" ")[1]

        lotoDateDt = dt.datetime.strptime(lotoDate, '%d.%m.%Y')
        newLotoDate = dt.datetime.strftime( lotoDateDt, '%Y-%m-%d')

        #transform date     04.01.2017 >> 2017-01-04
        print str(i) + " " + lotoDay + " " + newLotoDate
        print targetUrl + newLotoDate
        listUrls += targetUrl + newLotoDate + '\n'

    data_dir ="./url_captures/"
    filename = yearInt + '.urls.txt'

    file_ = open(data_dir + filename, 'w')
    file_.write( listUrls) #.encode('utf-8')
    file_.close()

    time.sleep(0.5)

    #time.sleep(1)

browser.close()
