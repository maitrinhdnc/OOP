import pandas

df = pandas.read_csv("hotels.csv", dtype={"id": str})
df_card = pandas.read_csv("cards.csv", dtype=str).to_dict(orient="records")
df_card_secure = pandas.read_csv("card_security.csv", dtype=str)
class User:
  pass

class Hotel:
  def __init__(self, hotel_id):
    self.hotel_id = hotel_id
    self.name = df.loc[df["id"]==self.hotel_id, "name"].squeeze()
  
  def book(self):
    df.loc[df["id"] == self.hotel_id, "available"] = "no"
    df.to_csv("hotels.csv", index=False)

  def available(self):
    availability = df.loc[df["id"] == self.hotel_id, "available"].squeeze()
    if availability == "yes":
      return True
    else:
      return False

  @staticmethod
  def get_hotel_count(data):
    return len(data)
    
  def __eq__(self, other):
    if self.hotel_id == other.hotel_id:
      return True
    else:
      return False

class ReservationTicket:
  def __init__(self, customer_name, hotel_object):
    self.customer_name = customer_name 
    self.hotel = hotel_object
    
  def generate(self):
    content = f"""
    Thank you for your reservation
    Here are your booking:
    Name: {self.customer_name}
    Hotel: {self.hotel.name}
    """ 
    return content     
  
  @property
  def the_customer_name(self):
    name = self.customer_name.strip()
    name = name.title()
    return name

class CreditCard():
  def __init__(self, number):
    self.number = number 
  
  def validate(self, expiration, holder, cvc):
    card_data = {"number":self.number, "expiration": expiration, "holder":holder, "cvc": cvc}
    if card_data in df_card:
      return True
    else:
      return False

class SecureCreditCard(CreditCard):
  def authenticate(self, given_password):
    password = df_card_secure.loc[df_card_secure["number"]==self.number, "password"].squeeze()
    if password == given_password:
      return True 
    else: 
      return False

print(Hotel.get_hotel_count(data=df))
print(df)
hotel1 = Hotel("134")
hotel2 = Hotel("134")
print(hotel1 == hotel2)
# ticket = ReservationTicket("trinh mai", hotel1)
# print(ticket.the_customer_name)
# hotel_id = input("Enter the id of the hotel: ")
# while hotel_id not in df["id"].tolist():
#   print("Wrong ID hotel. Please enter again")
#   hotel_id = input("Enter the id of the hotel: ")

# hotel = Hotel(hotel_id)
# if hotel.available():
#   # card_number = input("Enter the credit card number: ")
#   credit_card = SecureCreditCard(number="1234567890123456")
#   if credit_card.validate(expiration="12/26", holder="JOHN SMITH", cvc="123"):
#     if credit_card.authenticate(given_password="mypass"):
#       hotel.book()
#       name = input("Enter your name: ")
#       reservation_ticktet = ReservationTicket(name, hotel)
#       print(reservation_ticktet.generate())
#     else:
#       print("Credit Card authentication failed")
#   else:
#     print("There was problem with your payment")
# else:
#   print("Hotel is not free")


