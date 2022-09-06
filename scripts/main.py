import requests
from requests.auth import HTTPBasicAuth
import json
from pprint import pprint


credentials = ("carlos.neto.dev@gmail.com", "")
jira = JIRA(url, basic_auth=credentials)
get_property = jira.issue_property("OPS-10", "ground")
