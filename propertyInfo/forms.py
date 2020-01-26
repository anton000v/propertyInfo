from django import forms
from .models import NewBuilding, layoutImages, buildingImages
from .models import generate_slug
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

    slug = forms.SlugField(widget=forms.TextInput(attrs={'readonly': True}), required=False)

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

        form_name = self.cleaned_data['name']
        form_developer = self.cleaned_data['developer']
        form_address = self.cleaned_data['address']
        old_slug = self.cleaned_data['slug']
        # current_id = NewBuilding.objects.get(slug=old_slug).id
        new_slug = generate_slug(name=form_name, developer=form_developer, address=form_address)
        # print(current_id, ' - ', old_slug, ' - ', new_slug)
        if new_slug != old_slug:
            if new_slug == 'new':
                raise ValidationError('Slug не может быть "new".')
            if new_slug == '':
                raise ValidationError('Slug не может быть пустым.')
            if NewBuilding.objects.filter(slug=new_slug).exists():
                raise ValidationError("Slug '{0}', который вы хотите создать, уже существует".format(new_slug))
            # self.fields['slug'].widget.attrs['readonly'] = True
            return new_slug
        else:
            # self.fields['slug'].widget.attrs['readonly'] = True
            return old_slug
    # def clean_title(self, title):
    #     from django.utils.text import slugify
    #     from django.core.exceptions import ValidationError
    #
    #     slug = slugify(title)
    #
    #     if NewBuilding.objects.filter(slug=slug).exists():
    #         self. = 'aaa'
    #         raise ValidationError('A question with this title already exists.')
    #
    #     return title
