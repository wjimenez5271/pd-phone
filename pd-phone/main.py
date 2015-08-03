from flask import Flask, request, redirect
import twilio.twiml
from lib import phone_api
from lib import pd_api
from lib import config
from sys import exit

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def process_call_reuqest():
    c = config.get_config()
    pd = pd_api.PagerDuty(c['pd_subdomain'], c['pd_api_key'])

    oncall_number = pd.get_oncall_phone_number()
    oncall_message = 'This is the on-call phone service. Press any key to connect'

    resp = twilio.twiml.Redirect()
    resp.body(phone_api.Twillio.contruct_twimlet_api(oncall_number, oncall_message))

    return str(resp)


if __name__ == "__main__":
    while True:
        try:
            app.run(debug='debug', host='0.0.0.0')
        except KeyboardInterrupt:
            print 'Exiting upon user request'
            exit(0)
