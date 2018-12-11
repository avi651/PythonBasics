fruit = {"orange" : "a sweet, orange , citrus fruit",
         "apple": "good for making cider",
          "lemon": "a sour, yellow citrus fruit",
          "lime": "a sour, green citrus fruit"}


fruit["pear"] = "an odd shaped apple"
print(fruit)
while True:
    dict_key = input("Please enter a fruit:")
    if dict_key == "quit":
     break
    if dict_key in fruit:
        description = fruit.get(dict_key)
        print(description)
    else:
        print("We don't have a " + dict_key)
