from django.db import models

class Film(models.Model):
  GENRE = (
    ('horror', 'horror'),
    ('comedy', 'comedy'),
  )
  image = models.ImageField(upload_to='film/')
  title = models.CharField(max_length=100)
  created_at = models.DateTimeField(auto_now_add=True)
  genre = models.CharField(max_length=100, choices=GENRE)
  description = models.TextField()
  trailer = models.URLField()

  def __str__(self):
    return self.title
