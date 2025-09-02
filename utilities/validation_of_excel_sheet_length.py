import openpyxl

def validate_excel_file(path: str):
    wb = openpyxl.load_workbook(path)
    sheet = wb.active
    max_row = sheet.max_row
    assert max_row > 1, f"Excel file at {path} seems to be empty or has only headers."
    return max_row

