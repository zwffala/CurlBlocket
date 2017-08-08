import re

# <span class="subject-param address separator">
# 				Stockholms stad - Hägersten, Liljeholmen
#
# 				</span>
roomLocation = 'subject-param address separator'

def getRoomLocationStartLine(line):
    return re.search(roomLocation, line)

def getRoomLocation(lines):
    m = re.search('((.|\n)*)</span>', lines)
    if m is not None:
        m2 = re.search('[^\n^\t]*[^\n^\t]$', m.group(1), re.MULTILINE)
        if m2 is not None:
            return m2.group(0)
    return ''


# <a tabindex="50" class="item_link xiti_ad_heading" href="https://www.blocket.se/stockholm/2A_uthyres_vid_Telefonplan_74491121.htm?ca=11&w=1">
#
# 						2A uthyres vid Telefonplan
#
#
#
# 				</a>
adHeading = 'item_link xiti_ad_heading'
def getAdHeadingStartLine(line):
    return re.search(adHeading, line)

def getAdHeading(lines):
    m = re.search('((.|\n)*)</a>', lines)
    if m is not None:
        m2 = re.search('[^\n^\t]*[^\n^\t]$', m.group(1), re.MULTILINE)
        if m2 is not None:
            return m2.group(0)
    return ''

# <span class="li_detail_params first rooms">1,5 rum</span>
roomStyle = 'li_detail_params first rooms'
def getRoomStyleStartLine(line):
    return re.search(roomStyle, line)

def getRoomStyle(lines):
    m = re.search(roomStyle+'">(.*) rum</span>', lines)
    if m:
        return float(m.group(1).replace(',', '.'))
    return 0

# <span class="li_detail_params monthly_rent">5 500 kr/mån</span>
monthlyRent = 'li_detail_params monthly_rent'
def getMonthlyRentStartLine(line):
    return re.search(monthlyRent, line)

def getMonthlyRent(lines):
    m = re.search(monthlyRent+'">(.*) kr/mån</span>', lines)
    if m:
        return int(m.group(1).replace(' ', ''))
    return 0

# <span class="li_detail_params first weekly_rent_peakseason">Från: 3 500 kr/vecka</span>
weeklyRent = 'li_detail_params first weekly_rent_peakseason'
def getWeeklyRentStartLine(line):
    return re.search(weeklyRent, line)

def getWeeklyRent(lines):
    m = re.search(weeklyRent+'">Från: (.*) kr/vecka</span>', lines)
    if m:
        return int(m.group(1).replace(' ', ''))
    return 0

# <span class="li_detail_params size">25 m²</span>
roomSize = 'li_detail_params size'
def getRoomSizeStartLine(line):
    return re.search(roomSize, line)

def getRoomSize(lines):
    m = re.search(roomSize+'">(.*) m²</span>', lines)
    if m:
        return float(m.group(1).replace(' ', '').replace(',','.'))
    return 0

# datetime="2017-07-25 08:08:30">
onTheMarketTime = 'datetime'
def getOnMarketTimeStartLine(line):
    return re.search(onTheMarketTime, line)

def getOnMarketTime(lines):
    m = re.search(onTheMarketTime+'="(.*?)">', lines)
    if m:
        print(m.group(1))
        return m.group(1)
    return ''

line = ''' datetime=
"2017-07-25 08:08:30">1 aug <span class="time">17:07</span></time>
'''
getOnMarketTime(line)
