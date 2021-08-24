import locale
from datetime import date
from PIL import Image, ImageDraw, ImageFont


def centered_position(draw, text, font, color, strip_width, strip_height):
    txt_width, txt_height = draw.textsize(text, font)
    position = ((strip_width - txt_width) / 2, (strip_height - txt_height) / 2)

    draw.text(position, text, fill=color, font=font)


def cert_generator(id, course, participant):
    locale.setlocale(locale.LC_ALL, 'pt_BR')

    image = Image.open('certificate-model.png')
    draw = ImageDraw.Draw(image)

    font = ImageFont.truetype('fonts/LibreBasker/LibreBaskerville-Regular.ttf', size=22)
    body_font = ImageFont.truetype('fonts/LibreBasker/LibreBaskerville-Bold.ttf', size=50)
    small_bold = ImageFont.truetype('fonts/LibreBasker/LibreBaskerville-Bold.ttf', size=12)
    signature_font = ImageFont.truetype('fonts/Chopin/ChopinScript.ttf', size=70)

    blue = 'rgb(62, 73, 129)'
    black = 'rgb(0, 0, 0)'

    today = date.today().strftime("%d de %B de %Y")

    # Certificate body
    text = 'Certificamos que no dia %s,' % (today)
    centered_position(draw, text, body_font, blue, 1900, 950)

    text = '%s %s completou o curso presencial:' % (participant['first_name'], participant['last_name'])
    centered_position(draw, text, body_font, blue, 1900, 1080)

    text = '\"%s\"' % course.title()
    centered_position(draw, text, body_font, blue, 1900, 1343)

    # Instructor's signature
    text = '%s %s' % ('Rick', 'Sanchez')
    centered_position(draw, text, signature_font, black, 1212, 1780)

    text = '%s %s, Instrutor' % ('Rick', 'Sanchez')
    centered_position(draw, text, font, blue, 1212, 1930)

    # Student's signature
    text = '%s %s' % (participant['first_name'], participant['last_name'])
    centered_position(draw, text, signature_font, black, 2580, 1780)

    text = '%s %s, Aluno' % (participant['first_name'], participant['last_name'])
    centered_position(draw, text, font, blue, 2580, 1930)

    # Certificate Number and URL
    (x, y) = (536, 1184)
    text = 'LC-%s' % id
    draw.text((x, y), text, fill=black, font=small_bold)

    (x, y) = (1180, 1183)
    text = 'lampp.com/certificado/LC-%s' % id
    draw.text((x, y), text, fill=black, font=small_bold)

    image.save('certificates/LC-%s.png' % id)


p = {
    'first_name': 'Michell',
    'last_name': 'Lucino'
}
cert_generator(1, "Teste Curso de Exemplo", p)
