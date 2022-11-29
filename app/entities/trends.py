class Trends:
    class Trend:
        def __init__(self, keywords: str = None, contents: list = None):
            self.keywords = keywords
            self.contents = contents
            return

    def __init__(self, response):
        self.data = []
        self.parse_data(response)

        return

    def parse_data(self, response):
        try:
            for item in response["trends"]:
                trend = self.Trend(keywords=f"{item['keywords'][0].capitalize()}, {item['keywords'][1].capitalize()}",
                                   contents=item["content"][0:3])
                self.data.append(trend)
        except Exception as err:  # Поймать нужную ошибку
            print(err)

        return
