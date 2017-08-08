##########
# This is to curl the blocket and anylize the price a certain apartment can be rent out
# in the market giving the location, rent period and apartment area.
# It would be nice to know how long it takes to rent the apartment out.
# For long term rent only. So not consider weekly rent.
##########

import urllib3
import io
import utils

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
http = urllib3.PoolManager()
urlbase = 'https://www.blocket.se/bostad/uthyres/stockholm?cg_multi=3020'  # rent apartment
r = http.request('GET', urlbase)
pageContent = r.data.decode('utf-8')


# <a href="https://www.blocket.se/bostad/uthyres/stockholm?o=2"><span class="caret"></span><span class="sr-only">Nästa sida</span></a>
nextPage = 'Nästa sida'


#!grep data need to consider miss format tolarence (capital letter, space, unit)
# grep until no 'Nästa sida'



pageContentBuf = io.StringIO(pageContent)
# for line in pageContentBuf.readlines():
#     print(line)


# Todo: disgard entry with incomplete info
# Todo: consider entry update
# Todo: if re exp cannot handle multiple line, optimise
pageContentList = pageContentBuf.readlines()
for index, line in enumerate(pageContentList):
    if utils.getRoomLocationStartLine(line):
        address = utils.getRoomLocation(''.join(pageContentList[index+1:]))
        print(address)
    if utils.getAdHeadingStartLine(line):
        adHeading = utils.getAdHeading(''.join(pageContentList[index+1:]))
        print(adHeading)
    if utils.getRoomStyleStartLine(line):
        roomStyle = utils.getRoomStyle(''.join(pageContentList[index:]))
        print(roomStyle)
    if utils.getMonthlyRentStartLine(line):
        monthlyRent = utils.getMonthlyRent(''.join(pageContentList[index:]))
        print(monthlyRent)
    if utils.getRoomSizeStartLine(line):
        roomSize = utils.getRoomSize(''.join(pageContentList[index:]))
        print(roomSize)
    if utils.getOnMarketTimeStartLine(line):
        onMarketTime = utils.getOnMarketTime(''.join(pageContentList[index:]))
        print(onMarketTime)
