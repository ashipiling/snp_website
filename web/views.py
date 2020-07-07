from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import SNP
from django.contrib.auth.models import User

 
def index(request):
    return render(request, 'web/index.html', context={
        'title': 'CATG_SNP首页'
    })


# def index(request):
#     snp_list = SNP.objects.all()
#     return render( request, 'web/index.html', context={'welcome': snp_list} )

def analyse(request):
    text = SNP.objects.all()
    return render(request, 'web/analyse.html', context={'text': text} )

def detail_sa(request):
    snp_list = SNP.objects.all()
    return render( request, 'web/index.html', context={'welcome': snp_list} )


def detail_sm(request):
    snp_list = SNP.objects.all()
    return render( request, 'web/index.html', context={'welcome': snp_list} )


def detail_lm(request):
    snp_list = SNP.objects.all()
    return render( request, 'web/index.html', context={'welcome': snp_list} )

def upload(request):
    #待修改
    print("前端数据: ", request.POST)
    print("file:", request.FILES)
 
    for item in request.FILES:

        obj = request.FILES.get(item)      # 获取要写入的文件
        #filename = obj.name            # 获取文件名
        #f = open(filename, 'rb')

        for line in obj.chunks():

            #f.write(line)
            info = line.split()
            s = SNP(location = info[1], snp_type = info[0],
                    snp_site_1 = info[2],snp_site_2 = info[3],snp_site_3 = info[4],snp_site_4 = info[5],
                    snp_site_5 = info[6],snp_site_6 = info[7],snp_site_7 = info[8],snp_site_8 = info[9],
                    snp_site_9 = info[10],snp_site_10 = info[11],snp_site_11 = info[12],snp_site_12 = info[13],
                    snp_site_13 = info[14],snp_site_14 = info[15],snp_site_15 = info[16],snp_site_16 = info[17],)
            s.author = User.objects.get(username='luohao')
            s.save()
        #f.close()

    return HttpResponse('OK')
