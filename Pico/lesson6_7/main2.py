from machine import Timer,ADC,PWM,Pin,RTC

adc = machine.ADC(4) #
pwm = PWM(Pin(15),freq=50)
conversion_factor = 3.3/(65535)
rtc = RTC()

def do_thing(t):  #定義一個do_thing函式
    
    reading = adc.read_u16() * conversion_factor
    temp = 27 - (reading - 0.706)/0.001721
    year,month,day,weekly,hours,minuse,second,info = rtc.datetime())
    print(temp)
    
def do_thing1(t):
    adc1 = ADC(Pin(26))
    duty = adc1.read_u16()
    pwm.duty_u16(duty)           
    print(f'可變電阻:{round(duty/65536*10)}')

t1 = Timer(mode=Timer.PERIODIC, period=2000, callback=do_thing)
t2 = Timer(mode=Timer.PERIODIC, period=500, callback=do_thing1)

