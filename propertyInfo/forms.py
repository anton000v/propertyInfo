from django import forms
from .models import NewBuilding, layoutImages, buildingImages
from .widgets import ChoiceDistrictWidget, ChoiceMicroDistrictWidget, Select2Widget
from django.core.exceptions import ValidationError
import propertyInfo.choices as choices


class buildingImagesForm(forms.ModelForm):
    class Meta:
        model = buildingImages
        fields = ('buildingImage',)
        labels = {
            'buildingImage': ('buildingImage',),
        }
        exclude = ()


class NewBuildingForm(forms.ModelForm):
    # name = forms.CharField(max_length=200, verbose_name=u'Название', default=1)
    district = forms.ChoiceField(choices=choices.DISTRICT_CHOICES,
                                 label=u"Район", initial=choices.NOT_COMPLETED,
                                 widget=ChoiceDistrictWidget
                                 )

    micro_district = forms.ChoiceField(choices=choices.FULL_MICRO_DISTRICT_CHOICES,
                                       label=u"Микрорайон", initial=choices.MICRO_DISTRICT_DOES_NOT_EXIST,
                                       widget=ChoiceMicroDistrictWidget
                                       )
    # def save(self):

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

    def clean_slug(self):
        new_slug = self.cleaned_data['slug'].lower()

        if new_slug == 'new':
            raise ValidationError('Slug не может быть "new"')
        return new_slug

