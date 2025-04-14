t = int(input())
for _ in range(t):
    s = input()
    mins = min(s.count('0'), s.count('1'))
    if mins%2 == 0:
        print('NET')
    else:
        print('DA')