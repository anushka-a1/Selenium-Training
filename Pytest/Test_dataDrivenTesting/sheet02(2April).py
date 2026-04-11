# how the data is fetched
import openpyxl
def func1():
    wb=openpyxl.load_workbook(r"C:\Users\user\OneDrive\Desktop\Selenium\sample.xlsx")
    ws=wb["Sheet1"]
    data=[]
    for row in ws.iter_rows(min_row=2,values_only=True):
        data.append(row)
    return data
