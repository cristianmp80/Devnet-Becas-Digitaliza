import os
import sys
import json
import requests
from tabulate import *
requests.packages.urllib3.disable_warnings()

# Obtiene un ticket

def get_ticket():

    api_url = "https://devnetsbx-netacad-apicem-3.cisco.com/api/v1/ticket"
    headers = {"content-type": "application/json"}
    body_json = {
    "password": "Xj3BDqbU",
    "username": "devnetuser"
    }

    resp = requests.post(api_url,json.dumps(body_json),headers=headers,verify=False)
    #print("Ticket request status: ", resp.status_code)
    response_json = resp.json()

    serviceTicket = response_json["response"]["serviceTicket"]
    print("The service ticket number is: ", serviceTicket)

    return serviceTicket


# Nos devuelve una lista de los hosts de la red

def print_hosts():
    api_url = "https://devnetsbx-netacad-apicem-3.cisco.com/api/v1/host"
    ticket = get_ticket()
    headers = {"content-type": "application/json", "X-Auth-Token": ticket}

    resp = requests.get(api_url, headers=headers, verify=False)
    print("Status of /host request: ", resp.status_code)

    if resp.status_code != 200:
        raise Exception("Status code does not equal 200. Response text: " + resp.text)

    response_json = resp.json()

    host_list = []
    i = 0

    for item in response_json["response"]:
        i += 1
        host = [ i, item["hostType"], item["hostIp"] ]
        host_list.append( host )

    table_header = ["Number", "Type", "IP"]
    print( tabulate(host_list, table_header) )


# Nos devuelve una lista de los dispositivos de red

def print_devices():
    api_url = "https://devnetsbx-netacad-apicem-3.cisco.com/api/v1/network-device"
    ticket = get_ticket()
    headers = {"content-type": "application/json", "X-Auth-Token": ticket}

    resp = requests.get(api_url, headers=headers, verify=False)
    print("Status of /host request: ", resp.status_code)

    if resp.status_code != 200:
        raise Exception("Status code does not equal 200. Response text: " + resp.text)

    response_json = resp.json()

    dev_list = []
    i = 0

    for item in response_json["response"]:
        i += 1
        dev = [ i, item["family"], item["type"], item["managementIpAddress"] ]
        dev_list.append( dev )

    table_header = ["Number", "Family", "Type", "Mngmt IP"]
    print( tabulate(dev_list, table_header) )


# Nos devuelve una lista de pools de direcciones ip creados

def print_pools():
    api_url = "https://devnetsbx-netacad-apicem-3.cisco.com/api/v1/ippool"
    ticket = get_ticket()
    headers = {"scope": "ALL", "X-Auth-Token": ticket}

    resp = requests.get(api_url, headers=headers, verify=False)
    print("Status of /host request: ", resp.status_code)

    if resp.status_code != 200:
        raise Exception("Status code does not equal 200. Response text: " + resp.text)

    response_json = resp.json()

    pool_list = []
    i = 0

    for item in response_json["response"]:
        i += 1
        pool = (i, item["apicAppName"], item["ipPool"], item["startAddress"], item["endAddress"], item["nextAddress"], item["freeIpCount"])
        pool_list.append(pool)

    table_header = ["Number", "Pool Name", "Network", "Start Adress", "End Adress", "Next Address", "Free Ips"]
    print(tabulate(pool_list, table_header))



# Nos devuelve una lista de segmentos wireless

def print_wireless():
    api_url = "https://devnetsbx-netacad-apicem-3.cisco.com/api/v1/segment?type=wireless"
    ticket = get_ticket()
    headers = {"X-Auth-Token": ticket}

    resp = requests.get(api_url, headers=headers, verify=False)
    print("Status of /host request: ", resp.status_code)

    if resp.status_code != 200:
        raise Exception("Status code does not equal 200. Response text: " + resp.text)

    response_json = resp.json()

    wireless_list = []
    i = 0

    for item in response_json["response"]:
        i += 1
        devices = []
        for x in item["networkDevices"]:
            dev = x["hostName"]
            devices.append(dev)
        segment = [i, item["name"], devices]
        wireless_list.append(segment)

    table_header = ["Number", "Segment Name", "Devices Connected"]
    print(tabulate(wireless_list, table_header))



while True:
    if os.name == "posix":
        os.system ("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system ("cls")
    print("----------------------- MENU -----------------------")
    print("")
    print(" 1. Obtener una lista de hosts")
    print(" 2. Obtener una lista de dispositivos de red")
    print(" 3. Obtener una lista de pools de direcciones ip")
    print(" 4. Obtener una lista de segmentos wireless")
    print(" 0. Salir")
    print("----------------------------------------------------")
    print("")
    opciones = {"1":print_hosts, "2":print_devices, "3":print_pools, "4":print_wireless}
    op = input("Elija una opción: ")
    if op == "0":
        break
    
    try:
        opciones[op]()
        input("\n\nPulse INTRO para continuar...")
    except:
        input("\n\nOpcion inválida, pulse INTRO para continuar...")




