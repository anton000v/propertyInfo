from django.contrib import admin
from django.contrib.auth.models import Group
from .models import *

admin.site.site_header = 'My site'
admin.site.unregister(Group)


class newBuildingsTabularInLine(admin.TabularInline):
    model = buildingImages
    extra = 1


class newLayoutsTabularInLine(admin.TabularInline):
    class Meta:
        verbose_name = 'Планировки'
        verbose_name_plural = 'Items i18n'

    model = layoutImages
    extra = 1


class NewBuildingModelAdmin(admin.ModelAdmin):
    class Meta:
        model = NewBuilding
       # js = ('admin/test.js',)


    list_display = ('name', 'address', 'district', 'developer',)
    fieldsets = (
        (None, {
            'fields': (

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
    inlines = [newBuildingsTabularInLine, newLayoutsTabularInLine, ]


admin.site.register(NewBuilding, NewBuildingModelAdmin)






