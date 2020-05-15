#Netsparker_WebsiteGroups.py    
#@package   Netsparker_Rest_API
#@author    Samy Younsi (Shino Corp') <samyyounsi@hotmail.fr>
#@license   MIT License (http://www.opensource.org/licenses/mit-license.php)
#@link      https://github.com/ShinoNoNuma/Netsparker-Rest-API
#@docs      https://www.netsparkercloud.com/docs/index#/WebsiteGroups

import requests
import json

class WebsiteGroups(object):
    '''
      Deletes a website group.    
    '''
    def delete(credentials, data):
      endpoint_url = credentials["API_ROOT"] % "websitegroups/delete"
      json_data = json.dumps(data)
      response = requests.post(endpoint_url, headers={'Content-Type':'application/json'}, data=json_data, auth=(credentials["USER_ID"], credentials["API_TOKEN"]))
      json_response = response.json()
      return json_response

    '''
      Gets website group by name / Gets website group by id.
    '''
    def get(credentials, data):
      if "name" in data :
        endpoint_url = credentials["API_ROOT"] % "websitegroups/get" + "?" + "name=" + data["name"]
      else :
        endpoint_url = credentials["API_ROOT"] % "websitegroups/get" + "/" + data["id"]
      response = requests.get(endpoint_url, auth=(credentials["USER_ID"], credentials["API_TOKEN"]))
      json_response = response.json()
      return json_response

    '''
      Gets the list of website groups.
    '''
    def list(credentials, data):
      endpoint_url = credentials["API_ROOT"] % "websitegroups/list" + "?" + "page=" + data["page"] + "&pageSize=" + data["pageSize"]
      response = requests.get(endpoint_url, auth=(credentials["USER_ID"], credentials["API_TOKEN"]))
      json_response = response.json()
      return json_response

    '''
      Creates a new website group.
    '''
    def new(credentials, data):
      endpoint_url = credentials["API_ROOT"] % "websitegroups/new"
      json_data = json.dumps(data)
      response = requests.post(endpoint_url, headers={'Content-Type':'application/json'}, data=json_data, auth=(credentials["USER_ID"], credentials["API_TOKEN"]))
      json_response = response.json()
      return json_response

    '''
      Updates a website group.
    '''
    def update(credentials, data):
      endpoint_url = credentials["API_ROOT"] % "websitegroups/update"
      json_data = json.dumps(data)
      response = requests.post(endpoint_url, headers={'Content-Type':'application/json'}, data=json_data, auth=(credentials["USER_ID"], credentials["API_TOKEN"]))
      json_response = response.json()
      return json_response