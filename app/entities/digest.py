class Digest:
    class News:
        def __init__(self, id: int, text: str, date: str, channel_id: int):
            self.id = id
            self.text = text
            self.date = date
            self.channel_id = channel_id

    def __init__(self, response):
        self.data = {}
        self.parse_data(response)

        return

    def parse_data(self, response):

        try:
            print(response['digest'])
            for category, items in response['digest'].items():
                self.data[category] = []
                for item in items:
                    print(item)
                    news = self.News(id=item.get('id', None), text=item.get('text', None),
                                     date=item.get('date', None), channel_id=item.get('channel_id', None))
                    self.data[category].append(news)
            print(self.data)
        except Exception as err:  # Поймать нужную ошибку
            print(err)

        return