# Anyside Python API

Welcome to the Anyside Python API!<br />
[Node.js API](https://www.npmjs.com/package/anyside)

In order to use the Anyside API you will need an API key. You can get your API key by creating an account on [anyside.com](https://anyside.com/).

## Installation

To install the Python API and get started you can simply pip install Anyside into your project.

```sh
$ pip install Anyside
```

## Query Domain

When making a request must pass a anyside domain name.

Response will contain wallest connected with anyside

```python
from anyside import Anyside

anyside = Anyside(api_key='YOUR API KEY')

domain = anyside.query_domain(domain="QUERY DOMAIN NAME Eg. John.any")
print(domain)

"""
#Response Example:
{'Bitcoin': [{'address': '0xBTC-SOMESTUFF', 'name': 'Bitcoin'}],
 'Solana': [{'address': '0x...', 'name': 'Solana'}]}
"""
```

## Wallet lookup
When making a request must pass a vaild wallet address.

Response will contain anyside domain

```python
from anyside import Anyside

anyside = Anyside(api_key='YOUR API KEY')

lookupWallet = anyside.lookup_wallet(wallet_address="0xaeA38149566430Anyside7321B04Anyside")
print(lookupWallet)

"""
#Response Example:
{'domain': 'John.any'}
"""
```
Please subscribe on [Anyside](https://anyside.com/) to receive project updates.
You can aslo follow us on [Twitter](https://twitter.com/AnysideNames) and [Discord](https://discord.com/invite/MKDBhDEtUn).
