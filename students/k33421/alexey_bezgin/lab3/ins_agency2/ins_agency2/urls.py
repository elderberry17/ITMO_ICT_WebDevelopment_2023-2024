"""
URL configuration for ins_agency2 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path

from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('same_agreement/<int:company_id>/', CompanyNotExpiredAgreementsView.as_view(),
         name='not_expired_agreements'),
    path('agents_stat/<str:start_date>/<str:end_date>/', AgentAgreementsCountView.as_view(),
         name='counter_by_agent'),
    path('collective_agreements/<int:employee_id>/',
         EmployeesInSameCompanyView.as_view(), name='unique_employees_in_collective_agreements'),
    path('payout_summary/<str:start_date>/<str:end_date>/', PayoutSummaryView.as_view(), name='payout_summary'),
    path('companies_payouts/', CompanyPayoutSummaryView.as_view(), name='payout_summary'),
    path('report/', ReportView.as_view(), name='report'),
    path('auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken'))

]
