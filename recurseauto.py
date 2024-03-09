import string

from HellyTool import checkrs
from HellyTool import checkrsquick
from HellyTool import parsecondensed
from widgetvariable import Vvar
from widgetvariable import Evar
from widgetvariable import Cvar
from widgetvariable import CvarT
from widgetvariable import CvarF
from HellyTool import simplifycover
from HellyTool import labelappend
from HellyTool import mergevertex
from HellyTool import findrscover
from HellyTool import graphfindtriangles
from HellyTool import checkrsquicker
from HellyTool import vertexremoveduplicates
from check3SAT import numberofvariables, drawtruthtable, directsatcompute, labelbufferlength
import time


V = ['a1','b1','c1','z',
     'a2','b2','c2',
     't2','s2']

E = ['a1b1c1z',
     'a2b2c2z',
     'b1c1b2c2z',
     't2b1b2',
     's2c1c2']

C = ['b1c1b2c2z',
     'a1b1c1',
     'a2b2c2',
     't2b1b2',
     's2c1c2']

CT = C + ['a1b1z', 'a2c2z']

CF = C + ['a1c1z', 'a2b2z']

#checkrs(V,E,C)


def recurse(Vn,En,Cn,V,E,C,n):
     Vnstemp = Vn + ['w'+str(n).zfill(labelbufferlength), 'y'+str(n).zfill(labelbufferlength)]
     Vns = []
     for v in Vnstemp:
          if v != 'z':
               Vns = Vns + [v]
     Vns = Vns + ['a'+str(n).zfill(labelbufferlength)]
     Vns = Vns + ['b' + str(n).zfill(labelbufferlength)]
     Vns = Vns + ['c' + str(n).zfill(labelbufferlength)]
     Vns = Vns + ['z']

     #print('Vns: ',Vns)

     Bns = []
     Dns = []
     Ens = []
     for e in En:
         Ens.append(e)

     for i in range(1,n+1):
          Bns = Bns + ['b'+str(i).zfill(labelbufferlength)]
          Dns = Dns + ['c'+str(i).zfill(labelbufferlength)]

     q = ''
     Q = []
     for bi in Bns:
          q = q + bi
          Q = Q + [bi]
     for cj in Dns:
          q = q + cj
          Q = Q + [cj]
     q = q + 'z'
     Q = Q + ['z']

     Cns = []
     for c in C:
          Ctemp = ''
          ctemp = parsecondensed(c)
          for v in ctemp:
               if v == 'a':
                    Ctemp = Ctemp+'a'+str(n).zfill(labelbufferlength)
               else:
                    if v == 'b':
                         Ctemp = Ctemp+'b'+str(n).zfill(labelbufferlength)
                    else:
                         if v == 'c':
                              Ctemp = Ctemp+'c'+str(n).zfill(labelbufferlength)
                         else:
                              Ctemp = Ctemp + v
          Cns = Cns + [Ctemp]

     for c in Cn:
          ctemp = parsecondensed(c)
          all = True
          for v in ctemp:
               all = all and (v in Q)
          if not all:
               Cns = Cns + [c]

     for e in E:
          Etemp = ''
          etemp = parsecondensed(e)
          for v in etemp:
               if v == 'a':
                    Etemp = Etemp+'a'+str(n).zfill(labelbufferlength)
               else:
                    if v == 'b':
                         Etemp = Etemp+'b'+str(n).zfill(labelbufferlength)
                    else:
                         if v == 'c':
                              Etemp = Etemp + 'c' + str(n).zfill(labelbufferlength)
                         else:
                              Etemp = Etemp + v
          Ens = Ens + [Etemp]

     for e in Cn:
          etemp = parsecondensed(e)
          all = True
          for v in etemp:
              all = all and (v in q)
          if not all:
              Ens = Ens + [e]

     Cns = Cns + [q]
     Ens = Ens + [q]

     Cns = Cns + ['w'+str(n).zfill(labelbufferlength)+'c' + str(1).zfill(labelbufferlength) +'c'+str(n).zfill(labelbufferlength),
                  'y'+str(n).zfill(labelbufferlength)+'b' + str(1).zfill(labelbufferlength) +'b'+str(n).zfill(labelbufferlength)]
     Ens = Ens + ['w'+str(n).zfill(labelbufferlength)+'c' + str(1).zfill(labelbufferlength) +'c'+str(n).zfill(labelbufferlength),
                  'y'+str(n).zfill(labelbufferlength)+'b' + str(1).zfill(labelbufferlength) +'b'+str(n).zfill(labelbufferlength)]

     return Vns,Ens,Cns


V = [Vvar,Vvar]
E = [Evar,Evar]

C = [CvarF,CvarT]

for k in [0,1]:
    for n in range(3,5):
         V[k], E[k], C[k] = recurse( V[k], E[k], C[k],['a','b','c','z'], ['abcz'],['abc',['abz','acz'][k]], n)

VNot = [Vvar,Vvar]
ENot = [Evar,Evar]

CNot = [CvarT,CvarF]

for k in [0,1]:
    for n in range(3,5):
         VNot[k], ENot[k], CNot[k] = recurse( VNot[k], ENot[k], CNot[k],['a','b','c','z'], ['abcz'],['abc',['acz','abz'][k]], n)

def build3or(i1,i2,i3,var1,var2,var3):
    a1 = 'a' + i1.zfill(labelbufferlength) + var1.zfill(labelbufferlength)
    b1 = 'b' + i1.zfill(labelbufferlength) + var1.zfill(labelbufferlength)
    c1 = 'c' + i1.zfill(labelbufferlength) + var1.zfill(labelbufferlength)
    a2 = 'a' + i2.zfill(labelbufferlength) + var2.zfill(labelbufferlength)
    b2 = 'b' + i2.zfill(labelbufferlength) + var2.zfill(labelbufferlength)
    c2 = 'c' + i2.zfill(labelbufferlength) + var2.zfill(labelbufferlength)
    a3 = 'a' + i3.zfill(labelbufferlength) + var3.zfill(labelbufferlength)
    b3 = 'b' + i3.zfill(labelbufferlength) + var3.zfill(labelbufferlength)
    c3 = 'c' + i3.zfill(labelbufferlength) + var3.zfill(labelbufferlength)
    z1 = 'z' + var1.zfill(labelbufferlength)
    z2 = 'z' + var2.zfill(labelbufferlength)
    z3 = 'z' + var3.zfill(labelbufferlength)
    d1 = 'd' + i1.zfill(labelbufferlength) + var1.zfill(labelbufferlength)
    e1 = 'e' + i1.zfill(labelbufferlength) + var1.zfill(labelbufferlength)
    d2 = 'd' + i2.zfill(labelbufferlength) + var2.zfill(labelbufferlength)
    e2 = 'e' + i2.zfill(labelbufferlength) + var2.zfill(labelbufferlength)
    d3 = 'd' + i3.zfill(labelbufferlength) + var3.zfill(labelbufferlength)
    e3 = 'e' + i3.zfill(labelbufferlength) + var3.zfill(labelbufferlength)

    q1 = 'u' + i1.zfill(labelbufferlength) + var1.zfill(labelbufferlength)
    r1 = 'v' + i1.zfill(labelbufferlength) + var1.zfill(labelbufferlength)
    q2 = 'u' + i2.zfill(labelbufferlength) + var2.zfill(labelbufferlength)
    r2 = 'v' + i2.zfill(labelbufferlength) + var2.zfill(labelbufferlength)
    q3 = 'u' + i3.zfill(labelbufferlength) + var3.zfill(labelbufferlength)
    r3 = 'v' + i3.zfill(labelbufferlength) + var3.zfill(labelbufferlength)

    V3ortemp = [d1,d2,d3,e1,e2,e3,q1,q2,q3,r1,r2,r3]
    E3ortemp = [a1+b1+c1+d1+e1, a2+b2+c2+d2+e2, a3+b3+c3+d3+e3,
                a1+d1+e1+e3, a2+d2+e1+e2, a3+d3+e2+e3,
                d1 + d2 + d3 + e1 + e2 + e3,
                b1+q1+d1,
                b2+q2+d2,
                b3+q3+d3,
                c1+r1+e1,
                c2+r2+e2,
                c3+r3+e3]

    C3ortemp = [a1+b1+c1+d1+e1,a2+b2+c2+d2+e2,a3+b3+c3+d3+e3,
                  b1+q1+d1,
                  b2+q2+d2,
                  b3+q3+d3,
                  c1+r1+e1,
                  c2+r2+e2,
                  c3+r3+e3,
                d1+d2+d3+e1+e2+e3]

    C3orVtemp = []
    for b3temp in [0,1]:
        for b2temp in [0,1]:
            for b1temp in [0,1]:
                C3orVtemp = C3orVtemp + [C3ortemp + [a1+[b1,c1][b1temp] +z1, a2+[b2,c2][b2temp] + z2, a3+ [b3,c3][b3temp] +z3] +
                                         [a1+[e1,d1][b1temp] +e3, a2+[e2,d2][b2temp] + e1, a3+ [e3,d3][b3temp] +e2]]

    return V3ortemp, E3ortemp, C3orVtemp

def build3sat( Terms ):
    Termstemp = []
    biggest = 0
    j=0
    for c in Terms:
        vartemp = []
        negtemp = []
        for l in c:
            ntemp = ''
            if l[0] in string.digits:
                ntemp = ntemp + '+'
                v = l
            else:
                if not l[0] in ['+','-']:
                    print('Illegal format: ', l)
                v = ''
                ntemp = ntemp + l[0]
                for i in range(1,len(l)):
                    v = v + l[i]
            v = str(int(v)).zfill(labelbufferlength)
            biggest = int(v) if int(v) > biggest else biggest
            vartemp = vartemp + [v]
            negtemp = negtemp + [ntemp]
        Termstemp = Termstemp + [[vartemp,negtemp]]
        j = j + 1

    V = [Vvar, Vvar]
    E = [Evar, Evar]

    C = [CvarF, CvarT]

    varnum = biggest + 2 if biggest > j else j + 2
    for k in [0, 1]:
        for n in range(3, varnum):
            V[k], E[k], C[k] = recurse(V[k], E[k], C[k], ['a', 'b', 'c', 'z'], ['abcz'], ['abc', ['abz', 'acz'][k]], n)

    VNot = [Vvar, Vvar]
    ENot = [Evar, Evar]

    CNot = [CvarT, CvarF]

    for k in [0, 1]:
        for n in range(3, varnum):
            VNot[k], ENot[k], CNot[k] = recurse(VNot[k], ENot[k], CNot[k], ['a', 'b', 'c', 'z'], ['abcz'],
                                                ['abc', ['acz', 'abz'][k]], n)

    Vmaster3or = [[]]
    Emaster3or = [[]]
    Cmaster3or = [[]]
    for m in range(j):
        M0 = str(int(Termstemp[m][0][0])).zfill(labelbufferlength)
        M0Not = str(int(Termstemp[m][0][0])+biggest).zfill(labelbufferlength)
        l0 = M0 if Termstemp[m][1][0] == '+' else M0Not
        M1 = str(int(Termstemp[m][0][1])).zfill(labelbufferlength)
        M1Not = str(int(Termstemp[m][0][1])+biggest).zfill(labelbufferlength)
        l1 = M1 if Termstemp[m][1][1] == '+' else M1Not
        M2 = str(int(Termstemp[m][0][2])).zfill(labelbufferlength)
        M2Not = str(int(Termstemp[m][0][2])+biggest).zfill(labelbufferlength)
        l2 = M2 if Termstemp[m][1][2] == '+' else M2Not

        Vmaster3or = Vmaster3or + [[]]
        Emaster3or = Emaster3or + [[]]
        Cmaster3or = Cmaster3or + [[]]

        Vmaster3or[m],Emaster3or[m],Cmaster3or[m] = build3or(str(m+2).zfill(labelbufferlength),str(m+2).zfill(labelbufferlength),str(m+2).zfill(labelbufferlength),l0,l1,l2)

    r=[]
    for b in range(2**biggest):
        Vtemp = [[]]
        Etemp = [[]]
        Ctemp = [[]]
        VNottemp = [[]]
        ENottemp = [[]]
        CNottemp = [[]]
        VP = [[]]
        EP = [[]]
        CP = [[]]
        Vmaster = []
        Emaster = []
        Cmaster = []
        for n in range(biggest):
            bit = (b >> n) & 1
            Vtemp = Vtemp + [[]]
            Etemp = Etemp + [[]]
            Ctemp = Ctemp + [[]]
            VP = VP + [[]]
            EP = EP + [[]]
            CP = CP + [[]]
            N = str(n+1).zfill(labelbufferlength)
            Vtemp[n], Etemp[n], Ctemp[n] = labelappend(V[bit], E[bit], C[bit], N)

            VNottemp = VNottemp + [[]]
            ENottemp = ENottemp + [[]]
            CNottemp = CNottemp + [[]]
            NNot = str(n+1+biggest).zfill(labelbufferlength)
            VNottemp[n], ENottemp[n], CNottemp[n] = labelappend(VNot[bit], ENot[bit], CNot[bit], NNot )

            w1 = 'w' + N
            x1 = 'x' + N
            VP[n] = Vtemp[n] + VNottemp[n] + [w1, x1]
            a1 = 'a' + str(1).zfill(labelbufferlength) + N
            a1n = 'a' + str(1).zfill(labelbufferlength) + NNot
            b1 = 'b' + str(1).zfill(labelbufferlength) + N
            b1n = 'b' + str(1).zfill(labelbufferlength) + NNot
            c1 = 'c' + str(1).zfill(labelbufferlength) + N
            c1n = 'c' + str(1).zfill(labelbufferlength) + NNot

            EP[n] = Etemp[n] + ENottemp[n] + [b1+w1+b1n, c1+x1+c1n, b1+c1+b1n+c1n+a1]
            CP[n] = Ctemp[n] + CNottemp[n] + [b1+w1+b1n, c1+x1+c1n, b1+c1+b1n+c1n+a1]
            VP[n], EP[n], CP[n] = mergevertex(VP[n], EP[n], CP[n], a1n, a1)

            Vmaster = Vmaster + VP[n]
            Emaster = Emaster + EP[n]
            Cmaster = Cmaster + CP[n]

        for m in range(j):
            bt = 0
            if Termstemp[m][1][0] == '+':
                bt = bt + 1 * (b >> (int(Termstemp[m][0][0])-1) & 1)
            if Termstemp[m][1][1] == '+':
                bt = bt + 2 * (b >> (int(Termstemp[m][0][1])-1) & 1)
            if Termstemp[m][1][2] == '+':
                bt = bt + 4 * (b >> (int(Termstemp[m][0][2])-1) & 1)
            if Termstemp[m][1][0] == '-':
                bt = bt + 1 * (1 - (b >> (int(Termstemp[m][0][0])-1) & 1))
            if Termstemp[m][1][1] == '-':
                bt = bt + 2 * (1 - (b >> (int(Termstemp[m][0][1])-1) & 1))
            if Termstemp[m][1][2] == '-':
                bt = bt + 4 * (1 - (b >> (int(Termstemp[m][0][2])-1) & 1))


            Cmaster = (Cmaster + Cmaster3or[m][bt])
            Vmaster = Vmaster + Vmaster3or[m]
            Emaster = Emaster + Emaster3or[m]

        Cmaster = simplifycover(Cmaster, False)

        print('3SAT case: ', "{0:b}".format(b).zfill(biggest) )

        tic = time.perf_counter()


        """ a first effort to switch to checkrsquicker
        T = graphfindtriangles(Vmaster,Emaster,False)

        V = vertexremoveduplicates(Vmaster)
        E2 = []
        for e in Emaster:
            E2.append(parsecondensed(e))

        Vtemp = []
        for v in Vmaster:
            Vtemp.append(v)

        V2 = []
        while len(Vtemp) > 0:
            minv = Vtemp[0]
            for v in Vtemp:
                if v < minv:
                    minv = v
                    changed = True
            V2 = V2 + [minv]
            Vtemp.remove(minv)

        Voverall = []
        for v in V2:
            Voverall.append(v)

        E3 = []
        for e in E2:
            for e1 in e:
                for e2 in e:
                    if e1 < e2:
                        if not [e1, e2] in E3:
                            E3.append([e1, e2])

        Ctemp = []
        for c in Cmaster:
            Ctemp.append(parsecondensed(c))

        Ctemp2 = []
        for c in Ctemp:
            found = False
            for v in c:
                found = found or (v in V2)
            if found:
                Ctemp2.append(c)

        Coverall = Ctemp2
        Eoverall = []
        for e in E3:
            Eoverall.append(e)
        """

        r = r + [checkrsquick(Vmaster, Emaster, Cmaster, False)]
        toc = time.perf_counter()
        print(f"Checked the RS-cover in {toc - tic:0.4f} seconds")

    return r

tic2 = time.perf_counter()



#V = []
#E = []
#C = []
#V,E,C = recurse(Vvar,Evar,Cvar,['a','b','c','z'],['abcz'],['abc'],3)
#C = C + ['a01b01z','a02c02z']
#print(Vvar, Evar, Cvar, V,E,C)
#checkrs(V,E,C)
#findrscover(V,E,C,False)
def main():

    satproblem = [['+1','+2','-3'],['2','3','4'],['1','-2','-3'],['2','4','-5'],['3','-4','5'],['2','-3','6'],['3','5','6']] # runs in 2105 post concurrency code  on NUC12

    #satproblem = [['+1','+2','+3'],['-1','-2','+3'],['1','2','-3'],['1','2','-4'],['3','4','5'],['2','-3','5']] # runs in 7271 seconds ( 7419.6 seconds under failed multiprocess effort) on NUC12
    #satproblem = [['+1','+2','+3'],['-1','-2','+3'],['1','2','-3'],['1','2','-4']] # runs in 447.8 seconds (was 496.14 seconds ... 560 seconds under failed multiprocess effort) on NUC12

    #satproblem = [['+1','+2','+3'],['-1','-2','+3'],['1','2','-3']] # runs in 30.5 to 32.3 seconds (was 39.5 under failed multiprocess effort) seconds on NUC12
    n = numberofvariables(satproblem)
    r = build3sat(satproblem)
    rcomp = []
    match = True
    for b in range(2**n):
        rcomp = rcomp + [directsatcompute(satproblem,b)]
        match = match and (r[b] == directsatcompute(satproblem,b))
    drawtruthtable(range(2**n),r)
    drawtruthtable(range(2**n),rcomp)
    print('Match: ', match)

    toc2 = time.perf_counter()
    print(f"Checked the 3SAT instance in {toc2 - tic2:0.4f} seconds")

if __name__ == '__main__':
    main()
"""

The following code has been automated in the form of the above "build3sat" function.

Vmaster3or1, Emaster3or1, Cmaster3or1 = build3or('2', '2', '2', '01','02','03') #V1 V2 V3

Vmaster3or2, Emaster3or2, Cmaster3or2 = build3or( '3','3','3','06','07','03') #-V1 -V2 V3
Vmaster3or3, Emaster3or3, Cmaster3or3 = build3or( '3','3','2','01','02','08') #V1 V2 -V3
Vmaster3or4, Emaster3or4, Cmaster3or4 = build3or( '4','4','2','01','02','09') #V1 V2 -V4
Vmaster3or5, Emaster3or5, Cmaster3or5 = build3or( '3','2','2','03','04','05') #V3 V4 V5

tic2 = time.perf_counter()
for b1 in [0,1]:
    for b2 in [0,1]:
        for b3 in [0,1]:
            for b4 in [0,1]:
                for b5 in [0,1]:
                    bnot1 = 1-b1
                    bnot2 = 1-b2
                    bnot3 = 1-b3
                    bnot4 = 1-b4
                    bnot5 = 1-b5
                    V1, E1, C1 = labelappend(V[b1], E[b1], C[b1], '01')
                    V2, E2, C2 = labelappend(V[b2], E[b2], C[b2], '02')
                    V3, E3, C3 = labelappend(V[b3], E[b3], C[b3], '03')
                    V4, E4, C4 = labelappend(V[b4], E[b4], C[b4], '04')
                    V5, E5, C5 = labelappend(V[b5], E[b5], C[b5], '05')
                    V1Not, E1Not, C1Not = labelappend(VNot[b1], ENot[b1], CNot[b1],'06')
                    V2Not, E2Not, C2Not = labelappend(VNot[b2], ENot[b2], CNot[b2],'07')
                    V3Not, E3Not, C3Not = labelappend(VNot[b3], ENot[b3], CNot[b3],'08')
                    V4Not, E4Not, C4Not = labelappend(VNot[b4], ENot[b4], CNot[b4],'09')
                    V5Not, E5Not, C5Not = labelappend(VNot[b5], ENot[b5], CNot[b5], '10')

                    VP1 = V1 + V1Not + ['w1','x1']
                    EP1 = E1 + E1Not + ['b101w1b106','c101x1c106','b101c101b106c106a101']
                    CP1 = C1 + C1Not + ['b101w1b106','c101x1c106','b101c101b106c106a101']
                    VP1, EP1, CP1 = mergevertex(VP1,EP1,CP1,'a106','a101')

                    VP2 = V2 + V2Not + ['w2','x2']
                    EP2 = E2 + E2Not + ['b102w2b107','c102x2c107','b102c102b107c107a102']
                    CP2 = C2 + C2Not + ['b102w2b107','c102x2c107','b102c102b107c107a102']
                    VP2, EP2, CP2 = mergevertex(VP2,EP2,CP2,'a107','a102')

                    VP3 = V3 + V3Not + ['w3','x3']
                    EP3 = E3 + E3Not + ['b103w3b108','c103x3c108','b103c103b108c108a103']
                    CP3 = C3 + C3Not + ['b103w3b108','c103x3c108','b103c103b108c108a103']
                    VP3, EP3, CP3 = mergevertex(VP3,EP3,CP3,'a108','a103')

                    VP4 = V4 + V4Not + ['w4','x4']
                    EP4 = E4 + E4Not + ['b104w4b109','c104x4c109','b104c104b109c109a104']
                    CP4 = C4 + C4Not + ['b104w4b109','c104x4c109','b104c104b109c109a104']
                    VP4, EP4, CP4 = mergevertex(VP4,EP4,CP4,'a109','a104')

                    VP5 = V5 + V5Not + ['w5','x5']
                    EP5 = E5 + E5Not + ['b105w5b110','c105x5c110','b105c105b110c110a105']
                    CP5 = C5 + C5Not + ['b105w5b110','c105x5c110','b105c105b110c110a105']
                    VP5, EP5, CP5 = mergevertex(VP5,EP5,CP5,'a110','a105')

                    Vmaster = VP1 + VP2 + VP3 + VP4 + VP5
                    Emaster = EP1 + EP2 + EP3 + EP4 + EP5
                    Cmaster = CP1 + CP2 + CP3 + CP4 + CP5

                    Vmaster = Vmaster + Vmaster3or1 + Vmaster3or2 + Vmaster3or3 + Vmaster3or4 + Vmaster3or5
                    Emaster = Emaster + Emaster3or1 + Emaster3or2 + Emaster3or3 + Emaster3or4 + Emaster3or5

                    Cmaster = (Cmaster + Cmaster3or1[4*b1 + 2*b2 + b3] #V1 V2 V3
                               + Cmaster3or2[4*bnot1 + 2*bnot2 + b3]   #-V1 -V2 v3
                               + Cmaster3or3[4*b1 + 2*b2 + bnot3]      #V1 V2 -V3
                               + Cmaster3or4[4*b1 + 2*b2 + bnot4]      #V1 V2 -V4
                               + Cmaster3or5[4*b3 + 2*b4 + b5])        #V3 V4 V5
                    Cmaster = simplifycover(Cmaster, False)
                    print('3-way OR case: ',b1,b2,b3,b4,b5)

                    tic = time.perf_counter()
                    checkrsquick(Vmaster,Emaster,Cmaster, False)
                    toc = time.perf_counter()
                    print(f"Checked the RS-cover quick in {toc - tic:0.4f} seconds")

#                    tic = time.perf_counter()
#                    checkrs(Vmaster,Emaster,Cmaster, False)
#                    toc = time.perf_counter()
#                    print(f"Checked the RS-cover in {toc - tic:0.4f} seconds")

toc2 = time.perf_counter()
print(f"Checked the five variable possibilities in {toc2 - tic2:0.4f} seconds")


"""