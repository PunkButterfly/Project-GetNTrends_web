from entities import Period, ResponseData
from main_page import main_page
from error_page import error_page

try:

    # daily_response = ResponseData(Period.DAY)
    # daily_response.get_response_by_period(period="day")
    # weekly_response = ResponseData(Period.WEEK)
    # weekly_response.get_response_by_period(period="week")
    # monthly_response = ResponseData(Period.MONTH)
    # monthly_response.get_response_by_period(period="month")
    # yearly_response = ResponseData(Period.YEAR)
    # yearly_response.get_response_by_period(period="year")

    # Получение ответа вида {"insights": [],
    # "digest": {category: {'text': [], 'channel_id': []} for category in all_cat}}
    # И его парсинг в атрибуты digest и insight
    default_response = ResponseData('default')
    default_response.get_response_default()
    # получаем response вида:
    # ResponseData.digest.data: List[News_by_category: category, content, channels]
    received_responses = [default_response]
    main_page(received_responses)
except Exception:
    error_page()
