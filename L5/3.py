class Comb:
    unique = []
    
    def __init__(self, l):
        for i in range(len(l)+1):
            for j in range(len(l)+1):
                if(i == j) | (i > j):
                    continue
                Comb.unique.append(l[i:j])

        Comb.unique.append([])
    
    def display(self):
        print(Comb.unique)


n = int(input('Number of items in list: '))

l = [input() for i in range(n)]

obj = Comb(l)


obj.display()
