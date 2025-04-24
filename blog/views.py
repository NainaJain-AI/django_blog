# Standard library imports
from django.http import HttpResponseServerError
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Local application imports
from .models import JournalEntry
from .forms import JournalForm

def welcome(request):
    """
    Display the welcome/landing page of the journal application.
    
    This view serves as the entry point to the application, providing 
    information about the journal functionality and prompting users to log in.
    
    Args:
        request: The HTTP request
        
    Returns:
        Rendered HTML welcome page
    """
    # Count stats if user is authenticated
    stats = {}
    if request.user.is_authenticated:
        # Get some stats for the user's journal entries
        entry_count = JournalEntry.objects.filter(user=request.user).count()
        stats = {
            'entry_count': entry_count,
            'user_name': request.user.username,
        }
    
    return render(request, 'blog/welcome.html', {'stats': stats})

@login_required
def journal(request):
    """
    Display all journal entries for the logged-in user with pagination.
    
    Args:
        request: The HTTP request
        
    Returns:
        Rendered HTML page with paginated entries
    """
    # Get all entries for the current user
    entry_list = JournalEntry.objects.filter(user=request.user).order_by('-date')
    
    # Set up pagination - 10 entries per page
    paginator = Paginator(entry_list, 10)
    page = request.GET.get('page', 1)
    
    try:
        entries = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page
        entries = paginator.page(1)
    except EmptyPage:
        # If page is out of range, deliver last page of results
        entries = paginator.page(paginator.num_pages)
        
    return render(request, 'blog/journal.html', {'entries': entries})

@login_required
def add_entry(request):
    """
    Add a new journal entry.
    
    Args:
        request: The HTTP request
        
    Returns:
        Redirect to journal list on success or form with errors
    """
    if request.method == 'POST':
        form = JournalForm(request.POST)
        if form.is_valid():
            try:
                entry = form.save(commit=False)
                entry.user = request.user
                entry.save()
                return redirect('journal')
            except Exception as e:
                # Log the error and return a server error response
                print(f"Error saving journal entry: {e}")
                return HttpResponseServerError("An error occurred while saving your entry.")
    else:
        # For new form, default to today's date
        form = JournalForm(initial={'date': timezone.now().date()})
        
    return render(request, 'blog/add_entry.html', {'form': form})

@login_required
def edit_entry(request, entry_id):
    """
    Edit an existing journal entry.
    
    Args:
        request: The HTTP request
        entry_id: ID of the entry to edit
        
    Returns:
        Redirect to journal list on success or form with errors
    """
    # Get the entry or return 404 if not found
    entry = get_object_or_404(JournalEntry, id=entry_id, user=request.user)
    
    if request.method == 'POST':
        form = JournalForm(request.POST, instance=entry)
        if form.is_valid():
            try:
                form.save()
                return redirect('journal')
            except Exception as e:
                print(f"Error updating journal entry: {e}")
                return HttpResponseServerError("An error occurred while updating your entry.")
    else:
        form = JournalForm(instance=entry)
    
    return render(request, 'blog/edit_entry.html', {'form': form, 'entry': entry})
