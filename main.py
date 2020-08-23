
def solve(cadena,step):
    CADENA_FINAL= []
    
    #recorrer la cadena caracter por caracter
    for letra in cadena:
        
        if(letra.isalpha() == False):
            CADENA_FINAL.append(letra)

        #se recorre un contador desde el 65 a 91 que corresponde a los codigos ascci de las mayusculas
        for index in range (65 , 91):
            #se realiza la comparación de la letra con el rango para ver si pertenece
            if letra == chr(index):
                # se valida que la letra con los pasos al aumentar es mayor al rango
                if index + step > 90:
                    #se resetea a la primera letra conservando los pasos
                    reset = ((index + step) - 91) + 65
                    CADENA_FINAL.append(chr(reset))
                    #print(chr(reset))
                else:
                    #si no es mayor que el rango lo imprime
                    CADENA_FINAL.append(chr(index+step))
                    #print(chr(index+step))
                    
        #Mismas condiciones anteriores !
        for index2 in range (97,123) :
            if letra == chr(index2):
                if index2 + step > 122:
                    reset = ((index2 + step) - 123) + 97
                    CADENA_FINAL.append(chr(reset))
                    #print(chr(reset))
                else:
                    CADENA_FINAL.append(chr(index2+step))
                    #print(chr(index2+step))
            # else:
            #     CADENA_FINAL.append(letra)
    separator = ''
    print("Tu mensaje secreto es :")
    print(separator.join(CADENA_FINAL))

def main():
    print("ingrese mensaje : ")
    cadena = input()
    print("Ingrese parametro clave (INT) : ")
    step = input()
    solve(cadena,int(step))

main()