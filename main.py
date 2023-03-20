import datetime
import eat
import sport
import insert

from eat import Get_Day_Eat
insert.insert_sport()


# id = 1
# date = datetime.datetime.now()  # 测试用
# for i in Get_Day_Eat(id, date):
#     print(i)
# print()
# print("该天该用户吃的卡路里", eat.Get_Day_Eat_cal(id, date))
# print()
# print("该天该人所吃食物有")
# for i in eat.Get_Day_Eat_type(id, date):
#     print(i[2], i[3],'g')
#
# id = 2
# data = datetime.datetime.now()
# for i in sport.Get_Day_Sport(id, data):
#     print(i)
# print()
# print(sport.Get_Day_Sport_cal(id, data))
# for i in sport.Get_Day_Sport_type(id, date):
#     print(i[2])