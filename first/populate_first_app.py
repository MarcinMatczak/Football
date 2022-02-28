import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','first.settings')

import django
django.setup()

#FAKE POP SCRIPT
import random
from first_app.models import (Ekstraklasa, Pierwsza_Liga, Druga_Liga, Hiszpania, Anglia, Wlochy, Niemcy, Francja,Portugalia,Rosja,
Belgia,Ukraina,Holandia,Turcja,Austria,Dania,Szkocja,Czechy,Cypr,Szwajcaria,Grecja,Serbia,Chorwacja,Szwecja,Norwegia,Izrael,
Kazachstan,Bialorus,Azerbejdzan,Bulgaria,Rumunia,Slowacja,Liechtenstein,Slowenia, Wegry,Luxembourg,Litwa,Armenia,Lotwa,Albania,
Macedonia,Bosnia,Moldawia,Irlandia,Finlandia,Gruzja, Malta, Islandia, Walia, Irlandia_Pln, Gibraltar,Czarnogora,Estonia, Kosowo,
Wyspy_Owcze,Andora,San_Marino,     Elim_LM_1,Elim_LM_2,Elim_LM_3,Elim_LM_4,Elim_LE_3,Elim_LE_4, Elim_ECL_1,Elim_ECL_2,Elim_ECL_3,Elim_ECL_4,
LM_group,LE_group,ECL_group,    LM_1_8,LM_cwiercfinal,LM_polfinal,LM_final,LM_winner,LE_1_16,LE_1_8,LE_cwiercfinal,LE_polfinal,LE_final,LE_winner,
ECL_1_16,ECL_1_8,ECL_cwiercfinal,ECL_polfinal,ECL_final,ECL_winner)
from faker import Faker

fakegen = Faker()
topics = ['Search','Social','Marketplace','News','Games']
teams = ['Gornik','Piast','PBB','Stal','Pogon','Legia','Rakow','Lechia','Zaglebie','Lech','Slask','Warta','WislaK','Jagiellonia','WislaP','Cracovia']
ligi = ['Ekstraklasa','Laliga','Bundes']
def add_topic():
    t = Topic.objects.get_or_create(top_name = random.choice(topics))[0]
    t.save()
    return t
i = 0
def add_team():
    global i
    t = Team.objects.get_or_create(name = teams[i],points = 0, scored = 0, conceded = 0)[0]

    i = i+1
    t.save()
    return t
def populate(N=5):
    team16 = []
    nazwae = ""
    nazwap = ""
    for entry in range(N):
        #team16.append(add_team())
    #    top = add_topic()
    #    fake_url = fakegen.url()
        #fake_date = fakegen.date()
    #    fake_name = fakegen.company()
    #    webpg = Webpage.objects.get_or_create(topic=top,url=fake_url,name=fake_name)[0]
    #    acc_rec = AccessRecord.objects.get_or_create(name=webpg,date=fake_date)[0]
        Ekstraklasa.objects.all().update(country='(POL)')
        Pierwsza_Liga.objects.all().update(country='(POL)')
        Druga_Liga.objects.all().update(country='(POL)')
        Niemcy.objects.all().update(country='(GER)')
        Wlochy.objects.all().update(country='(ITA)')
        Hiszpania.objects.all().update(country='(ESP)')
        Francja.objects.all().update(country='(FRA)')
        Anglia.objects.all().update(country='(ENG)')
        Portugalia.objects.all().update(country='(POR)')
        Rosja.objects.all().update(country='(RUS)')
        Belgia.objects.all().update(country='(BEL)')
        Ukraina.objects.all().update(country='(UKR)')
        Holandia.objects.all().update(country='(NED)')
        Turcja.objects.all().update(country='(TUR)')
        Austria.objects.all().update(country='(AUT)')
        Dania.objects.all().update(country='(DEN)')
        Szkocja.objects.all().update(country='(SCO)')
        Czechy.objects.all().update(country='(CZE)')
        Cypr.objects.all().update(country='(CYP)')
        Szwajcaria.objects.all().update(country='(SUI)')
        Grecja.objects.all().update(country='(GRE)')
        Serbia.objects.all().update(country='(SRB)')
        Chorwacja.objects.all().update(country='(CRO)')
        Szwecja.objects.all().update(country='(SWE)')
        Norwegia.objects.all().update(country='(NOR)')
        Izrael.objects.all().update(country='(ISR)')
        Kazachstan.objects.all().update(country='(KAZ)')
        Bialorus.objects.all().update(country='(BLR)')
        Azerbejdzan.objects.all().update(country='(AZE)')
        Bulgaria.objects.all().update(country='(BUL)')
        Rumunia.objects.all().update(country='(ROU)')
        Slowacja.objects.all().update(country='(SVK)')
        Slowenia.objects.all().update(country='(SVN)')
        Wegry.objects.all().update(country='(HUN)')
        Luxembourg.objects.all().update(country='(LUX)')
        Litwa.objects.all().update(country='(LTU)')
        Armenia.objects.all().update(country='(ARM)')
        Lotwa.objects.all().update(country='(LAT)')
        Albania.objects.all().update(country='(ALB)')
        Macedonia.objects.all().update(country='(MKD)')
        Bosnia.objects.all().update(country='(BIH)')
        Moldawia.objects.all().update(country='(MDA)')
        Finlandia.objects.all().update(country='(FIN)')
        Irlandia.objects.all().update(country='(IRL)')
        Gruzja.objects.all().update(country='(GEO)')
        Malta.objects.all().update(country='(MLT)')
        Islandia.objects.all().update(country='(ISL)')
        Walia.objects.all().update(country='(WAL)')
        Irlandia_Pln.objects.all().update(country='(NIR)')
        Gibraltar.objects.all().update(country='(GBR)')
        Czarnogora.objects.all().update(country='(MNE)')
        Estonia.objects.all().update(country='(EST)')
        Kosowo.objects.all().update(country='(KSW)')
        Wyspy_Owcze.objects.all().update(country='(FRO)')
        Andora.objects.all().update(country='(AND)')
        San_Marino.objects.all().update(country='(SMR)')

if __name__ == '__main__':
    print("populating script!")
    populate(1)
    print("populating complete!")
