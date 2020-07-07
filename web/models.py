from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class SNP(models.Model):
    """
    文章的数据库表稍微复杂一点，主要是涉及的字段更多。
    """
 
    # 分离地点
    location = models.CharField(verbose_name='分离地点', max_length=70)
 
    # 分离时间
    isolated_time = models.DateTimeField(verbose_name='分离时间')
    created_time = models.DateTimeField(verbose_name='创建时间', default=timezone.now)
    modified_time = models.DateTimeField(verbose_name='修改时间')
 
    # snp最终类型
    snp_type = models.IntegerField(verbose_name='snp类型')

    snp_site_1 = models.CharField(max_length = 1)
    snp_site_2 = models.CharField(max_length = 1)
    snp_site_3 = models.CharField(max_length = 1)
    snp_site_4 = models.CharField(max_length = 1)
    snp_site_5 = models.CharField(max_length = 1)
    snp_site_6 = models.CharField(max_length = 1)
    snp_site_7 = models.CharField(max_length = 1)
    snp_site_8 = models.CharField(max_length = 1)
    snp_site_9 = models.CharField(max_length = 1)
    snp_site_10 = models.CharField(max_length = 1)
    snp_site_11 = models.CharField(max_length = 1)
    snp_site_12 = models.CharField(max_length = 1)
    snp_site_13 = models.CharField(max_length = 1)
    snp_site_14 = models.CharField(max_length = 1)
    snp_site_15 = models.CharField(max_length = 1)
    snp_site_16 = models.CharField(max_length = 1)
    # 创建人名字
    author = models.ForeignKey(User,verbose_name='添加者', on_delete=models.CASCADE)
    file = models.FileField(upload_to='file/')

    class Meta:
        verbose_name = 'snp明细'
        verbose_name_plural = verbose_name

    def save(self, *args, **kwargs):
        self.modified_time = timezone.now()
        super().save(*args, **kwargs)

    def __str__(self):
        #待修改，使得输出好看
        return 'snptype: '+ str(self.snp_type)
