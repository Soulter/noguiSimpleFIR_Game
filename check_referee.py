# @author Soulter  github.com/soulter


def referee(who,chess):
    if who == 1:
        team = "玩家"
    elif who == 2:
        team = "电脑"
    if chess[0] == who and chess[1] == who and chess[2] == who:
        print(team+" win!!!")
        exit()
    elif chess[3] == who and chess[4] == who and chess[5] == who:
        print(team+" win!!!")
        exit()
    elif chess[6] == who and chess[7] == who and chess[8] == who:
        print(team+" win!!!")
        exit()
    elif chess[6] == who and chess[7] == who and chess[8] == who:
        print(team+" win!!!")
        exit()
    elif chess[0] == who and chess[3] == who and chess[6] == who:
        print(team + " win!!!")
        exit()
    elif chess[1] == who and chess[4] == who and chess[7] == who:
        print(team+" win!!!")
        exit()
    elif chess[2] == who and chess[5] == who and chess[8] == who:
        print(team+" win!!!")
        exit()
    elif chess[0] == who and chess[4] == who and chess[8] == who:
        print(team+" win!!!")
        exit()
    elif chess[2] == who and chess[4] == who and chess[6] == who:
        print(team + " win!!!")
        exit()
