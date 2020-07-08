from django.shortcuts import render

from django.http import HttpResponse
from .models import SNP
from django.contrib.auth.models import User
from django.utils import timezone


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
    print("前端数据: ", request.POST)
    print("file:", request.FILES)
 
    for item in request.FILES:

        obj = request.FILES.get(item)

        for line in obj.chunks():
            info = line.split()
            s = SNP(location = info[1], snp_type = info[0], isolated_time = timezone.now(),created_time =timezone.now() , modified_time =timezone.now(),
                    snp_site_1 = info[2],snp_site_2 = info[3],snp_site_3 = info[4],snp_site_4 = info[5],
                    snp_site_5 = info[6],snp_site_6 = info[7],snp_site_7 = info[8],snp_site_8 = info[9],
                    snp_site_9 = info[10],snp_site_10 = info[11],snp_site_11 = info[12],snp_site_12 = info[13],
                    snp_site_13 = info[14],snp_site_14 = info[15],snp_site_15 = info[16],snp_site_16 = info[17],)
            s.author = User.objects.get(username='luohao')
            s.save()

    return HttpResponse('OK')
