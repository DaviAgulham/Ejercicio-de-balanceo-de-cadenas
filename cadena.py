def esta_balanceada(cadena):
    pila = []
    correspondencia = {')': '(', '}': '{', ']': '['}

    for char in cadena:
        if char in correspondencia.values():
            pila.append(char)
        elif char in correspondencia.keys():
            if pila and pila[-1] == correspondencia[char]:
                pila.pop()
            else:
                return False

    return not pila

# Ingresar cadena para ser balanceada
cadena = "{{{{{{ [ ( ) ] }}}}}}"
print(esta_balanceada(cadena))