from django.db import models
# Create your models here.


class BaseModel(models.Model):
    """
    Base Model, these entities will inherit to other model.
    """
    created_on = models.DateTimeField('date created', auto_now=True)
    modified_on = models.DateTimeField('date modified', auto_now_add=True)
    inactive = models.BooleanField('inactive', default=False)

    class Meta:
        ordering = ('created_on', 'modified_on', 'inactive')
        abstract = True


class Director(BaseModel):
    """
    Director Model
    """
    name = models.CharField('Name', max_length=100)
    def __str__(self):
        return '%s' % self.name


class Genre(BaseModel):
    """
    Genre Model
    """
    name = models.CharField('Name', max_length=100)
    def __str__(self):
        return '%s' % self.name


class Movie(BaseModel):
    name = models.CharField('Name', max_length=100)
    popularity = models.DecimalField('Popularity', default=0.00, max_digits=5, decimal_places=2)
    director = models.ForeignKey(Director, on_delete=models.CASCADE)
    genre = models.ManyToManyField(Genre)
    imdb_score = models.DecimalField('IMDB Score', default=0.0, max_digits=2, decimal_places=1)
    def __str__(self):
        return '%s' % self.name
