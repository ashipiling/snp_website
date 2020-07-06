from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import SNP
 
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

def upload_lh(request):
    #待修改
    print("前端数据: ", request.POST)
    print("file:", request.FILES)
 
    for item in request.FILES:
        obj = request.FILES.get(item)      # 获取要写入的文件
        filename = obj.name            # 获取文件名
        f = open(filename, 'rb')
        for line in obj.chunks():      # 分块写入
            f.write(line)
        f.close()
 
    return render(request, "index.html")
