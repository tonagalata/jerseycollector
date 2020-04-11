from django.db import models
from datetime import datetime
from django.urls import reverse

from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser

FIFACOUNTRIES = (
  ('AFG', 'Afghanistan'),
  ('ALB', 'Albania'),
  ('ALG', 'Algeria'),
  ('ASA', 'American Samoa'),
  ('AND', 'Andorra'),
  ('ANG', 'Angola'),
  ('AIA', 'Anguilla'),
  ('ATG', 'Antigua and Barbuda'),
  ('ARG', 'Argentina'),
  ('ARM', 'Armenia'),
  ('ARU', 'Aruba'),
  ('AUS', 'Australia'),
  ('AUT', 'Austria'),
  ('AZE', 'Azerbaijan'),
  ('BAH', 'Bahamas'),
  ('BHR', 'Bahrain'),
  ('BAN', 'Bangladesh'),
  ('BRB', 'Barbados'),
  ('BLR', 'Belarus'),
  ('BEL', 'Belgium'),
  ('BLZ', 'Belize'),
  ('BEN', 'Benin'),
  ('BER', 'Bermuda'),
  ('BHU', 'Bhutan'),
  ('BOL', 'Bolivia'),
  ('BIH', 'Bosnia and Herzegovina'),
  ('BOT', 'Botswana'),
  ('BRA', 'Brazil'),
  ('VGB', 'British Virgin Islands'),
  ('BRU', 'Brunei'),
  ('BUL', 'Bulgaria'),
  ('BFA', 'Burkina Faso'),
  ('BDI', 'Burundi'),
  ('CAM', 'Cambodia'),
  ('CMR', 'Cameroon'),
  ('CAN', 'Canada'),
  ('CPV', 'Cape Verde'),
  ('CAY', 'Cayman Islands'),
  ('CTA', 'Central African Republic'),
  ('CHA', 'Chad'),
  ('CHI', 'Chile'),
  ('CHN', 'China'),
  ('TPE', 'Chinese Taipei'),
  ('COL', 'Colombia'),
  ('COM', 'Comoros'),
  ('CGO', 'Congo'),
  ('COD', 'DR Congo'),
  ('COK', 'Cook Islands'),
  ('CRC', 'Costa Rica'),
  ('CIV', 'Ivory Coast'),
  ('CRO', 'Croatia'),
  ('CUB', 'Cuba'),
  ('CUW', 'Curaçao'),
  ('CYP', 'Cyprus'),
  ('CZE', 'Czech Republic'),
  ('DEN', 'Denmark'),
  ('DJI', 'Djibouti'),
  ('DMA', 'Dominica'),
  ('DOM', 'Dominican Republic'),
  ('ECU', 'Ecuador'),
  ('EGY', 'Egypt'),
  ('SLV', 'El Salvador'),
  ('ENG', 'England'),
  ('EQG', 'Equatorial Guinea'),
  ('ERI', 'Eritrea'),
  ('EST', 'Estonia'),
  ('ETH', 'Ethiopia'),
  ('FRO', 'Faroe Islands'),
  ('FIJ', 'Fiji'),
  ('FIN', 'Finland'),
  ('FRA', 'France'),
  ('GAB', 'Gabon'),
  ('GAM', 'Gambia'),
  ('GEO', 'Georgia'),
  ('GER', 'Germany'),
  ('GHA', 'Ghana'),
  ('GRE', 'Greece'),
  ('GRN', 'Grenada'),
  ('GUM', 'Guam'),
  ('GUA', 'Guatemala'),
  ('GUI', 'Guinea'),
  ('GNB', 'Guinea-Bissau'),
  ('GUY', 'Guyana'),
  ('HAI', 'Haiti'),
  ('HON', 'Honduras'),
  ('HKG', 'Hong Kong'),
  ('HUN', 'Hungary'),
  ('ISL', 'Iceland'),
  ('IND', 'India'),
  ('IDN', 'Indonesia'),
  ('IRA', 'Iran'),
  ('IRQ', 'Iraq'),
  ('ISR', 'Israel'),
  ('ITA', 'Italy'),
  ('JAM', 'Jamaica'),
  ('JPN', 'Japan'),
  ('JOR', 'Jordan'),
  ('KAZ', 'Kazakhstan'),
  ('KEN', 'Kenya'),
  ('PRK', 'North Korea'),
  ('KOR', 'South Korea'),
  ('KUW', 'Kuwait'),
  ('KGZ', 'Kyrgyzstan'),
  ('LAO', 'Laos'),
  ('LVA', 'Latvia'),
  ('LIB', 'Lebanon'),
  ('LES', 'Lesotho'),
  ('LBR', 'Liberia'),
  ('LBY', 'Libya'),
  ('LIE', 'Liechtenstein'),
  ('LTU', 'Lithuania'),
  ('LUX', 'Luxembourg'),
  ('MAC', 'Macau'),
  ('MKD', 'North Macedonia'),
  ('MAD', 'Madagascar'),
  ('MWI', 'Malawi'),
  ('MAS', 'Malaysia'),
  ('MDV', 'Maldives'),
  ('MLI', 'Mali'),
  ('MLT', 'Malta'),
  ('MTN', 'Mauritania'),
  ('MRI', 'Mauritius'),
  ('MEX', 'Mexico'),
  ('MDA', 'Moldova'),
  ('MNG', 'Mongolia'),
  ('MNE', 'Montenegro'),
  ('MSR', 'Montserrat'),
  ('MAR', 'Morocco'),
  ('MOZ', 'Mozambique'),
  ('MYA', 'Myanmar'),
  ('NAM', 'Namibia'),
  ('NEP', 'Nepal'),
  ('NED', 'Netherlands'),
  ('NCL', 'New Caledonia'),
  ('NZL', 'New Zealand'),
  ('NCA', 'Nicaragua'),
  ('NIG', 'Niger'),
  ('NGA', 'Nigeria'),
  ('NIR', 'Northern Ireland'),
  ('NOR', 'Norway'),
  ('OMA', 'Oman'),
  ('PAK', 'Pakistan'),
  ('PLE', 'Palestine'),
  ('PAN', 'Panama'),
  ('PNG', 'Papua New Guinea'),
  ('PAR', 'Paraguay'),
  ('PER', 'Peru'),
  ('PHI', 'Philippines'),
  ('POL', 'Poland'),
  ('POR', 'Portugal'),
  ('PUR', 'Puerto Rico'),
  ('QAT', 'Qatar'),
  ('IRL', 'Republic of Ireland'),
  ('ROU', 'Romania'),
  ('RUS', 'Russia'),
  ('RWA', 'Rwanda'),
  ('SKN', 'Saint Kitts and Nevis'),
  ('LCA', 'Saint Lucia'),
  ('VIN', 'Saint Vincent and the Grenadines'),
  ('SAM', 'Samoa'),
  ('SMR', 'San Marino'),
  ('STP', 'São Tomé and Príncipe'),
  ('KSA', 'Saudi Arabia'),
  ('SCO', 'Scotland'),
  ('SEN', 'Senegal'),
  ('SRB', 'Serbia'),
  ('SEY', 'Seychelles'),
  ('SLE', 'Sierra Leone'),
  ('SIN', 'Singapore'),
  ('SVK', 'Slovakia'),
  ('SVN', 'Slovenia'),
  ('SOL', 'Solomon Islands'),
  ('SOM', 'Somalia'),
  ('RSA', 'South Africa'),
  ('ESP', 'Spain'),
  ('SRI', 'Sri Lanka'),
  ('SDN', 'Sudan'),
  ('SSD', 'South Sudan'),
  ('SUR', 'Suriname'),
  ('SWZ', 'Swaziland'),
  ('SWE', 'Sweden'),
  ('SUI', 'Switzerland'),
  ('SYR', 'Syria'),
  ('TAH', 'Tahiti'),
  ('TJK', 'Tajikistan'),
  ('TAN', 'Tanzania'),
  ('THA', 'Thailand'),
  ('TLS', 'Timor-Leste (East Timor)'),
  ('TOG', 'Togo'),
  ('TGA', 'Tonga'),
  ('TRI', 'Trinidad and Tobago'),
  ('TUN', 'Tunisia'),
  ('TUR', 'Turkey'),
  ('TKM', 'Turkmenistan'),
  ('TCA', 'Turks and Caicos Islands'),
  ('UGA', 'Uganda'),
  ('UKR', 'Ukraine'),
  ('UAE', 'United Arab Emirates'),
  ('USA', 'United States'),
  ('URU', 'Uruguay'),
  ('VIR', 'United States Virgin Islands'),
  ('UZB', 'Uzbekistan'),
  ('VAN', 'Vanuatu'),
  ('VEN', 'Venezuela'),
  ('VIE', 'Vietnam'),
  ('WAL', 'Wales'),
  ('YEM', 'Yemen'),
  ('ZAM', 'Zambia'),
  ('ZIM', 'Zimbabwe')
)

JERSEY_TYPE = (
  ('C', 'Club'),
  ('N', 'National'),
  ('Y', 'Youth')
)

# Create your models here.
class Player(models.Model):
  name = models.CharField(max_length=250)
  number = models.IntegerField()
  years_played = models.CharField(max_length=250)

  def __str__(self):
    return f"{self.name} was number {self.number}"

class Sponsor(models.Model):
  name = models.CharField(max_length=250)
  years_sponsored = models.DateField()

  def __str__(self):
    return f"{self.name} was a Sponsor"


class Jersey(models.Model):
  team_name = models.CharField(max_length=200, unique=True)
  jersey_type = models.CharField(
    max_length=1,
    choices=JERSEY_TYPE,
    default=JERSEY_TYPE[0][0]
  )
  country = models.CharField(max_length=3, choices=FIFACOUNTRIES, default=FIFACOUNTRIES[0][0])
  year_added = models.DateField()
  jersey_colors = models.CharField(max_length=250)
  jersey_description = models.TextField(max_length=250)
  players = models.ManyToManyField(Player)
  sponsors = models.ManyToManyField(Sponsor)
  user = models.ForeignKey(User, on_delete=models.CASCADE)

  def __str__(self):
    return f"This is a {self.team_name} Jersey from {self.get_country_display()}"
  
  def get_absolute_url(self):
    return reverse('detail', kwargs={'jersey_id': self.id})

class Photo(models.Model):
  url = models.CharField(max_length=200)
  jersey = models.ForeignKey(Jersey, on_delete=models.CASCADE)

  def __str__(self):
   return f"Photo for jersey: {self.jersey_id} @{self.url}"

class Photo_player(models.Model):
  url = models.CharField(max_length=200)
  player = models.ForeignKey(Player, on_delete=models.CASCADE)

  def __str__(self):
   return f"Photo for player: {self.player_id} @{self.url}"

class Photo_sponsor(models.Model):
  url = models.CharField(max_length=200)
  sponsor = models.ForeignKey(Sponsor, on_delete=models.CASCADE)

  def __str__(self):
   return f"Photo for sponsor: {self.sponsor_id} @{self.url}"

class Championship(models.Model):
  name = models.CharField(max_length=250)
  date = models.DateField()

  jersey = models.ForeignKey(Jersey, on_delete=models.CASCADE)

  def __str__(self):
    return f"Won {self.name} on {self.date}"

  class Meta:
    ordering = ['date']