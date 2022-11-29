from pdf2image import convert_from_path
from datetime import datetime
from PIL import Image

from datetime import datetime
import base64
import unicodedata

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in {'pdf', 'png', 'jpg', 'jpeg', 'gif'}


def strip_accents(s):
    return ''.join(c for c in unicodedata.normalize('NFD', s) if unicodedata.category(c) != 'Mn')


def dpi_of_image(file):
    img = Image.open(file)
    file_destination = file.replace(".png", ".jpg")
    if img.mode in ("RGBA", "P"):
        img = img.convert('RGB')
    img.save(file_destination, dpi=(72.0, 72.0))
    return file_destination


def detect_mime_type(base64):
    signatures = {
        "JVBERi0": "application/pdf",
        "/9j/": "image/jpg",
        "iVBORw0KGgo": "image/png",
        "R0lGODdh": "image/gif",
        "R0lGODlh": "image/gif",
        "TU0AKgABR8L/": "image/tiff",
        "SUkqALxABgCAPh/": "image/tiff",
    }
    for s in signatures:
        if(base64.find(s) != -1):
            return signatures[s]
    return False


def pdf_from_base64_to_images_base64(base_64):
    paths_results = []
    seconds = datetime.today().timestamp()
    path = 'storage/tmp/' + str(seconds) + '.pdf'

    with open(path, "wb") as f:
        f.write(base64.b64decode(base_64))

    images_from_path = convert_from_path(pdf_path=path, dpi=72, poppler_path='/usr/bin')

    for i, image in enumerate(images_from_path):
        fname = 'storage/tmp/' + str(seconds) + "_page_" + str(i) + '.jpeg'
        new_width, new_height = 1125, 1500
        image.thumbnail((new_width, new_height))
        image.save(fname, "JPEG")
        with open(fname, "rb") as image_file:
            paths_results.append(base64.b64encode(
                image_file.read()).decode('utf-8'))

    return paths_results


def from_base64_to_base64_dpi(base_64):
    path = 'storage/tmp/' + str(datetime.today().timestamp()) + '.jpg'

    with open(path, "wb") as f:
        f.write(base64.b64decode(base_64))

    with open(dpi_of_image(path), "rb") as f:
        encoded_string = base64.b64encode(f.read()).decode('utf-8')

    return encoded_string

