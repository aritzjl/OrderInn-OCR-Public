# **[OrderInn](https://home.orderinn.com/) Menu OCR to Excel Converter**
![image](https://github.com/aritzjl/OrderInn-OCR-Public/assets/129123101/1d12eebb-f3f9-43d5-ba6c-20cefa97ce65)


Este proyecto Django permite a los usuarios de [OrderInn](https://home.orderinn.com/) subir fotos/pdfs de menús de restaurantes, extrae el texto utilizando la API de Google Vision y, luego, procesa este texto con la API de ChatGPT y un algoritmo específico para convertirlo en un archivo Excel con un formato específico.

## **Características**

- **Extracción de Texto:** Utiliza PyMuPDF y la API de Google Vision para extraer texto de imágenes y pdfs.
- **Procesamiento de Texto:** Implementa un algoritmo personalizado para procesar el texto extraído y convertirlo en formato estructurado.
- **Generación de PDF:** Convierte el texto estructurado en un PDF formateado específicamente para OrderInn.
- **Interfaz de Usuario Segura:** Requiere autenticación de usuario para subir y procesar imágenes.

## **Requisitos Previos**

Antes de comenzar, asegúrate de tener instalado Python y Django en tu sistema. Además, necesitarás credenciales de API válidas para Google Cloud Vision y OpenAI.

## **Configuración**

1. **Clonar el Repositorio:**
2. **Crear y activar un entorno virtual de python:**
    ```bash
    python3 -m venv venv #en linux
    source venv/bin/activate #en linux
    ```

3. **Instalar Dependencias:**
    
    ```bash
    pip install -r requirements.txt
    ```
    
4. **Configura tus apis de google y openai:**
5. **Ejecutar Migraciones:**
    
    ```bash
    python manage.py migrate
    ```
    
6. **Iniciar el Servidor de Desarrollo:**
    
    ```bash
    python manage.py runserver
    ```
    

## **Uso**

Para utilizar la aplicación:

1. Navega a **`http://localhost:8000`** en tu navegador.
2. Inicia sesión o regístrate para crear una cuenta de usuario.
![image](https://github.com/aritzjl/OrderInn-OCR-Public/assets/129123101/55ef46be-b66e-4de1-a2ec-04baff2772eb)


3. Sigue las instrucciones en pantalla para subir una foto de un menú.
![image](https://github.com/aritzjl/OrderInn-OCR-Public/assets/129123101/1cc4e19c-669b-448a-b26b-5b9c872e32d7)



4. Descarga el archivo Excel generado una vez que el proceso haya finalizado.
