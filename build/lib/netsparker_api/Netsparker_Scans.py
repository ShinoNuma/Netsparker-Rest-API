#Netsparker_Scans.py    
#@package   Netsparker_Rest_API
#@author    Samy Younsi (Shino Corp') <samyyounsi@hotmail.fr>
#@license   MIT License (http://www.opensource.org/licenses/mit-license.php)
#@link      https://github.com/ShinoNoNuma/Netsparker-Rest-API
#@docs      https://www.netsparkercloud.com/docs/index#/Scans

import requests
import json

class Scans(object):
    '''
      Stops a scan in progress.
    '''
    def cancel(credentials, data):
      endpoint_url = credentials["API_ROOT"] % "scans/cancel"
      json_data = json.dumps(data)
      response = requests.post(endpoint_url, headers={'Content-Type':'application/json'}, data=json_data, auth=(credentials["USER_ID"], credentials["API_TOKEN"]))
      json_response = response.json()
      return json_response

    '''
      Returns the custom report of a scan in the specified format.
    '''
    def custom_report(credentials, data):
      endpoint_url = credentials["API_ROOT"] % "scans/custom-report/" + "?" + "excludeIgnoreds=" + data["excludeIgnoreds"] + "&id=" + data["id"] + "&onlyConfirmedVulnerabilities=" + data["onlyConfirmedVulnerabilities"] + "&reportName=" + data["reportName"] + "&reportFormat=" + data["reportFormat"] 
      response = requests.get(endpoint_url, auth=(credentials["USER_ID"], credentials["API_TOKEN"]))
      json_response = response.json()
      return json_response

    '''
      Deletes scan data.
    '''
    def delete(credentials, data):
      endpoint_url = credentials["API_ROOT"] % "scans/delete"
      json_data = json.dumps(data)
      response = requests.post(endpoint_url, headers={'Content-Type':'application/json'}, data=json_data, auth=(credentials["USER_ID"], credentials["API_TOKEN"]))
      json_response = response.json()
      return json_response

    '''
      Gets the detail of a scan.
    '''
    def detail(credentials, data):
      endpoint_url = credentials["API_ROOT"] % "scans/detail" + "/" + data["detail"]
      response = requests.get(endpoint_url, auth=(credentials["USER_ID"], credentials["API_TOKEN"]))
      json_response = response.json()
      return json_response

    '''
      Downloads the scan file as zip
    '''
    def downloadscanfile(credentials, data):
      endpoint_url = credentials["API_ROOT"] % "scans/downloadscanfile" + "?" + "scanId=" + data["scanId"]
      response = requests.get(endpoint_url, auth=(credentials["USER_ID"], credentials["API_TOKEN"]))
      json_response = response.json()
      return json_response

    '''
      Launches an incremental scan based on the provided base scan identifier.
    '''
    def incremental(credentials, data):
      endpoint_url = credentials["API_ROOT"] % "scans/incremental"
      json_data = json.dumps(data)
      response = requests.post(endpoint_url, headers={'Content-Type':'application/json'}, data=json_data, auth=(credentials["USER_ID"], credentials["API_TOKEN"]))
      json_response = response.json()
      return json_response

    '''
      Gets the list of scans and their details.
    '''
    def list(credentials, data):
      endpoint_url = credentials["API_ROOT"] % "scans/list" + "?" + "page=" + data["page"] + "pageSize=" + data["pageSize"]
      response = requests.get(endpoint_url, auth=(credentials["USER_ID"], credentials["API_TOKEN"]))
      json_response = response.json()
      return json_response

    '''
      Gets the list of scans by state
    '''
    def listbystate(credentials, data):
      endpoint_url = credentials["API_ROOT"] % "scans/listbystate" + "?" + "scanTaskState=" + data["scanTaskState"] + "&targetUrlCriteria=" + data["targetUrlCriteria"] + "&page=" + data["page"] + "pageSize=" + data["pageSize"] + "&startDate=" + data["startDate"] + "&endDate=" + data["endDate"]
      response = requests.get(endpoint_url, auth=(credentials["USER_ID"], credentials["API_TOKEN"]))
      json_response = response.json()
      return json_response

    '''
      Gets the list of scans by stateChanged
    '''
    def listbystatechanged(credentials, data):
      endpoint_url = credentials["API_ROOT"] % "scans/listbystatechanged" + "?" + "startDate=" + data["startDate"] + "&endDate=" + data["endDate"] + "&page=" + data["page"] + "pageSize=" + data["pageSize"]
      response = requests.get(endpoint_url, auth=(credentials["USER_ID"], credentials["API_TOKEN"]))
      json_response = response.json()
      return json_response
    
    '''
      Gets the list of scans and their details.
    '''
    def listbywebsite(credentials, data):
      endpoint_url = credentials["API_ROOT"] % "scans/listbywebsite" + "?" + "websiteUrl=" + data["websiteUrl"] + "&targetUrl=" + data["targetUrl"] + "&page=" + data["page"] + "pageSize=" + data["pageSize"] + "initiatedDateSortType=" + data["initiatedDateSortType"]
      response = requests.get(endpoint_url, auth=(credentials["USER_ID"], credentials["API_TOKEN"]))
      json_response = response.json()
      return json_response

    '''
      Gets the list of scheduled scans which are scheduled to be launched in the future.
    '''
    def listscheduled(credentials, data):
      endpoint_url = credentials["API_ROOT"] % "scans/list-scheduled" + "?" + "page=" + data["page"] + "pageSize=" + data["pageSize"]
      response = requests.get(endpoint_url, auth=(credentials["USER_ID"], credentials["API_TOKEN"]))
      json_response = response.json()
      return json_response

    '''
      Launches a new scan.
    '''
    def new(credentials, data):
      endpoint_url = credentials["API_ROOT"] % "scans/new"
      json_data = json.dumps(data)
      response = requests.post(endpoint_url, headers={'Content-Type':'application/json'}, data=json_data, auth=(credentials["USER_ID"], credentials["API_TOKEN"]))
      json_response = response.json()
      return json_response

    '''
      Launches a new scan with same configuration from the scan specified with scan id.
    '''
    def newfromscan(credentials, data):
      endpoint_url = credentials["API_ROOT"] % "scans/newfromscan"
      json_data = json.dumps(data)
      response = requests.post(endpoint_url, headers={'Content-Type':'application/json'}, data=json_data, auth=(credentials["USER_ID"], credentials["API_TOKEN"]))
      json_response = response.json()
      return json_response

    '''
      Launches a new group scan.
    '''
    def newgroupscan(credentials, data):
      endpoint_url = credentials["API_ROOT"] % "scans/newgroupscan"
      json_data = json.dumps(data)
      response = requests.post(endpoint_url, headers={'Content-Type':'application/json'}, data=json_data, auth=(credentials["USER_ID"], credentials["API_TOKEN"]))
      json_response = response.json()
      return json_response
      
    '''
      Launches a new scan with profile id.
    '''    
    def newwithprofile(credentials, data):
      endpoint_url = credentials["API_ROOT"] % "scans/newwithprofile"
      json_data = json.dumps(data)
      response = requests.post(endpoint_url, headers={'Content-Type':'application/json'}, data=json_data, auth=(credentials["USER_ID"], credentials["API_TOKEN"]))
      json_response = response.json()
      return json_response

    '''
      Pauses a scan in progress.
    '''
    def pause(credentials, data):
      endpoint_url = credentials["API_ROOT"] % "scans/pause"
      json_data = json.dumps(data)
      response = requests.post(endpoint_url, headers={'Content-Type':'application/json'}, data=json_data, auth=(credentials["USER_ID"], credentials["API_TOKEN"]))
      json_response = response.json()
      return json_response

    '''
      Returns the report of a scan in the specified format.
    '''
    def report(credentials, data):
      endpoint_url = credentials["API_ROOT"] % "scans/report" + "?" + "contentFormat=" + data["contentFormat"] + "&excludeResponseData=" + data["excludeResponseData"] + "&format=" + data["format"] + "&id=" + data["id"] + "&type=" + data["type"] + "&onlyConfirmedIssues=" + data["onlyConfirmedIssues"] + "&excludeAddressedIssues=" + data["excludeAddressedIssues"]
      response = requests.get(endpoint_url, auth=(credentials["USER_ID"], credentials["API_TOKEN"]))
      json_response = response.json()
      return json_response

    '''
      Gets the result of a scan.
    '''
    def result(credentials, data):
      endpoint_url = credentials["API_ROOT"] % "scans/result" + "/" + data["id"]
      response = requests.get(endpoint_url, auth=(credentials["USER_ID"], credentials["API_TOKEN"]))
      json_response = response.json()
      return json_response

    '''
      Pauses a scan in progress.
    '''
    def pause(credentials, data):
      endpoint_url = credentials["API_ROOT"] % "scans/pause"
      json_data = json.dumps(data)
      response = requests.post(endpoint_url, headers={'Content-Type':'application/json'}, data=json_data, auth=(credentials["USER_ID"], credentials["API_TOKEN"]))
      json_response = response.json()
      return json_response

    '''
      Resumes a paused scan.
    '''
    def resume(credentials, data):
      endpoint_url = credentials["API_ROOT"] % "scans/resume"
      json_data = json.dumps(data)
      response = requests.post(endpoint_url, headers={'Content-Type':'application/json'}, data=json_data, auth=(credentials["USER_ID"], credentials["API_TOKEN"]))
      json_response = response.json()
      return json_response

    '''
      Launches a retest scan based on the provided base scan identifier.
    '''
    def retest(credentials, data):
      endpoint_url = credentials["API_ROOT"] % "scans/resume"
      json_data = json.dumps(data)
      response = requests.post(endpoint_url, headers={'Content-Type':'application/json'}, data=json_data, auth=(credentials["USER_ID"], credentials["API_TOKEN"]))
      json_response = response.json()
      return json_response

    '''
      Schedules a scan to be launched in the future.
    '''
    def schedule(credentials, data):
      endpoint_url = credentials["API_ROOT"] % "scans/schedule"
      json_data = json.dumps(data)
      response = requests.post(endpoint_url, headers={'Content-Type':'application/json'}, data=json_data, auth=(credentials["USER_ID"], credentials["API_TOKEN"]))
      json_response = response.json()
      return json_response

    '''
      Schedules an incremental scan to be launched in the future.
    '''
    def schedule_incremental(credentials, data):
      endpoint_url = credentials["API_ROOT"] % "scans/schedule-incremental"
      json_data = json.dumps(data)
      response = requests.post(endpoint_url, headers={'Content-Type':'application/json'}, data=json_data, auth=(credentials["USER_ID"], credentials["API_TOKEN"]))
      json_response = response.json()
      return json_response

    '''
      Gets the status of a scan.
    '''
    def status(credentials, data):
      endpoint_url = credentials["API_ROOT"] % "scans/status" + "/" + data["id"]
      response = requests.get(endpoint_url, auth=(credentials["USER_ID"], credentials["API_TOKEN"]))
      json_response = response.json()
      return json_response

    '''
      Removes a scheduled scan.
    '''
    def unschedule(credentials, data):
      endpoint_url = credentials["API_ROOT"] % "scans/unschedule"
      json_data = json.dumps(data)
      response = requests.post(endpoint_url, headers={'Content-Type':'application/json'}, data=json_data, auth=(credentials["USER_ID"], credentials["API_TOKEN"]))
      json_response = response.json()
      return json_response

    '''
      Updates scheduled scan.
    '''
    def update_scheduled(credentials, data):
      endpoint_url = credentials["API_ROOT"] % "scans/update-scheduled"
      json_data = json.dumps(data)
      response = requests.post(endpoint_url, headers={'Content-Type':'application/json'}, data=json_data, auth=(credentials["USER_ID"], credentials["API_TOKEN"]))
      json_response = response.json()
      return json_response

    '''
      Updates an incremental scheduled scan.
    '''
    def update_scheduled_incremental(credentials, data):
      endpoint_url = credentials["API_ROOT"] % "scans/update-scheduled-incremental"
      json_data = json.dumps(data)
      response = requests.post(endpoint_url, headers={'Content-Type':'application/json'}, data=json_data, auth=(credentials["USER_ID"], credentials["API_TOKEN"]))
      json_response = response.json()
      return json_response

    '''
      Verifies the specified form authentication settings.
    '''
    def verifyformauth(credentials, data):
      endpoint_url = credentials["API_ROOT"] % "scans/verifyformauth"
      json_data = json.dumps(data)
      response = requests.post(endpoint_url, headers={'Content-Type':'application/json'}, data=json_data, auth=(credentials["USER_ID"], credentials["API_TOKEN"]))
      json_response = response.json()
      return json_response