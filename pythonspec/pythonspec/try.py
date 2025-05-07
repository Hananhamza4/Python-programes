# try:
#     result=10/2
# except ZeroDivisionError:
#     print("cant divide with zero")

# try:
#     list1=[1,3,2,4,5,2,5]
#     print(list1[100])
# except:
#     print("error")

# try:
#     even=[2,4,6,8]
#     print(even[5])
# except ValueError:
#     print("no found")
# except ZeroDivisionError:
#     print("the value is zero")    

# try:
#     x=int("hello")
#     y=10/0
# except ValueError:
#     print("caught a valueError")
# except ZeroDivisionError:
#     print("cant be zero")


try:
    num=int(input("enter a number: "))
    result=10/num
except ValueError:
    print("invalid values")
except ZeroDivisionError:
    print("the value cant be zero")
else:
    print("Result",result)
finally:
    print("This is the final")    