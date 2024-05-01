from utilities import borrarPantalla, gotoxy
import time

class Menu:
    def __init__(self,titulo="",opciones=[],col=6,fil=1):
        self.titulo=titulo
        self.opciones=opciones
        self.col=col
        self.fil=fil
        
    def menu(self):
        gotoxy(self.col,self.fil);print(self.titulo)
        self.col-=5
        for opcion in self.opciones:
            self.fil +=1
            gotoxy(self.col,self.fil);print(opcion)
        gotoxy(self.col+5,self.fil+2)
        opc = input(f"Elija opcion[1...{len(self.opciones)}]: ") 
        return opc   

class Valida:
    #valida solo numeros normales
    def solo_numeros(self,mensajeError,col,fil):
        while True: 
            gotoxy(col,fil)            
            valor = input()
            try:
                if int(valor) > 0:
                    break
            except:
                gotoxy(col,fil);print(mensajeError)
                time.sleep(1)
                gotoxy(col,fil);print(" "*40)
        return valor
    
    def validar_numero_dni(self, mensajeError, col, fil):
        while True: 
            gotoxy(col, fil)            
            valor = input()
            try:
                if len(valor) == 10 and valor.isdigit():
                    coeficientes = [2, 1, 2, 1, 2, 1, 2, 1, 2]
                    total = 0
                    for i in range(9):
                        digito = int(valor[i]) * coeficientes[i]
                        if digito > 9:
                            digito -= 9
                        total += digito
                    verificador_esperado = (10 - (total % 10)) % 10
                    if verificador_esperado == int(valor[9]):
                        break  
                    else:
                        raise ValueError(mensajeError)
                else:
                    raise ValueError(mensajeError)
            except ValueError as e:
                gotoxy(col, fil)
                print(mensajeError)
                time.sleep(1)
                gotoxy(col, fil)
                print(" " * 30)
        return valor

    
    def validar_numero_dni_consulta(self,dni):
        if len(dni) == 10:
            return True
        return False

    def solo_letras(self,mensaje,mensajeError): 
        while True:
            valor = str(input("          ------>   | {} ".format(mensaje)))
            if valor.isalpha():
                break
            else:
                print("          ------><  | {} ".format(mensajeError))
        return valor
    #Valida tanto cantidad de caracteres como si ingresas numeros
    def validar_nombre_cliente(self, col, fil): 
        while True:
            gotoxy(col,fil) 
            valor = str(input())
            valor=valor.replace(' ','')
            if len(valor)>=30:
                gotoxy(col, fil); print('Maximo 30 caracteres')
                time.sleep(1)
                gotoxy(col, fil); print(" " * (100))
            elif valor.isalpha():
                break
            elif not valor.isalpha():
                gotoxy(col, fil); print('Debes ingresar letras')
                time.sleep(1)
                gotoxy(col, fil); print(" " * (40)) # Si falla, continúa con el ciclo
        return valor
    
    
    
    
    def validar_registro(self,lista_jon,json_ingresado):
        for json in lista_jon:
            if json['dni'] == json_ingresado['dni']:
                return True
        return False
    
    def solo_decimales(self,mensaje,mensajeError):
        while True:
            valor = str(input("          ------>   | {} ".format(mensaje)))
            try:
                valor = float(valor)
                if valor > float(0):
                    break
            except:
                print("          ------><  | {} ".format(mensajeError))
        return valor
    
    def solo_decimales_nuevo(self,mensajeError,col,fil):
        while True:
            gotoxy(col,fil) 
            valor = str(input())
            try:
                valor = float(valor)
                if valor > float(0):
                    break
            except:
                gotoxy(col, fil); print(mensajeError)
                time.sleep(1)
                gotoxy(col, fil); print(" " * (40))
        return valor
    
    def solo_decimales_cliente(self,col,fil):
        while True:
            gotoxy(col,fil) 
            valor = str(input())
            try:
                valor = float(valor)
                if valor > float(0):
                    break
            except:
                gotoxy(col,fil);print('Debes ingresar decimales')
                time.sleep(1)
                gotoxy(col,fil);print(" "*40)
        return valor
    def cedula():
        pass
    
class otra:
    pass    

if __name__ == '__main__':
    # instanciar el menu
    opciones_menu = ["1. Entero", "2. Letra", "3. Decimal"]
    menu = Menu(titulo="-- Mi Menú --", opciones=opciones_menu, col=10, fil=5)
    # llamada al menu
    opcion_elegida = menu.menu()
    print("Opción escogida:", opcion_elegida)
    valida = Valida()
    if(opciones_menu==1):
      numero_validado = valida.solo_numeros("Mensaje de error", 10, 10)
      print("Número validado:", numero_validado)
    
    numero_validado = valida.solo_numeros("Mensaje de error", 10, 10)
    print("Número validado:", numero_validado)
    
    letra_validada = valida.solo_letras("Ingrese una letra:", "Mensaje de error")
    print("Letra validada:", letra_validada)
    
    decimal_validado = valida.solo_decimales("Ingrese un decimal:", "Mensaje de error")
    print("Decimal validado:", decimal_validado)