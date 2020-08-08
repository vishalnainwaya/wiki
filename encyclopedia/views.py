from django.shortcuts import render
import markdown2
from . import util
import random
from django.http import HttpResponseRedirect
from django.urls  import reverse


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def link(request, link):
    if util.get_entry(link):
        content = markdown2.markdown(util.get_entry(link))
    else:
        content = None
    return  render(request, "encyclopedia/link.html",{
        "link": link , "content": content
    })

def randpg(request):
    link = random.choice(util.list_entries())
    return HttpResponseRedirect(reverse("link", kwargs = {"link":link}))

def search(request):
    query = request.POST["q"]
    entryList = util.list_entries()

    if query in entryList:
        return HttpResponseRedirect(reverse("link",kwargs={"link":query}))
    else:
        newList = []
        for entry in entryList:
            if query.lower() in entry.lower():
                newList.append(entry)
        return render(request,"encyclopedia/result.html",{
            "newList": newList
        })

def create(request):
    if request.method=="GET":
        return render(request,"encyclopedia/create.html")
    
    title = request.POST["title"]
    content = request.POST["pagecontent"]

    if util.get_entry(title):
        return render(request,"encyclopedia/create.html",{
            "error": "An entry already available , Please try again "
        })
    util.save_entry(title,content)

    return HttpResponseRedirect(reverse("link",kwargs={"link":title}))

def edit(request,link):
    content = util.get_entry(link)

    if request.method == "GET":
        return render(request, "encyclopedia/edit.html",{
            "link":link, "content":content
        })

    newContent = request.POST["newContent"]
    util.save_entry(link,newContent)

    return HttpResponseRedirect(reverse("link",kwargs={"link":link})) 
