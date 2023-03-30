import os
import conexion_SFTP

    
def cambiar_tail(carpeta):
    """
    Remplaza el codigo asignado "000007" en el HK5266 ya que la unidad del avion
    esta fallando y no permite cambiarlo.
    """
    with open(carpeta, mode='w') as f:
      f.write("HK5266")
      f.close()
      return


def extraer_archivos(carpeta):
    """
    Lee raiz, directorios y archivos de una ruta.
    """
    contenido = list(os.walk(carpeta))
    primer_posicion = contenido[0]                               
    root, directorios, files = primer_posicion
    return root, directorios, files


from datetime import date

def current_date():
 

    fecha_hoy = date.today()
    fecha_tuple = fecha_hoy.timetuple()
    
    current_año = str(fecha_tuple[0])
    current_mes = fecha_tuple[1]
    
   
    mes = {1 : '1. ENERO',
           2 : '2. FEBRERO',
           3 : '3. MARZO',
           4 : '4. ABRIL',
           5 : '5. MAYO',
           6 : '6. JUNIO',
           7 : '7. JULIO',
           8 : '8. AGOSTO',
           9 : '9. SEPTIEMBRE',
           10 : '10. OCTUBRE',
           11 : '11. NOVIEMBRE',
           12 : '12. DICIEMBRE'
           }
        
    current_mes = mes.get(current_mes)

    return current_año, current_mes




def tail(carpeta):
  
    #path = "G:/Mi unidad/01. HK-5199/2023/02 FEB/HK5199_19_FEB_2023"
    #path = "G:/Mi unidad/20. HK-5404/2023/2. FEBRERO/HK5404_22_FEB_2023"
        
    with open(carpeta, mode='r') as f:
        tail_archivo  = f.readline(6)
    
    
    
    AC_Matriculas = {'000005':'HK5199_',
                     'HK5199':'HK5199_',
                     '649   ':'HK5199_',
                     '00649 ':'HK5199_',
                     'HK5266':'HK5266_',
                     'HK5282':'HK5282_',
                     '000001':'HK5310_',
                     'HK5313':'HK5313_',
                     'HK5314':'HK5314_',
                     'HK5315':'HK5315_',
                     'HK5321':'HK5321_',
                     'HK5331':'HK5331_',
                     'HK5341':'HK5341_',
                     '000007':'HK5349_',
                     'HK5351':'HK5351_',
                     'HK5391':'HK5391_',
                     'HK5354':'HK5354_',
                     'HK5322':'HK5322_',
                     'HK5292':'HK5292_',
                     'HK5293':'HK5293_',
                     'HK5294':'HK5294_',
                     'HK5347':'HK5347_',
                     'V2-LIN':'HK5404_'                
                  }
    
    
    
    tail_descarga = AC_Matriculas.get(tail_archivo)
    return tail_descarga


def fecha_archivo():
    
    with open(carpeta, mode= "r") as f:
        lineas = f.readlines()
        cant_lineas = len(lineas) - 1
        ult_linea = lineas[cant_lineas]
        
        fecha = list(ult_linea[8:14])  
        
        dia = fecha[4] + fecha[5]
        mes = fecha[2] + fecha[3]
        año = fecha[0] + fecha[1]
    
    
    fecha_archivo = (f"{dia}_{mes}_{año}")
                                    
    return fecha_archivo

#######################   inicio    ##########                                    
"""    
Remplaza el codigo asignado "000007" en el HK5266 ya que la unidad del avion
esta fallando y no permite cambiarlo.
"""
carpeta = "G:\Mi unidad/02. HK-5266/2023"

folder_mes = extraer_archivos(carpeta)

for folder in folder_mes[1]:
    carpeta = os.path.join(folder_mes[0], folder)
    descarga = extraer_archivos(carpeta)
    for dia_descarga in descarga[1]:
        carpeta = os.path.join(descarga[0], dia_descarga)
        archivos_descarga = extraer_archivos(carpeta)
        for file in archivos_descarga:
                carpeta = os.path.join(archivos_descarga[0] , 'ACTAIL.TXT')
                if carpeta.endswith('ACTAIL.TXT'):
                    cambiar_tail(carpeta)
                    break
                break
#######################   fin      ###########                                      
import shutil

ruta_HK = []
ruta_año = []
ruta_mes = []
ruta_descarga = []
lista_año = []
lista_mes = []
lista_descarga = []
#lista_folder = []
lista_file = []
lista_terminados = []

        

hoy = current_date()

ruta = "G:/Mi unidad"
mi_unidad = os.listdir(ruta)


for matricula in mi_unidad:
    carpeta = os.path.join(ruta,matricula)
    carpeta = carpeta.replace("//","/")
    if os.path.isdir(carpeta):
        ruta_HK.append(carpeta)
        ruta_año.clear()
        lista_año = os.listdir(carpeta)
        
        for año in lista_año:
            if año == hoy[0]:
                carpeta = (os.path.join(os.path.join(ruta,matricula),año))
                carpeta  = carpeta.replace("//","/")
                if os.path.isdir(carpeta):
                    ruta_año.append(carpeta)
                    ruta_mes.clear()
                    lista_mes = os.listdir(carpeta)
                        
                                
                    for mes in lista_mes:
                        if mes == hoy[1]:
                            carpeta = os.path.join((os.path.join(os.path.join(ruta,matricula),año)),mes)
                            carpeta  = carpeta.replace("//","/")
                            if os.path.isdir(carpeta):  
                                ruta_mes.append(carpeta)
                                ruta_descarga.clear()
                                lista_terminados.clear()
                                lista_descarga = os.listdir(carpeta)
                                
                                for descarga in lista_descarga:
                                        carpeta = os.path.join((os.path.join((os.path.join(os.path.join(ruta,matricula),año)),mes)),descarga) 
                                        carpeta = carpeta.replace("//","/")
                                        if os.path.isdir(carpeta):
                                            lista_folder = extraer_archivos(carpeta)
        
                                        
                                            for archivo in lista_folder[2]:
                                                if archivo.endswith("ACTAIL.TXT"):
                                                    carpeta = os.path.join((os.path.join((os.path.join((os.path.join(os.path.join(ruta,matricula),año)),mes)),descarga)),archivo)
                                                    carpeta = carpeta.replace("//","/")
                                                    tail_descarga = tail(carpeta)
            
                                                    break
                                                else:
                                                    tail_descarga = "HK0000_"
                                                    continue
                                                
                                            for direc in lista_folder[1]:
                                                if direc.endswith(".ECT"):
                                                    carpeta = os.path.join((os.path.join((os.path.join((os.path.join(os.path.join(ruta,matricula),año)),mes)),descarga)),direc)
                                                    files = os.listdir(carpeta)
        
            
                                                    for file in files:
                                                        carpeta = os.path.join((os.path.join((os.path.join((os.path.join((os.path.join(os.path.join(ruta,matricula),año)),mes)),descarga)),direc)), file)
                                                        if carpeta.endswith(".DAT"):
                                                            fecha_descarga = fecha_archivo()
                                                                                                                       
                                                            nuevo_nombre =  tail_descarga + fecha_descarga
                                                            nueva_ruta = os.path.join(os.path.join((os.path.join(os.path.join(ruta,matricula),año)),mes), nuevo_nombre)
                                                            antigua_ruta = os.path.join((os.path.join((os.path.join(os.path.join(ruta,matricula),año)),mes)),descarga)
                                                            if os.path.exists(nueva_ruta): # si el archivo descargado existe
                                                                if os.path.exists(nueva_ruta + ".zip"): # si el archivo está comprimido
                                                                    break # si está comprimido sale
#                                                                os.renames(antigua_ruta,nueva_ruta)
                                                                shutil.make_archive(nueva_ruta,"zip",nueva_ruta) #si está, lo comprime
                                                                file_zip =nueva_ruta+".zip"
                                                                transmitir = conexion_SFTP.conexion_sftp(file_zip)
                                                                lista_terminados.append(tail_descarga + fecha_descarga)
                                                                break
                                                                
                                                            else:
                                                                os.renames(antigua_ruta,nueva_ruta) # comprimir y enviar sftp
                                                                shutil.make_archive(nueva_ruta,"zip",nueva_ruta)
                                                                file_zip =nueva_ruta+".zip"
                                                                transmitir = conexion_SFTP.conexion_sftp(file_zip)
                                                                lista_terminados.append(tail_descarga + fecha_descarga)
                                                                break
                                                        break         
                                                else:        
                                                    continue
         
                                        else:
                                            continue
                            else:
                                continue
                        else:
                            continue
                else:
                    continue
            else:
                continue
    else:
        continue 