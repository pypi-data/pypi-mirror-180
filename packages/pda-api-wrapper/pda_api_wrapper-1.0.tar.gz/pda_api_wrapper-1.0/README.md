# PDA API Wrapper

- Python wrapper for the PowerDNS Administrator (PDA) API

## Installation

```bash
pip install pda_api_wrapper
```

## Usage

```py
from pda_api_wrapper import PDAAPI

# initialize the API wrapper with the base URL, user and password
pda = PDAAPI(base_url='http://localhost:9191', user='admin', password='admin')

# create a domain
response = pda.create_domain(name='yourdomain.com.', kind='NATIVE', nameservers=['ns1.mydomain.com.'])
print(response)

# create an API key with administrator permissions
response = pda.create_apikey(description='masterkey', domains=[], role='Administrator')
print(response)

# get the PowerDNS configuration
response = pda.get_config()
print(response)

# sync domains using the API key
response = pda.sync_domains(key='YUdDdGhQM0tMQWV5alpJ')
print(response)

# get the list of accounts
response = pda.get_powerdnsadmin('accounts')
print(response)
```

## License

- This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
