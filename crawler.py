import re, urllib

textfile = file('list_of_URL.txt','wt')
print "Enter the URL you wish to crawl.."
print 'Usage  - "http://www.fanabc.com/index.php/fbc-archive.html" <-- With the double quotes'
myurl = input("@> ")
for i in re.findall('''href=["'](.[^"']+)["']''', urllib.urlopen(myurl).read(), re.I):
        print i
        for ee in re.findall('''href=["'](.[^"']+)["']''', urllib.urlopen(i).read(), re.I):
                print ee
                textfile.write(ee+'\n')
textfile.close()