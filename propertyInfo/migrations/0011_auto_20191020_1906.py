# Generated by Django 2.2.5 on 2019-10-20 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('propertyInfo', '0010_auto_20191020_1854'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newbuilding',
            name='district',
            field=models.CharField(choices=[('nc', 'Не заполнено'), ('Центр', (('ce', 'Центр'), ('gos', 'Госпром'), ('nag', 'Нагорный'), ('sog', 'Сосновая горка'), ('sok', 'Сокольники'), ('sha', 'Шатиловка'), ('nam', 'Научная метро'), ('nic', 'Нижний центр'), ('pcm', 'Площадь Конституции метро'), ('pum', 'Пушкинская метро'))), ('Прилегающие к центру', (('ujd', 'ЮЖД'), ('cer', 'Центральный рынок'))), ('Гагарина (Левада)', (('gam', 'Спортивная метро'), ('spm', 'Спортивная метро'), ('noc', 'Новый цирк'), ('kor', 'Конный рынок'), ('zum', 'Защитников Украины метро'))), ('Одесская районы', (('ode', 'Одесская'), ('osn', 'Основа'), ('aer', 'Аэропорт'), ('arp', 'Артема парк'), ('zmm', 'Завод Малышева метро'), ('ujn', 'Южнопроэктная'))), ('Холодногорское направление', (('hog', 'Холодная гора'), ('lig', 'Лысая гора'), ('zal', 'Залютино'), ('bav', 'Бавария'), ('nov', 'Новоселовека'), ('pes', 'Песочин'))), ('Новожановское направление', (('nov', 'Новожаново'), ('zam', 'Завод Шевченко'), ('mos', 'Москалевка'))), ('Роганское направление', (('htz', 'ХТЗ'), ('inm', 'Индустриальная метро'), ('htm', 'ХТЗ метро'), ('vop', 'Восточный поселок'), ('rog', 'Рогань'), ('gor', 'Горизонт'), ('sol', 'Солнечный'), ('nop', 'Новозападный поселок'))), ('Пятихатское направление', (('jup', 'Жуковского поселок'), ('les', 'Лесопарк'), ('pya', 'Пятихатки'))), ('Салтовское направление', (('sal', 'Салтовка'), ('ses', 'Северная Салтовка'), ('sts', 'Старая Салтовка'), ('sad', 'Сабурова Дача'), ('frb', 'Французский Бульвар'), ('kip', 'Кирова поселок'), ('kul', 'Кулиничи'), ('tur', 'Тюринка'), ('bod', 'Большая Даниловка'), ('nem', 'Немышля'), ('jur', 'Журавлевка'), ('kim', 'Киевская метро'), ('shi', 'Шишковка'), ('mjk', 'МЖК'))), ('Алексеевское направление', (('ale', 'Алексеевка'), ('pap', 'Павловое Поле'), ('pav', 'Павловка'), ('sor', 'Сортировка'), ('iva', 'Ивановка'))), ('Новые Дома', (('nod', 'Новые Дома'), ('kor', 'Коммунальный Рынок'), ('dvs', 'Дворец Спорта'), ('22b', '22 Больница'), ('mam', 'Масельского метро'), ('arm', 'Армейская метро'), ('mpm', 'Московский Проспект метро')))], default='nc', max_length=4, verbose_name='Район'),
        ),
    ]
