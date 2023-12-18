from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse, HttpResponse
from django.views.decorators.http import require_POST
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .forms import ImageCreateForm
from .models import Image

# Create your views here.


@login_required
def image_create(request):
    if request.method == 'POST':
        # form is sent
        form = ImageCreateForm(data=request.POST)

        if form.is_valid():
            # form data is valid
            cd = form.cleaned_data
            new_image = form.save(commit=False)
            # assign current user to the item
            new_image.user = request.user
            new_image.save()
            messages.success(
                request=request, message='Image added successfully')

            # redirect to new created item detail view
            return redirect(new_image.get_absolute_url())

    else:
        # build form with data provided by the bookmarklet via GET
        form = ImageCreateForm(data=request.GET)

    return render(request=request, template_name='images/image/create.html', context={'section': 'images', 'form': form})


def image_detail(request, id, slug):
    image = get_object_or_404(Image, id=id, slug=slug)

    return render(request=request, template_name='images/image/detail.html', context={'section': 'images', 'image': image})


@login_required
@require_POST
def image_like(request):
    image_id = request.POST.get('id')
    action = request.POST.get('action')

    if image_id and action:
        try:
            image = Image.objects.get(id=image_id)

            if action == 'like':
                image.users_like.add(request.user)
            else:
                image.users_like.remove(request.user)

            return JsonResponse({'status': 'ok'})
        except Image.DoesNotExist:
            pass

    return JsonResponse({'status': 'error'})


@login_required
def image_list(request):
    images = Image.objects.all()
    paginator = Paginator(object_list=images, per_page=8)
    page = request.GET.get('page')
    images_only = request.GET.get('images_only')

    try:
        images = paginator.page(number=page)

    except PageNotAnInteger:
        # if page is not an integer deliver the first page
        images = paginator.page(number=1)

    except EmptyPage:
        if images_only:
            return HttpResponse(content='')

        images = paginator.page(number=paginator.num_pages)

    if images_only:
        return render(request=request, template_name='images/image/list_images.html', context={'section': 'images', 'images': images})

    return render(request=request, template_name='images/image/list.html', context={'section': 'images', 'images': images})
