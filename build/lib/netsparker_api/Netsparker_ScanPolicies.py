#Netsparker_ScanPolicies.py    
#@package   Netsparker_Rest_API
#@author    Samy Younsi (Shino Corp') <samyyounsi@hotmail.fr>
#@license   MIT License (http://www.opensource.org/licenses/mit-license.php)
#@link      https://github.com/ShinoNoNuma/Netsparker-Rest-API
#@docs      https://www.netsparkercloud.com/docs/index#/ScanPolicies


import requests
import json

class ScanPolicies(object):
    '''
    Deletes a scan policy.
    '''
    def delete(credentials, data):
      endpoint_url = credentials["API_ROOT"] % "scanpolicies/delete"
      json_data = json.dumps(data)
      response = requests.post(endpoint_url, headers={'Content-Type':'application/json'}, data=json_data, auth=(credentials["USER_ID"], credentials["API_TOKEN"]))
      json_response = response.json()
      return json_response

    '''
    Gets the scan policy by the specified name / Gets the scan policy by the specified id.
    '''
    def get(credentials, data):
      if "name" in data :
        endpoint_url = credentials["API_ROOT"] % "scanpolicies/get" + "?" + "name=" + data["name"]
      else :
        endpoint_url = credentials["API_ROOT"] % "scanpolicies/get" + "/" + data["id"]
      response = requests.get(endpoint_url, auth=(credentials["USER_ID"], credentials["API_TOKEN"]))
      json_response = response.json()
      return json_response

    '''
    Gets the list of scan policies.
    '''
    def list(credentials, data):
      endpoint_url = credentials["API_ROOT"] % "scanpolicies/list" + "?" + "page=" + data["page"] + "&pageSize=" + data["pageSize"]
      response = requests.get(endpoint_url, auth=(credentials["USER_ID"], credentials["API_TOKEN"]))
      json_response = response.json()
      return json_response

    '''
    Creates a new scan policy.
    '''
    def new(credentials, data):
      endpoint_url = credentials["API_ROOT"] % "scanpolicies/new"
      json_data = json.dumps(data)
      response = requests.post(endpoint_url, headers={'Content-Type':'application/json'}, data=json_data, auth=(credentials["USER_ID"], credentials["API_TOKEN"]))
      json_response = response.json()
      return json_response

    '''
    Updates a scan policy.
    '''
    def update(credentials, data):
      endpoint_url = credentials["API_ROOT"] % "scanpolicies/update"
      json_data = json.dumps(data)
      response = requests.post(endpoint_url, headers={'Content-Type':'application/json'}, data=json_data, auth=(credentials["USER_ID"], credentials["API_TOKEN"]))
      json_response = response.json()
      return json_response