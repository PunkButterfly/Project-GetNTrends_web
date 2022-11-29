from entities import Period, ResponseData
from main_page import main_page
from error_page import error_page

try:
    # daily_response = ResponseData(Period.DAY)
    # daily_response.get_response_by_dates(start_date="2022-11-28", end_date="2022-11-29")
    # weekly_response = ResponseData(Period.WEEK)
    # weekly_response.get_response_by_dates(start_date="2022-11-28", end_date="2022-11-29")
    # monthly_response = ResponseData(Period.MONTH)
    # monthly_response.get_response_by_dates(start_date="2022-11-28", end_date="2022-11-29")
    # yearly_response = ResponseData(Period.YEAR)
    # yearly_response.get_response_by_dates(start_date="2022-11-28", end_date="2022-11-29")

    daily_response = ResponseData(Period.DAY)
    daily_response.get_response_by_period(period='day')
    weekly_response = ResponseData(Period.WEEK)
    weekly_response.get_response_by_period(period='week')
    monthly_response = ResponseData(Period.MONTH)
    monthly_response.get_response_by_period(period='month')
    # yearly_response = ResponseData(Period.YEAR)
    # yearly_response.get_response_by_period(period='year')

    received_responses = [daily_response, weekly_response, monthly_response] # yearly_response

    main_page(received_responses)

except Exception as err:
    error_page()

'''
streamlit run app/app.py
'''
