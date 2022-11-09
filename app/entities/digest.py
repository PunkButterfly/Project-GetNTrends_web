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

    def get_data(self) -> None:

        try:
            ### Связь с бэком
            for i in range(0, 5):
                news = self.News(title=f"Название статьи {i + 1}",
                                 content=f"Содержание статьи {i + 1}",
                                 date=f"0{i + 3}.11.22",
                                 url=f"badass:{i * 111}")

                self.data.append(news)
            ###
        except Exception as err:  # Поймать нужную ошибку при отсутствии связи с бэком
            print(err)

        return
