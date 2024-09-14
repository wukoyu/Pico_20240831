# import tools #輸入tools自訂模組；自訂的模組就是.py檔
import widget #輸入widget自訂Package；自訂的package是一個資料夾

while True:
    kg=0  #清除變數
    cm=0  #清除變數
    # cm,kg = tools.input_data() #呼叫function
    cm,kg = widget.input_data() #呼叫function
    print(f'身高={cm},體重={kg}')
    # BMI = calculate_bmi(kg,cm) #引數值呼叫法；需依照順序呼叫
    # BMI = tools.calculate_bmi(cm=cm, kg=kg) #引數名稱呼叫法；可以不依照順序呼叫
    BMI = widget.calculate_bmi(cm=cm, kg=kg) #引數名稱呼叫法；可以不依照順序呼叫
    print(f'BMI={BMI}') #此BMI為全域變數

    # print(tools.get_status(BMI))
    print(widget.get_status(BMI))
    play_again = input("還要繼續嗎？(y,n)")
    if play_again == "n":
        break
print('程式結束')