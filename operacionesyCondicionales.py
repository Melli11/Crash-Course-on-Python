
# This function compares two numbers and returns them
# # in increasing order.
# def order_numbers(number1, number2):
# 	if number2 > number1:
# 		return number1, number2
# 	else:
# 		return number2, number1

# # 1) Fill in the blanks so the print statement displays the result
# #    of the function call
# smaller,bigger = order_numbers(100, 99)
# print(smaller, bigger)

def lucky_number(name):
  number = len(name) * 9
  msj= "Hello " + name + ". Your lucky number is " + str(number)
  return msj
	    
print(lucky_number("Kay"))
print(lucky_number("Cameron"))

print("A dog" > "A mouse")
print(9999+8888)
print(100*100)
print(9999+8888 > 100*100)
print ("big" > "small")
print((10 >= 5*2) and (10 <= 5*2))
print(5//4) # Division Entera
print(5/4) # Division Real