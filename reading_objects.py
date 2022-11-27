import xlrd
from Library.config import Config
path = Config.Data_path


def read_locators():
    workbook = xlrd.open_workbook(Config.Data_path)
    worksheet = workbook.sheet_by_name('offers_module')
    rows = worksheet.get_rows()
    print(rows)
    header = next(rows)
    d = {}
    for row in rows:
        d[row[0].value] = (row[1].value, row[2].value)
    return d


print(read_locators())