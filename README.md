# EasyWooCommerce
App para conectar con WooCommerce y hacer mas fácil la manipulación de este





## Como usar [Tailwind](https://tailwindcss.com/) en los templates de Django


Ya esta instalado Tailwind en el proyecto de django, y para usarlos en las paginas html hay que usar:

* Antes del !DOCTYPE
´´´
{% load static tailwind_tags %}
´´´

* En el head

´´´
{% tailwind_css %}
´´´

Luego para desarrollar hay que dejar corriendo en la consola

* Comando
´´´
python manage.py tailwind start
´´´

* Comando

´´´
python manage.py runserver
´´´

### Para más información del tutorial que segui

* [Enlace del video tutorial](https://www.youtube.com/watch?v=76n7sqZocSk)
* [Documentacion de DJANGO-TAILWIND](https://django-tailwind.readthedocs.io/en/latest/installation.html)
