import json
from datetime import datetime
class SeatContext:
    def __init__(self, data_file="date.json"):
        with open(data_file, 'r') as file:
            self.data = json.load(file)
        self.state = UnoccupiedState()

    def set_state(self, state):
        self.state = state

    def book_seats(self, date, timing, table_type, table_numbers):
        self.state.book_seats(self.data, date, timing, table_type, table_numbers)

    def save_changes(self, data_file="date.json"):
        with open(data_file, 'w') as file:
            json.dump(self.data, file, indent=2)

class AbstractState:
    def book_seats(self, data, date, timing, table_type, table_numbers):
        raise NotImplementedError

class UnoccupiedState(AbstractState):
    def book_seats(self, data, date, timing, table_type, table_numbers):
        for entry in data:
            if entry["date"] == date and entry["timing"] == timing:
                index = entry["table_type"].index(table_type)
                if "occupied" not in entry:
                    entry["occupied"] = []
                for num in table_numbers:
                    if num in entry["table_number"][index]:
                        entry["table_number"][index].remove(num)
                        entry["occupied"].append(num)

class OccupiedState(AbstractState):
    def book_seats(self, data, date, timing, table_type, table_numbers):
        # Add logic for booking seats in the occupied state
        pass

# # Example usage:
# seat_context = SeatContext()
# unoccupied_state = UnoccupiedState()
# occupied_state = OccupiedState()

# # Set the initial state to UnoccupiedState
# seat_context.set_state(unoccupied_state)

# # Example inputs
# parsed_date = datetime.strptime("2023-12-27", "%Y-%m-%d")
# # Format the parsed date using the output format
# date_input = parsed_date.strftime("%m-%d-%Y")
# timing_input = "Breakfast"
# table_type_input = "Family"
# table_numbers_input = [1,2]

# # Book seats based on the input
# seat_context.book_seats(date_input, timing_input, table_type_input, table_numbers_input)

# # # Save changes to the data file
# seat_context.save_changes()
