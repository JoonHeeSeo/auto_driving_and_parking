from mongoengine import Document, StringField, DateTimeField

class Test(Document):
    title = StringField(max_length=200)
    publication_date = DateTimeField()


