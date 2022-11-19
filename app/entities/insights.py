from .period import Period


class Insights:
    class Insight:

        def __init__(self, title: str, date: str, url: str):
            self.title = title
            self.date = date
            self.url = url

    def __init__(self, period: Period):
        self.data = []
        self.period = period

        return
