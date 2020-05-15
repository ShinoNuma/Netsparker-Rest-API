#Netsparker_Agents.py    
#@package   Netsparker_Rest_API
#@author    Samy Younsi (Shino Corp') <samyyounsi@hotmail.fr>
#@license   MIT License (http://www.opensource.org/licenses/mit-license.php)
#@link      https://github.com/ShinoNoNuma/Netsparker-Rest-API
#@docs      https://www.netsparkercloud.com/docs/index#/Agents

import requests
import json

class Agents(object):
    '''
    Sets agent status as terminated.
    Before deleting an agent, please make sure that you've stopped the related service from the Windows Services Manager screen.
    If it is running, the agent will reappear on the page despite removal.
    '''
    def delete(credentials, data):
      endpoint_url = credentials["API_ROOT"] % "agents/delete"
      json_data = json.dumps(data)
      response = requests.post(endpoint_url, headers={'Content-Type':'application/json'}, data=json_data, auth=(credentials["USER_ID"], credentials["API_TOKEN"]))
      json_response = response.json()
      return json_response

    '''
    Gets the list of agents.
    '''
    def list(credentials, data):
      endpoint_url = credentials["API_ROOT"] % "agents/list" + "?" + "page=" + data["page"] + "&pageSize=" + data["pageSize"]
      response = requests.get(endpoint_url, auth=(credentials["USER_ID"], credentials["API_TOKEN"]))
      json_response = response.json()
      return json_response

    '''
    Sets agent status enable or disable.
    '''
    def setstatus(credentials, data):
      endpoint_url = credentials["API_ROOT"] % "agents/setstatus"
      json_data = json.dumps(data)
      response = requests.post(endpoint_url, headers={'Content-Type':'application/json'}, data=json_data, auth=(credentials["USER_ID"], credentials["API_TOKEN"]))
      json_response = response.json()
      return json_response