from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from .models import Bus_schedule,ScheduleCode
from .models import Bus_Stats
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib import colors

# Create your views here.s
def home(request):
    list = ScheduleCode.objects.all()
    return render(request,"buses/home.html",{
        "list": list
    })

def view_schedule(request, schedule_code):
    if request.method == 'POST':
        code = request.POST['code']
        schedule_list = Bus_schedule.objects.filter(schedule_code=code)

        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="bus_schedule.pdf"'

        p = canvas.Canvas(response, pagesize=letter)
        width, height = letter

        # Title
        p.setFont("Helvetica-Bold", 16)
        p.drawString(200, height - 40, "Bus Schedule")

        # Define column x-positions with more spacing
        col_x = {
            'code': 30,
            'departure': 130,
            'destination': 250,
            'departure_time': 390,
            'arrival_time': 510,
            'duration': 630
        }

        # Header drawing function
        def draw_headers(y):
            p.setFont("Helvetica-Bold", 12)
            p.drawString(col_x['code'], y, "Code")
            p.drawString(col_x['departure'], y, "Departure")
            p.drawString(col_x['destination'], y, "Destination")
            p.drawString(col_x['departure_time'], y, "Departure Time")
            p.drawString(col_x['arrival_time'], y, "Arrival Time")
            p.drawString(col_x['duration'], y, "Duration")
            p.setFont("Helvetica", 10)

        y_position = height - 80
        draw_headers(y_position)
        y_position -= 20

        for schedule in schedule_list:
            p.drawString(col_x['code'], y_position, code)
            p.drawString(col_x['departure'], y_position, schedule.departure)
            p.drawString(col_x['destination'], y_position, schedule.destination)
            p.drawString(col_x['departure_time'], y_position, schedule.departure_time.strftime('%H:%M'))
            p.drawString(col_x['arrival_time'], y_position, schedule.arrival_time.strftime('%H:%M'))
            p.drawString(col_x['duration'], y_position, str(schedule.duration))
            y_position -= 20

            if y_position < 40:
                p.showPage()
                y_position = height - 60
                draw_headers(y_position)
                y_position -= 20

        p.save()
        return response

    # GET request logic
    schedule_list = Bus_schedule.objects.filter(schedule_code=schedule_code)
    schedule = ScheduleCode(schedule_code=schedule_code)
    stats = Bus_Stats(schedule_code=schedule)
    stats.save()

    return render(request, "buses/view_schedule.html", {
        "list": schedule_list,
        "schedule_code": schedule_code
    })

