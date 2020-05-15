#Netsparker_Issues.py    
#@package   Netsparker_Rest_API
#@author    Samy Younsi (Shino Corp') <samyyounsi@hotmail.fr>
#@license   MIT License (http://www.opensource.org/licenses/mit-license.php)
#@link      https://github.com/ShinoNoNuma/Netsparker-Rest-API
#@docs      https://www.netsparkercloud.com/docs/index#/Issues

import requests
import json

class Issues(object):
    '''
    Gets the list of addressed issues.
    '''
    def addressedissues(credentials, data):
      endpoint_url = credentials["API_ROOT"] % "issues/addressedissues" + "?" + "severity=" + data["severity"] + "&webSiteName=" + data["webSiteName"] + "&websiteGroupName=" + data["websiteGroupName"] + "&page=" + data["page"] + "&pageSize=" + data["pageSize"]
      response = requests.get(endpoint_url, auth=(credentials["USER_ID"], credentials["API_TOKEN"]))
      json_response = response.json()
      return json_response

    '''
    Gets the list of all issues.
    '''
    def allissues(credentials, data):
      endpoint_url = credentials["API_ROOT"] % "issues/allissues" + "?" + "severity=" + data["severity"] + "&webSiteName=" + data["webSiteName"] + "&websiteGroupName=" + data["websiteGroupName"] + "&page=" + data["page"] + "&pageSize=" + data["pageSize"] + "&sortType=" + data["sortType"] + "&lastSeenDate=" + data["lastSeenDate"] + "&rawDetails=" + data["rawDetails"]
      response = requests.get(endpoint_url, auth=(credentials["USER_ID"], credentials["API_TOKEN"]))
      json_response = response.json()
      return json_response

    '''
    Gets issues by id.
    '''
    def get(credentials, data):
      endpoint_url = credentials["API_ROOT"] % "issues/get" + "/" + data["id"]
      response = requests.get(endpoint_url, auth=(credentials["USER_ID"], credentials["API_TOKEN"]))
      json_response = response.json()
      return json_response

    '''
    Gets vulnerability request/response content by id.
    '''
    def getvulnerabilitycontent(credentials, data):
      endpoint_url = credentials["API_ROOT"] % "issues/getvulnerabilitycontent" + "/" + data["id"]
      response = requests.get(endpoint_url, auth=(credentials["USER_ID"], credentials["API_TOKEN"]))
      json_response = response.json()
      return json_response

    '''
    Returns the report of issues in the csv format.
    '''
    def allissues(credentials, data):
      endpoint_url = credentials["API_ROOT"] % "issues/report" + "?" + "csvSeparator=" + data["csvSeparator"] + "&severity=" + data["severity"] + "&websiteGroupName=" + data["websiteGroupName"] + "&webSiteName=" + data["webSiteName"]
      response = requests.get(endpoint_url, auth=(credentials["USER_ID"], credentials["API_TOKEN"]))
      json_response = response.json()
      return json_response

    '''
    Gets the list of to-do issues.
    '''
    def todo(credentials, data):
      endpoint_url = credentials["API_ROOT"] % "issues/todo" + "?" + "severity=" + data["severity"] + "&webSiteName=" + data["webSiteName"] + "&websiteGroupName=" + data["websiteGroupName"] + "&page=" + data["page"] + "&pageSize=" + data["pageSize"] 
      response = requests.get(endpoint_url, auth=(credentials["USER_ID"], credentials["API_TOKEN"]))
      json_response = response.json()
      return json_response

    '''
    Gets the list of retest issues.
    '''
    def waitingforretest(credentials, data):
      endpoint_url = credentials["API_ROOT"] % "issues/waitingforretest" + "?" + "severity=" + data["severity"] + "&webSiteName=" + data["webSiteName"] + "&websiteGroupName=" + data["websiteGroupName"] + "&page=" + data["page"] + "&pageSize=" + data["pageSize"] 
      response = requests.get(endpoint_url, auth=(credentials["USER_ID"], credentials["API_TOKEN"]))
      json_response = response.json()
      return json_response