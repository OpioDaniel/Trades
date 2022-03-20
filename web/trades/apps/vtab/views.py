from django.shortcuts import render
from django.http import JsonResponse
from .models import Tabs


def home(request):
    return render(request, 'vtab/vtab.html', {'atm_name': 'atm'})


def tab_div_content(request):
    tab_name_ = request.POST['name']
    print(tab_name_)
    return render(request, 'vtab/include/'+tab_name_+'.html', {})


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
    def __init__(self, my_name):
        self.my_name = my_name

    def add_tab(self, params):
        tab_name = params['tab_name']
        print(tab_name)
        t, c = Tabs.objects.get_or_create(atm_name=self.my_name, tab_name=tab_name)
        print(t, c)
        results = {'status': 'ok', 'tab_id': t.id}
        return results

    def delete_tab(self, params):
        try:
            tab_name_ = params['tab_name']
            tab_to_delete = Tabs.objects.get(atm_name=self.my_name, tab_name=tab_name_)
            tab_id_ = tab_to_delete.id
            tab_to_delete.delete()
            results = {'status': 'ok', 'tab_id': tab_id_}
        except Exception as ex:
            results = {'status': 'ko', 'tab_id': "-1"}
        return results

    def get_tabs_from_table(self, params):
        tabs = Tabs.objects.filter(atm_name=self.my_name).all()
        print(9999999999999)
        print(tabs)
        results = {}
        print(results)
        print(8888888888888)
        for t in tabs:
            results[t.id] = {"tab_name": t.tab_name, "tab_text": t.tab_text, "tab_text_function": t.tab_text_function}
        return results


def activate_function(request):
    dic_ = request.POST['dic']
    dic_ = eval(dic_)
    obj_ = dic_['obj']
    fun_ = dic_['fun']
    atm_ = dic_['atm']
    params_ = dic_['params']
    s_ = obj_ + "('"+atm_+"')." + fun_ + "(params_)"
    result = eval(s_)
    # print(result)
    dic = {'status': 'ok', 'result': result}
    return JsonResponse(dic)


