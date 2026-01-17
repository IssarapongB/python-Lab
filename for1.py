#for:
myrange =range (10)#[0,1,...,9]
print(*myrange)
print(list(myrange))
myrange = range (5,10,)
print(*myrange)
myrange = range (1,10,2)
print(*myrange)

sum = 0
for i in range(1,10):
    sum += i
print(sum)


sum = 0
for i in range(5,11):
    if i % 2 == 0:
        sum += i
print(sum)