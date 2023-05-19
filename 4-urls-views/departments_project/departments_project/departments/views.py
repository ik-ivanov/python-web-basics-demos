from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.http.response import Http404
from django.http import HttpResponse, HttpResponseNotFound


# Create your views here.
def old_view(request):
    return redirect('new page')


def new_view(request):
    return HttpResponse('new view!')


def department_by_slug_view(request, department_name):
    print(department_name, type(department_name))
    return HttpResponse(f'{department_name}')

# def index(request):
#     return HttpResponse('index')
#
#
# def details(request, department_id):
#     departments_map = {
#         '1': "Developers",
#         '2': "QA"
#     }
#     payload = f"Department: {departments_map.get(str(department_id), 'Unknown')}"
#     # return HttpResponse(payload)
#     # return redirect('/departments/template/', permanent=True, department_id=department_id)
#     # return redirect('https://google.bg/')
#
#     return redirect('departments template', department_id=department_id)
#
#
# def details_template(request, department_id):
#     departments_map = {
#         '1': "Developers",
#         '2': "QA"
#     }
#     payload = f"Department: {departments_map.get(str(department_id), 'Unknown')}"
#
#     context = {
#         "title": "Departments title from context",
#         "payload": payload,
#     }
#
#     return render(request, 'departments/details.html', context=context)
#
#
# def details_error(request, department_id):
#     dep = 1
#
#     if department_id == 1:
#         return HttpResponse('I have such department!')
#     else:
#         #return HttpResponseNotFound('not found, sorry')
#         return HttpResponse('not found sorry 2', status=404)
#
#     #raise Http404
#     #raise Exception('custom')

