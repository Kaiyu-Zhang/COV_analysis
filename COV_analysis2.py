import numpy as np
from matplotlib import pyplot as plt

#导入数据
country_label=np.array(np.loadtxt('./COVID_extra.csv',dtype=str,delimiter=',',skiprows=1,usecols=(2),encoding='utf-8'))
country_data=np.array(np.loadtxt('./COVID_extra.csv',dtype=float ,delimiter=',',skiprows=1,usecols=(4,5,6,7),encoding='utf-8'))
China_label=np.array(np.loadtxt('./COVID_basedata.csv',dtype=str,delimiter=',',skiprows=1,usecols=(1,3,5),encoding='utf-8'))
China_data=np.array(np.loadtxt('./COVID_basedata.csv',dtype=float,delimiter=',',skiprows=1,usecols=(7,8,9,10),encoding='utf-8'))
#同理，定义查找数组和index数组
search_China =  np.array(["China"])
search_Japan = np.array(["Japan"])
search_Korea = np.array(["South Korea"])
index_China = []
index_Japan = []
index_Korea = []

#中国的数据处理
for i in range(country_label.shape[0]):  
    if ((country_label[i] == search_China ).all()):
        index_China.append(i)
x_China = range(len(index_China ) )   #定义横纵坐标
y_China_total = []
for i in index_China:      
    y_China_total.append(country_data[i,2]/country_data[i,0] )
    # y_China_total.append(country_data[i,2] )
    # y_China_total.append(country_data[i,1] )


#日本的数据处理
for i in range(country_label.shape[0]):     
    if ((country_label[i] == search_Japan ).all()):
        index_Japan.append(i)
x_Japan = range(len(index_Japan  ) )     #定义横纵坐标
y_Japan_total = []
for i in index_Japan:             
    y_Japan_total.append(country_data[i,2]/country_data[i,0])
    # y_Japan_total.append(country_data[i,2])
    # y_Japan_total.append(country_data[i,1])

#韩国的数据预处理
for i in range(country_label.shape[0]):
    if ((country_label[i] == search_Korea).all()):
        index_Korea.append(i)
x_Korea = range(len(index_China ) )     #定义横纵坐标
y_Korea_total = []
for i in index_Korea:
    y_Korea_total.append(country_data[i,2]/country_data[i,0] )
    # y_Korea_total.append(country_data[i,2] )
    # y_Korea_total.append(country_data[i,1] )

#作图
plt.title("Total deaths rate number comparison")
plt.xlabel("date")
plt.ylabel("Patient quantity")
plt.plot(x_China ,y_China_total)
plt.plot(x_Japan ,y_Japan_total )
plt.plot(x_Korea ,y_Korea_total )
plt.show()

# #作图
# plt.title("Total deaths number comparison")
# plt.xlabel("date")
# plt.ylabel("Patient quantity")
# plt.plot(x_China ,y_China_total)
# plt.plot(x_Japan ,y_Japan_total )
# plt.plot(x_Korea ,y_Korea_total )
# plt.show()

# #作图
# plt.title("New patient number comparison")
# plt.xlabel("date")
# plt.ylabel("Patient quantity")
# plt.plot(x_China ,y_China_total)
# plt.plot(x_Japan ,y_Japan_total )
# plt.plot(x_Korea ,y_Korea_total )
# plt.show()
