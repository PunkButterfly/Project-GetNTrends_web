class Trends:
    class Trend:
        def __init__(self, title: str = None):
            self.title = title

            return

    def __init__(self, response):
        self.data = []
        self.parse_data(response)

        return

    def parse_data(self, response):
        # TODO: Дописать парсер
        try:
            for i in range(0, 5):
                trend = self.Trend(title=f"Тренд {i + 1}")

                self.data.append(trend)
        except Exception as err:  # Поймать нужную ошибку
            print(err)

        return
