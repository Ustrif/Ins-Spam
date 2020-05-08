def chechmod():
    try:
        from selenium import webdriver
        import re
        import os
        import colorama
        from selenium.webdriver.chrome.options import Options
        open("kullanicilar.txt","r", encoding= "utf-8")
        open("şifreler.txt","r", encoding= "utf-8")
    except ModuleNotFoundError:
        print("* Modüllerden biri sisteminizde bulunmamaktadır.")
        input("* Bir tuşa basın ve modülleri yükleyin.")
        exit()
    except FileNotFoundError:
        print("* kullanicilar.txt veya şifreler.txt programın bulunduğu dizinde yoktur.")
        input("* Bir tuşa basın ve yazılımı sonlandırın.")
        exit()
        
if __name__ == "__main__":
    chechmod()
    import os
    if os.name == "nt":
        os.system("cls")
    from colorama import Fore, init, Style
    init(autoreset=True)
    print(Fore.BLUE + """
    
 ______                             ______                                    
/      |                           /      \                                   
$$$$$$/  _______    _______       /$$$$$$  |  ______    ______   _____  ____  
  $$ |  /       \  /       |      $$ \__$$/  /      \  /      \ /     \/    \ 
  $$ |  $$$$$$$  |/$$$$$$$/       $$      \ /$$$$$$  | $$$$$$  |$$$$$$ $$$$  |
  $$ |  $$ |  $$ |$$      \        $$$$$$  |$$ |  $$ | /    $$ |$$ | $$ | $$ |
 _$$ |_ $$ |  $$ | $$$$$$  |      /  \__$$ |$$ |__$$ |/$$$$$$$ |$$ | $$ | $$ |
/ $$   |$$ |  $$ |/     $$/       $$    $$/ $$    $$/ $$    $$ |$$ | $$ | $$ |
$$$$$$/ $$/   $$/ $$$$$$$/         $$$$$$/  $$$$$$$/   $$$$$$$/ $$/  $$/  $$/ 
                                            $$ |                              
                                            $$ |                              
                                            $$/                               
                                                                                .py

    """ + Style.RESET_ALL)
    şeh = input(Fore.GREEN + "* Şikayet edilecek hesabın kullanıcı adını giriniz ? = " + Fore.RED)
    print(Style.RESET_ALL + """
    ****************************
    *1 = Spam                  *
    *--------------------------*
    *2 = Taciz veya Zorbalık   *
    *--------------------------*
    *3 = Çıplaklaklık          *
    *--------------------------*
    *4 = Nefret Söylemi        *
    *--------------------------*
    *5 = Kendine Zarar Verme   *
    ****************************
    """)
    şikayetn = input(Fore.GREEN + "* Şikayet sebebi seçiniz ? [Numarası] = " + Fore.RED)
    print(Style.RESET_ALL + "")

    import time
    import re
    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options
    
    kullanıcıtext = open("kullanicilar.txt","r",encoding= "utf-8")
    şifretext = open("şifreler.txt","r",encoding= "utf-8")

    class insgir():
        def __init__(self):
            super().__init__()
            self.parola = kullanıcıtext
            self.kkadı = şifretext
            self.seh = şeh
            self.şikayetn = şikayetn
            print(Fore.GREEN +"* Veri aktarılıyor..." + Style.RESET_ALL)
            self.num()
        def num(self):
            self.options = Options()
            self.options.headless = True
            self.browser = webdriver.Chrome(options=self.options)

            self.url11 = "https://codeofaninja.com/tools/find-instagram-user-id"
            self.browser.get(self.url11)
            self.browser.find_element_by_xpath("//*[@id='user_input']").send_keys(self.seh)
            self.browser.find_element_by_xpath("//*[@id='find-instagram-uid']/p[2]/input").click()
            time.sleep(4)
            kullanıcıid = self.browser.find_element_by_xpath("//*[@id='answer']/div[1]/div[2]/div[1]/b").text
            global string
            string = (int(kullanıcıid))
            print(Fore.GREEN + "* Hesabın gerekli verileri toplandı..." + Style.RESET_ALL)
            self.browser.quit()

        
    class insspam():
        def __init__(self):
            super().__init__()

            self.insspambasla()

        def insspambasla(self):
            self.options = Options()
            self.options.headless = True
            self.browser = webdriver.Chrome(options=self.options)
            self.url = "https://www.instagram.com/accounts/login/?next=/users/{}/report/".format(string)
            self.browser.get(self.url)
            time.sleep(3)
            sayı1 = len(self.browser.find_elements_by_xpath("//*[@id='react-root']/section/main/article/div"))
            if sayı1 == 2 :
                self.browser.quit()
                self.insspambasla()
            else :
                self.browser.find_element_by_xpath("//*[@id='react-root']/section/main/div/article/div/div[1]/div/form/div[2]/div/label/input").send_keys(kkadı)
                self.browser.find_element_by_xpath("//*[@id='react-root']/section/main/div/article/div/div[1]/div/form/div[3]/div/label/input").send_keys(parola)
                self.browser.find_element_by_xpath("//*[@id='react-root']/section/main/div/article/div/div[1]/div/form/div[4]/button").click()
                time.sleep(3)
                sayı = len(self.browser.find_elements_by_xpath("//*[@id='react-root']/section/main/div/article/div/div[1]/div/form/div"))
                if sayı == 7 : 
                    print(Fore.RED + f"* {kkadı} hesabının şifresi veya parolası hatalı." + Style.RESET_ALL)
                    time.sleep(1)
                    print(Fore.RED + "* Bu hesabın atağı başarısız!")
                    self.browser.quit()
                else:
                    sayı2 = len(self.browser.find_elements_by_xpath("//*[@id='react-root']/section/nav/div[2]/div/div/div"))
                    if sayı2 == 3 :
                        print(Fore.RED + f"* {kkadı} Bu hesaba giriş yapıp onaylamasını yapınız." + Style.RESET_ALL)
                    else:
                        time.sleep(1)
                        say3 = len(self.browser.find_elements_by_xpath("//*[@id='react-root']/section/div/div/div"))
                        if say3 == 4:
                            print(Fore.RED + f"* {kkadı} Bu hesap doğrulamaya düşmüş." + Style.RESET_ALL)
                            self.browser.quit()
                        else:
                            sayı4 = len(self.browser.find_elements_by_xpath("/html/body/div/div"))
                            if sayı4 == 2:
                                print("* Hesap kapanmış atak bitiriliyor...")
                                print(Fore.CYAN + """* Yapımcı : "Atmaca """)
                                input(Fore.GREEN + "* Çıkmak için tuşa basınız...")
                                exit()
                            else:
                                if şikayetn == 1:
                                    self.browser.find_element_by_xpath("//*[@id='react-root']/div/ul/li[2]").click()

                                elif şikayetn == 2:
                                    self.browser.get(f"https://www.instagram.com/users/{string}/report/inappropriate")
                                    self.browser.find_element_by_xpath("//*[@id='react-root']/div/ul/li[1]").click()

                                elif şikayetn == 3:
                                    self.browser.get(f"https://www.instagram.com/users/{string}/report/inappropriate")
                                    self.browser.find_element_by_xpath("//*[@id='react-root']/div/ul/li[4]").click()
                        
                                elif şikayetn == 4:
                                    self.browser.get(f"https://www.instagram.com/users/{string}/report/inappropriate")
                                    self.browser.find_element_by_xpath("//*[@id='react-root']/div/ul/li[5]").click()

                                elif şikayetn == 5:
                                    self.browser.get(f"https://www.instagram.com/users/{string}/report/inappropriate")
                                    self.browser.find_element_by_xpath("//*[@id='react-root']/div/ul/li[6]").click()

                                else:
                                    self.browser.find_element_by_xpath("//*[@id='react-root']/div/ul/li[2]").click()

                                time.sleep(0.3)
                                print(Fore.GREEN + "* Atak başarılı!" + Style.RESET_ALL)
                                self.browser.quit()
    insgir()

    a = open("kullanicilar.txt","r", encoding= "utf-8").read().strip()
    b = open("şifreler.txt","r",encoding= "utf-8").read().strip()
    s = re.compile(r'\s+')
    for i,j in zip(*map(s.split, [a,b])):
        kkadı = i
        parola = j
        insspam()
    print(Fore.GREEN + "* Atak bitmiştir....")
    print(Fore.CYAN + """* Yapımcı : "Atmaca """)
    input(Fore.GREEN + "* Çıkmak için tuşa basınız...")
    exit()
    
        





        
    
