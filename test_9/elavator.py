"""
Ejercicio:


"""
pisos=[]
ruta_pisos=[1,4,5]
mapa_pisos={}
c = False
for p in range(0,5):
    p=p+1
    pisos.append(p)


piso_init=int(input("inserte piso inicial: "))

def ascenso(piso_init,ruta_pisos):
    ascenso = []
    for p in ruta_pisos:
        if p > piso_init:
            ascenso.append(p)
    return ascenso

def descenso(piso_init,ruta_pisos):
    descenso = []
    for p in ruta_pisos:
        if p < piso_init:
            descenso.append(p)
    return descenso

up=ascenso(piso_init,ruta_pisos)
down = descenso(piso_init,ruta_pisos)
print(up)
print(down)

s=""
nuevo_piso=""
nueva_ruta=[]
cursor=""
while nuevo_piso != "c":
    if len(up) >= len(down):
        up.sort
        down.sort
        ruta= up+down
        print(ruta)
        s= "Subiendo"
        ip= pisos[piso_init:max(up)+1]
        x=0
        for pa in ip:
            print("Elevador en piso", pa)
            print("Elevador subiendo")
            for i in up:
                if pa == i:
                    ruta.remove(i)
                    print("Elevador se detiene")
                    print(ruta)
                    x=i
            nuevo_piso=input()
            if nuevo_piso !=0:
                print("Piso ingresado: ", nuevo_piso)
                mapa_pisos[nuevo_piso]=pa
            else: nuevo_piso=""
        ruta.reverse()
        for p in range(min(down),x):
            act=x-p
            print("Elevador en piso", act)
            if act == 1:
                print("Elevador en el Lobby")
            else:
                print("Elevador Bajando")
            for i in down:
                if act == i:
                    ruta.remove(i)
                    print("Elevador se detiene")
                    print(ruta)
            nuevo_piso=input()
            if nuevo_piso != 0:
                print("Piso ingresado: ", nuevo_piso)
                mapa_pisos[nuevo_piso]=act
            else: nuevo_piso= ""
        cursor=act

print(mapa_pisos)       











