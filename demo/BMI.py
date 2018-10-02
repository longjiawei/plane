while True:
   def fun_bmi(person,height,weight):
        print(person + "的身高" + str(height) + "米\t体重：" + str(weight) + "千克")
        bmi = weight/height**2
        print("您的BMI指数为：" + str(bmi))
        if bmi<18.5:
            print("您的体重过轻~@——@~")
        if 18.5<=bmi<24.9:
            print("正常范围，注意保持（-_-）")
        if 24.9<=bmi<29.9:
            print("您的体重过重 ~@_@~")
        if bmi>=29.9:
            print("肥胖 ^@_@^")
   print("欢迎开始BMI测试")
   start = str(input("请选择是否开始："))
   if start == "否":
      break
   else:
      person = str(input("请输入您的姓名："))
      height = float(input("请输入您的身高（单位为米）:"))
      weight = float(input("请输入您的体重（单位为千克）:"))
      fun_bmi(person,height,weight)
   continue
        
    
