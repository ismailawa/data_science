# x = 0
# y = 10
# while  x <= y:
#     print(x)
#     x = x + 1
    
# z = 10 
# while z > 0:
#     print(z)
#     z -= 1
    
# d = 0   
# while d < 100:
#     print(d)
#     d += 1
    
    
studentmarks = [50,60,40,80,30,99,66,76,55,88]

index = 0
sum = 0
count = len(studentmarks)

while index < count:
    sum += studentmarks[index]
    index += 1
    
print(sum)
print(count)
print(sum/count)

a = [1,2,3,4,5,6,7,8,9,10,11,12]
index = 0
while index < len(a):
    print(a[index])
   
    if(a[index] == 4):
        break
    index += 1
   

b = [1,2,3,4,5,6,7,8,9,10,11,12]
print('--------------------start----------')
for x in b[2 :10]:
   
    print(x)

z = [1,2,3,4,5,6,7,8,9,10,11,12]
print('--------------------start----------')
for x in z[2:-2]:
   
    print(x)