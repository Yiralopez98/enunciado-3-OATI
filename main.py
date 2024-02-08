from sistema import Sistema
from producto import Producto
from consumidor import Consumidor
from orden import Orden

def main():
    sistema = Sistema()

    while True:
        print("\nSistema de Gestión de Pedidos")
        print("1. Agregar consumidor")
        print("2. Agregar producto")
        print("3. Realizar pedido")
        print("4. Consultar consumidores")
        print("5. Consultar productos")
        print("6. Consultar ordenes")
        print("7. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Ingrese el nombre del consumidor: ")
            apellido = input("Ingrese el apellido del consumidor: ")
            telefono = input("Ingrese el teléfono del consumidor: ")
            consumidor = Consumidor(len(sistema.consumidores) + 1, nombre, apellido, telefono)
            sistema.agregar_consumidor(consumidor)
            print("Consumidor agregado con éxito.")

        elif opcion == "2":
            descripcion = input("Ingrese la descripción del producto: ")
            precio = float(input("Ingrese el precio del producto: "))
            cantidad_en_stock = int(input("Ingrese la cantidad en stock del producto: "))
            producto = Producto(len(sistema.productos) + 1, descripcion, precio, cantidad_en_stock)
            sistema.agregar_producto(producto)
            print("Producto agregado con éxito.")
        
        elif opcion == "3":
            if not sistema.consumidores or not sistema.productos:
                print("No hay consumidores o productos disponibles para realizar un pedido.")
            else:
                print("\nListado de consumidores:")
                sistema.consultar_consumidores()
                consumidor_id = int(input("Seleccione el ID del consumidor para realizar el pedido: "))
                consumidor_seleccionado = None
                for consumidor in sistema.consumidores:
                    if consumidor.id == consumidor_id:
                        consumidor_seleccionado = consumidor
                        break
                if consumidor_seleccionado:
                    print("\nListado de productos:")
                    sistema.consultar_productos()
                    producto_ids = input("Ingrese los ID de los productos separados por comas: ").split(",")
                    productos_seleccionados = []
                    for producto_id in producto_ids:
                        producto_id = int(producto_id.strip())
                        for producto in sistema.productos:
                            if producto.id == producto_id:
                                productos_seleccionados.append(producto)
                                break
                    orden = Orden(len(sistema.ordenes) + 1, consumidor_seleccionado, productos_seleccionados)
                    sistema.agregar_orden(consumidor_seleccionado, productos_seleccionados)
                    print("Pedido realizado con éxito.")
                else:
                    print("El ID del consumidor seleccionado no es válido.")

        elif opcion == "4":
            print("\nListado de consumidores:")
            sistema.consultar_consumidores()

        elif opcion == "5":
            print("\nListado de productos:")
            sistema.consultar_productos()

        elif opcion == "6":
            print("\nListado de ordenes:")
            sistema.consultar_ordenes()

        elif opcion == "7":
            print("Gracias por usar la aplicación. ¡Hasta luego!")
            break

        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    main()
