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

    f = open('PX12LITEBIN.updated', 'r')
    proxyupdated = f.read()
    f.close()

    desc = 'The lukach.io API uses the IP2Location LITE database for IP geolocation from https://lite.ip2location.com.'

    code = 200
    msg = {
        'ip':str(ip),
        'geo': {
            'country_short':db.country_short,
            'country_long':db.country_long,
            'region':db.region,
            'city':db.city,
            'latitude':db.latitude,
            'longitude':db.longitude,
            'zip':db.zipcode,
            'timezone':db.timezone
        },
        'asn': {
            'asn':asn.asn, 
            'as_name': asn.as_name,
            'as_domain': asn.as_domain,
            'as_usagetype': asn.as_usagetype,
            'as_cidr': asn.as_cidr,
            'country_short': asn.country_short,
            'country_long': asn.country_long,
            'region': asn.region,
            'city': asn.city,
            'isp': asn.isp,
            'latitude': asn.latitude,
            'longitude': asn.longitude,
            'domain': asn.domain,
            'zipcode': asn.zipcode,
            'timezone': asn.timezone,
            'netspeed': asn.netspeed,
            'idd_code': asn.idd_code,
            'area_code': asn.area_code,
            'weather_code': asn.weather_code,
            'weather_name': asn.weather_name,
            'mcc': asn.mcc,
            'mnc': asn.mnc,
            'mobile_brand': asn.mobile_brand, 
            'elevation': asn.elevation,
            'usage_type': asn.usage_type,
            'address_type': asn.address_type,
            'category': asn.category,
            'district': asn.district
        },
        'proxy': {
            'is_proxy': proxy['is_proxy'],
            'proxy_type': proxy['proxy_type'],
            'country_short': proxy['country_short'],
            'country_long': proxy['country_long'],
            'region': proxy['region'],
            'city': proxy['city'],
            'isp': proxy['isp'],
            'domain': proxy['domain'],
            'usage_type': proxy['usage_type'],
            'asn': proxy['asn'],
            'as_name': proxy['as_name'],
            'last_seen': proxy['last_seen'],
            'threat': proxy['threat'],
            'provider': proxy['provider'],
            'fraud_score': proxy['fraud_score']
        },
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