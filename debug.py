import ipdb

from lib import *

dev1 = Dev("adm")
peanut = Dev("peanut")
chicken = Dev("chicken")


ft = Company("flat iron", 1970)
apple = Company("apple", 1570)


beer =Freebie("beer", 29, dev1, ft)
ic = Freebie("ice cream", 5, dev1, ft)



ipdb.set_trace()