from HellyTool import checkrs
from HellyTool import findrscover
from HellyTool import simplifycover

V = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v']

E = ['defghijklmnopq',
     'aehf','bedg','cghi',
     'fiv','iqu','djr','kns','mpt']

C = ['aef','bed','cgi','defghijklmnopq','fiv','djr','kns','mtp','iqu']
CFF = C + ['aeh','beg','chi','gjl','lno','oph']
CTF = C + ['afh', 'beg', 'cgh', 'gjl', 'lno','oph']
CFT = C + ['aeh', 'bdg', 'cgh', 'gkl', 'lmo','oqn']
CTT = C + ['afh', 'bdg', 'cgh', 'gkl', 'lmo','oqn']

CFFx = C +  ['aeh','beg','chg','gjl','lno','oph']

CFFxx = C + ['bdg','chi','aeh']

findrscover(V,E,['defghijklmnopq'], False)
#for c in findrscover(V,E,['defghijklmnopq'],False):
#     simplifycover(c)



#checkrs( V,E,CFFxx)
