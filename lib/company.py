from .freebie import Freebie

class Company:

    all = []
    # oldyear = 2025
    # if foundingYear < oldyear :
    #         oldyear = foundingYear


    
    
    def __init__(self, name:str, foundingYear:int):
        self.name = name 
        self.foundingYear = foundingYear
        Company.all.append(self)
        
        
    @property
    def freebies(self):
        return [freeB for freeB in Freebie.all if freeB.company == self]

    
    def devs( self ):
        return [ freeB.dev for freeB in self.freebies]
    
    def give_freebie(self, dev, itemName, value):
        Freebie(itemName, value , dev, self)

    @classmethod
    def oldest_company(cls):
        oldGuy = 2025
        for c in Company.all:
            if c.foundingYear < oldGuy:
                oldGuy = c.foundingYear
        return oldGuy
            

        