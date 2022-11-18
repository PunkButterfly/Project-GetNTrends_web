import requests
import json


def get_response(start_date: str = "2022-6-10", end_date: str = "2022-6-17"):
    data_dict = {"start_date": start_date, "end_date": end_date}
    response = requests.post("http://127.0.0.1:5000/by_period", data=data_dict).content.decode("utf-8")

    return json.loads(response)
