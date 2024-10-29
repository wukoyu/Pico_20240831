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
import tools,config


def do_thing(t):
    '''
    :param t:Timer的實體
    負責偵測溫度和光線
    每2秒執行1次
    '''
    conversion_factor = 3.3 / (65535)
    reading = adc.read_u16() * conversion_factor
    temperature = round(27 - (reading - 0.706)/0.001721,2) 
    print(f'溫度:{temperature}')
    mqtt.publish('SA-08/TEMPERATURE', f'{temperature}')
    blynk_mqtt.publish('ds/temperature',f'{temperature}')
    adc_value = adc_light.read_u16()
    print(f'光線:{adc_value}')
    line_state = 0 if adc_value < 3500 else 1
    print(f'光線:{line_state}')
    mqtt.publish('SA-08/LINE_LEVEL', f'{line_state}')
    blynk_mqtt.publish('ds/line_status',f'{line_state}')
    
    
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
    blynk_mqtt.publish('ds/led_level',f'{light_level}')
    

def main():
    global blynk_mqtt
    print(config.BLYNK_MQTT_BROKER)
    print(config.BLYNK_TEMPLATE_ID)
    print(config.BLYNK_AUTH_TOKEN)
    blynk_mqtt = MQTTClient(config.BLYNK_TEMPLATE_ID, config.BLYNK_MQTT_BROKER,user='device',password=config.BLYNK_AUTH_TOKEN,keepalive=60)
    blynk_mqtt.connect()
    
        

if __name__ == '__main__':
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
        #MQTT
        SERVER = "192.168.2.23"
        CLIENT_ID = binascii.hexlify(machine.unique_id())
        mqtt = MQTTClient(CLIENT_ID, SERVER,user='pi',password='raspberry')
        mqtt.connect()
        t1 = Timer(period=2000, mode=Timer.PERIODIC, callback=do_thing)
        t2 = Timer(period=500, mode=Timer.PERIODIC, callback=do_thing1)
    blynk_mqtt = None    
    main()