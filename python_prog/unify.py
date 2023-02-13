# s = 'Hitesh reddy'
# n = ''
# for i in s:
#     n = i + n
# print(n)
#print(' '.join(x[::-1] for x in s.split()))

# l = [3,6,8,2,4,10,34,65,1,9,7,99,88]
# len_max = l[0]
# secomf_max = l[1]
#
# for i in range(1,len(l)):
#     if l[i] >= len_max:
#         len_max = l[i]
#     elif l[i] > secomf_max and len_max != l[i]:
#         secomf_max =l[i]
#
# print(len_max)
# print(secomf_max)
# sec_max = sorted(l)
# print(sec_max[-2])

#file valid gmail address
import re

s = 'hItesh reDhdY'
d =  ''
c = 0
for i in s:
    if i != 'h':
       #c = c + 1
        d = d + '*'
    else:
        d = d + i
print(d)







