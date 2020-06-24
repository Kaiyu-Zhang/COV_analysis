import numpy as np
import pandas as pd
#导入数据，这里分别用label和data存储string和浮点类型的数据
country_label=np.array(np.loadtxt('./COVID_extra.csv',dtype=str,delimiter=',',skiprows=1,usecols=(2,3),encoding='utf-8'))
country_data=np.array(np.loadtxt('./COVID_extra.csv',dtype=float ,delimiter=',',skiprows=1,usecols=(4,5,6,7),encoding='utf-8'))
China_label=np.array(np.loadtxt('./COVID_basedata.csv',dtype=str,delimiter=',',skiprows=1,usecols=(0,1,2,3,4,5,6),encoding='utf-8'))
China_data=np.array(np.loadtxt('./COVID_basedata.csv',dtype=float,delimiter=',',skiprows=1,usecols=(7,8,9,10),encoding='utf-8'))


#选择查询模式,这里增加了用户交互的功能，即给出反馈
select = input("请输入查询模式(查询某地单日情况选择1，查询段时间内某地情况选择2，检索最大值选择3，检索最小值选择4，查询死亡率选择5）：")
print("当前使用模式：模式",select)
print("地区请输入英文名或拼音，日期标准格式为 XXXX-XX-XX")

#模式1
if (select  == "1"):
    area = input("请输入要查询的地区：")
    print("您要查询的地区是：", area)
    date1 = input("请输入要查询的日期：")
    print("您要查询的日期是：",date1)
    need = input("请输入要查询的信息(当前支持查询的信息有new_cases,new_deaths,total_cases,total_deaths)：") #获取用户进一步查询的信息
    print("您要查询的信息是：", need)
    searched_values = np.array([area,date1])  #这里定义查询数组，匹配查询
    for i in range(country_label.shape[0]):    #这里通过对country_label循环对比，找到要查询的内容对应的index
        if ((country_label[i]==searched_values).all()):     
            break
    if (need =="new_cases"):                                    #根据用户需求，将index对应的数据输出
        print ("查询新增病例new_cases为：",int(country_data[i,1] ) )
    elif (need == "new_deaths"):
        print("查询新增死亡数new_deaths为：", int(country_data[i, 3]) )
    elif (need =="total_cases"):
        print ("查询累积病例total_cases为：",int (country_data[i,0] ) )
    elif (need =="total_deaths"):
        print ("查询累计死亡数total_deaths为：",int(country_data[i,2] ) )
#模式2
elif (select  == "2"):
    area = input("请输入要查询的地区：")
    print("您要查询的地区是：", area)
    date_begin = input("请输入要查询的开始日期：")
    print("您要查询的开始日期是：", date_begin)
    date_end = input("请输入要查询的连续天数：")
    print("您要查询的连续天数是：", date_end)
    need = input("请输入要查询的信息(当前支持查询的信息有new_cases,new_deaths)：")
    print("您要查询的信息是：", need)
    searched_values = np.array([area, date_begin])   #同理，通过输入的地区和日期找到index的起始位置
    for i in range(country_label.shape[0]):
        if ((country_label[i] == searched_values).all()):
            break
    result = 0         #result用于统计累积量
    if (need == "new_cases"):          
        for x in range(i, i + int(date_end)+1):       #在该时间段进行累计
            result = result +country_data[x,1]
        print ("该段时间内的新增病例new_cases为：",int(result))
    elif (need == "new_deaths"):
        for x in range(i, i + int(date_end)+1):
            result = result +country_data[x,3]   
        print ("该段时间内的新增死亡数new_deaths为：",int(result))
#模式3
elif (select == "3"):
    area = input("请输入要查询的地区：")
    print("您要查询的地区是：", area)
    need = input("请输入要查询的信息(当前支持查询的信息有new_cases,new_deaths)：")
    print("您要查询的信息是：", need)
    count = np.sum(country_label == area)   #统计要查询的地区在label数组里出现的总次数
    index = np.where(country_label ==area)[0][0]   #找到第一个出现要查询地区的index位置
    new_data = country_data [index:index+count]   
    max_data = np.max(new_data,axis=0)          #找到拆分数据里每一列中的最大值，输出为一个数组
    if (need == "new_cases"):        
        t = max_data[1]               #得到最值数据
        index_t = np.where(country_data == t)[0][0]       #where函数定位最值数据所在的index
        print ("该地区最大新增病例数出现在",country_label[index_t][1] )        #通过index反输出日期
    elif (need == "new_deaths"):      
        t = max_data[3]
        index_t = np.where(country_data == t)[0][0]
        print ("该地区最大新增死亡数出现在",country_label[index_t][1] )
#模式4
elif (select == "4"):          
    area = input("请输入要查询的地区：")
    print("您要查询的地区是：", area)
    need = input("请输入要查询的信息(当前支持查询的信息有new_cases,new_deaths)：")
    print("您要查询的信息是：", need)
    count = np.sum(country_label == area)
    index = np.where(country_label == area)[0][0]
    new_data = country_data[index:index + count]
    max_data = np.min(new_data, axis=0)
    if (need == "new_cases"):
        t = max_data[1]
        index_t = np.where(country_data == t)[0][0]
        print("该地区最小新增病例数出现在",country_label[index_t][1])
    elif (need == "new_deaths"):
        t = max_data[3]
        index_t = np.where(country_data == t)[0][0]
        print("该地区最小新增死亡数出现在",country_label[index_t][1])
#模式5
elif (select  == "5"):
    area = input("请输入要查询的地区：")
    print("您要查询的地区是：", area)
    date1 = input("请输入要查询的日期：")
    print("您要查询的日期是：",date1)
    searched_values = np.array([area, date1])  
    for i in range(country_label.shape[0]):          #循环total_label找到对应的index
        if ((country_label[i] == searched_values).all()):
            break
    print ("当日该地区累计死亡率为：",country_data[i,2]/country_data[i,0] )  #根据index计算死亡率

else:
    print("您输入的模式不正确")















