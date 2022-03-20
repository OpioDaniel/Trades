from django.shortcuts import render
from .models import Apes, SlidingImages, SlidingTitle, Trial


def index(request):
    apes_ = Apes.objects.all()
    print(apes_)
    sliding_images_ = SlidingImages.objects.all()
    sliding_title_ = SlidingTitle.objects.all()
    return render(request, 'apewives/index.html', {'apes': apes_, 'sliding_images': sliding_images_,
                                                   'sliding_title': sliding_title_})


def trial(request):
    obj_ = Trial.objects.all()
    return render(request, 'apewives/trial.html', {'obj_': obj_})