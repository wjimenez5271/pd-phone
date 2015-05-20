from flask import Flask, request, redirect
import twilio.twiml
from lib import phone_api
from lib import pd_api

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def process_call_reuqest():

    pd = pd_api.PagerDuty('')

    oncall_number = pd.get_oncall_phone_number()
    oncall_message = 'Inbound call for oncall engineer. Press any key to connect'

    resp = twilio.twiml.Redirect()
    resp.body(phone_api.Twillio.contruct_twimlet_api(oncall_number, oncall_message))

    return str(resp)


if __name__ == "__main__":
    app.run(debug='debug', host='0.0.0.0')
