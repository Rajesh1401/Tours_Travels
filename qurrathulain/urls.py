"""qurrathulain URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from qurrathulain import view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('apt1/',view.homepage),
    path('apt2/',view.homepage),
    path('apt3/',view.localvariable),
    path('apt4/',view.globalvariable),
    path('apt5/',view.view1),
    path('apt6/',view.view2),
    path('apt7/',view.sum),
    path('apt8/',view.calculator),
    path('apt9/',view.find_biggest),
    path('apt10/',view.atm),
    path('apt11/',view.square),
    path('apt12/',view.swap_accounts),
    path('apt13/',view.biggest_number),
    path('apt14/',view.login),
    path('apt15/',view.student),
    path('apt16/',view.table),
    path('apt17/',view.student_results),
    path('apt18/',view.even),
    path('apt19/',view.testone),
    path('apt20/',view.testtwo),
    path('apt21/',view.images),
    path('apt22/',view.logo,name='logo'),
    path('apt23/',view.table1,name='table1'),
    path('apt24/',view.home,name='home'),
    path('apt25/',view.book,name='book'),
    path('apt26/',view.services,name='services'),
    path('apt27/',view.login1,name='login1'),
    path('apt28/',view.register,name='register'),
    path('apt29/',view.programming_language),
    path('apt30/',view.table2),
    path('apt31/',view.food,name='food'),
    path('apt32/',view.foodlogin,name='foodlogin'),
    path('apt33/',view.foodorder,name='foodorder'),
    path('apt34/',view.foodcontact,name='foodcontact'),
    path('apt35/',view.index,name='index'),
    path('apt36/',view.booking,name='booking'),
    path('apt37/',view.famousplaces,name='famousplaces'),
    path('apt38/',view.restaurants,name='restaurants'),
    path('apt39/',view.contactus,name='contactus'),
    path('apt40/',view.my_form),
    path('apt41/',view.drop),
    path('signin/',view.login1,name='login1'),
    path('contactus/',view.contact),
    path('booking/',view.book1),
    path('apt42/',view.payment,name='payment'),
    path('pay/',view.pay),
    path('arithmeticexception/',view.handle_arithmetic_exception),
    path('login/',view.signin,name="signin"),
    path('exc1/',view.my_view),
    path('exc2/',view.my_view1),
    path('inher/',view.result_view),
    path('inher1/',view.add_number),
    path('inher2/',view.inher),
    


]
