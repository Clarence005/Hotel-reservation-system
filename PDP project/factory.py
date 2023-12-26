# factory
class family:
    def price(self,tb):
        return tb*200

class party:
    def price(self,tb):
        return tb*800

class couple:
    def price(self,tb):
        return tb*100

def factory(types,tb):
    
    if(types == 'family'):
        return family().price(len(tb))
    if(types == 'party'):
        return party().price(len(tb))
    if(types == 'couple'):
        return couple().price(len(tb))
