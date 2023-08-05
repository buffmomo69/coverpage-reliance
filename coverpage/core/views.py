
from django.http import HttpResponse, FileResponse
from django.shortcuts import render
import subprocess
from django.template.loader import get_template
from weasyprint import HTML

def index(request):
    return render(request,"forms.html")




from django.http import HttpResponse, FileResponse
from django.shortcuts import render
import subprocess

def submit_lab_report(request):
    if request.method == "POST":
        name = request.POST.get("name")
        semester = request.POST.get("semester")
        program = request.POST.get("program")
        registration_no = request.POST.get("registernumber")
        teachers_name = request.POST.get("teachersname")
        department = request.POST.get("department")
        subject = request.POST.get('subject')
        
        context = {
            "name": name, "semester": semester,
            "program": program,
            "registernumber": registration_no,
            "teachersname": teachers_name,
            "department": department,
            "subject": subject,
        }
        
        return render(request,"coverpage.html",context)
        # template = get_template('coverpage.html')
        # rendered_html = template.render(context)
        # pdf_file = HTML(string=rendered_html).write_pdf()
        # response = HttpResponse(pdf_file,content_type = "application/pdf")
        # response['Content-Disposition'] = f'filename="coverpage-{subject}.pdf"'
        # return response

        
#         from django.template.loader import get_template
# from django.http import HttpResponse
# from weasyprint import HTML

# def generate_pdf(request):
#     # Get your HTML template
#     template = get_template('your_template.html')
#     context = {'your_context_variable': 'some_value'}

#     # Render the template with context
#     rendered_html = template.render(context)

#     # Generate PDF
#     pdf_file = HTML(string=rendered_html).write_pdf()

#     # Create HTTP response with PDF content
#     response = HttpResponse(pdf_file, content_type='application/pdf')
    # response['Content-Disposition'] = 'filename="your_generated_file.pdf"'
    # return response
