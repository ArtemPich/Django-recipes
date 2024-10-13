from django.shortcuts import render


def pasta(request):
    context = {
        'pasta': {
            'макароны, г': 0.3,
            'сыр, г': 0.5
        }
    }
    return render(request, "calculator/index.html", context)


def omlet(request):
    context = {
        'omlet': {
            'яйца, шт': 2,
            'молоко, л': 0.1,
            'соль, ч.л.': 0.5
        }
    }
    return render(request, 'calculator/index.html', context)


def buter(request):
    context = {
        'buter': {
            'хлеб, ломтик': 1,
            'колбаса, ломтик': 1,
            'сыр, ломтик': 1,
            'помидор, ломтик': 1,
        }
    }
    return render(request, 'calculator/index,html', context)

