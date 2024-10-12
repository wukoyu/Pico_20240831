import tools
from machine import Timer,ADC,Pin,PWM,RTC

tools.connect()

adc = ADC(4) #
adc_light = ADC(Pin(28))
pwm = PWM(Pin(15),freq=50)
conversion_factor = 3.3/(65535)
rtc = RTC()

def do_thing(t):  #定義一個do_thing函式
    reading = adc.read_u16() * conversion_factor
    temperature = 27 - (reading - 0.706)/0.001721
    #year,month,day,weekly,hours,minuse,seconds,info = rtc.datetime()
    #datetime_str = f"{year}-{month}-{day} {hours}:{minuse}:{seconds}"
    #print(datetime_str)
    print(f'溫度:{temperature}')
    adc_value = adc_light.read_u16()
    print(f'光線:{adc_value}')
    
def do_thing1(t):
    adc1 = ADC(Pin(26))
    duty = adc1.read_u16()
    pwm.duty_u16(duty)
    print(f'可變電阻:{round(duty/65536*10)}')

t1 = Timer(mode=Timer.PERIODIC, period=2000, callback=do_thing)
t2 = Timer(mode=Timer.PERIODIC, period=500, callback=do_thing1)



