from factory import factory
from Strategy import finding_discount
from state import SeatContext,UnoccupiedState,OccupiedState,AbstractState
from datetime import datetime

class Facade:
    
    def cal_price(self, t_type, val,us_id):
        price1 = self.price(t_type, val)
        print(1)
        dis = self.discount(price1,us_id)
        print(2,dis) 
        result = []
        result.append(price1)
        result.append(dis[0])
        result.append(dis[1])
        return result
    
    def price(self, t_type, val):
        price = factory(t_type, val)
        return price
    
    def discount(self, price,us_id):
        discount = finding_discount(price,us_id)
        return discount

    def change_state(self,table_no,timing,t_type,date):
        val = []
        for i in table_no:
            val.append(int(i))
        print(val,date)
        parsed_date = datetime.strptime(date, "%Y-%m-%d")

        # Format the parsed date using the output format
        date_input = parsed_date.strftime("%m-%d-%Y")
        # Example usage:
        seat_context = SeatContext()
        unoccupied_state = UnoccupiedState()
        occupied_state = OccupiedState()
        seat_context.set_state(unoccupied_state)
        print(timing,val,t_type,date_input)
        if(t_type == 'family'):
            seat_context.book_seats(date_input,timing,"Family",val)
            seat_context.save_changes()
        if(t_type == 'couple'):
            seat_context.book_seats(date_input,timing,"Couple",val)
            seat_context.save_changes()
        if(t_type == 'party'):
            seat_context.book_seats(date_input,timing,"Party",val)
            seat_context.save_changes()
        # Save changes to the data file


