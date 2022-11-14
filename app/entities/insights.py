from .period import Period


class Insights:
    class Insight:
        class Source:
            def __init__(self, title: str = None, content: str = None, date: str = None, url: str = None):
                self.title = title
                self.content = content
                self.date = date
                self.url = url

                return

        def __init__(self, header: str, sources: list):
            self.header = header
            self.sources = sources

    def __init__(self, period: Period):
        self.data = []
        self.period = period

        return

    def get_data(self):

        try:
            ### Связь с бэком
            news_in_insight = 5
            number_of_insights = 3
            for i in range(0, number_of_insights):
                insight_sources = []
                insight_header = f"Инсайт {i + 1}"
                for j in range(0, news_in_insight):
                    source = self.Insight.Source(title=f"Источник инсайта {j + 1}",
                                                 content=f"Содержание источника {j + 1}",
                                                 date=f"0{j + 3}.11.22",
                                                 url=f"badass:{j * 111}")

                    insight_sources.append(source)
                insight = self.Insight(insight_header, insight_sources)
                self.data.append(insight)
            ###
        except Exception as err:  # Поймать нужную ошибку при отсутствии связи с бэком
            print(err)

        return
