from django.shortcuts import render , redirect
from . models import Movie_info
from . forms import MovieForm,CensorForm

# Create your views here.

def create(request):
    if request.method == "POST":
        # title = request.POST.get("title")
        # year = request.POST.get("year")
        # summary = request.POST.get("summary")

        # Movie_Data = Movie_info(title=title,year=year,summary=summary)
        # Movie_Data.save()
        form = MovieForm(request.POST, request.FILES)
        censor_form = CensorForm(request.POST)
        if form.is_valid and censor_form.is_valid():
            # form.save()
            # censor_form.save()

            censor = censor_form.save()
            movie = form.save(commit=False)
            movie.censor_details = censor
            movie.save()

            return redirect("/")
    form = MovieForm()
    censor_form = CensorForm()
    
    return render(request, 'create.html', {"form":form, "censor_form":censor_form})

def list(req):
    data = Movie_info.objects.all()
    return render(req , "list.html",{"data":data})

def edit(req,pk):
    movi = Movie_info.objects.get(id=pk)

    if req.method == "POST":
        form = MovieForm(req.POST , req.FILES , instance=movi)
        censor_form = CensorForm(req.POST , instance=movi.censor_details)
        if form.is_valid():
            # form.save()
            # censor_form.save()
            # return redirect("/")
            censorInfo = censor_form.save()
            movie = form.save(commit=False)
            movie.censor_details = censorInfo
            print(movie)
            movie.save()

            return redirect("/")

    form = MovieForm(instance=movi)
    censor_form = CensorForm(instance=movi.censor_details)

    return render(req, 'create.html', {"form":form, "censor_form":censor_form})


def delete(req,pk):
    movi = Movie_info.objects.get(id=pk)
    movi.delete()

    data = Movie_info.objects.all()

    return render(req , "list.html",{"data":data})
