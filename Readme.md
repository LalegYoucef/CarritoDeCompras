# **Carrito De Compra**

¡Bienvenido a la prueba técnica de backend Carrito De compras! 
Esta aplicación simple permitiá a un frontend de realizar operaciones relacionadas con la gestión de productos, carrito de compras y procesos de compra de una tienda de ropa online, a traves de API's creada a usando DjangoRestFramework.
A continuación, se detallan las características y funcionalidades de la aplicación.

## **Características de la Aplicación**
Este endpoint devuelve un listado de productos ordenados por tipo (gorras primero, luego camisetas) y por fecha de inclusión en el catálogo (más recientes primero). La información incluye detalles como color, marca, tipo de tejido, tallaje, etc.

Endpoint: /productos

### **1-Listado de Productos**


### **2-CRUD del producto**


### **3-Añadir Producto al Carrito**

Permite agregar productos al carrito junto con la cantidad deseada. Se crea un carrito si no existe uno para el día actual.

Endpoint: POST /carrito
### **4-Ver el Carrito**

Muestra el contenido actual del carrito, incluyendo productos añadidos, cantidad y el total del carrito.

Endpoint: GET /carrito


### **5-Comprar el producto**
Finaliza la compra, recibiendo un formulario con los datos personales del cliente. Simula el envío de un email de confirmación.

Endpoint: POST /comprar

### **6-Actualización de Stock**
Un proceso automático actualiza el stock de los productos cada hora para evitar desajustes.
## **Instalación de la Aplicación**
### **1-**
