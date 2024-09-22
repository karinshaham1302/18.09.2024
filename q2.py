# start

world_record: float = 6.23
score: float = float(input('enter a number:'))
sum_good_score: float = 0.0

for _ in range(1, 7 + 1):
    score: float = float(input('enter a number:'))
    while score < 5.80:
        continue
    if score >= 5.80:
        print('good jump')
        score: float = float(input('enter a number:'))
        sum_good_score += score
    if score == world_record:
        print('wow! this is the world record, amazing!')
else:
    print('None')

print()
avg_good_score: float = sum_good_score / 7
print(f'good score: {sum_good_score}, everage = {avg_good_score}.2f')
name_of_athlete: str = input('the name of the athlete is:')
print(f'the new record is: {world_record}, the name of the athlete {name_of_athlete}')

# stop
