import easyocr
from pylab import rcParams
import pytesseract
from PIL import Image, ImageEnhance, ImageFilter


def getLisencePlateText(img):
    rcParams['figure.figsize'] = 8, 16

    reader = easyocr.Reader(['vi'])

    listWord = reader.readtext(img)
    result = ""
    for i in listWord:
        result += i[-2]
    return result


