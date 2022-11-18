from .period import Period
from .get_response import get_response


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
        self.parse_data()

        return

    def parse_data(self):

        try:
            # Связь с бэком

            response = get_response()  # TODO: дописать аргументы времени

            for item in response["digest"]:
                news = self.News(title=item["content"],
                                 content="Содержание статьи",
                                 date=response["dates"]["start_date"],
                                 url=f"https://badass")
                self.data.append(news)
            ###
        except Exception as err:  # Поймать нужную ошибку при отсутствии связи с бэком
            print(err)

        return
