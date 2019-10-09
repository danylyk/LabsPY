import random

class SSA:
    @staticmethod
    def Lab1 (v):
        sum = 0
        for i in v:
            sum += i
        return {'sum': sum, 'avg': sum/len(v)}

v = [int(random.random()*20)-10 for i in range(int(random.random()*10) + 5)]

print(v)
print(SSA.Lab1(v))