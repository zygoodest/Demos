from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Article

# Create your views here.

def hello_world(request):
    return HttpResponse("Hello World")

def article_content(request):
    article = Article.objects.all()[0]
    title = article.title
    brief_content = article.brief_content
    content = article.content
    article_id = article.article_id
    publish_data = article.publish_date
    return_str = '''
                    title: %s,
                    brief_content: %s,
                    content: %s,
                    article_id: %s,
                    publish_date: %s
                    ''' %\
                 (title, brief_content, content, article_id, publish_data)
    return HttpResponse(return_str)


def get_index_page(request):
    all_article = Article.objects.all()
    data = {"article_list": all_article}
    return render(request, "blog/index.html", data)


def get_detail_page(request, article_id):
    all_article = Article.objects.all()
    previous_index = 0
    next_index = 0
    for index, article in enumerate(all_article):
        if article.article_id == article_id:
            curr_article = article
            previous_index = index if index == 0 else index - 1
            next_index = index if index == len(all_article) else index + 1
            break
    section_list = curr_article.content.split('\n')
    data = {
        "curr_article": curr_article,
        "section_list": section_list,
        "previous_article": all_article[previous_index],
        "next_article": all_article[next_index]
    }
    return render(request, "blog/detail.html", data)











