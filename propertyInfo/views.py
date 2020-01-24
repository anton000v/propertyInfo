from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect, render_to_response
from .models import *
from .forms import NewBuildingForm, buildingImagesForm
from propertyInfo.models import NewBuilding, buildingImages, layoutImages
from django.forms import inlineformset_factory, modelformset_factory
from django.core.paginator import Paginator

from django.views import View


def main_screen(request):
    buildings = NewBuilding.objects.all()
    name_contains_query = request.GET.get('name_contains')
    address_contains_query = request.GET.get('address_contains')
    district_contains_query = request.GET.get('district_contains-select')
    developer_contains_query = request.GET.get('developer_contains-select')

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
        # 'user':
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


class PropertyDetail(View):
    def get(self, request, slug):
        building = get_object_or_404(NewBuilding, slug__iexact=slug)
        return render(request, 'propertyInfo/property_detail.html', {'building': building})


# def property_detail(request, slug):
#     building = get_object_or_404(NewBuilding, slug__iexact=slug)
#     return render(request, 'propertyInfo/property_detail.html', {'building': building})

class PropertyCreate(View):
    building_image_formset = modelformset_factory(buildingImages, fields=('buildingImage',), extra=1)
    layout_image_formset = modelformset_factory(layoutImages, fields=('layoutImage',), extra=1)
    way_from_metro_formset = inlineformset_factory(NewBuilding, wayFromMetro,
                                                   fields=('metroChoices', 'time', 'typeOfMovement', 'numberOfMeters',),
                                                   extra=3
                                                   )

    def get(self, request):
        way_formset = self.way_from_metro_formset(queryset=wayFromMetro.objects.none(), prefix='wayFromMetro')
        layout_formset = self.layout_image_formset(queryset=layoutImages.objects.none(), prefix='layoutImage')
        formset = self.building_image_formset(queryset=buildingImages.objects.none(), prefix='buildingImage')
        form = NewBuildingForm()
        context = {
            'form': form,
            'formset': formset,
            'layoutFormset': layout_formset,
            'wayFormset': way_formset,
            'saltovka_dbvalue': choices.SALTOVKA,
            'severnaya_saltovka_dbvalue': choices.SEVERNAYA_SALTOVKA,
            'micro_district_does_not_exist_choice': choices.MICRO_DISTRICT_DOES_NOT_EXIST_CHOICE,
            'micro_district_default_choice': choices.MICRO_DISTRICT_DEFAULT_CHOICE,
            'micro_district_saltovka_choices': choices.MICRO_DISTRICT_SALTOVKA_CHOICES,
            'micro_district_severnaya_saltovka_choices': choices.MICRO_DISTRICT_SEVERNAYA_SALTOVKA_CHOICES,

        }

        return render(request, 'propertyInfo/property_new.html', context)

    def post(self, request):
        form = NewBuildingForm(request.POST or None)
        formset = self.building_image_formset(request.POST or None, request.FILES or None, prefix='buildingImage')
        layout_formset = self.layout_image_formset(request.POST or None, request.FILES or None, prefix='layoutImage')
        way_formset = self.way_from_metro_formset(request.POST or None, prefix='wayFromMetro')

        # form_name = request.POST.get('name')
        # form_developer = request.POST.get('developer')
        # form_address = request.POST.get('address')
        # form.initial['slug'] = generate_slug(name=form_name, developer=form_developer, address=form_address)
        # print(form_name, form_developer, form_address)
        # print(form.slug)
        if form.is_valid() and formset.is_valid() and layout_formset.is_valid() and way_formset.is_valid():
            property_post = form.save()
            property_post.save()

            for f in way_formset:
                try:

                    cur_way = wayFromMetro(building=property_post,
                                           metroChoices=f.cleaned_data['metroChoices'],
                                           time=f.cleaned_data['time'],
                                           typeOfMovement=f.cleaned_data['typeOfMovement'],
                                           numberOfMeters=f.cleaned_data['numberOfMeters']
                                           )

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

            for f in layout_formset:
                try:
                    layout_photo = layoutImages(building=property_post, layoutImage=f.cleaned_data['layoutImage'])
                    layout_photo.save()

                except Exception as e:
                    break

            return redirect('property_detail', slug=property_post.slug)
        else:
            context = {
                'form': form,
                'formset': formset,
                'layoutFormset': layout_formset,
                'wayFormset': way_formset,
                'saltovka_dbvalue': choices.SALTOVKA,
                'severnaya_saltovka_dbvalue': choices.SEVERNAYA_SALTOVKA,
                'micro_district_does_not_exist_choice': choices.MICRO_DISTRICT_DOES_NOT_EXIST_CHOICE,
                'micro_district_default_choice': choices.MICRO_DISTRICT_DEFAULT_CHOICE,
                'micro_district_saltovka_choices': choices.MICRO_DISTRICT_SALTOVKA_CHOICES,
                'micro_district_severnaya_saltovka_choices': choices.MICRO_DISTRICT_SEVERNAYA_SALTOVKA_CHOICES,

            }

            return render(request, 'propertyInfo/property_new.html', context)


# def property_new(request):
#     buildingImageFormset = modelformset_factory(buildingImages, fields=('buildingImage',), extra=1)
#     layoutImageFormset = modelformset_factory(layoutImages, fields=('layoutImage',), extra=1)
#     wayFromMetroFormset = inlineformset_factory(NewBuilding, wayFromMetro,
#                                                 fields=('metroChoices', 'time', 'typeOfMovement', 'numberOfMeters',),
#                                                 extra=3
#                                                 )
#     if request.method == "POST":
#         form = NewBuildingForm(request.POST)
#         formset = buildingImageFormset(request.POST or None, request.FILES or None, prefix='buildingImage')
#         layoutFormset = layoutImageFormset(request.POST or None, request.FILES or None, prefix='layoutImage')
#         wayFormset = wayFromMetroFormset(request.POST or None, prefix='wayFromMetro')
#         if form.is_valid() and formset.is_valid() and layoutFormset.is_valid() and wayFormset.is_valid():
#             property_post = form.save()
#             property_post.save()
#             # wayFormset.save()
#
#             for f in wayFormset:
#                 try:
#
#                     cur_way = wayFromMetro(building=property_post,
#                                            metroChoices=f.cleaned_data['metroChoices'],
#                                            time=f.cleaned_data['time'],
#                                            typeOfMovement=f.cleaned_data['typeOfMovement'],
#                                            numberOfMeters=f.cleaned_data['numberOfMeters']
#                                            )
#                     # print('BEGIN=> ', f.cleaned_data['metroChoices'], ' <=/END')
#                     cur_way.save()
#
#                 except Exception as e:
#                     break
#
#             for f in formset:
#                 try:
#                     # print(' MY: ', f)
#                     photo = buildingImages(building=property_post, buildingImage=f.cleaned_data['buildingImage'])
#                     photo.save()
#
#                 except Exception as e:
#                     break
#
#             for f in layoutFormset:
#                 try:
#                     layout_photo = layoutImages(building=property_post, layoutImage=f.cleaned_data['layoutImage'])
#                     layout_photo.save()
#
#                 except Exception as e:
#                     break
#
#             return redirect('property_detail', pk=property_post.pk)
#     else:
#         wayFormset = wayFromMetroFormset(queryset=wayFromMetro.objects.none(), prefix='wayFromMetro')
#         layoutFormset = layoutImageFormset(queryset=layoutImages.objects.none(), prefix='layoutImage')
#         formset = buildingImageFormset(queryset=buildingImages.objects.none(), prefix='buildingImage')
#         form = NewBuildingForm()
#
#     context = {
#         'form': form,
#         'formset': formset,
#         'layoutFormset': layoutFormset,
#         'wayFormset': wayFormset,
#     }
#
#     return render(request, 'propertyInfo/property_new.html', context)

class PropertyEdit(View):
    building_image_inlineformset = inlineformset_factory(NewBuilding, buildingImages, fields=('buildingImage',),
                                                         extra=1,
                                                         can_delete=True)
    layout_image_inlineformset = inlineformset_factory(NewBuilding, layoutImages, fields=('layoutImage',), extra=1,
                                                       can_delete=True)
    way_from_metro_inlineformset = inlineformset_factory(NewBuilding, wayFromMetro,
                                                         fields=(
                                                             'metroChoices', 'time', 'typeOfMovement',
                                                             'numberOfMeters',),
                                                         extra=1, can_delete=True)

    def get(self, request, slug):
        property = get_object_or_404(NewBuilding, slug__iexact=slug)

        form = NewBuildingForm(instance=property)
        formset = self.building_image_inlineformset(instance=property, prefix='buildingImage')
        layout_formset = self.layout_image_inlineformset(instance=property, prefix='layoutImage')
        way_formset = self.way_from_metro_inlineformset(instance=property, prefix='wayFromMetro')

        context = {
            'form': form,
            'formset': formset,
            # 'lastElementOfFormset': formset.forms[-1],
            'layoutFormset': layout_formset,
            'wayFormset': way_formset,
            'saltovka_dbvalue': choices.SALTOVKA,
            'severnaya_saltovka_dbvalue': choices.SEVERNAYA_SALTOVKA,
            'micro_district_does_not_exist_choice': choices.MICRO_DISTRICT_DOES_NOT_EXIST_CHOICE,
            'micro_district_default_choice': choices.MICRO_DISTRICT_DEFAULT_CHOICE,
            'micro_district_saltovka_choices': choices.MICRO_DISTRICT_SALTOVKA_CHOICES,
            'micro_district_severnaya_saltovka_choices': choices.MICRO_DISTRICT_SEVERNAYA_SALTOVKA_CHOICES,
        }

        return render(request, 'propertyInfo/property_edit.html', context)

    def post(self, request, slug):
        property = get_object_or_404(NewBuilding, slug__iexact=slug)

        form = NewBuildingForm(request.POST, instance=property)

        formset = self.building_image_inlineformset(request.POST or None, request.FILES or None, prefix='buildingImage',
                                                    instance=property)
        layout_formset = self.layout_image_inlineformset(request.POST or None, request.FILES or None,
                                                         prefix='layoutImage',
                                                         instance=property)
        way_formset = self.way_from_metro_inlineformset(request.POST or None, prefix='wayFromMetro', instance=property)
        # print(' MY: < ', formset.deleted_forms, ' >')

        if form.is_valid() and formset.is_valid() and layout_formset.is_valid() and way_formset.is_valid():
            property = form.save()
            property.save()

            for f in way_formset.extra_forms:
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
            way_formset.save()
            for f in formset.extra_forms:
                # print('MY: ', f, ' -> ', list(queryset))
                try:
                    photo = buildingImages(building=property, buildingImage=f.cleaned_data['buildingImage'])
                    # cur_photo = photo.save()

                except Exception as e:
                    break
            formset.save()

            for f in layout_formset.extra_forms:
                # print('MY: ', f, ' -> ', list(queryset))
                try:
                    photo = layoutImages(building=property, layoutImage=f.cleaned_data['layoutImage'])
                    # cur_photo = photo.save()
                    # photo.save()

                except Exception as e:
                    break
            layout_formset.save()
            return redirect('property_detail', slug=property.slug)
        context = {
            'form': form,
            'formset': formset,
            # 'lastElementOfFormset': formset.forms[-1],
            'layoutFormset': layout_formset,
            'wayFormset': way_formset,
            'saltovka_dbvalue': choices.SALTOVKA,
            'severnaya_saltovka_dbvalue': choices.SEVERNAYA_SALTOVKA,
            'micro_district_does_not_exist_choice': choices.MICRO_DISTRICT_DOES_NOT_EXIST_CHOICE,
            'micro_district_default_choice': choices.MICRO_DISTRICT_DEFAULT_CHOICE,
            'micro_district_saltovka_choices': choices.MICRO_DISTRICT_SALTOVKA_CHOICES,
            'micro_district_severnaya_saltovka_choices': choices.MICRO_DISTRICT_SEVERNAYA_SALTOVKA_CHOICES,
        }
        return render(request, 'propertyInfo/property_edit.html', context)

# def property_edit(request, slug):
#     property = get_object_or_404(NewBuilding, slug__iexact=slug)
#     BuildingImageInlineFormSet = inlineformset_factory(NewBuilding, buildingImages, fields=('buildingImage',), extra=1,
#                                                        can_delete=True)
#     LayoutImageInlineFormSet = inlineformset_factory(NewBuilding, layoutImages, fields=('layoutImage',), extra=1,
#                                                      can_delete=True)
#     wayFromMetroFormset = inlineformset_factory(NewBuilding, wayFromMetro,
#                                                 fields=('metroChoices', 'time', 'typeOfMovement', 'numberOfMeters',),
#                                                 extra=1, can_delete=True)
#
#     # queryset = buildingImages.objects.filter(building=pk)
#
#     # empty = BuildingImageInlineFormSet.empty_form
#     # # empty is a form instance, so you can do whatever you want to it
#     # my_empty_form_init(empty_form)
#     # BuildingImageInlineFormSet.empty_form = empty_form
#     # BuildingImageInlineFormSet.empty_form = empty_form
#
#     if request.method == "POST":
#         form = NewBuildingForm(request.POST, instance=property)
#
#         formset = BuildingImageInlineFormSet(request.POST or None, request.FILES or None, prefix='buildingImage',
#                                              instance=property)
#         layoutFormset = LayoutImageInlineFormSet(request.POST or None, request.FILES or None, prefix='layoutImage',
#                                                  instance=property)
#         wayFormset = wayFromMetroFormset(request.POST or None, prefix='wayFromMetro', instance=property)
#         # print(' MY: < ', formset.deleted_forms, ' >')
#
#         if form.is_valid() and formset.is_valid() and layoutFormset.is_valid() and wayFormset.is_valid():
#             property = form.save()
#             property.save()
#
#             for f in wayFormset.extra_forms:
#                 try:
#
#                     cur_way = wayFromMetro(building=property,
#                                            metroChoices=f.cleaned_data['metroChoices'],
#                                            time=f.cleaned_data['time'],
#                                            typeOfMovement=f.cleaned_data['typeOfMovement'],
#                                            numberOfMeters=f.cleaned_data['numberOfMeters']
#                                            )
#                     # print('BEGIN=> ', f.cleaned_data['metroChoices'], ' <=/END')
#                     # cur_way.save()
#
#                 except Exception as e:
#                     break
#             wayFormset.save()
#             for f in formset.extra_forms:
#                 # print('MY: ', f, ' -> ', list(queryset))
#                 try:
#                     photo = buildingImages(building=property, buildingImage=f.cleaned_data['buildingImage'])
#                     # cur_photo = photo.save()
#
#                 except Exception as e:
#                     break
#             formset.save()
#
#             for f in layoutFormset.extra_forms:
#                 # print('MY: ', f, ' -> ', list(queryset))
#                 try:
#                     photo = layoutImages(building=property, layoutImage=f.cleaned_data['layoutImage'])
#                     # cur_photo = photo.save()
#                     # photo.save()
#
#                 except Exception as e:
#                     break
#             layoutFormset.save()
#             return redirect('property_detail', slug=property.slug)
#
#     else:
#         form = NewBuildingForm(instance=property)
#         formset = BuildingImageInlineFormSet(instance=property, prefix='buildingImage')
#         layoutFormset = LayoutImageInlineFormSet(instance=property, prefix='layoutImage')
#         wayFormset = wayFromMetroFormset(instance=property, prefix='wayFromMetro')
#     context = {
#         'form': form,
#         'formset': formset,
#         # 'lastElementOfFormset': formset.forms[-1],
#         'layoutFormset': layoutFormset,
#         'wayFormset': wayFormset,
#     }
#
#     return render(request, 'propertyInfo/property_edit.html', context)

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
