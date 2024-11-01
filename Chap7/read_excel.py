# read_excel.py
# Streamlining Your Research Laboratory with Python
# Authors:   Mark F. Russo, Ph.D and William Neil 
# Publisher: John Wiley & Sons, Inc.
# License:   MIT (https://opensource.org/licenses/MIT)

import openpyxl as xl

def read_picklists(name):
    wb = xl.load_workbook(name)
    ws = wb['picklists']
    # ws = wb.worksheets[0]
    # print(ws.title)
    
    for row in ws.rows:
        for cell in row:
            print(cell.value, end=' ')
        print()

    # for row in ws.rows:
    #     print(row[0].value)

if __name__ == '__main__':
    read_picklists("table2.xlsx")
