from django import forms
from django.utils import timezone
from datetime import date
import re

from .models import JournalEntry


class JournalForm(forms.ModelForm):
    """
    Form for creating and editing journal entries.
    
    This form handles validation for the JournalEntry model and provides
    customized widgets and labels for a better user experience.
    """
    
    class Meta:
        model = JournalEntry
        fields = ['date', 'title', 'content', 'mood', 'tags']
        widgets = {
            'date': forms.DateInput(
                attrs={
                    'type': 'date',
                    'class': 'form-control',
                    'placeholder': 'Select date'
                }
            ),
            'title': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Entry title'
                }
            ),
            'content': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'rows': 10,
                    'placeholder': 'Write your thoughts here...'
                }
            ),
            'mood': forms.Select(
                attrs={
                    'class': 'form-control'
                }
            ),
            'tags': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'space separated tags'
                }
            )
        }
        labels = {
            'date': 'Entry Date',
            'title': 'Title',
            'content': 'Journal Content',
            'mood': 'How are you feeling?',
            'tags': 'Tags'
        }
        help_texts = {
            'tags': 'Separate tags with spaces (e.g. "work personal growth")'
        }

    def __init__(self, *args, **kwargs):
        """
        Initialize the form with customized choices for mood and default date.
        """
        super().__init__(*args, **kwargs)
        
        # Add empty option to mood choices
        mood_choices = [('', 'Select mood')] + list(JournalEntry.MOOD_CHOICES)
        self.fields['mood'].widget.choices = mood_choices
        
        # Set default date for new entries
        if not self.instance.pk:  # Only for new entries
            self.initial['date'] = timezone.now().date()
    
    def clean_date(self):
        """
        Validate that the date is not in the future.
        """
        entry_date = self.cleaned_data.get('date')
        
        if entry_date and entry_date > date.today():
            raise forms.ValidationError("You cannot create journal entries for future dates.")
            
        return entry_date
    
    def clean_tags(self):
        """
        Validate that tags contain only letters, numbers, and spaces.
        """
        tags = self.cleaned_data.get('tags')
        
        if tags:
            # Check that tags contain only alphanumeric characters and spaces
            if not re.match(r'^[a-zA-Z0-9\s]+$', tags):
                raise forms.ValidationError(
                    "Tags can only contain letters, numbers, and spaces."
                )
                
            # Ensure no tag is longer than 20 characters
            for tag in tags.split():
                if len(tag) > 20:
                    raise forms.ValidationError(
                        f"Tag '{tag}' is too long. Tags must be 20 characters or less."
                    )
                    
        return tags
