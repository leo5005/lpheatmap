from django.urls import path
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path("index",views.Index.as_view(), name="index"),
    path("receive-attention-data",views.receive_attention_data, name="receive-attention-data"),
    path("receive-scroll-data",views.receive_scroll_data, name="receive-scroll-data"),
    path("receive-click-data",views.receive_click_data, name="receive-click-data"),
    path("a-heatmap/<int:pk>/",views.heatmap_view, name="a-heatmap"),
    path("c-heatmap/<int:pk>/",views.click_heatmap_view, name="c-heatmap"),
    path("s-heatmap/<int:pk>/",views.scroll_heatmap_view, name="s-heatmap"),
    path('',views.HomeView.as_view(),name='home'),
    path('urlform',views.save_url,name='urlform'),
    path('urlview', views.get_url, name='urlview'),
]
