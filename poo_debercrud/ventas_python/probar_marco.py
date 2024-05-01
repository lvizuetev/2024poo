def decorador_division_cero(func):
    # Esta es la función wrapper que envuelve la función original
    def nueva_funcionalidad(*args, **kwargs):
        try:
            return f"Dividir{args}= {func(*args, **kwargs)}"
        except ZeroDivisionError:
            # Si hay una división por cero, devolvemos un mensaje de error
            return "Error: División por cero"
    # Devolvemos la función wrapper
    return nueva_funcionalidad


@decorador_division_cero
def dividir(a, b):
    return a / b
print(dividir(2,2))