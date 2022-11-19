import requests
import json

from .digest import Digest
from .trends import Trends
from .insights import Insights
from .period import Period


class Response:
    def __init__(self, period: Period):
        self.response = None
        self.digest = None
        self.insights = None
        self.trends = None
        self.period = period

        self.get_response()

        self.parse_digest()
        self.parse_trends()
        self.parse_insights()

        return

    def get_response(self):
        # TODO: написать нормально через mode
        start_date = "2022-6-10"
        end_date = "2022-6-17"
        period = self.period
        try:
            data_dict = {"start_date": start_date, "end_date": end_date}
            response = requests.post("http://127.0.0.1:5000/by_period", data=data_dict).content.decode("utf-8")
        except Exception as err:  # Поймать нужную ошибку при отсутствии связи с бэком
            print(err)
            return None

        self.response = json.loads(response)

        return

    def parse_digest(self) -> Digest:
        digest = Digest(self.period)

        for item in self.response["digest"]:
            news = Digest.News(title=item["content"],
                               content="Содержание статьи",
                               date=self.response["dates"]["start_date"],
                               url=f"https://badass")
            digest.data.append(news)

        self.digest = digest

        return self.digest

    def parse_trends(self) -> Trends:
        trends = Trends(self.period)

        for item in range(0, 5):
            trend = Trends.Trend(title=f"Тренд {item + 1}")

            trends.data.append(trend)

        self.trends = trends

        return self.trends

    def parse_insights(self) -> Insights:
        insights = Insights(self.period)

        print(self.response["insights"])

        for item in self.response["insights"]:
            insight = Insights.Insight(title=item["content"],
                                       date=self.response["dates"]["start_date"],
                                       url="http://badass")
            insights.data.append(insight)

        self.insights = insights

        return self.insights
