import re

# <span class="subject-param address separator">
# 				Stockholms stad - Hägersten, Liljeholmen
#
# 				</span>
roomLocation = 'subject-param address separator'
def getAddressStart(line):
    return re.search(roomLocation, line)

def getAddress(lines):
    print(lines)
    m = re.search('((.|\n)*)</span>', lines)
    if m is not None:
        print('m.group(0) '+m.group(0))
        m2 = re.search('[^\n^\t]*[^\n^\t]$', m.group(1), re.MULTILINE)
        return m2.group(0)
    return 'not found'
