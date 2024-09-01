x=int(input("guess the no. x less than or equal to 100 : "))
match  x: 
   case _ if (x<=10 and x>=0):

     print("make your no. big")

   case _ if (x<=50 and x>10): 
     print("ur no. is  avg")

   case _ if (x<98 and x>50):
      print(" you are going to verge but few step left")
   case _ if (x== 99):
      print("one step left")
   case _ if (x==100) :
      print("you are supreme")

 