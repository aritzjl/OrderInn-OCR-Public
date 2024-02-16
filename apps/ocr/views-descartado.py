from django.shortcuts import render
from django.http import HttpResponse
import easyocr
from io import BytesIO
import base64
import requests
from PIL import Image
import csv
from openpyxl import Workbook
import openpyxl
from openpyxl.styles import Font
from openai import OpenAI


# Función para codificar la imagen en base64
def encode_image(image_bytes):
    return base64.b64encode(image_bytes).decode('utf-8')

# Función para procesar la imagen utilizando GPT Vision
def process_image_with_gpt_vision(image_bytes):
    # Codificar la imagen en base64
    base64_image = encode_image(image_bytes)

    api_key = "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"  # Reemplaza con tu API Key de OpenAI
    client=OpenAI(api_key="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")

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }

    messages = []
    mensaje = """
        Eres una herramienta para transformar textos en excel. Para ello, dado un texto, vas a devolver un texto en formato csv, es decir, cada columna separada por comas
        pudiendo dejar espacios en blanco es decir, si algún valor no encaja con la columna del excel, deja pon la coma peor no pongas ningún valor.
Los excel que debes crear, siempre van a tener estas columnas:
        Menu_RID    Rest_Name    Rest_City    Rest_State    Rest_Zip    Menu_ID    Item_ID    Category_ID    SubCategory_ID    Category_Sort    SubCategory_Sort    Item_Sort    Category_Name    SubCategory_Name    Item_Name    Item_Description    Item_IsFavorite    Item_IsAddExtras    Item_IsHeaderItemOnly    Item_IsOnPrintedMenu    Original_Price    Item_RestaurantPrice    Item_OIPrice    Item_WebPhoto

        Por ejemplo, si recibes este texto:

        Menu_RID    Rest_Name    Rest_City    Rest_State    Rest_Zip    Menu_ID    Item_ID    Category_ID    SubCategory_ID    Category_Sort    SubCategory_Sort    Item_Sort    Category_Name    SubCategory_Name    Item_Name    Item_Description    Item_IsFavorite    Item_IsAddExtras    Item_IsHeaderItemOnly    Item_IsOnPrintedMenu    Original_Price    Item_RestaurantPrice    Item_OIPrice    Item_WebPhoto
        12382    Ameci's    Camarillo    CA    93010    4132    1346762    10    35    9    133    5    Italian    Pasta    Spaghetti w/ Meat Sauce (Large)    Meat Sauce May Contain Ground Beef    0    0    0    1    13,99    11,19        
        155346    US Pizza    Surprise    AZ    85374    4647    1447108    13    33    13    289    7    Pizza    Pizza - Custom    14" Four Topping Pizza        0    0    0    1    18    14,4        
        154071    Rosati's Chicago Pizza    Ankeny    IA    50023    3369    1207260    16    38    2    41    5    Soups & Salads    Salads    Caesar Salad (Large)    Romaine Lettuce, Caesar Dressing & Croutons    0    0    0    1    6    4,8        

        Tu respuesta debería ser:

        12382,Ameci's,Camarillo,CA,93010,4132,1346762,10,35,9,133,5,Italian,Pasta,Spaghetti w/ Meat Sauce (Large),Meat Sauce May Contain Ground Beef,0,0,0,1,13.99,11.19,
        155346,US Pizza,Surprise,AZ,85374,4647,1447108,13,33,13,289,7,Pizza,Pizza - Custom,14" Four Topping Pizza,,,0,0,0,1,18,14.4,
        154071,Rosati's Chicago Pizza,Ankeny,IA,50023,3369,1207260,16,38,2,41,5,Soups & Salads,Salads,Caesar Salad (Large),Romaine Lettuce, Caesar Dressing & Croutons,0,0,0,1,6,4.8,
        


        COnvierte esto a csv:
        """

    message = {"role": "system", "content": mensaje}
    messages.append(message)


    message = {"role": "system", "content": mensaje}
    messages.append(message)


    message = {"role": "system", "content": mensaje}
    messages.append(message)

    response = client.chat.completions.create(
    model="gpt-4-vision-preview",
    messages=[
        {
        "role": "user",
        "content": [
            {"type": "text", "text": mensaje},
            {
            "type": "image_url",
            "image_url": {
                "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Gfp-wisconsin-madison-the-nature-boardwalk.jpg/2560px-Gfp-wisconsin-madison-the-nature-boardwalk.jpg",
            },
            },
        ],
        }
    ],
    max_tokens=300,
    )

    print(response.choices[0])
    print("---------------")
    return response.choices[0]



def process_image(image):
    # Procesar la imagen usando EasyOCR
    reader = easyocr.Reader(['en', 'es'])  # 'en' para inglés, puedes cambiarlo según el idioma
    result = reader.readtext(image)
    processed_text = '\n'.join([text[1] for text in result])
    return processed_text

def ocr(request):
    if request.method == 'POST' and request.FILES.get('image'):
        uploaded_image = request.FILES['image']
        img_byte_array = uploaded_image.read()
        # Procesar la imagen usando GPT Vision
        vision_result = process_image_with_gpt_vision(img_byte_array)
        
        # Convertir el texto en formato CSV a una lista de filas CSV
        csv_rows = vision_result.split('\n')
        csv_data = [row.split(',') for row in csv_rows]

        # Crear un archivo CSV temporal
        with open('temp.csv', 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerows(csv_data)

        # Crear un libro de trabajo de Excel
        wb = Workbook()
        ws = wb.active

        # Agregar títulos de columnas en negrita
        columnas = [
            "Menu_RID", "Rest_Name", "Rest_City", "Rest_State", "Rest_Zip", "Menu_ID", "Item_ID",
            "Category_ID", "SubCategory_ID", "Category_Sort", "SubCategory_Sort", "Item_Sort",
            "Category_Name", "SubCategory_Name", "Item_Name", "Item_Description", "Item_IsFavorite",
            "Item_IsAddExtras", "Item_IsHeaderItemOnly", "Item_IsOnPrintedMenu", "Original_Price",
            "Item_RestaurantPrice", "Item_OIPrice", "Item_WebPhoto"
        ]
        ws.append(columnas)
        for cell in ws[1]:
            cell.font = Font(bold=True)

        # Leer el archivo CSV temporal y escribir los datos en el libro de trabajo de Excel
        with open('temp.csv', 'r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            for row in reader:
                ws.append(row)

        # Guardar el libro de trabajo de Excel
        response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = 'attachment; filename="result.xlsx"'
        wb.save(response)

        return response
    else:
        return render(request, 'upload_image.html')