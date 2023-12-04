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
        activity = "Unkown person is inside your car"
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

def display_sensor_charts(request):
    # Get data for Motion sensor
    motion_data = SensorData.objects.filter(sensor='Motion')
    motion_labels = [entry.datetime.strftime("%H:%M:%S") for entry in motion_data]
    motion_values = [entry.status for entry in motion_data]

    # Get data for Touch sensor
    touch_data = SensorData.objects.filter(sensor='Touch')
    touch_labels = [entry.datetime.strftime("%H:%M:%S") for entry in touch_data]
    touch_values = [entry.status for entry in touch_data]

    # Get data for Fingerprint sensor
    fingerprint_data = SensorData.objects.filter(sensor='Fingerprint')
    fingerprint_labels = [entry.datetime.strftime("%H:%M:%S") for entry in fingerprint_data]
    fingerprint_values = [entry.status for entry in fingerprint_data]

    context = {
        'motion_labels': motion_labels,
        'motion_values': motion_values,
        'touch_labels': touch_labels,
        'touch_values': touch_values,
        'fingerprint_labels': fingerprint_labels,
        'fingerprint_values': fingerprint_values,
    }

    return render(request, 'sensorapp/sensor_charts.html', context)

from .utils import generate_sensor_data_report


def generate_sensor_data_report_view(request):
    sensor_data = SensorData.objects.all()
    pdf_response = generate_sensor_data_report(sensor_data)
    return pdf_response
    
