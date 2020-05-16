#Netsparker_Websites.py    
#@package   Netsparker_Rest_API
#@author    Samy Younsi (Shino Corp') <samyyounsi@hotmail.fr>
#@license   MIT License (http://www.opensource.org/licenses/mit-license.php)
#@link      https://github.com/ShinoNoNuma/Netsparker-Rest-API
#@docs      https://www.netsparkercloud.com/docs/index#/Websites

import requests
import json

class Websites(object):
    '''
      Deletes a website.
    '''
    def delete(credentials, data):
      endpoint_url = credentials["API_ROOT"] % "websites/delete"
      json_data = json.dumps(data)
      response = requests.post(endpoint_url, headers={'Content-Type':'application/json'}, data=json_data, auth=(credentials["USER_ID"], credentials["API_TOKEN"]))
      json_response = response.json()
      return json_response

    '''
      Gets website by name or URL / Gets website by id.
    '''
    def get(credentials, data):
      if "name" in data :
        endpoint_url = credentials["API_ROOT"] % "websites/get" + "?" + "query=" + data["query"]
      else :
        endpoint_url = credentials["API_ROOT"] % "websites/get" + "/" + data["id"]
      response = requests.get(endpoint_url, auth=(credentials["USER_ID"], credentials["API_TOKEN"]))
      json_response = response.json()
      return json_response

    '''
      Gets the list of websites by group name or id.
    '''
    def getwebsitesbygroup(credentials, data):
      endpoint_url = credentials["API_ROOT"] % "websites/getwebsitesbygroup" + "?" + "query=" + data["query"] + "&page=" + data["page"] + "&pageSize=" + data["pageSize"]
      response = requests.get(endpoint_url, auth=(credentials["USER_ID"], credentials["API_TOKEN"]))
      json_response = response.json()
      return json_response

    '''
      Gets the list of websites.
    '''
    def list(credentials, data):
      endpoint_url = credentials["API_ROOT"] % "websites/list" + "?" + "page=" + data["page"] + "&pageSize=" + data["pageSize"]
      response = requests.get(endpoint_url, auth=(credentials["USER_ID"], credentials["API_TOKEN"]))
      json_response = response.json()
      return json_response

    '''
      Creates a new website.
    '''
    def new(credentials, data):
      endpoint_url = credentials["API_ROOT"] % "websites/new"
      json_data = json.dumps(data)
      response = requests.post(endpoint_url, headers={'Content-Type':'application/json'}, data=json_data, auth=(credentials["USER_ID"], credentials["API_TOKEN"]))
      json_response = response.json()
      return json_response

    '''
      Sends the verification email if verification limit not exceeded yet.
    '''
    def sendverificationemail(credentials, data):
      endpoint_url = credentials["API_ROOT"] % "websites/sendverificationemail"
      json_data = json.dumps(data)
      response = requests.post(endpoint_url, headers={'Content-Type':'application/json'}, data=json_data, auth=(credentials["USER_ID"], credentials["API_TOKEN"]))
      json_response = response.json()
      return json_response

    '''
      Starts the verification with specified method.
    '''
    def startverification(credentials, data):
      endpoint_url = credentials["API_ROOT"] % "websites/startverification"
      json_data = json.dumps(data)
      response = requests.post(endpoint_url, headers={'Content-Type':'application/json'}, data=json_data, auth=(credentials["USER_ID"], credentials["API_TOKEN"]))
      json_response = response.json()
      return json_response

    '''
      Updates a website.
    '''
    def update(credentials, data):
      endpoint_url = credentials["API_ROOT"] % "websites/update"
      json_data = json.dumps(data)
      response = requests.post(endpoint_url, headers={'Content-Type':'application/json'}, data=json_data, auth=(credentials["USER_ID"], credentials["API_TOKEN"]))
      json_response = response.json()
      return json_response

    '''
      Renders verification file.
    '''
    def verificationfile(credentials, data):
      endpoint_url = credentials["API_ROOT"] % "websites/verificationfile" + "?" + "websiteUrl=" + data["websiteUrl"]
      response = requests.get(endpoint_url, auth=(credentials["USER_ID"], credentials["API_TOKEN"]))
      json_response = response.json()
      return json_response

    '''
      Executes verification process.
    '''
    def verify(credentials, data):
      endpoint_url = credentials["API_ROOT"] % "websites/verify"
      json_data = json.dumps(data)
      response = requests.post(endpoint_url, headers={'Content-Type':'application/json'}, data=json_data, auth=(credentials["USER_ID"], credentials["API_TOKEN"]))
      json_response = response.json()
      return json_response