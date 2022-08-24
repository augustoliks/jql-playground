import requests
from requests.auth import HTTPBasicAuth
import json
from pprint import pprint

email = "carlos.neto.dev@gmail.com"
jira_token = ""
# q = "issue in addedToSprintAfterStart('2', 'OPS Sprint 1')"
# q = "Sprint = 'OPS Sprint 1' AND issue not in addedToSprintAfterStart('2', 'OPS Sprint 1')"
# q = "Sprint = 'OPS Sprint 1'"


base = "https://liks.atlassian.net"

# url = "https://liks.atlassian.net/rest/api/3/search?jql=filter=10003"
# a = q.replace(' ', '+')
#
# url = f"{base}/rest/agile/1.0/board"
# url = f"{base}/rest/api/2/search?jql={a}"
# url = f"{base}/rest/api/3/issue/OPS-1"
url = f"{base}/rest/api/3/search?jql=issueFunction+in+addedAfterSprintStart('2','OPS Sprint 1')"




auth = HTTPBasicAuth(email, jira_token)

headers = {
   "Accept": "application/json",
   "Content-Type": "application/json"
}

response = requests.request(
   "GET",

   url,
   headers=headers,
   auth=auth
)

print(json.dumps(response.json()))
