##A customer buys two items from a store. Write a program that prompts the user
# to enter the prices of the 2 items. The program then asks the user 
# if they have a “discount coupon”. If the answer is ‘Y’ or ‘y’, the program outputs 
# the total price reduced by 10%, otherwise the program outputs the total price with no discount.
import math

item1=input ("Enter the Prices of Item 1: ")
item2=input ("Enter the Prices of Item 2: ")
discount=input("Do You have a Discount Coupon? y or Y for Yes -- N or n for No: ")
sum=float (item1)+float(item2) 
dis2= float (sum) - (float (0.10) * float (sum))
if discount == 'Y' or discount== 'y':
   print("Total Price: ",dis2)
else:
   print("No Discount->Total Price: ", sum)
