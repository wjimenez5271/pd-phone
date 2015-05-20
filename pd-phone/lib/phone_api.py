import requests

class Twillio(object):
    @staticmethod
    def contruct_twimlet_api(phone_number, message, timeout=7):
        return "http://twimlets.com/findme?PhoneNumbers[0]={0}&Message={1}&Timeout={2}".format(phone_number,
                                                                                               message,
                                                                                               timeout)

    def forward_call(self):
        raise NotImplementedError
