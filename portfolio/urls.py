from django.conf.urls.defaults import *


urlpatterns=patterns('portfolio.views',
    url(r'^category/$',
        'category_list', {
            'template_name': 'portfolio/category_list.html',
        }, name='portfolio_category_list',
    ),
    url(r'^category/(?P<slug>[-\w]+)/$',
        'category_detail', {
            'template_name': 'portfolio/category_detail.html',
        }, name='portfolio_category_detail',
    ),
    url(r'^skill/(?P<slug>[-\w]+)/$',
        'skill_detail', {
            'template_name': 'portfolio/skill_detail.html',
        }, name='portfolio_skill_detail',
    ),
    url(r'^project/(?P<slug>[-\w]+)/$',
        'project_detail', {
            'template_name': 'portfolio/project_detail.html',
        }, name='portfolio_project_detail',
    ),
    url(r'^$',
        'project_list', {
            'template_name': 'portfolio/project_list.html',
        }, name='portfolio_project_list',
    ),
)
