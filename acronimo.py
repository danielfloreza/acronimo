def show(acronimo):
    print("Tu acronimo es "+str(acronimo)+".\n")
    start()


def check(name):
    acronimo=[]
    acronimo.append(name[0])
    for i in range(len(name)):
        if name[i] == " ":
            if name[i+1] != " ":
                acronimo.append(name[i+1])
    acronimo="".join(acronimo)
    acronimo= acronimo.upper()
    
    show(acronimo)


def play():
    name = input("Escribe tu nombre completo:\n")
    name= name.strip()
    name_proof=name.replace(" ","")
    
    if name_proof.isalpha():
        print("\n")
        check(name)
    else:
        print("\nTu nombre no puede llevar un número, ni comas ni punto.\nVuelve a intertarlo.\n")
        play()

def start():
    answer=input("""¿Quieres continuar para saber el acronimo tu nombre?

1- Sí
2- No

""")
    
    answer=answer.strip()
    if answer.isdigit():
        if int(answer) == 1:
            play()
        elif int(answer) == 2:
            print("Hasta la próxima!\n")
        else:
            print("Escribe una opcion valida.\n")
            start()
    else:
        print("Escribe una opcion valida.\n")
        start()


def run():
    print("Bienvenido al creador de acronimos.\n")
    start()


if __name__ == '__main__':
    run()