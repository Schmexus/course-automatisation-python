import sys

def fast_input():
    return sys.stdin.readline().rstrip("\r\n")

def fast_output(x):
    sys.stdout.write(str(x)+'\n')

def fing_max_number(num):
    x = [int(i) for i in str(num)]
    if len(x) == 1:
        fast_output(0)
        return
    for i in range(len(x)-1):
        if x[i] < x[i+1]:
            x.remove(x[i])
            fast_output(''.join(map(str, x)))
            return
    x.remove(min(x))
    fast_output(''.join(map(str, x)))

iterator = int(fast_input())
numbers = []
while iterator > 0:
    numbers.append(fast_input())
    iterator-= 1
for i in numbers:
    fing_max_number(i)