import random
import sys
import binascii
import base58
import base64
import requests
from coincurve.keys import PrivateKey
from coincurve._libsecp256k1 import ffi


class CenterIdentity:
    def __init__(self, wif, username, url_prefix=None):

        self.wif = wif # this is the server side api key of the service, also their identity wif
        self.private_key = self.from_wif()
        self.username = username

        key = PrivateKey.from_hex(self.private_key)
        public_key = key.public_key.format().hex()
        self.identity = {
            'username': self.username,
            'username_signature': self.sign_deterministic(self.username),
            'public_key': public_key
        }

        self.url_prefix = url_prefix or 'https://centeridentity.com'

    def from_wif(self):
        return binascii.hexlify(base58.b58decode(self.wif))[2:-10].decode()

    def sign(self, message):
        x = ffi.new('long long *')
        x[0] = random.SystemRandom().randint(0, sys.maxsize)
        key = PrivateKey.from_hex(self.private_key)
        signature = key.sign(message.encode('utf-8'), custom_nonce=(ffi.NULL, x))
        return base64.b64encode(signature).decode('utf-8')

    def sign_deterministic(self, message):
        key = PrivateKey.from_hex(self.private_key)
        signature = key.sign(message.encode('utf-8'))
        return base64.b64encode(signature).decode('utf-8')

    def do_challenge(self, body):
        req = requests.post(f'{self.url_prefix}/challenge', json={
            'api_key': self.identity['username_signature'],
            'identity': self.identity
        })
        challenge_context = req.json()['challenge']
        signature = self.sign(challenge_context['challenge']['message'])
        challenge_context['challenge']['signature'] = signature
        challenge_context['client_identity'] = body['identity']
        return challenge_context

    def verify_client_challenge(self, challenge_context):
        req = requests.post(f'{self.url_prefix}/challenge', json=challenge_context)
        return req.json()

    def get_recovery(self, body):
        challenge_result = self.verify_client_challenge(body)
        if challenge_result['status'] is True:
            challenge_context = self.do_challenge(body)
            res = requests.post(f'{self.url_prefix}/get-recovery', json=challenge_context)
            return res.json()
        return {'status': False}

    def set_recovery(self, client_username, body):
        challenge_result = self.verify_client_challenge(body)
        if not challenge_result['status']:
            return {'status': False}
        if client_username != body['identity']['username']:
            return {'status': False}
        challenge_context = self.do_challenge(body)
        res = requests.post(f'{self.url_prefix}/set-recovery', json=challenge_context)
        return res.json()