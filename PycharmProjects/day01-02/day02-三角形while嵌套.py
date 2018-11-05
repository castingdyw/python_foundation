#倒三角
# i = 5
# while i >= 1:
#     j = 1
#     while j <= i:
#         print("*",end=" ")
#         j += 1
#     print()
#     i -= 1

#正三角
# i = 1
# while i <= 5:
#     j = 1
#     while j <= i:
#         print("*",end=" ")
#         j += 1
#     print()
#     i += 1

#两个三角形
i = 1
while i <= 9:
    if i <= 5:
        j = 1
        while j <= i:
            print('*',end=' ')
            j += 1
    else:
        j = 1
        while j <= 9-i+1:
            print('*',end=' ')
            j += 1
    print()
    i += 1