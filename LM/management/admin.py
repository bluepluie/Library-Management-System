from django.contrib import admin
from management.models import *

admin.site.register(MyUser)
admin.site.register(Book)
admin.site.register(Img)
admin.site.register(BookT)
admin.site.register(Reservation)
admin.site.register(BorrowInfo)
admin.site.register(BookEval)