from machine import Pin, PWM, ADC #Pin,PWM,ADC是Class

pwm = PWM(Pin(15))
adc = ADC(Pin(26)) #ADC0

pwm.freq(1000)

while True:
	duty = adc.read_u16()
	pwm.duty_u16(duty)

