# from django.shortcuts     import render

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
def App2TestPage(request):
    html = '''
    <h1>This is a test page App2....</h1>
    <h2>~~~~~~~~~~~~~~~~~~~~~~~~</h2>
    <hr>
    <p>try.......</p>
    
    
    <br>
    <br>
    <h3>TEST</h3>
    '''
    link_admin = True
    if link_admin:
        # template      = get_template('index.html')
        template      = get_template('testweb/Tutorial.html')
        content_posts = Post.objects.all()
        now           = datetime.now()
        html          = template.render(locals())
        return HttpResponse(html)
    else:
        return HttpResponse(html)

import random
def about(request):
    quotes = [
        '今日事，今日畢',
        '要怎麼收穫，先怎麼栽',
        '知識就是力量',
        '一個人的個性就是他的命運'
    ]
    quote = random.choice(quotes)
    return render(request, 'about.html', locals())


def LISTING(request, yr, mon, day):
    html = "<h2>List Date is {}/{}/{}</h2><hr>".format(yr, mon, day)
    return HttpResponse(html)


# https://www.cnblogs.com/komean/p/10457574.html
from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
def listing(request):
    html = '''
    <h1>django 變數傳值 : 維護中 !!!!</h1>
    '''
    # print(html)
    template = get_template("DjangoForm.html")
    user_name    =  ""
    user_city    =  ""
    user_school  =  ""
    user_email   =  ""
    user_message =  ""
    if request.method == 'POST':
        message = f'已收到您的訊息 ; 傳值方式為 : {request.method} => {request.POST["MyMSG"]}'
        form = forms.ContactForm(request.POST)
        # print(form)
        if form.is_valid():
            user_name    = form.changed_data["user_name"]
            user_city    = form.changed_data["user_city"]
            user_school  = form.changed_data["user_school"]
            user_email   = form.changed_data["user_email"]
            user_message = form.changed_data["user_message"]
    else:
        message = f"感謝您的來信   ; 傳值方式為 : {request.method}"
    log = """
        原本要用 form 的範例簡單寫個 app 但沒寫完 (目前還只能在 view 內傳值，且 POST 未能傳值成功
    """

    context = {
        "message"      : message,
        "Log"          : log,
        "user_name"    : user_name,
        "user_city"    : user_city,
        "user_school"  : user_school,
        "user_email"   : user_email,
        "user_message" : user_message,
    }
    html = template.render(context)

    return HttpResponse(html)



from django.shortcuts import redirect
def showpost(request):
    template = get_template('post.html')
    try:
        post = Product.objects.all()
        # if post != None:
        #     html = template.render(locals())
        html = template.render(locals())
        return HttpResponse(html)
    except:
        return redirect('/')
    # return('維護中....')

# def showpost(request, title):
#     template = get_template('post.html')
#     try:
#         post = Product.objects.get(title=title)
#         if post != None:
#             html = template.render(locals())
#             return HttpResponse(html)
#     except:
#         return redirect('/')
#     # return('維護中....')

def age(request):
    age_in=int(request.GET["age_in"])
    if age_in < 18:
        s="未成年"
    elif age_in >= 18 and age_in <=30:
        s="青年"
    elif age_in >=31 and age_in <=65:
        s="壯年"
    else:
        s="老年"
    return HttpResponse(f"你輸入的年齡 {age_in} 歲是{s}")

def age_form(request):
    return render(request, 'testweb/age_form.html')

def your_mail(request):
    user = str(request.POST["user"])
    mail = str(request.POST["mail"])
    
    html = f'<h1> 您好 {user} 已收到你的 mail ({mail})'
    return HttpResponse(html)

def your_mail_form(request):
    return render(request, 'testweb/your_mail_form.html')  







def orchidwebpage(request):
    html = '''
    <h1>維護中 !!!!</h1>
    '''
    template      = get_template('OrchidWebMain.html')
    content_posts = Product.objects.all()
    now           = datetime.now()
    context       = {
        "content_posts" : content_posts,
        "now"           : now,

        "HeadImgPath"   : "/static/images/forest.jpg",
        "MainTitle"     : "Phalaenopsis Breeding DataBase",
        "SubTitle"      : "Phalaenopsis AI Smart Breeding Platform"
    }
    html = template.render(context)
    
    return HttpResponse(html)






def djangoform(request):
    form = forms.ContactForm()
    return render(request, "DjangoForm.html", locals())

@csrf_exempt
def aiweblog(request):
    html = '''
    <h1>維護中 !!!!</h1>
    '''

    # SourceTemplat   = 'Bbase.html'
    template      = get_template('OrchidWebLogin.html')
    user_name     = ""
    user_password = ""
    save_login    = ""
    if request.method == 'POST':
        message = f'已收到您的訊息 ; 傳值方式為 : {self.request.method} => {self.request.POST["MyMSG"]}'
        form = forms.AiOrchidWebLogin(request.POST)
        if form.is_valid():
            user_name     = form.changed_data["user_name"]
            user_password = form.changed_data["user_password"]
            save_login    = form.changed_data["save_login"]
    else:
        # message = f"感謝您的來信   ; 傳值方式為 : {self.request.method}"
        form = forms.AiOrchidWebLogin()
    context = {
        "form"        : form,

        "HeadImgPath" : "/static/images/forest.jpg",
        "MainTitle"   : "Phalaenopsis Breeding DataBase",
        "SubTitle"    : "Phalaenopsis AI Smart Breeding Platform",
    }
    html = template.render(context)

    return HttpResponse(html)

class DbNameConvert(object):

    """Docstring for DbNameConvert. """

    def __init__(self, ModelName):
        """TODO: to be defined.

        :ModelName: TODO

        """
        self.ModelName = ModelName
        dict_convert = dict()
        dict_re_convert = dict()
        for field in ModelName._meta.fields:
            v, k = field.get_attname_column()
            dict_convert.update({k : v})
            dict_re_convert.update({v : k})

        self.dict_convert = dict_convert
        self.dict_re_convert = dict_re_convert
    def convert_obj_name(self, db_column):
        db_column = self.dict_convert[db_column]
        return db_column
    def convert_dict_object_name(self, dict_db_column):
        dict_convert_object_name = dict()
        for db_column, value in dict_db_column.items():
            object_name = self.dict_convert[db_column]
            dict_convert_object_name.update({object_name : value})
        return dict_convert_object_name
    def convert_list_object_name(self, list_db_column):
        list_convert_object_name = list()
        for db_column in list_db_column:
            object_name = self.dict_convert[db_column]
            list_convert_object_name.append(object_name)
        return list_convert_object_name
    def re_convert_list_dict_object_name(self, list_dict_db_column):
        list_dict_convert_object_name = list() 
        for list_row in list_dict_db_column:
            dict_convert_object_name = dict()
            for object_column, cell in list_row.items():
                db_column = self.dict_re_convert[object_column]
                dict_convert_object_name.update({db_column : cell})
            list_dict_convert_object_name.append(dict_convert_object_name)
        return list_dict_convert_object_name


def degradome(request):
    template = get_template('OrchidWebTable.html')
    DbConvert = DbNameConvert(Degradomeresult)
    # content_posts = DegradomeResult.objects.all()
    # list_column = [f.name for f in Degradomeresult._meta.get_fields()]
    list_column = [field.get_attname_column()[1] for field in Degradomeresult._meta.fields]
    list_column = list_column[1:] 
    # list_row = [list(i.values()) for i in list(Degradomeresult.objects.all().values())]
    # list_row = [list(i.values())[1:] for i in list(Degradomeresult.objects.all().values())]
    list_order = ['Transcript_ID', 'Cleavage_Position']
    list_order = DbConvert.convert_list_object_name(list_order)
    # set_rq_get = {'Transcript_ID', 'Cleavage_Position', 'miRNA_ID'}
    set_rq_get = {'Transcript_ID', 'Cleavage_Position', 'miRNA_ID'}
    # set_rq_get = ['Transcript_ID', 'Cleavage_Position', 'miRNA_ID']
    # set_rq_get = set(DbConvert.convert_list_object_name(set_rq_get))

    detail_page    = False
    miRNA_seq_page = False
    now_url        = request.get_full_path()
    if "detail/deg_miRNA_seq" in now_url:
        miRNA_seq_page = True
    if set_rq_get & set(request.GET):
        detail_page           = True
        GET_Transcript_ID     = str(request.GET["Transcript_ID"])
        GET_Cleavage_Position = int(
            float(
                request.GET["Cleavage_Position"]
            )
        )
        GET_miRNA_ID               = str(request.GET["miRNA_ID"])
        GET_miRNA_aligned_fragment = str(request.GET["miRNA_aligned_fragment"])
        GET_click                  = str(request.GET["click"])
        dict_filter = {
            "Transcript_ID" : GET_Transcript_ID
        }
        if GET_click == 'Cleavage_Position':
            dict_filter['Cleavage_Position'] = GET_Cleavage_Position
        dict_filter = DbConvert.convert_dict_object_name(dict_filter)
        # list_data = list(Degradomeresult.objects.filter(Transcript_ID=GET_Transcript_ID).order_by(*list_order).values())
        list_data = list(Degradomeresult.objects.filter(**dict_filter).order_by(*list_order).values())
    else:
        list_data = list(Degradomeresult.objects.all().order_by(*list_order).values())
    list_data = DbConvert.re_convert_list_dict_object_name(list_data)
    list_row                = list()
    list_col_atrr           = list()
    SelectRnaFoldGif        = ""
    list_tplot_info         = list()
    list_Selectparesnip2PDF = list()
    if miRNA_seq_page:
        SelectRnaFoldGif = GET_miRNA_ID.replace('miR', 'MIR').replace('nvL', 'NVL')+'-1.gif'
    else:
        if detail_page:
            DataSet = list_data[0]['DataSet']
            # print(DataSet)
            list_tissue = list()
            if DataSet == "FM_Only":
                list_tissue = ["FM"]
            elif DataSet == "5mmB_Only":
                list_tissue = ["5mmB"]
            elif DataSet == "FM_5mmB":
                list_tissue = ["FM", "5mmB"]
            else:
                pass
            for tissue in list_tissue:
                tplot_info = f"""
                    T-plot : 
                     Tissue={tissue},
                     Transcript_ID={GET_Transcript_ID},
                     Cleavage_Position={GET_Cleavage_Position}
                """.replace('    ', '').replace("\n", "")
                Selectparesnip2PDF = "{}_{}_CleavagePosition_{}_miRNAseq_{}_T-plots.pdf".format(
                    tissue,
                    GET_Transcript_ID,
                    GET_Cleavage_Position,
                    GET_miRNA_aligned_fragment,
                )
                list_tplot_info.append(tplot_info)
                list_Selectparesnip2PDF.append(Selectparesnip2PDF)
    for row in list_data:
        list_one_row      = list()
        
        # Transcript_ID          = row['Transcript_ID']
        # Cleavage_Position      = row['Cleavage_Position']
        # miRNA_ID               = row['miRNA_ID']
        # miRNA_aligned_fragment = row['miRNA_aligned_fragment'].replace('-', '')

        Transcript_ID          = row['Transcript_ID']
        Cleavage_Position      = row['Cleavage_Position']
        miRNA_ID               = row['miRNA_ID']
        miRNA_aligned_fragment = row['miRNA_aligned_fragment'].replace('-', '')

        if detail_page and miRNA_seq_page == False:
            if (
                Transcript_ID == GET_Transcript_ID
                and
                Cleavage_Position == GET_Cleavage_Position
            ):
                list_col_atrr.append('style="color:#c94f4f"')
            else:
                list_col_atrr.append("")
        else:
            list_col_atrr.append("")

        get_value = f"""
        ?Transcript_ID={Transcript_ID}
        &Cleavage_Position={Cleavage_Position}
        &miRNA_ID={miRNA_ID}
        &miRNA_aligned_fragment={miRNA_aligned_fragment}
        """.replace("\t", "").replace(" ", "").replace("\n", "")
        for col in row.keys():
            cell = row[col]
            if set([col]) & set_rq_get:
                if detail_page:
                    if miRNA_seq_page:
                        pass
                    else:
                        if col == 'miRNA_ID':
                            cell = f'<a href="/V3deg/detail/deg_miRNA_seq{get_value}&click={col}" target="_blank">{cell}</a>'
                else:
                    cell = f'<a href="/V3deg/detail{get_value}&click={col}" target="_blank">{cell}</a>'
            list_one_row.append(cell)
        list_row.append(list_one_row[1:])
            
    # list_col_atrr = list_col_atrr[1:]
    context = { 
        "list_column"             : list_column,
        "list_col_atrr"           : list_col_atrr,
        "list_row"                : list_row,
        "list_tplot_info"         : list_tplot_info,
        "list_Selectparesnip2PDF" : list_Selectparesnip2PDF,
        "SelectRnaFoldGif"        : SelectRnaFoldGif,
        "HeadImgPath"             : "/static/images/forest.jpg",
        "MainTitle"               : "Phalaenopsis Breeding DataBase",
        "SubTitle"                : "Phalaenopsis AI Smart Breeding Platform",
    }
    # html = template.render(locals())
    html = template.render(context)
    # print(html)
    # print(request.get_full_path())
    return HttpResponse(html)

### 寫法<2> 使用 render 渲染
#def homepage(request):
#    content_posts = Post.objects.all()
             # content_posts = Post.objects.all()[0:3]  ##  選取 list 裡面幾個
#    now = datetime.now()
#    return render(request, 'index.html', locals())
# --------------------------------------------------------
##  寫法<3> 透過 html 去印出
