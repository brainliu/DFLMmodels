#-*-coding:utf8-*-
#user:brian
#created_at:2018/7/17 14:51
# file: dengfgenxianxiong.py
#location: china chengdu 610000
import pandas as pd
from scipy import stats
import statsmodels.api as sm
import matplotlib.pyplot as plt
#模型要用到的常量
index_list=["x1","x2","x3","x4","x5","x6","x7","x8","x9","x10","x11","x12","x13","x14","x15","x16","x17","x18","x19","x20"]
variable_names=["C","x1","x2","x3","x4","x5","x6","x7","x8","x9","x10","x11","x12","x13","x14","x15","x16","x17","x18","x19","x20"]


X=4 #表示变量个数
data=pd.read_csv("7.csv",header=0)
N=data.shape[0] #数据的条数
new_index=index_list[0:X]
new_index.append("Y")
data.columns=new_index
K_alpha=2 #表示分为3份
delta=int(N/K_alpha) #表示每一份数据的数量
count=N-delta-1 #表示平移的补数

# index_data=data.columns.tolist()
# print(data.columns.tolist())
# print(data.columns.tolist())
data_x=data[new_index[0:-1]]
data_y=data[new_index[-1]]

###########
  #调用statsmodels里面的api，通过api调用相当于调用了statsmodels.regression.linear_model，可以使用linear_model文件里的函数
# Fit and summarize OLS model
#定义一个标准的求解OLS模型函数，用这个函数可以得到置信度下参数估计的结果
def one_lm_modle(data_x,data_y,N,C,modelname):
    """ #单一的回归模型计算函数
    :param data_x: 输入的数据x
    :param data_y: 输入的变量y
    :param N: 数据的总条数
    :param C: 置信度
    :param modelname:模型的名称
    :return: 返回单个的模型的计算结果
    """
    data_x=sm.add_constant(data_x) #增加一个常数变量
    mod = sm.OLS(data_y, data_x)
    res = mod.fit()
    print(res.summary())
    #res.bse   res.params  res.tvalues  res.pvalues
    coef_all=res.params.tolist() #求出来的模型系数，也是系数的平均值
    std_all=res.bse.tolist() #方差
    t_all=res.tvalues.tolist()#t检验的值
    p_all=res.pvalues.tolist()#概率p值
    up_conf_all=[]
    down_conf_all=[]
    model_name=[]
    # print(coef_all,std_all,t_all,p_all)
    #依次求每一个系数的置信度的值
    variable_name=variable_names[0:len(coef_all)]
    print(variable_name)
    for i in range(len(coef_all)):
        model_name.append(modelname)
        mean=coef_all[i]
        std=std_all[i]
        interval=stats.t.interval(C,N-1,mean,std)
        down_conf=interval[0]
        up_conf=interval[1]
        up_conf_all.append(up_conf) #置信度上限
        down_conf_all.append(down_conf)#置信度下线
    result=pd.DataFrame({"a_variable_name":variable_name,"b_model_name":model_name,"coef_all":coef_all,"std_all":std_all,
                         "t_all":t_all,"p_all":p_all,"down_conf_all":down_conf_all
                         ,"up_conf_all":up_conf_all})
    print(result)
    return result

# result2=one_lm_modle(data_x,data_y,N,0.95,"oriniganle1")
# result=result1.append(result2)
# print(result)



def denfeng_model(data_x,data_y,N,confid,count):
    """
    :param data_x: 原始数据处理后的x,汇总后整个的X
    :param data_y: 原始数据处理后的y，所有Y
    :param N: 数据的总条数
    :param confid: 模型的置信度
    :param count: 模型等分后的个数也就是step
    :return: 计算好的datafram矩阵
    """
    result_orinignal = one_lm_modle(data_x, data_y, N, confid, "modelorinagnal")
    for i in range(0,count):
        modelname="model"+str(i) #定义新的模型的名称
        data_x_temp=data_x.ix[i:i + delta - 1, :]
        data_y_temp = data_y[i:i+delta]
        result_temp=one_lm_modle(data_x_temp,data_y_temp,delta,0.95,modelname)
        result_orinignal=result_orinignal.append(result_temp)
    print(result_orinignal)
    return (result_orinignal)

#提取等分回归系数
#原来模型的系数以及置信度上下限制，以及等分模型各个变量的置信度上下限制
def DFMODELplot(result_Dengfen,X,index_list):
    """
    :param result_Dengfen: 所有的等分模型结果
    :param X: 变量个数
    :param index_list:初始的index_list 为常量
    :return: 图表
    """
    ori_coef=result_Dengfen[result_Dengfen["b_model_name"]=="modelorinagnal"]["coef_all"].tolist()
    ori_up=result_Dengfen[result_Dengfen["b_model_name"]=="modelorinagnal"]["up_conf_all"].tolist()
    ori_down=result_Dengfen[result_Dengfen["b_model_name"]=="modelorinagnal"]["down_conf_all"].tolist()
    #count 表示模型的数量
    for modelx in range(0,X):
        index_plot=" "
        if X<5:
            index_plot="22"+str(modelx+1)
        if X<7 and X>4:
            index_plot="23"+str(modelx+1)
        if X==8:
            index_plot = "24" + str(modelx + 1)
        if   X > 8:
            index_plot = "33" + str(modelx + 1)
            if modelx>9:
                index_plot = "33" + str(modelx-9 + 1)
            if modelx>18:
                index_plot = "33" + str(modelx - 18 + 1)

        plt.subplot(int(index_plot))
        x_label=range(count+1)
        variable_x=index_list[modelx]
        up_config_x=result_Dengfen[result_Dengfen["a_variable_name"]==variable_x]["up_conf_all"].tolist()
        downconfig_x=result_Dengfen[result_Dengfen["a_variable_name"]==variable_x]["down_conf_all"].tolist()
        coef_x=result_Dengfen[result_Dengfen["a_variable_name"]==variable_x]["coef_all"].tolist()

        ori_coef_x=ori_coef[modelx+1]
        ori_up_x=ori_up[modelx+1]
        ori_down_x=ori_down[modelx+1]
        # print(len(x_label),len(variable_x),len(up_config_x))
        plt.plot(x_label,up_config_x,'+',color='black')
        plt.plot(x_label, downconfig_x,'+',color='black')

        plt.fill_between(x_label, up_config_x, downconfig_x, color='blue', alpha=0.25)
        print(ori_coef_x,ori_up_x,ori_down_x)
        plt.plot(x_label, coef_x, color='black')
        plt.hlines(ori_coef_x, 0, count+1,colors="red")
        plt.hlines(ori_up_x, 0, count + 1,colors="green",linestyles='--' )
        plt.hlines(ori_down_x, 0, count + 1,colors="green",linestyles='--')
        plt.ylabel(index_list[modelx])
        plt.xlabel("step")
        if X<5:
            if modelx==X-1:
                plt.show()
        if X<7 and X>4:
            if modelx==X-1:
                plt.show()
        if X==8:
            if modelx==X-1:
                plt.show()
        if   X > 8 :
            if modelx==9 and X==9:
                plt.show()
            if modelx>9 and modelx<18 and modelx==X-1:
                plt.show()
            if modelx>18 and modelx<27 and modelx==X-1:
                plt.show()
                # plt.close()


def F_test():
    print("F检验结果：")
    for i in range(data.shape[1]-1):
        F_test=stats.ttest_ind(data_x.iloc[:,i], data_y, equal_var=False)
        print (F_test)
        #F_test.pvalue F_test.pvalue F_test.statistic

result_Dengfen=denfeng_model(data_x,data_y,N,0.95,count)
#
# print(1)
# DFMODELplot(result_Dengfen,X,index_list)
#
# F_test()

# F_test=stats.ttest_ind([1,2,3], [4,5,6], equal_var=False)
# print (F_test.pvalue,F_test.statistic)