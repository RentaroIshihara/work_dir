# views.py
from django.http import HttpResponse
from openpyxl import Workbook
from .models import MyModel

def export_to_excel(request):
    # Create a workbook and a worksheet
    wb = Workbook()
    ws = wb.active
    
    # Add column headers to the worksheet
    columns = ['Column1', 'Column2', 'Column3']  # ここは実際のモデルフィールドに合わせてください
    ws.append(columns)
    
    # Retrieve data from the database
    data = MyModel.objects.all()  # モデルに応じてクエリを調整してください
    
    # Populate the worksheet with data
    for item in data:
        row = [item.field1, item.field2, item.field3]  # 実際のフィールドに合わせて取得してください
        ws.append(row)
    
    # Save the workbook to a response
    response = HttpResponse(content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="my_data.xlsx"'
    wb.save(response)
    
    return response
