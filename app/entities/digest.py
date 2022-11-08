class Digest:
    class News:
        def __init__(self, title=None, content=None, date=None, url=None):
            self.title = title
            self.content = content
            self.date = date
            self.url = url

    def get_data(self):
        news = self.News()

        self.news_list.append(news)
        return

    news_list = []
