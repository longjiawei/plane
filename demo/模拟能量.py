print("查询能量请输入能量来源!退出程序请输入0 \n能量来源如下:\n生活缴费、行走捐、共享单车、线下支付、网络购票")
while True:
    j = input()
    if j =="生活缴费":
        print("200g")
    elif j =="行走捐":
        print("100g")
    elif j =="共享单车":
        print("150g")
    elif j =="线下支付":
        print("50g")
    elif j =="网络购票":
        print("120g")
    elif j=="0":
        print("已退出")
        break
