#Netsparker_Account.py    
#@package   Netsparker_Rest_API
#@author    Samy Younsi (Shino Corp') <samyyounsi@hotmail.fr>
#@license   MIT License (http://www.opensource.org/licenses/mit-license.php)
#@link      https://github.com/ShinoNoNuma/Netsparker-Rest-API
#@docs      https://www.netsparkercloud.com/docs/index#/Account

import requests

class Account(object):
    '''
    Gives user's account license.
    '''
    def license(credentials):
      endpoint_url = credentials["API_ROOT"] % "account/license"
      response = requests.get(endpoint_url, auth=(credentials["USER_ID"], credentials["API_TOKEN"]))
      json_response = response.json()
      return json_response

    '''
    Gets the information of callee
    '''
    def me(credentials):
      endpoint_url = credentials["API_ROOT"] % "account/me"
      response = requests.get(endpoint_url, auth=(credentials["USER_ID"], credentials["API_TOKEN"]))
      json_response = response.json()
      return json_response
