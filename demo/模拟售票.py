while 1:
    print("欢迎使用自动售票机~~~~")
    move = int(input("请选择正在上映的电影：1.《环太平洋：雷霆再起》  2.《头号玩家》  3《红海行动》  4《西虹市首富》"))
    class Move():
        def __init__(self,name):
            print("已选择电影：" + name)
            session = int(input("请选择电影播放场次：1、9：30  2、10：40  3、12：00"))
            class Session():
                def __init__(self,name2):
                    print("电影场次：" + name2)
                    seat = int(input("请选择座位 剩余座位：1、10_01, 2、10_02, 3、10_03, 4、10_04"))
                    class Seat():
                        def __init__(self,name3):
                            print("选择的座位："+ name3)
                            print("正在出票。。。")
                    if seat == 1:
                        Seat("10_01")
                    if seat == 2:
                        Seat("10_02")
                    if seat == 3:
                        Seat("10_03")
                    if seat == 4:
                        Seat("10_04")
            if session == 1:
                Session("9:30")
            if session == 2:
                Session("10:40")
            if session == 3:
                Session("12:00")
    if move == 1:
        choicemove = Move("《环太平洋：雷霆再起》")
    if move == 2:
        choicemove = Move("《头号玩家》")
    if move == 3:
        choicemove = Move("《红海行动》")
    if move == 4:
        choicemove = Move("《西虹市首富》")