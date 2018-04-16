# -*- coding: utf-8 -*-
from flask import Flask, request, make_response, Response, Flask, flash, redirect, render_template, request, session, abort
import plivo
app = Flask(__name__, static_url_path='')


@app.route('/send/')
def outbound_sms():
    client = plivo.RestClient(auth_id = '', auth_token = '')

    try:
        response = client.messages.create(
            src = '11111111', # Sender's phone number with country code
            dst = '919538183813', # Receiver's phone Number with country code
            text = 'You have a call coming your way',
        )
    #response = p.send_message(params)
    # Prints the complete response
        return str(response)
    except plivo.exceptions.PlivoRestError as e:
        print(e)

if __name__ == "__main__":
    app.run(debug=True)
