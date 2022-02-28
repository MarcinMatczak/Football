from django.db import models


class Ekstraklasa(models.Model):
    name = models.CharField(max_length=264)
    points = models.IntegerField(default=0)
    scored = models.IntegerField(default=0)
    conceded = models.IntegerField(default=0)
    difference = models.IntegerField(default=0)
    wins = models.IntegerField(default=0)
    loses = models.IntegerField(default=0)
    draws = models.IntegerField(default=0)
    strength = models.IntegerField(default=2000)
    image = models.ImageField(upload_to='upload/')
    country = models.CharField(max_length=264, default='()')

    def __str__(self):
        return self.name

class Pierwsza_Liga(models.Model):
    name = models.CharField(max_length=264)
    points = models.IntegerField(default=0)
    scored = models.IntegerField(default=0)
    conceded = models.IntegerField(default=0)
    difference = models.IntegerField(default=0)
    wins = models.IntegerField(default=0)
    loses = models.IntegerField(default=0)
    draws = models.IntegerField(default=0)
    strength = models.IntegerField(default=2000)
    image = models.ImageField(upload_to='upload/')
    country = models.CharField(max_length=264, default='()')
    def __str__(self):
        return self.name

class Druga_Liga(models.Model):
    name = models.CharField(max_length=264)
    points = models.IntegerField(default=0)
    scored = models.IntegerField(default=0)
    conceded = models.IntegerField(default=0)
    difference = models.IntegerField(default=0)
    wins = models.IntegerField(default=0)
    loses = models.IntegerField(default=0)
    draws = models.IntegerField(default=0)
    strength = models.IntegerField(default=2000)
    image = models.ImageField(upload_to='upload/')
    country = models.CharField(max_length=264, default='()')
    def __str__(self):
        return self.name

class Hiszpania(models.Model):
    name = models.CharField(max_length=264)
    points = models.IntegerField(default=0)
    scored = models.IntegerField(default=0)
    conceded = models.IntegerField(default=0)
    difference = models.IntegerField(default=0)
    wins = models.IntegerField(default=0)
    loses = models.IntegerField(default=0)
    draws = models.IntegerField(default=0)
    strength = models.IntegerField(default=2000)
    image = models.ImageField(upload_to='upload/')
    country = models.CharField(max_length=264, default='()')
    def __str__(self):
        return self.name

class Anglia(models.Model):
    name = models.CharField(max_length=264)
    points = models.IntegerField(default=0)
    scored = models.IntegerField(default=0)
    conceded = models.IntegerField(default=0)
    difference = models.IntegerField(default=0)
    wins = models.IntegerField(default=0)
    loses = models.IntegerField(default=0)
    draws = models.IntegerField(default=0)
    strength = models.IntegerField(default=2000)
    image = models.ImageField(upload_to='upload/')
    country = models.CharField(max_length=264, default='()')
    def __str__(self):
        return self.name

class Niemcy(models.Model):
    name = models.CharField(max_length=264)
    points = models.IntegerField(default=0)
    scored = models.IntegerField(default=0)
    conceded = models.IntegerField(default=0)
    difference = models.IntegerField(default=0)
    wins = models.IntegerField(default=0)
    loses = models.IntegerField(default=0)
    draws = models.IntegerField(default=0)
    strength = models.IntegerField(default=2000)
    image = models.ImageField(upload_to='upload/')
    country = models.CharField(max_length=264, default='()')
    def __str__(self):
        return self.name

class Wlochy(models.Model):
    name = models.CharField(max_length=264)
    points = models.IntegerField(default=0)
    scored = models.IntegerField(default=0)
    conceded = models.IntegerField(default=0)
    difference = models.IntegerField(default=0)
    wins = models.IntegerField(default=0)
    loses = models.IntegerField(default=0)
    draws = models.IntegerField(default=0)
    strength = models.IntegerField(default=2000)
    image = models.ImageField(upload_to='upload/')
    country = models.CharField(max_length=264, default='()')
    def __str__(self):
        return self.name

class Francja(models.Model):
    name = models.CharField(max_length=264)
    points = models.IntegerField(default=0)
    scored = models.IntegerField(default=0)
    conceded = models.IntegerField(default=0)
    difference = models.IntegerField(default=0)
    wins = models.IntegerField(default=0)
    loses = models.IntegerField(default=0)
    draws = models.IntegerField(default=0)
    strength = models.IntegerField(default=2000)
    image = models.ImageField(upload_to='upload/')
    country = models.CharField(max_length=264, default='()')
    def __str__(self):
        return self.name

class Portugalia(models.Model):
    name = models.CharField(max_length=264)
    points = models.IntegerField(default=0)
    scored = models.IntegerField(default=0)
    conceded = models.IntegerField(default=0)
    difference = models.IntegerField(default=0)
    wins = models.IntegerField(default=0)
    loses = models.IntegerField(default=0)
    draws = models.IntegerField(default=0)
    strength = models.IntegerField(default=2000)
    image = models.ImageField(upload_to='upload/')
    country = models.CharField(max_length=264, default='()')
    def __str__(self):
        return self.name
class Rosja(models.Model):
    name = models.CharField(max_length=264)
    points = models.IntegerField(default=0)
    scored = models.IntegerField(default=0)
    conceded = models.IntegerField(default=0)
    difference = models.IntegerField(default=0)
    wins = models.IntegerField(default=0)
    loses = models.IntegerField(default=0)
    draws = models.IntegerField(default=0)
    strength = models.IntegerField(default=2000)
    image = models.ImageField(upload_to='upload/')
    country = models.CharField(max_length=264, default='()')
    def __str__(self):
        return self.name
class Belgia(models.Model):
    name = models.CharField(max_length=264)
    points = models.IntegerField(default=0)
    scored = models.IntegerField(default=0)
    conceded = models.IntegerField(default=0)
    difference = models.IntegerField(default=0)
    wins = models.IntegerField(default=0)
    loses = models.IntegerField(default=0)
    draws = models.IntegerField(default=0)
    strength = models.IntegerField(default=2000)
    image = models.ImageField(upload_to='upload/')
    country = models.CharField(max_length=264, default='()')
    def __str__(self):
        return self.name
class Ukraina(models.Model):
    name = models.CharField(max_length=264)
    points = models.IntegerField(default=0)
    scored = models.IntegerField(default=0)
    conceded = models.IntegerField(default=0)
    difference = models.IntegerField(default=0)
    wins = models.IntegerField(default=0)
    loses = models.IntegerField(default=0)
    draws = models.IntegerField(default=0)
    strength = models.IntegerField(default=2000)
    image = models.ImageField(upload_to='upload/')
    country = models.CharField(max_length=264, default='()')
    def __str__(self):
        return self.name
class Holandia(models.Model):
    name = models.CharField(max_length=264)
    points = models.IntegerField(default=0)
    scored = models.IntegerField(default=0)
    conceded = models.IntegerField(default=0)
    difference = models.IntegerField(default=0)
    wins = models.IntegerField(default=0)
    loses = models.IntegerField(default=0)
    draws = models.IntegerField(default=0)
    strength = models.IntegerField(default=2000)
    image = models.ImageField(upload_to='upload/')
    country = models.CharField(max_length=264, default='()')
    def __str__(self):
        return self.name
class Turcja(models.Model):
    name = models.CharField(max_length=264)
    points = models.IntegerField(default=0)
    scored = models.IntegerField(default=0)
    conceded = models.IntegerField(default=0)
    difference = models.IntegerField(default=0)
    wins = models.IntegerField(default=0)
    loses = models.IntegerField(default=0)
    draws = models.IntegerField(default=0)
    strength = models.IntegerField(default=2000)
    image = models.ImageField(upload_to='upload/')
    country = models.CharField(max_length=264, default='()')
    def __str__(self):
        return self.name
class Austria(models.Model):
    name = models.CharField(max_length=264)
    points = models.IntegerField(default=0)
    scored = models.IntegerField(default=0)
    conceded = models.IntegerField(default=0)
    difference = models.IntegerField(default=0)
    wins = models.IntegerField(default=0)
    loses = models.IntegerField(default=0)
    draws = models.IntegerField(default=0)
    strength = models.IntegerField(default=2000)
    image = models.ImageField(upload_to='upload/')
    country = models.CharField(max_length=264, default='()')
    def __str__(self):
        return self.name
class Dania(models.Model):
    name = models.CharField(max_length=264)
    points = models.IntegerField(default=0)
    scored = models.IntegerField(default=0)
    conceded = models.IntegerField(default=0)
    difference = models.IntegerField(default=0)
    wins = models.IntegerField(default=0)
    loses = models.IntegerField(default=0)
    draws = models.IntegerField(default=0)
    strength = models.IntegerField(default=2000)
    image = models.ImageField(upload_to='upload/')
    country = models.CharField(max_length=264, default='()')
    def __str__(self):
        return self.name
class Szkocja(models.Model):
    name = models.CharField(max_length=264)
    points = models.IntegerField(default=0)
    scored = models.IntegerField(default=0)
    conceded = models.IntegerField(default=0)
    difference = models.IntegerField(default=0)
    wins = models.IntegerField(default=0)
    loses = models.IntegerField(default=0)
    draws = models.IntegerField(default=0)
    strength = models.IntegerField(default=2000)
    image = models.ImageField(upload_to='upload/')
    country = models.CharField(max_length=264, default='()')
    def __str__(self):
        return self.name
class Czechy(models.Model):
    name = models.CharField(max_length=264)
    points = models.IntegerField(default=0)
    scored = models.IntegerField(default=0)
    conceded = models.IntegerField(default=0)
    difference = models.IntegerField(default=0)
    wins = models.IntegerField(default=0)
    loses = models.IntegerField(default=0)
    draws = models.IntegerField(default=0)
    strength = models.IntegerField(default=2000)
    image = models.ImageField(upload_to='upload/')
    country = models.CharField(max_length=264, default='()')
    def __str__(self):
        return self.name
class Cypr(models.Model):
    name = models.CharField(max_length=264)
    points = models.IntegerField(default=0)
    scored = models.IntegerField(default=0)
    conceded = models.IntegerField(default=0)
    difference = models.IntegerField(default=0)
    wins = models.IntegerField(default=0)
    loses = models.IntegerField(default=0)
    draws = models.IntegerField(default=0)
    strength = models.IntegerField(default=2000)
    image = models.ImageField(upload_to='upload/')
    country = models.CharField(max_length=264, default='()')
    def __str__(self):
        return self.name
class Szwajcaria(models.Model):
    name = models.CharField(max_length=264)
    points = models.IntegerField(default=0)
    scored = models.IntegerField(default=0)
    conceded = models.IntegerField(default=0)
    difference = models.IntegerField(default=0)
    wins = models.IntegerField(default=0)
    loses = models.IntegerField(default=0)
    draws = models.IntegerField(default=0)
    strength = models.IntegerField(default=2000)
    image = models.ImageField(upload_to='upload/')
    country = models.CharField(max_length=264, default='()')
    def __str__(self):
        return self.name
class Grecja(models.Model):
    name = models.CharField(max_length=264)
    points = models.IntegerField(default=0)
    scored = models.IntegerField(default=0)
    conceded = models.IntegerField(default=0)
    difference = models.IntegerField(default=0)
    wins = models.IntegerField(default=0)
    loses = models.IntegerField(default=0)
    draws = models.IntegerField(default=0)
    strength = models.IntegerField(default=2000)
    image = models.ImageField(upload_to='upload/')
    country = models.CharField(max_length=264, default='()')
    def __str__(self):
        return self.name
class Serbia(models.Model):
    name = models.CharField(max_length=264)
    points = models.IntegerField(default=0)
    scored = models.IntegerField(default=0)
    conceded = models.IntegerField(default=0)
    difference = models.IntegerField(default=0)
    wins = models.IntegerField(default=0)
    loses = models.IntegerField(default=0)
    draws = models.IntegerField(default=0)
    strength = models.IntegerField(default=2000)
    image = models.ImageField(upload_to='upload/')
    country = models.CharField(max_length=264, default='()')
    def __str__(self):
        return self.name
class Chorwacja(models.Model):
    name = models.CharField(max_length=264)
    points = models.IntegerField(default=0)
    scored = models.IntegerField(default=0)
    conceded = models.IntegerField(default=0)
    difference = models.IntegerField(default=0)
    wins = models.IntegerField(default=0)
    loses = models.IntegerField(default=0)
    draws = models.IntegerField(default=0)
    strength = models.IntegerField(default=2000)
    image = models.ImageField(upload_to='upload/')
    country = models.CharField(max_length=264, default='()')
    def __str__(self):
        return self.name
class Szwecja(models.Model):
    name = models.CharField(max_length=264)
    points = models.IntegerField(default=0)
    scored = models.IntegerField(default=0)
    conceded = models.IntegerField(default=0)
    difference = models.IntegerField(default=0)
    wins = models.IntegerField(default=0)
    loses = models.IntegerField(default=0)
    draws = models.IntegerField(default=0)
    strength = models.IntegerField(default=2000)
    image = models.ImageField(upload_to='upload/')
    country = models.CharField(max_length=264, default='()')
    def __str__(self):
        return self.name
class Norwegia(models.Model):
    name = models.CharField(max_length=264)
    points = models.IntegerField(default=0)
    scored = models.IntegerField(default=0)
    conceded = models.IntegerField(default=0)
    difference = models.IntegerField(default=0)
    wins = models.IntegerField(default=0)
    loses = models.IntegerField(default=0)
    draws = models.IntegerField(default=0)
    strength = models.IntegerField(default=2000)
    image = models.ImageField(upload_to='upload/')
    country = models.CharField(max_length=264, default='()')
    def __str__(self):
        return self.name
class Izrael(models.Model):
    name = models.CharField(max_length=264)
    points = models.IntegerField(default=0)
    scored = models.IntegerField(default=0)
    conceded = models.IntegerField(default=0)
    difference = models.IntegerField(default=0)
    wins = models.IntegerField(default=0)
    loses = models.IntegerField(default=0)
    draws = models.IntegerField(default=0)
    strength = models.IntegerField(default=2000)
    image = models.ImageField(upload_to='upload/')
    country = models.CharField(max_length=264, default='()')
    def __str__(self):
        return self.name
class Kazachstan(models.Model):
    name = models.CharField(max_length=264)
    points = models.IntegerField(default=0)
    scored = models.IntegerField(default=0)
    conceded = models.IntegerField(default=0)
    difference = models.IntegerField(default=0)
    wins = models.IntegerField(default=0)
    loses = models.IntegerField(default=0)
    draws = models.IntegerField(default=0)
    strength = models.IntegerField(default=2000)
    image = models.ImageField(upload_to='upload/')
    country = models.CharField(max_length=264, default='()')
    def __str__(self):
        return self.name
class Bialorus(models.Model):
    name = models.CharField(max_length=264)
    points = models.IntegerField(default=0)
    scored = models.IntegerField(default=0)
    conceded = models.IntegerField(default=0)
    difference = models.IntegerField(default=0)
    wins = models.IntegerField(default=0)
    loses = models.IntegerField(default=0)
    draws = models.IntegerField(default=0)
    strength = models.IntegerField(default=2000)
    image = models.ImageField(upload_to='upload/')
    country = models.CharField(max_length=264, default='()')
    def __str__(self):
        return self.name
class Azerbejdzan(models.Model):
    name = models.CharField(max_length=264)
    points = models.IntegerField(default=0)
    scored = models.IntegerField(default=0)
    conceded = models.IntegerField(default=0)
    difference = models.IntegerField(default=0)
    wins = models.IntegerField(default=0)
    loses = models.IntegerField(default=0)
    draws = models.IntegerField(default=0)
    strength = models.IntegerField(default=2000)
    image = models.ImageField(upload_to='upload/')
    country = models.CharField(max_length=264, default='()')
    def __str__(self):
        return self.name
class Bulgaria(models.Model):
    name = models.CharField(max_length=264)
    points = models.IntegerField(default=0)
    scored = models.IntegerField(default=0)
    conceded = models.IntegerField(default=0)
    difference = models.IntegerField(default=0)
    wins = models.IntegerField(default=0)
    loses = models.IntegerField(default=0)
    draws = models.IntegerField(default=0)
    strength = models.IntegerField(default=2000)
    image = models.ImageField(upload_to='upload/')
    country = models.CharField(max_length=264, default='()')
    def __str__(self):
        return self.name
class Rumunia(models.Model):
    name = models.CharField(max_length=264)
    points = models.IntegerField(default=0)
    scored = models.IntegerField(default=0)
    conceded = models.IntegerField(default=0)
    difference = models.IntegerField(default=0)
    wins = models.IntegerField(default=0)
    loses = models.IntegerField(default=0)
    draws = models.IntegerField(default=0)
    strength = models.IntegerField(default=2000)
    image = models.ImageField(upload_to='upload/')
    country = models.CharField(max_length=264, default='()')
    def __str__(self):
        return self.name
class Slowacja(models.Model):
    name = models.CharField(max_length=264)
    points = models.IntegerField(default=0)
    scored = models.IntegerField(default=0)
    conceded = models.IntegerField(default=0)
    difference = models.IntegerField(default=0)
    wins = models.IntegerField(default=0)
    loses = models.IntegerField(default=0)
    draws = models.IntegerField(default=0)
    strength = models.IntegerField(default=2000)
    image = models.ImageField(upload_to='upload/')
    country = models.CharField(max_length=264, default='()')
    def __str__(self):
        return self.name
class Liechtenstein(models.Model):
    name = models.CharField(max_length=264)
    points = models.IntegerField(default=0)
    scored = models.IntegerField(default=0)
    conceded = models.IntegerField(default=0)
    difference = models.IntegerField(default=0)
    wins = models.IntegerField(default=0)
    loses = models.IntegerField(default=0)
    draws = models.IntegerField(default=0)
    strength = models.IntegerField(default=2000)
    image = models.ImageField(upload_to='upload/')
    country = models.CharField(max_length=264, default='()')
    def __str__(self):
        return self.name
class Slowenia(models.Model):
    name = models.CharField(max_length=264)
    points = models.IntegerField(default=0)
    scored = models.IntegerField(default=0)
    conceded = models.IntegerField(default=0)
    difference = models.IntegerField(default=0)
    wins = models.IntegerField(default=0)
    loses = models.IntegerField(default=0)
    draws = models.IntegerField(default=0)
    strength = models.IntegerField(default=2000)
    image = models.ImageField(upload_to='upload/')
    country = models.CharField(max_length=264, default='()')
    def __str__(self):
        return self.name
class Wegry(models.Model):
    name = models.CharField(max_length=264)
    points = models.IntegerField(default=0)
    scored = models.IntegerField(default=0)
    conceded = models.IntegerField(default=0)
    difference = models.IntegerField(default=0)
    wins = models.IntegerField(default=0)
    loses = models.IntegerField(default=0)
    draws = models.IntegerField(default=0)
    strength = models.IntegerField(default=2000)
    image = models.ImageField(upload_to='upload/')
    country = models.CharField(max_length=264, default='()')
    def __str__(self):
        return self.name
class Luxembourg(models.Model):
    name = models.CharField(max_length=264)
    points = models.IntegerField(default=0)
    scored = models.IntegerField(default=0)
    conceded = models.IntegerField(default=0)
    difference = models.IntegerField(default=0)
    wins = models.IntegerField(default=0)
    loses = models.IntegerField(default=0)
    draws = models.IntegerField(default=0)
    strength = models.IntegerField(default=2000)
    image = models.ImageField(upload_to='upload/')
    country = models.CharField(max_length=264, default='()')
    def __str__(self):
        return self.name
class Litwa(models.Model):
    name = models.CharField(max_length=264)
    points = models.IntegerField(default=0)
    scored = models.IntegerField(default=0)
    conceded = models.IntegerField(default=0)
    difference = models.IntegerField(default=0)
    wins = models.IntegerField(default=0)
    loses = models.IntegerField(default=0)
    draws = models.IntegerField(default=0)
    strength = models.IntegerField(default=2000)
    image = models.ImageField(upload_to='upload/')
    country = models.CharField(max_length=264, default='()')
    def __str__(self):
        return self.name
class Armenia(models.Model):
    name = models.CharField(max_length=264)
    points = models.IntegerField(default=0)
    scored = models.IntegerField(default=0)
    conceded = models.IntegerField(default=0)
    difference = models.IntegerField(default=0)
    wins = models.IntegerField(default=0)
    loses = models.IntegerField(default=0)
    draws = models.IntegerField(default=0)
    strength = models.IntegerField(default=2000)
    image = models.ImageField(upload_to='upload/')
    country = models.CharField(max_length=264, default='()')
    def __str__(self):
        return self.name
class Lotwa(models.Model):
    name = models.CharField(max_length=264)
    points = models.IntegerField(default=0)
    scored = models.IntegerField(default=0)
    conceded = models.IntegerField(default=0)
    difference = models.IntegerField(default=0)
    wins = models.IntegerField(default=0)
    loses = models.IntegerField(default=0)
    draws = models.IntegerField(default=0)
    strength = models.IntegerField(default=2000)
    image = models.ImageField(upload_to='upload/')
    country = models.CharField(max_length=264, default='()')
    def __str__(self):
        return self.name
class Albania(models.Model):
    name = models.CharField(max_length=264)
    points = models.IntegerField(default=0)
    scored = models.IntegerField(default=0)
    conceded = models.IntegerField(default=0)
    difference = models.IntegerField(default=0)
    wins = models.IntegerField(default=0)
    loses = models.IntegerField(default=0)
    draws = models.IntegerField(default=0)
    strength = models.IntegerField(default=2000)
    image = models.ImageField(upload_to='upload/')
    country = models.CharField(max_length=264, default='()')
    def __str__(self):
        return self.name
class Macedonia(models.Model):
    name = models.CharField(max_length=264)
    points = models.IntegerField(default=0)
    scored = models.IntegerField(default=0)
    conceded = models.IntegerField(default=0)
    difference = models.IntegerField(default=0)
    wins = models.IntegerField(default=0)
    loses = models.IntegerField(default=0)
    draws = models.IntegerField(default=0)
    strength = models.IntegerField(default=2000)
    image = models.ImageField(upload_to='upload/')
    country = models.CharField(max_length=264, default='()')
    def __str__(self):
        return self.name
class Bosnia(models.Model):
    name = models.CharField(max_length=264)
    points = models.IntegerField(default=0)
    scored = models.IntegerField(default=0)
    conceded = models.IntegerField(default=0)
    difference = models.IntegerField(default=0)
    wins = models.IntegerField(default=0)
    loses = models.IntegerField(default=0)
    draws = models.IntegerField(default=0)
    strength = models.IntegerField(default=2000)
    image = models.ImageField(upload_to='upload/')
    country = models.CharField(max_length=264, default='()')
    def __str__(self):
        return self.name
class Moldawia(models.Model):
    name = models.CharField(max_length=264)
    points = models.IntegerField(default=0)
    scored = models.IntegerField(default=0)
    conceded = models.IntegerField(default=0)
    difference = models.IntegerField(default=0)
    wins = models.IntegerField(default=0)
    loses = models.IntegerField(default=0)
    draws = models.IntegerField(default=0)
    strength = models.IntegerField(default=2000)
    image = models.ImageField(upload_to='upload/')
    country = models.CharField(max_length=264, default='()')
    def __str__(self):
        return self.name
class Irlandia(models.Model):
    name = models.CharField(max_length=264)
    points = models.IntegerField(default=0)
    scored = models.IntegerField(default=0)
    conceded = models.IntegerField(default=0)
    difference = models.IntegerField(default=0)
    wins = models.IntegerField(default=0)
    loses = models.IntegerField(default=0)
    draws = models.IntegerField(default=0)
    strength = models.IntegerField(default=2000)
    image = models.ImageField(upload_to='upload/')
    country = models.CharField(max_length=264, default='()')
    def __str__(self):
        return self.name
class Finlandia(models.Model):
    name = models.CharField(max_length=264)
    points = models.IntegerField(default=0)
    scored = models.IntegerField(default=0)
    conceded = models.IntegerField(default=0)
    difference = models.IntegerField(default=0)
    wins = models.IntegerField(default=0)
    loses = models.IntegerField(default=0)
    draws = models.IntegerField(default=0)
    strength = models.IntegerField(default=2000)
    image = models.ImageField(upload_to='upload/')
    country = models.CharField(max_length=264, default='()')
    def __str__(self):
        return self.name
class Gruzja(models.Model):
    name = models.CharField(max_length=264)
    points = models.IntegerField(default=0)
    scored = models.IntegerField(default=0)
    conceded = models.IntegerField(default=0)
    difference = models.IntegerField(default=0)
    wins = models.IntegerField(default=0)
    loses = models.IntegerField(default=0)
    draws = models.IntegerField(default=0)
    strength = models.IntegerField(default=2000)
    image = models.ImageField(upload_to='upload/')
    country = models.CharField(max_length=264, default='()')
    def __str__(self):
        return self.name
class Malta(models.Model):
    name = models.CharField(max_length=264)
    points = models.IntegerField(default=0)
    scored = models.IntegerField(default=0)
    conceded = models.IntegerField(default=0)
    difference = models.IntegerField(default=0)
    wins = models.IntegerField(default=0)
    loses = models.IntegerField(default=0)
    draws = models.IntegerField(default=0)
    strength = models.IntegerField(default=2000)
    image = models.ImageField(upload_to='upload/')
    country = models.CharField(max_length=264, default='()')
    def __str__(self):
        return self.name
class Islandia(models.Model):
    name = models.CharField(max_length=264)
    points = models.IntegerField(default=0)
    scored = models.IntegerField(default=0)
    conceded = models.IntegerField(default=0)
    difference = models.IntegerField(default=0)
    wins = models.IntegerField(default=0)
    loses = models.IntegerField(default=0)
    draws = models.IntegerField(default=0)
    strength = models.IntegerField(default=2000)
    image = models.ImageField(upload_to='upload/')
    country = models.CharField(max_length=264, default='()')
    def __str__(self):
        return self.name
class Walia(models.Model):
    name = models.CharField(max_length=264)
    points = models.IntegerField(default=0)
    scored = models.IntegerField(default=0)
    conceded = models.IntegerField(default=0)
    difference = models.IntegerField(default=0)
    wins = models.IntegerField(default=0)
    loses = models.IntegerField(default=0)
    draws = models.IntegerField(default=0)
    strength = models.IntegerField(default=2000)
    image = models.ImageField(upload_to='upload/')
    country = models.CharField(max_length=264, default='()')
    def __str__(self):
        return self.name
class Irlandia_Pln(models.Model):
    name = models.CharField(max_length=264)
    points = models.IntegerField(default=0)
    scored = models.IntegerField(default=0)
    conceded = models.IntegerField(default=0)
    difference = models.IntegerField(default=0)
    wins = models.IntegerField(default=0)
    loses = models.IntegerField(default=0)
    draws = models.IntegerField(default=0)
    strength = models.IntegerField(default=2000)
    image = models.ImageField(upload_to='upload/')
    country = models.CharField(max_length=264, default='()')
    def __str__(self):
        return self.name
class Gibraltar(models.Model):
    name = models.CharField(max_length=264)
    points = models.IntegerField(default=0)
    scored = models.IntegerField(default=0)
    conceded = models.IntegerField(default=0)
    difference = models.IntegerField(default=0)
    wins = models.IntegerField(default=0)
    loses = models.IntegerField(default=0)
    draws = models.IntegerField(default=0)
    strength = models.IntegerField(default=2000)
    image = models.ImageField(upload_to='upload/')
    country = models.CharField(max_length=264, default='()')
    def __str__(self):
        return self.name
class Czarnogora(models.Model):
    name = models.CharField(max_length=264)
    points = models.IntegerField(default=0)
    scored = models.IntegerField(default=0)
    conceded = models.IntegerField(default=0)
    difference = models.IntegerField(default=0)
    wins = models.IntegerField(default=0)
    loses = models.IntegerField(default=0)
    draws = models.IntegerField(default=0)
    strength = models.IntegerField(default=2000)
    image = models.ImageField(upload_to='upload/')
    country = models.CharField(max_length=264, default='()')
    def __str__(self):
        return self.name
class Estonia(models.Model):
    name = models.CharField(max_length=264)
    points = models.IntegerField(default=0)
    scored = models.IntegerField(default=0)
    conceded = models.IntegerField(default=0)
    difference = models.IntegerField(default=0)
    wins = models.IntegerField(default=0)
    loses = models.IntegerField(default=0)
    draws = models.IntegerField(default=0)
    strength = models.IntegerField(default=2000)
    image = models.ImageField(upload_to='upload/')
    country = models.CharField(max_length=264, default='()')
    def __str__(self):
        return self.name
class Kosowo(models.Model):
    name = models.CharField(max_length=264)
    points = models.IntegerField(default=0)
    scored = models.IntegerField(default=0)
    conceded = models.IntegerField(default=0)
    difference = models.IntegerField(default=0)
    wins = models.IntegerField(default=0)
    loses = models.IntegerField(default=0)
    draws = models.IntegerField(default=0)
    strength = models.IntegerField(default=2000)
    image = models.ImageField(upload_to='upload/')
    country = models.CharField(max_length=264, default='()')
    def __str__(self):
        return self.name
class Wyspy_Owcze(models.Model):
    name = models.CharField(max_length=264)
    points = models.IntegerField(default=0)
    scored = models.IntegerField(default=0)
    conceded = models.IntegerField(default=0)
    difference = models.IntegerField(default=0)
    wins = models.IntegerField(default=0)
    loses = models.IntegerField(default=0)
    draws = models.IntegerField(default=0)
    strength = models.IntegerField(default=2000)
    image = models.ImageField(upload_to='upload/')
    country = models.CharField(max_length=264, default='()')
    def __str__(self):
        return self.name
class Andora(models.Model):
    name = models.CharField(max_length=264)
    points = models.IntegerField(default=0)
    scored = models.IntegerField(default=0)
    conceded = models.IntegerField(default=0)
    difference = models.IntegerField(default=0)
    wins = models.IntegerField(default=0)
    loses = models.IntegerField(default=0)
    draws = models.IntegerField(default=0)
    strength = models.IntegerField(default=2000)
    image = models.ImageField(upload_to='upload/')
    country = models.CharField(max_length=264, default='()')
    def __str__(self):
        return self.name
class San_Marino(models.Model):
    name = models.CharField(max_length=264)
    points = models.IntegerField(default=0)
    scored = models.IntegerField(default=0)
    conceded = models.IntegerField(default=0)
    difference = models.IntegerField(default=0)
    wins = models.IntegerField(default=0)
    loses = models.IntegerField(default=0)
    draws = models.IntegerField(default=0)
    strength = models.IntegerField(default=2000)
    image = models.ImageField(upload_to='upload/')
    country = models.CharField(max_length=264, default='()')
    def __str__(self):
        return self.name



class Elim_LM_1(models.Model):
    name = models.CharField(max_length=264)
    strength = models.IntegerField(default=2000)
    image = models.ImageField(upload_to='upload/')
    last_scored = models.CharField(max_length=10,blank=True,default='')
    country = models.CharField(max_length=264, default='()')

    def __str__(self):
        return self.name
class Elim_LM_2(models.Model):
    name = models.CharField(max_length=264)
    strength = models.IntegerField(default=2000)
    image = models.ImageField(upload_to='upload/')
    last_scored = models.CharField(max_length=10,blank=True,default='')
    country = models.CharField(max_length=264, default='()')

    def __str__(self):
        return self.name
class Elim_LM_3(models.Model):
    name = models.CharField(max_length=264)
    strength = models.IntegerField(default=2000)
    image = models.ImageField(upload_to='upload/')
    last_scored = models.CharField(max_length=10,blank=True,default='')
    country = models.CharField(max_length=264, default='()')

    def __str__(self):
        return self.name
class Elim_LM_4(models.Model):
    name = models.CharField(max_length=264)
    strength = models.IntegerField(default=2000)
    image = models.ImageField(upload_to='upload/')
    last_scored = models.CharField(max_length=10,blank=True,default='')
    country = models.CharField(max_length=264, default='()')

    def __str__(self):
        return self.name

class Elim_LE_3(models.Model):
    name = models.CharField(max_length=264)
    strength = models.IntegerField(default=2000)
    image = models.ImageField(upload_to='upload/')
    last_scored = models.CharField(max_length=10,blank=True,default='')
    country = models.CharField(max_length=264, default='()')

    def __str__(self):
        return self.name
class Elim_LE_4(models.Model):
    name = models.CharField(max_length=264)
    strength = models.IntegerField(default=2000)
    image = models.ImageField(upload_to='upload/')
    last_scored = models.CharField(max_length=10,blank=True,default='')
    country = models.CharField(max_length=264, default='()')

    def __str__(self):
        return self.name

class Elim_ECL_1(models.Model):
    name = models.CharField(max_length=264)
    strength = models.IntegerField(default=2000)
    image = models.ImageField(upload_to='upload/')
    last_scored = models.CharField(max_length=10,blank=True,default='')
    country = models.CharField(max_length=264, default='()')

    def __str__(self):
        return self.name
class Elim_ECL_2(models.Model):
    name = models.CharField(max_length=264)
    strength = models.IntegerField(default=2000)
    image = models.ImageField(upload_to='upload/')
    last_scored = models.CharField(max_length=10,blank=True,default='')
    country = models.CharField(max_length=264, default='()')

    def __str__(self):
        return self.name
class Elim_ECL_3(models.Model):
    name = models.CharField(max_length=264)
    strength = models.IntegerField(default=2000)
    image = models.ImageField(upload_to='upload/')
    last_scored = models.CharField(max_length=10,blank=True,default='')
    country = models.CharField(max_length=264, default='()')

    def __str__(self):
        return self.name
class Elim_ECL_4(models.Model):
    name = models.CharField(max_length=264)
    strength = models.IntegerField(default=2000)
    image = models.ImageField(upload_to='upload/')
    last_scored = models.CharField(max_length=10,blank=True,default='')
    country = models.CharField(max_length=264, default='()')

    def __str__(self):
        return self.name

class LM_group(models.Model):
    name = models.CharField(max_length=264)
    points = models.IntegerField(default=0)
    scored = models.IntegerField(default=0)
    conceded = models.IntegerField(default=0)
    wins = models.IntegerField(default=0)
    loses = models.IntegerField(default=0)
    draws = models.IntegerField(default=0)
    strength = models.IntegerField(default=2000)
    image = models.ImageField(upload_to='upload/')
    country = models.CharField(max_length=264, default='()')
    def __str__(self):
        return self.name
class LE_group(models.Model):
    name = models.CharField(max_length=264)
    points = models.IntegerField(default=0)
    scored = models.IntegerField(default=0)
    conceded = models.IntegerField(default=0)
    wins = models.IntegerField(default=0)
    loses = models.IntegerField(default=0)
    draws = models.IntegerField(default=0)
    strength = models.IntegerField(default=2000)
    image = models.ImageField(upload_to='upload/')
    country = models.CharField(max_length=264, default='()')
    def __str__(self):
        return self.name
class ECL_group(models.Model):
    name = models.CharField(max_length=264)
    points = models.IntegerField(default=0)
    scored = models.IntegerField(default=0)
    conceded = models.IntegerField(default=0)
    wins = models.IntegerField(default=0)
    loses = models.IntegerField(default=0)
    draws = models.IntegerField(default=0)
    strength = models.IntegerField(default=2000)
    image = models.ImageField(upload_to='upload/')
    country = models.CharField(max_length=264, default='()')
    def __str__(self):
        return self.name


class LM_1_8(models.Model):
    name = models.CharField(max_length=264)
    strength = models.IntegerField(default=2000)
    image = models.ImageField(upload_to='upload/')
    last_scored = models.CharField(max_length=10,blank=True,default='')
    last_scored_2 = models.CharField(max_length=10,blank=True,default='')
    country = models.CharField(max_length=264, default='()')

    def __str__(self):
        return self.name
class LM_cwiercfinal(models.Model):
    name = models.CharField(max_length=264)
    strength = models.IntegerField(default=2000)
    image = models.ImageField(upload_to='upload/')
    last_scored = models.CharField(max_length=10,blank=True,default='')
    last_scored_2 = models.CharField(max_length=10,blank=True,default='')
    country = models.CharField(max_length=264, default='()')

    def __str__(self):
        return self.name
class LM_polfinal(models.Model):
    name = models.CharField(max_length=264)
    strength = models.IntegerField(default=2000)
    image = models.ImageField(upload_to='upload/')
    last_scored = models.CharField(max_length=10,blank=True,default='')
    last_scored_2 = models.CharField(max_length=10,blank=True,default='')
    country = models.CharField(max_length=264, default='()')

    def __str__(self):
        return self.name
class LM_final(models.Model):
    name = models.CharField(max_length=264)
    strength = models.IntegerField(default=2000)
    image = models.ImageField(upload_to='upload/')
    last_scored = models.CharField(max_length=10,blank=True,default='')
    country = models.CharField(max_length=264, default='()')

    def __str__(self):
        return self.name
class LM_winner(models.Model):
    name = models.CharField(max_length=264)
    strength = models.IntegerField(default=2000)
    image = models.ImageField(upload_to='upload/')
    last_scored = models.CharField(max_length=10,blank=True,default='')
    country = models.CharField(max_length=264, default='()')

    def __str__(self):
        return self.name

class LE_1_8(models.Model):
    name = models.CharField(max_length=264)
    strength = models.IntegerField(default=2000)
    image = models.ImageField(upload_to='upload/')
    last_scored = models.CharField(max_length=10,blank=True,default='')
    last_scored_2 = models.CharField(max_length=10,blank=True,default='')
    country = models.CharField(max_length=264, default='()')

    def __str__(self):
        return self.name
class LE_1_16(models.Model):
    name = models.CharField(max_length=264)
    strength = models.IntegerField(default=2000)
    image = models.ImageField(upload_to='upload/')
    last_scored = models.CharField(max_length=10,blank=True,default='')
    last_scored_2 = models.CharField(max_length=10,blank=True,default='')
    country = models.CharField(max_length=264, default='()')

    def __str__(self):
        return self.name
class LE_cwiercfinal(models.Model):
    name = models.CharField(max_length=264)
    strength = models.IntegerField(default=2000)
    image = models.ImageField(upload_to='upload/')
    last_scored = models.CharField(max_length=10,blank=True,default='')
    last_scored_2 = models.CharField(max_length=10,blank=True,default='')
    country = models.CharField(max_length=264, default='()')

    def __str__(self):
        return self.name
class LE_polfinal(models.Model):
    name = models.CharField(max_length=264)
    strength = models.IntegerField(default=2000)
    image = models.ImageField(upload_to='upload/')
    last_scored = models.CharField(max_length=10,blank=True,default='')
    last_scored_2 = models.CharField(max_length=10,blank=True,default='')
    country = models.CharField(max_length=264, default='()')

    def __str__(self):
        return self.name
class LE_final(models.Model):
    name = models.CharField(max_length=264)
    strength = models.IntegerField(default=2000)
    image = models.ImageField(upload_to='upload/')
    last_scored = models.CharField(max_length=10,blank=True,default='')
    country = models.CharField(max_length=264, default='()')

    def __str__(self):
        return self.name
class LE_winner(models.Model):
    name = models.CharField(max_length=264)
    strength = models.IntegerField(default=2000)
    image = models.ImageField(upload_to='upload/')
    last_scored = models.CharField(max_length=10,blank=True,default='')
    country = models.CharField(max_length=264, default='()')

    def __str__(self):
        return self.name

class ECL_1_8(models.Model):
    name = models.CharField(max_length=264)
    strength = models.IntegerField(default=2000)
    image = models.ImageField(upload_to='upload/')
    last_scored = models.CharField(max_length=10,blank=True,default='')
    last_scored_2 = models.CharField(max_length=10,blank=True,default='')
    country = models.CharField(max_length=264, default='()')

    def __str__(self):
        return self.name
class ECL_1_16(models.Model):
    name = models.CharField(max_length=264)
    strength = models.IntegerField(default=2000)
    image = models.ImageField(upload_to='upload/')
    last_scored = models.CharField(max_length=10,blank=True,default='')
    last_scored_2 = models.CharField(max_length=10,blank=True,default='')
    country = models.CharField(max_length=264, default='()')

    def __str__(self):
        return self.name
class ECL_cwiercfinal(models.Model):
    name = models.CharField(max_length=264)
    strength = models.IntegerField(default=2000)
    image = models.ImageField(upload_to='upload/')
    last_scored = models.CharField(max_length=10,blank=True,default='')
    last_scored_2 = models.CharField(max_length=10,blank=True,default='')
    country = models.CharField(max_length=264, default='()')

    def __str__(self):
        return self.name
class ECL_polfinal(models.Model):
    name = models.CharField(max_length=264)
    strength = models.IntegerField(default=2000)
    image = models.ImageField(upload_to='upload/')
    last_scored = models.CharField(max_length=10,blank=True,default='')
    last_scored_2 = models.CharField(max_length=10,blank=True,default='')
    country = models.CharField(max_length=264, default='()')

    def __str__(self):
        return self.name
class ECL_final(models.Model):
    name = models.CharField(max_length=264)
    strength = models.IntegerField(default=2000)
    image = models.ImageField(upload_to='upload/')
    last_scored = models.CharField(max_length=10,blank=True,default='')
    country = models.CharField(max_length=264, default='()')

    def __str__(self):
        return self.name
class ECL_winner(models.Model):
    name = models.CharField(max_length=264)
    strength = models.IntegerField(default=2000)
    image = models.ImageField(upload_to='upload/')
    last_scored = models.CharField(max_length=10,blank=True,default='')
    country = models.CharField(max_length=264, default='()')

    def __str__(self):
        return self.name

class LM_gallery(models.Model):
    name = models.CharField(max_length=264)
    image = models.ImageField(upload_to='upload/')
    country = models.CharField(max_length=264, default='()')

    def __str__(self):
        return self.name
class LE_gallery(models.Model):
    name = models.CharField(max_length=264)
    image = models.ImageField(upload_to='upload/')
    country = models.CharField(max_length=264, default='()')

    def __str__(self):
        return self.name
class ECL_gallery(models.Model):
    name = models.CharField(max_length=264)
    image = models.ImageField(upload_to='upload/')
    country = models.CharField(max_length=264, default='()')

    def __str__(self):
        return self.name
class POL_gallery(models.Model):
    name = models.CharField(max_length=264)
    image = models.ImageField(upload_to='upload/')

    def __str__(self):
        return self.name
class PP_gallery(models.Model):
    name = models.CharField(max_length=264)
    image = models.ImageField(upload_to='upload/')

    def __str__(self):
        return self.name
