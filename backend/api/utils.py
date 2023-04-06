import os

from django.conf import settings
from django.http import HttpResponse
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas

DATA_ROOT = os.path.join(settings.BASE_DIR, 'data')


def pdf_shopping_cart(final_list):
    font_path = os.path.join(DATA_ROOT, 'custom_font.ttf')
    pdfmetrics.registerFont(
        TTFont('custom_font', font_path, 'UTF-8'))
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = ('attachment; '
                                       'filename="shopping_list.pdf"')
    page = canvas.Canvas(response)
    page.setFont('custom_font', size=24)
    page.drawString(200, 800, 'Список ингредиентов')
    page.setFont('custom_font', size=16)
    height = 750
    for i, (name, data) in enumerate(final_list.items(), 1):
        page.drawString(75, height, (f'{i}. {name} - {data["amount"]}, '
                                     f'{data["measurement_unit"]}'))
        height -= 25
    page.showPage()
    page.save()
    return response
