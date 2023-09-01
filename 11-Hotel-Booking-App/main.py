import pandas

df = pandas.read_csv('hotels.csv', dtype={'id': str})
df_cc = pandas.read_csv('cards.csv', dtype=str).to_dict(orient='records')
df_cc_security = pandas.read_csv('card_security.csv', dtype=str)


class Hotel:
    def __init__(self, id_no):
        self.id_no = id_no
        self.name = df.loc[df['id'] == self.id_no, 'name'].squeeze()

    def book(self):
        """ Book a hotel by changing its availability to no. """
        df.loc[df['id'] == self.id_no, 'available'] = 'no'
        df.to_csv('hotels.csv', index=False)

    def available(self):
        """ Check if the hotel is available. """
        availability = df.loc[df['id'] == self.id_no, 'available'].squeeze()
        if availability == 'yes':
            return True
        else:
            return False


class ReservationTicket:
    def __init__(self, customer_name, hotel_obj):
        self.customer_name = customer_name
        self.hotel_obj = hotel_obj

    def generate(self):
        content = f"""
        Thank you for the reservation!
        Here are your ticket details:
        Name: {self.customer_name}
        Hotel: {self.hotel_obj.name}
        """
        return content


class CreditCard:
    def __init__(self, number):
        self.number = number

    def validate(self, expiration, holder, cvc):
        card_data = {'number': self.number,
                     'expiration': expiration,
                     'holder': holder,
                     'cvc': cvc}
        if card_data in df_cc:
            return True
        else:
            return False


class SecureCreditCard(CreditCard):
    def authenticate(self, given_password):
        password = df_cc_security.loc[df_cc_security['number'] == self.number, 'password'].squeeze()
        if password == given_password:
            return True
        else:
            return False


if __name__ == '__main__':
    print(df)
    hotel_id = input("Enter the ID of the hotel: ")
    hotel = Hotel(hotel_id)

    if hotel.available():
        cc_details = SecureCreditCard(number='1234567891011121')
        if cc_details.validate(expiration='12/26', holder='JOHN SMITH', cvc='123'):
            if cc_details.authenticate(given_password='mypass'):
                hotel.book()
                c_name = input("Enter your name: ")
                res_ticket = ReservationTicket(c_name, hotel)
                print(res_ticket.generate())
            else:
                print("The Credit Card authentication failed.")
        else:
            print("The Credit Card details are not valid.")
    else:
        print("Hotel has no vacancy.")
