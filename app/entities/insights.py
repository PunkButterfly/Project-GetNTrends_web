class Insights:
    class Insight:
        def __init__(self, content: str):
            self.content = content

    def __init__(self, response):
        self.data = []
        self.parse_data(response)

        return

    def parse_data(self, response):

        try:
            for item in response["insights"]:
                insight = self.Insight(content=item["content"])
                self.data.append(insight)
        except Exception as err:  # Поймать нужную ошибку
            print(err)

        return
