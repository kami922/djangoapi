from django.http import HttpResponse,JsonResponse

def hello(request):
    # return HttpResponse("Hello again <3")
    a = ["kamran","daim","qabeel","moin"]
    return JsonResponse(a,safe=False)

    