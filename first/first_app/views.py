from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import F
from first_app.models import (Ekstraklasa, Pierwsza_Liga, Druga_Liga, Hiszpania, Anglia, Wlochy, Niemcy, Francja,Portugalia,Rosja,
Belgia,Ukraina,Holandia,Turcja,Austria,Dania,Szkocja,Czechy,Cypr,Szwajcaria,Grecja,Serbia,Chorwacja,Szwecja,Norwegia,Izrael,
Kazachstan,Bialorus,Azerbejdzan,Bulgaria,Rumunia,Slowacja,Liechtenstein,Slowenia, Wegry,Luxembourg,Litwa,Armenia,Lotwa,Albania,
Macedonia,Bosnia,Moldawia,Irlandia,Finlandia,Gruzja, Malta, Islandia, Walia, Irlandia_Pln, Gibraltar,Czarnogora,Estonia, Kosowo,
Wyspy_Owcze,Andora,San_Marino,     Elim_LM_1,Elim_LM_2,Elim_LM_3,Elim_LM_4,Elim_LE_3,Elim_LE_4, Elim_ECL_1,Elim_ECL_2,Elim_ECL_3,Elim_ECL_4,
LM_group,LE_group,ECL_group,    LM_1_8,LM_cwiercfinal,LM_polfinal,LM_final,LM_winner,LE_1_16,LE_1_8,LE_cwiercfinal,LE_polfinal,LE_final,LE_winner,
ECL_1_16,ECL_1_8,ECL_cwiercfinal,ECL_polfinal,ECL_final,ECL_winner, LM_gallery,LE_gallery,ECL_gallery,POL_gallery,PP_gallery)
import random

def index(request):
    ekst_list = Ekstraklasa.objects.order_by('-points','-difference','-scored')
    pliga_list = Pierwsza_Liga.objects.order_by('-points','-difference','-scored')
    dliga_list = Druga_Liga.objects.order_by('-points','-difference','-scored')
    hiszpania_list = Hiszpania.objects.order_by('-points','-difference','-scored')
    francja_list = Francja.objects.order_by('-points','-difference','-scored')
    anglia_list = Anglia.objects.order_by('-points','-difference','-scored')
    niemcy_list = Niemcy.objects.order_by('-points','-difference','-scored')
    wlochy_list = Wlochy.objects.order_by('-points','-difference','-scored')
    portugalia_list = Portugalia.objects.order_by('-points','-difference','-scored')
    rosja_list = Rosja.objects.order_by('-points','-difference','-scored')
    belgia_list = Belgia.objects.order_by('-points','-difference','-scored')
    ukraina_list = Ukraina.objects.order_by('-points','-difference','-scored')
    holandia_list = Holandia.objects.order_by('-points','-difference','-scored')
    turcja_list = Turcja.objects.order_by('-points','-difference','-scored')
    austria_list = Austria.objects.order_by('-points','-difference','-scored')
    dania_list = Dania.objects.order_by('-points','-difference','-scored')
    szkocja_list = Szkocja.objects.order_by('-points','-difference','-scored')
    czechy_list = Czechy.objects.order_by('-points','-difference','-scored')
    cypr_list = Cypr.objects.order_by('-points','-difference','-scored')
    szwajcaria_list = Szwajcaria.objects.order_by('-points','-difference','-scored')
    grecja_list = Grecja.objects.order_by('-points','-difference','-scored')
    serbia_list = Serbia.objects.order_by('-points','-difference','-scored')
    chorwacja_list = Chorwacja.objects.order_by('-points','-difference','-scored')
    szwecja_list = Szwecja.objects.order_by('-points','-difference','-scored')
    norwegia_list = Norwegia.objects.order_by('-points','-difference','-scored')
    izrael_list = Izrael.objects.order_by('-points','-difference','-scored')
    kazachstan_list = Kazachstan.objects.order_by('-points','-difference','-scored')
    bialorus_list = Bialorus.objects.order_by('-points','-difference','-scored')
    azerbejdzan_list = Azerbejdzan.objects.order_by('-points','-difference','-scored')
    bulgaria_list = Bulgaria.objects.order_by('-points','-difference','-scored')
    rumunia_list = Rumunia.objects.order_by('-points','-difference','-scored')
    slowacja_list = Slowacja.objects.order_by('-points','-difference','-scored')
    liechtenstein_list = Liechtenstein.objects.order_by('-points','-difference','-scored')
    slowenia_list = Slowenia.objects.order_by('-points','-difference','-scored')
    wegry_list = Wegry.objects.order_by('-points','-difference','-scored')
    luxembourg_list = Luxembourg.objects.order_by('-points','-difference','-scored')
    litwa_list = Litwa.objects.order_by('-points','-difference','-scored')
    armenia_list = Armenia.objects.order_by('-points','-difference','-scored')
    lotwa_list = Lotwa.objects.order_by('-points','-difference','-scored')
    albania_list = Albania.objects.order_by('-points','-difference','-scored')
    macedonia_list = Macedonia.objects.order_by('-points','-difference','-scored')
    bosnia_list = Bosnia.objects.order_by('-points','-difference','-scored')
    moldawia_list = Moldawia.objects.order_by('-points','-difference','-scored')
    finlandia_list = Finlandia.objects.order_by('-points','-difference','-scored')
    irlandia_list = Irlandia.objects.order_by('-points','-difference','-scored')
    gruzja_list = Gruzja.objects.order_by('-points','-difference','-scored')
    malta_list = Malta.objects.order_by('-points','-difference','-scored')
    islandia_list = Islandia.objects.order_by('-points','-difference','-scored')
    walia_list = Walia.objects.order_by('-points','-difference','-scored')
    irlandia_Pln_list = Irlandia_Pln.objects.order_by('-points','-difference','-scored')
    gibraltar_list = Gibraltar.objects.order_by('-points','-difference','-scored')
    czarnogora_list = Czarnogora.objects.order_by('-points','-difference','-scored')
    estonia_list = Estonia.objects.order_by('-points','-difference','-scored')
    kosowo_list = Kosowo.objects.order_by('-points','-difference','-scored')
    wyspy_Owcze_list = Wyspy_Owcze.objects.order_by('-points','-difference','-scored')
    andora_list = Andora.objects.order_by('-points','-difference','-scored')
    san_Marino_list = San_Marino.objects.order_by('-points','-difference','-scored')

    all_dict = {'ekst_records':ekst_list,'pier_liga_records':pliga_list,'drug_liga_records':dliga_list,'hiszpania_records':hiszpania_list,'francja_records':francja_list,'anglia_records':anglia_list,
    'niemcy_records':niemcy_list,'wlochy_records':wlochy_list,'portugalia_records':portugalia_list,
    'rosja_records':rosja_list,
    'belgia_records':belgia_list,
    'ukraina_records':ukraina_list,
    'holandia_records':holandia_list,
    'turcja_records':turcja_list,
    'austria_records':austria_list,
    'dania_records':dania_list,
    'szkocja_records':szkocja_list,
    'czechy_records':czechy_list,
    'cypr_records':cypr_list,
    'szwajcaria_records':szwajcaria_list,
    'grecja_records':grecja_list,
    'serbia_records':serbia_list,
    'chorwacja_records':chorwacja_list,
    'szwecja_records':szwecja_list,
    'norwegia_records':norwegia_list,
    'izrael_records':izrael_list,
    'kazachstan_records':kazachstan_list,
    'bialorus_records':bialorus_list,
    'azerbejdzan_records':azerbejdzan_list,
    'bulgaria_records':bulgaria_list,
    'rumunia_records':rumunia_list,
    'slowacja_records':slowacja_list,
    'liechtenstein_records':liechtenstein_list,
    'slowenia_records':slowenia_list,
    'wegry_records':wegry_list,
    'luxembourg_records':luxembourg_list,
    'litwa_records':litwa_list,
    'armenia_records':armenia_list,
    'lotwa_records':lotwa_list,
    'albania_records':albania_list,
    'macedonia_records':macedonia_list,
    'bosnia_records':bosnia_list,
    'moldawia_records':moldawia_list,
    'finlandia_records':finlandia_list,
    'irlandia_records':irlandia_list,
    'gruzja_records':gruzja_list,
    'malta_records':malta_list,
    'islandia_records':islandia_list,
    'walia_records':walia_list,
    'irlandia_Pln_records':irlandia_Pln_list,
    'gibraltar_records':gibraltar_list,
    'czarnogora_records':czarnogora_list,
    'estonia_records':estonia_list,
    'kosowo_records':kosowo_list,
    'wyspy_Owcze_records':wyspy_Owcze_list,
    'andora_records':andora_list,
    'san_Marino_records':san_Marino_list,}
    return render(request,'first_app/index.html',context=all_dict)
def index_season(request):
    Ekstraklasa.objects.all().update(points=0,scored=0, conceded=0,wins = 0,loses=0,draws=0,difference=0)
    Pierwsza_Liga.objects.all().update(points=0,scored=0, conceded=0,wins = 0,loses=0,draws=0,difference=0)
    Druga_Liga.objects.all().update(points=0,scored=0, conceded=0,wins = 0,loses=0,draws=0,difference=0)
    Niemcy.objects.all().update(points=0,scored=0, conceded=0,wins = 0,loses=0,draws=0,difference=0)
    Wlochy.objects.all().update(points=0,scored=0, conceded=0,wins = 0,loses=0,draws=0,difference=0)
    Hiszpania.objects.all().update(points=0,scored=0, conceded=0,wins = 0,loses=0,draws=0,difference=0)
    Francja.objects.all().update(points=0,scored=0, conceded=0,wins = 0,loses=0,draws=0,difference=0)
    Anglia.objects.all().update(points=0,scored=0, conceded=0,wins = 0,loses=0,draws=0,difference=0)
    Portugalia.objects.all().update(points=0,scored=0, conceded=0,wins = 0,loses=0,draws=0,difference=0)
    Rosja.objects.all().update(points=0,scored=0, conceded=0,wins = 0,loses=0,draws=0,difference=0)
    Belgia.objects.all().update(points=0,scored=0, conceded=0,wins = 0,loses=0,draws=0,difference=0)
    Ukraina.objects.all().update(points=0,scored=0, conceded=0,wins = 0,loses=0,draws=0,difference=0)
    Holandia.objects.all().update(points=0,scored=0, conceded=0,wins = 0,loses=0,draws=0,difference=0)
    Turcja.objects.all().update(points=0,scored=0, conceded=0,wins = 0,loses=0,draws=0,difference=0)
    Austria.objects.all().update(points=0,scored=0, conceded=0,wins = 0,loses=0,draws=0,difference=0)
    Dania.objects.all().update(points=0,scored=0, conceded=0,wins = 0,loses=0,draws=0,difference=0)
    Szkocja.objects.all().update(points=0,scored=0, conceded=0,wins = 0,loses=0,draws=0,difference=0)
    Czechy.objects.all().update(points=0,scored=0, conceded=0,wins = 0,loses=0,draws=0,difference=0)
    Cypr.objects.all().update(points=0,scored=0, conceded=0,wins = 0,loses=0,draws=0,difference=0)
    Szwajcaria.objects.all().update(points=0,scored=0, conceded=0,wins = 0,loses=0,draws=0,difference=0)
    Grecja.objects.all().update(points=0,scored=0, conceded=0,wins = 0,loses=0,draws=0,difference=0)
    Serbia.objects.all().update(points=0,scored=0, conceded=0,wins = 0,loses=0,draws=0,difference=0)
    Chorwacja.objects.all().update(points=0,scored=0, conceded=0,wins = 0,loses=0,draws=0,difference=0)
    Szwecja.objects.all().update(points=0,scored=0, conceded=0,wins = 0,loses=0,draws=0,difference=0)
    Norwegia.objects.all().update(points=0,scored=0, conceded=0,wins = 0,loses=0,draws=0,difference=0)
    Izrael.objects.all().update(points=0,scored=0, conceded=0,wins = 0,loses=0,draws=0,difference=0)
    Kazachstan.objects.all().update(points=0,scored=0, conceded=0,wins = 0,loses=0,draws=0,difference=0)
    Bialorus.objects.all().update(points=0,scored=0, conceded=0,wins = 0,loses=0,draws=0,difference=0)
    Azerbejdzan.objects.all().update(points=0,scored=0, conceded=0,wins = 0,loses=0,draws=0,difference=0)
    Bulgaria.objects.all().update(points=0,scored=0, conceded=0,wins = 0,loses=0,draws=0,difference=0)
    Rumunia.objects.all().update(points=0,scored=0, conceded=0,wins = 0,loses=0,draws=0,difference=0)
    Slowacja.objects.all().update(points=0,scored=0, conceded=0,wins = 0,loses=0,draws=0,difference=0)
    Slowenia.objects.all().update(points=0,scored=0, conceded=0,wins = 0,loses=0,draws=0,difference=0)
    Wegry.objects.all().update(points=0,scored=0, conceded=0,wins = 0,loses=0,draws=0,difference=0)
    Luxembourg.objects.all().update(points=0,scored=0, conceded=0,wins = 0,loses=0,draws=0,difference=0)
    Litwa.objects.all().update(points=0,scored=0, conceded=0,wins = 0,loses=0,draws=0,difference=0)
    Armenia.objects.all().update(points=0,scored=0, conceded=0,wins = 0,loses=0,draws=0,difference=0)
    Lotwa.objects.all().update(points=0,scored=0, conceded=0,wins = 0,loses=0,draws=0,difference=0)
    Albania.objects.all().update(points=0,scored=0, conceded=0,wins = 0,loses=0,draws=0,difference=0)
    Macedonia.objects.all().update(points=0,scored=0, conceded=0,wins = 0,loses=0,draws=0,difference=0)
    Bosnia.objects.all().update(points=0,scored=0, conceded=0,wins = 0,loses=0,draws=0,difference=0)
    Moldawia.objects.all().update(points=0,scored=0, conceded=0,wins = 0,loses=0,draws=0,difference=0)
    Finlandia.objects.all().update(points=0,scored=0, conceded=0,wins = 0,loses=0,draws=0,difference=0)
    Irlandia.objects.all().update(points=0,scored=0, conceded=0,wins = 0,loses=0,draws=0,difference=0)
    Gruzja.objects.all().update(points=0,scored=0, conceded=0,wins = 0,loses=0,draws=0,difference=0)
    Malta.objects.all().update(points=0,scored=0, conceded=0,wins = 0,loses=0,draws=0,difference=0)
    Islandia.objects.all().update(points=0,scored=0, conceded=0,wins = 0,loses=0,draws=0,difference=0)
    Walia.objects.all().update(points=0,scored=0, conceded=0,wins = 0,loses=0,draws=0,difference=0)
    Irlandia_Pln.objects.all().update(points=0,scored=0, conceded=0,wins = 0,loses=0,draws=0,difference=0)
    Gibraltar.objects.all().update(points=0,scored=0, conceded=0,wins = 0,loses=0,draws=0,difference=0)
    Czarnogora.objects.all().update(points=0,scored=0, conceded=0,wins = 0,loses=0,draws=0,difference=0)
    Estonia.objects.all().update(points=0,scored=0, conceded=0,wins = 0,loses=0,draws=0,difference=0)
    Kosowo.objects.all().update(points=0,scored=0, conceded=0,wins = 0,loses=0,draws=0,difference=0)
    Wyspy_Owcze.objects.all().update(points=0,scored=0, conceded=0,wins = 0,loses=0,draws=0,difference=0)
    Andora.objects.all().update(points=0,scored=0, conceded=0,wins = 0,loses=0,draws=0,difference=0)
    San_Marino.objects.all().update(points=0,scored=0, conceded=0,wins = 0,loses=0,draws=0,difference=0)
    ekst_list = list(Ekstraklasa.objects.all())
    pliga_list =list(Pierwsza_Liga.objects.all())
    dliga_list=list(Druga_Liga.objects.all())
    niemcy_list=list(Niemcy.objects.all())
    anglia_list = list(Anglia.objects.all())
    hiszpania_list =list(Hiszpania.objects.all())
    wlochy_list=list(Wlochy.objects.all())
    francja_list=list(Francja.objects.all())

    portugalia_list = list(Portugalia.objects.all())
    rosja_list = list(Rosja.objects.all())
    belgia_list = list(Belgia.objects.all())
    ukraina_list = list(Ukraina.objects.all())
    holandia_list = list(Holandia.objects.all())
    turcja_list = list(Turcja.objects.all())
    austria_list = list(Austria.objects.all())
    dania_list = list(Dania.objects.all())
    szkocja_list = list(Szkocja.objects.all())
    czechy_list = list(Czechy.objects.all())
    cypr_list = list(Cypr.objects.all())
    szwajcaria_list = list(Szwajcaria.objects.all())
    grecja_list = list(Grecja.objects.all())
    serbia_list = list(Serbia.objects.all())
    chorwacja_list = list(Chorwacja.objects.all())
    szwecja_list = list(Szwecja.objects.all())
    norwegia_list = list(Norwegia.objects.all())
    izrael_list = list(Izrael.objects.all())
    kazachstan_list = list(Kazachstan.objects.all())
    bialorus_list = list(Bialorus.objects.all())
    azerbejdzan_list = list(Azerbejdzan.objects.all())
    bulgaria_list = list(Bulgaria.objects.all())
    rumunia_list = list(Rumunia.objects.all())
    slowacja_list = list(Slowacja.objects.all())
    slowenia_list = list(Slowenia.objects.all())
    wegry_list = list(Wegry.objects.all())
    luxembourg_list = list(Luxembourg.objects.all())
    litwa_list = list(Litwa.objects.all())
    armenia_list = list(Armenia.objects.all())
    lotwa_list = list(Lotwa.objects.all())
    albania_list = list(Albania.objects.all())
    macedonia_list = list(Macedonia.objects.all())
    bosnia_list = list(Bosnia.objects.all())
    moldawia_list = list(Moldawia.objects.all())
    finlandia_list = list(Finlandia.objects.all())
    irlandia_list = list(Irlandia.objects.all())
    gruzja_list = list(Gruzja.objects.all())
    malta_list = list(Malta.objects.all())
    islandia_list = list(Islandia.objects.all())
    walia_list = list(Walia.objects.all())
    irlandia_Pln_list = list(Irlandia_Pln.objects.all())
    gibraltar_list = list(Gibraltar.objects.all())
    czarnogora_list = list(Czarnogora.objects.all())
    estonia_list = list(Estonia.objects.all())
    kosowo_list = list(Kosowo.objects.all())
    wyspy_Owcze_list = list(Wyspy_Owcze.objects.all())
    andora_list = list(Andora.objects.all())
    san_Marino_list = list(San_Marino.objects.all())

    def match(team1, team2):
        host_limit = team1.strength
        guest_limit = 10000 - team2.strength
        b1=0
        b2=0
        for i in range(10):
            los = random.randint(0, 10000)
            if los < host_limit:
                b1 = b1 + 1
            elif los > guest_limit:
                b2 = b2 + 1
        if b1 > b2:
            team1.points = team1.points + 3
            team1.wins = team1.wins + 1
            team2.loses = team2.loses + 1
        elif b2 > b1:
            team2.points = team2.points + 3
            team2.wins = team2.wins + 1
            team1.loses = team1.loses + 1
        else:
            team2.points = team2.points + 1
            team1.points = team1.points + 1
            team1.draws = team1.draws + 1
            team2.draws = team2.draws + 1
        team1.scored = team1.scored + b1
        team1.conceded = team1.conceded + b2
        team2.scored = team2.scored + b2
        team2.conceded = team2.conceded + b1
    def season8(clubs):
        for i in range(4):
            match(clubs[0],clubs[7])
            match(clubs[1],clubs[6])
            match(clubs[2],clubs[5])
            match(clubs[3],clubs[4])

            match(clubs[4],clubs[7])
            match(clubs[5],clubs[3])
            match(clubs[6],clubs[2])
            match(clubs[0],clubs[1])

            match(clubs[1],clubs[7])
            match(clubs[2],clubs[0])
            match(clubs[3],clubs[6])
            match(clubs[4],clubs[5])

            match(clubs[5],clubs[7])
            match(clubs[6],clubs[4])
            match(clubs[0],clubs[3])
            match(clubs[1],clubs[2])

            match(clubs[2],clubs[7])
            match(clubs[3],clubs[1])
            match(clubs[4],clubs[0])
            match(clubs[5],clubs[6])

            match(clubs[6],clubs[7])
            match(clubs[0],clubs[5])
            match(clubs[1],clubs[4])
            match(clubs[2],clubs[3])

            match(clubs[3],clubs[7])
            match(clubs[4],clubs[2])
            match(clubs[5],clubs[1])
            match(clubs[6],clubs[0])
            for cl in clubs:
                cl.difference = cl.scored - cl.conceded
                cl.save()
    def season10(clubs):
        for i in range(4):
            match(clubs[0],clubs[9])
            match(clubs[1],clubs[8])
            match(clubs[2],clubs[7])
            match(clubs[3],clubs[6])
            match(clubs[4],clubs[5])

            match(clubs[5],clubs[9])
            match(clubs[6],clubs[4])
            match(clubs[7],clubs[3])
            match(clubs[8],clubs[2])
            match(clubs[0],clubs[1])

            match(clubs[1],clubs[9])
            match(clubs[2],clubs[0])
            match(clubs[3],clubs[8])
            match(clubs[4],clubs[7])
            match(clubs[5],clubs[6])

            match(clubs[6],clubs[9])
            match(clubs[7],clubs[5])
            match(clubs[8],clubs[4])
            match(clubs[0],clubs[3])
            match(clubs[1],clubs[2])

            match(clubs[2],clubs[9])
            match(clubs[3],clubs[1])
            match(clubs[4],clubs[0])
            match(clubs[5],clubs[8])
            match(clubs[6],clubs[7])

            match(clubs[7],clubs[9])
            match(clubs[8],clubs[6])
            match(clubs[0],clubs[5])
            match(clubs[1],clubs[4])
            match(clubs[2],clubs[3])

            match(clubs[3],clubs[9])
            match(clubs[4],clubs[2])
            match(clubs[5],clubs[1])
            match(clubs[6],clubs[0])
            match(clubs[7],clubs[8])

            match(clubs[8],clubs[9])
            match(clubs[0],clubs[7])
            match(clubs[1],clubs[6])
            match(clubs[2],clubs[5])
            match(clubs[3],clubs[4])

            match(clubs[4],clubs[9])
            match(clubs[5],clubs[3])
            match(clubs[6],clubs[2])
            match(clubs[7],clubs[1])
            match(clubs[8],clubs[0])
            for cl in clubs:
                cl.difference = cl.scored - cl.conceded
                cl.save()
    def season12(clubs):
        for i in range(3):
            match(clubs[0],clubs[11])
            match(clubs[1],clubs[10])
            match(clubs[2],clubs[9])
            match(clubs[3],clubs[8])
            match(clubs[4],clubs[7])
            match(clubs[5],clubs[6])

            match(clubs[6],clubs[11])
            match(clubs[7],clubs[5])
            match(clubs[8],clubs[4])
            match(clubs[9],clubs[3])
            match(clubs[10],clubs[2])
            match(clubs[0],clubs[1])

            match(clubs[1],clubs[11])
            match(clubs[2],clubs[0])
            match(clubs[3],clubs[10])
            match(clubs[4],clubs[9])
            match(clubs[5],clubs[8])
            match(clubs[6],clubs[7])

            match(clubs[7],clubs[11])
            match(clubs[8],clubs[6])
            match(clubs[9],clubs[5])
            match(clubs[10],clubs[4])
            match(clubs[0],clubs[3])
            match(clubs[1],clubs[2])

            match(clubs[2],clubs[11])
            match(clubs[3],clubs[1])
            match(clubs[4],clubs[0])
            match(clubs[5],clubs[10])
            match(clubs[6],clubs[9])
            match(clubs[7],clubs[8])

            match(clubs[8],clubs[11])
            match(clubs[9],clubs[7])
            match(clubs[10],clubs[6])
            match(clubs[0],clubs[5])
            match(clubs[1],clubs[4])
            match(clubs[2],clubs[3])

            match(clubs[3],clubs[11])
            match(clubs[4],clubs[2])
            match(clubs[5],clubs[1])
            match(clubs[6],clubs[0])
            match(clubs[7],clubs[10])
            match(clubs[8],clubs[9])

            match(clubs[9],clubs[11])
            match(clubs[10],clubs[8])
            match(clubs[0],clubs[7])
            match(clubs[1],clubs[6])
            match(clubs[2],clubs[5])
            match(clubs[3],clubs[4])

            match(clubs[4],clubs[11])
            match(clubs[5],clubs[3])
            match(clubs[6],clubs[2])
            match(clubs[7],clubs[1])
            match(clubs[8],clubs[0])
            match(clubs[9],clubs[10])

            match(clubs[10],clubs[11])
            match(clubs[0],clubs[9])
            match(clubs[1],clubs[8])
            match(clubs[2],clubs[7])
            match(clubs[3],clubs[6])
            match(clubs[4],clubs[5])

            match(clubs[5],clubs[11])
            match(clubs[6],clubs[4])
            match(clubs[7],clubs[3])
            match(clubs[8],clubs[2])
            match(clubs[9],clubs[1])
            match(clubs[10],clubs[0])
        for cl in clubs:
            cl.difference = cl.scored - cl.conceded
            cl.save()
    def season14(clubs):
        for i in range(2):
            match(clubs[0],clubs[13])
            match(clubs[1],clubs[12])
            match(clubs[2],clubs[11])
            match(clubs[3],clubs[10])
            match(clubs[4],clubs[9])
            match(clubs[5],clubs[8])
            match(clubs[6],clubs[7])

            match(clubs[7],clubs[13])
            match(clubs[8],clubs[6])
            match(clubs[9],clubs[5])
            match(clubs[10],clubs[4])
            match(clubs[11],clubs[3])
            match(clubs[12],clubs[2])
            match(clubs[0],clubs[1])

            match(clubs[1],clubs[13])
            match(clubs[2],clubs[0])
            match(clubs[3],clubs[12])
            match(clubs[4],clubs[11])
            match(clubs[5],clubs[10])
            match(clubs[6],clubs[9])
            match(clubs[7],clubs[8])

            match(clubs[8],clubs[13])
            match(clubs[9],clubs[7])
            match(clubs[10],clubs[6])
            match(clubs[11],clubs[5])
            match(clubs[12],clubs[4])
            match(clubs[0],clubs[3])
            match(clubs[3],clubs[2])

            match(clubs[2],clubs[13])
            match(clubs[3],clubs[1])
            match(clubs[4],clubs[0])
            match(clubs[5],clubs[12])
            match(clubs[6],clubs[11])
            match(clubs[7],clubs[10])
            match(clubs[8],clubs[9])

            match(clubs[9],clubs[13])
            match(clubs[10],clubs[8])
            match(clubs[11],clubs[7])
            match(clubs[12],clubs[6])
            match(clubs[0],clubs[5])
            match(clubs[1],clubs[4])
            match(clubs[2],clubs[3])

            match(clubs[3],clubs[13])
            match(clubs[4],clubs[2])
            match(clubs[5],clubs[1])
            match(clubs[6],clubs[0])
            match(clubs[7],clubs[12])
            match(clubs[8],clubs[11])
            match(clubs[9],clubs[10])

            match(clubs[10],clubs[13])
            match(clubs[11],clubs[9])
            match(clubs[12],clubs[8])
            match(clubs[0],clubs[7])
            match(clubs[1],clubs[6])
            match(clubs[2],clubs[5])
            match(clubs[3],clubs[4])

            match(clubs[4],clubs[13])
            match(clubs[5],clubs[3])
            match(clubs[6],clubs[2])
            match(clubs[7],clubs[1])
            match(clubs[8],clubs[0])
            match(clubs[9],clubs[12])
            match(clubs[10],clubs[11])

            match(clubs[11],clubs[13])
            match(clubs[12],clubs[10])
            match(clubs[0],clubs[9])
            match(clubs[1],clubs[8])
            match(clubs[2],clubs[7])
            match(clubs[3],clubs[6])
            match(clubs[4],clubs[5])

            match(clubs[5],clubs[13])
            match(clubs[6],clubs[4])
            match(clubs[7],clubs[3])
            match(clubs[8],clubs[2])
            match(clubs[9],clubs[1])
            match(clubs[10],clubs[0])
            match(clubs[11],clubs[12])

            match(clubs[12],clubs[13])
            match(clubs[0],clubs[11])
            match(clubs[1],clubs[10])
            match(clubs[2],clubs[9])
            match(clubs[3],clubs[8])
            match(clubs[4],clubs[7])
            match(clubs[5],clubs[6])

            match(clubs[6],clubs[13])
            match(clubs[7],clubs[5])
            match(clubs[8],clubs[4])
            match(clubs[9],clubs[3])
            match(clubs[10],clubs[2])
            match(clubs[11],clubs[1])
            match(clubs[12],clubs[0])
        for cl in clubs:
            cl.difference = cl.scored - cl.conceded
            cl.save()
    def season16(clubs):
        for i in range(2):
            # 1.kolejka
            match(clubs[0],clubs[15])
            match(clubs[1],clubs[14])
            match(clubs[2],clubs[13])
            match(clubs[3],clubs[12])
            match(clubs[4],clubs[11])
            match(clubs[5],clubs[10])
            match(clubs[6],clubs[9])
            match(clubs[7],clubs[8])
            # 2.kolejka
            match(clubs[8],clubs[15])
            match(clubs[9],clubs[7])
            match(clubs[10],clubs[6])
            match(clubs[11],clubs[5])
            match(clubs[12],clubs[4])
            match(clubs[13],clubs[3])
            match(clubs[14],clubs[2])
            match(clubs[0],clubs[1])
            # 3.kolejka
            match(clubs[1],clubs[15])
            match(clubs[2],clubs[0])
            match(clubs[3],clubs[14])
            match(clubs[4],clubs[13])
            match(clubs[5],clubs[12])
            match(clubs[6],clubs[11])
            match(clubs[7],clubs[10])
            match(clubs[8],clubs[9])
            # 4.kolejka
            match(clubs[9],clubs[15])
            match(clubs[10],clubs[8])
            match(clubs[11],clubs[7])
            match(clubs[12],clubs[6])
            match(clubs[13],clubs[5])
            match(clubs[14],clubs[4])
            match(clubs[0],clubs[3])
            match(clubs[1],clubs[2])
            # 5.kolejka
            match(clubs[2],clubs[15])
            match(clubs[3],clubs[1])
            match(clubs[4],clubs[0])
            match(clubs[5],clubs[14])
            match(clubs[6],clubs[13])
            match(clubs[7],clubs[12])
            match(clubs[8],clubs[11])
            match(clubs[9],clubs[10])
            # 6.kolejka
            match(clubs[10],clubs[15])
            match(clubs[11],clubs[9])
            match(clubs[12],clubs[8])
            match(clubs[13],clubs[7])
            match(clubs[14],clubs[6])
            match(clubs[0],clubs[5])
            match(clubs[1],clubs[4])
            match(clubs[2],clubs[3])
            # 7.kolejka
            match(clubs[3],clubs[15])
            match(clubs[4],clubs[2])
            match(clubs[5],clubs[1])
            match(clubs[6],clubs[0])
            match(clubs[7],clubs[14])
            match(clubs[8],clubs[13])
            match(clubs[9],clubs[12])
            match(clubs[10],clubs[11])
            # 8.kolejka
            match(clubs[11],clubs[15])
            match(clubs[12],clubs[10])
            match(clubs[13],clubs[9])
            match(clubs[14],clubs[8])
            match(clubs[0],clubs[7])
            match(clubs[1],clubs[6])
            match(clubs[2],clubs[5])
            match(clubs[3],clubs[4])
            # 9.kolejka
            match(clubs[4],clubs[15])
            match(clubs[5],clubs[3])
            match(clubs[6],clubs[2])
            match(clubs[7],clubs[1])
            match(clubs[8],clubs[0])
            match(clubs[9],clubs[14])
            match(clubs[10],clubs[13])
            match(clubs[11],clubs[12])
            # 10.kolejka
            match(clubs[12],clubs[15])
            match(clubs[13],clubs[11])
            match(clubs[14],clubs[10])
            match(clubs[0],clubs[9])
            match(clubs[1],clubs[8])
            match(clubs[2],clubs[7])
            match(clubs[3],clubs[6])
            match(clubs[4],clubs[5])
            # 11.kolejka
            match(clubs[5],clubs[15])
            match(clubs[6],clubs[4])
            match(clubs[7],clubs[3])
            match(clubs[8],clubs[2])
            match(clubs[9],clubs[1])
            match(clubs[10],clubs[0])
            match(clubs[11],clubs[14])
            match(clubs[12],clubs[13])
            # 12.kolejka
            match(clubs[13],clubs[15])
            match(clubs[14],clubs[12])
            match(clubs[0],clubs[11])
            match(clubs[1],clubs[10])
            match(clubs[2],clubs[9])
            match(clubs[3],clubs[8])
            match(clubs[4],clubs[7])
            match(clubs[5],clubs[6])
            # 13.kolejka
            match(clubs[6],clubs[15])
            match(clubs[7],clubs[5])
            match(clubs[8],clubs[4])
            match(clubs[9],clubs[3])
            match(clubs[10],clubs[2])
            match(clubs[11],clubs[1])
            match(clubs[12],clubs[0])
            match(clubs[13],clubs[14])
            # 14.kolejka
            match(clubs[14],clubs[15])
            match(clubs[0],clubs[13])
            match(clubs[1],clubs[12])
            match(clubs[2],clubs[11])
            match(clubs[3],clubs[10])
            match(clubs[4],clubs[9])
            match(clubs[5],clubs[8])
            match(clubs[6],clubs[7])
            # 15.kolejka
            match(clubs[7],clubs[15])
            match(clubs[8],clubs[6])
            match(clubs[9],clubs[5])
            match(clubs[10],clubs[4])
            match(clubs[11],clubs[3])
            match(clubs[12],clubs[2])
            match(clubs[13],clubs[1])
            match(clubs[14],clubs[0])
        for cl in clubs:
            cl.difference = cl.scored - cl.conceded
            cl.save()
    def season18(clubs):
        for i in range(2):
            match(clubs[0],clubs[17])
            match(clubs[1],clubs[16])
            match(clubs[2],clubs[15])
            match(clubs[3],clubs[14])
            match(clubs[4],clubs[13])
            match(clubs[5],clubs[12])
            match(clubs[6],clubs[11])
            match(clubs[7],clubs[10])
            match(clubs[8],clubs[9])
            match(clubs[9],clubs[17])
            match(clubs[10],clubs[8])
            match(clubs[11],clubs[7])
            match(clubs[12],clubs[6])
            match(clubs[13],clubs[5])
            match(clubs[14],clubs[4])
            match(clubs[15],clubs[3])
            match(clubs[16],clubs[2])
            match(clubs[0],clubs[1])
            match(clubs[1],clubs[17])
            match(clubs[2],clubs[0])
            match(clubs[3],clubs[16])
            match(clubs[4],clubs[15])
            match(clubs[5],clubs[14])
            match(clubs[6],clubs[13])
            match(clubs[7],clubs[12])
            match(clubs[8],clubs[11])
            match(clubs[9],clubs[10])
            match(clubs[10],clubs[17])
            match(clubs[11],clubs[9])
            match(clubs[12],clubs[8])
            match(clubs[13],clubs[7])
            match(clubs[14],clubs[6])
            match(clubs[15],clubs[5])
            match(clubs[16],clubs[4])
            match(clubs[0],clubs[3])
            match(clubs[1],clubs[2])
            match(clubs[2],clubs[17])
            match(clubs[3],clubs[1])
            match(clubs[4],clubs[0])
            match(clubs[5],clubs[16])
            match(clubs[6],clubs[15])
            match(clubs[7],clubs[14])
            match(clubs[8],clubs[13])
            match(clubs[9],clubs[12])
            match(clubs[10],clubs[11])
            match(clubs[11],clubs[17])
            match(clubs[12],clubs[10])
            match(clubs[13],clubs[9])
            match(clubs[14],clubs[8])
            match(clubs[15],clubs[7])
            match(clubs[16],clubs[6])
            match(clubs[0],clubs[5])
            match(clubs[1],clubs[4])
            match(clubs[2],clubs[3])
            match(clubs[3],clubs[17])
            match(clubs[4],clubs[2])
            match(clubs[5],clubs[1])
            match(clubs[6],clubs[0])
            match(clubs[7],clubs[16])
            match(clubs[8],clubs[15])
            match(clubs[9],clubs[14])
            match(clubs[10],clubs[13])
            match(clubs[11],clubs[12])
            match(clubs[12],clubs[17])
            match(clubs[13],clubs[11])
            match(clubs[14],clubs[10])
            match(clubs[15],clubs[9])
            match(clubs[16],clubs[8])
            match(clubs[0],clubs[7])
            match(clubs[1],clubs[6])
            match(clubs[2],clubs[5])
            match(clubs[3],clubs[4])
            match(clubs[4],clubs[17])
            match(clubs[5],clubs[3])
            match(clubs[6],clubs[2])
            match(clubs[7],clubs[1])
            match(clubs[8],clubs[0])
            match(clubs[9],clubs[16])
            match(clubs[10],clubs[15])
            match(clubs[11],clubs[14])
            match(clubs[12],clubs[13])
            match(clubs[13],clubs[17])
            match(clubs[14],clubs[12])
            match(clubs[15],clubs[11])
            match(clubs[16],clubs[10])
            match(clubs[0],clubs[9])
            match(clubs[1],clubs[8])
            match(clubs[2],clubs[7])
            match(clubs[3],clubs[6])
            match(clubs[4],clubs[5])
            match(clubs[5],clubs[17])
            match(clubs[6],clubs[4])
            match(clubs[7],clubs[3])
            match(clubs[8],clubs[2])
            match(clubs[9],clubs[1])
            match(clubs[10],clubs[0])
            match(clubs[11],clubs[16])
            match(clubs[12],clubs[15])
            match(clubs[13],clubs[14])
            match(clubs[14],clubs[17])
            match(clubs[15],clubs[13])
            match(clubs[16],clubs[12])
            match(clubs[0],clubs[11])
            match(clubs[1],clubs[10])
            match(clubs[2],clubs[9])
            match(clubs[3],clubs[8])
            match(clubs[4],clubs[7])
            match(clubs[5],clubs[6])
            match(clubs[6],clubs[17])
            match(clubs[7],clubs[5])
            match(clubs[8],clubs[4])
            match(clubs[9],clubs[3])
            match(clubs[10],clubs[2])
            match(clubs[11],clubs[1])
            match(clubs[12],clubs[0])
            match(clubs[13],clubs[16])
            match(clubs[14],clubs[15])
            match(clubs[15],clubs[17])
            match(clubs[16],clubs[14])
            match(clubs[0],clubs[13])
            match(clubs[1],clubs[12])
            match(clubs[2],clubs[11])
            match(clubs[3],clubs[10])
            match(clubs[4],clubs[9])
            match(clubs[5],clubs[8])
            match(clubs[6],clubs[7])
            match(clubs[7],clubs[17])
            match(clubs[8],clubs[6])
            match(clubs[9],clubs[5])
            match(clubs[10],clubs[4])
            match(clubs[11],clubs[3])
            match(clubs[12],clubs[2])
            match(clubs[13],clubs[1])
            match(clubs[14],clubs[0])
            match(clubs[15],clubs[16])
            match(clubs[16],clubs[17])
            match(clubs[0],clubs[15])
            match(clubs[1],clubs[14])
            match(clubs[2],clubs[13])
            match(clubs[3],clubs[12])
            match(clubs[4],clubs[11])
            match(clubs[5],clubs[10])
            match(clubs[6],clubs[9])
            match(clubs[7],clubs[8])
            match(clubs[8],clubs[17])
            match(clubs[9],clubs[7])
            match(clubs[10],clubs[6])
            match(clubs[11],clubs[5])
            match(clubs[12],clubs[4])
            match(clubs[13],clubs[3])
            match(clubs[14],clubs[2])
            match(clubs[15],clubs[1])
            match(clubs[16],clubs[0])
        for cl in clubs:
            cl.difference = cl.scored - cl.conceded
            cl.save()
    def season20(clubs):
        for i in range(2):
            match(clubs[0],clubs[19])
            match(clubs[1],clubs[18])
            match(clubs[2],clubs[17])
            match(clubs[3],clubs[16])
            match(clubs[4],clubs[15])
            match(clubs[5],clubs[14])
            match(clubs[6],clubs[13])
            match(clubs[7],clubs[12])
            match(clubs[8],clubs[11])
            match(clubs[9],clubs[10])

            match(clubs[10],clubs[19])
            match(clubs[11],clubs[9])
            match(clubs[12],clubs[8])
            match(clubs[13],clubs[7])
            match(clubs[14],clubs[6])
            match(clubs[15],clubs[5])
            match(clubs[16],clubs[4])
            match(clubs[17],clubs[3])
            match(clubs[18],clubs[2])
            match(clubs[0],clubs[1])

            match(clubs[1],clubs[19])
            match(clubs[2],clubs[0])
            match(clubs[3],clubs[18])
            match(clubs[4],clubs[17])
            match(clubs[5],clubs[16])
            match(clubs[6],clubs[15])
            match(clubs[7],clubs[14])
            match(clubs[8],clubs[13])
            match(clubs[9],clubs[12])
            match(clubs[10],clubs[11])

            match(clubs[11],clubs[19])
            match(clubs[12],clubs[10])
            match(clubs[13],clubs[9])
            match(clubs[14],clubs[8])
            match(clubs[15],clubs[7])
            match(clubs[16],clubs[6])
            match(clubs[17],clubs[5])
            match(clubs[18],clubs[4])
            match(clubs[0],clubs[3])
            match(clubs[1],clubs[2])

            match(clubs[2],clubs[19])
            match(clubs[3],clubs[1])
            match(clubs[4],clubs[0])
            match(clubs[5],clubs[18])
            match(clubs[6],clubs[17])
            match(clubs[7],clubs[16])
            match(clubs[8],clubs[15])
            match(clubs[9],clubs[14])
            match(clubs[10],clubs[13])
            match(clubs[11],clubs[12])

            match(clubs[12],clubs[19])
            match(clubs[13],clubs[11])
            match(clubs[14],clubs[10])
            match(clubs[15],clubs[9])
            match(clubs[16],clubs[8])
            match(clubs[17],clubs[7])
            match(clubs[18],clubs[6])
            match(clubs[0],clubs[5])
            match(clubs[1],clubs[4])
            match(clubs[2],clubs[3])

            match(clubs[3],clubs[19])
            match(clubs[4],clubs[2])
            match(clubs[5],clubs[1])
            match(clubs[6],clubs[0])
            match(clubs[7],clubs[18])
            match(clubs[8],clubs[17])
            match(clubs[9],clubs[16])
            match(clubs[10],clubs[15])
            match(clubs[11],clubs[14])
            match(clubs[12],clubs[13])

            match(clubs[13],clubs[19])
            match(clubs[14],clubs[12])
            match(clubs[15],clubs[11])
            match(clubs[16],clubs[10])
            match(clubs[17],clubs[9])
            match(clubs[18],clubs[8])
            match(clubs[0],clubs[7])
            match(clubs[1],clubs[6])
            match(clubs[2],clubs[5])
            match(clubs[3],clubs[4])

            match(clubs[4],clubs[19])
            match(clubs[5],clubs[3])
            match(clubs[6],clubs[2])
            match(clubs[7],clubs[1])
            match(clubs[8],clubs[0])
            match(clubs[9],clubs[18])
            match(clubs[10],clubs[17])
            match(clubs[11],clubs[16])
            match(clubs[12],clubs[15])
            match(clubs[13],clubs[14])

            match(clubs[14],clubs[19])
            match(clubs[15],clubs[13])
            match(clubs[16],clubs[12])
            match(clubs[17],clubs[11])
            match(clubs[18],clubs[10])
            match(clubs[0],clubs[9])
            match(clubs[1],clubs[8])
            match(clubs[2],clubs[7])
            match(clubs[3],clubs[6])
            match(clubs[4],clubs[5])

            match(clubs[5],clubs[19])
            match(clubs[6],clubs[4])
            match(clubs[7],clubs[3])
            match(clubs[8],clubs[2])
            match(clubs[9],clubs[1])
            match(clubs[10],clubs[0])
            match(clubs[11],clubs[18])
            match(clubs[12],clubs[17])
            match(clubs[13],clubs[16])
            match(clubs[14],clubs[15])

            match(clubs[15],clubs[19])
            match(clubs[16],clubs[14])
            match(clubs[17],clubs[13])
            match(clubs[18],clubs[12])
            match(clubs[0],clubs[11])
            match(clubs[1],clubs[10])
            match(clubs[2],clubs[9])
            match(clubs[3],clubs[8])
            match(clubs[4],clubs[7])
            match(clubs[5],clubs[6])

            match(clubs[6],clubs[19])
            match(clubs[7],clubs[5])
            match(clubs[8],clubs[4])
            match(clubs[9],clubs[3])
            match(clubs[10],clubs[2])
            match(clubs[11],clubs[1])
            match(clubs[12],clubs[0])
            match(clubs[13],clubs[18])
            match(clubs[14],clubs[17])
            match(clubs[15],clubs[16])

            match(clubs[16],clubs[19])
            match(clubs[17],clubs[15])
            match(clubs[18],clubs[14])
            match(clubs[0],clubs[13])
            match(clubs[1],clubs[12])
            match(clubs[2],clubs[11])
            match(clubs[3],clubs[10])
            match(clubs[4],clubs[9])
            match(clubs[5],clubs[8])
            match(clubs[6],clubs[7])

            match(clubs[7],clubs[19])
            match(clubs[8],clubs[6])
            match(clubs[9],clubs[5])
            match(clubs[10],clubs[4])
            match(clubs[11],clubs[3])
            match(clubs[12],clubs[2])
            match(clubs[13],clubs[1])
            match(clubs[14],clubs[0])
            match(clubs[15],clubs[18])
            match(clubs[16],clubs[17])

            match(clubs[17],clubs[19])
            match(clubs[18],clubs[16])
            match(clubs[0],clubs[15])
            match(clubs[1],clubs[14])
            match(clubs[2],clubs[13])
            match(clubs[3],clubs[12])
            match(clubs[4],clubs[11])
            match(clubs[5],clubs[10])
            match(clubs[6],clubs[9])
            match(clubs[7],clubs[8])

            match(clubs[8],clubs[19])
            match(clubs[9],clubs[7])
            match(clubs[10],clubs[6])
            match(clubs[11],clubs[5])
            match(clubs[12],clubs[4])
            match(clubs[13],clubs[3])
            match(clubs[14],clubs[2])
            match(clubs[15],clubs[1])
            match(clubs[16],clubs[0])
            match(clubs[17],clubs[18])

            match(clubs[18],clubs[19])
            match(clubs[0],clubs[17])
            match(clubs[1],clubs[16])
            match(clubs[2],clubs[15])
            match(clubs[3],clubs[14])
            match(clubs[4],clubs[13])
            match(clubs[5],clubs[12])
            match(clubs[6],clubs[11])
            match(clubs[7],clubs[10])
            match(clubs[8],clubs[9])

            match(clubs[9],clubs[19])
            match(clubs[10],clubs[8])
            match(clubs[11],clubs[7])
            match(clubs[12],clubs[6])
            match(clubs[13],clubs[5])
            match(clubs[14],clubs[4])
            match(clubs[15],clubs[3])
            match(clubs[16],clubs[2])
            match(clubs[17],clubs[1])
            match(clubs[18],clubs[0])
        for i in clubs:
            i.difference = i.scored - i.conceded
            i.save()

    season8(azerbejdzan_list)
    season8(lotwa_list)
    season8(andora_list)

    season10(wyspy_Owcze_list)
    season10(kosowo_list)
    season10(estonia_list)
    season10(czarnogora_list)
    season10(szwajcaria_list)
    season10(chorwacja_list)
    season10(slowenia_list)
    season10(litwa_list)
    season10(armenia_list)
    season10(albania_list)
    season10(moldawia_list)
    season10(irlandia_list)
    season10(gruzja_list)

    season12(austria_list)
    season12(dania_list)
    season12(szkocja_list)
    season12(slowacja_list)
    season12(wegry_list)
    season12(macedonia_list)
    season12(bosnia_list)
    season12(finlandia_list)
    season12(islandia_list)
    season12(walia_list)
    season12(irlandia_Pln_list)
    season12(gibraltar_list)

    season14(ukraina_list)
    season14(cypr_list)
    season14(grecja_list)
    season14(izrael_list)
    season14(kazachstan_list)
    season14(bulgaria_list)
    season14(san_Marino_list)

    season16(ekst_list)
    season16(rosja_list)
    season16(szwecja_list)
    season16(norwegia_list)
    season16(bialorus_list)
    season16(rumunia_list)
    season16(luxembourg_list)
    season16(malta_list)

    season18(pliga_list)
    season18(dliga_list)
    season18(niemcy_list)
    season18(portugalia_list)
    season18(belgia_list)
    season18(holandia_list)
    season18(czechy_list)

    season20(hiszpania_list)
    season20(anglia_list)
    season20(wlochy_list)
    season20(francja_list)
    season20(turcja_list)
    season20(serbia_list)
    ekst_list = Ekstraklasa.objects.order_by('-points','-difference','-scored')
    pliga_list = Pierwsza_Liga.objects.order_by('-points','-difference','-scored')
    dliga_list = Druga_Liga.objects.order_by('-points','-difference','-scored')
    hiszpania_list = Hiszpania.objects.order_by('-points','-difference','-scored')
    francja_list = Francja.objects.order_by('-points','-difference','-scored')
    anglia_list = Anglia.objects.order_by('-points','-difference','-scored')
    niemcy_list = Niemcy.objects.order_by('-points','-difference','-scored')
    wlochy_list = Wlochy.objects.order_by('-points','-difference','-scored')
    portugalia_list = Portugalia.objects.order_by('-points','-difference','-scored')
    rosja_list = Rosja.objects.order_by('-points','-difference','-scored')
    belgia_list = Belgia.objects.order_by('-points','-difference','-scored')
    ukraina_list = Ukraina.objects.order_by('-points','-difference','-scored')
    holandia_list = Holandia.objects.order_by('-points','-difference','-scored')
    turcja_list = Turcja.objects.order_by('-points','-difference','-scored')
    austria_list = Austria.objects.order_by('-points','-difference','-scored')
    dania_list = Dania.objects.order_by('-points','-difference','-scored')
    szkocja_list = Szkocja.objects.order_by('-points','-difference','-scored')
    czechy_list = Czechy.objects.order_by('-points','-difference','-scored')
    cypr_list = Cypr.objects.order_by('-points','-difference','-scored')
    szwajcaria_list = Szwajcaria.objects.order_by('-points','-difference','-scored')
    grecja_list = Grecja.objects.order_by('-points','-difference','-scored')
    serbia_list = Serbia.objects.order_by('-points','-difference','-scored')
    chorwacja_list = Chorwacja.objects.order_by('-points','-difference','-scored')
    szwecja_list = Szwecja.objects.order_by('-points','-difference','-scored')
    norwegia_list = Norwegia.objects.order_by('-points','-difference','-scored')
    izrael_list = Izrael.objects.order_by('-points','-difference','-scored')
    kazachstan_list = Kazachstan.objects.order_by('-points','-difference','-scored')
    bialorus_list = Bialorus.objects.order_by('-points','-difference','-scored')
    azerbejdzan_list = Azerbejdzan.objects.order_by('-points','-difference','-scored')
    bulgaria_list = Bulgaria.objects.order_by('-points','-difference','-scored')
    rumunia_list = Rumunia.objects.order_by('-points','-difference','-scored')
    slowacja_list = Slowacja.objects.order_by('-points','-difference','-scored')
    liechtenstein_list = Liechtenstein.objects.order_by('-points','-difference','-scored')
    slowenia_list = Slowenia.objects.order_by('-points','-difference','-scored')
    wegry_list = Wegry.objects.order_by('-points','-difference','-scored')
    luxembourg_list = Luxembourg.objects.order_by('-points','-difference','-scored')
    litwa_list = Litwa.objects.order_by('-points','-difference','-scored')
    armenia_list = Armenia.objects.order_by('-points','-difference','-scored')
    lotwa_list = Lotwa.objects.order_by('-points','-difference','-scored')
    albania_list = Albania.objects.order_by('-points','-difference','-scored')
    macedonia_list = Macedonia.objects.order_by('-points','-difference','-scored')
    bosnia_list = Bosnia.objects.order_by('-points','-difference','-scored')
    moldawia_list = Moldawia.objects.order_by('-points','-difference','-scored')
    finlandia_list = Finlandia.objects.order_by('-points','-difference','-scored')
    irlandia_list = Irlandia.objects.order_by('-points','-difference','-scored')
    gruzja_list = Gruzja.objects.order_by('-points','-difference','-scored')
    malta_list = Malta.objects.order_by('-points','-difference','-scored')
    islandia_list = Islandia.objects.order_by('-points','-difference','-scored')
    walia_list = Walia.objects.order_by('-points','-difference','-scored')
    irlandia_Pln_list = Irlandia_Pln.objects.order_by('-points','-difference','-scored')
    gibraltar_list = Gibraltar.objects.order_by('-points','-difference','-scored')
    czarnogora_list = Czarnogora.objects.order_by('-points','-difference','-scored')
    estonia_list = Estonia.objects.order_by('-points','-difference','-scored')
    kosowo_list = Kosowo.objects.order_by('-points','-difference','-scored')
    wyspy_Owcze_list = Wyspy_Owcze.objects.order_by('-points','-difference','-scored')
    andora_list = Andora.objects.order_by('-points','-difference','-scored')
    san_Marino_list = San_Marino.objects.order_by('-points','-difference','-scored')

    all_dict = {'ekst_records':ekst_list,'pier_liga_records':pliga_list,'drug_liga_records':dliga_list,'hiszpania_records':hiszpania_list,'francja_records':francja_list,'anglia_records':anglia_list,
    'niemcy_records':niemcy_list,'wlochy_records':wlochy_list,'portugalia_records':portugalia_list,
    'rosja_records':rosja_list,
    'belgia_records':belgia_list,
    'ukraina_records':ukraina_list,
    'holandia_records':holandia_list,
    'turcja_records':turcja_list,
    'austria_records':austria_list,
    'dania_records':dania_list,
    'szkocja_records':szkocja_list,
    'czechy_records':czechy_list,
    'cypr_records':cypr_list,
    'szwajcaria_records':szwajcaria_list,
    'grecja_records':grecja_list,
    'serbia_records':serbia_list,
    'chorwacja_records':chorwacja_list,
    'szwecja_records':szwecja_list,
    'norwegia_records':norwegia_list,
    'izrael_records':izrael_list,
    'kazachstan_records':kazachstan_list,
    'bialorus_records':bialorus_list,
    'azerbejdzan_records':azerbejdzan_list,
    'bulgaria_records':bulgaria_list,
    'rumunia_records':rumunia_list,
    'slowacja_records':slowacja_list,
    'liechtenstein_records':liechtenstein_list,
    'slowenia_records':slowenia_list,
    'wegry_records':wegry_list,
    'luxembourg_records':luxembourg_list,
    'litwa_records':litwa_list,
    'armenia_records':armenia_list,
    'lotwa_records':lotwa_list,
    'albania_records':albania_list,
    'macedonia_records':macedonia_list,
    'bosnia_records':bosnia_list,
    'moldawia_records':moldawia_list,
    'finlandia_records':finlandia_list,
    'irlandia_records':irlandia_list,
    'gruzja_records':gruzja_list,
    'malta_records':malta_list,
    'islandia_records':islandia_list,
    'walia_records':walia_list,
    'irlandia_Pln_records':irlandia_Pln_list,
    'gibraltar_records':gibraltar_list,
    'czarnogora_records':czarnogora_list,
    'estonia_records':estonia_list,
    'kosowo_records':kosowo_list,
    'wyspy_Owcze_records':wyspy_Owcze_list,
    'andora_records':andora_list,
    'san_Marino_records':san_Marino_list,}
    POL_gallery.objects.create(name=ekst_list[0].name,image=ekst_list[0].image)
    return render(request,'first_app/index.html',context=all_dict)
def index_clean(request):
    ekst_list = Ekstraklasa.objects.order_by('-points','-difference','-scored')
    pliga_list = Pierwsza_Liga.objects.order_by('-points','-difference','-scored')
    dliga_list = Druga_Liga.objects.order_by('-points','-difference','-scored')
    hiszpania_list = Hiszpania.objects.order_by('-points','-difference','-scored')
    francja_list = Francja.objects.order_by('-points','-difference','-scored')
    anglia_list = Anglia.objects.order_by('-points','-difference','-scored')
    niemcy_list = Niemcy.objects.order_by('-points','-difference','-scored')
    wlochy_list = Wlochy.objects.order_by('-points','-difference','-scored')
    portugalia_list = Portugalia.objects.order_by('-points','-difference','-scored')
    rosja_list = Rosja.objects.order_by('-points','-difference','-scored')
    belgia_list = Belgia.objects.order_by('-points','-difference','-scored')
    ukraina_list = Ukraina.objects.order_by('-points','-difference','-scored')
    holandia_list = Holandia.objects.order_by('-points','-difference','-scored')
    turcja_list = Turcja.objects.order_by('-points','-difference','-scored')
    austria_list = Austria.objects.order_by('-points','-difference','-scored')
    dania_list = Dania.objects.order_by('-points','-difference','-scored')
    szkocja_list = Szkocja.objects.order_by('-points','-difference','-scored')
    czechy_list = Czechy.objects.order_by('-points','-difference','-scored')
    cypr_list = Cypr.objects.order_by('-points','-difference','-scored')
    szwajcaria_list = Szwajcaria.objects.order_by('-points','-difference','-scored')
    grecja_list = Grecja.objects.order_by('-points','-difference','-scored')
    serbia_list = Serbia.objects.order_by('-points','-difference','-scored')
    chorwacja_list = Chorwacja.objects.order_by('-points','-difference','-scored')
    szwecja_list = Szwecja.objects.order_by('-points','-difference','-scored')
    norwegia_list = Norwegia.objects.order_by('-points','-difference','-scored')
    izrael_list = Izrael.objects.order_by('-points','-difference','-scored')
    kazachstan_list = Kazachstan.objects.order_by('-points','-difference','-scored')
    bialorus_list = Bialorus.objects.order_by('-points','-difference','-scored')
    azerbejdzan_list = Azerbejdzan.objects.order_by('-points','-difference','-scored')
    bulgaria_list = Bulgaria.objects.order_by('-points','-difference','-scored')
    rumunia_list = Rumunia.objects.order_by('-points','-difference','-scored')
    slowacja_list = Slowacja.objects.order_by('-points','-difference','-scored')
    liechtenstein_list = Liechtenstein.objects.order_by('-points','-difference','-scored')
    slowenia_list = Slowenia.objects.order_by('-points','-difference','-scored')
    wegry_list = Wegry.objects.order_by('-points','-difference','-scored')
    luxembourg_list = Luxembourg.objects.order_by('-points','-difference','-scored')
    litwa_list = Litwa.objects.order_by('-points','-difference','-scored')
    armenia_list = Armenia.objects.order_by('-points','-difference','-scored')
    lotwa_list = Lotwa.objects.order_by('-points','-difference','-scored')
    albania_list = Albania.objects.order_by('-points','-difference','-scored')
    macedonia_list = Macedonia.objects.order_by('-points','-difference','-scored')
    bosnia_list = Bosnia.objects.order_by('-points','-difference','-scored')
    moldawia_list = Moldawia.objects.order_by('-points','-difference','-scored')
    finlandia_list = Finlandia.objects.order_by('-points','-difference','-scored')
    irlandia_list = Irlandia.objects.order_by('-points','-difference','-scored')
    gruzja_list = Gruzja.objects.order_by('-points','-difference','-scored')
    malta_list = Malta.objects.order_by('-points','-difference','-scored')
    islandia_list = Islandia.objects.order_by('-points','-difference','-scored')
    walia_list = Walia.objects.order_by('-points','-difference','-scored')
    irlandia_Pln_list = Irlandia_Pln.objects.order_by('-points','-difference','-scored')
    gibraltar_list = Gibraltar.objects.order_by('-points','-difference','-scored')
    czarnogora_list = Czarnogora.objects.order_by('-points','-difference','-scored')
    estonia_list = Estonia.objects.order_by('-points','-difference','-scored')
    kosowo_list = Kosowo.objects.order_by('-points','-difference','-scored')
    wyspy_Owcze_list = Wyspy_Owcze.objects.order_by('-points','-difference','-scored')
    andora_list = Andora.objects.order_by('-points','-difference','-scored')
    san_Marino_list = San_Marino.objects.order_by('-points','-difference','-scored')
    all_dict = {'ekst_records':ekst_list,'pier_liga_records':pliga_list,'drug_liga_records':dliga_list,'hiszpania_records':hiszpania_list,'francja_records':francja_list,'anglia_records':anglia_list,
    'niemcy_records':niemcy_list,'wlochy_records':wlochy_list,'portugalia_records':portugalia_list,
    'rosja_records':rosja_list,
    'belgia_records':belgia_list,
    'ukraina_records':ukraina_list,
    'holandia_records':holandia_list,
    'turcja_records':turcja_list,
    'austria_records':austria_list,
    'dania_records':dania_list,
    'szkocja_records':szkocja_list,
    'czechy_records':czechy_list,
    'cypr_records':cypr_list,
    'szwajcaria_records':szwajcaria_list,
    'grecja_records':grecja_list,
    'serbia_records':serbia_list,
    'chorwacja_records':chorwacja_list,
    'szwecja_records':szwecja_list,
    'norwegia_records':norwegia_list,
    'izrael_records':izrael_list,
    'kazachstan_records':kazachstan_list,
    'bialorus_records':bialorus_list,
    'azerbejdzan_records':azerbejdzan_list,
    'bulgaria_records':bulgaria_list,
    'rumunia_records':rumunia_list,
    'slowacja_records':slowacja_list,
    'liechtenstein_records':liechtenstein_list,
    'slowenia_records':slowenia_list,
    'wegry_records':wegry_list,
    'luxembourg_records':luxembourg_list,
    'litwa_records':litwa_list,
    'armenia_records':armenia_list,
    'lotwa_records':lotwa_list,
    'albania_records':albania_list,
    'macedonia_records':macedonia_list,
    'bosnia_records':bosnia_list,
    'moldawia_records':moldawia_list,
    'finlandia_records':finlandia_list,
    'irlandia_records':irlandia_list,
    'gruzja_records':gruzja_list,
    'malta_records':malta_list,
    'islandia_records':islandia_list,
    'walia_records':walia_list,
    'irlandia_Pln_records':irlandia_Pln_list,
    'gibraltar_records':gibraltar_list,
    'czarnogora_records':czarnogora_list,
    'estonia_records':estonia_list,
    'kosowo_records':kosowo_list,
    'wyspy_Owcze_records':wyspy_Owcze_list,
    'andora_records':andora_list,
    'san_Marino_records':san_Marino_list,}
    Ekstraklasa.objects.all().update(points=0,scored=0, conceded=0,wins = 0,loses=0,draws=0)
    Pierwsza_Liga.objects.all().update(points=0,scored=0, conceded=0,wins = 0,loses=0,draws=0)
    Druga_Liga.objects.all().update(points=0,scored=0, conceded=0,wins = 0,loses=0,draws=0)
    Niemcy.objects.all().update(points=0,scored=0, conceded=0,wins = 0,loses=0,draws=0)
    Wlochy.objects.all().update(points=0,scored=0, conceded=0,wins = 0,loses=0,draws=0)
    Hiszpania.objects.all().update(points=0,scored=0, conceded=0,wins = 0,loses=0,draws=0)
    Francja.objects.all().update(points=0,scored=0, conceded=0,wins = 0,loses=0,draws=0)
    Anglia.objects.all().update(points=0,scored=0, conceded=0,wins = 0,loses=0,draws=0)
    Portugalia.objects.all().update(points=0,scored=0, conceded=0,wins = 0,loses=0,draws=0)
    Rosja.objects.all().update(points=0,scored=0, conceded=0,wins = 0,loses=0,draws=0)
    Belgia.objects.all().update(points=0,scored=0, conceded=0,wins = 0,loses=0,draws=0)
    Ukraina.objects.all().update(points=0,scored=0, conceded=0,wins = 0,loses=0,draws=0)
    Holandia.objects.all().update(points=0,scored=0, conceded=0,wins = 0,loses=0,draws=0)
    Turcja.objects.all().update(points=0,scored=0, conceded=0,wins = 0,loses=0,draws=0)
    Austria.objects.all().update(points=0,scored=0, conceded=0,wins = 0,loses=0,draws=0)
    Dania.objects.all().update(points=0,scored=0, conceded=0,wins = 0,loses=0,draws=0)
    Szkocja.objects.all().update(points=0,scored=0, conceded=0,wins = 0,loses=0,draws=0)
    Czechy.objects.all().update(points=0,scored=0, conceded=0,wins = 0,loses=0,draws=0)
    Cypr.objects.all().update(points=0,scored=0, conceded=0,wins = 0,loses=0,draws=0)
    Szwajcaria.objects.all().update(points=0,scored=0, conceded=0,wins = 0,loses=0,draws=0)
    Grecja.objects.all().update(points=0,scored=0, conceded=0,wins = 0,loses=0,draws=0)
    Serbia.objects.all().update(points=0,scored=0, conceded=0,wins = 0,loses=0,draws=0)
    Chorwacja.objects.all().update(points=0,scored=0, conceded=0,wins = 0,loses=0,draws=0)
    Szwecja.objects.all().update(points=0,scored=0, conceded=0,wins = 0,loses=0,draws=0)
    Norwegia.objects.all().update(points=0,scored=0, conceded=0,wins = 0,loses=0,draws=0)
    Izrael.objects.all().update(points=0,scored=0, conceded=0,wins = 0,loses=0,draws=0)
    Kazachstan.objects.all().update(points=0,scored=0, conceded=0,wins = 0,loses=0,draws=0)
    Bialorus.objects.all().update(points=0,scored=0, conceded=0,wins = 0,loses=0,draws=0)
    Azerbejdzan.objects.all().update(points=0,scored=0, conceded=0,wins = 0,loses=0,draws=0)
    Bulgaria.objects.all().update(points=0,scored=0, conceded=0,wins = 0,loses=0,draws=0)
    Rumunia.objects.all().update(points=0,scored=0, conceded=0,wins = 0,loses=0,draws=0)
    Slowacja.objects.all().update(points=0,scored=0, conceded=0,wins = 0,loses=0,draws=0)
    Slowenia.objects.all().update(points=0,scored=0, conceded=0,wins = 0,loses=0,draws=0)
    Wegry.objects.all().update(points=0,scored=0, conceded=0,wins = 0,loses=0,draws=0)
    Luxembourg.objects.all().update(points=0,scored=0, conceded=0,wins = 0,loses=0,draws=0)
    Litwa.objects.all().update(points=0,scored=0, conceded=0,wins = 0,loses=0,draws=0)
    Armenia.objects.all().update(points=0,scored=0, conceded=0,wins = 0,loses=0,draws=0)
    Lotwa.objects.all().update(points=0,scored=0, conceded=0,wins = 0,loses=0,draws=0)
    Albania.objects.all().update(points=0,scored=0, conceded=0,wins = 0,loses=0,draws=0)
    Macedonia.objects.all().update(points=0,scored=0, conceded=0,wins = 0,loses=0,draws=0)
    Bosnia.objects.all().update(points=0,scored=0, conceded=0,wins = 0,loses=0,draws=0)
    Moldawia.objects.all().update(points=0,scored=0, conceded=0,wins = 0,loses=0,draws=0)
    Finlandia.objects.all().update(points=0,scored=0, conceded=0,wins = 0,loses=0,draws=0)
    Irlandia.objects.all().update(points=0,scored=0, conceded=0,wins = 0,loses=0,draws=0)
    Gruzja.objects.all().update(points=0,scored=0, conceded=0,wins = 0,loses=0,draws=0)
    Malta.objects.all().update(points=0,scored=0, conceded=0,wins = 0,loses=0,draws=0)
    Islandia.objects.all().update(points=0,scored=0, conceded=0,wins = 0,loses=0,draws=0)
    Walia.objects.all().update(points=0,scored=0, conceded=0,wins = 0,loses=0,draws=0)
    Irlandia_Pln.objects.all().update(points=0,scored=0, conceded=0,wins = 0,loses=0,draws=0)
    Gibraltar.objects.all().update(points=0,scored=0, conceded=0,wins = 0,loses=0,draws=0)
    Czarnogora.objects.all().update(points=0,scored=0, conceded=0,wins = 0,loses=0,draws=0)
    Estonia.objects.all().update(points=0,scored=0, conceded=0,wins = 0,loses=0,draws=0)
    Kosowo.objects.all().update(points=0,scored=0, conceded=0,wins = 0,loses=0,draws=0)
    Wyspy_Owcze.objects.all().update(points=0,scored=0, conceded=0,wins = 0,loses=0,draws=0)
    Andora.objects.all().update(points=0,scored=0, conceded=0,wins = 0,loses=0,draws=0)
    San_Marino.objects.all().update(points=0,scored=0, conceded=0,wins = 0,loses=0,draws=0)

    return render(request,'first_app/index.html',context=all_dict)
def gallery_europa(request):
    ecl = ECL_gallery.objects.all()
    le = LE_gallery.objects.all()
    lm = LM_gallery.objects.all()
    dict = {'ECL_records':ecl,'LE_records':le,'LM_records':lm,}
    return render(request,'first_app/gallery_europa.html',context=dict)
def gallery_polska(request):
    ekst = POL_gallery.objects.all()
    pp = PP_gallery.objects.all()
    dict = {'POL_records':ekst,'PP_records':pp}
    return render(request,'first_app/gallery_polska.html',context=dict)

def europa(request):
    date_dict =  {'europa_insert':'Panel rozgrywek europejskich'}
    return render(request,'first_app/europa.html',context=date_dict)
def eliminacje_LM(request):
    LM_4 = Elim_LM_4.objects.all()
    LM_3 = Elim_LM_3.objects.all()
    LM_2 = Elim_LM_2.objects.all()
    LM_1 = Elim_LM_1.objects.all()
    dict = {'LM_4_records':LM_4,'LM_3_records':LM_3,'LM_2_records':LM_2,'LM_1_records':LM_1,}
    return render(request,'first_app/eliminacje_LM.html',context=dict)
def eliminacje_LE(request):
    LE_4 = Elim_LE_4.objects.all()
    LE_3 = Elim_LE_3.objects.all()
    dict = {'LE_4_records':LE_4,'LE_3_records':LE_3}
    return render(request,'first_app/eliminacje_LE.html',context=dict)
def eliminacje_ECL(request):
    ECL_4 = Elim_ECL_4.objects.all()
    ECL_3 = Elim_ECL_3.objects.all()
    ECL_2 = Elim_ECL_2.objects.all()
    ECL_1 = Elim_ECL_1.objects.all()
    dict = {'ECL_4_records':ECL_4,'ECL_3_records':ECL_3,'ECL_2_records':ECL_2,'ECL_1_records':ECL_1,}
    return render(request,'first_app/eliminacje_ECL.html',context=dict)
def eliminacje_season(request):
    ekst_list = Ekstraklasa.objects.order_by('-points','-difference','-scored')
    pliga_list = Pierwsza_Liga.objects.order_by('-points','-difference','-scored')
    dliga_list = Druga_Liga.objects.order_by('-points','-difference','-scored')
    hiszpania_list = Hiszpania.objects.order_by('-points','-difference','-scored')
    francja_list = Francja.objects.order_by('-points','-difference','-scored')
    anglia_list = Anglia.objects.order_by('-points','-difference','-scored')
    niemcy_list = Niemcy.objects.order_by('-points','-difference','-scored')
    wlochy_list = Wlochy.objects.order_by('-points','-difference','-scored')
    portugalia_list = Portugalia.objects.order_by('-points','-difference','-scored')
    rosja_list = Rosja.objects.order_by('-points','-difference','-scored')
    belgia_list = Belgia.objects.order_by('-points','-difference','-scored')
    ukraina_list = Ukraina.objects.order_by('-points','-difference','-scored')
    holandia_list = Holandia.objects.order_by('-points','-difference','-scored')
    turcja_list = Turcja.objects.order_by('-points','-difference','-scored')
    austria_list = Austria.objects.order_by('-points','-difference','-scored')
    dania_list = Dania.objects.order_by('-points','-difference','-scored')
    szkocja_list = Szkocja.objects.order_by('-points','-difference','-scored')
    czechy_list = Czechy.objects.order_by('-points','-difference','-scored')
    cypr_list = Cypr.objects.order_by('-points','-difference','-scored')
    szwajcaria_list = Szwajcaria.objects.order_by('-points','-difference','-scored')
    grecja_list = Grecja.objects.order_by('-points','-difference','-scored')
    serbia_list = Serbia.objects.order_by('-points','-difference','-scored')
    chorwacja_list = Chorwacja.objects.order_by('-points','-difference','-scored')
    szwecja_list = Szwecja.objects.order_by('-points','-difference','-scored')
    norwegia_list = Norwegia.objects.order_by('-points','-difference','-scored')
    izrael_list = Izrael.objects.order_by('-points','-difference','-scored')
    kazachstan_list = Kazachstan.objects.order_by('-points','-difference','-scored')
    bialorus_list = Bialorus.objects.order_by('-points','-difference','-scored')
    azerbejdzan_list = Azerbejdzan.objects.order_by('-points','-difference','-scored')
    bulgaria_list = Bulgaria.objects.order_by('-points','-difference','-scored')
    rumunia_list = Rumunia.objects.order_by('-points','-difference','-scored')
    slowacja_list = Slowacja.objects.order_by('-points','-difference','-scored')
    liechtenstein_list = Liechtenstein.objects.order_by('-points','-difference','-scored')
    slowenia_list = Slowenia.objects.order_by('-points','-difference','-scored')
    wegry_list = Wegry.objects.order_by('-points','-difference','-scored')
    luxembourg_list = Luxembourg.objects.order_by('-points','-difference','-scored')
    litwa_list = Litwa.objects.order_by('-points','-difference','-scored')
    armenia_list = Armenia.objects.order_by('-points','-difference','-scored')
    lotwa_list = Lotwa.objects.order_by('-points','-difference','-scored')
    albania_list = Albania.objects.order_by('-points','-difference','-scored')
    macedonia_list = Macedonia.objects.order_by('-points','-difference','-scored')
    bosnia_list = Bosnia.objects.order_by('-points','-difference','-scored')
    moldawia_list = Moldawia.objects.order_by('-points','-difference','-scored')
    finlandia_list = Finlandia.objects.order_by('-points','-difference','-scored')
    irlandia_list = Irlandia.objects.order_by('-points','-difference','-scored')
    gruzja_list = Gruzja.objects.order_by('-points','-difference','-scored')
    malta_list = Malta.objects.order_by('-points','-difference','-scored')
    islandia_list = Islandia.objects.order_by('-points','-difference','-scored')
    walia_list = Walia.objects.order_by('-points','-difference','-scored')
    irlandia_Pln_list = Irlandia_Pln.objects.order_by('-points','-difference','-scored')
    gibraltar_list = Gibraltar.objects.order_by('-points','-difference','-scored')
    czarnogora_list = Czarnogora.objects.order_by('-points','-difference','-scored')
    estonia_list = Estonia.objects.order_by('-points','-difference','-scored')
    kosowo_list = Kosowo.objects.order_by('-points','-difference','-scored')
    wyspy_Owcze_list = Wyspy_Owcze.objects.order_by('-points','-difference','-scored')
    andora_list = Andora.objects.order_by('-points','-difference','-scored')
    san_Marino_list = San_Marino.objects.order_by('-points','-difference','-scored')
    d=[]
    d.append(Elim_LM_4.objects.all())
    d.append(Elim_LM_3.objects.all())
    d.append(Elim_LM_2.objects.all())
    d.append(Elim_LM_1.objects.all())
    d.append(Elim_LE_4.objects.all())
    d.append(Elim_LE_3.objects.all())
    d.append(Elim_ECL_4.objects.all())
    d.append(Elim_ECL_3.objects.all())
    d.append(Elim_ECL_2.objects.all())
    d.append(Elim_ECL_1.objects.all())
    d.append(LM_group.objects.all())
    d.append(LE_group.objects.all())
    d.append(ECL_group.objects.all())
    d.append(LM_1_8.objects.all())
    d.append(LM_cwiercfinal.objects.all())
    d.append(LM_polfinal.objects.all())
    d.append(LM_final.objects.all())
    d.append(LM_winner.objects.all())
    d.append(LE_1_16.objects.all())
    d.append(LE_1_8.objects.all())
    d.append(LE_cwiercfinal.objects.all())
    d.append(LE_polfinal.objects.all())
    d.append(LE_final.objects.all())
    d.append(LE_winner.objects.all())
    d.append(ECL_1_16.objects.all())
    d.append(ECL_1_8.objects.all())
    d.append(ECL_cwiercfinal.objects.all())
    d.append(ECL_polfinal.objects.all())
    d.append(ECL_final.objects.all())
    d.append(ECL_winner.objects.all())
    for x in d:
        x.delete()
    groups_LM = []
    groups_LE = []
    groups_ECL = []
    t=[]
    LM_1_list = []
    LM_2_list = []
    LM_3_list = []
    LM_3_eliminated = []
    LM_4_list = []
    LE_3_list = []
    LE_4_list = []
    ECL_1_list = []
    ECL_2_list = []
    ECL_3_list = []
    ECL_4_list = []

    def match(team1, team2, runda):
        host_limit = team1.strength
        guest_limit = 10000 - team2.strength
        b1=0
        b2=0
        def dogrywka(team1, team2,b1,b2,runda):
            def karne(team1, team2,b1,b2,runda):
                k1=0
                k2=0
                for i in range(1,6):
                    los1 = random.randint(0, 100)
                    los2 = random.randint(0, 100)
                    if los1 < 75:
                        k1 = k1 + 1
                    elif los2 > 25:
                        k2 = k2 + 1
                while k1 == k2:
                    los1 = random.randint(0, 100)
                    los2 = random.randint(0, 100)
                    if los1 < 75:
                        k1 = k1 + 1
                    elif los2 > 25:
                        k2 = k2 + 1
                if k1 > k2:
                    if runda=="LM_1":
                        LM_2_list.append(team1)
                        ECL_2_list.append(team2)
                        team1.last_scored=str(b1)+' '+str(k1)+' pk'
                        team2.last_scored=str(b2)+' '+str(k2)
                    elif runda=="LM_2":
                        LM_3_list.append(team1)
                        LE_3_list.append(team2)
                        team1.last_scored=str(b1)+' '+str(k1)+' pk'
                        team2.last_scored=str(b2)+' '+str(k2)
                    elif runda=="LM_3":
                        LM_4_list.append(team1)
                        LM_3_eliminated.append(team2)
                        team1.last_scored=str(b1)+' '+str(k1)+' pk'
                        team2.last_scored=str(b2)+' '+str(k2)
                    elif runda=="LM_4":
                        groups_LM.append(team1)
                        groups_LE.append(team2)
                        team1.last_scored=str(b1)+' '+str(k1)+' pk'
                        team2.last_scored=str(b2)+' '+str(k2)
                    elif runda=="LE_3":
                        LE_4_list.append(team1)
                        ECL_4_list.append(team2)
                        team1.last_scored=str(b1)+' '+str(k1)+' pk'
                        team2.last_scored=str(b2)+' '+str(k2)
                    elif runda=="LE_4":
                        groups_LE.append(team1)
                        groups_ECL.append(team2)
                        team1.last_scored=str(b1)+' '+str(k1)+' pk'
                        team2.last_scored=str(b2)+' '+str(k2)
                    elif runda=="ECL_1":
                        ECL_2_list.append(team1)
                        team1.last_scored=str(b1)+' '+str(k1)+' pk'
                        team2.last_scored=str(b2)+' '+str(k2)
                    elif runda=="ECL_2":
                        ECL_3_list.append(team1)
                        team1.last_scored=str(b1)+' '+str(k1)+' pk'
                        team2.last_scored=str(b2)+' '+str(k2)
                    elif runda=="ECL_3":
                        ECL_4_list.append(team1)
                        team1.last_scored=str(b1)+' '+str(k1)+' pk'
                        team2.last_scored=str(b2)+' '+str(k2)
                    elif runda=="ECL_4":
                        groups_ECL.append(team1)
                        team1.last_scored=str(b1)+' '+str(k1)+' pk'
                        team2.last_scored=str(b2)+' '+str(k2)
                elif k2 > k1:
                    if runda=="LM_1":
                        LM_2_list.append(team2)
                        ECL_2_list.append(team1)
                        team1.last_scored=str(b1)+' '+str(k1)
                        team2.last_scored=str(b2)+' '+str(k2)+' pk'
                    elif runda=="LM_2":
                        LM_3_list.append(team2)
                        LE_3_list.append(team1)
                        team1.last_scored=str(b1)+' '+str(k1)
                        team2.last_scored=str(b2)+' '+str(k2)+' pk'
                    elif runda=="LM_3":
                        LM_4_list.append(team2)
                        LM_3_eliminated.append(team1)
                        team1.last_scored=str(b1)+' '+str(k1)
                        team2.last_scored=str(b2)+' '+str(k2)+' pk'
                    elif runda=="LM_4":
                        groups_LM.append(team2)
                        groups_LE.append(team1)
                        team1.last_scored=str(b1)+' '+str(k1)
                        team2.last_scored=str(b2)+' '+str(k2)+' pk'
                    elif runda=="LE_3":
                        LE_4_list.append(team2)
                        ECL_4_list.append(team1)
                        team1.last_scored=str(b1)+' '+str(k1)
                        team2.last_scored=str(b2)+' '+str(k2)+' pk'
                    elif runda=="LE_4":
                        groups_LE.append(team2)
                        groups_ECL.append(team1)
                        team1.last_scored=str(b1)+' '+str(k1)
                        team2.last_scored=str(b2)+' '+str(k2)+' pk'
                    elif runda=="ECL_1":
                        ECL_2_list.append(team2)
                        team1.last_scored=str(b1)+' '+str(k1)
                        team2.last_scored=str(b2)+' '+str(k2)+' pk'
                    elif runda=="ECL_2":
                        ECL_3_list.append(team2)
                        team1.last_scored=str(b1)+' '+str(k1)
                        team2.last_scored=str(b2)+' '+str(k2)+' pk'
                    elif runda=="ECL_3":
                        ECL_4_list.append(team2)
                        team1.last_scored=str(b1)+' '+str(k1)
                        team2.last_scored=str(b2)+' '+str(k2)+' pk'
                    elif runda=="ECL_4":
                        groups_ECL.append(team2)
                        team1.last_scored=str(b1)+' '+str(k1)
                        team2.last_scored=str(b2)+' '+str(k2)+' pk'
            for i in range(2):
                los = random.randint(0, 10000)
                if los < 8000:
                    b1 = b1 + 1
                elif los > 2000:
                    b2 = b2 + 1
            if b1 > b2:
                if runda=="LM_1":
                    LM_2_list.append(team1)
                    ECL_2_list.append(team2)
                    team1.last_scored=str(b1)+' pd'
                    team2.last_scored=str(b2)
                elif runda=="LM_2":
                    LM_3_list.append(team1)
                    LE_3_list.append(team2)
                    team1.last_scored=str(b1)+' pd'
                    team2.last_scored=str(b2)
                elif runda=="LM_3":
                    LM_4_list.append(team1)
                    LM_3_eliminated.append(team2)
                    team1.last_scored=str(b1)+' pd'
                    team2.last_scored=str(b2)
                elif runda=="LM_4":
                    groups_LM.append(team1)
                    groups_LE.append(team2)
                    team1.last_scored=str(b1)+' pd'
                    team2.last_scored=str(b2)
                elif runda=="LE_3":
                    LE_4_list.append(team1)
                    ECL_4_list.append(team2)
                    team1.last_scored=str(b1)+' pd'
                    team2.last_scored=str(b2)
                elif runda=="LE_4":
                    groups_LE.append(team1)
                    groups_ECL.append(team2)
                    team1.last_scored=str(b1)+' pd'
                    team2.last_scored=str(b2)
                elif runda=="ECL_1":
                    ECL_2_list.append(team1)
                    team1.last_scored=str(b1)+' pd'
                    team2.last_scored=str(b2)
                elif runda=="ECL_2":
                    ECL_3_list.append(team1)
                    team1.last_scored=str(b1)+' pd'
                    team2.last_scored=str(b2)
                elif runda=="ECL_3":
                    ECL_4_list.append(team1)
                    team1.last_scored=str(b1)+' pd'
                    team2.last_scored=str(b2)
                elif runda=="ECL_4":
                    groups_ECL.append(team1)
                    team1.last_scored=str(b1)+' pd'
                    team2.last_scored=str(b2)
            elif b2 > b1:
                if runda=="LM_1":
                    LM_2_list.append(team2)
                    ECL_2_list.append(team1)
                    team1.last_scored=str(b1)
                    team2.last_scored=str(b2)+' pd'
                elif runda=="LM_2":
                    LM_3_list.append(team2)
                    LE_3_list.append(team1)
                    team1.last_scored=str(b1)
                    team2.last_scored=str(b2)+' pd'
                elif runda=="LM_3":
                    LM_4_list.append(team2)
                    LM_3_eliminated.append(team1)
                    team1.last_scored=str(b1)
                    team2.last_scored=str(b2)+' pd'
                elif runda=="LM_4":
                    groups_LM.append(team2)
                    groups_LE.append(team1)
                    team1.last_scored=str(b1)
                    team2.last_scored=str(b2)+' pd'
                elif runda=="LE_3":
                    LE_4_list.append(team2)
                    ECL_4_list.append(team1)
                    team1.last_scored=str(b1)
                    team2.last_scored=str(b2)+' pd'
                elif runda=="LE_4":
                    groups_LE.append(team2)
                    groups_ECL.append(team1)
                    team1.last_scored=str(b1)
                    team2.last_scored=str(b2)+' pd'
                elif runda=="ECL_1":
                    ECL_2_list.append(team2)
                    team1.last_scored=str(b1)
                    team2.last_scored=str(b2)+' pd'
                elif runda=="ECL_2":
                    ECL_3_list.append(team2)
                    team1.last_scored=str(b1)
                    team2.last_scored=str(b2)+' pd'
                elif runda=="ECL_3":
                    ECL_4_list.append(team2)
                    team1.last_scored=str(b1)
                    team2.last_scored=str(b2)+' pd'
                elif runda=="ECL_4":
                    groups_ECL.append(team2)
                    team1.last_scored=str(b1)
                    team2.last_scored=str(b2)+' pd'
            else:
                karne(team1, team2,b1,b2,runda)
        for i in range(10):
            los = random.randint(0, 10000)
            if los < host_limit:
                b1 = b1 + 1
            elif los > guest_limit:
                b2 = b2 + 1
        if b1 > b2:
            if runda=="LM_1":
                LM_2_list.append(team1)
                ECL_2_list.append(team2)
                team1.last_scored=str(b1)
                team2.last_scored=str(b2)
            elif runda=="LM_2":
                LM_3_list.append(team1)
                LE_3_list.append(team2)
                team1.last_scored=str(b1)
                team2.last_scored=str(b2)
            elif runda=="LM_3":
                LM_4_list.append(team1)
                LM_3_eliminated.append(team2)
                team1.last_scored=str(b1)
                team2.last_scored=str(b2)
            elif runda=="LM_4":
                groups_LM.append(team1)
                groups_LE.append(team2)
                team1.last_scored=str(b1)
                team2.last_scored=str(b2)
            elif runda=="LE_3":
                LE_4_list.append(team1)
                ECL_4_list.append(team2)
                team1.last_scored=str(b1)
                team2.last_scored=str(b2)
            elif runda=="LE_4":
                groups_LE.append(team1)
                groups_ECL.append(team2)
                team1.last_scored=str(b1)
                team2.last_scored=str(b2)
            elif runda=="ECL_1":
                ECL_2_list.append(team1)
                team1.last_scored=str(b1)
                team2.last_scored=str(b2)
            elif runda=="ECL_2":
                ECL_3_list.append(team1)
                team1.last_scored=str(b1)
                team2.last_scored=str(b2)
            elif runda=="ECL_3":
                ECL_4_list.append(team1)
                team1.last_scored=str(b1)
                team2.last_scored=str(b2)
            elif runda=="ECL_4":
                groups_ECL.append(team1)
                team1.last_scored=str(b1)
                team2.last_scored=str(b2)
        elif b2 > b1:
            if runda=="LM_1":
                LM_2_list.append(team2)
                ECL_2_list.append(team1)
                team1.last_scored=str(b1)
                team2.last_scored=str(b2)
            elif runda=="LM_2":
                LM_3_list.append(team2)
                LE_3_list.append(team1)
                team1.last_scored=str(b1)
                team2.last_scored=str(b2)
            elif runda=="LM_3":
                LM_4_list.append(team2)
                LM_3_eliminated.append(team1)
                team1.last_scored=str(b1)
                team2.last_scored=str(b2)
            elif runda=="LM_4":
                groups_LM.append(team2)
                groups_LE.append(team1)
                team1.last_scored=str(b1)
                team2.last_scored=str(b2)
            elif runda=="LE_3":
                LE_4_list.append(team2)
                ECL_4_list.append(team1)
                team1.last_scored=str(b1)
                team2.last_scored=str(b2)
            elif runda=="LE_4":
                groups_LE.append(team2)
                groups_ECL.append(team1)
                team1.last_scored=str(b1)
                team2.last_scored=str(b2)
            elif runda=="ECL_1":
                ECL_2_list.append(team2)
                team1.last_scored=str(b1)
                team2.last_scored=str(b2)
            elif runda=="ECL_2":
                ECL_3_list.append(team2)
                team1.last_scored=str(b1)
                team2.last_scored=str(b2)
            elif runda=="ECL_3":
                ECL_4_list.append(team2)
                team1.last_scored=str(b1)
                team2.last_scored=str(b2)
            elif runda=="ECL_4":
                groups_ECL.append(team2)
                team1.last_scored=str(b1)
                team2.last_scored=str(b2)
        else:
            dogrywka(team1, team2,b1,b2,runda)

    #1 runda LM
    file_handle = open("static/LM_1.txt")
    lines = file_handle.readlines()
    random.shuffle(lines)
    for i in lines:
        eval(i)
    LM_1_list = list(Elim_LM_1.objects.all())
    for i in range(17):
        match(LM_1_list[2*i],LM_1_list[2*i+1],"LM_1")
        LM_1_list[2*i].save()
        LM_1_list[2*i+1].save()

    #2 runda LM
    file_handle = open("static/LM_2.txt")
    lines = file_handle.readlines()
    random.shuffle(lines)
    for i in lines:
        eval(i)
    LM_2_list = list(Elim_LM_2.objects.all())
    for i in range(13):
        match(LM_2_list[2*i],LM_2_list[2*i+1],"LM_2")
        LM_2_list[2*i].save()
        LM_2_list[2*i+1].save()

    #3 runda LM
    file_handle = open("static/LM_3.txt")
    lines = file_handle.readlines()
    random.shuffle(lines)
    for i in lines:
        eval(i)
    LM_3_list = list(Elim_LM_3.objects.all())
    for i in range(10):
        match(LM_3_list[2*i],LM_3_list[2*i+1],"LM_3")
        LM_3_list[2*i].save()
        LM_3_list[2*i+1].save()

    #4 runda LM
    random.shuffle(LM_3_eliminated)
    for i in range(6):
        LE_4_list.append(LM_3_eliminated[i])
    for i in range(6,10):
        groups_LE.append(LM_3_eliminated[i])
    file_handle = open("static/LM_4.txt")
    lines = file_handle.readlines()
    random.shuffle(lines)
    for i in lines:
        eval(i)
    LM_4_list = list(Elim_LM_4.objects.all())
    for i in range(6):
        match(LM_4_list[2*i],LM_4_list[2*i+1],"LM_4")
        LM_4_list[2*i].save()
        LM_4_list[2*i+1].save()

    #3 runda LE
    file_handle = open("static/LE_3.txt")
    lines = file_handle.readlines()
    random.shuffle(lines)
    for i in lines:
        eval(i)
    LE_3_list = list(Elim_LE_3.objects.all())
    for i in range(8):
        match(LE_3_list[2*i],LE_3_list[2*i+1],"LE_3")
        LE_3_list[2*i].save()
        LE_3_list[2*i+1].save()

    #4 runda LE
    file_handle = open("static/LE_4.txt")
    lines = file_handle.readlines()
    random.shuffle(lines)
    for i in lines:
        eval(i)
    LE_4_list = list(Elim_LE_4.objects.all())
    for i in range(10):
        match(LE_4_list[2*i],LE_4_list[2*i+1],"LE_4")
        LE_4_list[2*i].save()
        LE_4_list[2*i+1].save()

    #1 runda ECL
    file_handle = open("static/ECL_1.txt")
    lines = file_handle.readlines()
    random.shuffle(lines)
    for i in lines:
        eval(i)
    ECL_1_list = list(Elim_ECL_1.objects.all())
    for i in range(36):
        match(ECL_1_list[2*i],ECL_1_list[2*i+1],"ECL_1")
        ECL_1_list[2*i].save()
        ECL_1_list[2*i+1].save()

    #2 runda ECL
    file_handle = open("static/ECL_2.txt")
    lines = file_handle.readlines()
    random.shuffle(lines)
    for i in lines:
        eval(i)
    ECL_2_list = list(Elim_ECL_2.objects.all())
    for i in range(55):
        match(ECL_2_list[2*i],ECL_2_list[2*i+1],"ECL_2")
        ECL_2_list[2*i].save()
        ECL_2_list[2*i+1].save()

    #3 runda ECL
    file_handle = open("static/ECL_3.txt")
    lines = file_handle.readlines()
    random.shuffle(lines)
    for i in lines:
        eval(i)
    ECL_3_list = list(Elim_ECL_3.objects.all())
    for i in range(31):
        match(ECL_3_list[2*i],ECL_3_list[2*i+1],"ECL_3")
        ECL_3_list[2*i].save()
        ECL_3_list[2*i+1].save()

    #4 runda ECL
    file_handle = open("static/ECL_4.txt")
    lines = file_handle.readlines()
    random.shuffle(lines)
    for i in lines:
        eval(i)
    ECL_4_list = list(Elim_ECL_4.objects.all())
    for i in range(22):
        match(ECL_4_list[2*i],ECL_4_list[2*i+1],"ECL_4")
        ECL_4_list[2*i].save()
        ECL_4_list[2*i+1].save()

    #dodanie drużyn do fazy grupowej
    file_handle = open("static/groups_LM.txt")
    lines = file_handle.readlines()
    random.shuffle(lines)
    for i in lines:
        eval(i)
    file_handle = open("static/groups_LE.txt")
    lines = file_handle.readlines()
    random.shuffle(lines)
    for i in lines:
        eval(i)
    file_handle = open("static/groups_ECL.txt")
    lines = file_handle.readlines()
    random.shuffle(lines)
    for i in lines:
        eval(i)

    date_dict =  {'europa_insert':'coś tam'}
    return render(request,'first_app/europa.html',context=date_dict)
def europa_season(request):
    LM_list = LM_group.objects.all()
    LE_list = LE_group.objects.all()
    ECL_list = ECL_group.objects.all()
    LM_A = list(LM_list[:4])
    LM_B = list(LM_list[4:8])
    LM_C = list(LM_list[8:12])
    LM_D = list(LM_list[12:16])
    LM_E = list(LM_list[16:20])
    LM_F = list(LM_list[20:24])
    LM_G = list(LM_list[24:28])
    LM_H = list(LM_list[28:])

    LE_A = list(LE_list[:4])
    LE_B = list(LE_list[4:8])
    LE_C = list(LE_list[8:12])
    LE_D = list(LE_list[12:16])
    LE_E = list(LE_list[16:20])
    LE_F = list(LE_list[20:24])
    LE_G = list(LE_list[24:28])
    LE_H = list(LE_list[28:])

    ECL_A = list(ECL_list[:4])
    ECL_B = list(ECL_list[4:8])
    ECL_C = list(ECL_list[8:12])
    ECL_D = list(ECL_list[12:16])
    ECL_E = list(ECL_list[16:20])
    ECL_F = list(ECL_list[20:24])
    ECL_G = list(ECL_list[24:28])
    ECL_H = list(ECL_list[28:])

    LM_1_8_list = []
    LM_cwiercfinal_list = []
    LM_polfinal_list = []
    LM_final_list = []
    LM_winner_list = []
    LE_1_16_list = []
    LE_1_8_list = []
    LE_cwiercfinal_list = []
    LE_polfinal_list = []
    LE_final_list = []
    LE_winner_list = []
    ECL_1_16_list = []
    ECL_1_8_list = []
    ECL_cwiercfinal_list = []
    ECL_polfinal_list = []
    ECL_final_list = []
    ECL_winner_list = []
    def mecz_ligowy(team1,team2):
        host_limit = team1.strength
        guest_limit = 10000 - team2.strength
        b1=0
        b2=0
        for i in range(10):
            los = random.randint(0, 10000)
            if los < host_limit:
                b1 = b1 + 1
            elif los > guest_limit:
                b2 = b2 + 1
        if b1 > b2:
            team1.points = team1.points + 3
            team1.wins = team1.wins + 1
            team2.loses = team2.loses + 1
        elif b2 > b1:
            team2.points = team2.points + 3
            team2.wins = team2.wins + 1
            team1.loses = team1.loses + 1
        else:
            team2.points = team2.points + 1
            team1.points = team1.points + 1
            team1.draws = team1.draws + 1
            team2.draws = team2.draws + 1
        team1.scored = team1.scored + b1
        team1.conceded = team1.conceded + b2
        team2.scored = team2.scored + b2
        team2.conceded = team2.conceded + b1
    def mecz_pucharowy_1(team1,team2,runda):
        host_limit = team1.strength
        guest_limit = 10000 - team2.strength
        b1=0
        b2=0
        for i in range(10):
            los = random.randint(0, 10000)
            if los < host_limit:
                b1 = b1 + 1
            elif los > guest_limit:
                b2 = b2 + 1
        team1.last_scored = str(b1)
        team2.last_scored = str(b2)
    def mecz_pucharowy_2(team1,team2,runda):
        host_limit = team1.strength
        guest_limit = 10000 - team2.strength
        b1=0
        b2=0
        def dogrywka(team1, team2,b1,b2,runda):
            def karne(team1, team2,b1,b2,runda):
                k1=0
                k2=0
                for i in range(1,6):
                    los1 = random.randint(0, 100)
                    los2 = random.randint(0, 100)
                    if los1 < 75:
                        k1 = k1 + 1
                    elif los2 > 25:
                        k2 = k2 + 1
                while k1 == k2:
                    los1 = random.randint(0, 100)
                    los2 = random.randint(0, 100)
                    if los1 < 75:
                        k1 = k1 + 1
                    elif los2 > 25:
                        k2 = k2 + 1
                if k1 > k2:
                    if runda=="LM_1_8":
                        LM_cwiercfinal_list.append(team1)
                    elif runda=="LM_cwiercfinal":
                        LM_polfinal_list.append(team1)
                    elif runda=="LM_polfinal":
                        LM_final_list.append(team1)
                    elif runda=="LE_1_16":
                        LE_1_8_list.append(team1)
                    elif runda=="LE_1_8":
                        LE_cwiercfinal_list.append(team1)
                    elif runda=="LE_cwiercfinal":
                        LE_polfinal_list.append(team1)
                    elif runda=="LE_polfinal":
                        LE_final_list.append(team1)
                    elif runda=="ECL_1_16":
                        ECL_1_8_list.append(team1)
                    elif runda=="ECL_1_8":
                        ECL_cwiercfinal_list.append(team1)
                    elif runda=="ECL_cwiercfinal":
                        ECL_polfinal_list.append(team1)
                    elif runda=="ECL_polfinal":
                        ECL_final_list.append(team1)
                    team1.last_scored_2=str(b1)+' '+str(k1)+' pk'
                    team2.last_scored_2=str(b2)+' '+str(k2)
                elif k2 > k1:
                    if runda=="LM_1_8":
                        LM_cwiercfinal_list.append(team2)
                    elif runda=="LM_cwiercfinal":
                        LM_polfinal_list.append(team2)
                    elif runda=="LM_polfinal":
                        LM_final_list.append(team2)
                    elif runda=="LE_1_16":
                        LE_1_8_list.append(team2)
                    elif runda=="LE_1_8":
                        LE_cwiercfinal_list.append(team2)
                    elif runda=="LE_cwiercfinal":
                        LE_polfinal_list.append(team2)
                    elif runda=="LE_polfinal":
                        LE_final_list.append(team2)
                    elif runda=="ECL_1_16":
                        ECL_1_8_list.append(team2)
                    elif runda=="ECL_1_8":
                        ECL_cwiercfinal_list.append(team2)
                    elif runda=="ECL_cwiercfinal":
                        ECL_polfinal_list.append(team2)
                    elif runda=="ECL_polfinal":
                        ECL_final_list.append(team2)
                    team1.last_scored_2=str(b1)+' '+str(k1)
                    team2.last_scored_2=str(b2)+' '+str(k2)+' pk'
            for i in range(2):
                los = random.randint(0, 10000)
                if los > 8000:
                    b1 = b1 + 1
                elif los < 2000:
                    b2 = b2 + 1
            gole1 = b1 + int(team1.last_scored)
            gole2 = b2 + int(team2.last_scored)
            if gole1 > gole2:
                if runda=="LM_1_8":
                    LM_cwiercfinal_list.append(team1)
                elif runda=="LM_cwiercfinal":
                    LM_polfinal_list.append(team1)
                elif runda=="LM_polfinal":
                    LM_final_list.append(team1)
                elif runda=="LE_1_16":
                    LE_1_8_list.append(team1)
                elif runda=="LE_1_8":
                    LE_cwiercfinal_list.append(team1)
                elif runda=="LE_cwiercfinal":
                    LE_polfinal_list.append(team1)
                elif runda=="LE_polfinal":
                    LE_final_list.append(team1)
                elif runda=="ECL_1_16":
                    ECL_1_8_list.append(team1)
                elif runda=="ECL_1_8":
                    ECL_cwiercfinal_list.append(team1)
                elif runda=="ECL_cwiercfinal":
                    ECL_polfinal_list.append(team1)
                elif runda=="ECL_polfinal":
                    ECL_final_list.append(team1)
                team1.last_scored_2=str(b1)+' pd'
                team2.last_scored_2=str(b2)
            elif gole1 < gole2:
                if runda=="LM_1_8":
                    LM_cwiercfinal_list.append(team2)
                elif runda=="LM_cwiercfinal":
                    LM_polfinal_list.append(team2)
                elif runda=="LM_polfinal":
                    LM_final_list.append(team2)
                elif runda=="LE_1_16":
                    LE_1_8_list.append(team2)
                elif runda=="LE_1_8":
                    LE_cwiercfinal_list.append(team2)
                elif runda=="LE_cwiercfinal":
                    LE_polfinal_list.append(team2)
                elif runda=="LE_polfinal":
                    LE_final_list.append(team2)
                elif runda=="ECL_1_16":
                    ECL_1_8_list.append(team2)
                elif runda=="ECL_1_8":
                    ECL_cwiercfinal_list.append(team2)
                elif runda=="ECL_cwiercfinal":
                    ECL_polfinal_list.append(team2)
                elif runda=="ECL_polfinal":
                    ECL_final_list.append(team2)
                team1.last_scored_2=str(b1)
                team2.last_scored_2=str(b2)+' pd'
            else:
                if int(team1.last_scored) + 2*b1 > 2*int(team2.last_scored) + b2:
                    if runda=="LM_1_8":
                        LM_cwiercfinal_list.append(team1)
                    elif runda=="LM_cwiercfinal":
                        LM_polfinal_list.append(team1)
                    elif runda=="LM_polfinal":
                        LM_final_list.append(team1)
                    elif runda=="LE_1_16":
                        LE_1_8_list.append(team1)
                    elif runda=="LE_1_8":
                        LE_cwiercfinal_list.append(team1)
                    elif runda=="LE_cwiercfinal":
                        LE_polfinal_list.append(team1)
                    elif runda=="LE_polfinal":
                        LE_final_list.append(team1)
                    elif runda=="ECL_1_16":
                        ECL_1_8_list.append(team1)
                    elif runda=="ECL_1_8":
                        ECL_cwiercfinal_list.append(team1)
                    elif runda=="ECL_cwiercfinal":
                        ECL_polfinal_list.append(team1)
                    elif runda=="ECL_polfinal":
                        ECL_final_list.append(team1)
                    team1.last_scored_2=str(b1)
                    team2.last_scored_2=str(b2)
                elif int(team1.last_scored) + 2*b1 < 2*int(team2.last_scored) + b2:
                    if runda=="LM_1_8":
                        LM_cwiercfinal_list.append(team2)
                    elif runda=="LM_cwiercfinal":
                        LM_polfinal_list.append(team2)
                    elif runda=="LM_polfinal":
                        LM_final_list.append(team2)
                    elif runda=="LE_1_16":
                        LE_1_8_list.append(team2)
                    elif runda=="LE_1_8":
                        LE_cwiercfinal_list.append(team2)
                    elif runda=="LE_cwiercfinal":
                        LE_polfinal_list.append(team2)
                    elif runda=="LE_polfinal":
                        LE_final_list.append(team2)
                    elif runda=="ECL_1_16":
                        ECL_1_8_list.append(team2)
                    elif runda=="ECL_1_8":
                        ECL_cwiercfinal_list.append(team2)
                    elif runda=="ECL_cwiercfinal":
                        ECL_polfinal_list.append(team2)
                    elif runda=="ECL_polfinal":
                        ECL_final_list.append(team2)
                    team1.last_scored_2=str(b1)
                    team2.last_scored_2=str(b2)
                else:
                    karne(team1, team2,b1,b2,runda)
        for i in range(10):
            los = random.randint(0, 10000)
            if los < host_limit:
                b1 = b1 + 1
            elif los > guest_limit:
                b2 = b2 + 1
        gole1 = b1 + int(team1.last_scored)
        gole2 = b2 + int(team2.last_scored)
        if gole1 > gole2:
            if runda=="LM_1_8":
                LM_cwiercfinal_list.append(team1)
            elif runda=="LM_cwiercfinal":
                LM_polfinal_list.append(team1)
            elif runda=="LM_polfinal":
                LM_final_list.append(team1)
            elif runda=="LE_1_16":
                LE_1_8_list.append(team1)
            elif runda=="LE_1_8":
                LE_cwiercfinal_list.append(team1)
            elif runda=="LE_cwiercfinal":
                LE_polfinal_list.append(team1)
            elif runda=="LE_polfinal":
                LE_final_list.append(team1)
            elif runda=="ECL_1_16":
                ECL_1_8_list.append(team1)
            elif runda=="ECL_1_8":
                ECL_cwiercfinal_list.append(team1)
            elif runda=="ECL_cwiercfinal":
                ECL_polfinal_list.append(team1)
            elif runda=="ECL_polfinal":
                ECL_final_list.append(team1)
            team1.last_scored_2=str(b1)
            team2.last_scored_2=str(b2)
        elif gole1 < gole2:
            if runda=="LM_1_8":
                LM_cwiercfinal_list.append(team2)
            elif runda=="LM_cwiercfinal":
                LM_polfinal_list.append(team2)
            elif runda=="LM_polfinal":
                LM_final_list.append(team2)
            elif runda=="LE_1_16":
                LE_1_8_list.append(team2)
            elif runda=="LE_1_8":
                LE_cwiercfinal_list.append(team2)
            elif runda=="LE_cwiercfinal":
                LE_polfinal_list.append(team2)
            elif runda=="LE_polfinal":
                LE_final_list.append(team2)
            elif runda=="ECL_1_16":
                ECL_1_8_list.append(team2)
            elif runda=="ECL_1_8":
                ECL_cwiercfinal_list.append(team2)
            elif runda=="ECL_cwiercfinal":
                ECL_polfinal_list.append(team2)
            elif runda=="ECL_polfinal":
                ECL_final_list.append(team2)
            team1.last_scored_2=str(b1)
            team2.last_scored_2=str(b2)
        else:
            if int(team1.last_scored) + 2*b1 > 2*int(team2.last_scored) + b2:
                if runda=="LM_1_8":
                    LM_cwiercfinal_list.append(team1)
                elif runda=="LM_cwiercfinal":
                    LM_polfinal_list.append(team1)
                elif runda=="LM_polfinal":
                    LM_final_list.append(team1)
                elif runda=="LE_1_16":
                    LE_1_8_list.append(team1)
                elif runda=="LE_1_8":
                    LE_cwiercfinal_list.append(team1)
                elif runda=="LE_cwiercfinal":
                    LE_polfinal_list.append(team1)
                elif runda=="LE_polfinal":
                    LE_final_list.append(team1)
                elif runda=="ECL_1_16":
                    ECL_1_8_list.append(team1)
                elif runda=="ECL_1_8":
                    ECL_cwiercfinal_list.append(team1)
                elif runda=="ECL_cwiercfinal":
                    ECL_polfinal_list.append(team1)
                elif runda=="ECL_polfinal":
                    ECL_final_list.append(team1)
                team1.last_scored_2=str(b1)
                team2.last_scored_2=str(b2)
            elif int(team1.last_scored) + 2*b1 < 2*int(team2.last_scored) + b2:
                if runda=="LM_1_8":
                    LM_cwiercfinal_list.append(team2)
                elif runda=="LM_cwiercfinal":
                    LM_polfinal_list.append(team2)
                elif runda=="LM_polfinal":
                    LM_final_list.append(team2)
                elif runda=="LE_1_16":
                    LE_1_8_list.append(team2)
                elif runda=="LE_1_8":
                    LE_cwiercfinal_list.append(team2)
                elif runda=="LE_cwiercfinal":
                    LE_polfinal_list.append(team2)
                elif runda=="LE_polfinal":
                    LE_final_list.append(team2)
                elif runda=="ECL_1_16":
                    ECL_1_8_list.append(team2)
                elif runda=="ECL_1_8":
                    ECL_cwiercfinal_list.append(team2)
                elif runda=="ECL_cwiercfinal":
                    ECL_polfinal_list.append(team2)
                elif runda=="ECL_polfinal":
                    ECL_final_list.append(team2)
                team1.last_scored_2=str(b1)
                team2.last_scored_2=str(b2)
            else:
                dogrywka(team1,team2, b1, b2, runda)
    def final(team1, team2,runda):
        host_limit = team1.strength
        guest_limit = 10000 - team2.strength
        b1=0
        b2=0
        def dogrywka(team1,team2,b1,b2,runda):
            def karne(team1,team2,runda):
                k1=0
                k2=0
                for i in range(1,6):
                    los1 = random.randint(0, 100)
                    los2 = random.randint(0, 100)
                    if los1 < 75:
                        k1 = k1 + 1
                    elif los2 > 25:
                        k2 = k2 + 1
                while k1 == k2:
                    los1 = random.randint(0, 100)
                    los2 = random.randint(0, 100)
                    if los1 < 75:
                        k1 = k1 + 1
                    elif los2 > 25:
                        k2 = k2 + 1
                if k1 > k2:
                    if runda=="ECL_final":
                        ECL_winner_list.append(team1)
                    elif runda=="LM_final":
                        LM_winner_list.append(team1)
                    elif runda=="LE_final":
                        LE_winner_list.append(team1)
                    team1.last_scored=str(b1)+' '+str(k1)+' pk'
                    team2.last_scored=str(b2)+' '+str(k2)
                elif k2 > k1:
                    if runda=="ECL_final":
                        ECL_winner_list.append(team2)
                    elif runda=="LM_final":
                        LM_winner_list.append(team2)
                    elif runda=="LE_final":
                        LE_winner_list.append(team2)
                    team1.last_scored=str(b1)+' '+str(k1)
                    team2.last_scored=str(b2)+' '+str(k2)+' pk'
            for i in range(2):
                los = random.randint(0, 10000)
                if los > 8000:
                    b1 = b1 + 1
                elif los < 2000:
                    b2 = b2 + 1
            if b1 > b2:
                if runda=="ECL_final":
                    ECL_winner_list.append(team1)
                elif runda=="LM_final":
                    LM_winner_list.append(team1)
                elif runda=="LE_final":
                    LE_winner_list.append(team1)
                team1.last_scored=str(b1)+' pd'
                team2.last_scored=str(b2)
            elif b1 < b2:
                if runda=="ECL_final":
                    ECL_winner_list.append(team2)
                elif runda=="LM_final":
                    LM_winner_list.append(team2)
                elif runda=="LE_final":
                    LE_winner_list.append(team2)
                team1.last_scored=str(b1)
                team2.last_scored=str(b2)+' pd'
            else:
                karne(team1,team2,runda)
        for i in range(10):
            los = random.randint(0, 10000)
            if los < host_limit:
                b1 = b1 + 1
            elif los > guest_limit:
                b2 = b2 + 1
        if b1 > b2:
            if runda=="ECL_final":
                ECL_winner_list.append(team1)
            elif runda=="LM_final":
                LM_winner_list.append(team1)
            elif runda=="LE_final":
                LE_winner_list.append(team1)
            team1.last_scored=str(b1)
            team2.last_scored=str(b2)
        elif b2 > b1:
            if runda=="ECL_final":
                ECL_winner_list.append(team2)
            elif runda=="LM_final":
                LM_winner_list.append(team2)
            elif runda=="LE_final":
                LE_winner_list.append(team2)
            team1.last_scored=str(b1)
            team2.last_scored=str(b2)
        else:
            dogrywka(team1,team2,b1,b2,runda)
    def rozegraj_grupe(grupa):
        for i in range(2):
            mecz_ligowy(grupa[0],grupa[1])
            mecz_ligowy(grupa[2],grupa[3])

            mecz_ligowy(grupa[0],grupa[2])
            mecz_ligowy(grupa[1],grupa[3])

            mecz_ligowy(grupa[0],grupa[3])
            mecz_ligowy(grupa[1],grupa[2])
        grupa.sort(key=lambda x:(x.points,x.scored - x.conceded,x.scored),reverse = True)
        for cl in grupa:
            cl.save()

    rozegraj_grupe(LM_A)
    rozegraj_grupe(LM_B)
    rozegraj_grupe(LM_C)
    rozegraj_grupe(LM_D)
    rozegraj_grupe(LM_E)
    rozegraj_grupe(LM_F)
    rozegraj_grupe(LM_G)
    rozegraj_grupe(LM_H)
    rozegraj_grupe(LE_A)
    rozegraj_grupe(LE_B)
    rozegraj_grupe(LE_C)
    rozegraj_grupe(LE_D)
    rozegraj_grupe(LE_E)
    rozegraj_grupe(LE_F)
    rozegraj_grupe(LE_G)
    rozegraj_grupe(LE_H)
    rozegraj_grupe(ECL_A)
    rozegraj_grupe(ECL_B)
    rozegraj_grupe(ECL_C)
    rozegraj_grupe(ECL_D)
    rozegraj_grupe(ECL_E)
    rozegraj_grupe(ECL_F)
    rozegraj_grupe(ECL_G)
    rozegraj_grupe(ECL_H)

    for i in range(2):
        LM_1_8_list.append(LM_A[i])
        LM_1_8_list.append(LM_B[i])
        LM_1_8_list.append(LM_C[i])
        LM_1_8_list.append(LM_D[i])
        LM_1_8_list.append(LM_E[i])
        LM_1_8_list.append(LM_F[i])
        LM_1_8_list.append(LM_G[i])
        LM_1_8_list.append(LM_H[i])

    LE_1_16_list.append(LM_A[2])
    LE_1_16_list.append(LM_B[2])
    LE_1_16_list.append(LM_C[2])
    LE_1_16_list.append(LM_D[2])
    LE_1_16_list.append(LM_E[2])
    LE_1_16_list.append(LM_F[2])
    LE_1_16_list.append(LM_G[2])
    LE_1_16_list.append(LM_H[2])

    LE_1_8_list.append(LE_A[0])
    LE_1_8_list.append(LE_B[0])
    LE_1_8_list.append(LE_C[0])
    LE_1_8_list.append(LE_D[0])
    LE_1_8_list.append(LE_E[0])
    LE_1_8_list.append(LE_F[0])
    LE_1_8_list.append(LE_G[0])
    LE_1_8_list.append(LE_H[0])
    LE_1_16_list.append(LE_A[1])
    LE_1_16_list.append(LE_B[1])
    LE_1_16_list.append(LE_C[1])
    LE_1_16_list.append(LE_D[1])
    LE_1_16_list.append(LE_E[1])
    LE_1_16_list.append(LE_F[1])
    LE_1_16_list.append(LE_G[1])
    LE_1_16_list.append(LE_H[1])
    ECL_1_16_list.append(LE_A[2])
    ECL_1_16_list.append(LE_B[2])
    ECL_1_16_list.append(LE_C[2])
    ECL_1_16_list.append(LE_D[2])
    ECL_1_16_list.append(LE_E[2])
    ECL_1_16_list.append(LE_F[2])
    ECL_1_16_list.append(LE_G[2])
    ECL_1_16_list.append(LE_H[2])
    ECL_1_8_list.append(ECL_A[0])
    ECL_1_8_list.append(ECL_B[0])
    ECL_1_8_list.append(ECL_C[0])
    ECL_1_8_list.append(ECL_D[0])
    ECL_1_8_list.append(ECL_E[0])
    ECL_1_8_list.append(ECL_F[0])
    ECL_1_8_list.append(ECL_G[0])
    ECL_1_8_list.append(ECL_H[0])
    ECL_1_16_list.append(ECL_A[1])
    ECL_1_16_list.append(ECL_B[1])
    ECL_1_16_list.append(ECL_C[1])
    ECL_1_16_list.append(ECL_D[1])
    ECL_1_16_list.append(ECL_E[1])
    ECL_1_16_list.append(ECL_F[1])
    ECL_1_16_list.append(ECL_G[1])
    ECL_1_16_list.append(ECL_H[1])
    t=[]
    #1/16 ECL
    file_handle = open("static/LE_1_16.txt")
    lines = file_handle.readlines()
    random.shuffle(lines)
    for i in lines:
        eval(i)
    LE_1_16_list = list(LE_1_16.objects.all())
    for i in range(8):
        mecz_pucharowy_1(LE_1_16_list[2*i],LE_1_16_list[2*i+1],"LE_1_16")
        mecz_pucharowy_2(LE_1_16_list[2*i],LE_1_16_list[2*i+1],"LE_1_16")
        LE_1_16_list[2*i].save()
        LE_1_16_list[2*i+1].save()

    #1/16 ECL
    file_handle = open("static/ECL_1_16.txt")
    lines = file_handle.readlines()
    random.shuffle(lines)
    for i in lines:
        eval(i)
    ECL_1_16_list = list(ECL_1_16.objects.all())
    for i in range(8):
        mecz_pucharowy_1(ECL_1_16_list[2*i],ECL_1_16_list[2*i+1],"ECL_1_16")
        mecz_pucharowy_2(ECL_1_16_list[2*i],ECL_1_16_list[2*i+1],"ECL_1_16")
        ECL_1_16_list[2*i].save()
        ECL_1_16_list[2*i+1].save()

    #1/8 LM
    file_handle = open("static/LM_1_8.txt")
    lines = file_handle.readlines()
    random.shuffle(lines)
    for i in lines:
        eval(i)
    LM_1_8_list = list(LM_1_8.objects.all())
    for i in range(8):
        mecz_pucharowy_1(LM_1_8_list[2*i],LM_1_8_list[2*i+1],"LM_1_8")
        mecz_pucharowy_2(LM_1_8_list[2*i],LM_1_8_list[2*i+1],"LM_1_8")
        LM_1_8_list[2*i].save()
        LM_1_8_list[2*i+1].save()

    #1/8 LE
    file_handle = open("static/LE_1_8.txt")
    lines = file_handle.readlines()
    random.shuffle(lines)
    for i in lines:
        eval(i)
    LE_1_8_list = list(LE_1_8.objects.all())
    for i in range(8):
        mecz_pucharowy_1(LE_1_8_list[2*i],LE_1_8_list[2*i+1],"LE_1_8")
        mecz_pucharowy_2(LE_1_8_list[2*i],LE_1_8_list[2*i+1],"LE_1_8")
        LE_1_8_list[2*i].save()
        LE_1_8_list[2*i+1].save()

    #1/8 ECL
    file_handle = open("static/ECL_1_8.txt")
    lines = file_handle.readlines()
    random.shuffle(lines)
    for i in lines:
        eval(i)
    ECL_1_8_list = list(ECL_1_8.objects.all())
    for i in range(8):
        mecz_pucharowy_1(ECL_1_8_list[2*i],ECL_1_8_list[2*i+1],"ECL_1_8")
        mecz_pucharowy_2(ECL_1_8_list[2*i],ECL_1_8_list[2*i+1],"ECL_1_8")
        ECL_1_8_list[2*i].save()
        ECL_1_8_list[2*i+1].save()

    #1/4 LM
    file_handle = open("static/LM_cwiercfinal.txt")
    lines = file_handle.readlines()
    random.shuffle(lines)
    for i in lines:
        eval(i)
    LM_cwiercfinal_list = list(LM_cwiercfinal.objects.all())
    for i in range(4):
        mecz_pucharowy_1(LM_cwiercfinal_list[2*i],LM_cwiercfinal_list[2*i+1],"LM_cwiercfinal")
        mecz_pucharowy_2(LM_cwiercfinal_list[2*i],LM_cwiercfinal_list[2*i+1],"LM_cwiercfinal")
        LM_cwiercfinal_list[2*i].save()
        LM_cwiercfinal_list[2*i+1].save()

    #1/4 LE
    file_handle = open("static/LE_cwiercfinal.txt")
    lines = file_handle.readlines()
    random.shuffle(lines)
    for i in lines:
        eval(i)
    LE_cwiercfinal_list = list(LE_cwiercfinal.objects.all())
    for i in range(4):
        mecz_pucharowy_1(LE_cwiercfinal_list[2*i],LE_cwiercfinal_list[2*i+1],"LE_cwiercfinal")
        mecz_pucharowy_2(LE_cwiercfinal_list[2*i],LE_cwiercfinal_list[2*i+1],"LE_cwiercfinal")
        LE_cwiercfinal_list[2*i].save()
        LE_cwiercfinal_list[2*i+1].save()

    #1/4 ECL
    file_handle = open("static/ECL_cwiercfinal.txt")
    lines = file_handle.readlines()
    random.shuffle(lines)
    for i in lines:
        eval(i)
    ECL_cwiercfinal_list = list(ECL_cwiercfinal.objects.all())
    for i in range(4):
        mecz_pucharowy_1(ECL_cwiercfinal_list[2*i],ECL_cwiercfinal_list[2*i+1],"ECL_cwiercfinal")
        mecz_pucharowy_2(ECL_cwiercfinal_list[2*i],ECL_cwiercfinal_list[2*i+1],"ECL_cwiercfinal")
        ECL_cwiercfinal_list[2*i].save()
        ECL_cwiercfinal_list[2*i+1].save()

    #1/2 LM
    file_handle = open("static/LM_polfinal.txt")
    lines = file_handle.readlines()
    random.shuffle(lines)
    for i in lines:
        eval(i)
    LM_polfinal_list = list(LM_polfinal.objects.all())
    for i in range(2):
        mecz_pucharowy_1(LM_polfinal_list[2*i],LM_polfinal_list[2*i+1],"LM_polfinal")
        mecz_pucharowy_2(LM_polfinal_list[2*i],LM_polfinal_list[2*i+1],"LM_polfinal")
        LM_polfinal_list[2*i].save()
        LM_polfinal_list[2*i+1].save()

    #1/2 LE
    file_handle = open("static/LE_polfinal.txt")
    lines = file_handle.readlines()
    random.shuffle(lines)
    for i in lines:
        eval(i)
    LE_polfinal_list = list(LE_polfinal.objects.all())
    for i in range(2):
        mecz_pucharowy_1(LE_polfinal_list[2*i],LE_polfinal_list[2*i+1],"LE_polfinal")
        mecz_pucharowy_2(LE_polfinal_list[2*i],LE_polfinal_list[2*i+1],"LE_polfinal")
        LE_polfinal_list[2*i].save()
        LE_polfinal_list[2*i+1].save()

    #1/2 ECL
    file_handle = open("static/ECL_polfinal.txt")
    lines = file_handle.readlines()
    random.shuffle(lines)
    for i in lines:
        eval(i)
    ECL_polfinal_list = list(ECL_polfinal.objects.all())
    for i in range(2):
        mecz_pucharowy_1(ECL_polfinal_list[2*i],ECL_polfinal_list[2*i+1],"ECL_polfinal")
        mecz_pucharowy_2(ECL_polfinal_list[2*i],ECL_polfinal_list[2*i+1],"ECL_polfinal")
        ECL_polfinal_list[2*i].save()
        ECL_polfinal_list[2*i+1].save()

    #finały
    LM_final.objects.create(name=LM_final_list[0].name,image=LM_final_list[0].image,last_scored = LM_final_list[0].last_scored,country=LM_final_list[0].country)
    LE_final.objects.create(name=LE_final_list[0].name,image=LE_final_list[0].image,last_scored = LE_final_list[0].last_scored,country=LE_final_list[0].country)
    ECL_final.objects.create(name=ECL_final_list[0].name,image=ECL_final_list[0].image,last_scored = ECL_final_list[0].last_scored,country=ECL_final_list[0].country)
    LM_final.objects.create(name=LM_final_list[1].name,image=LM_final_list[1].image,last_scored = LM_final_list[1].last_scored,country=LM_final_list[1].country)
    LE_final.objects.create(name=LE_final_list[1].name,image=LE_final_list[1].image,last_scored = LE_final_list[1].last_scored,country=LE_final_list[1].country)
    ECL_final.objects.create(name=ECL_final_list[1].name,image=ECL_final_list[1].image,last_scored = ECL_final_list[1].last_scored,country=ECL_final_list[1].country)
    ECL_final_list = list(ECL_final.objects.all())
    LE_final_list = list(LE_final.objects.all())
    LM_final_list = list(LM_final.objects.all())

    final(ECL_final_list[0],ECL_final_list[1],'ECL_final')
    final(LM_final_list[0],LM_final_list[1],'LM_final')
    final(LE_final_list[0],LE_final_list[1],'LE_final')
    for i in range(2):
        LM_final_list[i].save()
        LE_final_list[i].save()
        ECL_final_list[i].save()
    LM_winner.objects.create(name=LM_winner_list[0].name,image=LM_winner_list[0].image,country=LM_winner_list[0].country)
    LE_winner.objects.create(name=LE_winner_list[0].name,image=LE_winner_list[0].image,country=LE_winner_list[0].country)
    ECL_winner.objects.create(name=ECL_winner_list[0].name,image=ECL_winner_list[0].image,country=ECL_winner_list[0].country)

    LM_gallery.objects.create(name=LM_winner_list[0].name,image=LM_winner_list[0].image,country=LM_winner_list[0].country)
    LE_gallery.objects.create(name=LE_winner_list[0].name,image=LE_winner_list[0].image,country=LE_winner_list[0].country)
    ECL_gallery.objects.create(name=ECL_winner_list[0].name,image=ECL_winner_list[0].image,country=ECL_winner_list[0].country)

    date_dict =  {'europa_insert':'Panel rozgrywek europejskich'}
    return render(request,'first_app/europa.html',context=date_dict)
def LM(request):
    LM_group_team = LM_group.objects.all()
    LM_list = list(LM_group_team)
    LM_A = LM_list[:4]
    LM_A.sort(key=lambda x:(x.points,x.scored - x.conceded,x.scored),reverse = True)
    LM_B = LM_list[4:8]
    LM_B.sort(key=lambda x:(x.points,x.scored - x.conceded,x.scored),reverse = True)
    LM_C = LM_list[8:12]
    LM_C.sort(key=lambda x:(x.points,x.scored - x.conceded,x.scored),reverse = True)
    LM_D = LM_list[12:16]
    LM_D.sort(key=lambda x:(x.points,x.scored - x.conceded,x.scored),reverse = True)
    LM_E = LM_list[16:20]
    LM_E.sort(key=lambda x:(x.points,x.scored - x.conceded,x.scored),reverse = True)
    LM_F = LM_list[20:24]
    LM_F.sort(key=lambda x:(x.points,x.scored - x.conceded,x.scored),reverse = True)
    LM_G = LM_list[24:28]
    LM_G.sort(key=lambda x:(x.points,x.scored - x.conceded,x.scored),reverse = True)
    LM_H = LM_list[28:]
    LM_H.sort(key=lambda x:(x.points,x.scored - x.conceded,x.scored),reverse = True)
    LM_1_8_teams = LM_1_8.objects.all()
    LM_cwiercfinal_teams = LM_cwiercfinal.objects.all()
    LM_polfinal_teams = LM_polfinal.objects.all()
    LM_final_teams = LM_final.objects.all()
    LM_winner_teams = LM_winner.objects.all()
    dict = {'LM_A_records':LM_A,'LM_B_records':LM_B,'LM_C_records':LM_C,'LM_D_records':LM_D,'LM_E_records':LM_E,'LM_F_records':LM_F,'LM_G_records':LM_G,'LM_H_records':LM_H,
    'LM_1_8_records':LM_1_8_teams,'LM_cwiercfinal_records':LM_cwiercfinal_teams,'LM_polfinal_records':LM_polfinal_teams,'LM_final_records':LM_final_teams,'LM_winner_records':LM_winner_teams}
    return render(request,'first_app/LM.html',context=dict)
def LE(request):
    LE_group_team = LE_group.objects.all()
    LE_list = list(LE_group_team)
    LE_A = LE_list[:4]
    LE_A.sort(key=lambda x:(x.points,x.scored - x.conceded,x.scored),reverse = True)
    LE_B = LE_list[4:8]
    LE_B.sort(key=lambda x:(x.points,x.scored - x.conceded,x.scored),reverse = True)
    LE_C = LE_list[8:12]
    LE_C.sort(key=lambda x:(x.points,x.scored - x.conceded,x.scored),reverse = True)
    LE_D = LE_list[12:16]
    LE_D.sort(key=lambda x:(x.points,x.scored - x.conceded,x.scored),reverse = True)
    LE_E = LE_list[16:20]
    LE_E.sort(key=lambda x:(x.points,x.scored - x.conceded,x.scored),reverse = True)
    LE_F = LE_list[20:24]
    LE_F.sort(key=lambda x:(x.points,x.scored - x.conceded,x.scored),reverse = True)
    LE_G = LE_list[24:28]
    LE_G.sort(key=lambda x:(x.points,x.scored - x.conceded,x.scored),reverse = True)
    LE_H = LE_list[28:]
    LE_H.sort(key=lambda x:(x.points,x.scored - x.conceded,x.scored),reverse = True)
    LE_1_16_teams = LE_1_16.objects.all()
    LE_1_8_teams = LE_1_8.objects.all()
    LE_cwiercfinal_teams = LE_cwiercfinal.objects.all()
    LE_polfinal_teams = LE_polfinal.objects.all()
    LE_final_teams = LE_final.objects.all()
    LE_winner_teams = LE_winner.objects.all()
    dict = {'LE_A_records':LE_A,'LE_B_records':LE_B,'LE_C_records':LE_C,'LE_D_records':LE_D,'LE_E_records':LE_E,'LE_F_records':LE_F,'LE_G_records':LE_G,'LE_H_records':LE_H,
    'LE_1_16_records':LE_1_16_teams,'LE_1_8_records':LE_1_8_teams,'LE_cwiercfinal_records':LE_cwiercfinal_teams,'LE_polfinal_records':LE_polfinal_teams,'LE_final_records':LE_final_teams,'LE_winner_records':LE_winner_teams}
    return render(request,'first_app/LE.html',context=dict)
def ECL(request):
    ECL_group_team = ECL_group.objects.all()
    ECL_list = list(ECL_group_team)
    ECL_A = ECL_list[:4]
    ECL_A.sort(key=lambda x:(x.points,x.scored - x.conceded,x.scored),reverse = True)
    ECL_B = ECL_list[4:8]
    ECL_B.sort(key=lambda x:(x.points,x.scored - x.conceded,x.scored),reverse = True)
    ECL_C = ECL_list[8:12]
    ECL_C.sort(key=lambda x:(x.points,x.scored - x.conceded,x.scored),reverse = True)
    ECL_D = ECL_list[12:16]
    ECL_D.sort(key=lambda x:(x.points,x.scored - x.conceded,x.scored),reverse = True)
    ECL_E = ECL_list[16:20]
    ECL_E.sort(key=lambda x:(x.points,x.scored - x.conceded,x.scored),reverse = True)
    ECL_F = ECL_list[20:24]
    ECL_F.sort(key=lambda x:(x.points,x.scored - x.conceded,x.scored),reverse = True)
    ECL_G = ECL_list[24:28]
    ECL_G.sort(key=lambda x:(x.points,x.scored - x.conceded,x.scored),reverse = True)
    ECL_H = ECL_list[28:]
    ECL_H.sort(key=lambda x:(x.points,x.scored - x.conceded,x.scored),reverse = True)
    ECL_1_16_teams = ECL_1_16.objects.all()
    ECL_1_8_teams = ECL_1_8.objects.all()
    ECL_cwiercfinal_teams = ECL_cwiercfinal.objects.all()
    ECL_polfinal_teams = ECL_polfinal.objects.all()
    ECL_final_teams = ECL_final.objects.all()
    ECL_winner_teams = ECL_winner.objects.all()
    dict = {'ECL_A_records':ECL_A,'ECL_B_records':ECL_B,'ECL_C_records':ECL_C,'ECL_D_records':ECL_D,'ECL_E_records':ECL_E,'ECL_F_records':ECL_F,'ECL_G_records':ECL_G,'ECL_H_records':ECL_H,
    'ECL_1_16_records':ECL_1_16_teams,'ECL_1_8_records':ECL_1_8_teams,'ECL_cwiercfinal_records':ECL_cwiercfinal_teams,'ECL_polfinal_records':ECL_polfinal_teams,'ECL_final_records':ECL_final_teams,'ECL_winner_records':ECL_winner_teams}
    return render(request,'first_app/ECL.html',context=dict)

def spadek(request):
    ekst_list = Ekstraklasa.objects.order_by('-points','-difference','-scored')
    pliga_list = Pierwsza_Liga.objects.order_by('-points','-difference','-scored')
    dliga_list = Druga_Liga.objects.order_by('-points','-difference','-scored')
    ekst_list_spadek = Ekstraklasa.objects.order_by('-points','-difference','-scored')[13:]
    pliga_list_awans = Pierwsza_Liga.objects.order_by('-points','-difference','-scored')[:3]
    pliga_list_spadek = Pierwsza_Liga.objects.order_by('-points','-difference','-scored')[15:]
    dliga_list_awans = Druga_Liga.objects.order_by('-points','-difference','-scored')[:3]
    temp_eks = ekst_list_spadek
    temp_pliga_awans = pliga_list_awans
    temp_pliga_spadek = pliga_list_spadek
    temp_dliga_awans = dliga_list_awans
    Ekstraklasa.objects.create(name=pliga_list_awans[0].name,image=pliga_list_awans[0].image,country = pliga_list_awans[0].country)
    Ekstraklasa.objects.create(name=pliga_list_awans[1].name,image=pliga_list_awans[1].image,country = pliga_list_awans[0].country)
    Ekstraklasa.objects.create(name=pliga_list_awans[2].name,image=pliga_list_awans[2].image,country = pliga_list_awans[0].country)
    Pierwsza_Liga.objects.create(name=temp_eks[0].name,image=temp_eks[0].image,country = pliga_list_awans[0].country)
    Pierwsza_Liga.objects.create(name=temp_eks[1].name,image=temp_eks[1].image,country = pliga_list_awans[0].country)
    Pierwsza_Liga.objects.create(name=temp_eks[2].name,image=temp_eks[2].image,country = pliga_list_awans[0].country)
    Pierwsza_Liga.objects.create(name=temp_dliga_awans[0].name,image=temp_dliga_awans[0].image,country = pliga_list_awans[0].country)
    Pierwsza_Liga.objects.create(name=temp_dliga_awans[1].name,image=temp_dliga_awans[1].image,country = pliga_list_awans[0].country)
    Pierwsza_Liga.objects.create(name=temp_dliga_awans[2].name,image=temp_dliga_awans[2].image,country = pliga_list_awans[0].country)
    Druga_Liga.objects.create(name=temp_pliga_spadek[0].name,image=temp_pliga_spadek[0].image,country = pliga_list_awans[0].country)
    Druga_Liga.objects.create(name=temp_pliga_spadek[1].name,image=temp_pliga_spadek[1].image,country = pliga_list_awans[0].country)
    Druga_Liga.objects.create(name=temp_pliga_spadek[2].name,image=temp_pliga_spadek[2].image,country = pliga_list_awans[0].country)
    for i in range(3):
        ekst_list[13].delete()
        pliga_list[0].delete()
        dliga_list[0].delete()
    for i in range(3):
        pliga_list[12].delete()
    all_dict = {'ekst_records':ekst_list,'pier_liga_records':pliga_list,'drug_liga_records':dliga_list}
    return render(request,'first_app/index.html',context=all_dict)
def ekstraklasa(request):
    ekst_list = Ekstraklasa.objects.order_by('-points','-difference','-scored')
    date_dict = {'ekst_records':ekst_list}
    return render(request,'first_app/podglad_ligi.html',context=date_dict)
def puchar_polski(request):

    ekst_list = Ekstraklasa.objects.all()
    pliga_list = Pierwsza_Liga.objects.all()
    dliga_list = Druga_Liga.objects.order_by('-points','-difference','-scored')[0:14]
    x1=list(ekst_list)
    x2=list(pliga_list)
    x3=list(dliga_list)
    for i in range(18):
        x1.append(x2[i])
        if i<14:
            x1.append(x3[i])
    runda_1 = x1[16:]
    random.shuffle(runda_1)
    runda_2 = x1[0:16]
    random.shuffle(runda_2)
    runda_3 = []
    cwiercfinal=[]
    polfinal=[]
    final=[]
    winner = []
    wyniki_runda_1=[]
    wyniki_runda_2=[]
    wyniki_runda_3=[]
    wyniki_cwiercfinal=[]
    wyniki_polfinal=[]
    wyniki_final=[]
    def match(team1, team2, runda):
        host_limit = team1.strength
        guest_limit = 10000 - team2.strength
        b1=0
        b2=0
        def dogrywka(team1, team2,b1,b2,runda):
            def karne(team1, team2,b1,b2,runda):
                k1=0
                k2=0
                i=1
                for i in range(5):
                    los1 = random.randint(0, 100)
                    los2 = random.randint(0, 100)
                    if los1 < 75:
                        k1 = k1 + 1
                    elif los2 > 25:
                        k2 = k2 + 1
                while k1 == k2:
                    los1 = random.randint(0, 100)
                    los2 = random.randint(0, 100)
                    if los1 < 75:
                        k1 = k1 + 1
                    elif los2 > 25:
                        k2 = k2 + 1
                if k1 > k2:
                    if runda=="runda_1":
                        runda_2.append(team1)
                        wyniki_runda_1.append(str(b1)+' '+str(k1)+'pk')
                        wyniki_runda_1.append(str(b2)+' '+str(k2))
                    elif runda=="runda_2":
                        runda_3.append(team1)
                        wyniki_runda_2.append(str(b1)+' '+str(k1)+'pk')
                        wyniki_runda_2.append(str(b2)+' '+str(k2))
                    elif runda=="runda_3":
                        cwiercfinal.append(team1)
                        wyniki_runda_3.append(str(b1)+' '+str(k1)+'pk')
                        wyniki_runda_3.append(str(b2)+' '+str(k2))
                    elif runda=="cwiercfinal":
                        polfinal.append(team1)
                        wyniki_cwiercfinal.append(str(b1)+' '+str(k1)+'pk')
                        wyniki_cwiercfinal.append(str(b2)+' '+str(k2))
                    elif runda=="polfinal":
                        final.append(team1)
                        wyniki_polfinal.append(str(b1)+' '+str(k1)+'pk')
                        wyniki_polfinal.append(str(b2)+' '+str(k2))
                    elif runda=="final":
                        winner.append(team1)
                        wyniki_final.append(str(b1)+' '+str(k1)+'pk')
                        wyniki_final.append(str(b2)+' '+str(k2))
                elif k2 > k1:
                    if runda=="runda_1":
                        runda_2.append(team2)
                        wyniki_runda_1.append(str(b1)+' '+str(k1))
                        wyniki_runda_1.append(str(b2)+' '+str(k2)+'pk')
                    elif runda=="runda_2":
                        runda_3.append(team2)
                        wyniki_runda_2.append(str(b1)+' '+str(k1))
                        wyniki_runda_2.append(str(b2)+' '+str(k2)+'pk')
                    elif runda=="runda_3":
                        cwiercfinal.append(team2)
                        wyniki_runda_3.append(str(b1)+' '+str(k1))
                        wyniki_runda_3.append(str(b2)+' '+str(k2)+'pk')
                    elif runda=="cwiercfinal":
                        polfinal.append(team2)
                        wyniki_cwiercfinal.append(str(b1)+' '+str(k1))
                        wyniki_cwiercfinal.append(str(b2)+' '+str(k2)+'pk')
                    elif runda=="polfinal":
                        final.append(team2)
                        wyniki_polfinal.append(str(b1)+' '+str(k1))
                        wyniki_polfinal.append(str(b2)+' '+str(k2)+'pk')
                    elif runda=="final":
                        winner.append(team2)
                        wyniki_final.append(str(b1)+' '+str(k1))
                        wyniki_final.append(str(b2)+' '+str(k2)+'pk')
            for i in range(2):
                los = random.randint(0, 10000)
                if los < 8000:
                    b1 = b1 + 1
                elif los > 2000:
                    b2 = b2 + 1
            if b1 > b2:
                if runda=="runda_1":
                    runda_2.append(team1)
                    wyniki_runda_1.append(str(b1)+'pd')
                    wyniki_runda_1.append(b2)
                elif runda=="runda_2":
                    runda_3.append(team1)
                    wyniki_runda_2.append(str(b1)+'pd')
                    wyniki_runda_2.append(b2)
                elif runda=="runda_3":
                    cwiercfinal.append(team1)
                    wyniki_runda_3.append(str(b1)+'pd')
                    wyniki_runda_3.append(b2)
                elif runda=="cwiercfinal":
                    polfinal.append(team1)
                    wyniki_cwiercfinal.append(str(b1)+'pd')
                    wyniki_cwiercfinal.append(b2)
                elif runda=="polfinal":
                    final.append(team1)
                    wyniki_polfinal.append(str(b1)+'pd')
                    wyniki_polfinal.append(b2)
                elif runda=="final":
                    winner.append(team1)
                    wyniki_final.append(str(b1)+'pd')
                    wyniki_final.append(b2)
            elif b2 > b1:
                if runda=="runda_1":
                    runda_2.append(team2)
                    wyniki_runda_1.append(b1)
                    wyniki_runda_1.append(str(b2)+'pd')
                elif runda=="runda_2":
                    runda_3.append(team2)
                    wyniki_runda_2.append(b1)
                    wyniki_runda_2.append(str(b2)+'pd')
                elif runda=="runda_3":
                    cwiercfinal.append(team2)
                    wyniki_runda_3.append(b1)
                    wyniki_runda_3.append(str(b2)+'pd')
                elif runda=="cwiercfinal":
                    polfinal.append(team2)
                    wyniki_cwiercfinal.append(b1)
                    wyniki_cwiercfinal.append(str(b2)+'pd')
                elif runda=="polfinal":
                    final.append(team2)
                    wyniki_polfinal.append(b1)
                    wyniki_polfinal.append(str(b2)+'pd')
                elif runda=="final":
                    winner.append(team2)
                    wyniki_final.append(b1)
                    wyniki_final.append(str(b2)+'pd')
            else:
                karne(team1, team2,b1,b2,runda)
        for i in range(10):
            los = random.randint(0, 10000)
            if los < host_limit:
                b1 = b1 + 1
            elif los > guest_limit:
                b2 = b2 + 1
        if b1 > b2:
            if runda=="runda_1":
                runda_2.append(team1)
                wyniki_runda_1.append(b1)
                wyniki_runda_1.append(b2)
            elif runda=="runda_2":
                runda_3.append(team1)
                wyniki_runda_2.append(b1)
                wyniki_runda_2.append(b2)
            elif runda=="runda_3":
                cwiercfinal.append(team1)
                wyniki_runda_3.append(b1)
                wyniki_runda_3.append(b2)
            elif runda=="cwiercfinal":
                polfinal.append(team1)
                wyniki_cwiercfinal.append(b1)
                wyniki_cwiercfinal.append(b2)
            elif runda=="polfinal":
                final.append(team1)
                wyniki_polfinal.append(b1)
                wyniki_polfinal.append(b2)
            elif runda=="final":
                winner.append(team1)
                wyniki_final.append(b1)
                wyniki_final.append(b2)
        elif b2 > b1:
            if runda=="runda_1":
                runda_2.append(team2)
                wyniki_runda_1.append(b1)
                wyniki_runda_1.append(b2)
            elif runda=="runda_2":
                runda_3.append(team2)
                wyniki_runda_2.append(b1)
                wyniki_runda_2.append(b2)
            elif runda=="runda_3":
                cwiercfinal.append(team2)
                wyniki_runda_3.append(b1)
                wyniki_runda_3.append(b2)
            elif runda=="cwiercfinal":
                polfinal.append(team2)
                wyniki_cwiercfinal.append(b1)
                wyniki_cwiercfinal.append(b2)
            elif runda=="polfinal":
                final.append(team2)
                wyniki_polfinal.append(b1)
                wyniki_polfinal.append(b2)
            elif runda=="final":
                winner.append(team2)
                wyniki_final.append(b1)
                wyniki_final.append(b2)
        else:
            dogrywka(team1, team2,b1,b2,runda)

    random.shuffle(runda_1)
    for i in range(16):
        match(runda_1[2*i],runda_1[2*i+1],"runda_1")
    random.shuffle(runda_2)
    for i in range(16):
        match(runda_2[2*i],runda_2[2*i+1],"runda_2")
    random.shuffle(runda_3)
    for i in range(8):
        match(runda_3[2*i],runda_3[2*i+1],"runda_3")
    random.shuffle(cwiercfinal)
    for i in range(4):
        match(cwiercfinal[2*i],cwiercfinal[2*i+1],"cwiercfinal")
    random.shuffle(polfinal)
    for i in range(2):
        match(polfinal[2*i],polfinal[2*i+1],"polfinal")
    match(final[0],final[1],"final")
    all_dict={'wyniki_runda_1':wyniki_runda_1,'wyniki_runda_2':wyniki_runda_2,'wyniki_runda_3':wyniki_runda_3,'wyniki_cwiercfinal':wyniki_cwiercfinal,'wyniki_polfinal':wyniki_polfinal,'wyniki_final':wyniki_final,'pierwsza_runda':runda_1,'druga_runda':runda_2,'trzecia_runda':runda_3,'cwiercfinal':cwiercfinal,'polfinal':polfinal,'final':final,'winner':winner}
    PP_gallery.objects.create(name=winner[0].name,image=winner[0].image)
    return render(request,'first_app/puchar.html',context=all_dict)
def pier_liga(request):
    pliga_list = Pierwsza_Liga.objects.order_by('-points','-difference','-scored')
    date_dict = {'pier_liga_records':pliga_list}
    return render(request,'first_app/podglad_ligi.html',context=date_dict)
def drug_liga(request):
    dliga_list = Druga_Liga.objects.order_by('-points','-difference','-scored')
    date_dict = {'drug_liga_records':dliga_list}
    return render(request,'first_app/podglad_ligi.html',context=date_dict)

def niemcy(request):
    list = Niemcy.objects.order_by('-points','-difference','-scored')
    date_dict = {'niemcy_records':list}
    return render(request,'first_app/podglad_ligi.html',context=date_dict)
def francja(request):
    list = Francja.objects.order_by('-points','-difference','-scored')
    date_dict = {'francja_records':list}
    return render(request,'first_app/podglad_ligi.html',context=date_dict)
def anglia(request):
    list = Anglia.objects.order_by('-points','-difference','-scored')
    date_dict = {'anglia_records':list}
    return render(request,'first_app/podglad_ligi.html',context=date_dict)
def hiszpania(request):
    list = Hiszpania.objects.order_by('-points','-difference','-scored')
    date_dict = {'hiszpania_records':list}
    return render(request,'first_app/podglad_ligi.html',context=date_dict)
def wlochy(request):
    list = Wlochy.objects.order_by('-points','-difference','-scored')
    date_dict = {'wlochy_records':list}
    return render(request,'first_app/podglad_ligi.html',context=date_dict)
def portugalia(request):
    list = Portugalia.objects.order_by('-points','-difference','-scored')
    date_dict = {'portugalia_records':list}
    return render(request,'first_app/podglad_ligi.html',context=date_dict)
def rosja(request):
    list = Rosja.objects.order_by('-points','-difference','-scored')
    date_dict = {'rosja_records':list}
    return render(request,'first_app/podglad_ligi.html',context=date_dict)
def belgia(request):
    list = Belgia.objects.order_by('-points','-difference','-scored')
    date_dict = {'belgia_records':list}
    return render(request,'first_app/podglad_ligi.html',context=date_dict)
def ukraina(request):
    list = Ukraina.objects.order_by('-points','-difference','-scored')
    date_dict = {'ukraina_records':list}
    return render(request,'first_app/podglad_ligi.html',context=date_dict)
def holandia(request):
    list = Holandia.objects.order_by('-points','-difference','-scored')
    date_dict = {'holandia_records':list}
    return render(request,'first_app/podglad_ligi.html',context=date_dict)
def turcja(request):
    list = Turcja.objects.order_by('-points','-difference','-scored')
    date_dict = {'turcja_records':list}
    return render(request,'first_app/podglad_ligi.html',context=date_dict)
def austria(request):
    list = Austria.objects.order_by('-points','-difference','-scored')
    date_dict = {'austria_records':list}
    return render(request,'first_app/podglad_ligi.html',context=date_dict)
def dania(request):
    list = Dania.objects.order_by('-points','-difference','-scored')
    date_dict = {'dania_records':list}
    return render(request,'first_app/podglad_ligi.html',context=date_dict)
def szkocja(request):
    list = Szkocja.objects.order_by('-points','-difference','-scored')
    date_dict = {'szkocja_records':list}
    return render(request,'first_app/podglad_ligi.html',context=date_dict)
def czechy(request):
    list = Czechy.objects.order_by('-points','-difference','-scored')
    date_dict = {'czechy_records':list}
    return render(request,'first_app/podglad_ligi.html',context=date_dict)
def cypr(request):
    list = Cypr.objects.order_by('-points','-difference','-scored')
    date_dict = {'cypr_records':list}
    return render(request,'first_app/podglad_ligi.html',context=date_dict)
def szwajcaria(request):
    list = Szwajcaria.objects.order_by('-points','-difference','-scored')
    date_dict = {'szwajcaria_records':list}
    return render(request,'first_app/podglad_ligi.html',context=date_dict)
def grecja(request):
    list = Grecja.objects.order_by('-points','-difference','-scored')
    date_dict = {'grecja_records':list}
    return render(request,'first_app/podglad_ligi.html',context=date_dict)
def serbia(request):
    list = Serbia.objects.order_by('-points','-difference','-scored')
    date_dict = {'serbia_records':list}
    return render(request,'first_app/podglad_ligi.html',context=date_dict)
def chorwacja(request):
    list = Chorwacja.objects.order_by('-points','-difference','-scored')
    date_dict = {'chorwacja_records':list}
    return render(request,'first_app/podglad_ligi.html',context=date_dict)
def szwecja(request):
    list = Szwecja.objects.order_by('-points','-difference','-scored')
    date_dict = {'szwecja_records':list}
    return render(request,'first_app/podglad_ligi.html',context=date_dict)
def norwegia(request):
    list = Norwegia.objects.order_by('-points','-difference','-scored')
    date_dict = {'norwegia_records':list}
    return render(request,'first_app/podglad_ligi.html',context=date_dict)
def izrael(request):
    list = Izrael.objects.order_by('-points','-difference','-scored')
    date_dict = {'izrael_records':list}
    return render(request,'first_app/podglad_ligi.html',context=date_dict)
def kazachstan(request):
    list = Kazachstan.objects.order_by('-points','-difference','-scored')
    date_dict = {'kazachstan_records':list}
    return render(request,'first_app/podglad_ligi.html',context=date_dict)
def bialorus(request):
    list = Bialorus.objects.order_by('-points','-difference','-scored')
    date_dict = {'bialorus_records':list}
    return render(request,'first_app/podglad_ligi.html',context=date_dict)
def azerbejdzan(request):
    list = Azerbejdzan.objects.order_by('-points','-difference','-scored')
    date_dict = {'azerbejdzan_records':list}
    return render(request,'first_app/podglad_ligi.html',context=date_dict)
def bulgaria(request):
    list = Bulgaria.objects.order_by('-points','-difference','-scored')
    date_dict = {'bulgaria_records':list}
    return render(request,'first_app/podglad_ligi.html',context=date_dict)
def rumunia(request):
    list = Rumunia.objects.order_by('-points','-difference','-scored')
    date_dict = {'rumunia_records':list}
    return render(request,'first_app/podglad_ligi.html',context=date_dict)
def slowacja(request):
    list = Slowacja.objects.order_by('-points','-difference','-scored')
    date_dict = {'slowacja_records':list}
    return render(request,'first_app/podglad_ligi.html',context=date_dict)
def liechtenstein(request):
    list = Liechtenstein.objects.order_by('-points','-difference','-scored')
    date_dict = {'liechtenstein_records':list}
    return render(request,'first_app/liechtenstein.html',context=date_dict)
def slowenia(request):
    list = Slowenia.objects.order_by('-points','-difference','-scored')
    date_dict = {'slowenia_records':list}
    return render(request,'first_app/podglad_ligi.html',context=date_dict)
def wegry(request):
    list = Wegry.objects.order_by('-points','-difference','-scored')
    date_dict = {'wegry_records':list}
    return render(request,'first_app/podglad_ligi.html',context=date_dict)
def luxembourg(request):
    list = Luxembourg.objects.order_by('-points','-difference','-scored')
    date_dict = {'luxembourg_records':list}
    return render(request,'first_app/podglad_ligi.html',context=date_dict)
def litwa(request):
    list = Litwa.objects.order_by('-points','-difference','-scored')
    date_dict = {'litwa_records':list}
    return render(request,'first_app/podglad_ligi.html',context=date_dict)
def armenia(request):
    list = Armenia.objects.order_by('-points','-difference','-scored')
    date_dict = {'armenia_records':list}
    return render(request,'first_app/podglad_ligi.html',context=date_dict)
def lotwa(request):
    list = Lotwa.objects.order_by('-points','-difference','-scored')
    date_dict = {'lotwa_records':list}
    return render(request,'first_app/podglad_ligi.html',context=date_dict)
def albania(request):
    list = Albania.objects.order_by('-points','-difference','-scored')
    date_dict = {'albania_records':list}
    return render(request,'first_app/podglad_ligi.html',context=date_dict)
def macedonia(request):
    list = Macedonia.objects.order_by('-points','-difference','-scored')
    date_dict = {'macedonia_records':list}
    return render(request,'first_app/podglad_ligi.html',context=date_dict)
def bosnia(request):
    list = Bosnia.objects.order_by('-points','-difference','-scored')
    date_dict = {'bosnia_records':list}
    return render(request,'first_app/podglad_ligi.html',context=date_dict)
def moldawia(request):
    list = Moldawia.objects.order_by('-points','-difference','-scored')
    date_dict = {'moldawia_records':list}
    return render(request,'first_app/podglad_ligi.html',context=date_dict)
def finlandia(request):
    list = Finlandia.objects.order_by('-points','-difference','-scored')
    date_dict = {'finlandia_records':list}
    return render(request,'first_app/podglad_ligi.html',context=date_dict)
def irlandia(request):
    list = Irlandia.objects.order_by('-points','-difference','-scored')
    date_dict = {'irlandia_records':list}
    return render(request,'first_app/podglad_ligi.html',context=date_dict)
def gruzja(request):
    list = Gruzja.objects.order_by('-points','-difference','-scored')
    date_dict = {'gruzja_records':list}
    return render(request,'first_app/podglad_ligi.html',context=date_dict)
def malta(request):
    list = Malta.objects.order_by('-points','-difference','-scored')
    date_dict = {'malta_records':list}
    return render(request,'first_app/podglad_ligi.html',context=date_dict)
def islandia(request):
    list = Islandia.objects.order_by('-points','-difference','-scored')
    date_dict = {'islandia_records':list}
    return render(request,'first_app/podglad_ligi.html',context=date_dict)
def walia(request):
    list = Walia.objects.order_by('-points','-difference','-scored')
    date_dict = {'walia_records':list}
    return render(request,'first_app/podglad_ligi.html',context=date_dict)
def irlandia_Pln(request):
    list = Irlandia_Pln.objects.order_by('-points','-difference','-scored')
    date_dict = {'irlandia_Pln_records':list}
    return render(request,'first_app/podglad_ligi.html',context=date_dict)
def gibraltar(request):
    list = Gibraltar.objects.order_by('-points','-difference','-scored')
    date_dict = {'gibraltar_records':list}
    return render(request,'first_app/podglad_ligi.html',context=date_dict)
def czarnogora(request):
    list = Czarnogora.objects.order_by('-points','-difference','-scored')
    date_dict = {'czarnogora_records':list}
    return render(request,'first_app/podglad_ligi.html',context=date_dict)
def estonia(request):
    list = Estonia.objects.order_by('-points','-difference','-scored')
    date_dict = {'estonia_records':list}
    return render(request,'first_app/podglad_ligi.html',context=date_dict)
def kosowo(request):
    list = Kosowo.objects.order_by('-points','-difference','-scored')
    date_dict = {'kosowo_records':list}
    return render(request,'first_app/podglad_ligi.html',context=date_dict)
def wyspy_Owcze(request):
    list = Wyspy_Owcze.objects.order_by('-points','-difference','-scored')
    date_dict = {'wyspy_Owcze_records':list}
    return render(request,'first_app/podglad_ligi.html',context=date_dict)
def andora(request):
    list = Andora.objects.order_by('-points','-difference','-scored')
    date_dict = {'andora_records':list}
    return render(request,'first_app/podglad_ligi.html',context=date_dict)
def san_Marino(request):
    list = San_Marino.objects.order_by('-points','-difference','-scored')
    date_dict = {'san_Marino_records':list}
    return render(request,'first_app/podglad_ligi.html',context=date_dict)
