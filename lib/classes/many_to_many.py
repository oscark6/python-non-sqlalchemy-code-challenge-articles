class Article:
    all = []

    def _init_(self, author, magazine, title):
        if not isinstance(author, Author):
            raise TypeError("author must be of type Author")
        if not isinstance(magazine, Magazine):
            raise TypeError("magazine must be of type Magazine")
        if not isinstance(title, str) or not (5 <= len(title)<= 50):
            raise TypeError("title must be a string between 5 and 50 characters")
        self._author = author
        self._magazine = magazine
        self.title = title
        Article.all.append(self)
        author._articles.append(self)
        magazine._articles.append(self)

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        if not isinstance(value, Author):
            raise ValueError("author must be of type Author")
        self._author = value

    @property
    def magazine(self):
        return self._magazine

    @magazine.setter
    def magazine(self, value):
        if not isinstance(value, Magazine):
            raise ValueError("magazine must be of type Magazine")
        self._magazine = value
        
class Author:
    def _init_(self, name):
        if not isinstance(name, str):
            raise TypeError("name must be a string")
        if len(name) == 0:
            raise ValueError("name cannot be empty")
        self._name = name
        self._articles = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        raise AttributeError("cannot set name")

    def articles(self):
        return self._articles

    def magazines(self):
        return list({article.magazine for article in self.articles()})

    def add_article(self, magazine, title):
        article = Article(self, magazine, title)
        return article

    def topic_areas(self):
        categories = list(set(article.magazine.category for article in self._articles))
        if categories:
          return categories
        else:
          return None

class Magazine:

    all = []
    
    def _init_(self, name, category):
        if not isinstance(name, str) or not (2 <= len(name) <= 16):
            raise ValueError("name must be a string between 2 and 16 characters")
        self.name = name
        if not isinstance(category, str) or len(category) == 0:
            raise ValueError("category must be a non-empty string")
        self.category = category
        self._articles = []
        Magazine.all.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or not (2 <= len(value) <= 16):
            raise ValueError("Name must be a string between 2 and 16 characters")
        self._name = value

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if not isinstance(value, str) or len(value) == 0:
            raise ValueError("Category must be a non-empty string")
        self._category = value

    def articles(self):
        return self._articles

    def contributors(self):
        return list({article.author for article in self.articles()})

    def article_titles(self):
        titles = [articles.title for articles in self.articles()]
        return titles if titles else None

    def contributing_authors(self):
        author_article_count = {}
        for article in self.articles():
            author = article.author
            if author in author_article_count:
                author_article_count[author] += 1
            else:
                author_article_count[author] = 1

        contributing_authors = [author for author, count in author_article_count.items() if count > 2]
        return contributing_authors if contributing_authors else None