#Netsparker_Technologies.py    
#@package   Netsparker_Rest_API
#@author    Samy Younsi (Shino Corp') <samyyounsi@hotmail.fr>
#@license   MIT License (http://www.opensource.org/licenses/mit-license.php)
#@link      https://github.com/ShinoNoNuma/Netsparker-Rest-API
#@docs      https://www.netsparkercloud.com/docs/index#/Technologies

import requests
import json

class Technologies(object):
    '''
      Gets the list of technologies that currently in use.
    '''
    def list(credentials, data):
      endpoint_url = credentials["API_ROOT"] % "technologies/list" + "?" + "webSiteName=" + data["webSiteName"] + "&technologyName=" + data["technologyName"] + "&page=" + data["page"] + "&pageSize=" + data["pageSize"]
      response = requests.get(endpoint_url, auth=(credentials["USER_ID"], credentials["API_TOKEN"]))
      json_response = response.json()
      return json_response

    '''
      Gets the list of out-of-date technologies that currently in use.
    '''   
    def outofdatetechnologies(credentials, data):
      endpoint_url = credentials["API_ROOT"] % "technologies/outofdatetechnologies" + "?" + "webSiteName=" + data["webSiteName"] + "&technologyName=" + data["technologyName"] + "&page=" + data["page"] + "&pageSize=" + data["pageSize"]
      response = requests.get(endpoint_url, auth=(credentials["USER_ID"], credentials["API_TOKEN"]))
      json_response = response.json()
      return json_response