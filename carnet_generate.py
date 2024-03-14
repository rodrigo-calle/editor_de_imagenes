from PIL import Image, ImageDraw, ImageFont
import csv

# Asegúrate de tener una fuente adecuada para el texto
font_path = "font/Arial.ttf"
font_size = 32
font = ImageFont.truetype(font_path, font_size)

# Carga la plantilla del carnet (asegúrate de tener el diseño base como una imagen)
template_image_path = "template/id_ridu.png"
output_folder = "./ridu_ids/"

def create_card(data):
    image = Image.open(template_image_path).convert("RGBA")  # Convertir a modo RGB
    draw = ImageDraw.Draw(image)
    # Ajusta estas coordenadas según tu diseño
    text_color = (0, 76, 153)  # Cambiar a un color visible

    draw.text((100, 225), data["nombres_apellidos"], fill=text_color, font=font)
    draw.text((100, 360), data["celular"], fill=text_color, font=font)
    draw.text((100, 490), data["sede"], fill=text_color, font=font)
    
    # Guarda la imagen en el directorio deseado
    output_path = f'{output_folder}{data["nombres_apellidos"].replace(" ", "_")}.png'
    image.save(output_path)
    print(f'Carnet creado: {output_path}')

# Lee los datos desde un archivo CSV
with open('data/data.csv', mode='r', encoding='utf-8') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        print(row)
        create_card(row)

