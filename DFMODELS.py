#-*-coding:utf8-*-
#user:brian
#created_at:2018/7/12 16:16
# file: 22.py
#location: china chengdu 610000
from PyQt5 import QtWidgets,QtGui
import sys
from mainwindow import Ui_MainWindow
from PyQt5.QtWidgets import QFileDialog
import time
import pandas as pd
from scipy import stats
import statsmodels.api as sm
import matplotlib.pyplot as plt
index_list=["x1","x2","x3","x4","x5","x6","x7","x8","x9","x10","x11","x12","x13","x14","x15","x16","x17","x18","x19","x20"]
variable_names=["C","x1","x2","x3","x4","x5","x6","x7","x8","x9","x10","x11","x12","x13","x14","x15","x16","x17","x18","x19","x20"]
class mywindow(QtWidgets.QMainWindow,Ui_MainWindow):
    def __init__(self):
        super(mywindow,self).__init__()
        self.setupUi(self)
        self.bianlianggeshu=None
        self.Kzhi=None
        self.modelname=None
        self.ZHIxingdu=None
        self.inputfilename=None
        self.outputfilename=None
        self.result_Dengfen=None
        self.models=None
        self.x11=None
        self.x12=None
        self.x13=None
        self.x14=None
    # 定义槽函数
    def hello(self):
        self.textEdit.setText("hello world")

    def plotmap(self):
        self.write_2_text(" 开始画图...\n")
        try:
            self.models.DFMODELplot(self.result_Dengfen,self.x11,self.x12,self.x13,self.x14)
            self.write_2_text(" 画图完成...\n")
        except:
            self.write_2_text(" 画图失败...\n")


    def opencsvfiles(self):
        fileName1, filetype = QFileDialog.getOpenFileName(self,
                                                          "选取要打开的数据文件","./","CSV Files (*.csv)")  # 设置文件扩展名过滤,注意用双分号间隔
        print(fileName1, filetype)
        self.inputfilename = fileName1

        self.textBrowser.setText(fileName1)
        # self.write_2_text(fileName1)
        self.write_2_text("加载数据输入文件%s成功!\n"%fileName1)
    def savepara(self):
        # 置信度  变量个数 模型名称 分段k值
        # self.bianlianggeshu=self.comboBox_2.currentText()
        # self.Kzhi=self.comboBox_4.currentText()
        # self.modelname=self.comboBox_3.currentText()
        # self.ZHIxingdu=self.comboBox.currentText()

        # self.textBrowser_3.show(self.comboBox.currentText())
        result_model=u"模型参数选择结果:\n" \
                     u"置信度=%s \n" \
                     u"变量个数=%s \n" \
                     u"模型选择=%s\n"\
                     u"分段K值=%s\n"%(self.comboBox.currentText(),self.comboBox_2.currentText(),
                                   self.comboBox_3.currentText(),self.comboBox_4.currentText(),
                                                                 )
        self.write_2_text(result_model)
        self.write_2_text("保存参数成功！")
    def Ftest(self):
        fileName3, filetype = QFileDialog.getOpenFileName(self,
                                                          "选取F检验结果文件(CSV格式)", "./", "CSV Files (*.csv)")

        self.write_2_text("F检验文件结果保存在%s，开始计算！"%fileName3)
        model_names_set=list(set(self.result_Dengfen["b_model_name"].tolist()))
        NNN=len(model_names_set)
        modes_t=[]
        p_values=[]
        F_statist=[]
        try:
            for i in range(NNN):
                for j in range(i+1,NNN):
                    temp1_name=model_names_set[i]
                    temp2_name=model_names_set[j]
                    values1=self.result_Dengfen[self.result_Dengfen["b_model_name"] == temp1_name]["coef_all"].tolist()
                    values2=self.result_Dengfen[self.result_Dengfen["b_model_name"] == temp2_name]["coef_all"].tolist()
                    modes_t.append("%s-%s"%(temp1_name,temp2_name))
                    F_test_all_values = stats.ttest_ind(values1, values2, equal_var=False)
                    p_values.append(F_test_all_values.pvalue)
                    F_statist.append(F_test_all_values.statistic)
            result_f_test=pd.DataFrame({"a_modes_t":modes_t,"b_p_values":p_values,"c_F_statist":F_statist})
            result_f_test.to_csv(fileName3)
            index_out = "模型    p检验值   F检验值"
            self.write_2_text("\n", 0)
            self.write_2_text(index_out, 0)
            for i in range(result_f_test.shape[0]):
                outfiles="%s     %s     %s"%(result_f_test.iloc[i, 0],result_f_test.iloc[i, 1],result_f_test.iloc[i, 2])
                self.write_2_text(outfiles, 0)
            self.write_2_text("F检验计算完成并保存成功！")
        except:
            self.write_2_text("F检验计算失败")

    def savepicturepara(self):
        self.x11 = int(self.comboBox_5.currentText())
        self.x12 = int(self.comboBox_6.currentText())
        self.x13 = int(self.comboBox_7.currentText())
        self.x14 = int(self.comboBox_8.currentText())
        x1=int(self.comboBox_5.currentText())
        x2 = int(self.comboBox_6.currentText())
        x3 = int(self.comboBox_7.currentText())
        x4 = int(self.comboBox_8.currentText())
        if x1==0:
            x1=""
        else:
            x1="a*x"
        if x2==0:
            x2=""
        else:
            x2="b*x^2"
        if x3==0:
            x3=""
        else:
            x3="b*x^3"
        if x4==0:
            x4=""
        else:
            x4="b*x^4"
        result_y="多项式为：%s + %s+ %s + %s  (其中a为常数项估计参数，b为对应变量估计系数)"%(x1,x2,x3,x4)
        self.write_2_text(result_y)
        self.write_2_text("保存多项式成功！")
        pass
    def write_2_text(self,items,flag=1):
        cursor = self.textBrowser_3.textCursor()
        cursor.movePosition(QtGui.QTextCursor.End)
        times_now=self.timestamp_to_date(time.time())
        if flag:
            cursor.insertText("%s: "%times_now)
        cursor.insertText(items)
        cursor.insertText("\n")
        self.textBrowser_3.setTextCursor(cursor)

    def timestamp_to_date(self,time_stamp, format_string="%Y-%m-%d %H:%M:%S"):
        time_array = time.localtime(time_stamp)
        str_date = time.strftime(format_string, time_array)
        return str_date
    def outfiles(self):
        fileName2, filetype = QFileDialog.getOpenFileName(self,
                                                          "选取要保存的结果文件(CSV格式)","./","CSV Files (*.csv)")  # 设置文件扩展名过滤,注意用双分号间隔
        print(fileName2, filetype)
        self.outputfilename = fileName2 #输出文件位置及名称
        self.textBrowser_2.setText(fileName2)
        # self.write_2_text(fileName1)
        self.write_2_text("加载结果保存文件%s成功! \n"%fileName2)
    def modelcal(self):
        self.write_2_text(" 开始计算...\n")
        print("开始计算")
        geshu=self.bianlianggeshu = self.comboBox_2.currentText()
        fenduan=self.Kzhi = self.comboBox_4.currentText()
        # self.modelname = self.comboBox_3.currentText()
        zhixn=self.ZHIxingdu = self.comboBox.currentText()
        infile=self.inputfilename
        outfile=self.outputfilename
        try:
            self.models=DFMODELS(infile,int(geshu),float(zhixn),int(fenduan),outfile)
            self.result_Dengfen = self.models.denfeng_model()
            self.write_2_text(" 参数计算完毕...\n")
            self.write_2_text("\n",0)
            index_out="变量名称     模型名称    回归系数     p检验值   t检验值"
            self.write_2_text("\n", 0)
            self.write_2_text(index_out,0)
            for i in range(self.result_Dengfen.shape[0]):

                out_file="%4s    %15s    %.2f    %.2f     %.2f"%(self.result_Dengfen.iloc[i, 0],self.result_Dengfen.iloc[i, 1],self.result_Dengfen.iloc[i,2]
                                                   ,self.result_Dengfen.iloc[i, 4],self.result_Dengfen.iloc[i, 6])
                self.write_2_text(out_file,0)
        except:
            self.write_2_text("计算失败，请检查参数设置和变量个数,以及文件夹路径不要出现中文")


class DFMODELS():
    def __init__(self,openfilename,variablecount,confid,K_alpha,savefilename):
        """
        :param filename: 文件名称
        :param variablecount: 变量个数
        :param confid: 置信度
        :param K_alpha: 几等分
        """
        self.X = variablecount # 表示变量个数
        self.data = pd.read_csv(openfilename, header=0)
        self.N = self.data.shape[0]  # 数据的条数
        self.new_index = index_list[0:self.X]
        self.new_index.append("Y")
        self.data.columns = self.new_index
        self.K_alpha = K_alpha  # 表示分为3份
        self.delta = int(self.N / self.K_alpha)  # 表示每一份数据的数量
        self.count = self.N - self.delta - 1  # 表示平移的补数
        self.data_x=self.data[self.new_index[0:-1]]
        self.data_y=self.data[self.new_index[-1]]
        self.confid=confid
        self.savefilenames=savefilename
        self.x11=None
        self.x12=None
        self.x13=None
        self.x14=None
    def one_lm_modle(self,data_x, data_y, modelname):
        """ #单一的回归模型计算函数
        :param data_x: 输入的数据x
        :param data_y: 输入的变量y
        :param N: 数据的总条数
        :param C: 置信度
        :param modelname:模型的名称
        :return: 返回单个的模型的计算结果
        """
        data_x = sm.add_constant(data_x)  # 增加一个常数变量
        mod = sm.OLS(data_y, data_x)
        res = mod.fit()
        print(res.summary())
        # res.bse   res.params  res.tvalues  res.pvalues
        coef_all = res.params.tolist()  # 求出来的模型系数，也是系数的平均值
        std_all = res.bse.tolist()  # 方差
        t_all = res.tvalues.tolist()  # t检验的值
        p_all = res.pvalues.tolist()  # 概率p值
        up_conf_all = []
        down_conf_all = []
        model_name = []
        # print(coef_all,std_all,t_all,p_all)
        # 依次求每一个系数的置信度的值
        variable_name = variable_names[0:len(coef_all)]
        print(variable_name)
        for i in range(len(coef_all)):
            model_name.append(modelname)
            mean = coef_all[i]
            std = std_all[i]
            interval = stats.t.interval(self.confid, self.N - 1, mean, std)
            down_conf = interval[0]
            up_conf = interval[1]
            up_conf_all.append(up_conf)  # 置信度上限
            down_conf_all.append(down_conf)  # 置信度下线
        result = pd.DataFrame(
            {"a_variable_name": variable_name, "b_model_name": model_name, "coef_all": coef_all, "std_all": std_all,
             "t_all": t_all, "p_all": p_all, "down_conf_all": down_conf_all
                , "up_conf_all": up_conf_all})
        print(result)
        return result

    def denfeng_model(self):
        """
        :param data_x: 原始数据处理后的x,汇总后整个的X
        :param data_y: 原始数据处理后的y，所有Y
        :param N: 数据的总条数
        :param confid: 模型的置信度
        :param count: 模型等分后的个数也就是step
        :return: 计算好的datafram矩阵
        """
        result_orinignal = self.one_lm_modle(self.data_x, self.data_y, "modelorinagnal")
        for i in range(0, self.count):
            modelname = "model" + str(i)  # 定义新的模型的名称
            data_x_temp = self.data_x.ix[i:i + self.delta - 1, :]
            data_y_temp = self.data_y[i:i + self.delta]
            result_temp = self.one_lm_modle(data_x_temp, data_y_temp, modelname)
            result_orinignal = result_orinignal.append(result_temp)
        print(result_orinignal)
        result_orinignal.to_csv(self.savefilenames)
        return (result_orinignal)

    def DFMODELplot(self,result_Dengfen,x11,x12,x13,x14):
        X=self.X
        ori_coef = result_Dengfen[result_Dengfen["b_model_name"] == "modelorinagnal"]["coef_all"].tolist()
        ori_up = result_Dengfen[result_Dengfen["b_model_name"] == "modelorinagnal"]["up_conf_all"].tolist()
        ori_down = result_Dengfen[result_Dengfen["b_model_name"] == "modelorinagnal"]["down_conf_all"].tolist()
        # count 表示模型的数量
        for modelx in range(0, X):
            index_plot = " "
            if X < 5:
                index_plot = "22" + str(modelx + 1)
            if X < 7 and X > 4:
                index_plot = "23" + str(modelx + 1)
            if X == 8:
                index_plot = "24" + str(modelx + 1)
            if X > 8:
                index_plot = "33" + str(modelx + 1)
                if modelx > 9:
                    index_plot = "33" + str(modelx - 9 + 1)
                if modelx > 18:
                    index_plot = "33" + str(modelx - 18 + 1)

            plt.subplot(int(index_plot))
            x_label = range(self.count + 1)
            variable_x = index_list[modelx]
            #需要进行平方处理的置信度上下线以及原来的线
            up_config_x_1 = result_Dengfen[result_Dengfen["a_variable_name"] == variable_x]["up_conf_all"].tolist()
            downconfig_x_1 = result_Dengfen[result_Dengfen["a_variable_name"] == variable_x]["down_conf_all"].tolist()
            coef_x_1 = result_Dengfen[result_Dengfen["a_variable_name"] == variable_x]["coef_all"].tolist()
            constant_x_1=result_Dengfen[result_Dengfen["a_variable_name"] == "C"]["coef_all"].tolist()

            def magnifi(x,c,y):
                result=[]
                for i in range(len(x)):
                    temp=0
                    if x11!=0:
                        temp+=c[i]*x[i]
                    if x12!=0:
                        temp+=y[i]*x[i]*x[i]
                    if x13!=0:
                        temp+=y[i]*x[i]*x[i]
                    if x14!=0:
                        temp+=y[i]*x[i]+x[i]+x[i]
                    result.append(temp)
                return result

            up_config_x=magnifi(x_label,constant_x_1,up_config_x_1)
            downconfig_x=magnifi(x_label,constant_x_1,downconfig_x_1)
            coef_x=magnifi(x_label,constant_x_1,coef_x_1)
            ori_coef_x = ori_coef[modelx + 1]
            ori_up_x = ori_up[modelx + 1]
            ori_down_x = ori_down[modelx + 1]
            # print(len(x_label),len(variable_x),len(up_config_x))
            plt.plot(x_label, up_config_x, '+', color='black')
            plt.plot(x_label, downconfig_x, '+', color='black')

            plt.fill_between(x_label, up_config_x, downconfig_x, color='blue', alpha=0.25)
            print(ori_coef_x, ori_up_x, ori_down_x)
            plt.plot(x_label, coef_x, color='black')
            plt.hlines(ori_coef_x, 0, self.count + 1, colors="red")
            plt.hlines(ori_up_x, 0, self.count + 1, colors="green", linestyles='--')
            plt.hlines(ori_down_x, 0, self.count + 1, colors="green", linestyles='--')
            plt.ylabel(index_list[modelx])
            plt.xlabel("step")
            if X < 5:
                if modelx == X - 1:
                    plt.show()
            if X < 7 and X > 4:
                if modelx == X - 1:
                    plt.show()
            if X == 8:
                if modelx == X - 1:
                    plt.show()
            if X > 8:
                if modelx == 9 and X == 9:
                    plt.show()
                if modelx > 9 and modelx < 18 and modelx == X - 1:
                    plt.show()
                if modelx > 18 and modelx < 27 and modelx == X - 1:
                    plt.show()
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = mywindow()
    window.show()
    sys.exit(app.exec_())