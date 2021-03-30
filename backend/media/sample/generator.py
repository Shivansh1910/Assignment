import cv2 as cv
import openpyxl
from PIL import Image, ImageFont, ImageDraw


def generatorname(name, x, y):
    template_path = 'certificate.jpg'
    output_path = 'new'
    size = 3

    font_size = int(size)
    font_color = (0, 0, 0)

    coordinate_y_adjustment = float(y)
    coordinate_x_adjustment = float(x)

    certi_name = str(name)

    img = cv.imread(template_path)

    font = cv.FONT_HERSHEY_PLAIN

    text_size = cv.getTextSize(certi_name, font, font_size, 10)[0]

    text_x = (img.shape[1] - text_size[0]) / 2 + coordinate_x_adjustment
    text_y = (img.shape[0] + text_size[1]) / 2 - coordinate_y_adjustment
    text_x = int(text_x)
    text_y = int(text_y)
    cv.putText(img, certi_name,
               (text_x, text_y),
               font,
               font_size,
               font_color, 3)

    certi_path = output_path + '/Certificate of ' + certi_name + '.jpg'

    cv.imwrite(certi_path, img)
    img = Image.fromarray(img)
    # img.show()
    img = img.convert('RGB')
    certi_path = output_path + '/Certificate of ' + name + '.pdf'
    img.save(certi_path)

    return


def generatordis(name, x, y, text):
    template_path = 'certificate3.jpg'
    image = Image.open(template_path)
    draw = ImageDraw.Draw(image)

    font = ImageFont.truetype(r'OpenSans-Bold.ttf', 50)
    spacing = 5
    # text = "This is to certify that\n " + name + \
    #     " \n had participated in the \n Annual Business Model Competition Eureka! 2019 \n conducted by E-Cell IIT Bombay \n and had been selected as Semi-Finalists in the same."
    x = int(x)
    y = int(y)
    text = str(text)

    draw.text((x, y), text, fill="black",
              font=font, spacing=spacing, align="center")
    img = image.convert('RGB')
    output_path = 'new'
    certi_path = output_path + '/Certificate of ' + name + '.pdf'
    img.save(certi_path)
    return


name = "Shrianshi"
x = 7
y = 15

x1 = 350
y1 = 600
text = "This is to certify that\n " + name + \
    "\n had participated in the \n Annual Business Model Competition Eureka! 2019 \n conducted by E-Cell IIT Bombay \n and had been selected as Semi-Finalists in the same."

generatorname(name, x, y)

# generatordis(name, x1, y1, text)
