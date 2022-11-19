from .period import Period


class Digest:
    class News:
        def __init__(self, title: str = None, content: str = None, date: str = None, url: str = None):
            self.title = title
            self.content = content
            self.date = date
            self.url = url

            return

    def __init__(self, period: Period):
        self.data = []
        self.period = period

        return
