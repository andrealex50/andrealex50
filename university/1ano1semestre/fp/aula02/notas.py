ATP1 = float(input('Nota de ATP1? '))
ATP2 = float(input('Nota de ATP2? '))
APx = float(input('Nota de APx? '))
AP1 = float(input('Nota de AP1? '))
AP2 = float(input('Nota de AP2? '))
CTP = (0.15*ATP1 + 0.15*ATP2)/0.30
CP = (0.10*APx + 0.10*AP1 + 0.50*AP2)/0.70
NF = 0.30*CTP + 0.70*CP 
if NF < 10:
   ATPR = float(input('Nota de ATPR? '))
   APR = float(input('Nota de APR? '))
NR = 0.30*max(CTP,ATPR)+0.70*max(CP,APR)
if CTP < 6.5:
   print('codigo 66')
else:
   print('A sua nota final é ', NF)
