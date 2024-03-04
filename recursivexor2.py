from HellyTool import checkrs

V = ['a','b','c','d','e','f','g','h','i',
     'j','k','l',
     'w','x',
     's','t','u','v','z']

E = ['ab','ac','az','bc','bz','cz',
     'bd','be','cd','ce',
     'dz','de','df','ez','ef','fz',
     'cs','es','ce','cg',
     'bt','dt','bd','bh','bv','gv',
     'cu','hu',
     'gz','gh','gi','hz','hi','iz',
     'jk','jl','jz','kl','kz','lz',
     'ck','cj','dk','dj','bj','bk','ej','ek',
     'hk','hj','gk','gj',
     'hw','kw','jx','gx',
     'bg','ch','dg','dh','eg','eh']


CT = ['abc','def','ghi','jkl','bcdeghjkz','ces','bdt','chu','bgv','hkw','gjx',
     'abz','efz','ihz','jlz']

CF = ['abc','def','ghi','jkl','bcdeghjkz','ces','bdt','chu','bgv','hkw','gjx',
     'acz','dfz','igz','klz']

CFx = ['abc','def','ghi','jkl','bcdeghjkz','ces','bdt','chu','bgv','hkw','gjx',
       'acz','dfz','igz','jlz']

CFxx = ['abc','def','ghi','jkl','bcdeghjkz','ces','bdt','chu','bgv','hkw','gjx',
        'acz','dfz','ihz','jlz']

CFxxx = ['abc','def','ghi','jkl','bcdeghjkz','ces','bdt','chu','bgv','hkw','gjx',
        'acz','dfz','ihz','klz']

CFxxxx = ['abc','def','ghi','jkl','bcdeghjkz','ces','bdt','chu','bgv','hkw','gjx',
       'acz','efz','igz','jlz']

CFxxxxx = ['abc','def','ghi','jkl','bcdeghjkz','ces','bdt','chu','bgv','hkw','gjx',
       'abz','efz','hiz','klz']


checkrs(V,E,CFxxxxx)