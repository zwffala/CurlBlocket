##########
# This is to curl the blocket and anylize the price a certain apartment can be rent out
# in the market giving the location, rent period and apartment area.
# It would be nice to know how long it takes to rent the apartment out.
##########

import urllib3
import io
import utils

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
http = urllib3.PoolManager()
urlbase = 'https://www.blocket.se/bostad/uthyres/stockholm'
r = http.request('GET', urlbase)
pageContent = r.data.decode('utf-8')


# <span class="li_detail_params monthly_rent">5 500 kr/mån</span>
monthlyRent = 'li_detail_params monthly_rent'

# <span class="li_detail_params first weekly_rent_peakseason">Från: 3 500 kr/vecka</span>
weeklyRent = 'li_detail_params first weekly_rent_peakseason'

# <span class="li_detail_params size">25 m²</span>
roomSize = 'li_detail_params size'

# datetime="2017-07-25 08:08:30"
onTheMarketTime = 'datetime'

# <a href="https://www.blocket.se/bostad/uthyres/stockholm?o=2"><span class="caret"></span><span class="sr-only">Nästa sida</span></a>
nextPage = 'Nästa sida'


#!grep data need to consider miss format tolarence (capital letter, space, unit)
# grep until no 'Nästa sida'



pageContentBuf = io.StringIO(pageContent)
# for line in pageContentBuf.readlines():
#     print(line)


pageContentList = pageContentBuf.readlines()
for index, line in enumerate(pageContentList):
    if utils.getRoomLocationStartLine(line) is not None:
        address = utils.getRoomLocation(''.join(pageContentList[index:]))
        print(address)
    if utils.getAdHeadingStartLine(line) is not None:
        adHeading = utils.getAdHeading(''.join(pageContentList[index:]))
        print(adHeading)
