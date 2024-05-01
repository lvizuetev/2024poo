from components import Menu,Valida
from utilities import borrarPantalla,gotoxy,gotxy_frame
from utilities import reset_color,red_color,green_color,bright_pink_color,purple_color,pink_color,bright_pink_color
from clsJson import JsonFile
from company  import Company
from customer import RegularClient,VipClient
from sales import Sale
from product  import Product
from iCrud import ICrud
import datetime
import time,os
from functools import reduce

path, _ = os.path.split(os.path.abspath(__file__))


class CrudClients(ICrud):
    def create(self):
        validar = Valida()
        borrarPantalla()
        gotxy_frame(0,0,167,100)
        gotoxy(65,2);print(bright_pink_color+"Registro de clientes")
        gotoxy(52,3);print(bright_pink_color+Company.get_business_name())
        gotoxy(1,4);print(bright_pink_color+"*"*167)
        gotoxy(7,6);print("Ingresa tu DNI:")
        gotoxy(7,7);print("Ingresa tu nombre:")
        gotoxy(7,8);print("Ingresa tu apellido:")
        gotoxy(7,9);print("Tipo de cliente (R/V):")
        gotoxy(23,6);dni = validar.validar_numero_dni("Error: No tiene formato DNI", 23, 6)
        gotoxy(26,7);nombre = validar.validar_nombre_cliente(col=26, fil=7)
        gotoxy(28,8);apellido = validar.validar_nombre_cliente(col=28, fil=8)
        gotoxy(30,9);tipo_cliente = input().lower()
        gotoxy(7,10);print(red_color+"Esta seguro de registrar el cliente?🤔 (y/n):")
        gotoxy(53,10);procesar = input().lower()

        if procesar.lower() == "y":
            cliente = RegularClient(dni=dni, first_name=nombre.upper(), last_name=apellido.upper(), card=True) if tipo_cliente.lower() == 'r' else VipClient(dni=dni, first_name=nombre.upper(), last_name=apellido.upper())
            json_file = JsonFile(path+'/archivos/clients.json')
            clientesArchivo = json_file.read()
            data = cliente.getJson()

            if validar.validar_registro(clientesArchivo, data):
                gotoxy(15, 12); print(bright_pink_color+"El cliente ya se encuentra registrado🥲")
                time.sleep(2)
            else:
                clientesArchivo.append(data)
                json_file = JsonFile(path+'/archivos/clients.json')
                json_file.save(clientesArchivo)
                gotoxy(7, 12); print(bright_pink_color+"Registro exitoso! ✅")
                time.sleep(2)
        else:
            gotoxy(7, 11); print(red_color+"Registro cancelado ❌...")
            gotoxy(7, 12); print(bright_pink_color+"¿Quieres intentarlo de nuevo? (y/n):")
            gotoxy(45, 12);retry = input().lower()
            if retry == 'y':
                self.create()
            else:
                time.sleep(2)

    def update(self):
        validar = Valida()
        borrarPantalla()
        gotxy_frame(0,0,167,100)
        gotoxy(65,1);print( "Actualizar Cliente")
        gotoxy(1,2);print(bright_pink_color+"*"*167)
        json_file = JsonFile(path+'/archivos/clients.json')
        lista_clientes=json_file.read()
        gotxy_frame(25,4,100,len(lista_clientes)+5)
        gotoxy(65,5);print(f"Lista de clientes")
        gotoxy(34,6);print(f"DNI")
        gotoxy(64,6);print(f"NOMBRE")
        gotoxy(94,6);print(f"APELLIDO")
        if lista_clientes:
            for i in range(len(lista_clientes)):
                gotoxy(34,7+i);print(f"{ lista_clientes[i]['dni']}")
                gotoxy(64,7+i);print(f"{ lista_clientes[i]['nombre']}")
                gotoxy(94,7+i);print(f"{ lista_clientes[i]['apellido']}")
            gotoxy(6,len(lista_clientes)+10);print("Ingresa el DNI:")
            gotoxy(22,len(lista_clientes)+10);dni = validar.validar_numero_dni("Error: DNI no valido", 22, len(lista_clientes)+10)
            cliente_dni = json_file.find("dni",dni)
            if cliente_dni:
                gotoxy(6,len(lista_clientes)+12);print(f"Hola, {cliente_dni[0]['nombre']} aqui puedes actualizar")
                gotoxy(6,len(lista_clientes)+14);print(f"Ingresa el nombre: {cliente_dni[0]['nombre']}")
                gotoxy(25,len(lista_clientes)+14);nombre = validar.validar_nombre_cliente(25,len(lista_clientes)+14)
                gotoxy(6,len(lista_clientes)+15);print(f"Ingresa el apellido: {cliente_dni[0]['apellido']}")
                gotoxy(27,len(lista_clientes)+15);apellido = validar.validar_nombre_cliente(27,len(lista_clientes)+15)
                data=json_file.read()
                cliente=cliente_dni[0]
                gotoxy(6,len(lista_clientes)+16);print(red_color+"Estas seguro de actualizar tus datos?🤔(y/n):")
                gotoxy(52,len(lista_clientes)+16);procesar = input().lower()
                if procesar.lower() == "y":
                    for i in data:
                        if i['dni'] == cliente['dni']:
                            i['nombre']=nombre.upper() if nombre else i['nombre']
                            i['apellido']=apellido.upper()  if apellido else i['apellido']
                            gotoxy(6,len(lista_clientes)+17);print(bright_pink_color+"Actualizacion exitosa!🌞")  
                            time.sleep(2)               
                else:
                    gotoxy(6,len(lista_clientes)+17);print(bright_pink_color+"Se cancelo la actualizacion ❌...")
                    time.sleep(2)
                json_file.save(data=data)    
                time.sleep(1)
            else:
                gotoxy(26,len(lista_clientes)+12);print("Cliente no existe")
                time.sleep(2)
        else:    
            gotoxy(60,7);print("No se han registrado clientes ")
            time.sleep(2)
    
    def delete(self):
        validar = Valida()
        borrarPantalla()
        gotxy_frame(0,0,167,100)
        gotoxy(65,1);print("Clientes Registrados")
        gotoxy(2,2);print(bright_pink_color+"*"*167)
        json_file = JsonFile(path+'/archivos/clients.json')
        lista_clientes=json_file.read()
        gotxy_frame(25,4,100,len(lista_clientes)+3)
        if lista_clientes:
            gotoxy(65,5);print(f"Lista de clientes")
            gotoxy(40,5);print(f"DNI")
            gotoxy(70,5);print(f"Nombre")
            gotoxy(100,5);print(f"Apellido")
            for i in range(len(lista_clientes)):
                gotoxy(40,6+i);print(f"{lista_clientes[i]['dni']}")
                gotoxy(70,6+i);print(f"{lista_clientes[i]['nombre']}")
                gotoxy(100,6+i);print(f"{lista_clientes[i]['apellido']}")
            gotoxy(7,len(lista_clientes)+10);print(bright_pink_color+"Elige como deseas eliminar (T/DNI):")
            gotoxy(43,len(lista_clientes)+10);procesar = input().lower()
            if procesar.lower() == "dni":
                gotoxy(7,len(lista_clientes)+11);print("Ingresa el DNI:")
                gotoxy(24,len(lista_clientes)+11);dni = validar.validar_numero_dni("Error: DNI no valido", 24, len(lista_clientes)+11)
                cliente_dni = json_file.find("dni",dni)
                if cliente_dni:
                    gotoxy(7,len(lista_clientes)+12);print(bright_pink_color+"Estas seguro de realizar la eliminacion🤔?(y/n):")
                    gotoxy(57,len(lista_clientes)+12);procesar = input().lower()
                    if procesar.lower()=='y':
                        lista_clientes.remove(cliente_dni[0])
                        json_file.save(lista_clientes)
                        gotoxy(7,len(lista_clientes)+14);print(bright_pink_color+"Eliminado con exito! ✅")
                        time.sleep(3)  
                    else:
                        gotoxy(7,len(lista_clientes)+14);print(red_color+"Eliminacion cancelada ❌")
                        time.sleep(2) 
                else:
                    gotoxy(7,len(lista_clientes)+12);print("DNI no encontrado")
                    time.sleep(3) 
            elif procesar.lower() == "t":
                gotoxy(7,len(lista_clientes)+11);print(bright_pink_color+"Estás seguro de eliminar todos los clientes?(y/n):")
                gotoxy(59,len(lista_clientes)+11);procesar = input().lower()
                if procesar.lower() == 'y':
                    lista_clientes=[]
                    json_file.save(lista_clientes)
                    gotoxy(7,len(lista_clientes)+13);print(bright_pink_color+"Eliminado con exito! ✅")
                    time.sleep(2)
                else:
                    gotoxy(7,len(lista_clientes)+13);print(red_color+"Eliminacion cancelada❌...")
                    time.sleep(2)
        else:  
            gotoxy(60,9);print(bright_pink_color+"No se han registrado clientes 📖")
        time.sleep(3)

    def consult(self):
        validar = Valida()
        borrarPantalla()
        gotxy_frame(0,0,167,100)
        gotoxy(65,2);print("Consultar cliente")
        gotoxy(2,3);print(bright_pink_color+"*"*167)
        json_file = JsonFile(path+'/archivos/clients.json')
        lista_clientes=json_file.read()
        gotxy_frame(25,4,100,len(lista_clientes)+5)
        gotoxy(65,5);print(f"Lista de clientes")
        gotoxy(34,6);print(f"DNI")
        gotoxy(64,6);print(f"NOMBRE")
        gotoxy(94,6);print(f"APELLIDO")
        if lista_clientes:
            for i in range(len(lista_clientes)):
                gotoxy(34,7+i);print(f"{ lista_clientes[i]['dni']}")
                gotoxy(64,7+i);print(f"{ lista_clientes[i]['nombre']}")
                gotoxy(94,7+i);print(f"{ lista_clientes[i]['apellido']}")
        
            gotoxy(25,len(lista_clientes)+9);print("Ingresa tu DNI:")
            gotoxy(41,len(lista_clientes)+9);dni = validar.validar_numero_dni("Error: DNI no valido", 41, len(lista_clientes)+9)
        
            cliente_dni = json_file.find("dni",dni)
            if cliente_dni:
                gotxy_frame(25,len(lista_clientes)+10,100,5)
                gotoxy(55,len(lista_clientes)+11);print(f"Datos del cliente con DNI: {cliente_dni[0]['dni']}")
                gotoxy(40,len(lista_clientes)+12);print(f"DNI")
                gotoxy(70,len(lista_clientes)+12);print(f"Nombre")
                gotoxy(100,len(lista_clientes)+12);print(f"Apellido")
                gotoxy(40,len(lista_clientes)+13);print(f"{cliente_dni[0]['dni']}")
                gotoxy(70,len(lista_clientes)+13);print(f"{cliente_dni[0]['nombre']}")
                gotoxy(100,len(lista_clientes)+13);print(f"{cliente_dni[0]['apellido']}")
                lista_clientes_vip = list(filter(lambda x : x['valor']==10000,lista_clientes))
                if lista_clientes_vip:
                    gotxy_frame(25,len(lista_clientes)+15,100,len(lista_clientes_vip)+4)
                    gotoxy(65,len(lista_clientes)+16);print(f"Lista de clientes VIP")
                    gotoxy(34,len(lista_clientes)+17);print(f"DNI")
                    gotoxy(64,len(lista_clientes)+17);print(f"NOMBRE")
                    gotoxy(94,len(lista_clientes)+17);print(f"APELLIDO")
                    for i in range(len(lista_clientes_vip)):
                        gotoxy(34,len(lista_clientes)+18+i);print(f"{ lista_clientes_vip[i]['dni']}")
                        gotoxy(64,len(lista_clientes)+18+i);print(f"{ lista_clientes_vip[i]['nombre']}")
                        gotoxy(94,len(lista_clientes)+18+i);print(f"{ lista_clientes_vip[i]['apellido']}")
            
            else:
                gotoxy(70,11);print(bright_pink_color+'Cliente no existe 😬')
        else:
            gotoxy(70,11);print(bright_pink_color+'No se han registrado clientes🥲')
        time.sleep(5) 

class CrudProducts(ICrud):
    def create(self):
        valida = Valida()
        borrarPantalla()
        gotxy_frame(0,0,167,100)
        gotoxy(65, 2); print(bright_pink_color + "Registro de Producto")
        gotoxy(50,3); print(bright_pink_color + Company.get_business_name())
        gotoxy(2,4);print(bright_pink_color+"*"*167)
        gotoxy(7,6);print("Ingresa el producto:")
        gotoxy(7,7);print("Ingresa el precio:")
        gotoxy(7,8);print("Ingresa el stock:")
        gotoxy(28,6);description = valida.validar_nombre_cliente(col=28, fil=6)
        gotoxy(26,7);price = valida.solo_decimales('','Error: solo decimales')
        gotoxy(25,8);stock = valida.solo_numeros('Error: Debe ser entero',col=25, fil=8)
        json_file = JsonFile(path + '/archivos/products.json')
        products = json_file.read()
        last_id = products[-1]["id"] + 1 if products else 1
        new_product = Product( last_id, description, price, stock)
        encontrado = json_file.find("descripcion", description)
        gotoxy(7,9);print(bright_pink_color+"Esta seguro de guardar el producto(y/n):")
        gotoxy(48,9);procesar = input().lower()
        if procesar == 'y':
            if encontrado:
                gotoxy(7,10);print(bright_pink_color+"Producto ya registrado. 😢")
                time.sleep(2)
                return
            else:
                products.append(new_product.getJson())
                json_file.save(products)
                gotoxy(7, 10); print(bright_pink_color+"Producto registrado exitosamente! ✅")
                time.sleep(2)
        else:
            gotoxy(7,10);print(red_color+"Registro cancelado ❌...")    
        time.sleep(2) 
        
    def update(self):
        validar = Valida()
        borrarPantalla()
        gotxy_frame(0,0,167,100)
        gotoxy(65,2);print("Actualizar Producto")
        gotoxy(2,3);print(bright_pink_color+"*"*167)
        json_file = JsonFile(path+'/archivos/products.json')
        lista_productos=json_file.read()
        if lista_productos:
            gotxy_frame(25,4,110,len(lista_productos)+5)
            gotoxy(34,6);print(f"ID")
            gotoxy(64,6);print(f"Descripcion")
            gotoxy(94,6);print(f"Precio")
            gotoxy(124,6);print(f"Stock")
            gotoxy(65,5);print(f"Lista de Productos ")
            if lista_productos:
                for i in range(len(lista_productos)):
                    gotoxy(34,7+i);print(f"{ lista_productos[i]['id']}")
                    gotoxy(64,7+i);print(f"{ lista_productos[i]['descripcion']}")
                    gotoxy(94,7+i);print(f"{ lista_productos[i]['precio']}")
                    gotoxy(124,7+i);print(f"{ lista_productos[i]['stock']}")
            gotoxy(6,len(lista_productos)+9);print("Ingresa el id:")
            gotoxy(21,len(lista_productos)+9);id = validar.solo_numeros('Error: Debe ser entero',21,len(lista_productos)+9)
            product_id = json_file.find("id",int(id))
            if product_id:
                gotxy_frame(25,len(lista_productos)+10,125,7)
                gotoxy(55,len(lista_productos)+11);print(f"Datos del producto con el ID: #{product_id[0]['id']}")
                gotoxy(25,len(lista_productos)+12);print(bright_pink_color+"*"*125)
                gotoxy(40,len(lista_productos)+13);print(f"id")
                gotoxy(70,len(lista_productos)+13);print(f"Descripcion")
                gotoxy(100,len(lista_productos)+13);print(f"Precio")
                gotoxy(120,len(lista_productos)+13);print(f"Stock")
                gotoxy(40,len(lista_productos)+14);print(f"{product_id[0]['id']}")
                gotoxy(70,len(lista_productos)+14);print(f"{product_id[0]['descripcion']}")
                gotoxy(100,len(lista_productos)+14);print(f"{product_id[0]['precio']}")
                gotoxy(120,len(lista_productos)+14);print(f"{product_id[0]['stock']}")
                while True:   
                    menu_main = Menu("Selecciona que dato deseas actualizar",["1) Descripcion","2) Precio", "3) Stock","4) Salir"],55,len(lista_productos)+18) 
                    opc = menu_main.menu()
                    if opc == "1":
                        borrarPantalla()
                        gotxy_frame(0,0,167,100)
                        gotoxy(65,2);print("Actualizar descripcion del producto")
                        gotoxy(2,3);print(bright_pink_color+"*"*167)
                        gotoxy(6,4);print("Ingresa la nueva descripcion:")
                        gotoxy(38,4);descripcion = validar.validar_nombre_cliente(36,4)
                        data=json_file.read()
                        producto=product_id[0]
                        gotoxy(6,5);print(bright_pink_color+"Estas seguro de actualizar tus datos🤔?(y/n):")
                        gotoxy(52,5);procesar = input().lower()
                        if procesar.lower() == "y":
                            for i in data:
                                if i['id'] == producto['id']:
                                    i['descripcion']=descripcion
                                    gotoxy(6,6);print(bright_pink_color+"Actualizado con exito ✅")
                                    time.sleep(1)
                            json_file.save(data)
                            time.sleep(1)
                            break
                        else:
                            gotoxy(6,6);print(red_color+"Se cancelo la actualizacion❌...")
                            time.sleep(1)
                            break
                    elif opc == "2":
                        borrarPantalla()
                        gotxy_frame(0,0,167,100)
                        gotoxy(65,2);print("Actualizar precio del producto")
                        gotoxy(2,3);print(bright_pink_color+"*"*167)
                        gotoxy(6,4);print("Ingresa el nuevo precio del producto:")
                        gotoxy(49,4);precio_nuevo = validar.solo_decimales('','Error: solo decimales')
                        data=json_file.read()
                        producto=product_id[0]
                        gotoxy(6,5);print(bright_pink_color+"Estas seguro de actualizar tus datos?🤔 (y/n):")
                        gotoxy(52,5);procesar = input().lower()
                        if procesar.lower() == "y":
                            for i in data:
                                if i['id'] == producto['id']:
                                    i['precio']=precio_nuevo
                                    gotoxy(6,6);print(green_color+"Actualizado con exito! ✅")
                                    time.sleep(1)
                            json_file.save(data)
                            time.sleep(1)
                            break
                        else:
                            gotoxy(6,6);print(red_color+"Se cancelo la actualizacion❌...")
                            time.sleep(1)
                            break
                    elif opc == "3":
                        borrarPantalla()
                        gotxy_frame(0,0,167,100)
                        gotoxy(65,2);print("Actualizar stock del producto")
                        gotoxy(2,3);print(bright_pink_color+"*"*167)
                        gotoxy(6,4);print("Ingresa el nuevo stock:")
                        gotoxy(30,4);stock = validar.solo_numeros('Error: Solo numeros',30,4)
                        data=json_file.read()
                        producto=product_id[0]
                        gotoxy(6,5);print(red_color+"Estas seguro de actualizar tus datos?🤔 (y/n):")
                        gotoxy(53,5);procesar = input().lower()
                        if procesar.lower() == "y":
                            for i in data:
                                if i['id'] == producto['id']:
                                    i['stock']=stock
                                    gotoxy(6,6);print(bright_pink_color+"Actualizado con exito! ✅")
                                    time.sleep(1)
                            json_file.save(data)
                            time.sleep(1)
                            break
                        else:
                            gotoxy(6,6);print(red_color+"Se cancelo la actualizacion...")
                            time.sleep(1)
                            break
                    elif opc == "4":
                        break
            else:
                gotoxy(25,len(lista_productos)+12);print(bright_pink_color+"El Id del producto no se encuentra registrado... 😬")
                time.sleep(1)
        else:
            gotoxy(6,6);print(bright_pink_color+"No hay productos registrados...🥲")
            time.sleep(2)
        time.sleep(3)

    def delete(self):
        validar = Valida()
        borrarPantalla()
        gotxy_frame(0,0,167,100)
        gotoxy(65,2);print("Productos Disponibles")
        gotoxy(2,3);print(bright_pink_color+"*"*167)
        json_file = JsonFile(path+'/archivos/products.json')
        products = json_file.read()
        if products:
            gotxy_frame(25,4,125,len(products)+3)
            gotoxy(40,5);print(f"id")
            gotoxy(70,5);print(f"Descripcion")
            gotoxy(100,5);print(f"Precio")
            gotoxy(120,5);print(f"Stock")
            for i in range(len(products)):
                gotoxy(40,6+i);print(f"{products[i]['id']}")
                gotoxy(70,6+i);print(f"{products[i]['descripcion']}")
                gotoxy(100,6+i);print(f"{products[i]['precio']}")
                gotoxy(120,6+i);print(f"{products[i]['stock']}")
            gotoxy(25,len(products)+7);print(red_color+"Escoge un metodo de eliminacion(T/ID):")
            gotoxy(65,len(products)+7);procesar = input().lower()
            if procesar.lower() == "id":
                while True:
                    gotoxy(25,len(products)+8);print("Ingresa el ID:")
                    gotoxy(41,len(products)+8);id = validar.solo_numeros("Error: ID debe ser entero", 41, len(products)+8)
                    product_id = json_file.find("id",int(id))
                    if len(product_id) != 0:
                        gotoxy(25,len(products)+9);print(red_color+"Estás seguro de realizar la eliminacion? 🤔 (y/n):")
                        gotoxy(75,len(products)+9);procesar = input().lower()
                        if procesar.lower()=='y':
                            products.remove(product_id[0])
                            json_file.save(products)
                            gotoxy(25,len(products)+11);print(bright_pink_color+"Eliminado con exito! ✅")
                            break
                        else:
                            gotoxy(25,len(products)+11);print(red_color+"Eliminacion cancelada... ❌")
                            time.sleep(2)
                            break
                    else:
                        gotoxy(24,len(products)+9);print(bright_pink_color+"DNI no encontrado📖")
                        time.sleep(3) 
            elif procesar.lower() == "t":
                gotoxy(25,len(products)+8);print(bright_pink_color+"Estás seguro de eliminar todos los productos?🤔(y/n):")
                gotoxy(80,len(products)+8);procesar = input().lower()
                if procesar.lower() == 'y':
                    products=[]
                    json_file.save(products)
                    gotoxy(25,len(products)+11);print(bright_pink_color+"Se elimino todo correctamente! ✅")
                    time.sleep(2)
                else:
                    gotoxy(25,len(products)+11);print(red_color+"Eliminacion cancelada...❌")
                    time.sleep(2)
        else:  
            gotoxy(10,3);print(bright_pink_color+"No se han agregado productos🥲")
        time.sleep(3)
    
    def consult(self):
        validar = Valida()
        borrarPantalla()
        gotxy_frame(0,0,167,100)
        gotoxy(65,2);print("Consultar producto")
        gotoxy(2,3);print(bright_pink_color+"*"*167)
        
        json_file = JsonFile(path+'/archivos/products.json')
        lista_productos=json_file.read()
        gotxy_frame(32,4,80,len(lista_productos)+5)
        gotoxy(34,6);print(f"ID")
        gotoxy(64,6);print(f"Producto")
        gotoxy(65,5);print(f"Lista de Productos ")
        if lista_productos:
            for i in range(len(lista_productos)):
                gotoxy(34,7+i);print(f"{ lista_productos[i]['id']}")
                gotoxy(64,7+i);print(f"{ lista_productos[i]['descripcion']}")
            gotoxy(7,len(lista_productos)+10);print("Ingresa el ID del producto:")
            gotoxy(35,len(lista_productos)+10);id = validar.solo_numeros("Error: ID debe ser entero", 35, len(lista_productos)+10)
            producto_id = json_file.find("id",int(id))
            if producto_id:
                gotxy_frame(25,len(lista_productos)+12,120,7)
                gotoxy(65,len(lista_productos)+13);print(bright_pink_color+f"Datos del producto con id: #{producto_id[0]['id']}")
                gotoxy(25,len(lista_productos)+14);print(bright_pink_color+"*"*120)
                gotoxy(30,len(lista_productos)+15);print(f"id")
                gotoxy(60,len(lista_productos)+15);print(f"Descripcion")
                gotoxy(90,len(lista_productos)+15);print(f"Precio")
                gotoxy(120,len(lista_productos)+15);print(f"Stock")
                gotoxy(30,len(lista_productos)+16);print(f"{producto_id[0]['id']}")
                gotoxy(60,len(lista_productos)+16);print(f"{producto_id[0]['descripcion']}")
                gotoxy(90,len(lista_productos)+16);print(f"{producto_id[0]['precio']}")
                gotoxy(120,len(lista_productos)+16);print(f"{producto_id[0]['stock']}")
                totales_map = list(map(lambda producto: producto["stock"], lista_productos))
                lista_productos_stock_mayor = list(filter(lambda x : int(x['stock'])>=50,lista_productos))
                if lista_productos_stock_mayor:
                    gotxy_frame(25,len(lista_productos)+19,120,len(lista_productos_stock_mayor)+4)
                    gotoxy(65,len(lista_productos)+20);print(f"Lista de con un stock superior a las 50 unidades")
                    gotoxy(34,len(lista_productos)+21);print(f"ID")
                    gotoxy(64,len(lista_productos)+21);print(f"Producto")
                    gotoxy(94,len(lista_productos)+21);print(f"Precio")
                    gotoxy(124,len(lista_productos)+21);print(f"Stock")
                    for i in range(len(lista_productos_stock_mayor)):
                        gotoxy(34,len(lista_productos)+22+i);print(f"{ lista_productos_stock_mayor[i]['id']}")
                        gotoxy(64,len(lista_productos)+22+i);print(f"{ lista_productos_stock_mayor[i]['descripcion']}")
                        gotoxy(94,len(lista_productos)+22+i);print(f"{ lista_productos_stock_mayor[i]['precio']}")
                        gotoxy(124,len(lista_productos)+22+i);print(f"{ lista_productos_stock_mayor[i]['stock']}")
                    gotoxy(60,len(lista_productos)+25);print(bright_pink_color+f"Map stock de productos: {totales_map}")
                gotoxy(60,len(lista_productos)+26);print(bright_pink_color+f"Gacias por usar el sistema💫")
                time.sleep(5)
            else:
                gotoxy(60,len(lista_productos_stock_mayor)+18);print(bright_pink_color+'Producto no existe ⚠️')
            time.sleep(5)
        else:
            gotoxy(60,11);print(bright_pink_color+'No hay productos pregistrados🥲')
        time.sleep(5)

class CrudSales(ICrud):
    def create(self):
        # cabecera de la venta
        validar = Valida()
        borrarPantalla()
        gotxy_frame(0,0,167,100)
        gotoxy(30,2);print(bright_pink_color+"Registro de Venta")
        gotoxy(17,3);print(bright_pink_color+Company.get_business_name())
        gotoxy(5,4);print(f"Factura#:F0999999 {' '*3} Fecha:{datetime.datetime.now()}")
        gotoxy(66,4);print("Subtotal:")
        gotoxy(66,5);print("Decuento:")
        gotoxy(66,6);print("Iva     :")
        gotoxy(66,7);print("Total   :")
        gotoxy(15,6);print("Cedula:")
        dni=validar.validar_numero_dni("Error: Sin fomato DNI",23,6)
        json_file = JsonFile(path+'/archivos/clients.json')
        client = json_file.find("dni",dni)
        if not client:
            gotoxy(35,6);print("Cliente no existe")
            time.sleep(2)
            return
        client = client[0]
        cli = RegularClient(client["nombre"],client["apellido"], client["dni"], card=True) 
        sale = Sale(cli)
        gotoxy(35,6);print(cli.fullName())
        gotoxy(2,8);print(bright_pink_color+"*"*90+reset_color) 
        gotoxy(5,9);print(bright_pink_color+"Linea") 
        gotoxy(12,9);print("Id_Articulo") 
        gotoxy(24,9);print("Descripcion") 
        gotoxy(38,9);print("Precio") 
        gotoxy(48,9);print("Cantidad") 
        gotoxy(58,9);print("Subtotal") 
        gotoxy(70,9);print("n->Terminar Venta)"+reset_color)
        # detalle de la venta
        follow ="s"
        line=1
        while follow.lower()=="s":
            gotoxy(7,9+line);print(line)
            gotoxy(15,9+line)
            id=int(validar.solo_numeros("Error: Solo numeros",15,9+line))
            json_file = JsonFile(path+'/archivos/products.json')
            prods = json_file.find("id",id)
            if not prods:
                gotoxy(24,9+line);print(bright_pink_color+"Producto no existe ⚠️")
                time.sleep(1)
                gotoxy(24,9+line);print(" "*20)
            else:    
                prods = prods[0]
                product = Product(prods["id"],prods["descripcion"],prods["precio"],prods["stock"])
                gotoxy(24,9+line);print(product.descrip)
                gotoxy(38,9+line);print(product.preci)
                gotoxy(49,9+line);qyt=int(validar.solo_numeros("Error:Solo numeros",49,9+line))
                gotoxy(59,9+line);print(product.preci*qyt)
                sale.add_detail(product,qyt)
                gotoxy(76,4);print(round(sale.subtotal,2))
                gotoxy(76,5);print(round(sale.discount,2))
                gotoxy(76,6);print(round(sale.iva,2))
                gotoxy(76,7);print(round(sale.total,2))
                gotoxy(74,9+line);follow=input() or "s"  
                gotoxy(76,9+line);print(green_color+"🛒✔"+reset_color)  
                line += 1
        gotoxy(15,9+line);print(bright_pink_color+"Esta seguro de grabar la venta(s/n):")
        gotoxy(54,9+line);procesar = input().lower()
        if procesar == "s":
            gotoxy(15,10+line);print(bright_pink_color+"😊 Venta Grabada satisfactoriamente 😊")
            # print(sale.getJson())  
            json_file = JsonFile(path+'/archivos/invoices.json')
            invoices = json_file.read()
            ult_invoices = invoices[-1]["factura"]+1 if invoices else 1
            data = sale.getJson()
            data["factura"]=ult_invoices
            invoices.append(data)
            json_file = JsonFile(path+'/archivos/invoices.json')
            json_file.save(invoices)
        else:
            gotoxy(20,10+line);print(red_color+" Venta Cancelada ⚠️")    
        time.sleep(2)
        
    def update(self):
        validar = Valida()
        borrarPantalla()
        gotxy_frame(0,0,167,100)
        gotoxy(65,2);print("Actualizar factura")
        gotoxy(2,3);print(bright_pink_color+"*"*167)
        json_file_invoices_data = JsonFile(path + '/archivos/invoices.json')
        invoices = json_file_invoices_data.read()
        if invoices:
            gotxy_frame(25,4,100,len(invoices)+3)
            gotoxy(40,5);print(f"Factura")
            gotoxy(70,5);print(f"Fecha")
            gotoxy(100,5);print(f"Cliente")
            for i in range(len(invoices)):
                gotoxy(40,6+i);print(f"{invoices[i]['factura']}")
                gotoxy(70,6+i);print(f"{invoices[i]['Fecha']}")
                gotoxy(100,6+i);print(f"{invoices[i]['cliente']}")
            gotoxy(25,len(invoices)+8);print("Ingresa el # de la factura:")
            gotoxy(53,len(invoices)+8);id_factura = validar.solo_numeros("Error: ID debe ser entero", 53, len(invoices)+8)
            json_file = JsonFile(path+'/archivos/invoices.json')
            factura_id = json_file.find("factura",int(id_factura))
            if factura_id:
                detalle = factura_id[0]['detalle']
                borrarPantalla()
                gotxy_frame(0,0,167,100)
                gotxy_frame(25,8,120,len(detalle)+5)
                gotoxy(7, 6); print(" " * (50))
                gotoxy(60, 2); print(" " * (50))
                gotoxy(2, 3); print(" " * (164))
                gotoxy(65,2);print(bright_pink_color+" Actualizar Factura ")
                gotoxy(50,3);print(bright_pink_color+Company.get_business_name())
                gotoxy(30,4);print(f"Factura#: {factura_id[0]['factura']} {' '*60} Fecha: {factura_id[0]['Fecha']}")
                gotoxy(30,5);print(f"Cliente: {factura_id[0]['cliente']}")
                gotoxy(2,7);print(bright_pink_color+"*"*164)
                gotoxy(65,9);print(f"Detalles de la compra")
                gotoxy(25,10);print(bright_pink_color+"*"*120)
                gotoxy(30,11);print(f"#")
                gotoxy(60,11);print(f"Producto")
                gotoxy(90,11);print(f"Precio")
                gotoxy(120,11);print(f"Cantidad")
                for i in range(len(detalle)):
                    gotoxy(30,12+i);print(f"{i+1}")
                    gotoxy(60,12+i);print(f"{detalle[i]['poducto']}")
                    gotoxy(90,12+i);print(f"{detalle[i]['precio']}")
                    gotoxy(120,12+i);print(f"{detalle[i]['cantidad']}")
                gotxy_frame(120,len(detalle)+12,25,6)
                gotoxy(122,len(detalle)+13);print(f"Subtotal: {factura_id[0]['subtotal']}")
                gotoxy(122,len(detalle)+14);print(f"Decuento: {round(factura_id[0]['descuento'],2)}")
                gotoxy(122,len(detalle)+15);print(f"Iva     : {factura_id[0]['iva']}")
                gotoxy(122,len(detalle)+16);print(f"Total   : {factura_id[0]['total']}")
                gotxy_frame(8,len(detalle)+14,50,8)
                menu_update = Menu("¿Qué opción desea modificar?", ["1) Toda la factura", "2) Salir",], 15, len(detalle)+15)  
                opcion = menu_update.menu()
                while opcion !='2': 
                    
                    if opcion == "1":
                        gotxy_frame(65,len(detalle)+14,54,19)
                        gotoxy(67,len(detalle)+15);print(bright_pink_color+"Productos en el detalle:")
                        for i in range(len(detalle)):
                            gotoxy(67,len(detalle)+16+i);print(f"{i + 1}. {detalle[i]['poducto']} - Cantidad: {detalle[i]['cantidad']}")
                        gotoxy(67,len(detalle)+19);print(bright_pink_color+'Escoge el indice:')
                        gotoxy(85,len(detalle)+19);indice_producto = int(validar.solo_numeros('Error: Solo enteros',85,len(detalle)+19)) - 1
                        if 0 <= indice_producto < len(detalle):
                            gotoxy(67,len(detalle)+20);print(bright_pink_color+'Ingresa el Id del nuevo Producto:')
                            gotoxy(100,len(detalle)+20);id = validar.solo_numeros('Error: Solo numeros',100,len(detalle)+20)
                            json_file_producto = JsonFile(path + '/archivos/products.json')
                            product_id = json_file_producto.find('id',int(id))
                            json_file_cliente = JsonFile(path + '/archivos/clients.json')
                            if product_id:
                                gotoxy(67,len(detalle)+21);print(bright_pink_color+'Nueva cantidad:')
                                gotoxy(83,len(detalle)+21);nueva_cantidad = int(validar.solo_numeros('Error: Solo enteros',83,len(detalle)+21))
                                gotoxy(67,len(detalle)+22);print(bright_pink_color+"Confirma tu DNI:")
                                gotoxy(84,len(detalle)+22);dni = validar.solo_numeros("Error: Solo números",84,len(detalle)+22)
                                gotoxy(67,len(detalle)+23);print(bright_pink_color+"Tipo de cliente (r/v):")
                                gotoxy(92,len(detalle)+23);respuesta=input().lower()
                                cliente_nombre = json_file_cliente.find('dni',dni)
                                if cliente_nombre:
                                    cliente=cliente_nombre[0]
                                    cli = RegularClient(dni=cliente['dni'],first_name=cliente['nombre'].upper(),last_name=cliente['apellido'].upper(),card=True) if respuesta.lower() == 'r' else VipClient(dni=cliente['dni'],first_name=cliente['nombre'].upper(),last_name=cliente['apellido'].upper())
                                    sale = Sale(cli)
                                    nuevo_producto = {
                                        "poducto": product_id[0]['descripcion'],
                                        "precio": product_id[0]['precio'],
                                        "cantidad": nueva_cantidad
                                    }
                                    detalle[indice_producto] = nuevo_producto
                                    for detail in range(len(detalle)):
                                        producto_buscado_id=json_file_producto.find('descripcion',detalle[detail]['poducto'])
                                        product = Product(producto_buscado_id[0]["id"],producto_buscado_id[0]["descripcion"],producto_buscado_id[0]["precio"],producto_buscado_id[0]["stock"])
                                        sale.add_detail(product, int(detalle[detail]['cantidad']))  # Agrega el detalle de la venta
                                    gotoxy(67,len(detalle)+25);print(bright_pink_color+f"Subtotal: {round(sale.subtotal, 2)}")
                                    gotoxy(67,len(detalle)+26);print(bright_pink_color+f"Descuento: {round(sale.discount, 2)}")
                                    gotoxy(67,len(detalle)+27);print(bright_pink_color+f"Iva     : {round(sale.iva, 2)}")
                                    gotoxy(67,len(detalle)+28);print(bright_pink_color+f"Total   : {round(sale.total, 2)}")
                                    gotoxy(67,len(detalle)+29);print(bright_pink_color + "¿Guardar cambios?(s/n): ")
                                    gotoxy(90,len(detalle)+29);procesar = input().lower()  # Pregunta si se quiere grabar la venta
                                    if procesar == "s":
                                        gotoxy(67,len(detalle)+31);print(bright_pink_color+"🎀 Actualización Grabada Satisfactoriamente 🎀")       
                                        data = sale.getJson()
                                        data["factura"] = factura_id[0]['factura']
                                        invoices[int(id_factura)-1] = data
                                        json_file = JsonFile(path + '/archivos/invoices.json')
                                        json_file.save(invoices)
                                        time.sleep(2)
                                        break
                                    else:
                                        gotoxy(67,len(detalle)+31);print(red_color+"Se cancelo la actualizacion❌.")
                                        time.sleep(2)
                                else:
                                    gotoxy(67,len(detalle)+24);print(bright_pink_color+"El cliente no existe.⚠️")
                                    time.sleep(2)
                            else:
                                gotoxy(84,len(detalle)+23);print(bright_pink_color+"Producto no existe.⚠️")
                                time.sleep(1)
                        else:
                            gotoxy(67,len(detalle)+21);print(red_color+"Índice de producto no válido. ❌")
                        break
                    
                    elif opcion == "2":
                        break
            else:
                gotoxy(60,len(invoices)+7);print(bright_pink_color+"No se encontro la factura ⚠️")
        else:
            gotoxy(60,len(invoices)+7);print(bright_pink_color+"No se ha registrado 🥲")


    
    def delete(self):
        validar = Valida()
        borrarPantalla()
        gotxy_frame(0,0,167,100)
        gotoxy(65,2);print("Facturas Registradas")
        gotoxy(2,3);print(bright_pink_color+"*"*167)
        json_file = JsonFile(path+'/archivos/invoices.json')
        facturas = json_file.read()
        if facturas:
            gotxy_frame(25,4,100,len(facturas)+3)
            gotoxy(40,5);print(bright_pink_color+f"Factura")
            gotoxy(70,5);print(bright_pink_color+f"Fecha")
            gotoxy(100,5);print(bright_pink_color+f"Cliente")
            for i in range(len(facturas)):
                gotoxy(40,6+i);print(f"{facturas[i]['factura']}")
                gotoxy(70,6+i);print(f"{facturas[i]['Fecha']}")
                gotoxy(100,6+i);print(f"{facturas[i]['cliente']}")
            gotoxy(25,len(facturas)+7);print(bright_pink_color+"Escoge un metodo de eliminacion(T/ID):")
            gotoxy(65,len(facturas)+7);procesar = input().lower()
            if procesar.lower() == "id":
                while True:
                    gotoxy(25,len(facturas)+8);print("Ingresa el ID:")
                    gotoxy(41,len(facturas)+8);id = validar.solo_numeros("Error: ID debe ser entero", 41, len(facturas)+8)
                    factura_id = json_file.find("factura",int(id))
                    if factura_id:
                        gotoxy(25,len(facturas)+9);print(bright_pink_color+"Estás seguro de realizar la eliminacion?(y/n):")
                        gotoxy(75,len(facturas)+9);procesar = input().lower()
                        if procesar.lower()=='y':
                            facturas.remove(factura_id[0])
                            json_file.save(facturas)
                            gotoxy(25,len(facturas)+11);print(bright_pink_color+"Eliminado con exito ✅")
                            break
                        else:
                            gotoxy(25,len(facturas)+10);print(red_color+"Eliminacion cancelada... ❌")
                            time.sleep(2)
                            break
                    else:
                        gotoxy(24,len(facturas)+9);print(bright_pink_color+"DNI no encontrado⚠️")
                        time.sleep(3) 
            elif procesar.lower() == "t":
                gotoxy(25,len(facturas)+8);print(bright_pink_color+"Estas seguro de eliminar todos los productos?🤔(y/n):")
                gotoxy(80,len(facturas)+8);procesar = input().lower()
                if procesar.lower() == 'y':
                    facturas=[]
                    json_file.save(facturas)
                    gotoxy(25,len(facturas)+11);print(bright_pink_color+"Se elimino todo correctamente ✅")
                    time.sleep(2)
                else:
                    gotoxy(25,len(facturas)+9);print(red_color+"Eliminacion cancelada...❌")
                    time.sleep(2)
        else:  
            gotoxy(60,5);print(bright_pink_color+"No se han agregado productos🥲")
        time.sleep(3)
            
    
    def consult(self):
        borrarPantalla()
        gotxy_frame(0,0,167,100)
        gotoxy(65,2);print("Consultar factura")
        gotoxy(2,3);print(bright_pink_color+"*"*165)
        gotoxy(7,6);print("Ingresa el # de la factura o enter para todas: ")
        gotoxy(55,6);id = input()
        json_file = JsonFile(path+'/archivos/invoices.json')
        facturas = json_file.read()
        if id:
            factura_id = json_file.find("factura",int(id))
            if factura_id:
                detalle = factura_id[0]['detalle']
                gotxy_frame(25,8,120,len(detalle)+5)
                gotoxy(7, 6); print(" " * (50))
                gotoxy(60, 2); print(" " * (50))
                gotoxy(2, 3); print(" " * (164))
                gotoxy(65,2);print(bright_pink_color+" Consultar Factura ")
                gotoxy(50,3);print(bright_pink_color+Company.get_business_name())
                gotoxy(30,4);print(f"Factura#: {factura_id[0]['factura']} {' '*60} Fecha: {factura_id[0]['Fecha']}")
                gotoxy(30,5);print(f"Cliente: {factura_id[0]['cliente']}")
                gotoxy(2,7);print(bright_pink_color+"*"*164)
                gotoxy(65,9);print(bright_pink_color+f"Detalles de la compra")
                gotoxy(25,10);print(bright_pink_color+"*"*120)
                gotoxy(30,11);print(f"#")
                gotoxy(60,11);print(f"Producto")
                gotoxy(90,11);print(f"Precio")
                gotoxy(120,11);print(f"Cantidad")
                for i in range(len(detalle)):
                    gotoxy(30,12+i);print(f"{i+1}")
                    gotoxy(60,12+i);print(f"{detalle[i]['poducto']}")
                    gotoxy(90,12+i);print(f"{detalle[i]['precio']}")
                    gotoxy(120,12+i);print(f"{detalle[i]['cantidad']}")
                gotxy_frame(120,len(detalle)+12,25,6)
                gotoxy(122,len(detalle)+13);print(f"Subtotal: {factura_id[0]['subtotal']}")
                gotoxy(122,len(detalle)+14);print(f"Decuento: {round(factura_id[0]['descuento'],2)}")
                gotoxy(122,len(detalle)+15);print(f"Iva     : {factura_id[0]['iva']}")
                gotoxy(60,len(detalle)+16);print(bright_pink_color+f"Gacias por usar el sistema😎")
            else:
                gotoxy(60,11);print('Factura no existe⚠️')
        else:
            gotxy_frame(25,7,120,len(facturas)+5)
            gotoxy(65,8);print(f"Facturas registradas")
            gotoxy(27,10);print(f"#Factura")
            gotoxy(57,10);print(f"Fecha")
            gotoxy(87,10);print(f"Cliente")
            for i in range(len(facturas)):
                gotoxy(27,11+i);print(f"{facturas[i]['factura']}")
                gotoxy(57,11+i);print(f"{facturas[i]['Fecha']}")
                gotoxy(87,11+i);print(f"{facturas[i]['cliente']}")
            suma = reduce(lambda total, invoice: round(total+ invoice["total"],2), facturas,0)
            totales_map = list(map(lambda invoice: invoice["total"], facturas))
            max_invoice = max(totales_map)
            min_invoice = min(totales_map)
            tot_invoices = sum(totales_map)
            gotoxy(25,9);print(bright_pink_color+"*"*120)
            gotxy_frame(25,len(facturas)+11,60,8)
            gotoxy(40,len(facturas)+12);print(bright_pink_color+f"Detalles de facturas en general")
            gotoxy(27,len(facturas)+13);print(bright_pink_color+f"Map Facturas:{totales_map}")
            gotoxy(27,len(facturas)+14);print(bright_pink_color+f"Max Factura:{max_invoice}")
            gotoxy(27,len(facturas)+15);print(bright_pink_color+f"Min Factura:{min_invoice}")
            gotoxy(27,len(facturas)+16);print(bright_pink_color+f"Sum Factura:{tot_invoices}")
            gotoxy(27,len(facturas)+17);print(bright_pink_color+f"Reduce Facturas:{suma}")
            time.sleep(10)

#Menu Proceso Principal
opc=''
while opc !='4':  
    borrarPantalla()
    gotxy_frame(0,0,167,100)      
    menu_main = Menu("Menu Facturacion",["1) Clientes","2) Productos","3) Ventas","4) Salir"],20,10)
    opc = menu_main.menu()
    if opc == "1":
        opc1 = ''
        while opc1 !='5':
            borrarPantalla() 
            gotxy_frame(0,0,167,100)
            clients = CrudClients()  
            menu_clients = Menu("Menu Cientes",["1) Registrar cliente","2) Actualizar","3) Eliminar","4) Consultar","5) Salir"],20,10)
            opc1 = menu_clients.menu()
            if opc1 == "1":
                clients.create()
                
            elif opc1 == "2":
                clients.update()
                
            elif opc1 == "3":
                clients.delete()
            elif opc1 == "4":
                clients.consult()
            print("Regresando al menu Clientes...")
            time.sleep(2)            
    elif opc == "2":
        opc2 = ''
        while opc2 !='5':
            borrarPantalla()
            gotxy_frame(0,0,167,100)
            products = CrudProducts()    
            menu_products = Menu("Menu Productos",["1) Ingresar","2) Actualizar","3) Eliminar","4) Consultar","5) Salir"],20,10)
            opc2 = menu_products.menu()
            if opc2 == "1":
                products.create()
            elif opc2 == "2":
                products.update()
            elif opc2 == "3":
                products.delete()
            elif opc2 == "4":
                products.consult()
    elif opc == "3":
        opc3 =''
        while opc3 !='5':
            borrarPantalla()
            gotxy_frame(0,0,167,100)
            sales = CrudSales()
            menu_sales = Menu("Menu Ventas",["1) Registro Venta","2) Consultar","3) Modificar","4) Eliminar","5) Salir"],20,10)
            opc3 = menu_sales.menu()
            if opc3 == "1":
                sales.create()
                
            elif opc3 == "2":
                sales.consult()
                time.sleep(2)
            elif opc3 == "3":
                sales.update()
                time.sleep(2)
            elif opc3 == "4":
                sales.delete()
                time.sleep(2)
    

    print("Regresando al menu Principal...")       

borrarPantalla()
input("Presione una tecla para salir...")
borrarPantalla()

