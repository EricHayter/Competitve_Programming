n = int(input())

highest_day = 0

swifts = list(map(int, input().split()))
semaphores = list(map(int, input().split()))

swifts_total = 0
semaphores_total = 0

for i in range(0,n):
    swifts_total += swifts[i]
    swifts_total += semaphores[i]
    if swifts_total == semaphores_total:
        highest_day == i + 1

print(highest_day)