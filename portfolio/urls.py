from django.conf.urls.defaults import *


urlpatterns=patterns('portfolio.views',
    url(
        regex=r'^$',
        view='category_list', {
            'template_name': 'portfolio/category_list.html',
        }, name='portfolio_category_list',
    ),
    url(
        regex=r'^category/(?P<slug>[-\w]+)/$',
        view='category_detail', {
            'template_name': 'portfolio/category_detail.html',
        }, name='portfolio_category_detail',
    ),
    url(
        regex=r'^project/(?P<slug>[-\w]+)/$',
        view='project_detail', {
            'template_name': 'portfolio/project_detail.html',
        }, name='portfolio_project_detail',
    ),
    url(
        regex=r'^skill/(?P<slug>[-\w]+)/$',
        view='skill_detail', {
            'template_name': 'portfolio/skill_detail.html',
        }, name='portfolio_skill_detail',
    ),       
)
