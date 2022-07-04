import os
import csv
import xlrd



class StatisticElectric(object):
    def __init__(self, data_file_path="./datas/cph.xlsx", sheet_name = "cph"):
        workbook = xlrd.open_workbook(data_file_path)
        workbook.sheet_by_name(sheet_name)
        
