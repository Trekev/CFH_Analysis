from __future__ import absolute_import
import os

flightNum = raw_input(u'What flight would you like to pull from?(NNN)')

systemID = {u'LMG': u'rtso',
            u'CFH': u'78000',
            u'GRAW': u'79000',
            u'MW41-1': u'71999',
            u'MW41-2': u'71998',
            u'MW41-3': u'71997'
            }

path = u'/opt/NESDIS/Wallops Campaign/' + flightNum
os.chdir(path)

for i in list(systemID.keys()):
    if i in os.listdir(os.getcwdu()):
        os.chdir(i)
	print i
	print os.getcwdu()
        for j in os.listdir(os.getcwdu()):
            if systemID[i] in j:
                os.system(u'cp ' + j + u' ' + u'/opt/NESDIS/Wallops\ Campaign/Processing')
        os.chdir(path)
	print os.getcwdu()