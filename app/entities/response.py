import requests
import json
import datetime as dt

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
        mode = "http://158.160.21.26:80/by_dates"
        params_dict = {"start_date": start_date, "end_date": end_date}

        received_response = self.get_response(mode, params_dict)

        return received_response

    def get_response_by_period(self, period: str):
        mode = "http://158.160.21.26:80/by_period"
        params_dict = {"period": period}

        received_response = self.get_response(mode, params_dict)

        return received_response

    def get_response_default(self):
        mode = "http://127.0.0.1:5000/default"
        params_dict = {}
        received_response = self.get_response(mode, params_dict)
        return received_response

    def get_response(self, mode: str, params: dict):

        response = requests.post(mode, data=params)
        print(response)

        response_content = response.content.decode("utf-8")

        if is_response_correct(response.status_code):

            json_response = json.loads(response_content)
            self.parse_response(json_response)

            return self.parse_response

        else:
            return None

    def parse_response(self, response):
        self.digest = Digest(response=response)
        #self.trends = Trends(response=response)
        self.insights = Insights(response=response)
        return


def is_response_correct(code):
    if code != 200:
        raise ConnectionError("Error connection")
    else:
        return True


def count_days_by_mode(mode: str) -> int:
    if mode == "day":
        return 1
    if mode == "week":
        return 7
    if mode == "month":
        return 30
    if mode == "year":
        return 365
