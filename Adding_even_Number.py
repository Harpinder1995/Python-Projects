total = 0
for n in range(1,101):
    if n%2==0:
        total += n
    else:
        continue
print(f"The Sum of Even Number from 1 to 100 is : {total}")
