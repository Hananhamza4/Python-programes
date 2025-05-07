# f=open("demofile.txt","x")

# with open("demofile.txt","w") as f:
#     f.write("my name is hanan")

# with open("demofile.txt","r") as f:
#     print(f.read())

# with open('demofile.txt',"r") as f:
#     print(f.read(6)) 
   
# lines= ["hello world\n","welcome to python\n","dolphin\n"]
# with open("demofile.txt","w") as f:
#     f.writelines(lines)

# with open("demofile.txt","r") as f:
#     print(f.read())

# with open("demofile.txt","r") as f:
#     print(f.readline())

# with open("demofile.txt","r") as f:
#     print(f.readlines())

# with open("demofile.txt","a") as f:
#     f.write("this text is addedd")

# with open("demofile.txt") as f:
#     print(f.read())

# import os
# os.remove("demofile.txt")

# import os
# if os.path.exists("demofile.txt"):
#     os.remove("demofile.txt")
# else:
#     print("the file does not exist")    

# import os
# os.rmdir("delete.txt")


## csv 

#f=open("newcsv.csv","x")
# import csv

# with open("newcsv.csv","w",newline="") as f:
#     w=csv.writer(f)
#     w.writerow(["Hanan","movie","friend"])
#     w.writerow(["hana","hanan",122])
#     w.writerow(["elephent","dog",2])


# import csv

# with open("newcsv.csv", "r",) as f:
#     r=csv.reader(f)

#     for row in r:
#         print(row)
# f=open("myfile.zip","x")


# import zipfile

# with zipfile.ZipFile("myfile.zip","w") as f:
#     f.write("newcsv.csv")
#     f.write("hallo.txt")
# import zipfile

# with zipfile.ZipFile("myfile.zip", "r")as f:
#     f.extractall("Hanan")
#     list1=f.namelist()
#     print(list1)



