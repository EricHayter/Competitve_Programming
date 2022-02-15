from audioop import reverse


n = int(input())

tides = list(map(int, input().split()))

tides.sort()
half = n //2 + n%2
first = tides[0:half]
second = tides[half:]
ordered_tides = []
final_string = ""

first.sort(reverse=True)

for i in range(0,half):
    try:
        ordered_tides.append(first[i])
        ordered_tides.append(second[i])
    except:
        pass

ordered_tides = list(map(str,ordered_tides))

print(" ".join(ordered_tides))