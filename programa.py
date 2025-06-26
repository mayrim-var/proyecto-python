cadena=[]
fecha=[]
hora=[]
temperatura=[]
humedad=[]
presion=[]
def extraer (nombre_archivo, len_header):
 line_count=0
 with open (nombre_archivo, 'r')as pfile:
  for linea in pfile:
   line_count+= 1
   if line_count<=len_header:
     continue
   if not linea:
     continue
 valores=linea.strip(",")
 if not linea:
  if len(valores) <4:
    print("Advertencia:linea con formato inesperado")
numeros=[]
for valor in valores [1:]:
    numeros.append (float(valor))
temperatura.append(numeros=[0])
humedad.append(numeros=[1])
presion.append(numeros=[2])
dia=[]
dia=valores[0].split("_")
fecha.append(valores[0].split("_")[0])
fecha.append(dia[0])
hora.append(dia[1])
