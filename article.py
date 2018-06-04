import db


class Article:

    def __init__(self, articleid, title, content, createddate, published, image, thumb, url, terms):
        self.articleid = articleid
        self.title = title
        self.content = content
        self.createddate = createddate
        self.published = published
        self.image = image
        self.thumb = thumb
        self.url = url
        self.terms = terms


def get_articles():
    result = db.get_data('''SELECT id, title, content, strftime('%Y-%m-%d %H:%M', createddate), \
                            published, image, thumb, url FROM articles''')

    articles = []
    for row in result:
        terms = db.get_data('''SELECT term FROM keyterms as kt INNER JOIN articleterms \
                        as at ON kt.id = at.termid WHERE at.articleid = ''' + str(row[0]))

        print('{0}'.format(terms[0]))
        article = Article(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], terms)

        articles.append(article)

    return articles


def get_keyterms():
    print("getting terms")
    result = db.get_data('''SELECT term FROM keyterms''')

    terms = []
    for row in result:
        print('{0}'.format(row[0]))
        term = row[0]
        terms.append(term)
    return terms
