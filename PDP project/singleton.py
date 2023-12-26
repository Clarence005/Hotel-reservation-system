import pickle
#Singleton pattern
class user:
    def __init__(self,u_id,u_name,password,email,ph_no):
        self.id = u_id
        self.name = u_name
        self.password = password
        self.email = email
        self.phone = ph_no
        self.orders = []
        self.count = 0

class owner:
    def __init__(self,u_id,u_name,password,email,ph_no):
        self.id = u_id
        self.name = u_name
        self.password = password
        self.email = email
        self.phone = ph_no
        self.orders = []

class Orders:
    def __init__(self,us_id,table_no,timing,t_type,date):
        self.id = us_id
        self.tb_no = table_no
        self.timing = timing
        self.t_type = t_type
        self.date = date



#Singleton pattern        
class Picklestorage:
    __instance = None
    @staticmethod
    def check():
        if(Picklestorage.__instance == None):
            Picklestorage()
        return Picklestorage.__instance
    
    def __init__(self):
        if(Picklestorage.__instance!= None):
            raise "Already a connectivity exist"
        else:
            self.users_file = "C:/Users/user/OneDrive/Documents/PDP project/user.pickle"
            self.owner_file = "C:/Users/user/OneDrive/Documents/PDP project/owner.pickle"
            self.tables_file = 'tables.pickle'
            Picklestorage.__instance = self
            
        
    def read_pickle_file(self, file_path):
        with open(file_path, 'rb') as file:
            data = pickle.load(file)
        return data

    def store_user(self,obj):
        val = self.read_pickle_file(self.users_file)
        val.append(obj)
        with open(self.users_file,'wb') as f1:
            pickle.dump(val,f1)
        # else:
        # value = []
        # with open(self.users_file,'wb') as f2:
        #     pickle.dump(value,f2)
    
    def store_owner(self,obj):
        val = self.read_pickle_file(self.owner_file)
        val.append(obj)
        with open(self.owner_file,'wb') as f1:
            pickle.dump(val,f1)
        # else:
        # value = []
        # with open(self.owner_file,'wb') as f2:
        #     pickle.dump(value,f2)




# u1=user("s","am","ue","l","s")
# p = Picklestorage()
# p.store_user(u1)
# o1=owner("s","am","ue","l","s")
# p = Picklestorage()
# p.store_owner(o1)