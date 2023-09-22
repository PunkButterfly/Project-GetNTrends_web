class Insights:
    class Insight:
        def __init__(self, content: str, raw_text: list[str]):
            self.content = content
            self.raw_text = raw_text

    def __init__(self, response):
        self.data = []
        self.parse_data(response)

        return

    def parse_data(self, response):

        try:
            for item in response["insights"]:
                insight = self.Insight(content=item.get("text", None), raw_text=item.get('raw_texts', None))
                self.data.append(insight)
        except Exception as err:  # Поймать нужную ошибку
            print(err)

        return