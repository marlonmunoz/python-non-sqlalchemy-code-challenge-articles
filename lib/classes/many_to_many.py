# ===================================================================================================


class Article:
    all = [] 
    
    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self._title = title
        Article.all.append(self) 
        author._articles.append(self)
        magazine._articles.append(self)

    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, value):
        if hasattr(self, '_title') and self._title is not None:
            raise AttributeError("Cannot modify title after it has been set")
        if not isinstance(value, str):
            raise ValueError("Title must be a string")
        if not 5 <= len(value) <= 50:
            raise ValueError("Title must be between 5 and 50 characters")
        self._title = value
    
    def add_author(self, author):
        if author not in self.authors:
            self.authors.append(author)
            author.add_article(self)



# ===================================================================================================


class Author:
    def __init__(self, name):
        self.name = name
        self._articles = []

    def add_article(self, magazine, title):
        # Check if an article with the same title already exists
        for article in self._articles:
            if article.title == title and article.magazine == magazine:
                return article  # Return the existing article

        # If no duplicate is found, create a new article
        article = Article(self, magazine, title)
        self._articles.append(article)
        magazine.add_article(article)
        return article

    def articles(self):
        return self._articles

    def clear_duplicates(self):
        unique_articles = []
        seen = set()
        for article in self._articles:
            identifier = (article.title, article.magazine)
            if identifier not in seen:
                unique_articles.append(article)
                seen.add(identifier)
        self._articles = unique_articles

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise ValueError("Name must be a string")
        if len(value) == 0:
            raise ValueError("Name cannot be empty")
        self._name = value

    def magazines(self):
        return list({article.magazine for article in self._articles})

    def topic_areas(self):
        if not self._articles:
            return None
        return list({article.magazine.category for article in self._articles})


# ===================================================================================================


class Magazine:
    all = [] ##

    def __init__(self, name, category):
        self.name = name
        self.category = category
        self._articles = []
        Magazine.all.append(self)

    def article_titles(self):
        return [article.title for article in self._articles] if self._articles else None

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if not isinstance(value, str):
            raise ValueError("Category must be a string")
        if len(value) == 0:
            raise ValueError("Category must have a length greater than 0")
        self._category = value

    def articles(self):
        return self._articles

    def clear_duplicates(self):
        unique_articles = []
        seen = set()
        for article in self._articles:
            identifier = (article.title, article.author)
            if identifier not in seen:
                unique_articles.append(article)
                seen.add(identifier)
        self._articles = unique_articles

    def contributors(self):
        return list({article.author for article in self._articles})

    def contributing_authors(self):
        author_count = {}
        for article in self._articles:
            author = article.author
            if author in author_count:
                author_count[author] += 1
            else:
                author_count[author] = 1
        contributing_authors = [author for author, count in author_count.items() if count > 2]
        return contributing_authors if contributing_authors else None
    
    def add_article(self, article):
        self._articles.append(article)

    @classmethod
    def top_publisher(cls):
        if not cls.all:
            return None
        return max(cls.all, key=lambda magazine: len(magazine._articles), default = None)

    


 