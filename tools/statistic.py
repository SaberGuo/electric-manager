from audioop import avg
import os
import csv
import openpyxl



class StatisticElectric(object):
    '''
    func: 完成任务1，用来统计相关用户的平均缴费金额和平均缴费次数
            平均缴费金额:
            平均缴费次数:
    '''
    def __init__(self, data_file_path="./datas/cph.xlsx", sheet_name = "cph"):
        workbook = openpyxl.load_workbook(data_file_path)
        self.sh = workbook.get_sheet_by_name(sheet_name)

        self.init_data_sheet()
        

    def init_data_sheet(self):
        self.data_dict = {}
        first = True
        for rx in self.sh.rows:
            if first:
                first = False
                continue
            user_id = str(rx[0].value)  #用户编号 1000000001
            fee_time = str(rx[1].value) #缴费时间 月/日/年
            fee = float(rx[2].value) #费用 元
            
            if user_id in self.data_dict.keys():
                self.data_dict[user_id].append((fee_time, fee))
            else:
                self.data_dict[user_id] = [(fee_time, fee)]



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


if __name__ == "__main__":
    se = StatisticElectric()
    avg_count, avg_fee = se.get_average_count_fee()
    print("average count:", avg_count)
    print("average fee:", avg_fee)