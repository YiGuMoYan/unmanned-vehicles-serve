from algorithm.models import Algorithm
from utils.response import *


# Create your views here.
def create(request):
    if request.method == "POST":
        name = request.POST.get("name")
        classify = request.POST.get("classify")
        Algorithm.objects.create(name=name, classify=classify)
        return success_response()
    return fail_response()


def get_classify_list(request):
    if request.method == "GET":
        algorithms = Algorithm.objects.all()
        classifies = Algorithm.objects.values("classify").distinct()
        print(classifies)
        res = []
        for classify in classifies:
            data = {
                "value": classify["classify"],
                "label": classify["classify"],
                "children": []
            }
            for algorithm in algorithms:
                if algorithm.classify == classify["classify"]:
                    data["children"].append({
                        "value": algorithm.name,
                        "label": algorithm.name
                    })
            res.append(data)
        return success_response(res)
    return fail_response()


def delete(request):
    if request.method == "GET":
        id = request.GET.get("id")
        Algorithm.objects.filter(id=id).delete()
        return success_response()
    return fail_response()


def get_list(request):
    if request.method == "GET":
        algorithms = Algorithm.objects.all()
        data = []
        for algorithm in algorithms:
            data.append({
                "id": algorithm.id,
                "name": algorithm.name,
                "classify": algorithm.classify
            })
        return success_response(data)
    return fail_response()
