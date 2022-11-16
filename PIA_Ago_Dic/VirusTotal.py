import requests
import time
import json
import pandas

def VirusTotal():
    domain_CSV = pandas.read_csv('urls.csv', header=0)
    Urls = domain_CSV['Dominios'].tolist()

    API_key = '4b0f4c0910761c7abe0d0b60cf57151363f46a2a8bd3f1187e597917a28dc899000000'
    url = 'https://www.virustotal.com/vtapi/v2/url/report'


    parameters = {'apikey': API_key, 'resource': Urls}

    for i in Urls:
        parameters = {'apikey': API_key, 'resource': i}

        response= requests.get(url=url, params=parameters)
        json_response= json.loads(response.text)
        
        if json_response['response_code'] <= 0:
            with open('resultados no encontrados.txt', 'a')  as notfound:
                notfound.write(i) and notfound.write("\t NO HA SIDO POSIBLE ESCANEARLO\n")
        elif json_response['response_code'] >= 1:

            if json_response['positives'] <= 0:
                with open('Virustotal Resultados Amigables.txt', 'a')  as clean:
                    clean.write(i) and clean.write("\t DOMINIO LIMPIO \n")
            else:
                with open('Virustotal Resultados Maliciosos.txt', 'a')  as malicious:
                    malicious.write(i) and malicious.write("\t Malicious") and malicious.write("\t DOMINIO MALICIOSO   "+ str(json_response['positives']) + "  Solutions\n")
        print('se ha analizado una url')
        time.sleep(15)