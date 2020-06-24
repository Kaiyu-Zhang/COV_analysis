import numpy as np
from matplotlib import pyplot as plt


#导入数据
China_label=np.array(np.loadtxt('./COVID_basedata.csv',dtype=str,delimiter=',',skiprows=1,usecols=(1,3,5),encoding='utf-8'))
China_data=np.array(np.loadtxt('./COVID_basedata.csv',dtype=float,delimiter=',',skiprows=1,usecols=(7,8,9,10),encoding='utf-8'))

#这里通过searched_XXX来标记查找规律的数据，index列表用于存储对应数据
searched_hubei = np.array(["中国","湖北省",""])
index_hubei = []
searched_wuhan = np.array(["中国","湖北省","武汉市"])
index_wuhan = []
searched_China = np.array(["中国","",""])
index_China = []


for i in range(China_label.shape[0]):  #这里通过label找到对应的湖北省数据的所有index
    if ((China_label[i] == searched_hubei).all()):
        index_hubei.append(i)
x_hubei = range(len(index_hubei))   #定义横纵坐标
y_hubei_total = []
for i in index_hubei:     #导入数组列表
    y_hubei_total.append(China_data[i,0]-China_data[i,2]-China_data[i,3] )
    #y_hubei_total.append(China_data[i,0] )


for i in range(China_label.shape[0]):   #这里通过label找到对应的武汉市数据的所有index
    if ((China_label[i] == searched_wuhan).all()):
        index_wuhan.append(i)
x_wuhan = range(len(index_wuhan))     #定义横纵坐标
y_wuhan_total = []
for i in index_wuhan:       #导入数组列表
    y_wuhan_total.append(China_data[i,0]-China_data[i,2]-China_data[i,3] )
    #y_wuhan_total.append(China_data[i,0] )


for i in range(China_label.shape[0]):   #这里通过label找到国内的总数据的index
    if ((China_label[i] == searched_China ).all()):
        index_China.append(i)
x_China = range(len(index_China ) )   #定义横纵坐标
y_China_total = []
for i in range(len(index_China )):   
    #这里计算的是国内其他地区的数据，方法为用全国的数据减去湖北省的数据
    x = China_data[index_China[i] ,0]-China_data[index_China[i] ,2]-China_data[index_China [i],3]-(China_data[index_hubei[i] ,0]-China_data[index_hubei[i] ,2]-China_data[index_hubei[i] ,3])
    y_China_total.append(x)
    #x = China_data[index_China[i] ,0]-(China_data[index_hubei[i] ,0])
    #y_China_total.append(x)

#作图
plt.title("Current patient number comparison")
plt.xlabel("date")
plt.ylabel("Patient quantity")
plt.plot(x_hubei ,y_hubei_total )
plt.plot(x_wuhan ,y_wuhan_total )
plt.plot(x_China ,y_China_total )
plt.show()


# #作图
# plt.title("Cumulative number of patients cured")
# plt.xlabel("date")
# plt.ylabel("Patient quantity")
# plt.plot(x_hubei ,y_hubei_total )
# plt.plot(x_wuhan ,y_wuhan_total )
# plt.plot(x_China ,y_China_total )
# plt.show()
