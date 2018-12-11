fruit = {"orange" : "a sweet, orange , citrus fruit",
         "apple": "good for making cider",
          "lemon": "a sour, yellow citrus fruit",
          "lime": "a sour, green citrus fruit"}

print(fruit)

ordered_keys = list(fruit.keys())
ordered_keys.sort()
for f in ordered_keys:
    print(f + " - " + fruit[f])
