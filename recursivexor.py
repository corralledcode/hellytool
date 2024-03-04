from HellyTool import checkrs

V = ['a','b','c','d','e','f','g','h','i','s','t','u','v','z']

E = ['ab','ac','az','bc','bz','cz',
     'bd','be','cd','ce',
     'dz','de','df','ez','ef','fz',
     'cs','es','ce','cg','ch'
     'bt','bg','bt','dt','bd','bh','bv','gv',
     'cu','hu',
     'gz','gh','gi','hz','hi','iz',
     'dg','dh','eg','eh','ch']

CT = ['abc','def','ghi','bcdez','bcghz','ces','bdt','chu','bgv',
     'abz','efz','ihz']
CF = ['abc','def','ghi','bcdez','bcghz','ces','bdt','chu','bgv',
     'acz','dfz','giz']

CFx = ['abc','def','ghi','bcdez','bcghz','ces','bdt','chu','bgv',
       'acz','efz','giz']

CT2 = ['abc','def','ghi','bcdeghz','ces','bdt','chu','bgv',
       'abz','efz','hiz']
CF2 = ['abc','def','ghi','bcdeghz','ces','bdt','chu','bgv',
       'acz','dfz','giz']

CF2x = ['abc','def','ghi','bcdeghz','ces','bdt','chu','bgv',
       'acz','efz','giz']

CF2xx = ['abc','def','ghi','bcdeghz','ces','bdt','chu','bgv',
       'abz','dfz','hiz']

CF2xxx = ['abc','def','ghi','bcdeghz','ces','bdt','chu','bgv',
       'acz','efz','hiz']


checkrs(V,E,CF2)