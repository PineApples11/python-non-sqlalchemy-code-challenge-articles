class Article:
    all = []
    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title
        Article.all.append(self)

        # many to many relationships
        self.magazine._authors.append(self.author)

        # one to many relationships
        self.magazine._articles.append(self)
        
        # many to  many relationships
        self.author._magazines.append(self.magazine)

        # one to one relationship
        self.author._articles.append(self)
    
    @property
    def title (self):
        return self._title
        

    @title.setter
    def title (self,title):
        if hasattr(self,"_title"):
             Exception 
        elif isinstance(title,str) and 5 <= len(title) <= 50:
            self._title = title
        else:
            raise Exception("The title should be longer than 5 characters and less than 50 characters")

    @property
    def author (self):
        return self._author

    @author.setter
    def author (self,author):
        if isinstance(author,Author):
            self._author = author
        else:
            raise Exception("Article's author must be a Author object")
        
    @property
    def magazine(self):
        return self._magazine
    
    @magazine.setter
    def magazine(self,magazine):
        if isinstance(magazine,Magazine):
            self._magazine = magazine
        else:
            raise Exception("Article's magazine must be a Magazine object")

class Author:
    def __init__(self, name):
        self.name = name
        self._magazines = []
        self._articles = []
    
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self,name):
        if hasattr(self,'_name'):
             Exception
        elif isinstance(name,str) and len(name) > 0:
            self._name = name
        else:
            raise Exception("The name must be more than 0 characters")
       
     

    def articles(self):
        return[article for article in Article.all if article.author == self ]
        

    def magazines(self):
        m_magazine = []
        for article in Article.all:
            if article.author == self:
                if article.magazine not in m_magazine:
                    m_magazine.append(article.magazine)
        return m_magazine
       

    def add_article(self, magazine, title):
        return Article(self,magazine,title)
        

    def topic_areas(self):
       if not self._articles:
           return None
       return list(set(magazine.category for magazine in self._magazines))
     
            
       
       
        



        

class Magazine:
    all=[]
    def __init__(self, name, category):
        self.name = name
        self.category = category
        self._authors = []
        self._articles =[]

    @property
    def name (self):
        return self._name 

    @name.setter
    def name (self,name):
        if isinstance(name,str) and 2 <= len(name) <= 16:
            self._name = name

    
    @property
    def category(self):
        return self._category
        

    @category.setter
    def category(self,category):
        if isinstance(category,str) and len(category) > 0:
            self._category = category
        

    def articles(self):
        return [article for article in Article.all if article.magazine == self]
        pass

    def contributors(self):
        return list(set(self._authors))
        # c_contributors = []
        # for article in Article.all:
        #     if article.author == self:
        #         if article.contributor not in c_contributors:
        #             c_contributors.append(article.contributor)
        # return set(c_contributors)


        pass

    def article_titles(self):
        return [article.title for article in self._articles] if self._articles else None
        pass

    def contributing_authors(self):
        c_contributors = []
        author_count ={}
        for article in Article.all:
            if article.magazine == self:
                if article.author in author_count:
                    author_count[article.author] += 1
                else:
                    author_count[article.author] = 1
        for author,count in author_count.items():
            if count > 2:
                c_contributors.append(author)
        return c_contributors if c_contributors else None
        

        

      
        pass