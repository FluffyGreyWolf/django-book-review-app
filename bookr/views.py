from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render

from plotly.offline import plot
import plotly.graph_objects as graphs

from io import BytesIO
import xlsxwriter

from .utils import get_books_read, get_books_read_by_month

def profile(request):
    return render(request, 'profile.html')

@login_required
def reading_history(request):
    user = request.user.username
    books_read = get_books_read(user)

    # Create an object to create files in memory
    temp_file = BytesIO()

    # Start a new workbook
    workbook = xlsxwriter.Workbook(temp_file)
    worksheet = workbook.add_worksheet()
    
    # Prepare the data to be written
    data = []
    for book_read in books_read:
        data.append([book_read['title'], str(book_read['completed_on'])])

    # Write data to worksheet
    for row in range(len(data)):
        for col in range(len(data[row])):
            worksheet.write(row, col, data[row][col])

    # Close the workbook
    workbook.close()

    # Capture data from memory file
    data_to_download = temp_file.getvalue()

    # Prepare response for download
    response = HttpResponse(content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename=reading_history.xlsx'
    response.write(data_to_download)

    return response