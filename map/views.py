from algorithm.models import Algorithm
from map.models import Map
from utils.response import *


# Create your views here.
def create(request):
    if request.method == "POST":
        name = request.POST.get("name")
        classify = request.POST.get("classify")
        algorithm = request.POST.get("algorithm")
        video = request.POST.get("video")
        Map.objects.create(name=name, classify=classify, algorithm=algorithm, video=video)
        return success_response()
    return fail_response()


def get_list(request):
    if request.method == "GET":
        videos = Map.objects.all()
        data = []
        for video in videos:
            data.append({
                "id": video.id,
                "name": video.name,
                "classify": video.classify,
                "algorithm": video.algorithm,
                "video": video.video
            })
        return success_response(data)
    return fail_response()


def delete(request):
    if request.method == "GET":
        id = request.GET.get("id")
        Map.objects.filter(id=id).delete()
        return success_response()
    return fail_response()


def only(request):
    if request.method == "GET":
        name_list = Map.objects.values("name").distinct()
        name_list = [name["name"] for name in name_list]
        return success_response({"name_list": name_list})
    return fail_response()


def get_algorithm_list(request):
    if request.method == "GET":
        name = request.GET.get("name")
        algorithm_list = Map.objects.filter(name=name).values("algorithm", "id", "classify").distinct()
        algorithm_list = [{'name': algorithm["algorithm"], 'id': algorithm["id"], 'classify': algorithm["classify"]} for algorithm in algorithm_list]
        res = []
        for algorithm in algorithm_list:
            classify = Algorithm.objects.filter(name=algorithm["name"]).first().classify
            data = {
                "classify": classify,
                "name": f"{algorithm['classify']}-{algorithm['name']}",
                "id": algorithm["id"]
            }
            res.append(data)

        return success_response(res)
    return fail_response()


def detail(request):
    if request.method == "GET":
        id = request.GET.get("id")
        map = Map.objects.filter(id=id).first()
        data = {
            "name": map.name,
            "classify": map.classify,
            "algorithm": map.algorithm,
            "video": map.video
        }
        return success_response(data)
    return fail_response()


def video(request):
    if request.method == "GET":
        id = request.GET.get("id")
        map = Map.objects.filter(id=id).first()
        map_list = Map.objects.filter(name=map.name, algorithm=map.algorithm).all()
        res = {}
        for m in map_list:
            if m.classify == "导航视频":
                res["navigation"] = m.video
            if m.classify == "实景视频":
                res["real"] = m.video
        return success_response(res)
    return fail_response()


def globalDef(request):
    if request.method == "GET":
        name_list = Algorithm.objects.filter(classify="全局算法").values("name")
        name_list = [name["name"] for name in name_list]
        map = Map.objects.filter(algorithm__in=name_list).first()
        res = {
            "name": map.name,
            "classify": map.classify,
            "algorithm": map.algorithm,
            "video": map.video
        }
        map_list = Map.objects.filter(name=map.name, algorithm=map.algorithm).all()
        for m in map_list:
            if m.classify == "导航视频":
                res["navigation"] = m.video
            if m.classify == "实景视频":
                res["real"] = m.video
        return success_response(res)
    return fail_response()


def localDef(request):
    if request.method == "GET":
        name_list = Algorithm.objects.filter(classify="局部算法").values("name")
        name_list = [name["name"] for name in name_list]
        map = Map.objects.filter(algorithm__in=name_list).first()
        res = {
            "name": map.name,
            "classify": map.classify,
            "algorithm": map.algorithm,
            "video": map.video
        }
        map_list = Map.objects.filter(name=map.name, algorithm=map.algorithm).all()
        for m in map_list:
            if m.classify == "导航视频":
                res["navigation"] = m.video
            if m.classify == "实景视频":
                res["real"] = m.video
        return success_response(res)
    return fail_response()
