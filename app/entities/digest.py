class Digest:
    class News:
        def __init__(self, title: str = None, content: str = None, date: str = None, channel: str = None):
            self.title = title
            self.content = content
            self.date = date
            self.channel = channel

            return

    def __init__(self, response):
        self.data = []
        self.parse_data(response)

        return

    def parse_data(self, response):

        try:
            for item in response["digest"]:
                news = self.News(title=item["title"],
                                 content=item["content"],
                                 # date=response["dates"]["start_date"],
                                 channel=item["channel"])
                self.data.append(news)
        except Exception as err:  # Поймать нужную ошибку
            print(err)

        return
