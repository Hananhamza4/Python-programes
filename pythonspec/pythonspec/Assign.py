# x=int(input("Enter the no of days in feb: "))

# if x>=29:
#     print("the year is leap yeaf")
# else:
#     print("the year is not leap year")

# Program to check if a year is a leap year or not

# year = int(input("Enter a year: "))

# # A leap year is divisible by 4
# # But if it is a century year (divisible by 100), it must also be divisible by 400
# if (year % 4 == 0):
#     if (year % 100 == 0):
#         if (year % 400 == 0):
#             print(f"{year} is a leap year.")
#         else:
#             print(f"{year} is not a leap year.")
#     else:
#         print(f"{year} is a leap year.")
# else:
#     print(f"{year} is not a leap year.")
# year=int(input("enter the year"))
# 2024
# if (year%4==0):
#     if(year %100==0):
#         if(year%400==0):
#             print(year,"this year is leap year")
#         else:
#             ("this year not leap year")
#     else:
#         print(year,"this year is leap year")
# else:
#     print("this is not a leap year")

# year=int(input("enter the year"))

# if(year%4==0)or(year%100)and(year%400):
#     print("the year is leap year")
# else:
#     print(' the year is not leap year')

# x=int(input("enter the a number :"))
# if x%3==0 and x%5==0:
#     print("fizzbuzz")
# elif x%3==0:
#     print("fizz")
# elif x%5==0:
#     print("buzz")
# else:
#     print(x,"none")

# num_1 = 10
# num_2 = 11
# print(num_1 % num_2)
# print(num_1 - num_2)
# print(num_1 * num_2)

# num_1=7
# num_2 = 6
# print(num_1 < num_2)
# print(num_1 > num_2)
# print(num_1 <= num_2)
# print(num_1 >= num_2)
# print(num_1==num_2)


# num_1=3
# num_2 = 4
# print((num_1 < num_2) and (num_1 != num_2))
# print((num_2 >= num_1) or (num_1 > num_2))
# print(not (num_1 == num_2))

# i=1
# while (i<6):
#     i = i +1
#     print(i)

# customer_num =5
# invoice_num =1212
# print("Invoice No(s):")
# while(customer_num >0):
#     print("INV -", invoice_num)
#     invoice_num = invoice_num +3
#     customer_num = customer_num -1

#Write a program to find sum of all integers greater than 100 and less than 200 that are divisible
#by 7.

# x=int(input("enter a number: "))
# y=int(input("enter the second number : "))
# sum=x+y
# if sum>100 and sum<200 and sum%7==0:
#     print("all the condition is true")
# else:
#     ("the number is not in the conditions")

# x = int(input("Enter a number: "))
# y = int(input("Enter the second number: "))
# sum = x + y

# if sum > 100 and sum < 200 and sum % 7 == 0:
#     print("All the conditions are true")
# else:
#     print("The number is not in the conditions")

# Program to find the sum of all integers greater than 100 and less than 200 divisible by 7

# total_sum = 0

# for number in range(101, 200):
#     if number % 7 == 0:
#         total_sum += number

# print("The sum of all integers greater than 100 and less than 200 divisible by 7 is:", total_sum)

# total_sum=0
# for number in range(101,200):
#     if number%7==0:
#         total_sum+=number
#         print("the sum of all the number is ",total_sum)

# num1=float(input("enter the number : "))
# num2=float(input("enter the second number: "))
# num3=float(input("enter the third number : "))

# if(num1>=num2) and (num1>=num3):
#     largest= num1
# elif(num2>=num1)and (num2>=num3):
#     largest=num2
# else:
#     largest=num3
# print("the largest number is ",largest)
# l=int(input("Enter the length of the rectangle:  "))
# w=int(input("enter the width of the rectangle: "))

# area=l*w
# peri=2*(l+w)

# print("the area is  : ",area,"\nthe perimwter is : ",peri)




# p=int(input("Enter the number to check prime or not :"))

# if p%1==0 and p%p==0 and p%p/2!=0:
#     print("the number is prime number")
# else:
#     print("number is not prime...")


# num = int(input("Enter a number: "))

# if num <= 1:
#     print(num, "is not a prime number")
# elif num == 2 or num == 3 or num == 5 or num == 7:
#     print(num, "is a prime number")
# elif num % 2 == 0 or num % 3 == 0 or num % 5 == 0 or num % 7 == 0:
#     print(num, "is not a prime number")
# else:
#     print(num, "might be a prime number")

# num=int(input("enter the num"))
# if num>1:
#     for i in range(2,num):
#         if(num%i==0):
#             print(num,"this is not prime")
#             break
#     else:
#         print("prime")
# else:
#     print("the number is lessthan 1")            

# num=int(input("enter the nume"))

# for i in range(0,11):
#     if 
#         print(i)
#     else:
#         print("bye")
