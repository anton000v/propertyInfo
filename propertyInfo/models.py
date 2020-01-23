from django.db import models

from multiselectfield import MultiSelectField
from django.contrib.auth.models import User
from django.shortcuts import reverse
import propertyInfo.choices as choices


class NewBuilding(models.Model):
    class Meta():
        db_table = 'NewBuildings'
        ordering = ['name']

    name = models.CharField(max_length=200, verbose_name=u'Название', default=1)
    # messageG = forms.CharField(widget=forms.Textarea, label='lolkek')
    address = models.CharField(max_length=200, verbose_name=u"Адрес", default=1)  # адресс
    administrativeDistrict = models.CharField(max_length=2, choices=choices.THE_ADMINISTRATIVE_DISTRICT_CHOICES,
                                              default=choices.NOT_COMPLETED,
                                              verbose_name=u"Административный район")  #
    district = models.CharField(max_length=4, choices=choices.DISTRICT_CHOICES,
                                default=choices.NOT_COMPLETED,
                                verbose_name=u"Район")  # )
    micro_district = models.CharField(max_length=4, choices=choices.FULL_MICRO_DISTRICT_CHOICES,
                                      default=choices.NOT_COMPLETED,
                                      verbose_name="Микрорайон")  # микрорайон
    location = models.CharField(max_length=200, verbose_name=u"Расположение", default=1)  #
    developer = models.CharField(max_length=100, verbose_name=u"Застройщик", default=1)  #
    theClass = models.CharField(max_length=2, choices=choices.THE_CLASS_CHOICES, default=choices.NOT_COMPLETED,
                                verbose_name=u"Класс")
    numberOfStoreys = models.PositiveSmallIntegerField(verbose_name=u"Этажность", default=1)  #
    numberOfBuildings = models.PositiveSmallIntegerField(verbose_name=u"Количество домов", default=1)  #
    numberOfSectionsOrEntrances = models.CharField(max_length=100, verbose_name=u"Количество секций/подьездов",
                                                   default=1)
    constructionTechnology = models.CharField(max_length=2, choices=choices.THE_CONSTRUCTION_TECHNOLOGY_CHOICES,
                                              default=choices.NOT_COMPLETED,
                                              verbose_name=u"Технология строительства")
    wallsType = models.CharField(max_length=2, choices=choices.THE_WALLS_TYPE_CHOICES, default=choices.NOT_COMPLETED,
                                 verbose_name=u"Стены")
    warming = models.CharField(max_length=2, choices=choices.THE_WARMING_CHOICES, default=choices.NOT_COMPLETED,
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
    heating = models.CharField(max_length=2, choices=choices.THE_HEATING_CHOICES, default=choices.NOT_COMPLETED,
                               verbose_name=u"Отопление")
    gasification = models.BooleanField(verbose_name=u"Газификация", default=1)
    elevator = models.CharField(max_length=50, verbose_name=u"Лифт", default=1)  #
    parking = MultiSelectField(choices=choices.THE_PARKING_CHOICES, default=choices.NOT_COMPLETED,
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
        return reverse('property_detail', kwargs={'slug': self.slug})

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
    THE_METRO_CHOICES = [
        (choices.NOT_COMPLETED, choices.DEFAULT),
        ('Салтовская линия', (
            (choices.GEROYEV_TRUDA, 'Героев Труда'),
            (choices.STUDENCHESKAYA, 'Студенческая'),
            (choices.AKADEMINA_PAVLOVA, 'Академика Павлова'),
            (choices.AKADEMINA_BARABASHOVA, 'Академика Барабашова'),
            (choices.KIEVSKAYA, 'Киевская'),
            (choices.PUSHKINSKAYA, 'Пушкинская'),
            (choices.UNIVERSITET, 'Университет'),
            (choices.ISTORICHESKII_MUZEI, 'Исторический Музей'),
        )
         ),
        ('Алексеевская линия', (
            (choices.POBEDA, 'Победа'),
            (choices.ALEXEEVSKAYA, 'Алексеевская'),
            (choices.AVGUSTA_23, '23 Августа'),
            (choices.BOTANICHESKII_SAD, 'Ботанический сад'),
            (choices.NAUCHNAYA, 'Научная'),
            (choices.GOSPROM, 'Госпром'),
            (choices.ARCHITECTORA_BIKETOVA, 'Архитектора Бикетова'),
            (choices.ZASCHITNIKOV_UKRAINI, 'Защитников Украины'),
            (choices.METROSTROITELEY, 'Метростроителей'),
        )
         ),
        ('Холодногорско-Заводская линия', (
            (choices.HOLODNAYA_GORA, 'Холодная Гора'),
            (choices.UJNII_VOKZAL, 'Южный Вокзал'),
            (choices.CENTRALNII_RINOK, 'Центральный рынок'),
            (choices.PLOSHAD_KONSTITUCII, 'Площадь Конституции'),
            (choices.PROSPECT_GAGARINA, 'Проспект Гагарина'),
            (choices.SPORTIVNAYA, 'Спортинвая'),
            (choices.ZAVOD_IMENI_MALISHEVA, 'Завод имени Малышева'),
            (choices.MOSKOVSKII_PROSPECT, 'Московский Проспект'),
            (choices.DVOREC_SPORTA, 'Дворец Спорта'),
            (choices.ARMEISKAYA, 'Армейская'),
            (choices.IMENI_MASELSKOGO, 'Имени А.С. Масельского'),
            (choices.TRAKTORNII_ZAVOD, 'Тракторный Завод'),
            (choices.INDUSTRIALNAYA, 'Индустриальная'),
        )
         ),
    ]

    building = models.ForeignKey(NewBuilding, on_delete=models.CASCADE, related_name='wayFromMetro', )
    metroChoices = models.CharField(max_length=3, choices=THE_METRO_CHOICES, default=choices.NOT_COMPLETED,
                                    verbose_name=u"Метро")
    time = models.SmallIntegerField(verbose_name=u"Время", default=1)
    typeOfMovement = models.CharField(max_length=2, choices=choices.THE_TYPE_OF_MOVEMENT_CHOICES,
                                      default=choices.NOT_COMPLETED,
                                      verbose_name=u"Как")
    numberOfMeters = models.SmallIntegerField(verbose_name=u"Расстояние", default=1)

    def __str__(self):
        return '%s - %s' % (self.building, self.metroChoices)
