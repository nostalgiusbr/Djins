#Criar um relógio!
import time

hora = 0
minuto = 0
segundo = 0

 
while hora <= 25:

    if hora < 10 and minuto < 10 and segundo >= 10:
        print (f'Hora Atual = 0{hora}:0{minuto}:{segundo}')
        segundo += 1

    elif hora < 10 and minuto < 10 and segundo < 10 :    
        print (f'Hora Atual = 0{hora}:0{minuto}:0{segundo}')
        segundo += 1

    elif hora >= 10 and minuto < 10 and segundo < 10:  
        print (f'Hora Atual = {hora}:0{minuto}:0{segundo}')
        segundo += 1

    elif hora >= 10 and minuto >= 10 and segundo < 10:
        print (f'Hora Atual = {hora}:{minuto}:0{segundo}')
        segundo += 1

    elif hora < 10 and minuto >= 10 and segundo < 10:
        print (f'Hora Atual = 0{hora}:{minuto}:0{segundo}')
        segundo += 1

    elif hora < 10 and minuto >= 10 and segundo >= 10:
        print (f'Hora Atual = 0{hora}:{minuto}:{segundo}')
        segundo += 1           
    
    if segundo == 60:
        segundo = 0
        minuto += 1

    if minuto == 60:
        minuto = 0
        hora += 1

    if hora == 24:
        segundo = 0
        minuto = 0
        hora = 0  
    time.sleep(1)  
       
    
 
          