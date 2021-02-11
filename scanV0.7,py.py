#scaner de paginas
# wolf hound team

import sys
import socket
import os
import time
#from IPy import IP

os.system("title Scan_Port_V0.7")
os.system(" COLOR A")
'''
pagina para pruebas :
www.thestudentcave.freecluster.eu <-- con esta ya no
testphp.vulnweb.com
'''
print("\t╔════════════════════════════════════════╗")
print("\t║           + Wolf Hound Team +          ║")
print("\t║Departamento de ciberseguridad          ║")
print("\t║Scaner de puertos para paginas webs v0.7║")
print("\t╚════════════════════════════════════════╝")


def actividad(s):
    return s.recv(1024)

def main():
    print("\n+++++ Introduce la pagina web ++++++")
    objetivo=input(">>>")
    print("Introduce el puerto inicial ")
    inicio=input(">>>")
    print("Introduce el puerto final ")
    final=input(">>>")
    print("velocidad de analisis mientras mas alto el tiempo mas preciso es (0.0 ~ 1.0)")
    velocidad=(input(">>"))
    if (inicio=='' or inicio==" " or int(inicio)<0):
        print(" El puerto inicial no ha sido configurado , \n cambiado por defecto a 0")
        inicio=0
    if (velocidad==None or velocidad=='' or velocidad==' ' or  float(velocidad)<0.00001):
        print("La velocidad de analisis no permite el funcionamiento correcto \n se ha cambiado a la velocidad por defecto 0.5")
        velocidad=0.5
    if(int(inicio)>int(final) or inicio==None or final==None or int(final)>65535):
        print(" los datos introducidos no permiten el correcto \n funcionamiento del programa , recuerda que \n el puerto inicial no puede ser mayor\n al final y que el puerto final no \n puede ser mayor a 65535 .")
        print("\n Re-iniciando el programa.........")
    lista=[]
    proceso=[]
    si=0
    no=0
    ip=socket.gethostbyname(objetivo)
    print("La ip de la pagina es :",ip)
    
#calculo de avance mediante porcentaje -------------
    for port in range(int(inicio),int(final)):
        try:
            sock=socket.socket()
            sock.settimeout(float(velocidad))
            sock.connect((ip,port))
            #print("[+] puerto "+str(port)+"<-------- esta abierto ")
            try :
                puente=actividad(sock)
                proceso.append(puente.decode())
                #print("[+++]el puerto :"+str(port)+" esta abierto con la actividad :"+str(puente.decode()))
            except:
                proceso.append("no se sabe")
                #print("[+]el puerto :"+str(port)+" esta abierto pero se desconoce la actividad")
            lista.append(port)
            si+=1
        except:
            #print("[-] puerto "+str(port)+" esta cerrado")
            no+=1

        os.system("cls")
        print("\n \n")
        print("\t\t\t PORCENTAJE DE ANALISIS ")
        print("\t\t╔══════════════════════════════════════════════════╗")
        avance=((port-int(inicio))/(int(final)-int(inicio)))*100
        porcentaje="%.1f"%avance
        print("\t\t","█"*int((avance/2)),"-",str(porcentaje)+"%")
        print("\t\t╚══════════════════════════════════════════════════╝")
        print("\n\n\t\t<*manten esta ventana abierta mientras el programa funcione*>")

    time.sleep(2)
    os.system("cls")
   
    print("╔══════════════════════════════════════════════════════╗")
    print("║                RESULTADO DEL ANALISIS                ║")
    print("║ ")
    print("║ Nombre de la pagina a analizar :\n║ --"+str(objetivo),"--")
    print("║ Ip de la pagina analizada :",str(ip))
    print("║ -----------Resultado del escaneo ---------")
    print("║ Puertos totales analizados :",int(final)-int(inicio))
    print("║ Puerto Inicial :"+str(inicio))
    print("║ Puerto Final:"+str(final))
    
    
    print("║ Puertos Cerrados:"+str(no))
    if(si>0):
        print("║ Puertos Abiertos:"+str(si))
        print("║ <<<<numeros de los puertos abiertos >>>>>")
        conteo=0
        while conteo!=si:
            print("║Puerto n°:",lista[conteo]," Abierto , proceso:",proceso[conteo])
            conteo+=1
    else:
        print("║ **** No hay puertos abiertos ****")
    print("╚══════════════════════════════════════════════════════╝")
    print("-------------------fin del analisis--------------------")
    print("pesiona ENTER para cerrar el programa o selecciona 'Y' para reiniciarlo")
    salir=input(">>>")
    if salir.upper()=="Y":
        main()
    
    sys.exit(0)

main()
