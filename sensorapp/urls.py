from django.urls import path
from .views import sensor_data_view,sensor_html_view,dashboard,table_view,line_chart_data,my_report_view,generate_sensor_data_report_view
from django.contrib.auth import views as auth_views


urlpatterns = [
    # ... your other URL patterns ...
    path('', sensor_html_view, name='sensor_view'),
    path('sensor_data/', sensor_data_view, name='sensor_data_view'),
    path('dashboard/', dashboard, name='dashboard'),
    path('table_view/', table_view, name='table_view'),
    path('line_chart_json/', line_chart_data, name='line_chart_data'),
    path('generate_report/', my_report_view, name='generate_report'), 
    path('generate_sensor_data_report/', generate_sensor_data_report_view, name='generate_sensor_data_report'),
    path('accounts/login/',auth_views.LoginView.as_view(template_name='sensorapp/login.html'),name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='sensorapp/logout.html'),name='logout'),
]
