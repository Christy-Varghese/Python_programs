#Store input numbers
num1 = input("   Enter the number :")
num2 = input(" Enter ther next number :")

#Add two numbers
ans = float(num1) + float(num2)

#Subtract two numbers
dif = float(num1) - float(num2)

#Multiply two numbers
mul = float(num1) * float(num2)

#Divide two numbers
quo = float(num1) / float(num2)

#Display
print('The sum of {0} and {1} is {2}'.format(num1,num2,ans))

print('The difference of {0} and {1} is {2}'.format(num1,num2,dif))

print('The product of {0} and {1} is {2}'.format(num1,num2,mul))

print('The qoutient of {0} and {1} is {2}'.format(num1,num2,quo))
