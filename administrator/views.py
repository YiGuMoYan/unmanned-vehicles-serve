from .models import Administrator
from utils.response import *


# Create your views here.
def login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        print(username, password)
        administrator = Administrator.objects.get(username=username)
        if administrator is None:
            return fail_response("用户不存在")

        if password != administrator.password:
            return fail_response("密码错误")

        return success_response()
    return fail_response()
