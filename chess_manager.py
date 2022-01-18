import print_chess
import random
import check_referee

# @author Soulter  github.com/soulter

def empty_chess():
    # 0为空棋位 1为玩家棋位 2为电脑棋位
    chess=[0,0,0,0,0,0,0,0,0]
    p_chess = """
    -   -   -
    -   -   -
    -   -   -
    """
    print(p_chess)
    return chess


def turn_player(position,chess):
    #转到玩家下棋
    if chess[position-1] == 0:
        print("##成功下棋##")
        chess[position-1] = 1
        print_chess.print_chess(chess)
        check_referee.referee(1,chess)
        return chess


def turn_computer(chess):
    #轮到电脑下棋
    print(chess)
    for i in chess:  #检测是否还有空余的棋位,
        if i == 0:
            while 1:
                cChessPos = random.randint(0, 8)
                if chess[cChessPos] == 0:
                    chess[cChessPos] = 2
                    print_chess.print_chess(chess)
                    print("##电脑已下棋##")
                    check_referee.referee(2,chess)
                    return chess
    print("平局")
    print_chess.print_chess(chess)
    exit()

