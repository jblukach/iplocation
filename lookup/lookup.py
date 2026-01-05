import IP2Location
import ipaddress
import json
import os

def handler(event, context):

    try:

        try:
            ip = ipaddress.ip_address(event['rawQueryString'])
            ip = str(event['rawQueryString'])
        except ValueError:
            ip = ipaddress.ip_address(event['requestContext']['http']['sourceIp'])
            ip = str(event['requestContext']['http']['sourceIp'])

        asnipv4db = IP2Location.IP2Location('IP2LOCATION-LITE-ASN.BIN')
        asnipv6db = IP2Location.IP2Location('IP2LOCATION-LITE-ASN.IPV6.BIN')
        cityipv4db = IP2Location.IP2Location('IP2LOCATION-LITE-DB11.BIN')
        cityipv6db = IP2Location.IP2Location('IP2LOCATION-LITE-DB11.IPV6.BIN')
        proxydb = IP2Location.IP2Location('IP2PROXY-LITE-PX12.BIN')
        
        asnipv4 = asnipv4db.get_all(ip)
        asnipv6 = asnipv6db.get_all(ip)
        cityipv4 = cityipv4db.get_all(ip)
        cityipv6 = cityipv6db.get_all(ip)
        proxyaddr = proxydb.get_all(ip)

        f = open('DBASNLITEBIN.updated', 'r')
        asnipv4updated = f.read()
        f.close()

        f = open('DBASNLITEBINIPV6.updated', 'r')
        asnipv6updated = f.read()
        f.close()

        f = open('DB11LITEBIN.updated', 'r')
        cityipv4updated = f.read()
        f.close()

        f = open('DB11LITEBINIPV6.updated', 'r')
        cityipv6updated = f.read()
        f.close()

        f = open('PX12LITEBIN.updated', 'r')
        proxyupdated = f.read()
        f.close()

        desc = 'The lukach.io API uses the IP2Location LITE database for IP geolocation from https://lite.ip2location.com.'

        code = 200
        msg = {
            'ip':str(ip),
            'asn ipv4': asnipv4,
            'asn ipv6': asnipv6,
            'city ipv4': cityipv4,
            'city ipv6': cityipv6,
            'proxy': proxyaddr,
            'attribution':desc,
            'IP2LOCATION-LITE-ASN.BIN':asnipv4updated,
            'IP2LOCATION-LITE-ASN.IPV6.BIN':asnipv6updated,
            'IP2LOCATION-LITE-DB11.BIN':cityipv4updated,
            'IP2LOCATION-LITE-DB11.IPV6.BIN':cityipv6updated,
            'IP2PROXY-LITE-PX12.BIN':proxyupdated,
            'region': os.environ['AWS_REGION']
        }

    except:
        code = 404
        msg = 'Invalid IP Address'
        pass

    return {
        'statusCode': code,
        'body': json.dumps(msg, indent = 4)
    }