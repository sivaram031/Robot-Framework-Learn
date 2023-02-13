# chars = "abcdefghijklmnopqrstuvwxyz"
# check_string = "sivarsamanatha"
#
# for char in chars:
#   count = check_string.count(char)
#   if count == 2:
#    print (char, count)
#x = 'pavan'
# x = 'aeiou'
# s = 'hello'
# n = ''
# c = 0
# for i in s:
#   if i not in x:
#     c = c + 1
#     n = n + c * '*'
#
#   else:
#     n = n + i
#
# print(n)

# inp = 'pavan'
# d = {}

# for i in inp:
#   d [i] = d.get(i,0) + 1
#   print(d)





# s = 'how are you hello'
# n = ''
# #print(s.replace('o','a'))
# for i in s:
#     if i == 'o':
#         n = n + 'a'
#     else:
#         n = n + i
# print(n)
import re

# file = open("C:\\Users\\Sivaram\\PycharmProjects\\Robot-Framework-Learn\python_prog\\re.txt",'r')
# data = file.read()
#
# regex = r'[a-zA-Z0-9._]+@[a-zA-Z0-9]+.[a-zA-Z]{2,3}'
# n = re.findall(regex, data)
# print(n)
p = 10
n = 5

del(n)
print(n)
l = []
s = ' '
for i in range(1,n+1):
    l.append(i)

print(l)
print("Something")
for i in l:
    s = s + ''.join(str(i))
print(s)