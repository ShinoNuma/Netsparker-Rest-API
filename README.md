
# A REST interface to Netsparker
[![PyPI Version](https://badge.fury.io/py/nessrest.svg)](https://pypi.python.org/pypi/netsparker_rest_api)
### Dependencies:

* Netsparker Team or Enterprise License (Not working with standard license)
* Python 3.3+
* requests module (install via pip)
* The dependencies can be satisfied via `pip install -r requirements.txt`

### Quick Install
```
pip install netsparker_rest_api
```
### API Documentations:
```
https://www.netsparkercloud.com/docs/index
```
### Some examples:

* Get your account information.

```python 
  from Netsparker_Rest_API import Netsparker_Account
  
  credentials = {
  "API_ROOT": "https://www.netsparkercloud.com/api/1.0/%s",
  "USER_ID": "NETSPARKER CLOUD API USER_ID GOES HERE",
  "API_TOKEN": "NETSPARKER CLOUD API API_TOKEN GOES HERE"
  }
  
  my_info = Netsparker_Account.Account.me(credentials)
  print(my_info)
```

* Schedules a scan to be launched in the future.

```python
  from Netsparker_Rest_API import Netsparker_Scans
  
  credentials = {
  "API_ROOT": "https://www.netsparkercloud.com/api/1.0/%s",
  "USER_ID": "NETSPARKER CLOUD API USER_ID GOES HERE",
  "API_TOKEN": "NETSPARKER CLOUD API API_TOKEN GOES HERE"
  }

  data = {
  "Name": "Scheduled Scan-1",
  "NextExecutionTime": "15/05/2020 10:20 PM",
  "ScheduleRunType": "Weekly",
  "CustomRecurrence": {
    "RepeatType": "Weeks",
    "Interval": 1,
    "EndingType": "Never",
    "DaysOfWeek": [
      "Friday"
    ],
    "EndOn": "21/07/2022 10:42 PM"
  },
  "TargetUri": "http://php.testsparker.com/",
  "Cookies": "name1=value1; name2=value2",
  "CrawlAndAttack": "true",
  "EnableHeuristicChecksInCustomUrlRewrite": "true",
  }

  schedule_scan = Netsparker_Scans.Scans.schedule(credentials, data)
  print(schedule_scan)
```

* Returns the custom report of a scan in the specified format.

```python
  from Netsparker_Rest_API import Netsparker_Scans
  
  credentials = {
  "API_ROOT": "https://www.netsparkercloud.com/api/1.0/%s",
  "USER_ID": "NETSPARKER CLOUD API USER_ID GOES HERE",
  "API_TOKEN": "NETSPARKER CLOUD API API_TOKEN GOES HERE"
  }
  
  data = {
  "id": "8705818b4fc644a33957ab9c01765d06",
  "reportName": "ScheduledScan-1Report ",
  "onlyConfirmedVulnerabilities": "false",
  "excludeIgnoreds": "false",
  "reportFormat": "Json"
  }
  
  report_csv = Netsparker_Scans.Scans.custom_report(credentials, data)
  print(report_csv)
```

### Building modules:

* To build a package to install via `pip` or `easy_install`, execute:
    * `python setup.py sdist`
* The resulting build will be in `$PWD/dist/Netsparker_Rest_API-<version>.tar.gz`
