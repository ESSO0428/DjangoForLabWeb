# Create your views here.



# from django.shortcuts     import render

# Create your views here.

# -----(其他)---------
# 時間需要
from datetime         import datetime
from re               import template
# 用 model
# from app2.models    import Post, Product
from app2.models      import *

# ---------------------------------------
##  寫法<2> 使用 render 直接簡短渲染寫法
from django.shortcuts import render
## render 與底下的 HttpResponse 將會將
## templete 抓來用，再回傳給使用者
# ----------------------------------------
 ##  寫法<3> 使用到 get_template  & HttpResponse
 ##   當你這個 view 有很多 templete 時候 get_template 可以幫你選版 通常是中間的 base.html
 ##   再用 HttpResponse(html) 去把你要的畫面拼出來
from django.template.loader import get_template
from django.http            import HttpResponse
from app2                   import forms
##################################
#     Create your views here.    #
##################################
##  寫法<1> 直接印 html
from django.views.decorators.csrf import csrf_exempt
# @csrf_exempt
# def aiweblog(request):
#     html = '''
#     <h1>維護中 !!!!</h1>
#     '''

#     # SourceTemplat   = 'Bbase.html'
#     template      = get_template('OrchidWebLogin.html')
#     user_name     = ""
#     user_password = ""
#     save_login    = ""
#     if request.method == 'POST':
#         message = f'已收到您的訊息 ; 傳值方式為 : {self.request.method} => {self.request.POST["MyMSG"]}'
#         form = forms.AiOrchidWebLogin(request.POST)
#         if form.is_valid():
#             user_name     = form.changed_data["user_name"]
#             user_password = form.changed_data["user_password"]
#             save_login    = form.changed_data["save_login"]
#     else:
#         # message = f"感謝您的來信   ; 傳值方式為 : {self.request.method}"
#         form = forms.AiOrchidWebLogin()
#     context = {
#         "form"        : form,

#         "HeadImgPath" : "/static/images/forest.jpg",
#         "MainTitle"   : "Phalaenopsis Breeding DataBase",
#         "SubTitle"    : "Phalaenopsis AI Smart Breeding Platform",
#     }
#     html = template.render(context)

#     return HttpResponse(html)

