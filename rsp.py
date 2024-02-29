import random
rsp = ['가위','바위','보']
random_rsp = random.choice(rsp)

print('가위 바위 보 게임을 시작하겠습니다')
print(random_rsp)

# def rsp():
while True:
        
        player =input()
        print(player)

        if player == random_rsp: 
            print('비김')
            break
        elif (player == '가위' and random_rsp == '바위') or (player == '바위' and random_rsp =='보') or (player == '보' and random_rsp == '가위'):
            print('짐')
            break
        elif (player == '보' and random_rsp == '바위') or (player == '가위' and random_rsp =='보') or (player == '바위' and random_rsp == '가위'):
            print('이김')
            break
        else:
            print('제대로 ㄱ')

yn = 'ㄱㄱ'

while True:
    rsp()
    print('다시?')

    player=input()
    print(player)

    if player == yn:
        print('다시')

    else:
        break

