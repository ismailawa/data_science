# 1. Enter first number
x = input("Enter first number: ")
# 2. Enter sign
sign = input("Enter operation eg. '+', '-', '*', '/' or '%: ")
# 3. Enter second number
y = input("Enter second number: ")

# convert input to float
convert_x = float(x)
convert_y = float(y)
# 4. Calculate the answer

# 4.1. check sign
if sign == '+':
# 4.2 if the sign is plus we add the two number x and y
   answer = convert_x  + convert_y
   print(answer) 

elif sign == '-':
# 4.3 if the sign is minus we subtract the two number x and y
   answer = convert_x  - convert_y
   print(answer) 

elif sign == '*':
# 4.4 if the sign is multification we multify the two number x and y
    answer = convert_x  * convert_y
    print(answer) 
else:
   print("Enter valid sign please enter a valid sign eg. '+', '-', '*', '/' or '%")


