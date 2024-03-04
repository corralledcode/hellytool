from HellyTool import checkrs
from HellyTool import findrscover

V = ['a','b','c','f','g','h','q','r','z']
E = ['ab','ac','az','bc','bz','cz',
     'ag','af','ar',
     'bq','cq','gh','ch','br','gf',
     'cg','bg']

C = ['abr','bcq','afg','cgh','abz','bcz','abcg']

findrscover(V,E,[],False)
#checkrs(V,E,C)