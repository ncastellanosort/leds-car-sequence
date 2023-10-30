from machine import Pin
from utime import sleep, sleep_ms
import uasyncio as asyncio

puertos = [12, 14, 27, 26, 25, 33, 32] 
leds = []

for npuer in puertos:
  leds.append(Pin(npuer, Pin.OUT))

#matriz para secuencia 5
matriz = [
    [1,0,0,0,0,0,0],
    [1,1,0,0,0,0,0],
    [1,0,1,0,0,0,0],
    [1,1,0,1,0,0,0],
    [1,0,1,0,1,0,0],
    [1,1,0,1,0,1,0],
    [1,0,1,0,1,0,1],
    
    [0,1,0,1,0,1,0],
    [1,0,1,0,1,0,1],
    [0,1,0,1,0,1,0],
    [1,0,1,0,1,0,1],
    [0,1,0,1,0,1,0],
    [1,0,1,0,1,0,1],
    [0,1,0,1,0,1,0],
    [1,0,1,0,1,0,1],
    [0,1,0,1,0,1,0],

    [1,0,1,0,1,0,1],
    [0,1,0,1,0,1,1],
    [0,0,1,0,1,0,1],
    [0,0,0,1,0,1,1],
    [0,0,0,0,1,0,1],
    [0,0,0,0,0,1,1],
    [0,0,0,0,0,0,1],
    [0,0,0,0,0,0,0],
    
    [0,0,0,0,0,0,1],
    [0,0,0,0,0,1,1],
    [0,0,0,0,1,0,1],
    [0,0,0,1,0,1,1],
    [0,0,1,0,1,0,1],
    [0,1,0,1,0,1,1],
    
    [1,0,1,0,1,0,1],
    [0,1,0,1,0,1,0],
    [1,0,1,0,1,0,1],
    [0,1,0,1,0,1,0],
    [1,0,1,0,1,0,1],
    [0,1,0,1,0,1,0],
    [1,0,1,0,1,0,1],
    [0,1,0,1,0,1,0],

    [1,0,1,0,1,0,1],
    [1,1,0,1,0,1,0],
    [1,0,1,0,1,0,0],
    [1,1,0,1,0,0,0],
    [1,0,1,0,0,0,0],
    [1,1,0,0,0,0,0],
    [1,0,0,0,0,0,0],
    [0,0,0,0,0,0,0],   
    
    [1,0,0,0,0,0,0],
    [1,1,0,0,0,0,0],
    [1,0,1,0,0,0,0],
    [1,1,0,1,0,0,0],
    [1,0,1,0,1,0,0],
    [1,1,0,1,0,1,0],
    [1,0,1,0,1,0,1],
    
    [0,1,0,1,0,1,0],
    [1,0,1,0,1,0,1],
    [0,1,0,1,0,1,0],
    [1,0,1,0,1,0,1],
    [0,1,0,1,0,1,0],
    [1,0,1,0,1,0,1],
    [0,1,0,1,0,1,0],
    [1,0,1,0,1,0,1],
    [0,1,0,1,0,1,0],

    [1,0,1,0,1,0,1],
    [0,1,0,1,0,1,1],
    [0,0,1,0,1,0,1],
    [0,0,0,1,0,1,1],
    [0,0,0,0,1,0,1],
    [0,0,0,0,0,1,1],
    [0,0,0,0,0,0,1],
    [0,0,0,0,0,0,0],
    
    [0,0,0,0,0,0,1],
    [0,0,0,0,0,1,1],
    [0,0,0,0,1,0,1],
    [0,0,0,1,0,1,1],
    [0,0,1,0,1,0,1],
    [0,1,0,1,0,1,1],
    
    [1,0,1,0,1,0,1],
    [0,1,0,1,0,1,0],
    [1,0,1,0,1,0,1],
    [0,1,0,1,0,1,0],
    [1,0,1,0,1,0,1],
    [0,1,0,1,0,1,0],
    [1,0,1,0,1,0,1],
    [0,1,0,1,0,1,0],

    [1,0,1,0,1,0,1],
    [1,1,0,1,0,1,0],
    [1,0,1,0,1,0,0],
    [1,1,0,1,0,0,0],
    [1,0,1,0,0,0,0],
    [1,1,0,0,0,0,0],
    [1,0,0,0,0,0,0],
    [0,0,0,0,0,0,0],
    
]

# ledsPwm = []

# for npuer in puertos:
#     pwm = PWM(Pin(npuer), freq=1000, duty=0)
#     ledsPwm.append(pwm)


# def brillo(brill):
#     for pwm in ledsPwm:
#         pwm.duty(int(brill)) 


#-------------------------------------------   
#apagar todos los leds
def apagados():
  for led in leds:
    led.off()
  sleep(0.1)
#-------------------------------------------
#------------------------------------------- 
#para primera y segunda secuencia  
def ledValue(sleepValor):
  for led in leds:
    led.value(1)
    sleep_ms(sleepValor) #tiempo entre que prende y apaga
    led.value(not led.value())
#------------------------------------------- 
def ledValueReversed(sleepValor):
  for led in reversed(leds):
    led.value(1)
    sleep_ms(sleepValor)
    led.value(not led.value())
#-------------------------------------------    
#primera secuencia funciones
def derecha1():
  ledValue(100) #los prende
  apagados() #los apaga todos
#------------------------------------------- 
def izquierda1():
  ledValueReversed(100)
  apagados()
#-------------------------------------------
#-------------------------------------------
#segunda secuencia funciones
def derecha2():
  ledValue(60)
  apagados()
#-------------------------------------------
def izquierda2():
  ledValueReversed(60)
  apagados()
#-------------------------------------------
#-------------------------------------------
#funciones cuarta secuencia
def izq4F(sleep1, sleep2, sleep3):
  def izquierda4P():
    for led in leds[4:]:
      led.value(1)  
    sleep(sleep1)
      
  def izquierda4A():
    for led in leds[4:]:
      led.value(not led.value())
    sleep(sleep2)
  
  cont = 0
  while cont < 2:
    izquierda4P()
    izquierda4A()
    cont = cont + 1
  sleep(sleep3)
#-------------------------------------------

def der4F(sleep1, sleep2, sleep3):
  def derecha4P():
    for led in leds[:3]:
      led.value(1)
    sleep(sleep1)
    
  def derecha4A():
    for led in leds[:3]:
      led.value(not led.value())
    sleep(sleep2)
      
  cont = 0
  while cont < 2:
    derecha4P()
    derecha4A()
    cont = cont + 1
  sleep(sleep3)
  
#-------------------------------------------
#-------------------------------------------
#-------------------------------------------
#funciones quinta secuencia
def primeras(inicio1,fin1,inicio2,fin2):
  for led in leds[inicio1:fin1]: 
    led.value(1)
    for led in leds[inicio2:fin2]: 
      led.value(1)
  sleep(0.0055)
  apagados()

def segundas(inicio1,fin1,inicio2,fin2):
  for led in leds[inicio1:fin1]: 
    led.value(1)
    for led in leds[inicio2:fin2]:
      led.value(1)
  sleep(0.0055)
  apagados()

def terceras(inicio1,fin1,inicio2,fin2):
  for led in leds[inicio1:fin1]: 
    led.value(1)
    for led in leds[inicio2:fin2]: 
      led.value(1)
  sleep(0.0055)
  apagados()
  
def cuartas(inicio,fin):
  for led in leds[inicio:fin]:
    led.value(1) 
  sleep(0.0055)
  apagados()

def todas():
  for led in leds:
    led.value(1)
  sleep(0.0055)
  apagados()
  
#-------------------------------------------

def primerasRep():
  cont = 0
  while cont < 1:
    primeras(0,1,6,7)
    apagados()
    primeras(0,1,6,7)
    cont = cont + 1
  sleep(0.3)

def segundasRep():
  cont = 0
  while cont < 1:
    segundas(1,2,5,6)
    apagados()
    segundas(1,2,5,6)
    cont = cont + 1
  sleep(0.3)

def tercerasRep():
  cont = 0
  while cont < 1:
    segundas(2,3,4,5)
    apagados()
    segundas(2,3,4,5)
    cont = cont + 1
  sleep(0.3)

def cuartaRep():
  cont = 0
  while cont < 1:
    cuartas(3,4)
    apagados()
    cuartas(3,4)
    cont = cont + 1
  sleep(0.3)

def todasRep():
  cont = 0
  while cont < 1:
    todas()
    apagados()
    todas()
    cont = cont + 1
  sleep(0.3)
#-------------------------------------------
#-------------------------------------------
#funciones sexta secuencia

async def derecha1a():
  for led in reversed(leds[:4]):
    led.value(1)
    sleep(0.01)
    led.value(0)
    await asyncio.sleep(0.1)
  
async def izquierda1a():
  for led in leds[3:]:
    led.value(1)
    sleep(0.01)
    led.value(0)
    await asyncio.sleep(0.1)
    

async def derecha2a():
  for led in leds[:4]:
    led.value(1)
    sleep(0.01)
    led.value(0)
    await asyncio.sleep(0.1)
        
async def izquierda2a():   
  for led in reversed(leds[3:]):
    led.value(1)
    sleep(0.01)
    led.value(0)
    await asyncio.sleep(0.1)
#-------------------------------------------
#funciones septima secuencia
def ledMedioValor(valor):
    for led in leds[3:4]:
        led.value(valor)

def todosLeds(ledValor):
    for led in leds:
        led.value(ledValor)

async def derecha(sleepValor, sleeepAsyncio):
    for led in reversed(leds[:3]):
        led.value(1)
        sleep(sleepValor)
        await asyncio.sleep(sleeepAsyncio)
        
    for led in leds[:3]:
        led.value(0)
        sleep(sleepValor)
        await asyncio.sleep(sleeepAsyncio)
        
async def izquierda(sleepValor, sleeepAsyncio):
    for led in leds[4:]:
        led.value(1)
        sleep(sleepValor)
        await asyncio.sleep(sleeepAsyncio)
        
    for led in reversed(leds[4:]):
        led.value(0)
        sleep(sleepValor)
        await asyncio.sleep(sleeepAsyncio)
        
        
async def derechaAa(asyncioValor, sleepValor):
    for led in leds[:4]:
      led.value(1)
      sleep(sleepValor) #0.001
      await asyncio.sleep(asyncioValor) #0.05
    
    for led in leds[:4]:
      led.value(0)
      sleep(sleepValor)
      await asyncio.sleep(asyncioValor)
      
    for led in reversed(leds[:4]):
      led.value(1)
      sleep(sleepValor)
      await asyncio.sleep(asyncioValor)
        
    for led in reversed(leds[:4]):
      led.value(0)
      sleep(sleepValor)
      await asyncio.sleep(asyncioValor)
        
async def izquierdaAa(asyncioValor, sleepValor):
    for led in reversed(leds[3:]):
      led.value(1)
      sleep(sleepValor)
      await asyncio.sleep(asyncioValor)
      
    for led in reversed(leds[3:]):
      led.value(0)
      sleep(sleepValor)
      await asyncio.sleep(asyncioValor)
      
    for led in leds[3:]:
      led.value(1)
      sleep(sleepValor)
      await asyncio.sleep(asyncioValor)
        
    for led in leds[3:]:
      led.value(0)
      sleep(sleepValor)
      await asyncio.sleep(asyncioValor)
      
def parte1():
    cont = 0
    while cont < 4:
        ledMedioValor(0)
        sleep(0.1)
        ledMedioValor(1)
        loop = asyncio.get_event_loop()
        loop.create_task(derecha(0.001,0.1))
        loop.create_task(izquierda(0.001,0.1))
        loop.run_forever()
        ledMedioValor(0)
        cont = cont + 1

def parte2():
    cont = 0
    while cont < 5:
        loop = asyncio.get_event_loop()
        loop.create_task(derechaAa(0.05, 0.001))
        loop.create_task(izquierdaAa(0.05, 0.001))
        loop.run_forever()
        cont = cont + 1

#-------------------------------------------
#-------------------------------------------  
# primera secuencia
def primera():
  cont = 0
  while cont < 7:
    derecha1()
    izquierda1()
    cont = cont + 1 
#------------------------------------------- 
#segunda secuencia
def segunda():
  cont = 0
  while cont < 6:
    derecha2()
    izquierda2()
    cont = cont + 1
#------------------------------------------- 
#tercera secuencia   
def tercera():  
  for fila in matriz:
    for col, valor in enumerate(fila):
      led_pin = puertos[col]
      pin_obj = Pin(led_pin, Pin.OUT)
      if valor == 1:
        pin_obj.value(1)
      else:
        pin_obj.value(0)
    sleep(0.1) #espera
#------------------------------------------- 
#cuarta secuencia
def cuarta():
  cont = 0
  while cont < 4:
    izq4F(0.055, 0.055, 0.3)
    der4F(0.055, 0.055, 0.3)
    cont = cont + 1
#------------------------------------------- 
#quinta secuencia
def quinta():
  cont = 0
  while cont < 2:
    primerasRep()
    sleep(0.0001)
    segundasRep()
    sleep(0.0001)
    tercerasRep()
    sleep(0.0001)
    cuartaRep()
    sleep(0.0001)
    todasRep()
    sleep(0.0001)
    cont = cont + 1
#------------------------------------------- 
#sexta secuencia
def sexta():
  cont = 0
  while cont < 12:
    loop = asyncio.get_event_loop()
    loop.create_task(derecha1a())
    loop.create_task(izquierda1a())
    loop.run_forever()
    cont = cont + 1
    
  cont = 0
  while cont < 20:
    loop = asyncio.get_event_loop()
    loop.create_task(derecha2a())
    loop.create_task(izquierda2a())
    loop.run_forever()
    cont = cont + 1
#------------------------------------------- 
#septima secuencia
def septima():
  todosLeds(1)
  sleep(5)
  todosLeds(0)
  parte1()
  parte2()
  todosLeds(1)
#------------------------------------------- 
#------------------------------------------- 
#secuencia
while True:
  primera()
  segunda()
  tercera()
  cuarta()
  quinta()
  sexta()
  septima()
  apagados()
  segunda()
  break



  


      
  
  
  
  
  
  
  
  
  
  

  

    





  


