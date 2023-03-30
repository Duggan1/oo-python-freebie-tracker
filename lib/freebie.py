# from .company import Company

class Freebie:

    all = []

     
    
    def __init__(self, itemName:str, value:int, dev , company):
        self.item_name = itemName 
        self.value = value
        self.dev = dev
        self.company = company
        Freebie.all.append(self)
        # Company.freebies.append(self)

    
    
    def print_details(self):
        return f"{self.dev.name} owns a {self.item_name} from {self.company.name}."