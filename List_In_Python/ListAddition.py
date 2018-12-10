menu = []
menu.append(["egg","spam","bacon"])
menu.append(["egg","sausage","bacon"])
menu.append(["egg","spam"])
menu.append(["egg","bcaon","spam"])
menu.append(["egg","bcaon","sausage","spam"])
menu.append(["spam","bacon","sausage","spam"])
menu.append(["spam","egg","sausage","bacon","spam"])
menu.append(["spam","egg","sausage","spam"])

#print(menu)


for meal in menu:
    if not "spam" in meal:
        print(meal)
        for ingredients in meal:
            print(ingredients)
