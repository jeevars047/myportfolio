from django.contrib import admin
from portfolioapp.models import Portfolio

class PortfolioAdmin(admin.ModelAdmin):
    list_display = ['name','email','mobile']
admin.site.register(Portfolio,PortfolioAdmin)
