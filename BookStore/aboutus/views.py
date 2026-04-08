from django.shortcuts import render

# Create your views here.
def index(request):
    highlights = [
        {"title": "Curated Collection", "text": "We hand-pick titles that inspire thought, imagination, and growth."},
        {"title": "Reader Community", "text": "Our platform connects people who love stories and meaningful conversations."},
        {"title": "Author Discovery", "text": "We spotlight emerging and classic voices from around the world."},
    ]
    return render(request, "aboutus/index.html", context={"highlights": highlights})