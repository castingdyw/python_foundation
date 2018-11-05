#能不能上车，安检，车票
danger = 0 # 0代表没有危险品，1代表有危险品
ticket = 0 # 0代表没有车票，1代表有车票

#安检
if danger == 0:
    print("安检通过")
    #检票
    if ticket == 1:
        print("可以上车")
    else:
        print("不能上车")
else:
    print("不能进站")
