from diary.models import Page
import random

def validate_pages():
    pages = Page.objects.all()

    for page in pages:
        if page.score < 0 or page.score > 10:
            page.score = random.randint(1, 10)
            page.save()