#Learning the use of variables,Data types,User inputs and typecasting
num1=54
print(type(num1))
print(num1)
num2=int(input("Enter the second number "))
num2=float(num2)
print("After Conversion ",type(num2))
sum=num1+num2 #implicit type-casting
print("Sum of int and float data type is of type ",type(sum),"and result is ",sum)
num3="74"
num3=int(num3)
prod=num1*num3 #explicit type-casting
print("product of int and int data type is of type ",type(prod),"and result is ",prod)
#swap two numbers 
num1,num3=num3,num1
print("Value of num1 is ",num1)
print("Value of num3 is ",num3)