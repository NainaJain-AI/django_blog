from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

def user_journal_image_path(instance, filename):
    """
    Generate a user-specific upload path for journal entry images.
    """
    # Return the path where the file will be stored
    return f'journal_images/{instance.user.id}/{filename}'

class JournalEntry(models.Model):
    """
    Model representing a daily journal entry.
    
    Allows users to record their daily thoughts and feelings with a title,
    content, mood, and optional tags.
    """
    # Mood choices for the dropdown
    # Mood choices for the dropdown
    MOOD_CHOICES = [
        ('😊 Happy', 'Happy'),
        ('😐 Neutral', 'Neutral'),
        ('😔 Sad', 'Sad'),
        ('😡 Angry', 'Angry'),
        ('😴 Tired', 'Tired'),
        ('🤩 Excited', 'Excited'),
    ]
    
    # Weather choices for the dropdown
    WEATHER_CHOICES = [
        ('☀️ Sunny', 'Sunny'),
        ('🌤️ Partly Cloudy', 'Partly Cloudy'),
        ('☁️ Cloudy', 'Cloudy'),
        ('🌧️ Rainy', 'Rainy'),
        ('⛈️ Stormy', 'Stormy'),
        ('❄️ Snowy', 'Snowy'),
        ('🌫️ Foggy', 'Foggy'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE, help_text="The user who created this journal entry")
    date = models.DateField(default=timezone.now, help_text="Date of the journal entry")
    title = models.CharField(max_length=200, help_text="Title of the journal entry")
    content = models.TextField(help_text="Main content of the journal entry")
    mood = models.CharField(max_length=50, blank=True, choices=MOOD_CHOICES, help_text="How you were feeling")
    tags = models.CharField(max_length=200, blank=True, help_text="Space-separated tags to categorize entries")
    
    # New fields
    created_at = models.DateTimeField(default=timezone.now, help_text="When this entry was first created")
    updated_at = models.DateTimeField(default=timezone.now, help_text="When this entry was last updated")
    image = models.ImageField(upload_to=user_journal_image_path, blank=True, null=True, help_text="An image to attach to your journal entry")
    is_private = models.BooleanField(default=True, help_text="Whether this entry is private or can be viewed by others")
    weather = models.CharField(max_length=50, blank=True, choices=WEATHER_CHOICES, help_text="The weather on this day")

    class Meta:
        ordering = ['-date']
        verbose_name_plural = "Journal Entries"

    def __str__(self):
        return f"{self.date} - {self.title}"    