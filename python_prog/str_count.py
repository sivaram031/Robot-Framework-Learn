# inp = 'aabcbbcddefd'
# out = []
# prev = ''
# c = 1
#
# for i in inp:
#     if i == prev:
#         c +=1
#     else:
#         prev = i
#         if c > 0:
#             out.append(str(c))
#         out.append(i)
#         c = 1
# print(''.join(out))

inp = 'aabcbddef'
c = 0

for i in inp:
    if i == 'b':
        c +=1
print(c)

