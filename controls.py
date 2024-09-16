
def  calculate_discount ():
  

 Price =int(input("what is the price of the item?"))

 discount_percent=0.01
 if Price>=2000:
  cashPrice=Price*discount_percent
  print(f"price is,{Price-cashPrice}")
  
 else:
  print('no discount')
print(calculate_discount())




 
 






