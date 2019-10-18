from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect, render_to_response
from .models import *
# from dal import autocomplete
from .forms import NewBuildingForm, buildingImagesForm
from propertyInfo.models import NewBuilding, buildingImages, layoutImages
from django.forms import inlineformset_factory, modelformset_factory
from django.core.paginator import Paginator

from django.views import View
from django.http import HttpResponse
from django.db.models.functions import Lower
from django.http import JsonResponse


# def get_district_choices_list():
#     DISTRICT_CHOICES_AS_LIST = []
#     # for dTitle, dNames in choices.DISTRICT_CHOICES[1:]:
#     # for dName in dNames:
#     #         DISTRICT_CHOICES_AS_LIST.append(dName[1])
#
#     for dTitle, dNames in choices.DISTRICT_CHOICES[1:]:
#         choices_list_titles = []
#         choices_list_titles.append(dTitle)
#         choices_list_names = []
#         for dName in dNames:
#             choices_list_names.append(dName[1])
#         choices_list_titles.append(choices_list_names)
#         DISTRICT_CHOICES_AS_LIST.append(choices_list_titles)
#     # print("ПРОВЕРКА: ", DISTRICT_CHOICES_AS_LIST)
#     return DISTRICT_CHOICES_AS_LIST


# def convert_human_oriented_district_to_dbview(district_name):
#     DISTRICT_CHOICES_AS_DICT = {}
#     for dTitle, dNames in choices.DISTRICT_CHOICES[1:]:
#         for dName in dNames:
#             DISTRICT_CHOICES_AS_DICT[dName[0]] = dName[1]
#     for k, v in DISTRICT_CHOICES_AS_DICT.items():
#         if v == district_name:
#             return k

# def example(request):
#     spravka = 'spravka'
#     some_rude_world = 'САСАТЬ!!!'
#     number_list = [1,2,3,4,5,6]
#     return render(request, 'example/example.html', {'key1': spravka,
#                                                     'key2': some_rude_world,
#                                                     'key3':number_list,
#                                                     }
#                   )


def main_screen(request):
    # example_dict = {'ce': 'Центр', 'nod': 'Новые Дома'}

    buildings = NewBuilding.objects.all()

    name_contains_query = request.GET.get('name_contains')
    address_contains_query = request.GET.get('address_contains')
    district_contains_query = request.GET.get('district_contains-select')
    developer_contains_query = request.GET.get('developer_contains-select')

    # print('PROVERKA: ', district_contains_query)

    if name_contains_query != '' and name_contains_query is not None:
        buildings = buildings.filter(name__icontains=name_contains_query)
    else:
        name_contains_query = ''
    if address_contains_query != '' and address_contains_query is not None:
        buildings &= buildings.filter(address__icontains=address_contains_query)
    else:
        address_contains_query = ''
    if district_contains_query != '' and district_contains_query is not None and district_contains_query != choices.NOT_COMPLETED:
        buildings &= buildings.filter(
            district__icontains=district_contains_query)
    else:
        district_contains_query = ''
    if developer_contains_query != '' and developer_contains_query is not None:
        buildings &= buildings.filter(developer__icontains=developer_contains_query)
    else:
        developer_contains_query = ''

    paginator = Paginator(buildings, 9)

    page_number = request.GET.get('page', 1)

    buildings_page = paginator.get_page(page_number)

    is_paginated = buildings_page.has_other_pages()

    if buildings_page.has_previous():
        previous_page_url = '?page={}'.format(buildings_page.previous_page_number())
    else:
        previous_page_url = ''

    if buildings_page.has_next():
        next_page_url = '?page={}'.format(buildings_page.next_page_number())
    else:
        next_page_url = ''
    context = {
        'buildings_page': buildings_page,
        # 'district_dict' : example_dict
        'districts': choices.DISTRICT_CHOICES,
        # 'default_for_human': choices.DEFAULT,
        # 'not_completed_for_db' :choices.NOT_COMPLETED,
        'name_contains_query': name_contains_query,
        'address_contains_query': address_contains_query,
        'district_contains_query': district_contains_query,
        'developer_contains_query': developer_contains_query,
        'is_paginated': is_paginated,
        'previous_page_url': previous_page_url,
        'next_page_url': next_page_url,
    }
    return render(request, 'propertyInfo/index.html', context)


def property_detail(request, pk):
    building = get_object_or_404(NewBuilding, pk=pk)
    return render(request, 'propertyInfo/property_detail.html', {'building': building})


#
# buildingImagesFormSet = forms.models.inlineformset_factory(NewBuilding, buildingImages,
#                                                     form=buildingImagesForm,fields=['buildingImage',], extra=1)
def property_new(request):
    buildingImageFormset = modelformset_factory(buildingImages, fields=('buildingImage',), extra=1)
    layoutImageFormset = modelformset_factory(layoutImages, fields=('layoutImage',), extra=1)
    wayFromMetroFormset = inlineformset_factory(NewBuilding, wayFromMetro,
                                                fields=('metroChoices', 'time', 'typeOfMovement', 'numberOfMeters',),
                                                extra=3
                                                )
    if request.method == "POST":

        form = NewBuildingForm(request.POST)
        formset = buildingImageFormset(request.POST or None, request.FILES or None, prefix='buildingImage')
        layoutFormset = layoutImageFormset(request.POST or None, request.FILES or None, prefix='layoutImage')
        wayFormset = wayFromMetroFormset(request.POST or None, prefix='wayFromMetro')
        if form.is_valid() and formset.is_valid() and layoutFormset.is_valid() and wayFormset.is_valid():
            property_post = form.save()
            property_post.save()
            # wayFormset.save()

            for f in wayFormset:
                try:

                    cur_way = wayFromMetro(building=property_post,
                                           metroChoices=f.cleaned_data['metroChoices'],
                                           time=f.cleaned_data['time'],
                                           typeOfMovement=f.cleaned_data['typeOfMovement'],
                                           numberOfMeters=f.cleaned_data['numberOfMeters']
                                           )
                    # print('BEGIN=> ', f.cleaned_data['metroChoices'], ' <=/END')
                    cur_way.save()

                except Exception as e:
                    break

            for f in formset:
                try:
                    # print(' MY: ', f)
                    photo = buildingImages(building=property_post, buildingImage=f.cleaned_data['buildingImage'])
                    photo.save()

                except Exception as e:
                    break

            for f in layoutFormset:
                try:
                    layout_photo = layoutImages(building=property_post, layoutImage=f.cleaned_data['layoutImage'])
                    layout_photo.save()

                except Exception as e:
                    break

            return redirect('property_detail', pk=property_post.pk)
    else:
        wayFormset = wayFromMetroFormset(queryset=wayFromMetro.objects.none(), prefix='wayFromMetro')
        layoutFormset = layoutImageFormset(queryset=layoutImages.objects.none(), prefix='layoutImage')
        formset = buildingImageFormset(queryset=buildingImages.objects.none(), prefix='buildingImage')
        form = NewBuildingForm()

    context = {
        'form': form,
        'formset': formset,
        'layoutFormset': layoutFormset,
        'wayFormset': wayFormset,
    }

    return render(request, 'propertyInfo/property_new.html', context)


def property_edit(request, pk):
    property = get_object_or_404(NewBuilding, pk=pk)
    BuildingImageInlineFormSet = inlineformset_factory(NewBuilding, buildingImages, fields=('buildingImage',), extra=1,
                                                       can_delete=True)
    LayoutImageInlineFormSet = inlineformset_factory(NewBuilding, layoutImages, fields=('layoutImage',), extra=1,
                                                     can_delete=True)
    wayFromMetroFormset = inlineformset_factory(NewBuilding, wayFromMetro,
                                                fields=('metroChoices', 'time', 'typeOfMovement', 'numberOfMeters',),
                                                extra=1, can_delete=True)

    queryset = buildingImages.objects.filter(building=pk)

    # empty = BuildingImageInlineFormSet.empty_form
    # # empty is a form instance, so you can do whatever you want to it
    # my_empty_form_init(empty_form)
    # BuildingImageInlineFormSet.empty_form = empty_form
    # BuildingImageInlineFormSet.empty_form = empty_form

    if request.method == "POST":
        form = NewBuildingForm(request.POST, instance=property)

        formset = BuildingImageInlineFormSet(request.POST or None, request.FILES or None, prefix='buildingImage',
                                             instance=property)
        layoutFormset = LayoutImageInlineFormSet(request.POST or None, request.FILES or None, prefix='layoutImage',
                                                 instance=property)
        wayFormset = wayFromMetroFormset(request.POST or None, prefix='wayFromMetro', instance=property)
        # print(' MY: < ', formset.deleted_forms, ' >')

        if form.is_valid() and formset.is_valid() and layoutFormset.is_valid() and wayFormset.is_valid():
            property = form.save()
            property.save()

            for f in wayFormset.extra_forms:
                try:

                    cur_way = wayFromMetro(building=property,
                                           metroChoices=f.cleaned_data['metroChoices'],
                                           time=f.cleaned_data['time'],
                                           typeOfMovement=f.cleaned_data['typeOfMovement'],
                                           numberOfMeters=f.cleaned_data['numberOfMeters']
                                           )
                    # print('BEGIN=> ', f.cleaned_data['metroChoices'], ' <=/END')
                    # cur_way.save()

                except Exception as e:
                    break
            wayFormset.save()
            for f in formset.extra_forms:
                # print('MY: ', f, ' -> ', list(queryset))
                try:
                    photo = buildingImages(building=property, buildingImage=f.cleaned_data['buildingImage'])
                    # cur_photo = photo.save()

                except Exception as e:
                    break
            formset.save()

            for f in layoutFormset.extra_forms:
                # print('MY: ', f, ' -> ', list(queryset))
                try:
                    photo = layoutImages(building=property, layoutImage=f.cleaned_data['layoutImage'])
                    # cur_photo = photo.save()
                    # photo.save()

                except Exception as e:
                    break
            layoutFormset.save()
            return redirect('property_detail', pk=property.pk)

    else:
        form = NewBuildingForm(instance=property)
        formset = BuildingImageInlineFormSet(instance=property, prefix='buildingImage')
        layoutFormset = LayoutImageInlineFormSet(instance=property, prefix='layoutImage')
        wayFormset = wayFromMetroFormset(instance=property, prefix='wayFromMetro')
    context = {
        'form': form,
        'formset': formset,
        # 'lastElementOfFormset': formset.forms[-1],
        'layoutFormset': layoutFormset,
        'wayFormset': wayFormset,
    }

    return render(request, 'propertyInfo/property_edit.html', context)

# -----------Для ajax обновления данных
# def update_content(request):
#     print('AAAAAAAAAAAAAAAAAAAAAAAAAAAAA')
#
#
#     if request.GET:
#
#         buildings = NewBuilding.objects.all()
#         name_contains_query = request.GET.get('name_contains')
#         address_contains_query = request.GET.get('address_contains')
#         district_contains_query = convert_human_oriented_district_to_dbview(request.GET.get('district_contains'))
#         developer_contains_query = request.GET.get('developer_contains')
#
#         if name_contains_query != '' and name_contains_query is not None:
#             buildings = buildings.filter(name__icontains=name_contains_query)
#         # print('Type: ', type(buildings))
#         if address_contains_query != '' and address_contains_query is not None:
#             buildings &= buildings.filter(address__icontains=address_contains_query)
#         if district_contains_query != '' and district_contains_query is not None:
#             buildings &= buildings.filter(district__icontains=district_contains_query)
#         if developer_contains_query != '' and developer_contains_query is not None:
#             buildings &= buildings.filter(developer__icontains=developer_contains_query)
#         context = {
#             'buildings': buildings,
#             # 'district_dict' : example_dict
#             'districts': get_district_choices_list(),
#         }
#
#         print(context)
#         return render_to_response('propertyInfo/cards_container.html ',context)
#
#     else:
#         return HttpResponse('no')
