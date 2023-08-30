import pandas

df = pandas.read_csv('hotels.csv')


class Hotel:
    def __init__(self, id_no):
        pass

    def book(self):
        pass

    def available(self):
        pass


class ReservationTicket:
    def __init__(self, customer_name, hotel_obj):
        pass

    def generate(self):
        content = f"Booked ticket for customer at Hotel"
        return content


if __name__ == '__main__':
    hotel_id = input("Enter the ID of the hotel: ")
    hotel = Hotel(hotel_id)

    if hotel.available():
        hotel.book()
        c_name = input("Enter your name: ")
        res_ticket = ReservationTicket(c_name, hotel)
        print(res_ticket.generate())
    else:
        print("Hotel has no vacancy.")
