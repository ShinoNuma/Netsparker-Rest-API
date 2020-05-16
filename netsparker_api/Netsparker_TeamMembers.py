#Netsparker_TeamMembers.py    
#@package   Netsparker_Rest_API
#@author    Samy Younsi (Shino Corp') <samyyounsi@hotmail.fr>
#@license   MIT License (http://www.opensource.org/licenses/mit-license.php)
#@link      https://github.com/ShinoNoNuma/Netsparker-Rest-API
#@docs      https://www.netsparkercloud.com/docs/index#/TeamMembers

import requests
import json

class TeamMembers(object):
    '''
      Deletes a user.
    '''
    def delete(credentials, data):
      endpoint_url = credentials["API_ROOT"] % "teammembers/delete"
      json_data = json.dumps(data)
      response = requests.post(endpoint_url, headers={'Content-Type':'application/json'}, data=json_data, auth=(credentials["USER_ID"], credentials["API_TOKEN"]))
      json_response = response.json()
      return json_response

    '''
      Gets user by id.
    '''
    def get(credentials, data):
      endpoint_url = credentials["API_ROOT"] % "teammembers/get" + "/" + data["id"]
      response = requests.get(endpoint_url, auth=(credentials["USER_ID"], credentials["API_TOKEN"]))
      json_response = response.json()
      return json_response

    '''
      Gets user by email.
    '''
    def getbyemail(credentials, data):
      endpoint_url = credentials["API_ROOT"] % "teammembers/getbyemail" + "?" + "email=" + data["email"]
      response = requests.get(endpoint_url, auth=(credentials["USER_ID"], credentials["API_TOKEN"]))
      json_response = response.json()
      return json_response

    '''
      Gets a list all of the time zones.
    '''
    def gettimezones(credentials):
      endpoint_url = credentials["API_ROOT"] % "teammembers/gettimezones"
      response = requests.get(endpoint_url, auth=(credentials["USER_ID"], credentials["API_TOKEN"]))
      json_response = response.json()
      return json_response

    '''
      Gets the list of users.
    '''
    def list(credentials, data):
      endpoint_url = credentials["API_ROOT"] % "teammembers/list" + "?" + "page=" + data["page"] + "&pageSize=" + data["pageSize"]
      response = requests.get(endpoint_url, auth=(credentials["USER_ID"], credentials["API_TOKEN"]))
      json_response = response.json()
      return json_response

    '''
      Creates a new member.
    '''
    def new(credentials, data):
      endpoint_url = credentials["API_ROOT"] % "teammembers/new"
      json_data = json.dumps(data)
      response = requests.post(endpoint_url, headers={'Content-Type':'application/json'}, data=json_data, auth=(credentials["USER_ID"], credentials["API_TOKEN"]))
      json_response = response.json()
      return json_response

    '''
      Updates an user.
    '''
    def update(credentials, data):
      endpoint_url = credentials["API_ROOT"] % "teammembers/update"
      json_data = json.dumps(data)
      response = requests.post(endpoint_url, headers={'Content-Type':'application/json'}, data=json_data, auth=(credentials["USER_ID"], credentials["API_TOKEN"]))
      json_response = response.json()
      return json_response