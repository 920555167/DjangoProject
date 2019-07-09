import time
import calendar
from django.template import Template, Context
from django.http import HttpResponse
def index(request):
    return HttpResponse("")
def num(request,year,month,day):
    c=int(month)
    d=int(day)
    e=int(year)
    a=0
    for i in range(1,c):
        c = calendar.monthrange(e,i)
        a+=c[1]
    a=a+d
    return HttpResponse(a)
def get_time(request,m,d):
    m,d=int(m),int(d)
    struct_time=time.m,((2019,m,d,0,0,0,0,0,0))
    mktime=time.mktime(struct_time)
    local=time.localtime(mktime)
    result="%s_%s 是今年的第%s天"%(m,d,local.tm_yday)
    return HttpResponse(result)
def say(request):
    string = '''
    <html>
        <head>
            <title>
                index
            </title>
        </head>
        <body>
            <p>hello i am {{name}},i like:</p>
            {% for h in hobby %}
                <p style="color:red">{{h}}</p>
            {% endfor %}
        </body>
    </html>
    '''
    dicts = {
        "name": "张",
        "hobby": [
            "eat",
            "sing",
            "python",
            "linux"
        ]
    }
    t = Template(string)#构造模块
    c = Context(dicts)#构造字典
    result = t.render(c)#渲染
    return HttpResponse(result)

def zuo(request):
    string='''
    <html>
        <head>
            <title>
                index
            </title>
        </head>
        <body >
            <div style="background-color:black">
                {% ifequal login.password 12345  %}
                         <div style="background-color:black;display:inline-block">
                             {% for line in student %}
                                <div >
                                     <p style="float:left display:block"><img src="{{ line.picture}}" style="width:150px;height:150px;"></p>
                                     <p style="color:purple"><b>&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp{{line.name}}</b></p>
                                </div>
                             {% endfor %}
                         </div>
                         <div style="background-color:black;display:inline-block;">
                            <img src="http://shouyou.3dmgame.com/uploadimg/xiaz/2017/1227/1514362320399.png" style="width:1300px;height:1000px;position:absolute; top:10px; ">
                         </div>
                         <div style="float:right;background-color:black;display:inline-block">
                             {% for line in student1 %}
                                <div >
                                     <p style="float:right display:block"><img src="{{ line.picture}}" style="width:150px;height:150px;"></p>
                                     <p style="color:purple"><b>&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp{{line.name}}</b></p>
                                </div>
                             {% endfor %}
                         </div>
                {% else %}
                    请登出
                {% endifequal %}
            </div>
        </body>
    </html>
    '''
    dicts={
        "login":{"admin":"zhang","password":12345},
        "student":[
            {"name": "鬼切",
             "picture": "http://5b0988e595225.cdn.sohucs.com/q_70,c_zoom,w_640/images/20180730/77eb090dcc5e42f0bb35ed44ea966468.jpeg"},
            {"name": "小袖之手",
             "picture": "http://www.33lc.com/uploadfile/2018/1019/20181019105624780.jpg"},
            {"name": "青行灯",
             "picture": "http://mp.880sy.com/2016/1224/1482546288271879.png"},
            {"name": "妖刀姬",
             "picture": "http://n.sinaimg.cn/games/crawl/20161124/BXIM-fxyawmp0001466.jpg"},
            {"name":"一反木棉",
             "picture":"http://img.game333.net/uploads/newshouyou/2018/11/12/584_2018111225159636.jpg"}
        ],
        "student1": [

            {"name": "以津真天",
             "picture": "http://i.redshu.com/up/2017/d/db90a48ab0f86472"},
            {"name": "荒",
             "picture": "https://img.mp.itc.cn/upload/20170413/faf6a7cf0fac4dab9327685557c6aeea_th.jpg"},
            {"name": "般若",
             "picture": "https://i.17173cdn.com/2fhnvk/YWxqaGBf/cms3/RavmRTblqxmvDbs.jpg"},
            {"name": "一目连",
             "picture": "http://web.52pk.com/uploads/161109/42_141820_8236.jpg"},
            {"name": "姑获鸟",
             "picture": "https://img.mp.itc.cn/upload/20170705/f11c37b58c2749fe9815eef87b2d2a54_th.jpg"}
        ]
    }
    t=Template(string)
    c=Context(dicts)
    result=t.render(c)
    return HttpResponse(result)