import IP2Location
import IP2Proxy
import ipaddress
import json
import os

def handler(event, context):

    try:

        ip = ipaddress.ip_address(event['rawQueryString'])
        ip = str(event['rawQueryString'])

    except ValueError:

        ip = ipaddress.ip_address(event['requestContext']['http']['sourceIp'])
        ip = str(event['requestContext']['http']['sourceIp'])

    if '.' in ip:

        asndb = IP2Location.IP2Location('IP2LOCATION-LITE-ASN.BIN')
        asn = asndb.get_all(ip)

        ipdb = IP2Location.IP2Location('IP2LOCATION-LITE-DB11.BIN')
        db = ipdb.get_all(ip)

        f = open('DBASNLITEBIN.updated', 'r')
        asnupdated = f.read()
        f.close()

        f = open('DB11LITEBIN.updated', 'r')
        dbupdated = f.read()
        f.close()

    if ':' in ip:

        asndb = IP2Location.IP2Location('IP2LOCATION-LITE-ASN.IPV6.BIN')
        asn = asndb.get_all(ip)

        ipdb = IP2Location.IP2Location('IP2LOCATION-LITE-DB11.IPV6.BIN')
        db = ipdb.get_all(ip)

        f = open('DBASNLITEBINIPV6.updated', 'r')
        asnupdated = f.read()
        f.close()

        f = open('DB11LITEBINIPV6.updated', 'r')
        dbupdated = f.read()
        f.close()

    proxydb = IP2Proxy.IP2Proxy()
    proxydb.open('IP2PROXY-LITE-PX12.BIN')
    proxy = proxydb.get_all(ip)
    proxydb.close()

    print(asn)
    print(db)
    print(proxy)

    f = open('PX12LITEBIN.updated', 'r')
    proxyupdated = f.read()
    f.close()

    desc = 'The lukach.io API uses the IP2Location LITE database for IP geolocation from https://lite.ip2location.com.'

    code = 200
    msg = {
        'ip':str(ip),
        'asn': asn,
        'db': db,
        'proxy': proxy,
        'attribution':desc,
        'IP2LOCATION-LITE-ASN':asnupdated,
        'IP2LOCATION-LITE-DB11':dbupdated,
        'IP2PROXY-LITE-PX12':proxyupdated,
        'region': os.environ['AWS_REGION']
    }

    return {
        'statusCode': code,
        'body': json.dumps(msg, indent = 4)
    }