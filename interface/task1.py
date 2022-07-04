from tools.statistic import StatisticElectric
import sys

def main(data_file_path="./datas/cph.xlsx", sheet_name = "cph"):
    se = StatisticElectric(data_file_path, sheet_name)
    avg_count, avg_fee = se.get_average_count_fee()
    print("average count:", avg_count)
    print("average fee:", avg_fee)
    #todo:写入到csv中



if __name__ == "__main__":
    data_file_path = sys.argv[1]
    sheet_name = sys.argv[2]
    main(data_file_path, sheet_name)
