# start

positive_number: int = None
negative_number: int = None
counter: int = 0
num: int = int(input('enter a number:'))

for _ in range(1, 10 + 1):
    while True:
        if num == -999:
            break
        if num < -1000 or num > 1000:
            print('ignore')
            num = int(input('enter a number:'))
            continue

        if positive_number is None or num > positive_number:
            positive_number = num
        if negative_number is None or num < negative_number:
            negative_number = num
            num = int(input('enter a number:'))
            counter += 1
        if num == 0:
            counter += 1
            print('zero')
            num = int(input('enter a number:'))
        if num % 7 == 0:
            counter += 1
            print('the number divide by 7')

print()
print(f'total number is: {counter}')
print(f'the last positive number is: {positive_number}')
print(f'the last negative is: {negative_number}')

# stop
