import getssid
import wifi_connect

ssid = ""
#the condition may be change to ssid != "ESSID"
while( ssid == "" ):
    wifi_connect.connectTo("DJAWEB_8108","youcef1998bnd","wlp2s0")
    ssid = getssid.getSSID()
print("connected to",ssid,"!")
