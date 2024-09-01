class Travel:
    def __init__(self,country,month,type):
        self.country=country
        self.month=int(month)
        self.type=type
        self.price=0

    def trip_info(self):
        if self.month>=11 and self.month<=3:
            print(f"You are going to {self.country} in the winter! This is a {self.type} trip!")
     
        elif self.month>3 and self.month<7:
            print(f"You are going to {self.country} in the summer! This is a {self.type} trip!")
        elif self.month>=7 and self.month<11:
            print(f"You are going to {self.country} in the rainy! This is a {self.type} trip!")
        else:
            print("Invalid Input")

    def cal_cost(self,cost):
        costs=[]
        while cost !=0:
            self.price+=cost
            costs.append(cost)
            cost=int(input("Enter another cost: "))

        advice=self.advice(self.price)
        inspect=self.list_inspect(costs)
        return advice,inspect
    



        # call next method
        # call checker method
        # return two things

    def advice(self,money):
        if money<=500:
            print("Low Budget!")
        elif money>500 and money<1500:
            print("Take a flight to anywhere....")
        else:
            print("Luxury trip")

    def list_inspect(self,costs):
        less_than_ten=0
        for i in costs:
            if i>=10:
                less_than_ten+=1

        if less_than_ten<10:
            self.price +=100
            print(f"Updated price: {self.price}")



location=input("Enter a country: ").capitalize()
trip_type=input("Leisure or business: ")
month=input("Enter the month in number: ")

test=Travel(location,month,trip_type)
test.trip_info()
flight_cost=float(input("Enter flight cost: "))
test.cal_cost(flight_cost)

