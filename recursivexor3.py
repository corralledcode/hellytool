from HellyTool import checkrs

V = ['a','b','c','d','e','f','g','h','i',
     's','t','u','v','z']

E = ['ab','ac','az','bc','bz','cz',
     'bd','be','cd','ce',
     'dz','de','df','ez','ef','fz',
     'cs','es','cg','ch',
     'bt','dt','bh','bg',
     'gz','gh','gi','hz','hi','iz',
     'eh','eg','dh','dg',
     'cu','hu','bv','gv']


CT = ['abc','def','ghi','bcdeghz','ces','bdt','chu','bgv',
     'abz','efz','hiz']

CF = ['abc','def','ghi','bcdeghz','ces','bdt','chu','bgv',
     'acz','dfz','giz']

CFx = ['abc','def','ghi','bcdeghz','ces','bdt','chu','bgv',
       'acz','dfz','hiz']

CFxx = ['abc','def','ghi','bcdeghz','ces','bdt','chu','bgv',
       'acz','efz','giz']

CFxxx = ['abc','def','ghi','bcdeghz','ces','bdt','chu','bgv',
         'acz','dfz','giz']



checkrs(V,E,CT)