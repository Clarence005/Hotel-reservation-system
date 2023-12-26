#Observer pattern
import pickle
from singleton import user,owner,Orders
class Book:

    def __init__(self):
        with open( "C:/Users/user/OneDrive/Documents/PDP project/user.pickle", 'rb') as file:
            self.users = pickle.load(file)
        with open( "C:/Users/user/OneDrive/Documents/PDP project/owner.pickle", 'rb') as file1:
            self.owner = pickle.load(file1)
    
    def upd_orders(self,obj1):
        val = self.users
        for i in val:
            if(i.id == obj1.id):
                i.orders.append(obj1)
                i.count +=1
                print(i.count)
        with open( "C:/Users/user/OneDrive/Documents/PDP project/user.pickle",'wb') as f1:
            pickle.dump(val,f1)
    
    def up_owners(self,obj1):
        val = self.owner
        for i in val:
            i.orders.append(obj1)
                
        with open( "C:/Users/user/OneDrive/Documents/PDP project/owner.pickle",'wb') as f1:
            pickle.dump(val,f1)