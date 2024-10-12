import network # MicroPython libraries 網路配置
import urequests as requests
import time
import rp2
from machine import WDT

rp2.country('TW') #設定我們的wifi的地區是台灣(可以不設)
'''
ssid = 'A590301'
password = 'A590301AA'
'''

ssid = 'dlink-51F2'
password = '4586531abc'


wlan = network.WLAN(network.STA_IF)
#構造函數，創建WLAN網路介面物件，STA表示Station Mode可用於連接到AP
wlan.active(True)#方法；啟動 （“up”） 或停用 （“down”） 網络介面
wlan.connect(ssid, password)
wlan.config(pm = 0xa11140) #預設是省電模式,可以設為非省電模式

def connect():  
    #等待連線或失敗
    #status=0,1,2正在連線
    #status=3連線成功
    #status>=3失敗的連線
    max_wait = 10    

    while max_wait > 0:
        status = wlan.status()
        if status < 0 or status >= 3:
            break
        max_wait -= 1
        print("等待連線")
        time.sleep(1)

    #處理錯誤
    if wlan.status() != 3:
        print('連線失敗,重新開機')
        raise RuntimeError('連線失敗') #開發階段,出現錯誤,中斷執行
        #wdt = WDT(timeout=2000) #無連接電腦時,重新開機(成品時,請使用這個)
        #wdt.feed()
    else:
        print('連線成功')
        status = wlan.ifconfig()
        print(f'ip={status[0]}') 
        
        
def reconnect():
    if wlan.status() == 3: #還在連線,只是傳送的server無回應
        print(f"執行reconnect,連線正常({wlan.status()})")
        return
    else:
        print("嘗試重新連線")
        wlan.disconnect()
        wlan.connect(ssid, password)
        connect() #再連線一次

connect()