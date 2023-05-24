N = int(input())

fib_series = []
if N >= 1:
    fib_series.append(0)

if N >= 2:
    fib_series.append(1)

for i in range(2,N):
    next_fib = fib_series[-1] + fib_series[-2]
    fib_series.append(next_fib)

print(*fib_series)