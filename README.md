# open-mappers

Shipping providers and data structures mappers.
The project goal is to offer a unified interface (API) for different shipping providers.

**Note: This project is the first draft version shared as Open Source.**

**Note:** Written with Python 3

## You can play with it

### Installation

```shell
  pip install --process-dependency-links -e git://github.com/OpenShip/open_mappers.git#egg=open_mappers
```

Use DHL mapper and providers to send rate request

```python
from open_mappers.mappers.dhl.dhl_client import  DHLClient
from open_mappers.mappers.dhl.dhl_provider import initProvider
from open_mappers.domain import entities as E

dhlClient = DHLClient(
  "https://xmlpi-ea.dhl.com/XMLShippingServlet",
  "YOUR_DHL_SITE_ID",
  "YOUR_DHL_SITE_PASSWORD",
  "YOUR_DHL_ACCOUNT_NUMBER"
)

dhlProvider = initProvider(dhlClient)

shipper = {"Address": {"PostalCode":"H3N1S4", "CountryCode":"CA"}}
recipient = {"Address": {"City":"Lome", "CountryCode":"TG"}}
shipmentDetails = {"Packages": [{"Id":"1", "Height":3, "Lenght":10, "Width":3,"Weight":4.0}]}

quoteRequest = E.createQuoteRequest(
  Shipper=shipper,
  Recipient=recipient,
  ShipmentDetails=shipmentDetails
)

request = dhlProvider.mapper.quote_request(quoteRequest)
response = dhlProvider.get_quotes(request)

quotes = dhlProvider.mapper.quote_response(response)

print(E.jsonify(quotes))
# -->
#[
#    [ --> Quote list
#        {
#            "BaseCharge": 195.32,
#            "Discount": 0,
#            "DutiesAndTaxes": 0,
#            "ExtraCharges": [
#                {
#                    "Name": "FUEL SURCHARGE",
#                    "Value": 10.74
#                }
#            ],
#            "Provider": "DHL",
#            "ServiceName": "EXPRESS WORLDWIDE DOC",
#            "ServiceType": "TD",
#            "TotalCharge": 206.06
#        }
#    ],
#    [] --> Error list
#]

```

Use Fedex mapper and providers to send rate request

```python
from open_mappers.mappers.fedex.fedex_client import  FedexClient
from open_mappers.mappers.fedex.fedex_provider import initProvider
from open_mappers.domain import entities as E

fedexClient = FedexClient(
  "https://wsbeta.fedex.com:443/web-services",
  "FEDEX_USER_KEY",
  "FEDEX_PASSWORD",
  "FEDEX_ACCOUNT_NUMBER",
  "FEDEX_METER_NUMBER"
)

fedexProvider = initProvider(fedexClient)

shipper = {"Address": {"PostalCode":"H3N1S4", "CountryCode":"CA"}}
recipient = {"Address": {"City":"Lome", "CountryCode":"TG"}}
shipmentDetails = {"Packages": [{"Id":"1", "Height":3, "Lenght":10, "Width":3,"Weight":4.0}]}

quoteRequest = E.createQuoteRequest(
  Shipper=shipper,
  Recipient=recipient,
  ShipmentDetails=shipmentDetails
)

request = fedexProvider.mapper.quote_request(quoteRequest)
response = fedexProvider.get_quotes(request)

quotes = fedexProvider.mapper.quote_response(response)

```

TODOS:

- Add more features coverage to providers mappers
- Error handling for xml responses from providers

Contributions are welcome.