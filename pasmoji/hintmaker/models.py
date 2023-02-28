from django.db import models
from django.conf import settings
from django.db import models

class MakeHint(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='user')
    site_name = models.URLField( verbose_name='Site' )
    PASSWORD_TYPE=[
        ('Login','login'),
        ('File','file'),

    ]
    password_type=models.CharField(max_length=150,choices=PASSWORD_TYPE,verbose_name='Password type',blank=True)
    created = models.DateTimeField(auto_now_add=True,)
    updated = models.DateTimeField(auto_now=True)
    hint=models.CharField(max_length=500,verbose_name='Your hint')
    slug=models.SlugField(blank=True)
    def __str__(self):
        return f'{self.user}-{self.slug}'

    ordering = ['created']