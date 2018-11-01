import views

urlspattern = (
    (r'^/$',views.index),
    (r'^login/$',views.login),
    (r'^dologin/$',views.dologin),
)