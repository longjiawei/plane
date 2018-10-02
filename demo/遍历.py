print("2017--2018赛季NBA西北联盟前八名：")
team = ["火箭","勇士","开拓者","爵士","鹈鹕","马刺","雷霆","森林狼"]
for i,item in enumerate(team,1):
    if i%2 != 0:
        print(item+"\t\t",end='')
    else:
        print(item+"\n")
