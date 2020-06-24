import numpy as np
from matplotlib import pyplot as plt

#导入数据
country_label=np.array(np.loadtxt('./COVID_extra.csv',dtype=str,delimiter=',',skiprows=1,usecols=(2),encoding='utf-8'))
country_data=np.array(np.loadtxt('./COVID_extra.csv',dtype=float ,delimiter=',',skiprows=1,usecols=(4,5,6,7),encoding='utf-8'))

#同理，定义查找数组和index数组
search_China =  np.array(["China"])
index_China = []
search_USA = np.array(["United States"])
index_USA = []
search_UK = np.array(["United Kingdom"])
index_UK = []
search_German = np.array(["Germany"])
index_German = []
search_Brazil = np.array(["Brazil"])
index_Brazil = []
search_Norway = np.array(["Norway"])
index_Norway = []









#中国的数据处理
for i in range(country_label.shape[0]):
    if ((country_label[i] == search_China ).all()):
        index_China.append(i)
x_China = range(len(index_China ) )
y_China_total = []
for i in index_China:
    y_China_total.append(country_data[i,2]/country_data[i,0] )
    # y_China_total.append(country_data[i,2] )
    # y_China_total.append(country_data[i,1] )


#美国的数据处理
for i in range(country_label.shape[0]):
    if ((country_label[i] == search_USA ).all()):
        index_USA.append(i)
x_USA = range(len(index_USA ) )
y_USA_total = []
for i in index_USA:
    y_USA_total.append(country_data[i,2]/country_data[i,0] )
    # y_USA_total.append(country_data[i,2] )
    # y_USA_total.append(country_data[i,1] )


#英国的数据处理
for i in range(country_label.shape[0]):
    if ((country_label[i] == search_UK  ).all()):
        index_UK.append(i)
x_UK = range(len(index_UK ) )
y_UK_total = []
for i in index_UK:
    y_UK_total.append(country_data[i,2]/country_data[i,0] )
    # y_UK_total.append(country_data[i,2] )
    # y_UK_total.append(country_data[i,1] )


#德国的数据处理
for i in range(country_label.shape[0]):
    if ((country_label[i] == search_German ).all()):
        index_German.append(i)
x_German = range(len(index_German ) )
y_German_total = []
for i in index_German:
    y_German_total.append(country_data[i,2]/country_data[i,0] )
    # y_German_total.append(country_data[i,2] )
    # y_German_total.append(country_data[i,1] )


#巴西的数据处理
for i in range(country_label.shape[0]):
    if ((country_label[i] == search_Brazil ).all()):
        index_Brazil.append(i)
x_Brazil = range(len(index_Brazil ) )
y_Brazil_total = []
for i in index_Brazil:
    y_Brazil_total.append(country_data[i,2]/country_data[i,0] )
    # y_Brazil_total.append(country_data[i,2] )
    # y_Brazil_total.append(country_data[i,1] )

#挪威的数据处理
for i in range(country_label.shape[0]):
    if ((country_label[i] == search_Norway ).all()):
        index_Norway.append(i)
x_Norway = range(len(index_Norway ) )
y_Norway_total = []
for i in index_Norway:
    y_Norway_total.append(country_data[i,2]/country_data[i,0] )
    # y_Norway_total.append(country_data[i,2] )
    # y_Norway_total.append(country_data[i,1] )


#作图
plt.title("Total deaths rate number comparison")
plt.xlabel("date")
plt.ylabel("Patient quantity")
plt.plot(x_China ,y_China_total)
plt.plot(x_USA ,y_USA_total )
plt.plot(x_UK ,y_UK_total )
plt.plot(x_German ,y_German_total)
plt.plot(x_Brazil ,y_Brazil_total )
plt.plot(x_Norway ,y_Norway_total )
plt.show()

# #作图
# plt.title("Total deaths number comparison")
# plt.xlabel("date")
# plt.ylabel("Patient quantity")
# plt.plot(x_China ,y_China_total)
# plt.plot(x_USA ,y_USA_total )
# plt.plot(x_UK ,y_UK_total )
# plt.plot(x_German ,y_German_total)
# plt.plot(x_Brazil ,y_Brazil_total )
# plt.plot(x_Norway ,y_Norway_total )
# plt.show()

# #作图
# plt.title("New case number comparison")
# plt.xlabel("date")
# plt.ylabel("Patient quantity")
# plt.plot(x_China ,y_China_total)
# plt.plot(x_USA ,y_USA_total )
# plt.plot(x_UK ,y_UK_total )
# plt.plot(x_German ,y_German_total)
# plt.plot(x_Brazil ,y_Brazil_total )
# plt.plot(x_Norway ,y_Norway_total )
# plt.show()
