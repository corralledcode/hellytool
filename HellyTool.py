
import string
import time

def parsecondensed(s):
    P = []
    i = 0
    while i < len(s):
        if s[i] not in string.ascii_letters:
            print('Parse error not alpha: ',s)
            i = i+1
        else:
            sa = s[i]
            sn = ''
            i = i+1
            while i < len(s) and s[i] in string.digits:
                sn = sn+s[i]
                i = i + 1
            P.append(sa+sn)
    return P



def checkrs(V,E,C,verbose=True):

    V = vertexremoveduplicates(V)
    E2 = []
    for e in E:
        E2.append(parsecondensed(e))

    C2 = []
    for c in C:
        C2.append(parsecondensed(c))

    E3 = []
    for e in E2:
        for e1 in e:
            for e2 in e:
                if e1 < e2:
                    if not [e1,e2] in E3:
                        E3.append([e1,e2])


    #print('Ordered edges: ',E3)
    allcovered = True
    for v1 in V:
        for v2 in V:
            if [v1,v2] in E3:
               covered = False
               for c in C2:
                    if v1 in c and v2 in c:
                        covered = True
               if not covered:
                   allcovered = False
                   print('Edge ', v1, ' to ', v2, 'not covered')
               #else:
               #    print('Edge ', v1, ' to ', v2, ' covered')
    if verbose:
        print('All covered: ', allcovered)
    alllegaledges = True
    for c in C2:
        legaledges = True
        illegaledges = []
        for v1 in c:
            for v2 in c:
                if v1 < v2:
                    legaledges = (legaledges and ([v1,v2] in E3))
                    if not [v1,v2] in E3:
                        illegaledges.append(v1+v2)
        if not legaledges:
            print('Illegal edges: ',illegaledges,' in cover: ',c)
            alllegaledges = False
    if not alllegaledges:
        print('All edges legal: ',alllegaledges)
    alltriangle = True
    for v1 in V:
        for v2 in V:
            for v3 in V:
                if v1<v2 and v2<v3:
                    if [v1,v2] in E3 and [v1,v3] in E3 and [v2,v3] in E3:
                        if verbose:
                            print('Triangle ',v1+v2+v3)
                        allmeet = False
                        N = []
                        neighborstext=[]
                        for c in C2:
                            if (v1 in c and v2 in c) or (v1 in c and v3 in c) or (v2 in c and v3 in c):
                                N.append(c)
                        neighborstext = neighborstext + N
                        if verbose:
                            print('neighbors: ',N)
                        meettext = ''
                        for v in V:
                            meet = True
                            for n in N:
                                meet = (meet and (v in n))
                                if not meet: # added
                                    break    # added
                            if meet:
                                meettext = meettext + v
                                #print('Meet ',v,': ',meet)
                                allmeet = True
                        if verbose:
                            print('Meet: ',meettext)
                            print('All meet at triangle ', v1+v2+v3, allmeet)
                        else:
                            if not allmeet:
                                print('Failed at triangle ',v1+v2+v3, ' with meet ',meettext, 'neighbors ',neighborstext)
                        alltriangle = (alltriangle and allmeet)
                #if not alltriangle: #added
                #    break           #added
            #if not alltriangle:     #added
            #    break               #added
        #if not alltriangle:         #added
        #    break                   #added

    print('All triangles met: ', alltriangle)
    return alltriangle

def checkrsquicker(V,E,C,T = [],verbose=True):

    E2 = E
    C2 = C


    E3 = E2

#    if T == []:
#        T = graphfindtriangles(V,E3)

    alltriangle = True
    for t in T:
        #if verbose:
        #    print('Triangle ',v1+v2+v3)
        allmeet = False
        N = []
        #neighborstext=[]
        for c in C2:
            if (t[0] in c and t[1] in c) or (t[1] in c and t[2] in c) or (t[2] in c and t[0] in c):
                N.append(c)
        #neighborstext = neighborstext + N
        #if verbose:
        #    print('neighbors: ',N)
        #meettext = ''

        for v in N[0]: # changed
            meet = True
            for n in range(1,len(N)):
                meet = (meet and (v in N[n]))
                if not meet: # added
                    break    # added
            if meet:
                #meettext = meettext + v
                #print('Meet ',v,': ',meet)
                allmeet = True
                break
        #if verbose:
        #    print('Meet: ',meettext)
        #    print('All meet at triangle ', v1+v2+v3, allmeet)
        #else:
        #    if not allmeet:
        #        print('Failed at triangle ',v1+v2+v3, ' with meet ',meettext, 'neighbors ',neighborstext)
        alltriangle = (alltriangle and allmeet)
        if not alltriangle: #added
            T.remove(t)
            T.insert(0,t)
            break           #added
     #if verbose:
    #    print('All triangles met: ', alltriangle)
    return alltriangle

def checkrsquick(V,E,C,verbose=True):

    V = vertexremoveduplicates(V)
    E2 = []
    for e in E:
        E2.append(parsecondensed(e))

    C2 = []
    for c in C:
        C2.append(parsecondensed(c))

    E3 = []
    for e in E2:
        for e1 in e:
            for e2 in e:
                if e1 < e2:
                    if not [e1,e2] in E3:
                        E3.append([e1,e2])


    #print('Ordered edges: ',E3)
    allcovered = True
    for v1 in V:
        for v2 in V:
            if [v1,v2] in E3:
               covered = False
               for c in C2:
                    if v1 in c and v2 in c:
                        covered = True
               if not covered:
                   allcovered = False
                   print('Edge ', v1, ' to ', v2, 'not covered')
               #else:
               #    print('Edge ', v1, ' to ', v2, ' covered')
    if verbose:
        print('All covered: ', allcovered)
    alllegaledges = True
    for c in C2:
        legaledges = True
        illegaledges = []
        for v1 in c:
            for v2 in c:
                if v1 < v2:
                    legaledges = (legaledges and ([v1,v2] in E3))
                    if not [v1,v2] in E3:
                        illegaledges.append(v1+v2)
        if not legaledges:
            print('Illegal edges: ',illegaledges,' in cover: ',c)
            alllegaledges = False
    if not alllegaledges:
        print('All edges legal: ',alllegaledges)
    alltriangle = True
    for v1 in V:
        for v2 in V:
            for v3 in V:
                if v1<v2 and v2<v3:
                    if [v1,v2] in E3 and [v1,v3] in E3 and [v2,v3] in E3:
                        if verbose:
                            print('Triangle ',v1+v2+v3)
                        allmeet = False
                        N = []
                        neighborstext=[]
                        for c in C2:
                            if (v1 in c and v2 in c) or (v1 in c and v3 in c) or (v2 in c and v3 in c):
                                N.append(c)
                        neighborstext = neighborstext + N
                        if verbose:
                            print('neighbors: ',N)
                        meettext = ''
                        if len(N)>0:
                            for v in N[0]: # changed
                                meet = True
                                for n in N:
                                    meet = (meet and (v in n))
                                    if not meet: # added
                                        break    # added
                                if meet:
                                    meettext = meettext + v
                                    #print('Meet ',v,': ',meet)
                                    allmeet = True
                                    break
                        if verbose:
                            print('Meet: ',meettext)
                            print('All meet at triangle ', v1+v2+v3, allmeet)
                        else:
                            if not allmeet:
                                print('Failed at triangle ',v1+v2+v3, ' with meet ',meettext, 'neighbors ',neighborstext)
                        alltriangle = (alltriangle and allmeet)
                if not alltriangle: #added
                    break           #added
            if not alltriangle:     #added
                break               #added
        if not alltriangle:         #added
            break                   #added
    if verbose:
        print('All triangles met: ', alltriangle)
    return alltriangle

def simplifycover(C,verbose=True):
    Ctemp = C
    inprocess = True
    while inprocess:
        inprocess = False
        for c1 in C:
            for c2 in C:
                c1temp = parsecondensed(c1)
                c2temp = parsecondensed(c2)
                if c1 != c2:
                    all = True
                    for v in c2temp:
                        all = (all and (v in c1temp))
                    if all:
                        Ctemp.remove(c2)
                        if verbose:
                            print('Removed: ',c2,' Covered by: ',c1)
                        inprocess = True

    return Ctemp

def graphfindtriangles(V,E):

    output = []
    for v1 in V:
        for v2 in V:
            for v3 in V:
                if v1<v2 and v2<v3:
                    if [v1,v2] in E and [v1,v3] in E and [v2,v3] in E:
                        output.append([v1,v2,v3])
    return output

def labelappend( V, E, C, d ):
    Vtemp = []
    for v in V:
        v = v + str(d)
        Vtemp = Vtemp + [v]

    Etemp = []
    for e in E:
        temp = ''
        etemp = parsecondensed(e)
        for v in etemp:
            temp = temp + v+str(d)
        Etemp = Etemp + [temp]

    Ctemp = []
    for c in C:
        temp = ''
        ctemp = parsecondensed(c)
        for v in ctemp:
            temp = temp + v + str(d)
        Ctemp = Ctemp + [temp]

    return Vtemp, Etemp, Ctemp

def mergevertex(V,E,C,v1,v2):
    Vtemp = []
    for v in V:
        if v != v1:
            Vtemp = Vtemp + [v]

    Etemp = []
    for e in E:
        etemp = parsecondensed(e)
        while v1 in etemp and v2 in etemp:
            etemp.remove(v2)
        e2temp = ''
        n = 0
        for v in etemp:
            if v == v1:
                e2temp = e2temp + v2
                n = n+1
            else:
                e2temp = e2temp + v
                n = n+1
        Etemp = Etemp + [e2temp]
        if n <= 1:
            print('Edge consisting of only one vertex: ',Etemp)
    Ctemp = []
    for c in C:
        ctemp = parsecondensed(c)
        while v1 in ctemp and v2 in ctemp:
            ctemp.remove(v2)
        c2temp = ''
        n = 0
        for v in ctemp:
            if v == v1:
                c2temp = c2temp + v2
                n=n+1
            else:
                c2temp = c2temp + v
                n=n+1
        Ctemp = Ctemp + [c2temp]
        if n <= 1:
            print('Cover consisting of only one vertex: ', Ctemp)

    return Vtemp,Etemp,Ctemp

def vertexremoveduplicates(V):
    Vtemp = list(set(V))
    return Vtemp

def neighborcount(V,E,v):
    count = 0
    for vtemp in V:
        for e in E:
            if (not v == vtemp) and v in e and vtemp in e:
                count = count + 1
    return count
def findncoversbare( V,E,n):
    allc = [[]]
    if n <= 0:
        return allc
    n = n - 1
    Carray = findncoversbare(V, E, n)
    for c in Carray:
        Vtemp = []
        for v in V:
            Vtemp.append(v) # working list
        cnew = []
        for v in c: # now remove any either not connected or already repped
            cnew.append(v)
            for v2 in V:
                if (v >= v2) and (v2 in Vtemp):
                    Vtemp.remove(v2)
                    continue
                found = False
                for e in E:
                    found = found or (v2 in e and v in e)
                if (not found) and (v2 in Vtemp):
                    Vtemp.remove(v2)
        for v in Vtemp:
            allc.append(cnew + [v])
    if n >= 15:
        print('...finding covers up to depth n=',n)
    return allc

def findncovers(V,E,n):
    E2 = []
    V = vertexremoveduplicates(V)
    for e in E:
        E2.append(parsecondensed(e))
    return findncoversbare(V,E2,n)

def maxcliquesize(V,E):
    maxn = 0
    Vtemp = []
    V = vertexremoveduplicates(V)
    E2 = []
    for e in E:
        E2.append(e)
#        E2.append(parsecondensed(e))
    for v in V:
        n = neighborcount(V,E2,v)
        Vtemp.append([v,n])
        if n > maxn:
            maxn = n

    length = maxn+1
    while length > 0:
        Vtemp2 = []
        for i in range(len(Vtemp)):
            if Vtemp[i][1] >= length-1:
                Vtemp2.append([Vtemp[i][0]])
        if (len(Vtemp2) == 0) or (len(Vtemp2) < length - 1):
            length = length - 1
            continue
        for i in range(2**(len(Vtemp2))):
            count = 0
            for j in range(len(Vtemp2)):
                if ((2**j) & i) > 0:
                    count = count + 1

            if count == length:
                allconnected = True
                for k in range(len(Vtemp2)):
                    for l in range(len(Vtemp2)):
                        if (not k == l) and ((2**k & i) > 0) and ((2**l & i) >0):
                            connected = False
                            for e in E2:
                                connected = connected or ((Vtemp2[k][0] in e) and (Vtemp2[l][0] in e))
                            allconnected = allconnected and connected
                if allconnected:
                    return length
        length = length - 1

    return length

def findrscover(V, E, C = [], verbose = True):

    tic = time.perf_counter()

    Ctemp = []
    for c in C:
        Ctemp.append(parsecondensed(c))

    V = vertexremoveduplicates(V)
    E2 = []
    for e in E:
        E2.append(parsecondensed(e))

    Vtemp = []
    for v in V:
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

    Vtemp = []
    for v in V2: # is every neighbor to v covered by some one covering set
        allcovered = False
        n = neighborcount(V2,E2,v)
        if n == 2:
            temp = [v]
            for e in E2:
                if v in e:
                    for v2 in V2:
                        if (not v == v2) and (v2 in e):
                            temp = temp + [v2]
            print( 'Added triangle cover ',temp)
            if not temp in Ctemp:
                Ctemp.append(temp)
        for c in Ctemp:
            if v in c:
                allcovered = True
                for v2 in V2:
                    for e in E2:
                        if (v in e and v2 in e):
                            allcovered = allcovered and (v2 in c)
        if not allcovered:
            Vtemp.append(v)
        else:
            print( 'Removing vertex ',v)
    V2 = Vtemp
    if len(V2) == 0:
        print( 'Zero vertices remain.')
        return Ctemp


    Ctemp2 = []
    for c in Ctemp:
        found = False
        for v in c:
            found = found or (v in V2)
        if found:
            Ctemp2.append(c)

    E3 = []
    for e in E2:
        for e1 in e:
            for e2 in e:
                if e1 < e2:
                    if not [e1,e2] in E3:
                        E3.append([e1,e2])

    Eoverall = []
    for e in E3:
        Eoverall.append(e)

    Delta = 1
    for v in V2:
        Delta = max(Delta, neighborcount(V2,E3,v))

#    for e in E2:
#        i = 0
#        found = False
#        while not found and i < len(Ctemp):
#            found = (e in Ctemp[i])
#            i = i + 1
#        if not found:
#            for v in e:
#                if not v in V3:
#                    V3.append(v)

    if Delta < 30:
        mcs = maxcliquesize(V2,E3)
    else:
        print( 'Large Delta warning, unlikely to complete in a timely manner: using Delta =', Delta, 'as a guess for max clique size')
        mcs = Delta

    contemp = []

    print('Using max clique size =',mcs,' to reduce the problem of 2**',len(V2),'=',2**len(V2),' subsets of vertices')

    contemp = findncoversbare(V2,E3,mcs)
    T = graphfindtriangles(V, E3)

    """ following code working but commented out to make way for findncovers
    for k in range(2**len(V2)):
        subgraph = []
        count = 0
        for i in range(len(V2)):
            if (k & (2**i)) > 0:
                subgraph.append(V2[i])
                count = count + 1
                if count > mcs:
                    break
        if count > mcs:
            continue

        allconnected = True
        for i in range(len(subgraph)):
            for j in range(i+1,len(subgraph)):
                edgeconnected = False
                for k in E3:
                    edgeconnected = edgeconnected or ((subgraph[i] in k) and (subgraph[j] in k)) #also try with [,] tuple
                allconnected = allconnected and edgeconnected
                if not allconnected:
                    break
            if not allconnected:
                break
        if allconnected:

            allvfound = False
            for c in Ctemp2:
                found = True
                for v in subgraph:
                    found = found and v in c
                allvfound = allvfound or found
            if not allvfound:
                contemp.append(subgraph)


    #tidy up
    """

    contemp2 = []
    for subgraph in contemp:
        allvfound = False
        for c in Ctemp2:
            found = True
            for v in subgraph:
                found = found and v in c
            allvfound = allvfound or found
        if not allvfound:
            contemp2.append(subgraph)
    con = []
    for c in contemp2:
        if len(c) >= 3:
            #temp = ''
            #for k in c:
            #    temp = temp + k
            con.append(c)
#            constr.append(temp)

    rscovers = []
    print(con, len(con),2**len(con))

    for n in range(2**len(con)):
 #       Cstr = []
        C2 = []
        count = 0
        for k in range(len(con)):
            if ((2 ** k) & n) > 0:
                #              Cstr.append(constr[k])
                C2.append(con[k])
            # C2 = simplifycover(C2,verbose)

        for c in Ctemp2:
            C2.append(c)

        #C2 = simplifycover(C2,verbose)


    #    E3 = []
    #    for e in E2:
    #        for e1 in e:
    #            for e2 in e:
    #                if e1 < e2:
    #                    if not [e1, e2] in E3:
    #                        E3.append([e1, e2])

        allcovered = True
        for v1 in V2:
            for v2 in V2:
                if [v1, v2] in E3:
                    covered = False
                    for c in C2:
                        if v1 in c and v2 in c:
                            covered = True
                    if not covered:
                        allcovered = False
                        break
                if not allcovered:
                    break
            if not allcovered:
                break

                    #    print('Edge ', v1, ' to ', v2, 'not covered')
                    # else:
                    #    print('Edge ', v1, ' to ', v2, ' covered')

        if verbose:
            print('All covered: ', allcovered)
        if allcovered:
            if checkrsquicker(Voverall,Eoverall,C2,T,verbose):
                rscovers.append(C2)
    toc = time.perf_counter()
    print('Found', len(rscovers), 'RS-covers:')
    for c in rscovers:
        temp = []
        for c2 in c:
            if not c2 in Ctemp:
                temp.append(c2)
        print('C +', temp)
    print('where C =',Ctemp)
    print(f"Time elapsed {toc - tic:0.4f} seconds")

    return rscovers


#findrscover(['b','a','d','c','a100','a4','d2','c1'],['ab','ac','dc'])
#findrscover(['b','a','d','c','f','z'],['ab','ac','dc','bc','dbc','dfz','abzf'])
#findrscover(['b','a','c'],['ab','ac','bc'],[],True)
#print(maxcliquesize(['b','a','c'],['ab','ac','bc']))

#V=('a','b','c','a2','a23','a','b3','b100','b2','a','b3')
#E=('ab','ba2','aa23','ad','bb3','b100b2','b101b','ba','da2','abca2')
#C=('aba2','aa23d','bb3','b2b100')

#print( mergevertex(V,E,C,'b','a'))
#checkrs(V,E,C)


#print( simplifycover(['abc','abcde','abef','abcdz','dez','bcd','bc','zdxu','zdx']))