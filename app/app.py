from entities import Period, ResponseData
from main_page import main_page
from error_page import error_page

daily_response = ResponseData(Period.DAY)
daily_response.get_response_by_period(period='day')
weekly_response = ResponseData(Period.WEEK)
weekly_response.get_response_by_period(period='week')
monthly_response = ResponseData(Period.MONTH)
monthly_response.get_response_by_period(period='month')
yearly_response = ResponseData(Period.YEAR)
yearly_response.get_response_by_period(period='year')

received_responses = [daily_response, weekly_response, monthly_response, yearly_response]

try:
    main_page(received_responses)
except Exception:
    error_page()

'''
streamlit run app/app.py
'''
