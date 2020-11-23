import os
import sys

DIR_TASK = os.path.basename(os.getcwd())
DIR_LIB = os.path.abspath(os.path.join(os.path.dirname(__file__),"../"))
DIR_TASK = os.path.dirname(os.path.abspath(__file__))

import json, csv, time, string, itertools, copy, yaml
import datetime as dt
import urllib

os.chdir( os.path.dirname(__file__) )

CONFIG_FILE_NAME = '001.01_config'
config = yaml.load( stream = file( DIR_TASK + '\\' + CONFIG_FILE_NAME + '.yml', 'r'), Loader=yaml.FullLoader)
#yaml.dump( config, file( DIR_TASK + '\\config.yml', 'w') )

sys.path.append( DIR_LIB )

from lib.router import Router
router = Router( )
print '>> Walk, Don`t Run'


def tsToDate( miliTs ):
  #convert Drawdate To Timestamp
  tss= float( str(miliTs)[ : -3] )
  return dt.datetime.fromtimestamp(tss).strftime('%Y-%m-%d')


# --------------------------------------------------------------------------

outputPath =  router.getRoute( config['target']['route'] ) + config['target']['dir']

#com: create output folder
if not os.path.exists( outputPath ):
  os.makedirs( outputPath )

# --------------------------------------------------------------------------

data_dir = router.getRoute( config['source']['route'] ) + config['source']['dir']
listFiles = os.listdir( data_dir )

container = { }

for idFile, nameFile in enumerate( listFiles ):

  if '!' in nameFile:
    continue

  #com: extract year: capture_2018.txt
  keyYear = str( nameFile.split(".")[0].split("_")[1] )

  container[ keyYear ] = { }
  #COM: Get Lines in File
  with open( data_dir + nameFile) as f:
    lines = f.readlines()

  for idLine , urlLine in enumerate( lines ):

    ##COM: Get content of Url
    url = urlLine
    urlDate = str( url.split("/")[-1].translate(None, '\n')  )
  
    response = urllib.urlopen(url)
    data = json.loads(response.read())[0] # return an object nested in a list -> [0]

    naturalOrderNumbers = [ num['drawNumber'] for num in data['drawNumbersCollection']]
    sortedNumbers = naturalOrderNumbers[:]
    sortedNumbers.sort()

    oddObj = [ { 
        'type': odd['winningClassDescription']['winningClassShortName'].replace(' ',''),
        'odds': odd['odds'],
        'winners': odd['numberOfWinners'],
      } for odd in data['oddsCollection'] ] 

    date = tsToDate( data['drawDate'] )
    container[ keyYear ][ urlDate ] = {
      'numbers': naturalOrderNumbers,
      'numbers_sorted': sortedNumbers,
      'super_number': data['superNumber'],
      'timestamp_ms': data['drawDate'],
      'url': urlLine.translate(None, '\n'),
      'week_day': data['gameType']['name'].split(' ')[2],
      'week_day_n': dt.datetime.strptime( date, '%Y-%m-%d').weekday(),
      'ts': date,
      'odds':oddObj
    }

  #com: Convert to sorted List of Items
  sortedItems = []
  sortedKeysList = container[ keyYear ].keys()
  sortedKeysList.sort()

  for key in sortedKeysList:
    sortedItems.append( container[ keyYear ][key] )

  outputFilePath = outputPath + config['target']['file'].replace("$ID$", str( keyYear ) )
  with open( outputFilePath, 'a') as outfile:
    json.dump( sortedItems, outfile) #container[ keyYear ]
