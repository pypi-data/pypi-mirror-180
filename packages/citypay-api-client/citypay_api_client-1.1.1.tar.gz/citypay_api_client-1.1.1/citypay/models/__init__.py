# flake8: noqa

# import all models into this package
# if you have many models here with many references from one model to another this may
# raise a RecursionError
# to avoid this, import only the models that you directly need like:
# from from citypay.model.pet import Pet
# or import this package, but before doing it, use:
# import sys
# sys.setrecursionlimit(n)

from citypay.model.account_create import AccountCreate
from citypay.model.account_status import AccountStatus
from citypay.model.acknowledgement import Acknowledgement
from citypay.model.acl_check_request import AclCheckRequest
from citypay.model.acl_check_response_model import AclCheckResponseModel
from citypay.model.airline_advice import AirlineAdvice
from citypay.model.airline_segment import AirlineSegment
from citypay.model.auth_reference import AuthReference
from citypay.model.auth_references import AuthReferences
from citypay.model.auth_request import AuthRequest
from citypay.model.auth_response import AuthResponse
from citypay.model.authen_required import AuthenRequired
from citypay.model.batch import Batch
from citypay.model.batch_report_request import BatchReportRequest
from citypay.model.batch_report_response_model import BatchReportResponseModel
from citypay.model.batch_transaction import BatchTransaction
from citypay.model.batch_transaction_result_model import BatchTransactionResultModel
from citypay.model.bin import Bin
from citypay.model.bin_lookup import BinLookup
from citypay.model.c_res_auth_request import CResAuthRequest
from citypay.model.capture_request import CaptureRequest
from citypay.model.card import Card
from citypay.model.card_holder_account import CardHolderAccount
from citypay.model.card_status import CardStatus
from citypay.model.charge_request import ChargeRequest
from citypay.model.check_batch_status import CheckBatchStatus
from citypay.model.check_batch_status_response import CheckBatchStatusResponse
from citypay.model.contact_details import ContactDetails
from citypay.model.decision import Decision
from citypay.model.direct_post_request import DirectPostRequest
from citypay.model.direct_token_auth_request import DirectTokenAuthRequest
from citypay.model.domain_key_check_request import DomainKeyCheckRequest
from citypay.model.domain_key_request import DomainKeyRequest
from citypay.model.domain_key_response import DomainKeyResponse
from citypay.model.error import Error
from citypay.model.event_data_model import EventDataModel
from citypay.model.exists import Exists
from citypay.model.external_mpi import ExternalMPI
from citypay.model.list_merchants_response import ListMerchantsResponse
from citypay.model.mcc6012 import MCC6012
from citypay.model.merchant import Merchant
from citypay.model.pa_res_auth_request import PaResAuthRequest
from citypay.model.paylink_address import PaylinkAddress
from citypay.model.paylink_adjustment_request import PaylinkAdjustmentRequest
from citypay.model.paylink_attachment_request import PaylinkAttachmentRequest
from citypay.model.paylink_attachment_result import PaylinkAttachmentResult
from citypay.model.paylink_bill_payment_token_request import PaylinkBillPaymentTokenRequest
from citypay.model.paylink_card_holder import PaylinkCardHolder
from citypay.model.paylink_cart import PaylinkCart
from citypay.model.paylink_cart_item_model import PaylinkCartItemModel
from citypay.model.paylink_config import PaylinkConfig
from citypay.model.paylink_custom_param import PaylinkCustomParam
from citypay.model.paylink_email_notification_path import PaylinkEmailNotificationPath
from citypay.model.paylink_error_code import PaylinkErrorCode
from citypay.model.paylink_field_guard_model import PaylinkFieldGuardModel
from citypay.model.paylink_part_payments import PaylinkPartPayments
from citypay.model.paylink_sms_notification_path import PaylinkSMSNotificationPath
from citypay.model.paylink_state_event import PaylinkStateEvent
from citypay.model.paylink_token_created import PaylinkTokenCreated
from citypay.model.paylink_token_request_model import PaylinkTokenRequestModel
from citypay.model.paylink_token_status import PaylinkTokenStatus
from citypay.model.paylink_token_status_change_request import PaylinkTokenStatusChangeRequest
from citypay.model.paylink_token_status_change_response import PaylinkTokenStatusChangeResponse
from citypay.model.paylink_ui import PaylinkUI
from citypay.model.ping import Ping
from citypay.model.process_batch_request import ProcessBatchRequest
from citypay.model.process_batch_response import ProcessBatchResponse
from citypay.model.refund_request import RefundRequest
from citypay.model.register_card import RegisterCard
from citypay.model.request_challenged import RequestChallenged
from citypay.model.retrieve_request import RetrieveRequest
from citypay.model.three_d_secure import ThreeDSecure
from citypay.model.tokenisation_response_model import TokenisationResponseModel
from citypay.model.void_request import VoidRequest
