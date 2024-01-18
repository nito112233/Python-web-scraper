# Nodarbību laika apjoma analīzes rīks

## Projekta uzdevums

Nepieciešams izveidot programmu, kas automātiski iegūst informāciju par nodarbībām no tīmekļa vietnes *https://nodarbibas.rtu.lv/*, automātiski izvēloties filtrus ar studiju programmu "Informācijas tehnoloģija" 1. kursu 1. grupu. Programmmai jānolasa un jāveic analīzi par kopējo laiku, kas veltīts nodarbībām katrā mēnesī, uzādot grafiku par katru mēnesi, vieglākai datu apskatei. Programmas lietotājs var izvēlēties semestri izmantojot termināli ievadot 1, 2 vai 3.

Programma paredzēta ātrai noslodzes noteikšanai, lai vieglāk ieplānot laiku darbam un brīvajam laikam.

## Izmantotās Python bibliotēkas

1. Selenium

Bibliotēka tiek izmantota, lai veiktu automatizētas darbības tīmekļa vietnē, nolasītu lapas saturu, un aizpildītu formas elementus.

2. Matplotlib

Bibliotēka tiek izmantota, lai vizualizētu datus, konkrēti, lai radītu stabiņu diagrammu ar mēnešiem un atbilstošajiem nodarbību laikiem.

3. Time

Bibliotēka tiek izmantota, lai nodrošinātu laika aizture starp dažādām funkcijām, piemēram, gaidīšanu, kad tiek ielādēti elementi tīmekļa lapā.

## Programmatūras izmantošanas metodes

Lietotājam palaižot main.py ir jāizvēlas 1 vai 2 vai 3, lai izvēlētos konkrētu semestru. Automātiski tiek aizpildīta forma. Tiek ievākti nodarbību dati un apkoti atsevišķos kollonu grafikos katram mēnesim. Grafiks attēlo mēneša dienas un laiku katrā dienā, kā arī kopējo laiku konkrētā mēnesī.

Lai sāktu izmantot programmu, izpildiet main.py failu un ievadiet nepieciešamos parametru. Programma pēc tam automātiski apstrādā datus un ģenerē rezultātus.

## Uzstādīšana un izpilde

1. Noklonējiet repozitoriju: git clone *https://github.com/nito112233/Python-web-scraper.git*
2. Pārvietojieties uz projekta direktoriju: cd project-directory
3. Instalējiet bibliotēkas, ja tās nav ieinstalētas: pip install selenium, pip install matplotlib
4. Palaidiet programmu: python main.py
5. Ievadiet 1 vai 2 vai 3, lai izvēlētos kādu no semestriem
6. Aizveriet matplotlib grafika logu, kad esat gatavi pāriet uz nākamo mēnesi

Dastins Zvans, IT 1.kurss 1. grupa RTU

## Programmas darbības ierakstu var apskatīt ieraksts.mov!