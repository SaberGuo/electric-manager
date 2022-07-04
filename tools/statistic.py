import os
import csv
import xlrd



class StatisticElectric(object):
    '''
    func: 完成任务1，用来统计相关用户的平均缴费金额和平均缴费次数
            平均缴费金额:
            平均缴费次数:
    '''
    def __init__(self, data_file_path="./datas/cph.xlsx", sheet_name = "cph"):
        workbook = xlrd.open_workbook(data_file_path)
        self.sh = workbook.sheet_by_name(sheet_name)

        self.init_data_sheet()
        

    def init_data_sheet(self):
        self.data_dict = {}
        for rx in range(1,self.sh.nrows):
            user_id = self.sh.cell_value(rx, 0)  #用户编号 1000000001
            fee_time = self.sh.cell_value(rx, 1) #缴费时间 月/日/年
            fee = self.sh.cell_value(rx, 2) #费用 元
            if user_id in self.data_dict.keys():
                self.data_dict[user_id] = [(fee_time, fee)]
            else:
                self.data_dict[user_id].append((fee_time, fee))



    def get_average_count_fee(self):
        #获取平均缴费次数和缴费金额
        if self.data_dict:
            user_count = 0
            total_fee_count = 0
            total_fee = 0
            for key, item in self.data_dict.items():
                user_count+=1
                total_fee_count+=len(item)
                for f_time, fee in item:
                    total_fee+=fee
            
            return total_fee_count/user_count, total_fee/user_count
