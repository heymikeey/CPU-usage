# Cpu-Usage

## Del 1 Kopiera

-info
NU har du 2 filer i din mapp, cpu_usage.py och cpu_usage.service.

Steg 1. Börja med att kopiera in cpu_usage.py in i /usr/bin/ som sudo
Kommando: sudo cp cpu_usage.py /usr/bin/

Steg 2. nu ska du köpiera in cpu_usage.service in i /etc/systemd/system/ som sudo
Kommando: sudo cp cpu_usage.service /etc/systemd/system/



## Del 2 Starta Service

-info
NU ska du starta service filen och sedan kolla om den är up and running med status, sedan ska vi kolla om servicefilen har skrivit en loggfil, som vi kan titta på om vi överskrider minnesanvändningen som vi har angett. 
Om du skriver enabled så sätts servicefilen på automatiskt vid omstart eller boot. 
Skriver du stop så stänger du av servicen.

Steg 1. Börja med att starta service filen som sudo, servicefilen har ett inmatat värde som kör cpu_usage.py varje 5:e minut och har 100MB som gränsvärde för minnesanvändning.
Så vi väntar i 5 min här efter vi skrivit in kommandot.
Kommando: sudo systemctl start cpu_usage.service

Steg 2. Vi kollar status bara för att se om den är igång ordentligt.
Kommando: sudo systemctl status cpu_usage.service

Steg 3. Nu ska vi använda oss utav enable, den startar servicen vid startup(boot)
Kommando: sudo systemctl enable cpu_usage.service

Steg 4. För att stoppa cpu_usage.service skriver in följande kommando
Kommando: sudo systemctl stop cpu_usage.service


## Del 3 The final Bang! Loggfilen

-info 
Här ska vi då kolla om loggfilen skrevs ut efter 5 min. Nu ska vi in i mappen där loggfilen skapades.
Ifall den skapades.
Kommando:  sudo cat /tmp/cpu_usage_rapport.txt 




