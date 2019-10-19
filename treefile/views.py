from django.shortcuts import render
from .models import gallery, category, doctor, service, blog, testimonial


def index(req):
    cat = category.objects.all()
    gettestimonial = testimonial.objects.all()
    alldocotor = doctor.objects.all()
    context = {
        'category' : cat,
        'gettestimonial': gettestimonial,
        'alldocotor': alldocotor
    }
    return render(req, 'index.html', context)

def about(req):
    cat = category.objects.all()
    alldocotor = doctor.objects.all()
    context = {
        'category' : cat,
        'alldocotor' : alldocotor
    }
    return render(req, 'about.html', context)

def team(req):
    cat = category.objects.all()
    alldocotor = doctor.objects.all()
    context = {
        'category' : cat,
        'alldocotor' : alldocotor
    }
    return render(req, 'team.html', context)

def galleryPage(req):
    cat = category.objects.all()
    img = gallery.objects.all()
    context = {
        'category' : cat,
        'image' : img
    }
    return render(req, 'gallery.html', context)

def blogi(req):
    cat = category.objects.all()
    blogData = blog.objects.all()
    context = {
        'category' : cat,
        'blogData': blogData
    }
    return render(req, 'blog.html', context)

def contact(req):
    cat = category.objects.all()
    context = {
        'category' : cat
    }
    return render(req, 'contact.html', context)

def teamDetail(req, id, name):
    cat = category.objects.all()
    if req.method == 'GET':
        doci = doctor.objects.get(pk=id)
        otherdoci = doctor.objects.exclude(id__exact=id)
        context = {
            'category' : cat,
            'doci' : doci,
            'otherdoci' : otherdoci,
        }
        return render(req, 'teamDetail.html', context)
    else:
        return redirect('/')

def servicedetail(req, id, name):
    cat = category.objects.all()
    if req.method == 'GET':
        catdata = category.objects.get(pk=id)
        otherservice = service.objects.filter(cat=id)
        context = {
            'category' : cat,
            'catdata' : catdata,
            'otherservice': otherservice
        }
        return render(req, 'serviceDetail.html', context)
    else:
        return redirect('/')

def blogdetail(req, id, name):
    cat = category.objects.all()
    if req.method == 'GET':
        blogdet = blog.objects.get(pk=id)
        otherpost = blog.objects.exclude(id__exact=id)
        context = {
            'category' : cat,
            'blogdetail' : blogdet,
            'otherpost': otherpost
        }
        return render(req, 'blogDetail.html', context)
    else:
        return redirect('/')
