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

    def get_data(self):

        try:
            ### Связь с бэком
            for i in range(0, 5):
                trend = self.Trend(title=f"Тренд {i + 1}")

                self.data.append(trend)
            ###
        except Exception as err:  # Поймать нужную ошибку при отсутствии связи с бэком
            print(err)

        return
