#user inputs
# name = input("Enter your name : ")
# age = input("Enter your age : ")
# print("Hello " + name + "!  You are " + age)

#lists
numbers = [34, 5, 12, 12, 71, 39]
friends = ['john', 'max', 'zamzon', 'oscaa']
dogs= ['zeeba', 'sudu', 'rocky', 'alex']

friends.extend(numbers) # extend friends list by adding numbers list
friends.append('george') # add george to the last of friends list
friends.insert(2, 'Tucker') # add Tucker to index 2 position
friends.remove('max') #delete max
# friends.clear() #make list empty
friends.pop() #remove the last value

print(friends)
print(friends.index('Tucker')) #print the index of value
print(numbers.count(12)) #the number of values

dogs.sort() #a-z
print(dogs)
numbers.reverse() #reverse the list
print(numbers)

dogs2 = dogs.copy() #make a copy of dogs list
print(dogs2)