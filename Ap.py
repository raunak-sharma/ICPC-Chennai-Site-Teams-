from bs4 import BeautifulSoup
import urllib2
from collections import Counter, OrderedDict

url = "https://icpc.baylor.edu/regionals/finder/asia-chennai-first-round-2017"
content = urllib2.urlopen(url).read()
soup = BeautifulSoup(content, "html5lib")

#source code
code = soup.prettify()
code1 = code.encode('ascii', 'ignore').decode('ascii')

myclass = soup.find_all("span", { "class" : "gridCols" } )

z = []
clglist = []

for i in range(len(myclass)) :
    z = ''.join(str(myclass[i]))
    strr = ''
    j = 23
    while z[j] != '\n' :
        strr += z[j]
        j = j + 1
    clglist.append(strr)

x = Counter(clglist)
c = OrderedDict(x.most_common())

i = 1

for key, value  in c.items() :
    print '{: <85}'.format(key) + ' : %d' %(value)
    i = i + 1

print "Total Teams = %d" %len(c)