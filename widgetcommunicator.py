from HellyTool import checkrs
from HellyTool import findrscover
from HellyTool import maxcliquesize
from HellyTool import findncovers


V = ['a','b','c','d','e','f','z','s','t']
E = ['ab','ac','bc','az','bz','cz','bd','cd','ce','be','dz','ez','de','ef','df','zf','cs','es','bt','dt']
C = ['abz','abc','cse','btd','bcdez','def','efz']


findrscover(V,E,['bcdez'], False)

#print(maxcliquesize(V,E))

#checkrs(V,E,C,True)