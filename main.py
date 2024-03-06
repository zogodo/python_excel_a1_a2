import xlrd
import xlwt

excel_src_parh = './src.xlsx'
excel_new_path = './new.xlsx'

excel_src = xlrd.open_workbook(excel_src_parh)
sheet_src = excel_src.sheet_by_name('源数据')
# sheet_src = excel_src.sheets()[0] #打开第一个表


print(sheet_src.cell_value(1, 2))


excel_new = xlwt.Workbook(encoding='utf-8')
sheet_new = excel_new.add_sheet('new')

sheet_new.write(0, 0, 'CC')

excel_new.save(excel_new_path) #如果文件已存在会被覆盖,执行此句python时,不能打开new.xlsx
