from __future__ import annotations

class Digest:
    class News:
        def __init__(self, title: str = None, content: str = None, date: str = None, channel: str = None):
            self.title = title
            self.content = content
            self.date = date
            self.channel = channel

            return

    class News_by_category:
        def __init__(self, category: str = None, content: list[str] = None, channels: list[str] = None):
            self.category = category
            self.content = content
            self.channels = channels

            return

    def __init__(self, response):
        self.data = []
        self.all_categories = []
        self.not_empty_cat_info = []
        self.perse_data_categories(response)
        #self.parse_data(response)

        return

    def perse_data_categories(self, response):
        try:
            for category, category_info in response["digest"].items():
                news_per_cat = self.News_by_category(category=category,
                                                     content=category_info.get('text'),
                                                     channels=category_info.get('channel_id'))
                if len(category_info['text']):
                    self.not_empty_cat_info.append(category)
                self.all_categories.append(category)
                self.data.append(news_per_cat)

        except Exception as err:
            print(err)

        return

    def parse_data(self, response):

        try:
            for item in response["digest"]:
                news = self.News(#title=item.get("title", None),
                                 content=item["text"]
                                 # date=response["dates"]["start_date"],
                                 #channel=item["channel"]
                                 )
                self.data.append(news)
        except Exception as err:  # Поймать нужную ошибку
            print(err)

        return
