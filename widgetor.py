from HellyTool import checkrs

V = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','q','r','s','t']
E = ['af','ae','ah','ef','ej','fh',
     'be','bg','bd','dg','de','eg'
     'cg','ch','ci','gh','gi','hi',
     'df','dh','di','dk','dj','dl','dm','dn','dq',
     'ei','eh','ej','ek','el','em','en',
     'fg','fh','fi','fj','fk','fl','fm','fn','ft',
     'gk','gj','gl','gm','gn',
     'hj','hk','hl','hm','hn',
     'ij','ik','il','im','in','is','it'
     'jk','jl','jm','jn','jq',
     'kl','km','kn','kr',
     'lm','ln',
     'mn','ms',
     'nr']

C = ['aef','bed','cgi','defghijklmn','fit','djq','knr','sim',]
CFF = ['aef','bed','cgi','defghijklmn','fit','djq','knr','sim',
       'aeh','beg','chi','gjl','lnh']
CTF = ['aef','bed','cgi','defghijklmn','fit','djq','knr','sim',
       'afh','beg','cgh','gjl','lnh']
CFT = ['aef','bed','cgi','defghijklmn','fit','djq','knr','sim',
       'aeh','bdg','cgh','gkl','lmh']
CTT = ['aef','bed','cgi','defghijklmn','fit','djq','knr','sim',
       'afh','bdg','cgh','gkl','lmh']

checkrs( V,E,CFT)
