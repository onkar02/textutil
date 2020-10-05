#access the server by command python manage.py runserver


#i have created this file omkar sonawane
from django.http import HttpResponse
from django.shortcuts import render

def about(request):
    return render(request,'about.html')

def index(request):
    return render(request,'index.html')

# return HttpResponse("home")
def analyze(request):
    #get the text
    djtext=request.POST.get('text','default')#get the text written in text area or input to the variable djtext

    #check checkbox value
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    charactercounter = request.POST.get('charactercounter', 'off')

    purpose=""
    answer=djtext
    #check which checkbox is on

    if removepunc=='on':
        punctuations='''!()-[]{};:"'\,<>./?@#$^&*_~'''
        analyzed=""
        for char in djtext:
            if char not in punctuations:
                analyzed=analyzed+char
        params={'purpose':'remove punctutation','analyzed_text':analyzed}
        purpose += '|remove punctutation|'
        answer = analyzed
        # analyze the text

    if fullcaps=='on':
        analyzed=""
        for char in answer:
            analyzed=analyzed+char.upper()
        params = {'purpose': 'change to uppercase', 'analyzed_text': analyzed}
        # analyze the text
        answer=analyzed
        purpose += '|change to uppercase|'

    if newlineremover=='on':
        analyzed = ""
        for char in answer:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char
            else:
                print("no")
        params = {'purpose': 'remove NewLines', 'analyzed_text': analyzed}
        purpose += '|remove NewLines|'
        answer = analyzed
        # analyze the text

    if extraspaceremover == 'on':
        analyzed=""
        for index,char in enumerate(answer):
            if not (answer[index]== " " and answer[index+1] == " "):
                analyzed = analyzed + char
        params = {'purpose': 'remove extraspace', 'analyzed_text': analyzed}
        answer = analyzed
        purpose += '|remove extraspace|'
        # analyze the text

    if charactercounter == 'on':
        analyzed=""
        count=0
        for char in answer:
            if char==" ":
                count=count+1
        analyzed=analyzed+str(count)
        params = {'purpose': 'number of character in your text is', 'analyzed_text':analyzed}
        answer += analyzed
        purpose += '|number of character in your text is|'
        # analyze the text

    params={'purpose':purpose,'analyzed_text':answer}
    if removepunc== 'on' or fullcaps=='on' or newlineremover== 'on' or extraspaceremover == 'on' or charactercounter == 'on' :
         return render(request, 'analyze.html', params)

    else:
        return HttpResponse ("please select any of the operation and try again")
