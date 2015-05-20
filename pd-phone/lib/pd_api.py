import requests
import json

class PagerDuty(object):
    def __init__(self, subdomain, auth_token):
        self.subdomain = subdomain
        self.auth_token = auth_token

    def call_api(self, api):
        url = 'https://{0}.pagerduty.com/{1}'.format(self.subdomain, api )
        headers = {'Authorization': 'Token token={0}'.format(self.auth_token)}
        return requests.get(url, headers=headers)

    def get_oncall_phone_number(self):
        results = self.call_api('api/v1/users/on_call').json()
        user = results['users']['on_call'][0]['escalation_policy']['id']
        results = self.call_api('users/{0}/contact_methods'.format(user)).json()
        for cm in results["contact_methods"]:
            if cm['type'] is 'phone':
                return cm['phone_number']
            else:
                raise Exception('Unable to find phone number for on-call contact')