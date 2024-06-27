from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys
import link_url
import random
import requests
# chrome_profile_directory = r"C:\Users\Administrator\AppData\Local\Google\Chrome\User Data\Default"
acc_start = int(input("Which account do you want to start? "))
time.sleep(1)
Logouted = False
def take_key2Fa(link):
    s = requests.session()
    heardes = {
        'authority':'2fa.live',
        'Accept-Language': 'vi,en-US;q=0.9,en;q=0.8',
        'Content-Type':'application/json',
        'Referer': 'https://2fa.live/',
        'Sec-Ch-Ua':'"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
        'Sec-Ch-Ua-Mobile':'?0',
        'Sec-Ch-Ua-Platform':"Windows",
        'Sec-Fetch-Dest':'empty',
        'Sec-Fetch-Mode':'cors',
        'Sec-Fetch-Site':'same-origin',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36'
    }
    s.headers.update(heardes)
    Key2fa = s.get(url=f'https://2fa.live/tok/{link}', headers=heardes)
    return Key2fa.text[10:16]

def log_out(driver):
    driver.get('http://facebook.com')
    #Chấp thuận tắt trang web
    try:
        # Chờ đợi cho đến khi thông báo xuất hiện (tối đa 10 giây)
        alert = driver.switch_to.alert
        # Tắt thông báo bằng cách chấp nhận nó
        alert.accept()
    except:
        # Không có thông báo xuất hiện hoặc đã xử lý thông báo
        pass  
    for i in range(0,10):
        time.sleep(1)
        try:
            driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/div[2]/div[5]/div[1]/span/div").click()
            break
        except:
            continue
    for i in range(0,10):
        time.sleep(1)
        try:
            try:                                    
                driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/div[2]/div[5]/div[2]/div/div/div[1]/div[1]/div/div/div/div/div/div/div/div/div[1]/div/div/div[1]/div[2]/div/div[6]/div/div[1]").click()
                break
            except:
                try:
                    driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/div[2]/div[5]/div[2]/div/div/div[1]/div[1]/div/div/div/div/div/div/div/div/div[1]/div/div/div[1]/div[2]/div/div[6]/div/div[1]/div[2]/div").click()
                    break
                except:
                    driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/div[2]/div[5]/div[2]/div/div/div[1]/div[1]/div/div/div/div/div/div/div/div/div[1]/div/div/div[1]/div[2]/div/div[5]/div/div[1]/div[2]/div").click()
                    break
        except:
            continue
    # Xuất hiện thông báo bạn có muốn 
    time.sleep(0.5)
    try:
        # Chờ đợi cho đến khi thông báo xuất hiện (tối đa 10 giây)
        alert = driver.switch_to.alert
        # Tắt thông báo bằng cách chấp nhận nó
        alert.accept()
    except:
        # Không có thông báo xuất hiện hoặc đã xử lý thông báo
        pass
def Check_Dismiss_Ban(tk,mk,link_2Fa,driver):
    #Check dissmiss
    try:
        driver.find_element(By.XPATH,"/html/body/div[1]/div/div/div/div/div/div/div[2]/div/div/div[1]/div/div/div/div/div/div/div/div/div/div/div[3]/div/div").click()
        time.sleep(1)
        driver.get('http://facebook.com')
        time.sleep(2)
        #Click avt
        for i in range(0,10):
            time.sleep(1)
            if i == 9:
                return
            try:
                driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/div[2]/div[5]/div[1]/span/div").click()
                break
            except:
                continue
        time.sleep(2)
        # Change Page
        try:        
            driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/div[2]/div[5]/div[2]/div/div[2]/div[1]/div[1]/div/div/div/div/div/div/div/div/div[1]/div/div/div[1]/div[1]/div/div/div[1]/div/div[2]/span/div/div[1]").click()
        except:
            try:   
                driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/div[2]/div[5]/div[2]/div/div/div[1]/div[1]/div/div/div/div/div/div/div/div/div[1]/div/div/div[1]/div[1]/div/div/div[1]/div/div[2]/span/div/div[1]/div[1]").click()
            except:                                      
                try:
                    driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/div[2]/div[5]/div[2]/div/div/div[1]/div[1]/div/div/div/div/div/div/div/div/div[1]/div/div/div[1]/div[1]/div/div/a/div[1]/div[3]").click()   
                except:
                    try:
                        driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/div[2]/div[5]/div[2]/div/div[1]/div[1]/div[1]/div/div/div/div/div/div/div/div/div[1]/div/div/div[1]/div[1]/div/div/div[1]/div/div[2]/span/div/div[1]").click()   
                    except:
                        return True
        finally:
            time.sleep(2)
    except:
        try:
            #Ban acc    
            try:        
                driver.find_element(By.XPATH,"/html/body/div[1]/div/div/div/div/div/div/div[1]/div/div[3]/div[1]/div[1]/span/div").click()
            except:
                driver.find_element(By.XPATH,"/html/body/div[1]/div/div/div/div/div/div/div[1]/div/div[3]/div[1]/div[2]/span/div").click()
                
            time.sleep(1)
            driver.find_element(By.XPATH,"/html/body/div[1]/div/div/div/div/div/div/div[1]/div/div[3]/div[2]/div/div/div[1]/div[1]/div/div/div/div/div/div/div/div[1]/div/div[2]/div/div[2]/div/div[1]/div[2]/div").click()
            time.sleep(1)
            try:
                driver.find_element(By.XPATH,"/html/body/div[3]/div[1]/div/div[2]/div/div/div/div/div/div/div[3]/div/div/div/div/div[1]/div/div").click()
            except: pass
            global Logouted
            Logouted = True
            file_error = open(r'Error.txt','a', encoding='utf-8')
            file_error.write(tk + ' | ' + mk + '|' + link_2Fa)
            file_error.close()
            print("Acc bị khóa")
            return True
        except:
            return False
def click_link_with_wait(driver, i, j):
    try:
        #normal
        driver.find_element(By.XPATH,f"/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div/div[4]/div[2]/div/div[2]/div[{i}]/div[1]/div/div/div/div/div/div/div/div/div/div/div[{j}]/div/div/div[4]/div/div/div[1]/div/div[2]/div/div[2]/div/div[1]").click()                                        
        return True
    except:
        try: # share
            driver.find_element(By.XPATH,f"/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div/div[4]/div[2]/div/div[2]/div[{i}]/div[1]/div/div/div/div/div/div/div/div/div/div/div[{j}]/div/div/div[4]/div/div/div[1]/div/div/div/div[2]/div/div[1]").click()
            return True
        except:                    
            try: # tagname
                driver.find_element(By.XPATH,f"/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div/div[4]/div[2]/div/div[2]/div[{i}]/div[1]/div/div/div/div/div/div/div/div/div/div/div[{j}]/div/div/div[5]/div/div/div[1]/div/div[2]/div/div[2]/div/div[1]").click()
                return True
            except:
                try: # reels
                    driver.find_element(By.XPATH,f"/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div/div[4]/div[2]/div/div[2]/div[{i}]/div[1]/div/div/div/div/div/div/div/div/div/div/div[{j}]/div/div/div[2]/div/div[1]/div/a/div[2]/div/div/div/div[3]/div/div/div/div[1]/div").click()
                    return True
                except:
                    return False                                     

def Tool_Comment(url,condition_cmt,name,tk,mk,is2Fa,link_2Fa,driver):
    try:
        driver.get('http://facebook.com')
        time.sleep(2)
        content_comment =  "Content"
        # if condition_cmt == 2:
        #     content_comment =  "Content"
        #Check_1
        if Check_Dismiss_Ban(tk,mk,link_2Fa,driver):
            return
        # Loggin
        characters = "liACPMOT"
        count_comment = 0
        number_comment = 15
        user = driver.find_element(By.ID, "email")
        user.send_keys(tk)
        password = driver.find_element(By.ID, "pass")
        password.send_keys(mk)
        password.send_keys(Keys.ENTER)
        if(is2Fa):
            try:
                time.sleep(1)
                try:
                    keyboard = driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div[1]/div/form/div/div[2]/ul/li[3]/span/input")
                except:
                    keyboard = driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div[1]/div/form/div/div[2]/ul/li[2]/span/input")
                key = take_key2Fa(link_2Fa)
                keyboard.send_keys(key)
                time.sleep(1)
                keyboard = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[1]/div/form/div/div[3]/div[1]/button").click()
                time.sleep(2)
                keyboard = driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div[1]/div/form/div/div[3]/div[1]/button").click()
                try:
                    driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[1]/div/form/div/div[3]/div[1]/button").click()
                    time.sleep(1)
                    driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[1]/div/form/div/div[3]/div[1]/button[1]").click()
                    time.sleep(1)
                    driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[1]/div/form/div/div[3]/div[1]/button").click()
                except:
                    pass
            except:
                try:
                    driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[1]/div/form/div/div[3]/div[1]/button").click()
                    time.sleep(1)
                    driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[1]/div/form/div/div[3]/div[1]/button[1]").click()
                    time.sleep(1)
                    driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[1]/div/form/div/div[3]/div[1]/button").click()
                except:
                    pass
        time.sleep(4)

        #thông báo gỡ cmt
        clicked = True
        while clicked:
            for i in range(1,6):
                try:
                    driver.find_element(By.XPATH,f"/html/body/div[{i}]/div[1]/div/div[2]/div/div/div/div[2]/div").click()
                    time.sleep(3)
                    break
                except:
                    if(i==5):
                        clicked = False
        #Check_1
        if Check_Dismiss_Ban(tk,mk,link_2Fa,driver):
            return
        # Click Avt
        for i in range(0,10):
            time.sleep(1)
            if i == 9:
                print("Lỗi không click vào avt được!!!!!!!!!!")
                global Logouted
                Logouted = True
                file_error = open(r'Error.txt','a', encoding='utf-8')
                file_error.write(tk + ' | ' + mk + '|' + link_2Fa)
                file_error.close()
                return
            try:
                driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/div[2]/div[5]/div[1]/span/div").click()
                break
            except:
                continue

        time.sleep(1)
        # Change Page                                      
        try:
            driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/div[2]/div[5]/div[2]/div/div/div[1]/div[1]/div/div/div/div/div/div/div/div/div[1]/div/div/div[1]/div[1]/div/div/a/div[1]/div[3]").click()   
        except:
            try:
                driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/div[2]/div[5]/div[2]/div/div/div[1]/div[1]/div/div/div/div/div/div/div/div/div[1]/div/div/div[1]/div[1]/div/div/div[1]/div/span/div/div/div/div/div[1]/div").click()
            except:
                print("Lỗi không convert được Page!!!!!!!!!!")
                return
        time.sleep(4)
        for pos in range(0,len(url)):
            #Check_2
            if Check_Dismiss_Ban(tk,mk,link_2Fa,driver):
                return
            
            if count_comment >= number_comment:
                print(f"Done {count_comment} comments")
                return
            x=y=0
            driver.get(url[pos])
            #Chấp thuận tắt trang web
            try:
                # Chờ đợi cho đến khi thông báo xuất hiện (tối đa 10 giây)
                alert = driver.switch_to.alert
                # Tắt thông báo bằng cách chấp nhận nó
                alert.accept()
            except:
                # Không có thông báo xuất hiện hoặc đã xử lý thông báo
                pass
            time.sleep(3)
            for i in range(1, 20):
                for j in range(1,20):
                    if click_link_with_wait(driver, i, j):
                        x = i
                        y = j
                        break

            if x==0 and y==0:
                # print("Đã bị block")
                file = open(r'Block.txt','a')
                file.write(url[pos] +'\n')
                file.close()
                continue    
            for k in range (1,8):
                time.sleep(3)
                #Kiểm tra xem có bị không comment được không
                for pos_bl in range(1,10):
                    try:              
                        driver.find_element(By.XPATH,f"/html/body/div[{pos_bl}]/div[1]/div/div[2]/div/div/div/div/div/div/div[3]/div/div/div/div/div/div").click()                           
                        print("Tài khoản đang bị chặn comment: ", tk)
                        return
                    except:
                        continue

                try: # Normal
                    #Click on button Comment
                    try:
                        driver.find_element(By.XPATH,f"/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div/div[4]/div[2]/div/div[2]/div[{x}]/div[{k}]/div/div/div/div/div/div/div/div/div/div/div[{y}]/div/div/div[4]/div/div/div[1]/div/div[2]/div/div[2]/div/div[1]").click()    
                    except:
                        try:
                            driver.find_element(By.XPATH,f"/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div/div[4]/div[2]/div/div[2]/div[{x}]/div[{k}]/div/div/div/div/div/div/div/div/div/div/div[{y}]/div/div/div[2]/div/div[1]/div/a/div[2]/div/div/div/div[3]/div/div/div/div[1]/div").click()
                        except:
                            try:
                                driver.find_element(By.XPATH,f"/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div/div[4]/div[2]/div/div[2]/div[{x}]/div[{k}]/div/div/div/div/div/div/div/div/div/div/div[{y}]/div/div/div[4]/div/div/div[1]/div/div/div/div[2]/div/div[1]").click()
                            except:
                                try:
                                    driver.find_element(By.XPATH,f"/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div/div[4]/div[2]/div/div[2]/div[{x}]/div[{k}]/div/div/div/div/div/div/div/div/div/div/div[{y}]/div/div/div[5]/div/div/div[1]/div/div[2]/div/div[2]/div/div[1]").click()
                                except:
                                    pass
                    #Begin Find Name
                    try:
                        #Bình thường
                        for p in range(1,10):
                            try:
                                element = driver.find_element(By.XPATH, f"/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div/div[4]/div[2]/div/div[2]/div[{x}]/div[{k}]/div/div/div/div/div/div/div/div/div/div/div[{y}]/div/div/div[4]/div/div/div[2]/div[{p}]/div/div/div[2]/div[1]/div[1]/div/div/span/a/span/span")
                                content = element.text
                                break
                            except:
                                if p == 9:
                                    raise
                    except:                        
                        try:
                            for p in range(1,10):
                                try:
                                    element = driver.find_element(By.XPATH,f"/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div/div[4]/div[2]/div/div[2]/div[{x}]/div[{k}]/div/div/div/div/div/div/div/div/div/div/div[{y}]/div/div/div[4]/div/div/div[2]/div[{p}]/div/div/div[2]/div[1]/div[1]/div/div/div[1]/span/a/span/span")                    
                                    content = element.text
                                    break
                                except:
                                    try:
                                        element = driver.find_element(By.XPATH,f"/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div/div[4]/div[2]/div/div[2]/div[{x}]/div[{k}]/div/div/div/div/div/div/div/div/div/div/div[{y}]/div/div/div[4]/div/div/div[2]/div[{p}]/div/div/div[2]/div[1]/div[1]/div/div/div/div/span/a/span/span")
                                        content = element.text
                                    except:
                                        if p == 9:
                                            raise
                        except: 
                            #Share post
                            try:
                                element = driver.find_element(By.XPATH,f"/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div/div[4]/div[2]/div/div[2]/div[{x}]/div[{k}]/div/div/div/div/div/div/div/div/div/div/div[{y}]/div/div/div[4]/div/div/div[2]/div[3]/div/div/div[2]/div[1]/div[1]/div/div/span/a/span/span")
                                content = element.text
                            except:
                                try:
                                    #Tag Name
                                    for p in range(1,10):  
                                        try:
                                            element = driver.find_element(By.XPATH,f"/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div/div[4]/div[2]/div/div[2]/div[{x}]/div[{k}]/div/div/div/div/div/div/div/div/div/div/div[{y}]/div/div/div[5]/div/div/div[2]/div[{p}]/div/div/div[2]/div[1]/div[1]/div/div/span[1]/a/span/span")
                                            content = element.text
                                            break
                                        except:
                                            if p ==9:
                                                raise
                                except:
                                    time.sleep(1.5)
                                    try:
                                        #Hiện bài viết
                                        try:                              
                                            element = driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div[2]/div[2]/div[3]/div/div[2]/div/div[2]/ul/li[1]/div[1]/div/div[2]/div[1]/div[1]/div/div/div/div/span/a/span/span")
                                            content = element.text
                                        except:
                                            element = driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div[2]/div[2]/div[3]/div/div[2]/div/div[2]/ul/li[1]/div[1]/div/div[2]/div[1]/div[1]/div/div/span/a/span/span")
                                            content = element.text
                                    except:
                                        #Reels
                                        try:  
                                            element = driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/div[5]/div/div/div[3]/div[2]/div/div/div[1]/div/div/div/div/div[3]/div[2]/div[1]/div/div[1]/div/div[3]/div/div[2]/div/div/div/div[1]/div[2]/div[2]/div[1]/div[1]/div/div[1]/div/div/span/a/span/span")
                                            content = element.text 
                                        except:
                                            content = ' '
                    #End Find Name 
                    if content != name:
                        #Begin Comment
                        try: 
                            #Bình thường
                            try:        
                                for p in range(1,10):
                                    try: 
                                        driver.find_element(By.XPATH,f"/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div/div[4]/div[2]/div/div[2]/div[{x}]/div[{k}]/div/div/div/div/div/div/div/div/div/div/div[{y}]/div/div/div[4]/div/div/div[2]/div[{p}]/div/div/div/div[2]/div/div[2]/form/div/div[1]/div[1]/div/div[1]/p").send_keys(random.choice(characters)+content_comment)
                                        break
                                    except:
                                        if p == 9:
                                            raise 
                            except:
                                try:
                                    for p in range(1,10):
                                        try:
                                            driver.find_element(By.XPATH,f"/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div/div[4]/div[2]/div/div[2]/div[{x}]/div[{k}]/div/div/div/div/div/div/div/div/div/div/div[{y}]/div/div/div[4]/div/div/div[2]/div[{p}]/div/div/div/div/div/div[2]/form/div/div[1]/div[1]/div/div[1]/p").send_keys(random.choice(characters)+content_comment)
                                            break
                                        except:
                                            if p == 9:
                                                raise
                                except:
                                    for p in range(1,10):
                                        try:
                                            driver.find_element(By.XPATH,f"/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div/div[4]/div[2]/div/div[2]/div[{x}]/div[{k}]/div/div/div/div/div/div/div/div/div/div/div[{y}]/div/div/div[5]/div/div/div[2]/div[{p}]/div/div/div/div[2]/div/div[2]/form/div/div[1]/div[1]/div/div[1]/p").send_keys(random.choice(characters)+content_comment)
                                            break
                                        except:
                                            if p == 9:
                                                raise               
                        except:
                                #Share Post
                                try:
                                    #Tag Name
                                    try: 
                                        driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div[3]/div/div/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div/div/div[2]/form/div/div[1]/div[1]/div/div[1]/p").send_keys(random.choice(characters)+content_comment)
                                    except:
                                        for i in range(1,10):
                                            try:
                                                driver.find_element(By.XPATH,f"/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div/div[4]/div[2]/div/div[2]/div[{x}]/div[{k}]/div/div/div/div/div/div/div/div/div/div/div[{y}]/div/div/div[5]/div/div/div[2]/div[{i}]/div/div/div/div/div/div[2]/form/div/div[1]/div[1]/div/div[1]/p").send_keys(random.choice(characters)+content_comment)
                                                break
                                            except:
                                                if i==9:
                                                    raise
                                except:
                                    try:
                                        #Hiện lên
                                        driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div[3]/div/div/div/div/div/div[1]/div/div/div/div[2]/form/div/div[1]/div[1]/div/div[1]/p").send_keys(random.choice(characters)+content_comment)
                                    except:
                                        #Reels
                                        try:
                                            for p in range (1,10):
                                                try:
                                                    driver.find_element(By.XPATH,f"/html/body/div[1]/div/div[1]/div/div[5]/div/div/div[3]/div[2]/div/div/div[1]/div/div/div/div/div[3]/div[2]/div/div/div[1]/div/div[3]/div/div[{p}]/div/div/div/div/div/div/div/div/div/div[2]/form/div/div[1]/div/div/div[1]/p").send_keys(random.choice(characters)+content_comment)                                                             
                                                    break
                                                except:
                                                    if p == 9:
                                                        raise
                                        except:
                                            driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/div[2]/div[1]/div[1]/span/div").click()
                                            continue
                        #End Comment
                        time.sleep(0.5)
                        #Begin Send Comment
                        try:
                            try:
                                #Bình thường
                                for i in range(1,10):
                                    try:
                                        driver.find_element(By.XPATH,f"/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div/div[4]/div[2]/div/div[2]/div[{x}]/div[{k}]/div/div/div/div/div/div/div/div/div/div/div[{y}]/div/div/div[4]/div/div/div[2]/div[{i}]/div/div/div/div[2]/div/div[2]/form/div/div[2]/div/div[2]/div/div/div/span/div").click()                                        
                                        break                            
                                    except:
                                        if i == 9:
                                            raise
                            except:
                                for i in range(1,10):
                                    try:                                            
                                        driver.find_element(By.XPATH,f"/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div/div[4]/div[2]/div/div[2]/div[{x}]/div[{k}]/div/div/div/div/div/div/div/div/div/div/div[{y}]/div/div/div[4]/div/div/div[2]/div[{i}]/div/div/div/div/div/div[2]/form/div/div[2]/div/div[2]/div/div/div/span/div").click()
                                        break                            
                                    except:
                                        if i == 9:
                                            raise    
                        except:
                            try:
                                #Reels
                                driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/div[2]/div[1]/div[1]/span/div")
                                for p in range (1,11):                            
                                    try:
                                        driver.find_element(By.XPATH,f"/html/body/div[1]/div/div[1]/div/div[5]/div/div/div[3]/div[2]/div/div/div[1]/div/div/div/div/div[3]/div[2]/div/div/div[1]/div/div[3]/div/div[{p}]/div/div/div/div/div/div/div[2]/div/div/div[2]/form/div/div[2]/div/div[2]/div/div/div/span/div").click() 
                                        break
                                    except:
                                        pass
                                #Share post
                            except:
                                try:
                                        driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div[3]/div/div/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div/div/div[2]/form/div/div[2]/div/div[2]/div/div/div/span/div").click()
                                except:
                                    #Hiện lên                                                                                        
                                    driver.find_element(By.XPATH,f"/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div/div[4]/div[2]/div/div[2]/div[{x}]/div[{k}]/div/div/div/div/div/div/div/div/div/div/div[{y}]/div/div/div[5]/div/div/div[2]/div[2]/div/div/div/div/div/div[2]/form/div/div[2]/div/div[2]/div/div/div/span/div").click()
                        time.sleep(0.5)
                        # Tắt Bảng
                        try:
                            try:
                                #Tắt reels
                                driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/div[2]/div[1]/div[1]/span/div").click()
                            except:
                                try:
                                    driver.find_element(By.XPATH,'/html/body/div[1]/div/div[1]/div/div[4]/div/div[2]/div[1]/div/div[2]/div/div/div/div/div/div/div[3]/div/div/div/div/div[1]/div/div').click()
                                except:
                                    driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div[1]/div/div[2]/div").click()
                        except:
                            pass
                        print('Đã cmt',count_comment)
                        count_comment+=1
                    else: break
                except:
                    #Check_3
                    if Check_Dismiss_Ban(tk,mk,link_2Fa,driver):
                        return
                    # print("Đường dẫn đã bị lỗi:"+url[pos])
                    print("Lỗi Không xác định được!!!!")
                    # input("abc: ")
                    break
    except:
        print("Đang bị lỗi tài khoản: ", tk)
        return
        
def main():
    global acc_start
    global Logouted
    # global chrome_profile_directory
    Acc = list()
    fileAccount = open(r'Account.txt', 'r', encoding='utf-8')
    for line in fileAccount:
        Acc.append(line.strip().split('|'))
    while True:
        if acc_start < len(Acc)+1:
            break
    while True:
        for i in range (acc_start,len(Acc)+1):
            Logouted = False
            print(f"Start account {i}")
            # nếu acc ở vị trí i bị lỗi thì pass qua acc mới
            if  i == 9 : continue
            options = webdriver.ChromeOptions()
            options.add_argument("--start-maximized")
            options.add_argument("--disable-notifications")
            # options.add_argument(f"--user-data-dir={chrome_profile_directory}")
            driver = webdriver.Chrome(options=options)
            if len(Acc[i-1]) == 4:
                Tool_Comment(getattr(link_url, f'url_{i}'), Acc[i-1][2], Acc[i-1][3], Acc[i-1][0],Acc[i-1][1],False,"",driver)
            if len(Acc[i-1]) == 5:
                Tool_Comment(getattr(link_url, f'url_{i}'), Acc[i-1][3], Acc[i-1][4], Acc[i-1][0],Acc[i-1][1],True,Acc[i-1][2],driver)
            if(Logouted == False):
                log_out(driver)
            else:
                file_error = open(r'Error.txt','a', encoding='utf-8')
                file_error.write(f'| {i}\n')
                file_error.close()
            print(f'Done account {i}')
            print('====================================================================')
            driver.quit()
            
        print('Done all!!!')
        with open(r'Check.txt', 'a', encoding='utf-8') as file_error: file_error.write('\n')
        file_error = open(r'Error.txt','a', encoding='utf-8')
        file_error.write('====================================================================\n')
        file_error.close()
        file_block = open(r'Block.txt','a', encoding='utf-8')
        file_block.write('====================================================================\n')
        file_block.close()

if __name__ == "__main__":
    main()
    input("Done...........................")
