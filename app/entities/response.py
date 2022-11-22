import requests
import json

from .period import Period
from .digest import Digest
from .trends import Trends
from .insights import Insights


class ResponseData:
    def __init__(self, period: Period):
        self.response = None

        self.period = period
        self.digest = None
        self.trends = None
        self.insights = None

    def get_response_by_dates(self, start_date: str, end_date: str):
        mode = "http://127.0.0.1:5000/by_dates"
        params_dict = {"start_date": start_date, "end_date": end_date}

        return self.get_response(mode, params_dict)

    def get_response_by_period(self, period: str):
        mode = "http://127.0.0.1:5000/by_period"
        params_dict = {"period": period}

        return self.get_response(mode, params_dict)

    def get_response(self, mode: str, params: dict):
        response = requests.post(mode, data=params)
        response_content = response.content.decode("utf-8")

        if is_response_correct(response.status_code):

            json_response = json.loads(response_content)
            self.parse_response(json_response)

            return self.parse_response

        else:
            return None

    def parse_response(self, response):
        self.digest = Digest(response=response)
        self.trends = Trends(response=response)
        self.insights = Insights(response=response)

        return


def is_response_correct(code):
    if code != 200:
        raise ConnectionError("Bad connection")
    else:
        return True
