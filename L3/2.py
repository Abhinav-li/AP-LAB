print('Enter numbers. Press F to exit: ')
l = []
while 1:
    x = input()
    if((x == 'F' )|( x  =='f')):
        break
    
    else:
        l.append(int(x))

def func(list1):
    x = set([])
    for i in list1:
        x.add(i)
    l = list(x)
    return l


print(func(l))