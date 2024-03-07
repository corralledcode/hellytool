import string

labelbufferlength = 2

def drawtruthtable(B,R):
    biggest = 0
    for b in B:
        if b > 2**biggest:
            biggest = biggest + 1
    for b in B:
        print( "{0:b}".format(b).zfill(biggest), ' ', R[b])

def numberofvariables ( Terms ):
    Termstemp = []
    biggest = 0
    j=0
    for c in Terms:
        for l in c:
            ntemp = ''
            if l[0] in string.digits:
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

    return biggest


def directsatcompute( Terms, Input ):
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
    r2 = True
    for c in Termstemp:
        r = False
        ct = c[0]
        cn = c[1]
        for n in range(len(ct)):
            lt = [False,True] if cn[n]=='+' else [True,False]
            r = r or (lt[(Input >> (int(ct[n])-1)) & 1])
            #r = r or (lt[Input & 2**(int(ct[n])-1) > 0])
        r2 = r2 and r

    return r2
