from django.conf.urls import url

from App import views

urlpatterns = [
    url(r"^home/",views.home,name='home'),
    url(r"^cart/", views.cart, name='cart'),
    url(r"^mine/", views.mine, name='mine'),
    url(r"^market/", views.market, name='market'),
    url(r"^marketcategory/(\d+)/(\d+)/(\d+)/", views.marketCategory, name="marketcategory"),
    url(r"^login/",views.login,name='login'),
    url(r'^dologin/',views.dologin,name='dologin'),
    url(r'^quit/',views.quit,name='quit'),
    url(r"^register/",views.register,name='register'),
    url(r"^doregister/",views.doregister,name='doregister'),
    url(r'^checkusername/',views.checkusername,name='checkuserid'),
    url(r'^success/',views.success,name='success'),
    url(r'^error/',views.error,name='error'),
    url(r'^cart/',views.Cart,name='cart'),
    url(r'^addchangecart/',views.addchangecart,name='addchangecart'),
    url(r'^subchangecart/',views.subchangecart,name='subchangecart'),
]