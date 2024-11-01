import machine #這個模組通常用於微控制器Pi Pico，提供對硬體的低層次控制。
import utime #MicroPython特有模組，是對Time模組的簡化與最佳化

sensor_temp = machine.ADC(4)
conversion_factor = 3.3 / (65535)

while True:
    reading = sensor_temp.read_u16() * conversion_factor
    
    # The temperature sensor measures the Vbe voltage of a biased bipolar diode, connected to the fifth ADC channel
    # Typically, Vbe = 0.706V at 27 degrees C, with a slope of -1.721mV (0.001721) per degree.
    temperature = 27 - (reading - 0.706)/0.001721
    print(temperature)
    utime.sleep(2)