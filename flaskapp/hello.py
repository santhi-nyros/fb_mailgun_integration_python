from flask import Flask
application = Flask(__name__)

import json
import requests
from flask import request
from facebookads.api import FacebookAdsApi
from facebookads import objects
from facebookads.adobjects.lead import Lead



@application.route('/', methods=['GET','POST'])
def get_webhook_lead():
    if request.method == "GET":
        if (request.args.get('hub.verify_token') == '12345678'):
            return request.args.get('hub.challenge')
        return 'Error, wrong validation token'

    if request.method == "POST":
        my_app_id = '<YOUR_APP_ID>'
        my_app_secret = '<YOUR_APP_SECRET>'
        my_access_token = '<YOUR_ACCESS_TOKEN>'

        FacebookAdsApi.init(my_app_id, my_app_secret, my_access_token)
        res = request.data
        res = json.loads(res.decode("utf-8"))

        lead_id = res['entry'][0]['changes'][0]['value']['leadgen_id']
        lead = Lead(lead_id)
        lead.remote_read()

        email = lead['field_data'][0]['values'][0]
        name = lead['field_data'][1]['values'][0]
        result = add_list_member(email,name);

        return 'Hello,formId:  {0}!'.format(lead)


def add_list_member(email,name):
    #Mailgu api key
    key = '<YOUR_MAILGUN_API_KEY>'
    domain = '<YOUR_MAILGUN_DOMAIN_NAME>'

    # adding lead mail to maillist in mailgun account
    mailList_url = "https://api.mailgun.net/v3/lists/santhi@{0}/members".format(domain)


    result = requests.post(mailList_url, auth=('api', key), data={
        'subscribed': True,
        'address': email,
        'name': name,
        'description': 'testing mail list'
    })

    # sending mail to lead
    request_url = 'https://api.mailgun.net/v2/{0}/messages'.format(domain)
    request = requests.post(request_url, auth=('api', key), data={
        'from': 'santhi.nyros@gmail.com',
        'to': email,
        'subject': 'Hello',
        'text': 'Hello {0}, This is a Testing mail from mailgun'.format(name)
    })
    return result


if __name__ == "__main__":
    application.run(host='0.0.0.0')
