def func(list1):
    ans = 1
    for i in list1:
        ans = ans * i
    return ans

print('Enter numbers. Press F to exit: ')
l = []
while 1:
    x = input()
    if((x == 'F' )|( x  =='f')):
        break
    
    else:
        l.append(int(x))


print(func(l))
