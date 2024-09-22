# start

for i in range(1, 5 + 2, 2):
    for j in range(1, i + 1):
            print(j, end=' ')
    print()
for i in range(3, 1 - 1, -2):
    for j in range(1, i + 1):
        print(j, end=' ')
    print()

# stop

# start
max_number: int = int(input('enter a number:'))
number: int = 1
spaces: int = max_number // 2

for _ in range(1, (max_number - number) // 2):
    print(' ',end=' ')

for _ in range(1, number + 1):
    print(f'{number}',end=' ')
print()
spaces -= -1

#stop


#start
max_number: int = int(input('enter a number:'))
spaces: int = max_number // 2

for i in range(1, 5 + 2, 2):
    for j in range(1, i + 1):
            print(j, end=' ')
    print()
for i in range(3, 1 - 1, -2):
    for j in range(1, i + 1):
        print(j, end=' ')
    print()

#stop

