# row = 7
# r = 2 * row -2
#
# for i in range(0,row):
#     for j in range(0, r):
#         print(end=' ')
#     r = r -2
#     for j in range(0,i+1):
#         print(" * ",end='')
#     print('')

n= 5
fact = 1

for i in range(1,n+1):
    fact = fact * i
    print(fact)