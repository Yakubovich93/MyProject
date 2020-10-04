from django.shortcuts import render, get_object_or_404
from django.core.mail import send_mail

from . import models
from . import forms
# Create your views here.

BODY_TEMPLATE = (
                "{title} at {uri} was recommended to you by {name}.\n\n"
                    "Comment: {comment}"
            )

def all_materials(request):
    materials_list = models.Material.objects.all()
    return render(request,
                  'materials/all_materials.html',
                  {'materials': materials_list})

def material_details(request, year, month, day, slug):
    material = get_object_or_404(models.Material,
                                 slug=slug,
                                 publish__year=year,
                                 publish__month=month,
                                 publish__day=day)
    return render(request,
                  'materials/detail.html',
                  {'material':material})

def share_material(request, material_id):
    material = get_object_or_404(models.Material,
                                 id=material_id)

    sent = False

    if request.method == 'POST':
        form = forms.EmailMaterialForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            material_uri = request.build_absolute_uri(
                material.get_absolute_url()
            )

            body = BODY_TEMPLATE.format(
                                        title=material.title,
                                        uri=material_uri,
                                        name=cd['name'],
                                        comment=cd['comment']
            )
            subject = "{name} ({email}) recommends you {title}".format(
                name=cd['name'],
                email=cd['my_email'],
                title=material.title,

            )
            send_mail(subject, body, 'admin@mysite.com', [cd['to_email'], ])
            sent = True
    else:
        form = forms.EmailMaterialForm()
    return render(request,
                  'materials/share.html',
                  {'material':material,
                   'form':form,
                   'sent': sent})

