mystr=("banana","apple","cherry")
myit=iter(mystr)
print(next(myit))
print(next(myit))
print(next(myit))

class MyNumber:
    def __iter__(self):
        self.a=1
        return self
    def __next__(self):
        x=self.a
        self.a+=1
        return x
myclass=MyNumber()
myit=iter(myclass)

print(next(myit))
print(next(myit))

