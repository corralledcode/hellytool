from HellyTool import checkrs
from HellyTool import simplifycover
from HellyTool import findrscover
from HellyTool import maxcliquesize

"""
V4or = ['a1','b1','c1','d1','e1','f1','g1','h1','s1','t1','u1','v1','w1','z1','y1',
        'h2','h3','h4']

E4or = ['a1b1c1z1','a1d1e1y1','a1b1c1d1e1','a1d1e1f1','d1e1g1y1',
        'e1f1h1h2','e1g1h1h4',
        'a1c1d1e1f1g1y1',
        'h1h2h3h4',
        'e1g1h1y1',
        'e1f1h1a1',
        'a1f1u1','g1v1y1',
        'b1d1s1','c1e1t1',
        'h2h3h4w1']

C4or = ['b1c1z1','a1b1c1d1e1','a1d1e1f1','d1e1g1y1',
        'a1c1d1e1f1g1y1',
        'e1g1h1y1',
        'e1f1h1a1',
        'a1f1u1', 'g1v1y1',
        'b1d1s1', 'c1e1t1',
        'h2h3h4w1',
        'f1h1h2',
        'g1h1h4',
        'h1h2h3',
        'h2h3h4',
        'h1h3h4']

C4orT = C4or + ['a1c1z1','a1d1y1','e1g1h4','e1f1h2']

print (C4or)
"""

"""
V4or = ['a1','b1','c1','d1','e1','f1','g1','h1','s1','t1','u1','v1','w1','z1','y1',
        'h2','h3','h4']

E4or = ['a1d1e1y1','a1d1e1f1','d1e1g1y1',
        'e1f1h1h2','e1g1h1h4',
        'e1f1g1h1',
        'a1d1e1f1g1y1',
        'h1h2h3h4',
        'e1g1h1y1',
        'e1f1h1a1',
        'a1f1u1','g1v1y1',
        'h2h3h4w1']

C4or = [#'a1d1e1f1',#'d1e1g1y1',
        'a1d1e1f1g1y1',
        'e1g1h1y1',
        'e1f1h1a1',
        'e1f1g1h1',
        'a1f1u1', 'g1v1y1',
        'h2h3h4w1',
        'f1h1h2',
        'g1h1h4',
        'h1h2h3',
        'h2h3h4',
        'h1h3h4']

C4orT = C4or + ['a1d1y1','e1g1h4','e1f1h2']
"""

"""
V4or = ['a1','b1','c1','d1','e1','f1','g1','h1','s1','t1','u1','v1','w1','z1','y1',
        'h2','h3','h4']

E4or = ['a1d1e1y1','h1h2h3h4','a1e1f1y1','e1g1h1h3','e1f1h1h2','a1f1u1','a1g1v1','a1e1f1g1h1y1','f1h4','g1h4']

C4or = ['a1e1f1g1h1y1','a1d1y1','d1e1y1','e1f1h2','a1f1u1','a1g1v1','e1f1h2',
        'h2h3h4','e1g1h3','e1f1g1h1h4']

C4orT = C4or + []


V4or = ['a1','b1','c1','d1','s1','t1','z1',
        'e1','f1','g1','h1','u1','v1','y1',
        'i1','i2','i3','i4']

E4or = ['a1b1c1z1','a1b1c1d1f1g1h1i1','a1d1i1i3','b1d1t1','c1i1s1','i1i2i3i4',
        'a1f1g1y1','a1f1g1h1i1','a1h1i1i2','f1i1v1','g1h1u1',
        'd1h1i1i2i3i4']

C4or = ['c1b1z1','a1b1c1d1f1g1h1i1','c1i1s1','b1d1t1',
        'f1g1y1','f1i1v1','g1h1u1',
        'd1h1i1i2i3i4']

C4orT = C4or + ['a1c1z1','a1d1i3',
                'a1f1y1','a1h1i2']


V4or = ['a1','b1','c1','d1','s1','t1','z1',
        'e1','e2','e3','e4']

E4or = ['a1b1c1z1','a1b1c1d1e1e3','a1d1e1e2',
        'c1e1t1','b1d1s1','a1e3',
        'd1e1e2e3e4']

C4or = ['b1c1z1','a1b1c1d1e1e3',
        'c1e1t1','b1d1s1',
        'a1e1e3',
        'd1e1e2e3e4']

C4orT = C4or + ['a1c1z1','a1d1e2']
"""

"""
V4or = ['a1','b1','c1','d1',
        's1','t1','z1',
        'f1','g1','h1','i1',
        'u1','v1','y1',
        'a2','b2','c2','d2',
        's2','t2','z2',
        'f2','g2','h2','i2',
        'u2','v2','y2',
        'a3','b3','c3','d3',
        's3','t3','z3',
        'f3','g3','h3','i3',
        'u3','v3','y3',
        'e1','e2','e3','e4',
        'w','x']

E4or = ['a1b1c1z1','a1b1c1d1e1','a1d1e1e2',
        'b1d1s1','c1e1t1',
        'f1g1h1y1','e1f1g1h1i1','f1i1e1e3',
        'g1e1u1','h1i1v1',

        'a2b2c2z2', 'a2b2c2d2e2', 'a2d2e2e4',
        'b2d2s2', 'c2e2t2',
        'f2g2h2y2', 'e2f2g2h2i2', 'f2i2e2e1',
        'g2e2u2', 'h2i2v2',

        'a3b3c3z3', 'a3b3c3d3e4', 'a3d3e4e3',
        'b3d3s3', 'c3e4t3',
        'f3g3h3y3', 'e4f3g3h3i3', 'f3i3e4e2',
        'g3e4u3', 'h3i3v3',

        'a4b4c4z4', 'a4b4c4d4e3', 'a4d4e3e1',
        'b4d4s4', 'c4e3t4',
        'f4g4h4y4', 'e3f4g4h4i4', 'f4i4e3e4',
        'g4e3u4', 'h4i4v4',

        'd1d2d3d4e1e2e3e4i1i2i3i4'
        #'e2e3w1','e1e4x1'
        ]

C4or = ['b1c1z1','a1b1c1d1e1',
        'b1d1s1','c1e1t1',
        'g1h1y1','e1f1g1h1i1',
        'g1e1u1','h1i1v1',

        'b2c2z2', 'a2b2c2d2e2',
        'b2d2s2', 'c2e2t2',
        'g2h2y2', 'e2f2g2h2i2',
        'g2e2u2', 'h2i2v2',

        'b3c3z3', 'a3b3c3d3e4',
        'b3d3s3', 'c3e4t3',
        'g3h3y3', 'e4f3g3h3i3',
        'g3e4u3', 'h3i3v3',

        'b4c4z4', 'a4b4c4d4e3',
        'b4d4s4', 'c4e3t4',
        'g4h4y4', 'e3f4g4h4i4',
        'g4e3u4', 'h4i4v4',

        #'e2e3w1','e1e4x1',
        'd1d2d3d4e1e2e3e4i1i2i3i4']

C4orT = C4or + ['a1c1z1','f1g1y1',
                'a1d1e2','e3f1i1',

                'a2c2z2', 'f2g2y2',
                'a2d2e4', 'e1f2i2',

                'a3c3z3', 'f3g3y3',
                'a3d3e3', 'e2f3i3',

                'a4c4z4', 'f4g4y4',
                'a4d4e1', 'e4f4i4']

C4orF = C4or + ['a1b1z1','f1h1y1',
                'a2b2z2','f2h2y2',
                'a3b3z3', 'f3h3y3',
                'a4b4z4', 'f4h4y4',

                'a1e1e2','e1e3f1',
                'a2e2e4','e2e1f2',
                'a3e4e3','e4e2f3',
                'a4e3e1','e3e4f4']


V4or = ['a1','b1','c1','d1','e1','f1','g1',
        's1','t1','z1',
        'a2','b2','c2','d2','e2','f2','g2',
        's2','t2','z2',
        'a3','b3','c3','d3','e3','f3','g3',
        's3','t3','z3',
        'a4','b4','c4','d4','e4','f4','g4',
        's4','t4','z4',
        'h1','h2','h3','h4']

E4or = ['a1b1c1d1e1', 'a1b1c1z1', 'a1d1d2d3e1', 'c1e1s1', 'b1d1t1',
        'a2b2c2d2e2', 'a2b2c2z2', 'a2d2d3d4e2', 'c2e2s2', 'b2d2t2',
        'a3b3c3d3e3', 'a3b3c3z3', 'a3d3d4d1e3', 'c3e3s3', 'b3d3t3',
        'a4b4c4d4e4', 'a4b4c4z4', 'a4d4d1d2e4', 'c4e4s4', 'b4d4t4',
        'd1d2d3d4e1e2e3e4',
        'a1b1c1d1e1d2',
        'a2b2c2d2e2d3',
        'a3b3c3d3e3d4',
        'a4b4c4d4e4d1']

C4or = ['b1c1z1', 'c1e1s1', 'b1d1t1',
        'b2c2z2', 'c2e2s2', 'b2d2t2',
        'b3c3z3', 'c3e3s3', 'b3d3t3',
        'b4c4z4', 'c4e4s4', 'b4d4t4',
        'd1d2d3d4e1e2e3e4',
        'a1b1c1d1e1d2',
        'a2b2c2d2e2d3',
        'a3b3c3d3e3d4',
        'a4b4c4d4e4d1']

C4orTTTT = C4or + ['a1b1z1','a1d3d2e1',
                   'a2b2z2','a2d4d3e2',
                   'a3b3z3','a3d1d4e3',
                   'a4b4z4','a4d2d1e4']

C4orTTTF = C4or + ['a1c1z1','a1d1d2d3',
                   'a2b2z2','a2d4d3e2',
                   'a3b3z3','a3d1d4e3',
                   'a4b4z4','a4d2d1e4']



C4orFFFF = C4or + ['a1c1z1','a1d1d2d3',
                   'a2c2z2','a2d2d3d4',
                   'a3c3z3','a3d3d4d1',
                   'a4c4z4','a4d4d1d2']


C4orFFFT = C4or + ['a1b1z1','a1d3d2e1',
                   'a2c2z2','a2d2d3d4',
                   'a3c3z3','a3d3d4d1',
                   'a4c4z4','a4d4d1d2']

C4orFTFT = C4or + ['a1b1z1','a1d3e1','a1d2e1',
                   'a2c2z2','a2d2d3d4',
                   'a3b3z3','a3d1e1','a3d4e3',
                   'a4c4z4','a4d4d1d2']

"""

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
