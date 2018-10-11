from django.shortcuts import render


def post_list(request):
    """主页路由的试图函数"""
    return render(request, 'blog/post_list.html', {})
