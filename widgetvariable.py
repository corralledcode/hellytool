from HellyTool import checkrs
from HellyTool import findrscover

Vvar = ['a01','b01','c01','a02','b02','c02','z',
        'q01','q02','s02','t02']
Evar = ['a01b01c01z','a02b02c02z',
        'b01c01b02c02z',
        'b01c01q01','b02c02q02',
        'b01b02t02','c01c02s02']
Cvar = ['b01c01b02c02z', 'a01b01c01', 'a02b02c02',
        'b01c01q01','b02c02q02',
        'b01b02t02','c01c02s02']

CvarT = Cvar + ['a01b01z','a02c02z']
CvarF = Cvar + ['a01c01z','a02b02z']
CvarFx = Cvar + ['a01c01z','a02c02z']

#checkrs(Vvar,Evar,CvarF)

findrscover(Vvar,Evar,['b01c01b02c02z'],False)