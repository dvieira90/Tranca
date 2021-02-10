import urequests, json, network, utime, mfrc522

SSID = 'IoT'
PASSWD = '42375011'
URLS = 'http://10.0.1.196:5000'

class Porta:
    def __init__(self, porta):
        self.nome = porta['porta']
        self.users = porta['users']

    def tags(self):
        lista = []
        for i in self.users:
            lista = lista + i['tags']
        return lista

    def nome_porta(self):
        return self.nome

    def usuarios(self):
        lista = []
        for i in self.users:
            lista.append(i['nome'])
        return lista

    def __str__(self):
        return "Porta: {} \nUsuarios: {}\nTags:{}".format(self.nome, self.usuarios(), self.tags())

sta_if = network.WLAN(network.STA_IF)
#Metodo que faz a conexão com o WiFi
def do_connect():
    print('conectanto a rede....')
    sta_if.active(True)
    sta_if.connect(SSID, PASSWD)

def do_read():
    try:
        uid_tag = "none"

        rdr = mfrc522.MFRC522(sck=2, mosi=0, miso=4, rst=14, cs=5)


        (stat, tag_type) = rdr.request(rdr.REQIDL)

        if stat == rdr.OK:

            (stat, raw_uid) = rdr.anticoll()

            if stat == rdr.OK:

                uid_tag = str(raw_uid[0]) + str(raw_uid[1]) + str(raw_uid[2]) + str(raw_uid[3])
        return uid_tag

    except Exception as e:
        return e

#Metodo que faz uma chamada GET ao servidor para obter o codigo de trabalho especificando qual porta
def get_code(url):
    try:
        response = urequests.get("{}{}?porta=cercomp".format(URLS, url))
        parsed = response.json()
        return parsed['code']
    except:
        return 'erro'

#Metodo que faz uma chamada GET ao servidor para obter o usuarios do servidor e suas tags
def get_users(url):
    try:
        response = urequests.get("{}{}?porta=cercomp".format(URLS, url))
        obj = response.json()
        return obj
    except:
        return 'erro'

#Metodo que faz uma chamada GET ao servidor para obter as URLs de trabalho
def get_url():
    try:
        response = urequests.get(URLS)        
        obj = response.json()
        return obj
    except:
        return 'erro'