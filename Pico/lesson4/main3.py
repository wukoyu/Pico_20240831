from machine import Timer, Pin

# tim = Timer(period=5000, mode=Timer.ONE_SHOT, callback=lambda t:print(1))
# tim.init(period=1000, mode=Timer.PERIODIC, callback=lambda t:print(2))
green_led = Pin("LED",Pin.OUT)
green_count =0
def green_led_mycallback(t:Timer):
    global green_count
    green_count = green_count +1
    # print(f"目前mycallback被執行:{count}次")
    green_led.toggle()
    print("green_led初執行")
    if green_count >= 10:
        t.deinit() # 取消初始化計時器。停止定時器，並停用定時器週邊。

green_led_timer = Timer(period=1000,mode=Timer.PERIODIC,callback=green_led_mycallback)

red_led = Pin(15,Pin.OUT)
red_count =0
def red_led_mycallback(t:Timer):
    global red_count
    red_count = red_count +1
    # print(f"目前mycallback被執行:{count}次")
    red_led.toggle()
    print("red_led初執行")
    if red_count >= 10:
        t.deinit() # 取消初始化計時器。停止定時器，並停用定時器週邊。

red_led_timer = Timer(period=2000,mode=Timer.PERIODIC,callback=red_led_mycallback)