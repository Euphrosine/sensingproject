import json

from django.http import JsonResponse
from .models import SensorData
from django.utils import timezone
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse


def sensor_data_view(request):
    status = request.GET.get('status', None)

    activity = ""
    sensor = ""

    if status == "1":
        activity = "Unauthorized person trying to enter the car with fingerprint"
        sensor = "Fingerprint"
    elif status == "2":
        activity = "Unkown person is passing near your car"
        sensor = "Motion"
    elif status == "3":
        activity = "Unknown person touched your car"
        sensor = "Touch"

    data_to_save = {
        'datetime': timezone.now(),
        'sensor' : sensor,
        'activity': activity,
        'status': status
    }

    SensorData.objects.create(**data_to_save)

    sensor_data = SensorData.objects.all()

    # Filter out entries with status "4"
    response_data = [{'datetime': entry.datetime, 'sensor': entry.sensor,'activity': entry.activity, 'status': entry.status} for entry in sensor_data if entry.status != '4']

    return JsonResponse(response_data, safe=False)



@login_required
def display_chart_data(request):
    touch_count = SensorData.objects.filter(sensor='Touch').count()
    motion_count = SensorData.objects.filter(sensor='Motion').count()
    fingerprint_count = SensorData.objects.filter(sensor='Fingerprint').count()
    sensor_data = SensorData.objects.exclude(sensor='Aproximity')  # Exclude Aproximity

    context = {
        'sensor_data': sensor_data,
        'touch_count': touch_count,
        'motion_count': motion_count,
        'fingerprint_count': fingerprint_count,
    }

    return render(request, 'sensorapp/chart_data_view.html', context)



from .utils import generate_sensor_data_report


def generate_sensor_data_report_view(request):
    sensor_data = SensorData.objects.all()
    pdf_response = generate_sensor_data_report(sensor_data)
    return pdf_response
    
