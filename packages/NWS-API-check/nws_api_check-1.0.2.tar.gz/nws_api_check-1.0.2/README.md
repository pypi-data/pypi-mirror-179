# Description
Checks the response from endpoints at api.weather.gov, which will be used in the next version of forecast pages. For more information, see the [API Web Service](https://www.weather.gov/documentation/services-web-api) documentation. 

## Installation
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install.

```bash
pip install NWS-API-Check -t targetDirectory/
```

## Usage
```bash
python api.py
```

## Input
The user is asked to choose between testing the development, QA/preview, or production URL.

## Prerequisites
* Python 3 
* Install modules: datetime, json, pytz, requests, urllib

## License

[MIT](https://choosealicense.com/licenses/mit/)
