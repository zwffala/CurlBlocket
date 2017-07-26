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

# <span class="subject-param address separator">
# 				Stockholms stad - Hägersten, Liljeholmen
#
# 				</span>
roomLocation = 'subject-param address separator'


# <a tabindex="50" class="item_link xiti_ad_heading" href="https://www.blocket.se/stockholm/2A_uthyres_vid_Telefonplan_74491121.htm?ca=11&w=1">
#
# 						2A uthyres vid Telefonplan
#
#
#
# 				</a>
adHeading = 'item_link xiti_ad_heading'

# <span class="li_detail_params first rooms">1,5 rum
roomStyle = 'li_detail_params first rooms'

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

# for line in pageContentBuf.readlines():
#     if utils.getAddressStart(line):
#         continue


lines = '''# <span class="subject-param address separator">
# 				Stockholms stad - Hägersten, Liljeholmen
#
# 				</span>'''


linesBuf = io.StringIO(lines)
linesList = linesBuf.readlines()
for index, line in enumerate(linesList):
    if utils.getAddressStart(line) is not None:
        address = utils.getAddress(''.join(linesList[index+1:]))
        print(address)
