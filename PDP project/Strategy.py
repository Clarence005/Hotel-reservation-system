import pickle



class CustomerDiscount:
    def __init__(self, price, discount_strategy):
        self.price = price
        self.discount_strategy = discount_strategy

    def price_after_discount(self):
        if self.discount_strategy:
            discount = self.discount_strategy(self)
        else:
            discount = 0

        return self.price - discount

    def rep(self):
        print("Price: {}, price after discount: {}".format(self.price, self.price_after_discount()))

def Strategy_1(order):
    discount = order.price * 0.10
    return discount

def Strategy_2(order):
    discount = order.price * 0.25
    return discount

def finding_discount(price, us_id):
    with open("C:/Users/user/OneDrive/Documents/PDP project/user.pickle", 'rb') as f1:
        a = pickle.load(f1)
    for i in a:
        if i.id == us_id:
            print(i.count)
            if i.count == 0:
                val = CustomerDiscount(int(price), Strategy_1)
                val1 = val.price_after_discount()
                print(val1)
                return ["10%", val1]
            elif i.count == 4:
                val = CustomerDiscount(int(price), Strategy_2)
                val1 = val.price_after_discount()
                return ["25%", val1]
            else:
                return [0, 0]
