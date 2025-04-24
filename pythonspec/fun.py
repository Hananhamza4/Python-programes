# def my_function(lname):
#     print("david "+lname)
# my_function("hanan")
# my_function("toibas")
# my_function("linux")
#####deafult function
# def my_function(a=3,b=4):
#     sum=a+b
#     print("sum",sum)
# my_function(2,3)
# my_function()
########key value
# def display_info(first_name,last_name):
#     print(first_name,last_name)

# display_info("hanan","mangalath")

def find_sum(*numbers):
    result=0
    for i in numbers:
        result=result+i
    print("sum= ", result)

find_sum(1,2,3)
find_sum(4,9)
