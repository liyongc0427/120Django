from django.http import HttpResponse


def about(request):
    return HttpResponse("wd")

def index(request):
    return HttpResponse("我是哒哒哒哒")

def data(request):
    import datetime
    now = datetime.datetime.now()
    return HttpResponse(now)

from django.template import Template,Context
def indexhtml(request):
    html = """
    <html>
        <head></head>
        <body>
            <h1>我是index页面</h1>
            <img src= "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1581411508987&di=cbdca7e2f9a7ec386010de592e747153&imgtype=0&src=http%3A%2F%2Fp2.img.cctvpic.com%2Fphotoworkspace%2Fcontentimg%2F2015%2F01%2F06%2F2015010611140684943.png">
        </body>
        姓名:{{ name }} 年龄:{{ age }}
    </html>
    """
    # return HttpResponse(html)
    template_ojb = Template(html)
    parmas = {"name":"大萨达","age":55}
    content_obj = Context(parmas)
    result = template_ojb.render(content_obj)
    return HttpResponse(result)

def retest(request,num):
    print(num)
    return HttpResponse("我是retest视图")

def textdemo(request,city,year):
    result = "我在%s年%s" % (year,city)
    return HttpResponse(result)

def text(request,num2,num1):
    #num1 num2 属于位置参数，只是占位而已
    result = "%s,%s" %(num1,num2)
    print(result)
    return HttpResponse(result)