from django.db import models

from multiselectfield import MultiSelectField
from django.contrib.auth.models import User
from django.shortcuts import reverse
import propertyInfo.choices as choices


class NewBuilding(models.Model):
    class Meta():
        db_table = 'NewBuildings'
        ordering = ['name']

    # --------------------default values:
    NOT_COMPLETED = 'nc'
    DEFAULT = 'Не заполнено'




    name = models.CharField(max_length=200, verbose_name=u'Название', default=1)
    # messageG = forms.CharField(widget=forms.Textarea, label='lolkek')
    address = models.CharField(max_length=200, verbose_name=u"Адрес", default=1)  # адресс
    administrativeDistrict = models.CharField(max_length=2, choices=choices.THE_ADMINISTRATIVE_DISTRICT_CHOICES,
                                              default=NOT_COMPLETED,
                                              verbose_name=u"Административный район")  #
    district = models.CharField(max_length=4, choices=choices.DISTRICT_CHOICES,
                                default=choices.NOT_COMPLETED,
                                verbose_name=u"Район")  # )
    micro_district = models.CharField(max_length=4, choices=choices.MYCRO_DISTRICT_CHOICES, default=NOT_COMPLETED,
                                      verbose_name="Микрорайон")  # микрорайон
    location = models.CharField(max_length=200, verbose_name=u"Расположение", default=1)  #
    developer = models.CharField(max_length=100, verbose_name=u"Застройщик", default=1)  #
    theClass = models.CharField(max_length=2, choices=choices.THE_CLASS_CHOICES, default=NOT_COMPLETED,
                                verbose_name=u"Класс")
    numberOfStoreys = models.PositiveSmallIntegerField(verbose_name=u"Этажность", default=1)  #
    numberOfBuildings = models.PositiveSmallIntegerField(verbose_name=u"Количество домов", default=1)  #
    numberOfSectionsOrEntrances = models.CharField(max_length=100, verbose_name=u"Количество секций/подьездов",
                                                   default=1)
    constructionTechnology = models.CharField(max_length=2, choices=choices.THE_CONSTRUCTION_TECHNOLOGY_CHOICES,
                                              default=NOT_COMPLETED,
                                              verbose_name=u"Технология строительства")
    wallsType = models.CharField(max_length=2, choices=choices.THE_WALLS_TYPE_CHOICES, default=NOT_COMPLETED,
                                 verbose_name=u"Стены")
    warming = models.CharField(max_length=2, choices=choices.THE_WARMING_CHOICES, default=NOT_COMPLETED,
                               verbose_name=u"Утепление")  #
    roomHeight = models.PositiveSmallIntegerField(verbose_name=u"Высота помещений", default=1)  #
    numberOfApartmentsInTheHouse = models.PositiveSmallIntegerField(verbose_name=u"Кол-во квартир в доме", default=1)  #

    # ----------------------------------------------------
    numberOfOneRoom = models.PositiveSmallIntegerField(verbose_name=u"Кол-во 1к.кв.", default=1)
    squareOfOneRoom = models.PositiveSmallIntegerField(verbose_name=u"Площадь 1к.кв.", default=1)
    numberOfTwoRoom = models.PositiveSmallIntegerField(verbose_name=u"Кол-во 2к.кв.", default=1)
    squareOfTwoRoom = models.PositiveSmallIntegerField(verbose_name=u"Площадь 2к.кв.", default=1)
    numberOfThreeRoom = models.PositiveSmallIntegerField(verbose_name=u"Кол-во 3к.кв.", default=1)
    squareOfThreeRoom = models.PositiveSmallIntegerField(verbose_name=u"Площадь 3к.кв.", default=1)
    numberOfFourRoom = models.PositiveSmallIntegerField(verbose_name=u"Кол-во 4к.кв.", default=1)
    squareOfFourRoom = models.PositiveSmallIntegerField(verbose_name=u"Площадь 4к.кв.", default=1)
    # ----------------------------------------------------

    numberOfApartmensPerFloor = models.PositiveSmallIntegerField(verbose_name=u"Кол-во квартир на этаже", default=1)  #
    commercialPremises = models.PositiveSmallIntegerField(verbose_name=u"Коммерческие помещения",
                                                          null=True, default=1)  # пишешь только этаж
    heating = models.CharField(max_length=2, choices=choices.THE_HEATING_CHOICES, default=NOT_COMPLETED,
                               verbose_name=u"Отопление")
    gasification = models.BooleanField(verbose_name=u"Газификация", default=1)
    elevator = models.CharField(max_length=50, verbose_name=u"Лифт", default=1)  #
    parking = MultiSelectField(choices=choices.THE_PARKING_CHOICES, default=NOT_COMPLETED,
                               verbose_name=u"Паркинг")
    numberOfParkingSpaces = models.SmallIntegerField(verbose_name=u"Кол-во машиномест", default=1)
    price = models.SmallIntegerField(verbose_name=u"Цена за м2 у застройщика", default=1)
    completionDate = models.SmallIntegerField(verbose_name=u"Сдан и принят в эксплуатацию", default=1)
    description = models.TextField(verbose_name=u"Описание", default=1)

    slug = models.SlugField(max_length=150, unique=True, default='def')  # editable = False

    # def save(self, *args, **kwargs):
    #     _slug = '%s-%s' % (self.name, self.address)
    #     self.slug = slugify(_slug)
    #     super(NewBuilding, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('property_detail',kwargs={'slug': self.slug})

    def __str__(self):
        return self.address


class buildingImages(models.Model):
    building = models.ForeignKey(NewBuilding, on_delete=models.CASCADE, related_name='buildingImages')
    buildingImage = models.ImageField(verbose_name='Фото', blank=True, null=True, editable=True)

    def __str__(self):
        return '%s - %s' % (self.building, self.buildingImage)


class layoutImages(models.Model):
    building = models.ForeignKey(NewBuilding, on_delete=models.CASCADE, related_name='layoutImages')
    layoutImage = models.ImageField(verbose_name='Планировки', blank=True, null=True)

    def __str__(self):
        return '%s - %s' % (self.building, self.layoutImage)


class wayFromMetro(models.Model):
    # -------------------- default values:
    NOT_COMPLETED = 'nc'
    DEFAULT = 'Не заполнено'

    # --------------------- Metro choices
    SALTOVSKAYA_LINE = 'sl'
    ALEXEEVSKAYA_LINE = 'al'
    HOLODNOGORSKAYA_LINE = 'hl'

    # --------------------- Saltovskaya Line
    GEROYEV_TRUDA = 'gtr'
    STUDENCHESKAYA = 'stk'
    AKADEMINA_PAVLOVA = 'akp'
    AKADEMINA_BARABASHOVA = 'akb'
    KIEVSKAYA = 'kie'
    PUSHKINSKAYA = 'psh'
    UNIVERSITET = 'uni'
    ISTORICHESKII_MUZEI = 'ism'

    # ----------------------- Alekseevskaya Line
    POBEDA = 'pob'
    ALEXEEVSKAYA = 'ale'
    AVGUSTA_23 = '23a'
    BOTANICHESKII_SAD = 'bts'
    NAUCHNAYA = 'nau'
    GOSPROM = 'gos'
    ARCHITECTORA_BIKETOVA = 'arb'
    ZASCHITNIKOV_UKRAINI = 'zau'
    METROSTROITELEY = 'met'

    # ----------------------- Holodnogorsko zavodskaya Line
    HOLODNAYA_GORA = 'hog'
    UJNII_VOKZAL = 'ujv'
    CENTRALNII_RINOK = 'cer'
    PLOSHAD_KONSTITUCII = 'plk'
    PROSPECT_GAGARINA = 'prg'
    SPORTIVNAYA = 'spo'
    ZAVOD_IMENI_MALISHEVA = 'zim'
    MOSKOVSKII_PROSPECT = 'mop'
    DVOREC_SPORTA = 'dvs'
    ARMEISKAYA = 'arm'
    IMENI_MASELSKOGO = 'imm'
    TRAKTORNII_ZAVOD = 'trz'
    INDUSTRIALNAYA = 'ind'
    # THE_METRO_CHOICES = (
    #     (NOT_COMPLETED, DEFAULT),
    #     (SALTOVSKAYA_LINE, 'Салтовская линия'),
    #     (ALEXEEVSKAYA_LINE, 'Алексеевская линия'),
    #     (HOLODNOGORSKAYA_LINE, 'Холодногорская линия')
    # )
    THE_METRO_CHOICES = [
        (NOT_COMPLETED, DEFAULT),
        ('Салтовская линия', (
            (GEROYEV_TRUDA, 'Героев Труда'),
            (STUDENCHESKAYA, 'Студенческая'),
            (AKADEMINA_PAVLOVA, 'Академика Павлова'),
            (AKADEMINA_BARABASHOVA, 'Академика Барабашова'),
            (KIEVSKAYA, 'Киевская'),
            (PUSHKINSKAYA, 'Пушкинская'),
            (UNIVERSITET, 'Университет'),
            (ISTORICHESKII_MUZEI, 'Исторический Музей'),
        )
         ),
        ('Алексеевская линия', (
            (POBEDA, 'Победа'),
            (ALEXEEVSKAYA, 'Алексеевская'),
            (AVGUSTA_23, '23 Августа'),
            (BOTANICHESKII_SAD, 'Ботанический сад'),
            (NAUCHNAYA, 'Научная'),
            (GOSPROM, 'Госпром'),
            (ARCHITECTORA_BIKETOVA, 'Архитектора Бикетова'),
            (ZASCHITNIKOV_UKRAINI, 'Защитников Украины'),
            (METROSTROITELEY, 'Метростроителей'),
        )
         ),
        ('Холодногорско-Заводская линия', (
            (HOLODNAYA_GORA, 'Холодная Гора'),
            (UJNII_VOKZAL, 'Южный Вокзал'),
            (CENTRALNII_RINOK, 'Центральный рынок'),
            (PLOSHAD_KONSTITUCII, 'Площадь Конституции'),
            (PROSPECT_GAGARINA, 'Проспект Гагарина'),
            (SPORTIVNAYA, 'Спортинвая'),
            (ZAVOD_IMENI_MALISHEVA, 'Завод имени Малышева'),
            (MOSKOVSKII_PROSPECT, 'Московский Проспект'),
            (DVOREC_SPORTA, 'Дворец Спорта'),
            (ARMEISKAYA, 'Армейская'),
            (IMENI_MASELSKOGO, 'Имени А.С. Масельского'),
            (TRAKTORNII_ZAVOD, 'Тракторный Завод'),
            (INDUSTRIALNAYA, 'Индустриальная'),
        )
         ),
    ]
    # --------------------- Type of movement choices
    ON_FOOT = 'of'
    BY_CAR = 'bc'
    THE_TYPE_OF_MOVEMENT_CHOICES = (
        (NOT_COMPLETED, DEFAULT),
        (ON_FOOT, 'Пешком'),
        (BY_CAR, 'На машине'),
    )

    building = models.ForeignKey(NewBuilding, on_delete=models.CASCADE, related_name='wayFromMetro', )
    metroChoices = models.CharField(max_length=3, choices=THE_METRO_CHOICES, default=NOT_COMPLETED,
                                    verbose_name=u"Метро")
    time = models.SmallIntegerField(verbose_name=u"Время", default=1)
    typeOfMovement = models.CharField(max_length=2, choices=THE_TYPE_OF_MOVEMENT_CHOICES, default=NOT_COMPLETED,
                                      verbose_name=u"Как")
    numberOfMeters = models.SmallIntegerField(verbose_name=u"Расстояние", default=1)

    def __str__(self):
        return '%s - %s' % (self.building, self.metroChoices)
    # class Location(models.Model):
    #
    #     country = models.ForeignKey(NewBuilding)
    #     city = models.CharField(max_length=50)
    #     street = models.CharField(max_length=100)
    #
    # from smart_selects.db_fields import ChainedForeignKey

    # class Locat(models.Model):
    #
    #     country = ChainedForeignKey(
    #         NewBuilding,
    #         # chained_field="continent",
    #         # chained_model_field="continent",
    #         show_all=False,
    #         auto_choose=True,
    #         sort=True)
    #     city = models.CharField(max_length=50)
    #     street = models.CharField(max_length=100)
    # ------------------------------------

# class Country(models.Model):
#     name = models.CharField(max_length=200)
#     # name = models.CharField(max_length=200)
#     test = models.ForeignKey(
#         'self',
#         models.CASCADE,
#         null=True,
#         blank=True,
#         related_name='related_test_models'
#     )
#
#     for_inline = models.ForeignKey(
#         'self',
#         models.CASCADE,
#         null=True,
#         blank=True,
#         related_name='inline_test_models'
#     )
#
#     def __str__(self):
#         return self.name
#
#
# class Person(models.Model):
#     visited_countries = models.ManyToManyField('propertyInfo.Country')
#
#
# class Customer(models.Model):
#     first_name = models.CharField(max_length=255)
#     last_name = models.CharField(max_length=255)
#     is_premium = models.BooleanField(default=False)
#
#
# class Author(models.Model):
#     name = models.CharField(max_length=100)
#
#
# class Book(models.Model):
#     author = models.ForeignKey(Author, on_delete=models.CASCADE)
#     title = models.CharField(max_length=100)
