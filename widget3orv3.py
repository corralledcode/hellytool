from HellyTool import checkrs
from HellyTool import findrscover
from HellyTool import simplifycover
from HellyTool import maxcliquesize
from HellyTool import findncovers

V3or = ['a','b','c','d','e','f','u','v','w']
E3or = ['abuv','cduw','efwv',
        'bdfuvw']
C3or = ['bdfuvw','abu','evf','cdw']
C3orFFF = C3or + ['auv','cuw','evw']
C3orFFT = C3or + ['auv','cuw','efw']
C3orFTF = C3or + ['auv','cud','evw']
C3orFTT = C3or + ['auv','cud','efw']
C3orTFF = C3or + ['abv','cuw','evw']
C3orTFT = C3or + ['abv','cuw','efw']
C3orTTF = C3or + ['abv','cud','evw']
C3orTTT = C3or + ['abv','cuw','efw']


V3or = ['a1','d1','e1',
        'a2','d2','e2',
        'a3','d3','e3']
E3or = ['a1d1e1e3',
        'a2d2e1e2',
        'a3d3e2e3',
        'd1d2d3e1e2e3']

C3or = ['a1d1e1',
        'a2d2e2',
        'a3d3e3',
        'd1d2d3e1e2e3']

V3orE = V3or + ['b1','c1','z1',
                'b2','c2','z2',
                'b3','c3','z3',
                'r1','s1','r2','s2','r3','s3']

E3orE = E3or + ['a1b1c1z1','b1d1r1','c1e1s1','a1b1c1d1e1',
                'a2b2c2z2','b2d2r2','c2e2s2','a2b2c2d2e2',
                'a3b3c3z3','b3d3r3','c3e3s3','a3b3c3d3e3']

C3orE = C3or + ['b1c1z1', 'b1d1r1', 'c1e1s1', 'a1b1c1d1e1',
                'b2c2z2', 'b2d2r2', 'c2e2s2', 'a2b2c2d2e2',
                'b3c3z3', 'b3d3r3', 'c3e3s3', 'a3b3c3d3e3']


C3orE = simplifycover(C3orE)

#checkrs(V3orE,E3orE,C3orE + ['a1b1z1','a2b2z2','a3b3z3','a3e2e3','a1e1e3','a2e2e1'])

#print(maxcliquesize(V3orE,E3or))

findrscover(V3orE,E3orE,['d1d2d3e1e2e3','a1b1c1d1e1','a2b2c2d2e2','b1c1z1','b2c2z2','b3c3z3','a3b3c3d3e3'],False)

