# This file is executed on every boot (including wake-boot from deepsleep)
import esp
esp.osdebug(None)
import gc
gc.collect()

#import webrepl
#webrepl.start()
def do_connect():
    import credenziali
    import network
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print('connecting to network...')
        
        wlan.connect(credenziali.utente(), credenziali.passw())
        while not wlan.isconnected():
            pass
    print('network config:', wlan.ifconfig())

def do_AP_mode():
    import network
    
    ssid = 'CasettaBuonanotte'
    password = '123456789'

    ap = network.WLAN(network.AP_IF)
    ap.active(True)
    ap.config(essid=ssid, password=password)

    while ap.active() == False:
      pass

    print('Connection successful as AP')
    print('Connettimi al: ',ap.ifconfig())
    
filename = "credenziali.py"
try:
    f = open(filename, "r")
    # continue with the file.
    f.close()
    router = True
except OSError:  # open failed
    # handle the file open case
    router = False

if router == True:
    do_connect()
else:
    do_AP_mode()


