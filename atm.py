class ATM:
    def __init__(self, card_number, pin_number):
        self.card_number = card_number
        self.pin_number = pin_number

    def cash_withdrawal(self):
        print("Cash withdrawal method called.")
      
    def balance_enquiry(self):
        print("Balance inquiry method called.")
       

card_number = "1234567890123456"  
pin_number = "1234"  
my_atm = ATM(card_number, pin_number)

my_atm.cash_withdrawal()
my_atm.balance_enquiry()
