from HellyTool import checkrs

V = ['a','b','c','d','e','f','u','v','w']
E = ['ab','au','av','bv','bu','uv',
     'cd','cu','cw','du','dw',
     'ef','ev','ew','fv','fw','vw',
     'du','fu','bw','uw']
C = ['fvwu','bvwu','duvw']
CFFF = ['fvwu','bvwu','duvw','abu','evf','cud',
        'auv','cuw','evw']
CFFT = ['fvwu','bvwu','duvw','abu','evf','cud',
        'auv','cuw','efw']
CFTF = ['fvwu','bvwu','duvw','abu','evf','cud',
        'auv','cdw','evw']
CFTT = ['fvwu','bvwu','duvw','abu','evf','cud',
        'auv','cdw','efw']
CTFF = ['fvwu','bvwu','duvw','abu','evf','cud',
        'abv','cuw','evw']
CTFT = ['fvwu','bvwu','duvw','abu','evf','cud',
        'abv','cuw','efw']
CTTF = ['fvwu','bvwu','duvw','abu','evf','cud',
        'abv','cdw','evw']
CTTT = ['fvwu','bvwu','duvw','abu','evf','cud',
        'abv','cdw','efw']

checkrs(V,E,CFTF)