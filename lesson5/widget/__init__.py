# 自訂Function寫法；def function_name():

def input_data()->tuple[int,int]: #->tuple[int,int]可加可不加；但加了可讀性更好；稱作型別提示
    while True: #輸入身高無限迴圈
        try:
            cm = int(input("請輸入身高(公分):"))
            if cm > 300:
                raise Exception("超過300公分")
            break
        except ValueError:
                print('輸入格式錯誤')
                continue
        except Exception as e:
                print(f'輸入錯誤{cm}')
                continue
    while True: #輸入體重無限迴圈
        try:    
            kg = int(input("請輸入體重(公斤):"))
            if kg > 300:
                raise Exception("超過300公斤")
            break
        except ValueError:
                print('輸入格式錯誤')
                continue
        except Exception as e:
                print(f'輸入錯誤{kg}')
                continue
    return (cm,kg) #可省略括號

def get_status(bmi:float)->str: #:float->str可加可不加；但加了可讀性更好；稱作型別提示

    if bmi >=35:
        return "重度肥胖：BMI ≧ 35"
    elif bmi >=30:
        return "中度肥胖：30 ≦ BMI" 
    elif bmi >=27:
        return "輕度肥胖：27 ≦ BMI" 
    elif bmi >=24:
        return "過重" 
    elif bmi >=18.5:
        return "正常範圍" 
    else:
        return "體重過輕" 

def calculate_bmi(kg:int,cm:int)->float: # 型別提示；此函式需輸入兩個整數、輸出一個浮點數
    cm=(cm/100)*(cm/100)
    BMI=kg/cm #此BMI為區域變數
    return BMI