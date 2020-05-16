#Netsparker_AuditLogs.py    
#@package   Netsparker_Rest_API
#@author    Samy Younsi (Shino Corp') <samyyounsi@hotmail.fr>
#@license   MIT License (http://www.opensource.org/licenses/mit-license.php)
#@link      https://github.com/ShinoNoNuma/Netsparker-Rest-API
#@docs      https://www.netsparkercloud.com/docs/index#/AuditLogs

import requests
import json

class AuditLogs(object):
    '''
    Returns the selected log type in the csv format as a downloadable file.
    '''
    def list(credentials, data):
      endpoint_url = credentials["API_ROOT"] % "auditlogs/export" + "?" + "page=" + data["page"] + "&pageSize=" + data["pageSize"] + "&csvSeparator=" + data["csvSeparator"] + "&startDate=" + data["startDate"] + "&endDate=" + data["endDate"]
      response = requests.get(endpoint_url, auth=(credentials["USER_ID"], credentials["API_TOKEN"]))
      json_response = response.json()
      return json_response