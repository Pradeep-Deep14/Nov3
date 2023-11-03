names = ['john','carol','yellen']
fruits = ['apple','banana','mango']
listNew = list(zip(names,fruits))
listNew = [list(x) for x in listNew]
print(listNew)