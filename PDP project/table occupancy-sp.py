import json
from datetime import datetime

# State interface
class TableState:
    def get_state(self):
        pass

    def change_state(self):
        pass

# Concrete states
class UnoccupiedState(TableState):
    def get_state(self):
        return 0  # Unoccupied state

    def change_state(self):
        return OccupiedState()

class OccupiedState(TableState):
    def get_state(self):
        return 1  # Occupied state

    def change_state(self):
        return UnoccupiedState()

# Context class
class Table:
    def __init__(self, table_number, table_type, booking_time):
        self.table_number = table_number
        self.table_type = table_type
        self.booking_time = booking_time
        self.state = UnoccupiedState()

    def get_state(self):
        return self.state.get_state()

    def change_state(self):
        self.state = self.state.change_state()

    def check_booking_status(self, current_time):
        if self.get_state() == 0 and self.booking_time > current_time:
            self.change_state()
            print(f"Table {self.table_number} is now unoccupied.")

    def book_table(self, booking_time):
        self.booking_time = booking_time
        self.change_state()
        print(f"Table {self.table_number} booked successfully for {self.booking_time}.")

# Load tables from JSON
def load_tables_from_json(file_path):
    with open(file_path, 'r') as file:
        tables_data = json.load(file)
    return [Table(table_number=data['table_number'], table_type=data['table_type'],
                  booking_time=datetime.fromisoformat(data['booking_time']))
            for data in tables_data]

# Save tables to JSON
def save_tables_to_json(file_path, table_list):
    tables_data = [{'table_number': table.table_number, 'table_type': table.table_type,
                    'booking_time': table.booking_time.isoformat()}
                   for table in table_list]
    with open(file_path, 'w') as file:
        json.dump(tables_data, file, indent=2)

# dictionary unoccupied tables
unoccupied_tables_dict = {}

# file
json_file_path = 'tables.json'

# Loading tables 
table_list = load_tables_from_json(json_file_path)

# Inputs for booking-date
date_input = input("Enter the date (YYYY-MM-DD): ")
year, month, day = map(int, date_input.split('-'))

# Inputs- time
time_input = input("Enter the time (HH:MM:SS): ")
hour, minute, second = map(int, time_input.split(':'))

input_datetime = datetime(year, month, day, hour, minute, second)

# Check unoccupied tables 
user_input_table_type = input("Enter the table type (Family/Party/Couple): ").capitalize()

for table in table_list:
    table.check_booking_status(input_datetime)
    if table.get_state() == 0 and table.table_type == user_input_table_type:
        if user_input_table_type not in unoccupied_tables_dict:
            unoccupied_tables_dict[user_input_table_type] = []
        unoccupied_tables_dict[user_input_table_type].append(table.table_number)

# Display unoccupied tables
if user_input_table_type in unoccupied_tables_dict:
    print(f"Unoccupied {user_input_table_type} tables: {unoccupied_tables_dict[user_input_table_type]}")
else:
    print(f"No unoccupied tables of type {user_input_table_type} found.")

# Book a table
table_number_to_book = int(input("Enter the table number you want to book: "))
for table in table_list:
    if table.table_number == table_number_to_book:
        table.book_table(input_datetime)
        break

# Saving the updated table status back to the JSON file
save_tables_to_json(json_file_path, table_list)

