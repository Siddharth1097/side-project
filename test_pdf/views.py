from django.shortcuts import render
from io import BytesIO
from django.http import HttpResponse
from django.views import View
from django.template.loader import get_template

from xhtml2pdf import pisa

def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html  = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None

# class ViewPDF(View):
#     def get(self, request, *args, **kwargs):
#         context = {
#             "company": "Dennnis Ivanov Company",
#             "address": "123 Street name",
#             "city": "Vancouver",
#             "state": "WA",
#             "zipcode": "98663",
#
#             "phone": "555-555-2345",
#             "email": "youremail@dennisivy.com",
#             "website": "dennisivy.com",
#         }
#
#         pdf = render_to_pdf('pdf_template.html', context)
#         return HttpResponse(pdf, content_type='application/pdf')

class ViewPDF(View):
    def get(self, request, *args, **kwargs):
        context = {
            "first_name": "Siddharth",
            "last_name": "Menon",
            "city": "Bangalore",
            "phone": "1234567890",
            "email": "sidd@mail.com",
        }
        pdf = render_to_pdf('pdf_template.html', context)
        return HttpResponse(pdf, content_type='application/pdf')


def home_page(request):
    return render(request, 'index.html', {})
