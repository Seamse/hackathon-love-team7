from django.db import models
from django.contrib.auth.models import User


class Letter(models.Model):
    """
    A class for the Letter model
    """
    body = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="bottle_letter"
    )
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        """
        Ordering by descending order
        """
        ordering = ["-created_on"]

    def __str__(self):
        """
        Returns the letter body string
        Args:
            self (object): self.
        Returns:
            The letter body string
        """
        return str(self.body)


class Reply(models.Model):
    """
    A class for the Reply model
    """
    letter = models.ForeignKey(Letter, on_delete=models.CASCADE,
                               related_name="replys")
    name = models.CharField(max_length=80)
    body = models.CharField(max_length=100, unique=True)
    created_on = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(
        User, related_name='bottlereply_like', blank=True)

    class Meta:
        """
        Ordering by ascending order
        """
        ordering = ["created_on"]

    def __str__(self):
        """
        Returns the reply name string
        Args:
            self (object): self.
        Returns:
            The reply body by name string
        """
        return f"Reply {self.body} by {self.name}"
