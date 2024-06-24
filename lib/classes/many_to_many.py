class Article:
    all_articles = []

    def __init__(self, author, magazine, title):
        self._author = author
        self._magazine = magazine
        self._title = title
        Article.all_articles.append(self)
    
    @property
    def title(self):
        return self._title
    
    @property
    def author(self):
        return self._author
    
    @author.setter
    def author(self, new_author):
        if isinstance(new_author, Author):
            self._author = new_author
        else:
            raise ValueError("Author must be an instance of the Author class.")
    
    @property
    def magazine(self):
        return self._magazine
    
    @magazine.setter
    def magazine(self, new_magazine):
        if isinstance(new_magazine, Magazine):
            self._magazine = new_magazine
        else:
            raise ValueError("Magazine must be an instance of the Magazine class.")
        
class Author:
    def __init__(self, name):
        self._name = name
    
    @property
    def name(self):
        return self._name
    
    def articles(self):
        return [article for article in Article.all_articles if article.author == self]
    
    def magazines(self):
        return list(set([article.magazine for article in self.articles()]))
    
    def add_article(self, magazine, title):
        new_article = Article(self, magazine, title)
        return new_article
    
    def topic_areas(self):
        magazines = self.magazines()
        if not magazines:
            return None
        return list(set([magazine.category for magazine in magazines]))

class Magazine:
    def _init_(self, name, category):
        self._name = name
        self._category = category

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and 2 <= len(value) <= 16:
            self._name = value

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if isinstance(value, str) and len(value) > 0:
            self._category = value

    def articles(self):
        return [article for article in Article.all if article.magazine == self]

    def contributors(self):
        return list(set(article.author for article in self.articles()))

    def article_titles(self):
        titles = [article.title for article in self.articles()]
        return titles if titles else None

    def contributing_authors(self):
        author_articles = {}
        for article in self.articles():
            author = article.author
            if author not in author_articles:
                author_articles[author] = 0
            author_articles[author] += 1
        return [author for author, count in author_articles.items() if count > 2] or None

    @staticmethod
    def top_publisher():
        if not Article.all:
            return None
        magazine_article_counts = {}
        for article in Article.all:
            magazine = article.magazine
            if magazine not in magazine_article_counts:
                magazine_article_counts[magazine] = 0
            magazine_article_counts[magazine] += 1
        top_magazine = max(magazine_article_counts, key=magazine_article_counts.get)
        return top_magazine if magazine_article_counts[top_magazine] > 0 else None