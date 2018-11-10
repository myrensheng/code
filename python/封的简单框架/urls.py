import views

urlspattern = (
    (r'^/$',views.index),
    (r'^login/$',views.login),
    (r'^dologin/$',views.dologin),
)
# 测试pull是否可用
