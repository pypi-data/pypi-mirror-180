# coding: utf-8

from __future__ import absolute_import

import json
import unittest
import uuid
import citypay
from citypay import Configuration
from citypay.api.card_holder_account_api import CardHolderAccountApi
from citypay.api.operational_functions_api import OperationalFunctionsApi
from citypay.api.authorisation_and_payment_api import AuthorisationAndPaymentApi
from citypay.model.account_create import AccountCreate
from citypay.model.api_key import *
import requests
import base64

from citypay.model.auth_request import AuthRequest
from citypay.model.c_res_auth_request import CResAuthRequest
from citypay.model.charge_request import ChargeRequest
from citypay.model.contact_details import ContactDetails
from citypay.model.ping import Ping
from citypay.model.register_card import RegisterCard
from citypay.model.three_d_secure import ThreeDSecure
from citypay.utils.digest import validate_digest


class TestApiIntegration(unittest.TestCase):
    """Error unit test stubs"""

    @classmethod
    def setUpClass(self):

        if 'CP_CLIENT_ID' not in os.environ:
            raise Exception("No CP_CLIENT_ID set")

        if 'CP_LICENCE_KEY' not in os.environ:
            raise Exception("No CP_LICENCE_KEY set")

        if 'CP_MERCHANT_ID' not in os.environ:
            raise Exception("No CP_MERCHANT_ID set")

        self.client_id = os.environ['CP_CLIENT_ID']
        self.licence_key = os.environ['CP_LICENCE_KEY']
        self.merchant_id = os.environ['CP_MERCHANT_ID']

        # create new api key on each call
        client_api_key = api_key_generate(self.client_id, self.licence_key)
        self.api_client = citypay.ApiClient(Configuration(
            host="https://sandbox.citypay.com/v6",
            server_index=1,
            api_key={'cp-api-key': str(client_api_key)}
        ))

    def testPing(self):
        api_response = OperationalFunctionsApi(self.api_client).ping_request(Ping(
            identifier="it_test"
        ))
        self.assertEqual("044", api_response.code)
        self.assertEqual("it_test", api_response.identifier)
        self.assertEqual("Ping OK", api_response.message)
        self.assertIsNotNone(api_response.context)

    def testListMerchants(self):
        api_list_merchants = OperationalFunctionsApi(self.api_client).list_merchants_request(self.client_id)
        self.assertEqual(api_list_merchants.clientid, str(self.client_id))

    def testAuthorise(self):

        id = uuid.uuid4().hex
        decision = AuthorisationAndPaymentApi(self.api_client).authorisation_request(AuthRequest(
            amount=1395,
            cardnumber="4000 0000 0000 0002",
            expmonth=12,
            expyear=2030,
            csc="012",
            identifier=id,
            merchantid=int(self.merchant_id),
            threedsecure=ThreeDSecure(
                tds_policy="2"
            )
        ))

        self.assertIsNone(decision.authen_required())
        self.assertIsNone(decision.request_challenged())
        self.assertIsNotNone(decision.auth_response())

        response = decision.auth_response()
        self.assertEqual(response.result_code, "001")
        self.assertEqual(response.identifier, id)
        self.assertEqual(response.authcode, "A12345")
        self.assertEqual(response.amount, 1395)
        self.assertTrue(validate_digest(response, self.licence_key))

    def testAuthorise3DSv2Test(self):
        id = uuid.uuid4().hex
        decision = AuthorisationAndPaymentApi(self.api_client).authorisation_request(AuthRequest(
            amount=1396,
            cardnumber="4000 0000 0000 0002",
            expmonth=12,
            expyear=2030,
            csc="123",
            identifier=id,
            merchantid=int(self.merchant_id),
            trans_type="A",
            threedsecure=ThreeDSecure(
                cp_bx="eyJhIjoiRkFwSCIsImMiOjI0LCJpIjoid3dIOTExTlBKSkdBRVhVZCIsImoiOmZhbHNlLCJsIjoiZW4tVVMiLCJoIjoxNDQwLCJ3IjoyNTYwLCJ0IjowLCJ1IjoiTW96aWxsYS81LjAgKE1hY2ludG9zaDsgSW50ZWwgTWFjIE9TIFggMTFfMl8zKSBBcHBsZVdlYktpdC81MzcuMzYgKEtIVE1MLCBsaWtlIEdlY2tvKSBDaHJvbWUvODkuMC40Mzg5LjgyIFNhZmFyaS81MzcuMzYiLCJ2IjoiMS4wLjAifQ",
                merchant_termurl="https://citypay.com/acs/return"
            )
        ))

        self.assertIsNone(decision.authen_required())
        self.assertIsNotNone(decision.request_challenged())
        self.assertIsNone(decision.auth_response())

        response = decision.request_challenged()
        self.assertIsNotNone(response.creq)
        self.assertIsNotNone(response.acs_url)
        self.assertIsNotNone(response.threedserver_trans_id)

        content = {
            "threeDSSessionData": response.threedserver_trans_id,
            "creq": response.creq
        }

        url = "https://sandbox.citypay.com/3dsv2/acs"
        headers = {'Content-type': 'application/json'}

        res = requests.post(url, data=json.dumps(content), headers=headers)
        res_obj = json.loads(res.text)

        self.assertIsNotNone(res_obj['acsTransID'])
        self.assertIsNotNone(res_obj['messageType'])
        self.assertIsNotNone(res_obj['messageVersion'])
        self.assertIsNotNone(res_obj['threeDSServerTransID'])
        self.assertIsNotNone(res_obj['transStatus'])

        c_res_auth_request = CResAuthRequest(cres=base64.b64encode(res.text.encode("ascii")).decode("ascii"))

        c_res_request_response =  AuthorisationAndPaymentApi(self.api_client).c_res_request(c_res_auth_request)

        self.assertEqual(c_res_request_response.amount, 1396)
        self.assertEqual(c_res_request_response.authcode, "A12345")
        self.assertEqual(c_res_request_response.authen_result, "Y")
        self.assertEqual(c_res_request_response.authorised, True)

    def testCardHolderAccounts(self):

        cha_id = uuid.uuid4().hex
        api = CardHolderAccountApi(self.api_client)
        result = api.account_create(AccountCreate(
            account_id=cha_id,
            contact=ContactDetails(
                address1="7 Esplanade",
                area="St Helier",
                company="CityPay Limited",
                country="JE",
                email="dev@citypay.com",
                firstname="Integration",
                lastname="Test",
                postcode="JE2 3QA"
            )
        ))

        self.assertEqual(result.account_id, cha_id)
        self.assertEqual(result.contact.address1, "7 Esplanade")

        result = api.account_card_register_request(cha_id, RegisterCard(
            cardnumber="4000 0000 0000 0002",
            expmonth=12,
            expyear=2030
        ))
        self.assertEqual(result.account_id, cha_id)
        self.assertEqual(len(result.cards), 1)
        self.assertEqual(result.cards[0].expmonth, 12)
        self.assertEqual(result.cards[0].expyear, 2030)

        result = api.account_retrieve_request(cha_id)
        self.assertEqual(result.account_id, cha_id)
        self.assertEqual(result.contact.address1, "7 Esplanade")
        self.assertEqual(len(result.cards), 1)
        self.assertEqual(result.cards[0].expmonth, 12)
        self.assertEqual(result.cards[0].expyear, 2030)

        identifier = uuid.uuid4().hex
        decision = api.charge_request(ChargeRequest(
            amount=7801,
            identifier=identifier,
            merchantid=int(self.merchant_id),
            token=result.cards[0].token,
            csc="012",
            threedsecure=ThreeDSecure(
                tds_policy="2"
            )
        ))

        self.assertIsNone(decision.authen_required())
        self.assertIsNone(decision.request_challenged())
        self.assertIsNotNone(decision.auth_response())

        response = decision.auth_response()
        self.assertEqual("001", response.result_code)
        self.assertEqual(identifier, response.identifier)
        self.assertEqual("A12345", response.authcode)
        self.assertEqual(7801, response.amount)

        # attempt with 3dsv1
        identifier = uuid.uuid4().hex
        decision = api.charge_request(ChargeRequest(
            amount=7802,
            identifier=identifier,
            merchantid=int(self.merchant_id),
            token=result.cards[0].token,
            csc="801",
            trans_type='A',
            threedsecure=ThreeDSecure(
                accept_headers="text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                merchant_termurl="https://citypay.com/example-url",
                user_agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36",
                downgrade1=True
            )
        ))

        self.assertIsNotNone(decision.authen_required())
        self.assertIsNone(decision.request_challenged())
        self.assertIsNone(decision.auth_response())

        self.assertIsNotNone(decision.authen_required().acs_url)
        self.assertIsNotNone(decision.authen_required().md)
        self.assertIsNotNone(decision.authen_required().pareq)

        result = api.account_delete_request(cha_id)
        self.assertEqual(result.code, "001")

    def tearDown(self):
        self.api_client.close()


if __name__ == '__main__':
    unittest.main()
