from entities import Period, ResponseData
from main_page import main_page
from error_page import error_page

try:

    daily_response = ResponseData(Period.DAY)
    daily_response.get_response_by_dates(start_date="2022-11-30", end_date="2022-12-01")
    weekly_response = ResponseData(Period.WEEK)
    weekly_response.get_response_by_dates(start_date="2022-11-24", end_date="2022-12-01")
    monthly_response = ResponseData(Period.MONTH)
    monthly_response.get_response_by_dates(start_date="2022-11-01", end_date="2022-12-01")
    yearly_response = ResponseData(Period.YEAR)
    yearly_response.get_response_by_dates(start_date="2021-12-01", end_date="2022-12-01")

    received_responses = [daily_response, weekly_response, monthly_response, yearly_response]

    main_page(received_responses)
except Exception:
    error_page()
