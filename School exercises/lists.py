bikes = ['redline', 'tracks', 'giant']

first_bike = bikes[0]
last_bike = bikes[-1]

for bike in bikes: 
    print(bike)

bikes.append('mountain')
bikes.append('sponge')
bikes.append('tank')


print(last_bike)

# if you want to insert some value use bikes.insert(index, 'whatever you want to insert')
#print every item in bikes list
for i in bikes:
    print(i)

#remove some element with del bikes[index
print (bikes[-2])
del bikes[-2]
print (bikes[-2])

#check presentation on fronter for list cheatsheet
bike = input()
if bike in bikes: 
    print("it is in the list")
else: print("its not")