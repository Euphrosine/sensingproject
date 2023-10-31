from django.urls import path
from .views import sensor_data_view,display_chart_data,generate_sensor_data_report_view
from django.contrib.auth import views as auth_views


urlpatterns = [
    # ... your other URL patterns ...
    path('', display_chart_data, name='display_chart_data'),
    path('sensor_data/', sensor_data_view, name='sensor_data_view'), 
    path('generate_sensor_data_report/', generate_sensor_data_report_view, name='generate_sensor_data_report'),
    path('accounts/login/',auth_views.LoginView.as_view(template_name='sensorapp/login.html'),name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='sensorapp/logout.html'),name='logout'),
]
