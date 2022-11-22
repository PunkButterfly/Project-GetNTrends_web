class Digest:
    class News:
        def __init__(self, title: str = None, content: str = None, date: str = None, url: str = None):
            self.title = title
            self.content = content
            self.date = date
            self.url = url

            return

    def __init__(self, response):
        self.data = []
        self.parse_data(response)

        return

    def parse_data(self, response):

        try:
            for item in response["digest"]:
                news = self.News(title=item["content"],
                                 content="Содержание статьи",
                                 date=response["dates"]["start_date"],
                                 url=f"https://badass")
                self.data.append(news)
        except Exception as err:  # Поймать нужную ошибку
            print(err)

        return
