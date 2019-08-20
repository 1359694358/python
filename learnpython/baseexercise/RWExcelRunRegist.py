import openpyxl

SheetName="login data"
accounts=[{"userName":"test1","password":"123456"},
          {"userName":"test2","password":"abcdef"},
          {"userName":"test3","password":"ghjikl"}]

workbook=openpyxl.Workbook()
sheet=workbook.active
sheet.title=SheetName
addTitle=False
for item in accounts:
    if not addTitle:
        itemValue=[]
        for key in item.keys():
            itemValue.append(key)
        sheet.append(itemValue)
        addTitle=True
    itemValue = []
    for key in item.values():
        itemValue.append(key)
    sheet.append(itemValue)
workbook.save("./logindata.xlsx")



