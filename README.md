# wherexShop
Página de evaluación para empresa Wherex.

https://wherexshop.herokuapp.com/

## Requerimientos

Crear una aplicación que permita almacenar clientes, productos y ventas. El sistema debe registrar las ventas con su detalle y guardar los totales incluyendo el iva, descuento general y el total

  ● Se requiere implementar al menos 4 entidades (Cliente, Producto, Venta y Detalle).

  ● Crear un listado de las ventas y un enlace a la información de venta.

  ● Crear, modificar y eliminar venta
  
  
## Stack

Para esta plataforma utilice en el backend Python y Django ya que se requería trabajar bajo el patrón MVC, en el Front me apoye en la librería de Bootstrap 5 para realizar la página lo más rápido posible, apoyándome de CSS y JS para realizar pequeñas personalizaciones y funciones dentro de la página.

Utilice ademas librerías como FontAwesomeIcon e highlight.js para poder destacar sintaxis SQL utilizado en la página y facilitar su lectura.


## Vistas

### HomePage

En esta vista se pueden agregar productos al carrito de compras, en donde se mostrara el precio total, junto con los descuentos e iva de cada uno de los productos que se vayan agregando. Se selecciona el cliente al cual generar la venta y se almacena la venta en el sistema junto con el detalle de cada uno de los productos.

![Home Page](https://user-images.githubusercontent.com/43582318/118384147-d027e580-b5d1-11eb-88e6-f1827189201e.png)


### Listado clientes

En la vista de listado de clientes se listan a todos los clientes que están almacenados, ademas se puede acceder al historial de ventas específicos de cada cliente y actualizar sus datos. Ademas en esta misma vista se puede ingresar un nuevo cliente y eliminar un cliente ya ingresado.

![New Mockup 2](https://user-images.githubusercontent.com/43582318/118384149-d0c07c00-b5d1-11eb-8e63-6c00925669a5.png)


### Listado productos

La vista de listado de productos muestra el listado de todos los productos que están almacenados y da acceso a poder modificar sus datos, tales como el stock o el valor. En esta vista también se pueden ingresar nuevos productos como eliminar los ya existentes

![New Mockup 3](https://user-images.githubusercontent.com/43582318/118384150-d1591280-b5d1-11eb-9a0f-a83a90568b2c.png)


### Historial ventas

En esta vista se listan todas las ventas que están almacenadas en la base de datos, listando las por fecha de ingreso y permitiendo acceder al detalle completo de cada una de ellas

![New Mockup 4](https://user-images.githubusercontent.com/43582318/118384151-d1591280-b5d1-11eb-9a15-771d7447a937.png)


### Diagrama de Entidad-Relación

Para esta aplicación se utilizo una base de datos SQLite que cuenta con 4 entidades, Cliente, Producto, Venta, y Detalle Venta.

![Diagrama ER de DBMS (notación UML)](https://user-images.githubusercontent.com/43582318/118384597-3d894580-b5d5-11eb-85aa-9b38b20e7819.jpeg)

