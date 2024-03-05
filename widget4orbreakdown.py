from HellyTool import findrscover
from HellyTool import checkrs
from HellyTool import simplifycover


V4or = ['a1','b1','c1','d1','e1',
        's1','t1','z1',
        'a2','b2','c2','d2','e2',
        's2','t2','z2',
        'a3','b3','c3','d3','e3',
        's3','t3','z3',
        'a4','b4','c4','d4','e4',
        's4','t4','z4',
        'd1','d2','d3','d4',
        'g1','g2','g3','g4',
        'j1','j2','j3','j4','l1','l2','l3','l4','m1','m2','m3','m4','n1','n2','n3','n4','o1','o2','o3','o4','p1','p2','p3','p4','q1','q2','q3','q4','u1','u2','u3','u4','v1','v2','v3','v4',
        'k1','k2','k3','k4']

E4or = ['g1g2g3g4',
        'd1g1g2g4','d2g1g2g3','d3g2g3g4','d4g1g3g4',
        'a1b1c1d1g4e1', 'a1b1c1z1', 'a1g4d1g2e1j1k1', 'c1e1s1', 'b1g4t1',
        'a2b2c2d2g1e2', 'a2b2c2z2', 'a2g1d2g3e2j2k2', 'c2e2s2', 'b2g1t2',
        'a3b3c3d3g2e3', 'a3b3c3z3', 'a3g2d3g4e3j3k3', 'c3e3s3', 'b3g2t3',
        'a4b4c4d4g3e4', 'a4b4c4z4', 'a4g3d4g1e4j4k4', 'c4e4s4', 'b4g3t4',
        'e1d1d2d3d4k1g1g2g3g4j1',
        'e2d2d3d4d1k2g1g2g3g4j2',
        'e3d3d4d1d2k3g1g2g3g4j3',
        'e4d4d1d2d3k4g1g2g3g4j4',
        'a1b1c1g1g2g3','a2b2c2g2g3g4','a3b3c3g3g4g1','a4b4c4g4g1g2',
        'g2g4g1j1','g3g1g2j2','g4g2g3j3','g1g3g4j4',
        'd1j1k1l1','j1k1l1m1n1','l1m1n1o1','j1p1m1','k1n1q1','j1k1u1','m1n1v1',
        'd2j2k2l2','j2k2l2m2n2','l2m2n2o2','j2p2m2','k2n2q2','j2k2u2','m2n2v2',
        'd3j3k3l3','j3k3l3m3n3','l3m3n3o3','j3p3m3','k3n3q3','j3k3u3','m3n3v3',
        'd4j4k4l4','j4k4l4m4n4','l4m4n4o4','j4p4m4','k4n4q4','j4k4u4','m4n4v4']

C4or = ['b1c1z1', 'c1e1s1', 'b1g4t1',
        'b2c2z2', 'c2e2s2', 'b2g1t2',
        'b3c3z3', 'c3e3s3', 'b3g2t3',
        'b4c4z4', 'c4e4s4', 'b4g3t4',
        'g4e1d1d2d3d4k1g1g2g3j1',
        'g1e2d2d3d4d1k2g2g3g4j2',
        'g2e3d3d4d1d2k3g3g4g1j3',
        'g3e4d4d1d2d3k4g4g1g2j4',
        'a1b1c1g4d1e1g1g2g3',
        'a2b2c2g1d2e2g2g3g4',
        'a3b3c3g2d3e3g3g4g1',
        'a4b4c4g3d4e4g4g1g2',

        'a1d1j1k1','j1k1l1m1n1','m1n1o1','j1p1m1','k1n1q1','j1k1u1','m1n1v1',
        'a2d2j2k2','j2k2l2m2n2','m2n2o2','j2p2m2','k2n2q2','j2k2u2','m2n2v2',
        'a3d3j3k3','j3k3l3m3n3','m3n3o3','j3p3m3','k3n3q3','j3k3u3','m3n3v3',
        'a4d4j4k4','j4k4l4m4n4','m4n4o4','j4p4m4','k4n4q4','j4k4u4','m4n4v4']



C4orFFFF = C4or + ['a1c1z1','a1d1g2g4g1j1','d1j1l1','l1n1o1',
                   'a2c2z2','a2d2g3g1g2j2','d2j2l2','l2n2o2',
                   'a3c3z3','a3d3g4g2g3j3','d3j3l3','l3n3o3',
                   'a4c4z4','a4d4g1g3g4j4','d4j4l4','l4n4o4']

C4orFFFT = C4or + ['a1b1z1','a1d1g2e1k1','d1k1l1','l1m1o1',
                   'a2c2z2','a2d2g3g1g2j2','d2j2l2','l2n2o2',
                   'a3c3z3','a3d3g4g2g3j3','d3j3l3','l3n3o3',
                   'a4c4z4','a4d4g1g3g4j4','d4j4l4','l4n4o4']

C4orFFTF = C4or + ['a1c1z1','a1d1g2g4g1j1','d1j1l1','l1n1o1',
                   'a2b2z2','a2d2g3e2k2','d2k2l2','l2m2o2',
                   'a3c3z3','a3d3g4g2g3j3','d3j3l3','l3n3o3',
                   'a4c4z4','a4d4g1g3g4j4','d4j4l4','l4n4o4']


C4orFFTT = C4or + ['a1b1z1','a1d1g2e1k1','d1k1l1','l1m1o1',
                   'a2b2z2','a2d2g3e2k2','d2k2l2','l2m2o2',
                   'a3c3z3','a3d3g4g2g3j3','d3j3l3','l3n3o3',
                   'a4c4z4','a4d4g1g3g4j4','d4j4l4','l4n4o4']

C4orFTFF = C4or + ['a1c1z1','a1d1g2g4g1j1','d1j1l1','l1n1o1',
                   'a2c2z2','a2d2g3g1g2j2','d2j2l2','l2n2o2',
                   'a3b3z3','a3d3g4e3k3','d3k3l3','l3m3o3',
                   'a4c4z4','a4d4g1g3g4j4','d4j4l4','l4n4o4']

C4orFTFT = C4or + ['a1b1z1','a1d1g2e1k1','d1k1l1','l1m1o1',
                   'a2c2z2','a2d2g3g1g2j2','d2j2l2','l2n2o2',
                   'a3b3z3','a3d3g4e3k3','d3k3l3','l3m3o3',
                   'a4c4z4','a4d4g1g3g4j4','d4j4l4','l4n4o4']

C4orFTTF = C4or + ['a1c1z1','a1d1g2g4g1j1','d1j1l1','l1n1o1',
                   'a2b2z2','a2d2g3e2k2','d2k2l2','l2m2o2',
                   'a3b3z3','a3d3g4e3k3','d3k3l3','l3m3o3',
                   'a4c4z4','a4d4g1g3g4j4','d4j4l4','l4n4o4']

C4orFTTT = C4or + ['a1c1z1','a1d1g2g4g1j1','d1j1l1','l1n1o1',
                   'a2b2z2','a2d2g3e2k2','d2k2l2','l2m2o2',
                   'a3b3z3','a3d3g4e3k3','d3k3l3','l3m3o3',
                   'a4b4z4','a4d4g1e4k4','d4k4l4','l4m4o4']

C4orTFFF = C4or + ['a1c1z1','a1d1g2g4g1j1','d1j1l1','l1n1o1',
                   'a2c2z2','a2d2g3g1g2j2','d2j2l2','l2n2o2',
                   'a3c3z3','a3d3g4g2g3j3','d3j3l3','l3n3o3',
                   'a4b4z4','a4d4g1e4k4','d4k4l4','l4m4o4']

C4orTFFT = C4or + ['a1b1z1','a1d1g2e1k1','d1k1l1','l1m1o1',
                   'a2c2z2','a2d2g3g1g2j2','d2j2l2','l2n2o2',
                   'a3c3z3','a3d3g4g2g3j3','d3j3l3','l3n3o3',
                   'a4b4z4','a4d4g1e4k4','d4k4l4','l4m4o4']

C4orTFTF = C4or + ['a1c1z1','a1d1g2g4g1j1','d1j1l1','l1n1o1',
                   'a2b2z2','a2d2g3e2k2','d2k2l2','l2m2o2',
                   'a3c3z3','a3d3g4g2g3j3','d3j3l3','l3n3o3',
                   'a4b4z4','a4d4g1e4k4','d4k4l4','l4m4o4']

C4orTFTT = C4or + ['a1b1z1','a1d1g2e1k1','d1k1l1','l1m1o1',
                   'a2b2z2','a2d2g3e2k2','d2k2l2','l2m2o2',
                   'a3c3z3','a3d3g4g2g3j3','d3j3l3','l3n3o3',
                   'a4b4z4','a4d4g1e4k4','d4k4l4','l4m4o4']

C4orTTFF = C4or + ['a1c1z1','a1d1g2g4g1j1','d1j1l1','l1n1o1',
                   'a2c2z2','a2d2g3g1g2j2','d2j2l2','l2n2o2',
                   'a3b3z3', 'a3d3g4e3k3', 'd3k3l3', 'l3m3o3',
                   'a4b4z4', 'a4d4g1e4k4', 'd4k4l4', 'l4m4o4']

C4orTTFT = C4or + ['a1b1z1','a1d1g2e1k1','d1k1l1','l1m1o1',
                   'a2c2z2','a2d2g3g1g2j2','d2j2l2','l2n2o2',
                   'a3b3z3', 'a3d3g4e3k3', 'd3k3l3', 'l3m3o3',
                   'a4b4z4', 'a4d4g1e4k4', 'd4k4l4', 'l4m4o4']

C4orTTTF = C4or + ['a1c1z1','a1d1g2g4g1j1','d1j1l1','l1n1o1',
                   'a2b2z2','a2d2g3e2k2','d2k2l2','l2m2o2',
                   'a3b3z3', 'a3d3g4e3k3', 'd3k3l3', 'l3m3o3',
                   'a4b4z4', 'a4d4g1e4k4', 'd4k4l4', 'l4m4o4']

C4orTTTT = C4or + ['a1b1z1','a1d1g2e1k1','d1k1l1','l1m1o1',
                   'a2b2z2','a2d2g3e2k2','d2k2l2','l2m2o2',
                   'a3b3z3','a3d3g4e3k3','d3k3l3','l3m3o3',
                   'a4b4z4','a4d4g1e4k4','d4k4l4','l4m4o4']


simplifycover(C4orFFFF)
simplifycover(C4orFFFT)
simplifycover(C4orFFTF)
simplifycover(C4orFFTT)
simplifycover(C4orFTFF)
simplifycover(C4orFTFT)
simplifycover(C4orFTTF)
simplifycover(C4orFTTT)
simplifycover(C4orTFFF)
simplifycover(C4orTFFT)
simplifycover(C4orTFTF)
simplifycover(C4orTFTT)
simplifycover(C4orTTFF)
simplifycover(C4orTTFT)
simplifycover(C4orTTTF)
simplifycover(C4orTTTT)

#checkrs(V4or,E4or,C4orFFFF)

#print(maxcliquesize(V4or,E4or))
findrscover(V4or,E4or,C4orTTTT, False)