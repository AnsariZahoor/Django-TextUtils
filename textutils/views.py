from django.http import HttpResponse
from django.shortcuts import render


# def index(request):
#     return HttpResponse("Hello world")

def index(request):
    return render(request, 'index.html')


def analyze(request):
    # get the text
    djtext = request.POST.get('text', 'default')

    # check with checkbox on
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    lenoftext = request.POST.get('lenoftext', 'off')

    if removepunc != 'off':
        punctuations = '''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
        analyzed = ''
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char

        params = {'purpose': 'Remove Punctuations', 'analyzed_text': analyzed, 'original_text':djtext}
        djtext = analyzed
        # return render(request, 'index.html', params)

    if fullcaps != 'off':
        analyzed = ''
        for char in djtext:
            analyzed = analyzed + char.upper()

        params = {'purpose': 'UPPERCASE', 'analyzed_text': analyzed, 'original_text':djtext}
        djtext = analyzed
        # return render(request, 'index.html', params)

    if extraspaceremover == 'on':
        analyzed = ''
        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1] == " "):
                analyzed = analyzed + char

        params = {'purpose': 'Extra space removed', 'analyzed_text': analyzed, 'original_text':djtext}
        djtext = analyzed
        # return render(request, 'index.html', params)

    if lenoftext == 'on':
        analyzed = len(djtext)
        params = {'purpose': 'Number of letters', 'analyzed_text': analyzed, 'original_text': djtext}
        # return render(request, 'index.html', params)

    if removepunc != 'on' and fullcaps != 'on' and extraspaceremover != 'on' and lenoftext != 'on':
        return render(request, 'index.html')

    return render(request, 'index.html', params)