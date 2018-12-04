name = input("Please enter your name: ")
age = int(input("Hi old are you, {0}? ".format(name)))  #Adding type cast
print(age)

if age > 18:
	print("You are old enough to vote")
else:
	print("Please come back in {0}".format(18 - age))