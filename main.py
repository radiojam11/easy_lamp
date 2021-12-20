#import ntptime #si prende l'ora da internet
#from machine import RTC
#rtc = RTC() #creo oggetto rtc 
#ntptime.settime()  #aggiorno l'ora di RTC con l'ora di internet
#ricordarsi di chiamare rtc.datetime(9 almeno ogni 7 ore per problemi di overflow della libreria
#RTC perde secondi ogni ora quindi per avere ora corretta aggiornare spesso con ntptime.settime()

import gc
gc.collect()
import machine, neopixel, network, urequests
from time import sleep, time                 
from pagineweb import *
    
def do_server():
    """Creo un server web con le pagine di configurazione lampada e registrazione dati accesso router casalingo - se entro qui sono in AP mode"""
    try:
      import usocket as socket
    except:
      import socket
    # Creo un socket e mi metto in ascolto
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('', 80))
    s.listen(5)

    while True:
      conn, addr = s.accept()
      print('Got a connection from %s' % str(addr))
      request = conn.recv(1024)
      request = str(request)         #stringa che riceve la richiesta da parte del Client o la risposta dal Form
      print('Content = %s' % request)
      lista = request.split(" ")
        
      if "/action_page.php?" in request:    # se ricevo la risposta dal Form entro qui  
        for el in lista:                    # cerco Utente e Password dentro la chiamata dal Client Form
            if "/action_page.php?" in el:
                indice_user_passw = lista[1].index("?") #cerco l'indice del punto esclamativo
                stringa_UP = lista[1][(indice_user_passw+1):]   #il primo carattere dopo il punto esclamativo inizia la stringa, la prendo tutta
                lista_UP = stringa_UP.split("&")                #la divido al carattere &   *****IMPORTANTE : SE LA PASSWORD DEL ROUTER CONTIENE IL CARATTERE &  NON FUNZIONA **BUG**
                UTENTE = lista_UP[0][6:]                        #ottengo UTENTE
                PASSW = lista_UP[1][4:]                         #ottengo PASSW
                break                                           #termino il ciclo di for
        filename = "credenziali.py"                                    #nome del file dove registro le credenziali di accesso al Router casalingo
        # creo la stringa da registrare nel file delle Credenziali    
        # ATTENZIONE a non modificare gli spazi qui sotto
        strcred = """def utente():
    return """ + "'" + UTENTE + "'" + """
def passw():
    return """ + "'" + PASSW + "'" 
        f = open(filename, "w+")             #creo il file delle credenziali
        f.write(strcred)
        f.close()
                
        response = registrato()              # rispondo al Client con una pagina di cortesia e resetto x Connettermi 
        conn.send(response)
        sleep(5)
        machine.reset()
      elif "/pagina_form.php" in request:
        response = form_page()                # Risposta al Client Web con il Form da compilare x Credenziali
        conn.send(response)
      elif "/mod_colore.php" in request:
        response = mod_colore()                # Risposta al Client Web con il Form da compilare x Colori
        conn.send(response)
      elif "/color_page.php" in request:
        # inserire controllo colori
        # e registrazione scelte su file config.txt
        indice_colori=request.index("?")
        stringa_sporca_colori = request[indice_colori+1:]
        print(stringa_sporca_colori)
        Rosso = stringa_sporca_colori[7:10]
        print(Rosso)
        Verde = stringa_sporca_colori[18:21]
        print(Verde)
        Blu = stringa_sporca_colori[27:30]
        print(Blu)  #fino qui funziona!
        
        #                            #da migliorare con altre casette
        #                            #ATTENZIONE non va bene DA SISTEMARE
        filename = "configRGB1.txt"                             #nome del file dove registro la scelta del colore della casetta secondaria n.1
                                                                # creo la stringa da registrare nel file
        strcred = "RGB1=("+Rosso+","+Verde+","+Blu+")\n" 
        f = open(filename, "w+")                                #creo il file della configurazione colore RGB1
        f.write(strcred)
        f.close()
                
        response = registrato()                # rispondo al Client con una pagina di cortesia e resetto x Ripartire 
        conn.send(response)
        sleep(5)
        machine.reset()
      else:                                # Se il CLient chiama root(/) , o qualsiasi altra pagina non prevista - Rispondo con il menu
        response = menu()                  # Risposta al Client Web con una pagina di Menu
        conn.send(response)
      conn.close()

     
def controlla_struttura():
    """sono online e controllo sul server se esiste la mia configurazione - se non esiste ne creo una di default - se tutto bene restituisco stato_cartella e mac address"""
    import ubinascii
    api_key = 'unastringadelgenere1234'
    mac = ubinascii.hexlify(network.WLAN().config('mac'),':').decode()
    print("il mio mac address e : "+mac)
    try:
        #controllo se esiste la cartrella con il mio mac address
        stringa = 'https://iot.sottosopraweb.com/casette/'+mac+'/'
        request = urequests.get(stringa)
    except Exception as e: 
        print(e)
        print("ho sollevato una eccezione")
        #print(request.text())
    if request.status_code == 403:            #devo intercettare l'errore 403 = forbidden
        #vuol dire che esiste la cartella - il server rende 403 Forbidden - OK regolare
        request.close()
        return "cartellaOK", mac
    elif request.status_code == 404:
        #vuol dire che non esiste la cartella con il mac address - va fatta la registrazione - MAC ergo SUM !
        request.close()
        sleep(1)
        request = urequests.get('https://iot.sottosopraweb.com/casette/registra_mio_mac.php?macadd='+mac+'&api_key='+api_key)
        if request.text == "FATTO!" or request.status_code == 403:
            request.close()
            return "cartellaOK", mac
        else:
            request.close()
            return "NOTregistered", mac
    else:
        request.close()
        print(request.status_code)
        return "Somethings_WRONG", mac

    #request = urequests.get('https//iot.sottosopraweb.com/casette/'+mac+"/config.txt")
    
    


def controlla_tipo_connessione():
    """Controllo che tipo di connessione ho creato al boot si sistema"""
    sta_if = network.WLAN(network.STA_IF)
    ap_if = network.WLAN(network.AP_IF)
    if sta_if.active():
        # sono connesso al router
        return "online"
    elif ap_if.active():
        # sono in AP mode
        return "AP_mode"
    else:
        # sono ne pesce ne carne
        return "UNKNOW"
   
def scarica_config(mac):
    """Ricevo il mac e faccio una requests al server nella mia cartella mac per ottenere la lettura del mio file config.txt """
    request = urequests.get('https://iot.sottosopraweb.com/casette/'+mac+'/config.txt')
    print("ho appena scaricato il file config.txt ")
    print(request.text)
    return  request.text

def accendo_spengo(config_list, pin_datiLed): 
    """Ricevo la config_list che contiene il numero dei LEd e la lista dei colori RGB e aggiorno la catenaria della striscia di led"""
    # esempio coonfig_list[0] il mio mac   ['7c:9e:bd:f8:d8:dc', [255, 255, 255], '0', '2', '8']       ogni mac contiene ['mac', [colori], 'status', 'numero figli', 'numero_LED']
    nLed = 0           # # nLed contiene il numero totale dei led (lampada principale + lampade figli) 
    # sommo il numero dei led di ogni lampada e trovo nLed
    for el in config_list:
        nLed = nLed + int(el[4])       #calcolo il totale dei led nella catenaria
    np = neopixel.NeoPixel(machine.Pin(pin_datiLed), nLed) #creo oggetto neopixel
    
    
    # ---Accendo i Led del Colore Scelto---
    contatore = 0
    for el in config_list:             #per ogni mac address
        for i in range(int(el[4])):    #per ogni elemento della catena di led di ogni lampada collegata alla catenaria
            # Coloro i led della Lampada nel colore scelto
            np[contatore] = (int(el[1][0]), int(el[1][1]), int(el[1][2]))
            # print('accendo il led numero ..', contatore)
            contatore = contatore + 1
    np.write() # PASSO IL COLORE SCELTO A TUTTI I LED
    # ---Accendo i Led del Colore Scelto---FINE----
    
    sleep(5)                    # DA ELIMINARE IN SEGUITO
    for el in range (nLed):     # setto tutto a black
        np[el] = (0, 0, 0)
    np.write()
    return True
    
    
def controllo_switch():
    """Faccio il controllo degli switch e comunico lo stato """
    pass
    return sw1, sw2
    
def segnalo_stato_al_cloud(mac, stato):
    """Ricevo il mio mac e lo stato della lampada principale poi lo comunico al server cloud"""
    api_key = 'unastringadelgenere1234'
    request = urequests.get('https://iot.sottosopraweb.com/casette/registra_mio_status.php?macadd='+mac+'&api_key='+api_key)
    if request.text == "FATTO!":
            request.close()
            return True
    return False

def leggo_stato_figlio(mac_figlio):
    """Ricevo il mac del figlio e ne controllo lo stato sul server cloud"""
    request = urequests.get('https://iot.sottosopraweb.com/casette/'+mac_figlio+'/status.txt')
    return request.text               # stato di mac_figlio

   
# Qui comincia il main         

#Area LED
#nLed = 3 # numero dei pixel disponibili  nella Lampada Principale
# il numero dei leds verra' aggiornato dopo la lettura della config_list

pin_datiLed = 27 #pin sul quale sono collegati i led fisicamente

# np = neopixel.NeoPixel(machine.Pin(pin_datiLed), nLed) #creo oggetto neopixel


# tempo intervallo tra i check online - settato di default a 30 secondi
tempo_check = 30
last_sw1 = 0
last_sw2 = 0
sw1 = 0
sw2 = 0
#controlla se sono online
if controlla_tipo_connessione() == "online" :
    stato_cartella, mac = controlla_struttura()  #controllo se esite la struttura sul sito e quindi vengo riconosciuto dal sistema
    if stato_cartella == "cartellaOK":           #se tutto ok allora prendo la configurazione definita sul server
        
        # mi prendo la configurazione registrata sul sito e converto con eval la stringa ricevuta in un dizionario, il cui unico elemento e' "conf"
        
        #config_list = eval(scarica_config(mac))['conf']

        # Gestisco la configurazione ricevuta in config_list
        
        # in questa forma  [['$macadd', [255, 255, 255], '0', '0', '10' ]]  una lista di liste che contengono ogni mac contiene ['mac', [colori], 'status', 'numero figli', 'numero_LED']
        # tutti i dati di lampada ed eventuali figli: [mac0, mac1, mac2...]  
        
        # mac0=lampada principale 
        # ogni mac contiene ['mac', [colori], 'status', 'numero figli', 'numero_LED']
        
        # Controlla ogni tempo_check lo status delle lampade
        time_marc = 0
        time_marc1 = 0
        time_marc2 = 0
        tempo_debounce = 0.03   # 300 millisecondi debounce time
        
        config_list = eval(scarica_config(mac))['conf']  # QUESTA OPERAZIONE VIENE FATTA UNA SOLA VOLTA APPENA ACCESA LA LAMPADA.
        #                                                # SE SI AGGIORNA IL CLOUD VA RESETTATA LA LAMPADA PER ACQUISIRE I NUOVI SETTAGGI
        
        # se nella config_list trovo piu' di un elemento (il primo e' sempre la lampada principale)
        # mi scarico lo status dal server del o degli elementi figlio trovati
        # ed aggiorno il config_list col nuovo status
        while True:
            # ----------------------------------controllo stato delle lampade figlio
            if (time() - time_marc) > tempo_check:
                if len(config_list) > 1:
                    for i in range(1, len(config_list)):
                        mac_fg = config_list[i][0]
                        config_list[i][2] = leggo_stato_figlio(mac_fg)      # leggo lo status del mac figlio e aggiorno lo staus nella config_list
                        # qui ho il config_list aggiornato con tutti gli status corretti.
                        #print("ho aggiornato lo status del figlio ", i)
                        #print(config_list[i][2])
                        #print(config_list)
                    accendo_spengo(config_list, pin_datiLed, agg_mac)  #comunico il config_list ed il pin a cui corrispondono i led, e anche quale macaddress voglio aggiornare
                print("Adesso aspetto ** 30 secondi **")
                print(gc.mem_free())
                time_marc = int(time())
            # ----------------------------------controllo stato delle lampade figlio----FINE 
                
            
            # Controllo stato degli switch lampada principale
            sw1, sw2 = controllo_switch()
            if sw1 != last_sw1 and (time() - time_marc1) > tempo_debounce:
                # sw1 ha cambiato di stato !
                
                sw1 = last_sw1
                time_marc1 = time()
            if sw2 != last_sw2 and (time() - time_marc2) > tempo_debounce:
                # sw2 ha cambiato di stato !
                
                sw2 = last_sw2
                time_marc1 = time()
                
                
    elif cartella == "NOTregistered":
        print(cartella)
        machine.reset()
    else:
        print(cartella)
        machine.reset()
    
elif status == "AP_mode" :
    # Sono in AP_mode e parto col server
    do_server()
    # aggiungere possibilita' di accendere e spengere la lamada anche off line
else:
    #qualcosa non funziona
    machine.reset()
    
#per ottenere il mac address   
#import network
#import ubinascii
#mac = ubinascii.hexlify(network.WLAN().config('mac'),':').decode()
#print mac
