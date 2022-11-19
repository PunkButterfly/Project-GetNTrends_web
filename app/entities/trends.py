from .period import Period


class Trends:
    class Trend:
        def __init__(self, title: str = None):
            self.title = title

            return

    def __init__(self, period: Period):
        self.data = []
        self.period = period

        return
