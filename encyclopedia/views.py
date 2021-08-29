from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
import random
import markdown2

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def entry(request,entry):
    if util.get_entry(entry):
        content = markdown2.markdown(util.get_entry(entry))
    else:
        content="No entries found"

    return render(request,"encyclopedia/entry.html",{
        "entry":entry , "content":content
    })

def edit(request,entry):
    if (request.POST):
        #newentry = request.POST["heading"]
        newcontent = request.POST["data"]
        util.save_entry(entry,newcontent)
        #return HttpResponseRedirect(reverse("index"))
        return HttpResponseRedirect(reverse("entry",kwargs={"entry":entry}))
    else:
        return render(request,"encyclopedia/edit.html",{
            "entry":entry,"content":util.get_entry(entry)
        })   

def search(request):
    
    query = request.POST["q"]
    
    entries = util.list_entries()
    if(query.lower() in (entry.lower() for entry in entries)):
        return HttpResponseRedirect(reverse("entry", kwargs={"entry":query}))

    else:
        li =[]
        status=0
        #if(query.lower() in (entry.lower() for entry in entries)):    
        for entry in entries:
            if query.lower() in entry.lower():
                li.append(entry)
                status=1
        
        return render(request,"encyclopedia/search.html",{
                "entries":li , "status": status
            })
        
    
     

def create(request):
    if(request.POST):
        title = request.POST["heading"]
        content = request.POST["data"]
        util.save_entry(title,content)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request,"encyclopedia/create.html")

def randompage(request):
    entries = util.list_entries()
    entry=random.choice(entries)
    
    content = markdown2.markdown(util.get_entry(entry))
    
    return HttpResponseRedirect(reverse("entry",kwargs={"entry":entry}))
    #return render(request,"encyclopedia/randompage.html",{
    #    "entry":entry, "content":content })
def deleteentry(request,entry):
    util.delete_entry(entry)
    return HttpResponseRedirect(reverse("index"))
    