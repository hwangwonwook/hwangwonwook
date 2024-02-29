import random
random_number = random.randint(1,100)

print('숫자를 맞춰보시오')
print(random_number)

count = 0

while True:
    
    player_number = int(input())
    print(player_number)

    count += 1
    print(count)

    if random_number > player_number:
        print('up')


    elif random_number < player_number:
        print('down')
    
    else:
        print('correct answer')
        break










