import json
import urllib2
import datetime
curr_date = str(datetime.datetime.now())

#### West Nile Zika
westniletozika = json.load(urllib2.urlopen("https://data.cdc.gov/resource/rcpn-dfmg.json"))
with open('westniletozika' + curr_date +'.json', 'w') as outfile:
    json.dump(westniletozika, outfile)

#### TB
tb = json.load(urllib2.urlopen("https://data.cdc.gov/resource/dfu7-ewxh.json"))


with open('tb' + curr_date +'.json', 'w') as outfile:
    json.dump(tb, outfile)

##### Vibriosis
Vibriosis_data = json.load(urllib2.urlopen("https://data.cdc.gov/resource/y3jh-cim3.json"))


with open('Vibriosis_data' + curr_date +'.json', 'w') as outfile:
    json.dump(Vibriosis_data, outfile)

##### TetanustoVaricella
TetanustoVaricella = json.load(urllib2.urlopen("https://data.cdc.gov/resource/v9up-rs3x.json"))


with open('TetanustoVaricella' + curr_date +'.json', 'w') as outfile:
    json.dump(TetanustoVaricella, outfile)


#### SpottedfeverrickettsiosistoSyph
SpottedfeverrickettsiosistoSyph = json.load(urllib2.urlopen("https://data.cdc.gov/resource/e8px-pinp.json"))


with open('SpottedfeverrickettsiosistoSyph' + curr_date +'.json', 'w') as outfile:
    json.dump(SpottedfeverrickettsiosistoSyph, outfile)



#### Salmonellosisexcludingtyphoidfev
Salmonellosisexcludingtyphoidfev = json.load(urllib2.urlopen("https://data.cdc.gov/resource/rhry-k9aj.json"))


with open('Salmonellosisexcludingtyphoidfev' + curr_date +'.json', 'w') as outfile:
    json.dump(Salmonellosisexcludingtyphoidfev, outfile)


#### RabiesanimaltoRubellacongenital
RabiesanimaltoRubellacongenital = json.load(urllib2.urlopen("https://data.cdc.gov/resource/rhry-k9aj.json"))


with open('RabiesanimaltoRubellacongenital' + curr_date +'.json', 'w') as outfile:
    json.dump(RabiesanimaltoRubellacongenital, outfile)

#### MeningococcaldiseasetoPertussis

MeningococcaldiseasetoPertussis = json.load(urllib2.urlopen("https://data.cdc.gov/resource/w3an-exa3.json"))


with open('MeningococcaldiseasetoPertussis' + curr_date +'.json', 'w') as outfile:
    json.dump(MeningococcaldiseasetoPertussis, outfile)


#### LegionellosistoMalaria
LegionellosistoMalaria = json.load(urllib2.urlopen("https://data.cdc.gov/resource/yi9b-zyiu.json"))


with open('LegionellosistoMalaria' + curr_date +'.json', 'w') as outfile:
    json.dump(LegionellosistoMalaria, outfile)


#### infrequentlyreportednotifiabledis
infrequentlyreportednotifiabledis = json.load(urllib2.urlopen("https://data.cdc.gov/resource/dsgf-ve3v.json"))


with open('infrequentlyreportednotifiabledis' + curr_date +'.json', 'w') as outfile:
    json.dump(infrequentlyreportednotifiabledis, outfile)
