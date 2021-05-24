from .models import URL


def FullURLDuble(self):
    return URL.objects.filter(full_url=self).count()