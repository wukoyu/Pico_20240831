#! usr/bin/micropython

'''
led->gpio15
光敏電阻 -> gpio28
可變電阻 -> gpio26
內建溫度sensor -> adc最後1pin,共5pin
'''

from machine import Timer,ADC,Pin,PWM,RTC
import binascii
from umqtt.simple import MQTTClient
import tools


def do_thing(t):
    '''
    :param t:Timer的實體
    負責偵測溫度和光線
    每2秒執行1次
    '''
    conversion_factor = 3.3 / (65535)
    reading = adc.read_u16() * conversion_factor
    temperature = round(27 - (reading - 0.706)/0.001721,2)  #round是內建函式；取整數，round(number, None)
    print(f'溫度:{temperature}')  
    mqtt.publish('SA-08/TEMP', f'{temperature}')
    adc_value = adc_light.read_u16()
    print(f'光線:{adc_value}')
    mqtt.publish('SA-08/LIGHT_LEVEL', f'{adc_value}')
    
    
def do_thing1(t):
    '''
    :param t:Timer的實體
    負責可變電阻和改變led的亮度
    '''    
    
    duty = adc1.read_u16()
    pwm.duty_u16(duty)
    light_level = round(duty/65535*10)
    print(f'可變電阻:{light_level}')
    mqtt.publish('SA-08/LED_LEVEL', f'{light_level}')

def main():
    pass
       

if __name__ == '__main__':
    # 全域變數設定
    adc = ADC(4) #內建溫度
    adc1 = ADC(Pin(26)) #可變電阻
    adc_light = ADC(Pin(28)) #光敏電阻
    pwm = PWM(Pin(15),freq=50) #pwm led
    #連線internet
    try:
        tools.connect()
    except RuntimeError as e:
        print(e)
    except Exception:
        print('不知明的錯誤')
    else:
        #連線MQTT Broker
        SERVER = "192.168.0.252"
        CLIENT_ID = binascii.hexlify(machine.unique_id())
        mqtt = MQTTClient(CLIENT_ID, SERVER,user='pi',password='raspberry')
        mqtt.connect() #此行應該在連上網路後再執行
        t1 = Timer(period=2000, mode=Timer.PERIODIC, callback=do_thing)
        t2 = Timer(period=500, mode=Timer.PERIODIC, callback=do_thing1)
    #main()
    
    
    