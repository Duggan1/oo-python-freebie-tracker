from .freebie import Freebie

class Dev:
    
    def __init__(self, name:str):
        self.name = name
        # self.freebies = []

    @property
    def freebies(self):
        return [freeB for freeB in Freebie.all if freeB.dev == self]

    @property
    def companies(self):
        return [ freeB.company for freeB in self.freebies]
    

    @property
    def inl(self):
        return [freeB.item_name for freeB in Freebie.all if freeB.dev == self]

    def received_one(self,item_name):
        return item_name in self.inl
    
    def give_away(self, dev, freebie):
        if freebie in self.freebies:
            freebie.dev = dev

        else:
            print("not yours and or not free")

