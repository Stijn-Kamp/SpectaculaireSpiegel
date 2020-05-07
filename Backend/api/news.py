from api.api_reader import ApiReader


class News:
    def __init__(self):
        raise NotImplementedError

    def get_articles(self):
        raise NotImplementedError

    class Article:
        def __init__(self, title, source, time, url):
            self.title = title
            self.source = source
            self.time = time
            self.url = url


class NewsApi(News):
    def __init__(self, apiKey, country='nl', **parameters):
        self.newsApiReader = ApiReader("https://newsapi.org/v2/top-headlines",
                                       apiKey=apiKey, country=country, **parameters)

    def get_articles(self):
        articles = self.newsApiReader.get()
        if articles is None:
            return None
        articles = articles.get("articles")
        newsItems = []
        for article in articles:
            url = article.get('url')
            title = article.get('title')
            if title:
                title = title.rsplit('-', 1)[0]  # remove source
                title = title.rsplit('|', 1)[0]  # remove category
            time = article.get('publishedAt')
            source = article.get('source')
            source = source.get('name') if source else source
            newsItems.append(self.Article(title, source, time, url))
        return self.remove_doubles(newsItems)

    @staticmethod
    def remove_doubles(array):
        """removes double values from an array, the order of the elements could differ"""
        return list(set(array))
