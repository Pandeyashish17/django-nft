from django.shortcuts import redirect, render
from .models import NFTname
from .forms import NFtnameForm
# Create your views here.
names=['ashish','bishal','abhay']



def home(request):
    nfts = NFTname.objects.all()
    context={ "nfts":nfts }

    return render(request, 'index.html',context)




def addNFT(request):
    form=NFtnameForm()
    if request.method == "POST":
        form=NFtnameForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    context={"form":form}
    return render(request,'addNFT.html',context)


def delete(request,pk):
    nft=NFTname.objects.get(id=pk)
    if request.method == "POST":
        nft.delete()
        return redirect("home")
    context={ "nft":nft }

    return render(request, 'delete.html',context)




def update(request,pk):
    nft=NFTname.objects.get(id=pk)
    form=NFtnameForm(instance=nft)
  
    if request.method == "POST":
        form=NFtnameForm(request.POST,instance=nft)
        if form.is_valid():
            form.save()
            return redirect("home")
    context={"form":form}
    return render(request,'addNFT.html',context)
