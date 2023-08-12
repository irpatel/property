import openpyxl

def generate_excel(data):
    workbook = openpyxl.Workbook()
    sheet = workbook.active

    # Implement logic to generate Excel file using data
    # You can use data from the get_utility_records() function

    return workbook
