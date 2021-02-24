import openpyxl
from openpyxl.worksheet.worksheet import Worksheet


class ExcelHandle:
    def __init__(self, fpath):
        self.fpath = fpath

    def read(self, sheet_name):
        wb = openpyxl.open(self.fpath)
        ws = wb[sheet_name]
        data = list(ws.values)

        header = data[0]
        all_data = []
        for row in data[1:]:
            row_dict = dict(zip(header, row))
            all_data.append(row_dict)
        return all_data

    def write(self, sheet, data, column, row):
        write_wb = openpyxl.load_workbook(self.fpath)
        write_ws: Worksheet = write_wb[sheet]
        write_ws.cell(row=row, column=column).value = data
        write_wb.save(self.fpath)
        write_wb.close()
