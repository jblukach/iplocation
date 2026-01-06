# iplocation

## Overview

`iplocation` provides a lightweight, API-driven IP intelligence service built on top of **IP2Location LITE** and **IP2Proxy LITE** databases. It delivers IP geolocation, ASN metadata, and proxy detection in a single, consistent JSON response, suitable for security analytics, observability pipelines, enrichment workflows, and application-level decision making.

The service is exposed via a simple HTTP endpoint and is designed to be fast, cache-friendly, and easy to integrate into both serverless and traditional workloads.

---

## 1. IP2LOCATION-LITE-ASN.BIN and IP2LOCATION-LITE-ASN.IPV6.BIN

These databases provide **Autonomous System Number (ASN)** intelligence for both IPv4 and IPv6 addresses.

Included attributes:

- ASN number
- Autonomous System name
- ISP / organization metadata
- Usage type and network categorization (where available)

This data is useful for:

- Network attribution
- Traffic source analysis
- Security investigations
- Observability enrichment

Both IPv4 and IPv6 binaries are supported to ensure full dual-stack coverage.

---

## 2. IP2LOCATION-LITE-DB11.BIN and IP2LOCATION-LITE-DB11.IPV6.BIN

These databases provide **geographic IP intelligence** for IPv4 and IPv6 addresses.

Included attributes:

- Country (short and long name)
- Region / state
- City
- Latitude and longitude
- ZIP / postal code
- Timezone

Common use cases:

- Geo-based routing
- Localization
- Compliance reporting
- Monitoring and analytics dashboards

IPv6 parity is maintained to ensure consistent results across modern networks.

---

## 3. IP2PROXY-LITE-PX12.BIN

The IP2Proxy LITE PX12 database is used for **proxy and anonymity detection**.

Capabilities include:

- Proxy presence detection (`is_proxy`)
- Proxy type classification
- Known proxy and hosting provider indicators
- Threat and fraud-related metadata (where available)

This data is commonly used for:

- Fraud prevention
- Abuse detection
- Rate limiting and access control
- Security signal enrichment

---

## 4. Integrated IP Intelligence Workflows

`iplocation` combines **geolocation**, **ASN intelligence**, and **proxy detection** into a single response to simplify downstream processing.

Benefits of the integrated approach:

- One API call instead of multiple lookups
- Consistent schema across data sources
- Easier ingestion into logs, metrics, and traces
- Ideal for serverless, SIEM, and observability platforms

### Sample Response

```json
{
  "ip": "134.129.111.111",
  "geo": {
    "country_short": "US",
    "country_long": "United States of America",
    "region": "North Dakota",
    "city": "Fargo",
    "latitude": "46.877190",
    "longitude": "-96.789803",
    "zip": "58105",
    "timezone": "-06:00"
  },
  "asn": {
    "asn": "19530",
    "as_name": "State of North Dakota Itd"
  },
  "proxy": {
    "is_proxy": 0,
    "proxy_type": "-"
  }
}
```

---

## 5. How to use

### HTTP API

Perform a lookup by issuing a GET request with an IP address:

```bash
curl "https://api.lukach.io/geo/ip2location?134.129.111.111"
```

The API returns a structured JSON document containing:

- `geo` — geographic location data
- `asn` — autonomous system information
- `proxy` — proxy and anonymity indicators
- `attribution` — data source attribution
- Database build timestamps

### Application Integration

The API can be integrated into:

- Lambda functions and serverless pipelines
- Log enrichment (CloudWatch, OpenSearch, SIEMs)
- Security tooling
- Custom applications and APIs

Because the output is JSON, it is compatible with most languages and frameworks without additional parsing libraries.

---

## 6. References

- IP2Location Python SDK – Quick Start  
  https://ip2location-python.readthedocs.io/en/latest/quickstart.html

- IP2Proxy Python SDK – Quick Start  
  https://ip2proxy-python.readthedocs.io/en/latest/quickstart.html

- IP2Location LITE Databases  
  https://lite.ip2location.com

---

## Conclusion

`iplocation` offers a simple, unified way to enrich IP addresses with **location**, **network ownership**, and **proxy intelligence** using trusted IP2Location LITE data sources. By exposing this information through a single API endpoint, it reduces complexity while enabling powerful security, observability, and analytics use cases.

This project is ideal for teams looking for a lightweight, transparent, and easily extensible IP intelligence solution.
