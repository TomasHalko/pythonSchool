dataset = [22.0, 25.0, 19.8, 20.0, 20.2, 19.5, 21.9, 35.0]

total = 0.0
avg = 0.0

for item in dataset: 
    total = total + item

avg = total/ len(dataset)

print(avg)