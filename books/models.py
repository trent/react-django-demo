from django.db import models

class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    class Meta(object):
        ordering = ('last_name', 'first_name')

    def __unicode__(self):
        return "{}, {}".format(self.last_name, self.first_name)

class Book(models.Model):
    CATEGORY_CHOICES = (
            ('Autobiography', 'Autobiography'),
            ('Biography', 'Biography'),
            ('Fiction', 'Fiction'),
            ('Non-Fiction', 'Non-Fiction'),
            ('Play', 'Play'),
            ('foo', 'foo'),
        )
    name = models.CharField(max_length=200)
    author = models.ForeignKey(Author)
    publish_date = models.DateField()
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)

    class Meta(object):
        ordering = ('name',)

    def __unicode__(self):
        return self.name