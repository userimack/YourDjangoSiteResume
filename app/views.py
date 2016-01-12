"""
Definition of views.
"""

from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime

YOUR_INFO = {
    'name' : 'Mahendra Yadav',
    'bio' : 'Dr. B. C. Roy Engineering College, Durgapur, CSE, 3rd Year',
    'email' : 'mahendra.k12@gmail.com', # Leave blank if you'd prefer not to share your email with other conference attendees
    'twitter_username' : 'userimack', # No @ symbol, just the handle.
    'github_username' : "userimack", 
    'headshot_url' : 'https://en.gravatar.com/userimack', # Link to your GitHub, Twitter, or Gravatar profile image.
}
    
def home(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/base.html',
        context_instance = RequestContext(request,
            {
                'attendee' : YOUR_INFO,    
                'year': datetime.now().year,
            })
    )