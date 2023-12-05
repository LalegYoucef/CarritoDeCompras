# Carrito de Compras

¡Bienvenido a la prueba técnica del backend Carrito de Compras! Esta aplicación simple permite a un frontend realizar operaciones relacionadas con la gestión de productos, carrito de compras y procesos de compra de una tienda de ropa en línea, a través de APIs creadas con Django Rest Framework. A continuación, se detallan las características y funcionalidades de la aplicación.

## Características de la Aplicación

**1. Listado de Productos:**
Devuelve un listado de productos ordenados por tipo y por fecha de inclusión en el catálogo, incluyendo detalles como color, marca, tipo de tejido, tallaje, etc.

**2. CRUD del Producto:**
Permite realizar operaciones básicas de Crear, Leer, Actualizar y Eliminar (CRUD) sobre los productos.

**3. Añadir Producto al Carrito:**
Permite agregar productos al carrito junto con la cantidad deseada. Se crea un carrito si no existe uno para el día actual.

**4. Ver el Carrito:**
Muestra el contenido actual del carrito, incluyendo productos añadidos, cantidad y el total del carrito.

**5. Comprar el Producto:**
Finaliza la compra, recibiendo un formulario con los datos personales del cliente. Simula el envío de un correo electrónico de confirmación.

**6. Actualización de Stock:**
Un proceso automático actualiza el stock de los productos cada hora para evitar desajustes.

## Instalación de la Aplicación

Hay dos opciones válidas para instalar el Carrito de Compras:

1. **Via Docker:**
 - Clone el proyecto en su máquina local utilizando el comando:
     ```bash
     git clone https://github.com/LalegYoucef/CarritoDeCompras.git
     ``` 
     En la carpeta de su elección
 - `cd tuCarpeta` y activa el venv `source myvenv/bin/activate`
   - Ejecute `docker build -t carritodecompra` para crear la imagen y `docker run -p Port:Port carritodecompra` para ejecutar .

2. **Clonando el Proyecto:**
   - Clone el proyecto en su máquina local utilizando el comando:
     ```bash
     git clone https://github.com/LalegYoucef/CarritoDeCompras.git
     ```
   - `cd tuCarpeta/CarritoDeCompra` activa el venv `source ../myvenv/bin/activate`
   - `pip install -r requirements.txt `
   -`python manage.py runserver `


¡Disfrute explorando y utilizando el Carrito de Compras!

# Importante 

El fichero **PostmanCollection.json** contiene todas las endpoints disponibles de la app
