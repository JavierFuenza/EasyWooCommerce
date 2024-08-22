import os
from dotenv import load_dotenv
from django.shortcuts import render
from woocommerce import API
load_dotenv()
#DATOS API
wcapi = API(
    url='https://pruebawoo.javierfuenzam.com/',
    consumer_key= os.getenv('CONSUMER_KEY'),
    consumer_secret= os.getenv('CONSUMER_SECRET'),
    wp_api = True,
    version="wc/v3"
)
#Listar productos
def getProd (id='0'):
    """
    Funcion para obtener productos utilizando la api, 
    se puede ingresar un id de producto en especifico, 
    o dejar vacio para listar todos los productos 
    """
    if id == '0':
        productos:str = wcapi.get("products/").json()
    else:
        productos:str = wcapi.get(f"products/{id}").json()
    return str(productos)

