import openpyxl


wb = openpyxl.load_workbook("transactions.xlsx")
print(wb.sheetnames)
sheet = wb["Sheet1"]
cell = sheet["a1"]
print(cell.value)
print(sheet[1: 3])
sheet.append([1, 2, 3])
wb.save("transactions2.xlsx")
