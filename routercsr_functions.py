import os
import json
import requests
from ncclient import manager
import xml.dom.minidom
import xmltodict
from tabulate import *
from netmiko import ConnectHandler

requests.packages.urllib3.disable_warnings()




def print_interfaces():
    api_url = "https://192.168.56.102/restconf/data/ietf-interfaces:interfaces"
    headers = { "Accept": "application/yang-data+json", "Content-type":"application/yang-data+json"}
    basicauth = ("cisco", "cisco123!")

    resp = requests.get(api_url, auth=basicauth, headers=headers, verify=False)
    response_json = resp.json()
    interface_list = []
    n = 0
    for item in response_json["ietf-interfaces:interfaces"]["interface"]:
        n += 1
        if "address" in item["ietf-ip:ipv4"]:
            interface = [n, item["name"], item["ietf-ip:ipv4"]["address"][0]["ip"]]
        else:
            interface = [n, item["name"], ""]
        interface_list.append(interface)

    api_url = "https://192.168.56.102/restconf/data/ietf-interfaces:interfaces-state"
    resp = requests.get(api_url, auth=basicauth, headers=headers, verify=False)
    response_json = resp.json()
    mac_list = []
    n = 0
    for item in response_json["ietf-interfaces:interfaces-state"]["interface"]:
        interface_list[n].append(item["phys-address"])
        n += 1

    table_header = ["Num", "Interface Name", "IP Address", "MAC Address"]
    print("\nInterfaces:\n")
    print(tabulate(interface_list, table_header))



def crear_interfaz():
    n = input("\nDame el numero de interfaz de loopback que quieras crear: ")
    ip_addr = input("Dame su dirección ip: ")
    netmask = input("Dame su máscara de red: ")
    desc = input("Dame su descripción: ")

    sshCli = ConnectHandler(device_type="cisco_ios", host="192.168.56.102", port=22, username="cisco", password="cisco123!")

    direccionamiento = "ip address " + ip_addr + " " + netmask
    list_commands = ["interface loopback " + n, direccionamiento, "description " + desc]

    output = sshCli.send_config_set(list_commands)
    print("Config output from the device: \n{}\n".format(output))



def borrar_interfaz(interfaz):
    api_url = "https://192.168.56.102/restconf/data/ietf-interfaces:interfaces/interface=Loopback" + interfaz
    headers = {"Accept": "application/yang-data+json", "Content-type":"application/yang-data+json"}
    basicauth = ("cisco", "cisco123!")

    resp = requests.delete(api_url, auth=basicauth, headers=headers, verify=False)

    if (resp.status_code >= 200 and resp.status_code <= 299):
        print("STATUS OK: {}".format(resp.status_code))
    else:
        print("Error code {}, reply: {}".format(resp.status_code, resp.json()))
    


def borrar_interfaces():
    print_interfaces()
    n = input("\nElige la interfaz loopback que quieres borrar: ")
    borrar_interfaz(n)

    

def routing():
    api_url = "https://192.168.56.102/restconf/data/ietf-routing:routing"
    headers = { "Accept": "application/yang-data+json", "Content-type":"application/yang-data+json"}
    basicauth = ("cisco", "cisco123!")

    resp = requests.get(api_url, auth=basicauth, headers=headers, verify=False)
    response_json = resp.json()

    route_list = []
    n = 0
    for item in response_json["ietf-routing:routing"]["routing-instance"][0]["routing-protocols"]["routing-protocol"][0]["static-routes"]["ietf-ipv4-unicast-routing:ipv4"]["route"]:
        n += 1
        if "outgoing-interface" in item["next-hop"] and "next-hop-address" in item["next-hop"]:
            route = [n, "Static", item["destination-prefix"], item["next-hop"]["next-hop-address"], item["next-hop"]["outgoing-interface"]]
        elif "next-hop-address" in item["next-hop"]:
            route = [n, "Static", item["destination-prefix"], item["next-hop"]["next-hop-address"], ""]
        elif "outgoing-interface" in item["next-hop"]:
            route = [n, "Static", item["destination-prefix"], "", item["next-hop"]["outgoing-interface"]]
        else:
            route = [n, "Static", item["destination-prefix"], "", ""]
        route_list.append(route)

    table_header = ["Num", "Tipo de Ruta", "Red Destino", "Siguiente Salto", "Interfaz de Salida"]
    print("\nTabla de Rutas:\n")
    print(tabulate(route_list, table_header))




while True:
    if os.name == "posix":
        os.system ("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system ("cls")
    print("----------------------- MENU -----------------------")
    print("")
    print(" 1. Listar interfaces.")
    print(" 2. Crear interfaz.")
    print(" 3. Borrar interfaz.")
    print(" 4. Tabla de routing.")
    print(" 0. Salir")
    print("----------------------------------------------------")
    print("")
    opciones = {"1":print_interfaces, "2":crear_interfaz, "3":borrar_interfaces, "4":routing}
    op = input("Elija una opción: ")
    if op == "0":
        break
   
    try:
        opciones[op]()
        input("\n\nPulse INTRO para continuar...")
    except:
        input("\n\nOpcion inválida, pulse INTRO para continuar...")