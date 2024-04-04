from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.utils import timezone



class Author(models.Model):
    
    """
    Model representing an Author.
    """  
    author = models.OneToOneField(get_user_model(),on_delete=models.CASCADE, )
    salutation = models.CharField(max_length=200)
    pics = models.ImageField(upload_to="author_headshots/", blank=True)

    def __str__(self):
        return self.author.username


class Genre(models.Model):
    """
    Model representing a book genre.
    """
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Book(models.Model):
    
    """
    Model representing a book (e.g., a novel, non-fiction, etc.).
    """
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
    genre = models.ManyToManyField(Genre)
    description = models.TextField()
    price= models.DecimalField(max_digits=6, decimal_places=2)
    cover= models.ImageField(upload_to="covers/",  blank=True)
    publish_date = models.DateTimeField(default=timezone.now, editable=False)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-publish_date']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        """
        Returns the canonical URL for a book detail view.
        """
        return reverse("book_detail", kwargs={"pk": self.pk})
    


class Review (models.Model):
    """
    Model representing a review for a book.
    """

    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='reviews')
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='reviews')
    content = models.TextField()
    rating = models.IntegerField()  # Assuming rating is an integer value representing a score
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
       return self.content

