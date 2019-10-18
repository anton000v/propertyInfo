# from dal import autocomplete

from django import forms

from .models import NewBuilding, layoutImages, buildingImages

from .widgets import ChoiceDistrictWidget, ChoiceMicroDistrictWidget, Select2Widget

import propertyInfo.choices as choices

# class PersonForm(forms.ModelForm):
#     birth_country = forms.ModelChoiceField(
#         queryset=Country.objects.all(),
#         widget=autocomplete.ModelSelect2(url='country-autocomplete')
#     )
#
#     class Meta:
#         model = Person
#         fields = ('__all__')


# ChildItemInlineFormset = inlineformset_factory(NewBuilding, buildingImages, fields=('buildingImage',), extra=0)


class buildingImagesForm(forms.ModelForm):
    class Meta:
        model = buildingImages
        fields = ('buildingImage',)
        labels = {
            'buildingImage': ('buildingImage',),
        }
        exclude = ()


# from djangoformsetjs.utils import formset_media_js
#
# def get_choice_list():
#     # all cites to used as chice list
#     return ['Pune', 'Patna', 'Mumbai', 'Delhi']

class NewBuildingForm(forms.ModelForm):


    # ----------------microdistricts of 'SEVARNAYA SALTOVKA'
    SS1 = 'ss1'
    SS2 = 'ss2'
    SS3 = 'ss3'
    SS4 = 'ss4'
    SS5 = 'ss5'
    # ----------------microdistricts of 'SALTOVKA'
    m601 = '601'
    m602 = '602'
    m603 = '603'
    m604 = '604'
    m605 = '605'
    m606 = '606'
    m606A = '606a'
    m607 = '607'
    m608 = '608'
    m615 = '608'
    m616 = '608'
    m624 = '608'
    m625 = '608'
    m626 = '608'
    m656 = '608'
    m520 = '608'
    m522 = '608'
    m524 = '608'
    m531 = '608'
    m533 = '608'
    m535 = '608'
    HLEBZAVOD_8 = 'hl8'

    MYCRO_DISTRICT_CHOICES = [
        (choices.NOT_COMPLETED, choices.DEFAULT),
        ('Салтовка', (
            (m601, '601'),
            (m602, '602'),
            (m603, '603'),
            (m604, '604'),
            (m605, '605'),
            (m606, '606'),
            (m606A, '606-A'),
            (m607, '607'),
            (m608, '608'),
            (m615, '615'),
            (m616, '616'),
            (m624, '624'),
            (m625, '625'),
            (m626, '626'),
            (m656, '656'),
            (m520, '520'),
            (m522, '522'),
            (m524, '524'),
            (m531, '531'),
            (m533, '533'),
            (m535, '535'),
            (HLEBZAVOD_8, '8 Хлебзавод'),
        )
         ),
        ('Северная Салтовка', (
            (SS1, 'Северная Салтовка - 1'),
            (SS2, 'Северная Салтовка - 2'),
            (SS3, 'Северная Салтовка - 3'),
            (SS4, 'Северная Салтовка - 4'),
            (SS5, 'Северная Салтовка - 5'),
        )
         ),
    ]

    district = forms.ChoiceField(choices=choices.DISTRICT_CHOICES,
                                 label=u"Район", initial=choices.NOT_COMPLETED,
                                 widget=ChoiceDistrictWidget
                                 )

    micro_district = forms.ChoiceField(choices=MYCRO_DISTRICT_CHOICES,
                                       label=u"Микрорайон", initial=choices.NOT_COMPLETED,
                                       widget=ChoiceMicroDistrictWidget
                                       )

    class Meta:
        model = NewBuilding

        # Возможно, филдсет не нужен
        fieldsets = (
            (None, {
                'fields': (
                    # 'country',
                    'city',
                    'name',
                    'address',
                    'administrativeDistrict',
                    'district',
                    'micro_district',
                    'location',
                    'developer',
                    'theClass',
                    'numberOfStoreys',
                    'numberOfBuildings',
                    'numberOfSectionsOrEntrances',
                    'constructionTechnology',
                    'wallsType',
                    'warming',
                    'roomHeight',
                    'numberOfApartmentsInTheHouse',
                )
            }),
            ('Типы квартир', {
                'classes': ('grp-open',),
                'fields': (
                    ('numberOfOneRoom', 'squareOfOneRoom'),
                    ('numberOfTwoRoom', 'squareOfTwoRoom'),
                    ('numberOfThreeRoom', 'squareOfThreeRoom'),
                    ('numberOfFourRoom', 'squareOfFourRoom'),),
            }),
            (' ', {
                'fields': (
                    'numberOfApartmensPerFloor',
                    'commercialPremises',

                ),
            }),
            ('Коммуникации', {
                'fields': (
                    'heating',
                    'gasification',),
            }),
            (' ', {
                'fields': (
                    'elevator',
                    'parking',
                    'numberOfParkingSpaces',
                    'price',
                    'completionDate',
                    'description'),
            }),
        )

        exclude = ()
