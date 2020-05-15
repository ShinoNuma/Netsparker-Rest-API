#Netsparker_Notifications.py    
#@package   Netsparker_Rest_API
#@author    Samy Younsi (Shino Corp') <samyyounsi@hotmail.fr>
#@license   MIT License (http://www.opensource.org/licenses/mit-license.php)
#@link      https://github.com/ShinoNoNuma/Netsparker-Rest-API
#@docs      https://www.netsparkercloud.com/docs/index#/Notifications

import requests
import json

class Notifications(object):
    '''
    Deletes an existing scan notification definition.
    '''
    def delete(credentials, data):
      endpoint_url = credentials["API_ROOT"] % "notifications/delete"
      json_data = json.dumps(data)
      response = requests.post(endpoint_url, headers={'Content-Type':'application/json'}, data=json_data, auth=(credentials["USER_ID"], credentials["API_TOKEN"]))
      json_response = response.json()
      return json_response

    '''
    Gets the notification.
    '''
    def get(credentials, data):
      endpoint_url = credentials["API_ROOT"] % "notifications/get" + "/" + data["id"]
      response = requests.get(endpoint_url, auth=(credentials["USER_ID"], credentials["API_TOKEN"]))
      json_response = response.json()
      return json_response

    '''
    Gets the list of notifications grouped by their Scopes and ordered by priorities for the given event.
    '''
    def getpriorities(credentials, data):
      endpoint_url = credentials["API_ROOT"] % "notifications/getpriorities" + "?" + "event=" + data["event"]
      json_data = json.dumps(data)
      response = requests.get(endpoint_url, auth=(credentials["USER_ID"], credentials["API_TOKEN"]))
      json_response = response.json()
      return json_response

    '''
    Gets the list of notifications.
    '''
    def list(credentials, data):
      endpoint_url = credentials["API_ROOT"] % "notifications/list" + "?" + "page=" + data["page"] + "&pageSize=" + data["pageSize"]
      json_data = json.dumps(data)
      response = requests.get(endpoint_url, auth=(credentials["USER_ID"], credentials["API_TOKEN"]))
      json_response = response.json()
      return json_response

    '''
    Creates a new scan notification definition.
    '''
    def new(credentials, data):
      endpoint_url = credentials["API_ROOT"] % "notifications/new"
      json_data = json.dumps(data)
      response = requests.post(endpoint_url, headers={'Content-Type':'application/json'}, data=json_data, auth=(credentials["USER_ID"], credentials["API_TOKEN"]))
      json_response = response.json()
      return json_response

    '''
    Sets the priorities of notifications.
    '''
    def setpriorities(credentials, data):
      endpoint_url = credentials["API_ROOT"] % "notifications/setpriorities"
      json_data = json.dumps(data)
      response = requests.post(endpoint_url, headers={'Content-Type':'application/json'}, data=json_data, auth=(credentials["USER_ID"], credentials["API_TOKEN"]))
      json_response = response.json()
      return json_response

    '''
    Updates an existing scan notification definition.
    '''
    def update(credentials, data):
      endpoint_url = credentials["API_ROOT"] % "notifications/update"
      json_data = json.dumps(data)
      response = requests.post(endpoint_url, headers={'Content-Type':'application/json'}, data=json_data, auth=(credentials["USER_ID"], credentials["API_TOKEN"]))
      json_response = response.json()
      return json_response