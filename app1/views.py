from django.shortcuts import render,redirect
from app1.models import MovieWorldModel
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from app1.forms import MovieForm

# Create your views here.
# def home(request):
#         m=MovieWorldModel.objects.all()
#         return render(request,'home.html',context={"movie":m})

class HomeView(ListView):

    model =MovieWorldModel

    context_object_name="movie"

    template_name='home.html'


    def get_queryset(self):
        queryset=super().get_queryset().filter(title__startswith="m")
        return queryset
    # def get_context_data(self,objecct_list=None,**kwargs):   # to display or to to add additional data  -1method
    #     context=super().get_context_data()
    #     context["name"]="arun"
    #     context['age']=24
    #     return context

    #or second method
    # extra_context=
    


# def add(request):
#     if(request.method=="POST"):
#         t=request.POST['t'] 
#         d=request.POST['d']
#         l=request.POST['l']
#         y=request.POST['y']
#         i=request.FILES['i']

#         m=MovieWorldModel.objects.create(title=t,description=d,language=l,year=y,image=i)
#         m.save()
#         return redirect('home')

#  by using biult in metho
# from app1.forms import MovieForm
# def add(request):
#     if(request.method=="POST"):
#         form=MovieForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect("app1:home")



#     form=MovieForm()   #creating object of the model
#     context={'form':form}
#     return render(request,'add.htmml',context)

#     return  render(request,'add.html')


from django.urls import reverse_lazy

class AddMovie(CreateView):

    model=MovieWorldModel

    form_class=MovieForm

    template_name="add1.html"

    success_url=reverse_lazy('home')  # to redirect to home.html page






# def details(request,p):

#     m=MovieWorldModel.objects.get(id=p)
#     context={"movie":m}

#     return render(request,'details.html',context)

class details(DetailView):
    model=MovieWorldModel

    context_object_name="movie"

    template_name='details.html'

# def delete(request,p):
#     k=MovieWorldModel.objects.get(id=p)
#     k.delete()
#     return redirect('home')

# def edit(request,p):
#     m=MovieWorldModel.objects.get(id=p)
#     if(request.method=="POST"):
#         m.title=request.POST['t'] 
#         m.description=request.POST['d']
#         m.language=request.POST['l']
#         m.year=request.POST['y']
      

#         if (request.FILES.get('i')==None):
#             m.save()
#         else:
#             m.image=request.FILES.get('i')

#         m.save()
#         # return redirect('home')
#         return redirect('details',p)
#     context={'movie':m}
#     return render(request,'edit.html',context)

# update=edit

class Update(UpdateView):

    model=MovieWorldModel
    form_class=MovieForm

    template_name='edit1.html'
    success_url=reverse_lazy('home')


    
class delete(DeleteView):

    template_name='delete1.html'
    model=MovieWorldModel
    success_url=reverse_lazy('home')