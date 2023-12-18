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
    table = tb.split()
    if(types == 'family'):
        return family().price(len(table))
    if(types == 'Party'):
        return party().price(len(table))
    if(types == 'couple'):
        return couple().price(len(table))
