age = [3,5,6,7,8]
print(age)
age.remove(3)
print(age)
age.append(2)
print(age)
print(age[0])
age.sort()
print(age)
print(age[0])
age.pop()
print(age)
age.pop()
print(age)

conbine = [1,2,3,4,5,6,7,8,9]

oddNumberList = []

for i in conbine:  
    if i % 2 != 0:
      oddNumberList.append(i)
      
print(oddNumberList)

a = [1,3,4,6,'gdgd', 'teye']
b = [1,2,3,4,5, 'q','capitalize']
a.extend(b)

a.insert(3,"Teddy")
a.append(50)
print(a)