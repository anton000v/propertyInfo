NOT_COMPLETED = 'nc'
DEFAULT = 'Не заполнено'

# ----------CENTER
CENTER = 'ce'
GOSPROM = 'gos'
NAGORNII = 'nag'
SOSNOVAYA_GORKA = 'sog'
SOKOLNIKI = 'sok'
SHATILOVKA = 'sha'
NAUCHAYA_METRO = 'nam'
NIJNII_CENTER = 'nic'
PLOSHAD_CONSTITUCII_METRO = 'pcm'
PUSHKINSKAYA_METRO = 'pum'

# ----------adjacent to the center
UJD = 'ujd'
CENTRALNII_RINOK = 'cer'

# -----------GAGARINA(LEVADA)
GAGARINA_METRO = 'gam'
SPORTIVNAYA_METRO = 'spm'
NOVII_CIRK = 'noc'
KONNII_RINOK = 'kor'
ZASCHITNIKOV_UKRAINI_METRO = 'zum'

# -----------ODESSA DISTRICTS
ODESSKAYA = 'ode'
OSNOVA = 'osn'
AEROPORT = 'aer'
ARTEMA_PARK = 'arp'
ZAVOD_MALISHEVA_METRO = 'zmm'
UJNOPROEKTNAYA = 'ujn'

# ----------HOLODNOGORSKOE DIRECTION
HOLODNAYA_GORA = 'hog'
LISAYA_GORA = 'lig'
ZALUTINO = 'zal'
BAVARIYA = 'bav'
NOVOSELOVKA = 'nov'
PESOCHIN = 'pes'

# ---------NOVOJANOVSKOYE DIRECTION
NOVOJANOVO = 'nov'
ZAVOD_SHEVCHENKO = 'zam'
MOSKALEVKA = 'mos'

# --------ROGANKOYE DIRECTION
HTZ = 'htz'
INDUSTRIALNAYA_METRO = 'inm'
HTZ_METRO = 'htm'
VOSTOCHNII_POSELOK = 'vop'
ROGAN = 'rog'
GORIZONT = 'gor'
SOLNECHNII = 'sol'
NOVOZAPADNII_POSELOK = 'nop'

# --------PYATIHATSKOE DIRECTION
JUKOVSKOGO_POSELOK = 'jup'
LESOPARK = 'les'
PYATIHATKI = 'pya'

# --------SALTOVSKOYE DIRECTION
SALTOVKA = 'sal'
SEVERNAYA_SALTOVKA = 'ses'
STARAYA_SALTOVKA = 'sts'
SABUROVA_DACHA = 'sad'
FRANCUZKII_BOULEVAR = 'frb'
KIROVA_POSELOK = 'kip'
KULINICHI = 'kul'
TURINKA = 'tur'
BOLSHAYA_DANILOVKA = 'bod'
NEMISHLYA = 'nem'
JURAVLEVKA = 'jur'
KIEVSKAYA_METRO = 'kim'
SHISHKOVKA = 'shi'
MJK = 'mjk'  # ??????????????????????

# ---------ALEXEYEVSKOE DIRECTION
ALEKSEEVKA = 'ale'
PAVLOVOE_POLE = 'pap'
PAVLOVKA = 'pav'
SORTIRIVKA = 'sor'
IVANOVKA = 'iva'

# -------NOVIE DOMA
NOVIE_DOMA = 'nod'
KOMMUNALNII_RINOK = 'kor'
DVOREC_SPORTA = 'dvs'
BOLNICA22 = '22b'
MASELSKOGO_METRO = 'mam'
ARMEYSKAYA_METRO = 'arm'
MOSKOVSKII_PROSPECT_METRO = 'mpm'

# example_dict = {'Center': 'cent', 'Novie Doma': 3}


DISTRICT_CHOICES = [
    (NOT_COMPLETED, DEFAULT),
    ('Центр', (
        (CENTER, 'Центр'),
        (GOSPROM, 'Госпром'),
        (NAGORNII, 'Нагорный'),
        (SOSNOVAYA_GORKA, 'Сосновая горка'),
        (SOKOLNIKI, 'Сокольники'),
        (SHATILOVKA, 'Шатиловка'),
        (NAUCHAYA_METRO, 'Научная метро'),
        (NIJNII_CENTER, 'Нижний центр'),
        (PLOSHAD_CONSTITUCII_METRO, 'Площадь Конституции метро'),
        (PUSHKINSKAYA_METRO, 'Пушкинская метро'),
    )
     ),
    ('Прилегающие к центру', (
        (UJD, 'ЮЖД'),
        (CENTRALNII_RINOK, 'Центральный рынок'),
    )
     ),
    ('Гагарина (Левада)', (
        (GAGARINA_METRO, 'Спортивная метро'),
        (SPORTIVNAYA_METRO, 'Спортивная метро'),
        (NOVII_CIRK, 'Новый цирк'),
        (KOMMUNALNII_RINOK, 'Конный рынок'),
        (ZASCHITNIKOV_UKRAINI_METRO, 'Защитников Украины метро'),
    )
     ),
    ('Одесская районы', (
        (ODESSKAYA, 'Одесская'),
        (OSNOVA, 'Основа'),
        (AEROPORT, 'Аэропорт'),
        (ARTEMA_PARK, 'Артема парк'),
        (ZAVOD_MALISHEVA_METRO, 'Завод Малышева метро'),
        (UJNOPROEKTNAYA, 'Южнопроэктная'),
    )
     ),
    ('Холодногорское направление', (
        (HOLODNAYA_GORA, 'Холодная гора'),
        (LISAYA_GORA, 'Лысая гора'),
        (ZALUTINO, 'Залютино'),
        (BAVARIYA, 'Бавария'),
        (NOVOSELOVKA, 'Новоселовека'),
        (PESOCHIN, 'Песочин'),
    )
     ),
    ('Новожановское направление', (
        (NOVOJANOVO, 'Новожаново'),
        (ZAVOD_SHEVCHENKO, 'Завод Шевченко'),
        (MOSKALEVKA, 'Москалевка'),
    )
     ),
    ('Роганское направление', (
        (HTZ, 'ХТЗ'),
        (INDUSTRIALNAYA_METRO, 'Индустриальная метро'),
        (HTZ_METRO, 'ХТЗ метро'),
        (VOSTOCHNII_POSELOK, 'Восточный поселок'),
        (ROGAN, 'Рогань'),
        (GORIZONT, 'Горизонт'),
        (SOLNECHNII, 'Солнечный'),
        (NOVOZAPADNII_POSELOK, 'Новозападный поселок'),
    )
     ),
    ('Пятихатское направление', (
        (JUKOVSKOGO_POSELOK, 'Жуковского поселок'),
        (LESOPARK, 'Лесопарк'),
        (PYATIHATKI, 'Пятихатки'),
    )
     ),
    ('Салтовское направление', (
        (SALTOVKA, 'Салтовка'),
        (SEVERNAYA_SALTOVKA, 'Северная Салтовка'),
        (STARAYA_SALTOVKA, 'Старая Салтовка'),
        (SABUROVA_DACHA, 'Сабурова Дача'),
        (FRANCUZKII_BOULEVAR, 'Французский Бульвар'),
        (KIROVA_POSELOK, 'Кирова поселок'),
        (KULINICHI, 'Кулиничи'),
        (TURINKA, 'Тюринка'),
        (BOLSHAYA_DANILOVKA, 'Большая Даниловка'),
        (NEMISHLYA, 'Немышля'),
        (JURAVLEVKA, 'Журавлевка'),
        (KIEVSKAYA_METRO, 'Киевская метро'),
        (SHISHKOVKA, 'Шишковка'),
        (MJK, 'МЖК'),
    )
     ),
    ('Алексеевское направление', (
        (ALEKSEEVKA, 'Алексеевка'),
        (PAVLOVOE_POLE, 'Павловое Поле'),
        (PAVLOVKA, 'Павловка'),
        (SORTIRIVKA, 'Сортировка'),
        (IVANOVKA, 'Ивановка'),
    )
     ),
    ('Новые Дома', (
        (NOVIE_DOMA, 'Новые Дома'),
        (KOMMUNALNII_RINOK, 'Коммунальный Рынок'),
        (DVOREC_SPORTA, 'Дворец Спорта'),
        (BOLNICA22, '22 Больница'),
        (MASELSKOGO_METRO, 'Масельского метро'),
        (ARMEYSKAYA_METRO, 'Армейская метро'),
        (MOSKOVSKII_PROSPECT_METRO, 'Московский Проспект метро'),
    )
     ),
]
