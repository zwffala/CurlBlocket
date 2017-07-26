import re

# <span class="subject-param address separator">
# 				Stockholms stad - Hägersten, Liljeholmen
#
# 				</span>
roomLocation = 'subject-param address separator'

def getRoomLocationStartLine(line):
    return re.search(roomLocation, line)

def getRoomLocation(lines):
    print(lines)
    m = re.search('((.|\n)*)</span>', lines)
    if m is not None:
        print('m.group(1)'+m.group(1))
        m2 = re.search('(.*)[^\n^\t]', m.group(1), re.MULTILINE)
        if m2 is not None:
            print('m2.group(0)'+m2.group(0))
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
#def getRoomStypeStartLine()


lines = '''# <span class="subject-param address separator">
# 				Stockholms stad - Hägersten, Liljeholmen
#
# 				</span>'''
getRoomLocation(lines)