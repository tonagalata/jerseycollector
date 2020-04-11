# Generated by Django 3.0.4 on 2020-04-09 04:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Jersey',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team_name', models.CharField(max_length=200, unique=True)),
                ('jersey_type', models.CharField(choices=[('C', 'Club'), ('N', 'National'), ('Y', 'Youth')], default='C', max_length=1)),
                ('country', models.CharField(choices=[('AFG', 'Afghanistan'), ('ALB', 'Albania'), ('ALG', 'Algeria'), ('ASA', 'American Samoa'), ('AND', 'Andorra'), ('ANG', 'Angola'), ('AIA', 'Anguilla'), ('ATG', 'Antigua and Barbuda'), ('ARG', 'Argentina'), ('ARM', 'Armenia'), ('ARU', 'Aruba'), ('AUS', 'Australia'), ('AUT', 'Austria'), ('AZE', 'Azerbaijan'), ('BAH', 'Bahamas'), ('BHR', 'Bahrain'), ('BAN', 'Bangladesh'), ('BRB', 'Barbados'), ('BLR', 'Belarus'), ('BEL', 'Belgium'), ('BLZ', 'Belize'), ('BEN', 'Benin'), ('BER', 'Bermuda'), ('BHU', 'Bhutan'), ('BOL', 'Bolivia'), ('BIH', 'Bosnia and Herzegovina'), ('BOT', 'Botswana'), ('BRA', 'Brazil'), ('VGB', 'British Virgin Islands'), ('BRU', 'Brunei'), ('BUL', 'Bulgaria'), ('BFA', 'Burkina Faso'), ('BDI', 'Burundi'), ('CAM', 'Cambodia'), ('CMR', 'Cameroon'), ('CAN', 'Canada'), ('CPV', 'Cape Verde'), ('CAY', 'Cayman Islands'), ('CTA', 'Central African Republic'), ('CHA', 'Chad'), ('CHI', 'Chile'), ('CHN', 'China'), ('TPE', 'Chinese Taipei'), ('COL', 'Colombia'), ('COM', 'Comoros'), ('CGO', 'Congo'), ('COD', 'DR Congo'), ('COK', 'Cook Islands'), ('CRC', 'Costa Rica'), ('CIV', 'Ivory Coast'), ('CRO', 'Croatia'), ('CUB', 'Cuba'), ('CUW', 'Curaçao'), ('CYP', 'Cyprus'), ('CZE', 'Czech Republic'), ('DEN', 'Denmark'), ('DJI', 'Djibouti'), ('DMA', 'Dominica'), ('DOM', 'Dominican Republic'), ('ECU', 'Ecuador'), ('EGY', 'Egypt'), ('SLV', 'El Salvador'), ('ENG', 'England'), ('EQG', 'Equatorial Guinea'), ('ERI', 'Eritrea'), ('EST', 'Estonia'), ('ETH', 'Ethiopia'), ('FRO', 'Faroe Islands'), ('FIJ', 'Fiji'), ('FIN', 'Finland'), ('FRA', 'France'), ('GAB', 'Gabon'), ('GAM', 'Gambia'), ('GEO', 'Georgia'), ('GER', 'Germany'), ('GHA', 'Ghana'), ('GRE', 'Greece'), ('GRN', 'Grenada'), ('GUM', 'Guam'), ('GUA', 'Guatemala'), ('GUI', 'Guinea'), ('GNB', 'Guinea-Bissau'), ('GUY', 'Guyana'), ('HAI', 'Haiti'), ('HON', 'Honduras'), ('HKG', 'Hong Kong'), ('HUN', 'Hungary'), ('ISL', 'Iceland'), ('IND', 'India'), ('IDN', 'Indonesia'), ('IRA', 'Iran'), ('IRQ', 'Iraq'), ('ISR', 'Israel'), ('ITA', 'Italy'), ('JAM', 'Jamaica'), ('JPN', 'Japan'), ('JOR', 'Jordan'), ('KAZ', 'Kazakhstan'), ('KEN', 'Kenya'), ('PRK', 'North Korea'), ('KOR', 'South Korea'), ('KUW', 'Kuwait'), ('KGZ', 'Kyrgyzstan'), ('LAO', 'Laos'), ('LVA', 'Latvia'), ('LIB', 'Lebanon'), ('LES', 'Lesotho'), ('LBR', 'Liberia'), ('LBY', 'Libya'), ('LIE', 'Liechtenstein'), ('LTU', 'Lithuania'), ('LUX', 'Luxembourg'), ('MAC', 'Macau'), ('MKD', 'North Macedonia'), ('MAD', 'Madagascar'), ('MWI', 'Malawi'), ('MAS', 'Malaysia'), ('MDV', 'Maldives'), ('MLI', 'Mali'), ('MLT', 'Malta'), ('MTN', 'Mauritania'), ('MRI', 'Mauritius'), ('MEX', 'Mexico'), ('MDA', 'Moldova'), ('MNG', 'Mongolia'), ('MNE', 'Montenegro'), ('MSR', 'Montserrat'), ('MAR', 'Morocco'), ('MOZ', 'Mozambique'), ('MYA', 'Myanmar'), ('NAM', 'Namibia'), ('NEP', 'Nepal'), ('NED', 'Netherlands'), ('NCL', 'New Caledonia'), ('NZL', 'New Zealand'), ('NCA', 'Nicaragua'), ('NIG', 'Niger'), ('NGA', 'Nigeria'), ('NIR', 'Northern Ireland'), ('NOR', 'Norway'), ('OMA', 'Oman'), ('PAK', 'Pakistan'), ('PLE', 'Palestine'), ('PAN', 'Panama'), ('PNG', 'Papua New Guinea'), ('PAR', 'Paraguay'), ('PER', 'Peru'), ('PHI', 'Philippines'), ('POL', 'Poland'), ('POR', 'Portugal'), ('PUR', 'Puerto Rico'), ('QAT', 'Qatar'), ('IRL', 'Republic of Ireland'), ('ROU', 'Romania'), ('RUS', 'Russia'), ('RWA', 'Rwanda'), ('SKN', 'Saint Kitts and Nevis'), ('LCA', 'Saint Lucia'), ('VIN', 'Saint Vincent and the Grenadines'), ('SAM', 'Samoa'), ('SMR', 'San Marino'), ('STP', 'São Tomé and Príncipe'), ('KSA', 'Saudi Arabia'), ('SCO', 'Scotland'), ('SEN', 'Senegal'), ('SRB', 'Serbia'), ('SEY', 'Seychelles'), ('SLE', 'Sierra Leone'), ('SIN', 'Singapore'), ('SVK', 'Slovakia'), ('SVN', 'Slovenia'), ('SOL', 'Solomon Islands'), ('SOM', 'Somalia'), ('RSA', 'South Africa'), ('ESP', 'Spain'), ('SRI', 'Sri Lanka'), ('SDN', 'Sudan'), ('SSD', 'South Sudan'), ('SUR', 'Suriname'), ('SWZ', 'Swaziland'), ('SWE', 'Sweden'), ('SUI', 'Switzerland'), ('SYR', 'Syria'), ('TAH', 'Tahiti'), ('TJK', 'Tajikistan'), ('TAN', 'Tanzania'), ('THA', 'Thailand'), ('TLS', 'Timor-Leste (East Timor)'), ('TOG', 'Togo'), ('TGA', 'Tonga'), ('TRI', 'Trinidad and Tobago'), ('TUN', 'Tunisia'), ('TUR', 'Turkey'), ('TKM', 'Turkmenistan'), ('TCA', 'Turks and Caicos Islands'), ('UGA', 'Uganda'), ('UKR', 'Ukraine'), ('UAE', 'United Arab Emirates'), ('USA', 'United States'), ('URU', 'Uruguay'), ('VIR', 'United States Virgin Islands'), ('UZB', 'Uzbekistan'), ('VAN', 'Vanuatu'), ('VEN', 'Venezuela'), ('VIE', 'Vietnam'), ('WAL', 'Wales'), ('YEM', 'Yemen'), ('ZAM', 'Zambia'), ('ZIM', 'Zimbabwe')], default='AFG', max_length=3)),
                ('year_added', models.DateField()),
                ('jersey_colors', models.CharField(max_length=250)),
                ('jersey_description', models.TextField(max_length=250)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('number', models.IntegerField()),
                ('years_played', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Sponsor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('years_sponsored', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=200)),
                ('jersey', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.Jersey')),
            ],
        ),
        migrations.CreateModel(
            name='Championship',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('date', models.DateField()),
                ('jersey', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.Jersey')),
            ],
        ),
    ]