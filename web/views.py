from django.shortcuts import render

from django.http import HttpResponse
from .models import SNP
from django.contrib.auth.models import User
from django.utils import timezone
import xlrd

def index(request):
    return render(request, 'web/index.html', context={
        'title': 'CATG_SNP'
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


    # 获取file类型的input标签值，即文件内容
    files = request.data
    file = files['file']
    workbook = xlrd.open_workbook( filename=None, file_contents=file.read() )
    sheet1 = workbook.sheet_by_index(0)  # sheet索引从0开始
    print(sheet1.name, sheet1.nrows, sheet1.ncols)

    for i in range(1, sheet1.nrows):
        info = sheet1.row_values(i)
        s = SNP(location=info[2], snp_type=int(info[1]), isolated_time=timezone.now(), created_time=timezone.now(),
                modified_time=timezone.now(),
                snp_site_1=info[4], snp_site_2=info[5], snp_site_3=info[6], snp_site_4=info[7],
                snp_site_5=info[8], snp_site_6=info[9], snp_site_7=info[10], snp_site_8=info[11],
                snp_site_9=info[12], snp_site_10=info[12], snp_site_11=info[14], snp_site_12=info[15],
                snp_site_13=info[16], snp_site_14=info[17], snp_site_15=info[18], snp_site_16=info[19], )
        s.author = User.objects.get(username='luohao')
        s.save()


    return HttpResponse('OK')

