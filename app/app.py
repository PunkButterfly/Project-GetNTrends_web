from entities import ResponseData
from main_page import main_page
from error_page import error_page

try:

    default_response = ResponseData('default')
    default_response.get_response_default()

    received_responses = [default_response]
    main_page(received_responses)
except Exception:
    error_page()
