from django.shortcuts import render


def landing(reques):
    return render(reques, 'main_page.html', locals())
