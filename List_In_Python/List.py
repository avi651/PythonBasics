#ipAddress = input("Please enter an IP address: ")
#print(ipAddress.count("."))

parrot_list = ["non pinin","no more","a stiff","bereft of live"]

for state in parrot_list:
    print("This parrot is " + state)

even = [2,4,6,8]
odd = [1,3,5,7,9]

numbers = even + odd
numbers.sort()
numbers_in_order = sorted(numbers)
print(numbers_in_order)

if numbers == numbers_in_order:
    print("The list are equal")
else:
    print("The list are not equal")
