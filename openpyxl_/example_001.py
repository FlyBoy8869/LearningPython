from pprint import pprint as pp
import openpyxl

FILENAME = "234300-3 Robot Quote Log.xlsx"

wb = openpyxl.load_workbook(FILENAME, read_only=False, keep_vba=True)
ws = wb.active
# pp(dir(wb))
print(f"workbook sheets: {wb.sheetnames}")
pp(dir(ws))
# print(ws.print_title_rows)

wb.close()
