from HellyTool import checkrs

V = ['a','b','c','d','e','f','u','v','w']
E = ['abuv','cduw','efwv',
     'bdfuvw']
C = ['bdfuvw','abu','evf','cud']
CFFF = C + ['auv','cuw','evw']
CFFT = C + ['auv','cuw','efw']
CFTF = C + ['auv','cdw','evw']
CFTT = C + ['auv','cdw','efw']
CTFF = C + ['abv','cuw','evw']
CTFT = C + ['abv','cuw','efw']
CTTF = C + ['abv','cdw','evw']
CTTT = C + ['abv','cdw','efw']

#checkrs(V,E,CTFT)
checkrs(V,E,CFFF)