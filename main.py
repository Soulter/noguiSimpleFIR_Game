# BY SOULTER 转载请注明出处和QQ:905617992
#On 2018/05/06 at noon


import  chess_manager
print("###井字棋### By:Soulter\n\t1.开始\n\t其余任意键.结束")
if input("选择:") == "1":

    choice_order = input("\t1.先下\n\t其余任意键.后下\n选择:")
    if choice_order == "1":
        # ---------------------------------------------------------------START as the FIRST
        # 检验是否为新游戏
        start_tag = 1
        if start_tag == 1:
            chess = chess_manager.empty_chess() # 新建棋盘,并且取得新棋盘序列
            start_tag = 0
        while 1:
            pChessPos = ""
            while pChessPos not in ["1","2","3","4","5","6","7","8","9"] :
                pChessPos = input("##请下棋(1-9)##:")
            while chess[int(pChessPos)-1] != 0 :
                pChessPos = input("##请下棋(1-9)##:")
            pChessPos = int(pChessPos)
            chess = chess_manager.turn_player(pChessPos,chess)#处理玩家的动作,并刷新棋盘

            print("##电脑开始下棋##")
            chess = chess_manager.turn_computer(chess)

            print("-----------------------------")
    else:
        # ---------------------------------------------------------------START as the FIRST
        # 检验是否为新游戏
        start_tag = 1
        if start_tag == 1:
            chess = chess_manager.empty_chess() # 新建棋盘,并且取得新棋盘序列
            start_tag = 0
        while 1:
            print("##电脑开始下棋##")
            chess = chess_manager.turn_computer(chess)

            pChessPos = ""
            while pChessPos not in ["1","2","3","4","5","6","7","8","9"] :
                pChessPos = input("##请下棋(1-9)##:")
            while chess[int(pChessPos)-1] != 0 :
                pChessPos = input("##请下棋(1-9)##:")
            pChessPos = int(pChessPos)
            chess = chess_manager.turn_player(pChessPos,chess)#处理玩家的动作,并刷新棋盘
            print("-----------------------------")
else:
    exit()







