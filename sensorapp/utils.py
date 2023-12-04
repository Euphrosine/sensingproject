from reportlab.pdfgen import canvas
from datetime import datetime
from django.http import HttpResponse

def generate_sensor_data_report(sensor_data):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename=sensor_data_report_{datetime.now().strftime("%Y-%m-%d_%H-%M")}.pdf'

    p = canvas.Canvas(response)

    # Set the font for the title
    p.setFont("Helvetica-Bold", 18)

    # Draw the title
    p.drawString(70, 1000, "Sensor Data Report")

    # Set the font back to regular
    p.setFont("Helvetica", 12)

    y_offset = 750  # Initial vertical position

    for i, data in enumerate(sensor_data):
        # Entry Label
        p.setFont("Helvetica-Bold", 12)
        p.drawString(90, y_offset, f"Entry {i + 1}:")
        p.setFont("Helvetica", 12)  # Set back to regular font

        # Data Fields
        p.drawString(90, y_offset - 20, f"DateTime: {data.datetime}")
        p.drawString(90, y_offset - 40, f"Sensor: {data.sensor}")
        p.drawString(90, y_offset - 60, f"Activity: {data.activity}")
        p.drawString(90, y_offset - 80, f"Status: {data.status}")

        # Calculate the height of the current entry based on its content
        entry_height = 100  # Adjust this value as needed
        y_offset -= entry_height

        # Check if a new page is needed
        if y_offset < 60:
            p.showPage()
            y_offset = 750  # Reset the vertical position for a new page

    p.save()

    return response
