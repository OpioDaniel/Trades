from django.shortcuts import render
from django.http import JsonResponse
from .models import Tabs


def home(request):
    return render(request, 'vtab/vtab1.html', {})


def tab_div_content(request):
    tab_name_ = request.POST['name']
    print(tab_name_)
    return render(request, 'vtab/include/'+tab_name_+'.html', {})


def add_tab(request):
    tab_name = request.POST['tab_name']
    print(tab_name)
    t, c = Tabs.objects.get_or_create(tab_name=tab_name)
    print(t, c)
    dic = {'status':'ok', 'tab_id': t.id}
    return JsonResponse(dic)


def get_tabs_from_table(request):
    tabs = Tabs.objects.all()
    dic = {}
    for t in tabs:
        dic[t.id] = {"tab_name": t.tab_name, "tab_text": t.tab_text}
    return JsonResponse(dic)


def delete_tab(request):
    try:
        tab_name_ = request.POST["tab_name"]
        tab_to_delete = Tabs.objects.get(tab_name=tab_name_)
        tab_id_ = tab_to_delete.id
        tab_to_delete.delete()
        dic = {'status': 'ok', 'tab_id': tab_id_}
    except Exception as ex:
        dic = {'status': 'ko', 'tab_id': "-1"}
    return JsonResponse(dic)


def update_text_tab(request):
    try:
        tab_id_ = request.POST["tab_id"]
        tab_value_ = request.POST["value"]
        tab_to_update = Tabs.objects.get(id=tab_id_)
        tab_to_update.tab_text = tab_value_
        tab_to_update.save()
        dic = {'status': 'ok'}
    except Exception as ex:
        dic = {'status': 'ko'}
    return JsonResponse(dic)


class AdvancedTab(object):
    def __init__(self):
        pass

    def get_tabs_from_table(request):
        tabs = Tabs.objects.all()
        dic = {}
        for t in tabs:
            dic[t.id] = {"tab_name": t.tab_name, "tab_text": t.tab_text}
        # print(dic)
        return dic

    def get_tabs(self):
        print(6666666666666)
        print(self)
        print(555555555555)
        return {'abc': 'ok'}


def activate_function(request):
    tab_name_cl_ = request.POST['tab_name_cl']
    fun_ = request.POST['fun']
    info_ = request.POST['info']
    infos_ = eval(info_)
    dic = tab_name_cl_ + '.' + fun_ + "(infos_)"
    result = eval(dic)
    # print(result)
    result_ = {'status': 'ok', 'result': result}
    return JsonResponse(result_)


