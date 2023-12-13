# I'm going to create input

# this is the dictionary of fruits
fruits = {'apple':'130', 'avocado':'50', 'banana':'110',
          'cataloupe':'50','grapefruit':'60','grapes':'90',
          'honeydew melon':'50','kiwifruit':'90','lemon':'15',
          'lime':'20', 'nectarine':'60','orange':'80','peach':'60',
          'pear':'100','pineapple':'50','plums':'70','strawberries':'50',
          'sweet cherries':'100','tangerine':'50','watermelon':'80'}



fruit_m = input("Item: ")


# I'm going to convert in lower case
fruit_l = fruit_m.lower()

# this is the result
if not fruit_l in fruits:
    print("", end = "")
else:
    #print calories via keys
    print('Calories:'+fruits[fruit_l])
