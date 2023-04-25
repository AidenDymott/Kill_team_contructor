from django.contrib import admin
from . models import Member, Kommando, Krieg, Sister, Xeno, Imperium, Chao, Kommand_list

admin.site.register(Member)
admin.site.register(Kommando)
admin.site.register(Kommand_list)
admin.site.register(Krieg)
admin.site.register(Sister)
admin.site.register(Xeno)
admin.site.register(Imperium)
admin.site.register(Chao)