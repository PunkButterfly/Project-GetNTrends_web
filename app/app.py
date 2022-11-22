from entities import Period, ResponseData
from main_page import main_page
from error_page import error_page

try:
    daily_response = ResponseData(Period.DAY)
    daily_response.get_response_by_dates(start_date="2022-6-10", end_date="2022-6-17")
    weekly_response = ResponseData(Period.WEEK)
    weekly_response.get_response_by_dates(start_date="2022-6-10", end_date="2022-6-17")
    monthly_response = ResponseData(Period.MONTH)
    monthly_response.get_response_by_dates(start_date="2022-6-10", end_date="2022-6-17")
    yearly_response = ResponseData(Period.YEAR)
    yearly_response.get_response_by_dates(start_date="2022-6-10", end_date="2022-6-17")

    received_responses = [daily_response, weekly_response, monthly_response, yearly_response]

    main_page(received_responses)

except ConnectionError as err:
    error_page()



'''
streamlit run app/app.py
'''
