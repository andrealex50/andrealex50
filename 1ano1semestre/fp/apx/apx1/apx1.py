#Variáveis a pedir
year = int(input('Ano? '))
month = int(input('Mês? '))
day = int(input('Dia? '))


#Função que verifica se o ano é bissexto
def isLeapYear(year):
    if ((year % 400 == 0) or (year % 100 != 0) and (year % 4 == 0)):
      return True
    else:
      return False


#Função que calcula o número de dias do mês introduzido 
def monthDays(year, month):
   if month in (1, 3, 5, 7, 8, 10, 12):   #meses com 31 dias
      diasdomes = 31
   elif month == 2:   #mês de fevereiro que tem duas possibilidades
      if  isLeapYear(year):
         diasdomes = 29   #para ano bissexto
      else:
         diasdomes = 28   #para ano não bissexto
   else:
      diasdomes = 30   #restantes meses que têm 30 dias
   return diasdomes


#Função que determina o dia seguinte ao dia introduzido
def nextDay(year, month, day):
   if day < monthDays(year, month):   #acrescentar 1 dia já sabendo se é bissexto ou não através da função anterior
      day += 1
   else:
      day = 1   #casos em que o dia seguinte é dia 1
      if month == 12:   #se o mês for dezembro o dia seguinte passa a ser no ano seguinte em janeiro
         month = 1
         year += 1
      else:
         month +=1   #restantes casos sem ser o mês de dezembro
   return year, month, day


#Função que determina se a função é válida ou inválida
def dateIsValid(year, month, day):
   if year <= 0:
      print('ERRO')
      return False
   if month <= 0 and month > 12:
      print('ERRO')
      return False
   if day <= 0:
      print('ERRO')
      return False
   if month in (1, 3, 5, 7, 8, 10, 12) and day > 31:   #meses com 31 dias, que são inválidos se o dia for superior a 31
      print('ERRO')
      return False
   elif month in (4, 6, 9, 11) and day > 30:   #meses com 30 dias, que são inválidos se o dia for superior a 30
      print('ERRO')
      return False
   if month == 2:   #fevereiro dividido em duas possibilidades
      if isLeapYear(year):   #se for bissexto
         if day > 29:
            print('ERRO')
            return False
         else:  
            return True
      elif day > 28:   #se não for bissexto
         print('ERRO')
         return False
      else:
         return True
   else:   #o resto das datas são válidas 
      return True
      

#Função que determina o dia anterior ao dia introduzido
def previousDay(year, month, day):
   if day == 1:
      if month in (5, 7, 10, 12):   #se o mês tiver 31 dias e o dia introduzido for 1, o mês anterior vai ter 30 dias
         month -= 1
         day = 30
      elif month in (2, 4, 6, 9, 11 ):   #se o mês tiver 30 dias e o dia introduzido for 1, o mês anterior vai ter 31 dias
         month -= 1
         day = 31
      elif month == 3:   #se o mês for março, o mês anterior vai ser fevereiro
         if isLeapYear(year):   #o mês anterior tem 29 dias for bissexto
            month -= 1
            day = 29
         else:   #o mês anterior tem 28 dias se for não bissexto
            month -= 1
            day = 28
      elif month == 1:   #se o mês for janeiro, o mês passa a ser do ano passado
         month = 12
         day = 31
         year -= 1
      elif month == 8:   #se o mês for outubro, o mês passado tem o mesmo número de dias
         month -= 1
         day = 31
   else:   #se o dia introduzido não for 1
      day -= 1 
   return year, month, day







