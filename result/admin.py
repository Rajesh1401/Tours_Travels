from django.contrib import admin
from result.models import Login
from result.models import Contactus
from result.models import Booking
from result.models import Payment
from result.models import Signin
class Saveenquiry(admin.ModelAdmin):
    en=('lemail','lpassword')
admin.site.register(Login,Saveenquiry)

class Saveenquiry(admin.ModelAdmin):
    en=('customer_name','mobile_number','email_id','query_text')
admin.site.register(Contactus,Saveenquiry)

class Saveenquiry(admin.ModelAdmin):
    en=('location','destination')
admin.site.register(Booking,Saveenquiry)

class Saveenquiry(admin.ModelAdmin):
    en=('name','card','number','expiry','cvv')
admin.site.register(Payment,Saveenquiry)

class Saveenquiry(admin.ModelAdmin):
    en=('suname','suemail','supassword')
admin.site.register(Signin,Saveenquiry)
# Register your models here.
