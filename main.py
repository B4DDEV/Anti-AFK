import pydirectinput, time, fade, os
import threading as th

keep_going = True
partner = []
key = []
timeout = 0
class Main:
    global timeout
    def __init__(self):

        self.tern = False
        self.ke = False
        

    def console(self):
        text = f"""
 ▄▄▄      ███▄    █ ▄▄▄█████▓  ██▓     ▄▄▄        █████ ▀██ ▄█▀
▒████▄    ██ ▀█   █ ▓  ██▒ ▓▒▒▓██▒    ▒████▄    ▓██      ██▄█▒ 
▒██  ▀█▄ ▓██  ▀█ ██▒▒ ▓██░ ▒░▒▒██▒    ▒██  ▀█▄  ▒████   ▓███▄░ 
░██▄▄▄▄██▓██▒  ▐▌██▒░ ▓██▓ ░ ░░██░    ░██▄▄▄▄██ ░▓█▒    ▓██ █▄ 
 ▓█   ▓██▒██░   ▓██░  ▒██▒ ░ ░░██░     ▓█   ▓██▒░▒█░    ▒██▒ █▄
 ▒▒   ▓▒█░ ▒░   ▒ ▒   ▒ ░░    ░▓       ▒▒   ▓▒█░ ▒ ░    ▒ ▒▒ ▓▒
  ░   ▒▒ ░ ░░   ░ ▒░    ░    ░ ▒ ░      ░   ▒▒ ░ ░      ░ ░▒ ▒░
  ░   ▒     ░   ░ ░   ░      ░ ▒ ░      ░   ▒    ░ ░    ░ ░░ ░ 
      ░           ░            ░            ░  ░        ░  ░        
        
        Key or patern : {partner} | {key}
        
        Timeout : {timeout}

        [!] Press Enter in console to end the process
        """

        self.banner = fade.purpleblue(text)
        print(self.banner)

    def start(self):
        global timeout
        valid_input = ["Key", "key", "Pattern", "pattern"]
        while True:
            self.keyorpatern = input("[!] - Single Key or Pattern (Key/Pattern) : ")
            if self.keyorpatern in valid_input:
                break
        
        if self.keyorpatern.lower() == "key":
            partner.clear()
            self.singlekey = str(input("[+] Provide the single key you want to use : "))
            if len(self.singlekey) < 1:
                self.singlekey = str(input("[+] Provide the single key you want to use : "))
            key.append(self.singlekey)
            self.timt = int(input("[+] How much timeout before restarting key :"))
            timeout = self.timt
            self.ke = True

        elif self.keyorpatern.lower() == "pattern":
            partner.clear()
            self.howmuchkey = int(input("[+] How much key in your pattern :"))
            for i in range(self.howmuchkey):
                os.system("cls")
                self.newkey = input(f"[{len(partner)}/{self.howmuchkey}] Enter the key :")
                partner.append(str(self.newkey))
            self.timt = int(input("[+] How much timeout between key pattern :"))
            timeout = self.timt

            self.tern = True
        os.system("cls")


class worker:
    
    def waiting(self):
        self.object = Main()
        word = ""
        if self.object.ke == True:
            word = "Key"
        elif self.object.tern == True:
            word = "Pattern"
        


        print(f"[!] Waiting Ten Second before executing {word}")
        time.sleep(5)


    def single(self):
        time.sleep(timeout)
        pydirectinput.press(key[0])
        

    
    def patern(self):
        for i in partner:
            time.sleep(timeout)
            pydirectinput.press(i)
            


def key_capture():
    global keep_going
    input()
    keep_going = False


def threadfonc():
    th.Thread(target=key_capture, args=(), name='key_capture', daemon=True).start()
    while keep_going:
        if keep_going == False:
            break
        else:
            if mainobject.tern == True:
                secondobject.patern()
            elif mainobject.ke == True:
                secondobject.single()


if __name__ == "__main__":
    mainobject = Main()
    secondobject = worker()
    mainobject.start()
    secondobject.waiting()
    mainobject.console()
    threadfonc()

