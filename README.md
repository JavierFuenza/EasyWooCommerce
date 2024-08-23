# EasyWooCommerce
Una aplicación para conectar con WooCommerce y facilitar su manipulación.

## Cómo usar [Tailwind](https://tailwindcss.com/) en los templates de Django

Tailwind ya está instalado en el proyecto de Django. Para utilizarlo en tus páginas HTML, sigue estos pasos:

1. **Cargar las etiquetas de Tailwind en los templates:**

   - Antes de la declaración `<!DOCTYPE>`, añade la siguiente línea:
     ```django
     {% load static tailwind_tags %}
     ```

2. **Incluir el CSS de Tailwind en el `<head>`:**

   - Dentro de la sección `<head>` de tu HTML, añade:
     ```django
     {% tailwind_css %}
     ```

3. **Desarrollar con Tailwind:**

   - Para iniciar el proceso de desarrollo y compilación de Tailwind, ejecuta el siguiente comando en la consola:
     ```bash
     python manage.py tailwind start
     ```

   - Simultáneamente, puedes correr el servidor de Django con:
     ```bash
     python manage.py runserver
     ```

### Para más información

- [Video tutorial que seguí](https://www.youtube.com/watch?v=76n7sqZocSk)
- [Documentación de DJANGO-TAILWIND](https://django-tailwind.readthedocs.io/en/latest/installation.html)
