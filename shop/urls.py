
from django.urls import path
from . import views
urlpatterns = [
    path("",views.login,name="login"),
    path("index/<int:myid>",views.index,name="index"),
    path("createacc/",views.createacc,name="createacc"),
    path("about/",views.about,name="about"),
    path("Contact/",views.Contact,name="Contact"),
    path("quickview/<int:myid>/<int:pid>",views.quickview,name="quickview"),
    path("track/",views.track,name="track"),
    path("checkout/",views.checkout,name="checkout"),
    path("search/",views.search,name="search"),
    path("adress/<int:myid>",views.adress,name="adress"),
    path("review/<int:myid>",views.review,name="review"),
    path("payment/",views.payment,name="payment"),
    path("cart/<int:myid>",views.cart,name="cart"),
    path("info/",views.info,name="info"),
    path("su/",views.su,name="su"),
    path("loginfo/",views.loginfo,name="loginfo"),
    path("productinfo/",views.productinfo,name="productinfo"),
    path("Home/<int:myid>",views.Home,name="Home"),
    path("Home1/",views.Home1,name="Home1")
]
