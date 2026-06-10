```markdown
# Definition
Tegelik Püsiv Oht (APT) loodi vastase poolt, kellel on kõrged spetsialiseerumise tasemed ja märkimisväärsed ressursid, võimaldades tal kasutada mitmeid erinevaid rünnaku vektoreid (nt küber, füüsiline ja petus), et luua võimalusi oma eesmärkide saavutamiseks (NIST, 2012).

# Primary reference(s)
Rahvusvaheline Standardi ja Tehnoloogia Instituut, 2012. Juhend riskianalüüsi läbiviimiseks. DOI:10.6028/NIST.SP.800-30r1. Külastatud 25. jaanuar 2025.

# Annotations
Lisakujunduslik kirjeldus  
Tegelik Püsiv Oht (APT) küber‑turvalisuses viitab pikaks ja sihipäraseks küberrünnakuks, kus sageli luba‑taoline kasutaja pääseb võrgule ja jääb pikka aega märkamata. APT‑ide peamine eesmärk on tavaliselt võrgu tegevuse jälgimine, andmete vargused või häirete tekitamine, mitte koheselt kahju tekitamine. See oht loetakse „täiustatuduks” tänu keerukatele tehnikatele, mida kasutatakse nõrkuspindade ära kasutamiseks, ning „püsivaks” pideva pingutuse tõttu konkreetse eesmärgi saavutamiseks.  
Üks varasemaid tunnustatud APT‑juhtumeid oli Titan Rain rünnakud aastatel 2003‑2006, kus ründajad tungisid Ameerika Ühendriikide kaitsekeskkonnasse tundlikku teabe vargamiseks (Council of Foreign Relations 2005). Stuxnet istu, mis avastati 2010, märkas märkimisväärset tõusku, näidates APT‑ide suutlikkust füüsilist kahju tekitada, sihtides Iirani tuuma sentrifuge (Zetter 2014). Teine silmapaistev näide oli Operation Aurora rünnak 2009, mis sihtis mitmeid ettevõtteid, sealhulgas Google’i, et pääseda ligipääsule intellektuaalomandi vargustele ja aktivistide e‑posti kontodele (Council of Foreign Relations 2010). Hiljutised juhtumid, näiteks SolarWinds (2020) ja Nobelium’s kampaaniad (2022), näitavad arenevaid APT‑tehnikaid, mis sihtivad varusõhkeid ja pilveinfrastruktuuri (Ghanbari et al., 2024).  

APT‑d kasutavad mitmekülgset tehnikad, et saavutada oma eesmärgid. Need rünnakud on kavandatud nende sihtmärkide omaduste põhjal, mistõttu võivad need võtta palju vorme. Sageli algavad need rünnakud sihtriitese süsteemi tungimisega, kasutades lõuandlust, nulli‑päevase nõrkuspinda või muid täiustatud tehnikaid, et tungida süsteemidesse märkamata. Sisenemise järel võivad ründajad jääda vaikseks, jälgides liiklust ja kogudes teavet, või kasutada lateral movement’i, et navigeerida võrgu vahel, kasutades õiguste tõstmist tundlikele aladele pääsemiseks. Püsivus säilib tagaseega ja rootkitide paigaldamise kaudu, võimaldades pidevat ligipääsu ja andmete eksfiltratsiooni ilma turvaalarme lülitamata.  

Lemmik‑kultuurilised tegurid, eriti riikijõud ja korraldatud küberkuritegevus, kasutavad sageli APT‑d, kuna nende tõhusus pikaajaliste strateegiliste eesmärkide saavutamisel. Kuigi vähem tavalised kui massi‑sihtlikud rünnakud nagu lunapõrand, esindavad APT‑d märkimisväärset osa kõrge mõjul juhtuvate küberjuhtumite protsentist. Nende keerukus ja potentsiaal märkimisväärse kahju tekitamiseks teevad neist eelistatud meetodid spiooniametiks, intellektuaalomandi varguseks või kahjustamiseks.

# Metrics and numeric limits
Pole rakendatav.

# Key relevant UN convention / multilateral treaty
Rahvusvahelised õiguslikud instrumendid, mis käsitlevad APT‑id, on osa laiemast küber‑turvalisuse ja küberkuritegevuse raamistikest. Euroopas Kogukonna Budapesti kokkulepe küberkuritegevuse kohta pakub alust rahvusvahelisele koostööle küberkuritegude võitluses, sealhulgas APT‑id hõlmavad. ÜRO resolutsioonid küberturvalisuse kohta julgustavad liikmesriike võtma meetmeid kriitilise infrastruktuuri kaitseks ja teabevahetuse edendamiseks, et ennetada küberohte. Kuid konkreetselt APT‑idel keskenduvade lepingu puudumine tõstatab globaalset väljakutset nende keerukate ja arenevate ohtude käsitlemiseks. Kuna APT‑id toimivad tihti riikijõudade poolt, kuulub nende reguleerimine rahvusvahelise avaliku õigusala alla.

# Drivers
Pole rakendatav.

# Impacts
Pole rakendatav.

# Multi-hazard context
Pole rakendatav.

# Risk Management
Kaitse APT‑i vastu on keeruline ülesanne, arvestades ründaja poolt kulutatud aega, ressursse ja jõupingutusi oma operatsiooni täitmiseks. Lisaks, arvestades mitmekülgset lähenemist, mida APT võtab, on keeruline esitada üldvalke strateegiaid, mis minimeerivad riski kõigi juhtumite jaoks. APT‑ide keeruline ja arenev olemus nõuab kohandatud ja kohanemisvõimelist kaitse lähenemist, sest ükski lahendus ei suuda kõiki võimalikke ohte katta. Selle asemel peavad organisatsioonid integreerima mitmeid strateegiaid, et tagada robustne kaitse. Asharani et al. (2019) järgi on APT‑i kaitse strateegiad jaotatud kolme peamisesse rühma: jälgimine, tuvastamine ja vähendamine. Igaüks mängib kriitilist rolli luba‑taolise ligipääsu riskide minimeerimisel.  

## Jälgimismeetodid
Need hõlmavad tööriistu, nagu tulemüürid ja viirusetõrje tarkvara, et jälgida süsteemi erinevaid osi. Tõhusad tulemüürid suudavad analüüsida liiklust tuntud pahavara mustrite ja allkirjade jaoks, samuti käituvad käitumisanalüüsi kasutades, et tuvastada ebatavalist tegevust. Lisaks on CPU kasutuse jälgimine oluline, kuna ressursside ebaolulised mustrid võivad viidata kahtlasele käitumisele.  

## Tuvastamismeetodid
Need hõlmavad erinevate anomaaliatuvastuse meetodite kasutamist, nagu staatiline analüüs, neuraalne võrk ja masinõpe (Hodge & Austin et al., 2004). Need tehnoloogiad aitavad tuvastada APT‑id, mis püsivad keskmise kuni pikaajalise perioodiga. Näiteks võib rünnakutuvastussüsteem (IDS) analüüsida võrgu liiklust, et tuvastada ebatavalist tegevust ja hoiata turvatöötajaid võimalike ohtude kohta.  

## Vähendamise meetod
APT‑i vähendamine on võimalik nii reaktiivsete kui ka proaktiivsete lähenemistega. Reaktiivsed meetodid hõlmavad võimalike rünnaku tee ja nõrkuspindade tuvastamist hetkel, kriitiliste alade prognoosimist ja nende raskusastme hindamist. Proaktiivsed strateegiad keskenduvad aga ründajate petmisele. Need tehnoloogiad on mõeldud intruudiid petma ja neid viima oma rünnakustrateegia muutma, vähendades ohu mõju.

# Monitoring
Pole rakendatav.

# References
Alshamrani, A., Myneni, S., Chowdhary, A. ja Huang, D., 2019. Uurimus täiustatud püsivate ohtude kohta: tehnikaid, lahendusi, väljakutseid ja uurimisvõimalusi. *IEEE Communications Surveys & Tutorials*, vol. 21, nr. 2, lk 1851‑1877, 2. kvartal 2019, doi:10.1109/COMST.2019.2891891. Külastatud 16. jaanuar 2025.  
Brandao, P.R. ja Limonova, V., 2021. Täiustatud püsivate ohtude kaitsmismeetodid (APT). *American Journal of Applied Sciences*, 2021. DOI:10.3844/ajassp.2021.207.212. Külastatud 16. jaanuar 2025.  
Council on Foreign Relations (CFR), 2005. Titan Rain. Külastatud 16. jaanuar 2025.  
Council on Foreign Relations (CFR), 2010. Operation Aurora. Külastatud 16. jaanuar 2025.  
Ghanbari, H., Koskinen, K. ja Wei, Y., 2024. Alates SolarWinds kuni Kaseya: varusõhke rünnakute tõus digitaalses maailmas. *Journal of Information Technology Teaching Cases*, 0(0). DOI:10.1177/20438869241299823. Külastatud 16. jaanuar 2025.  
Hodge, V.J. ja Austin, J., 2004. Anomaaliatuvastamise meetodite uuring. *Artificial Intelligence Review*, 22, lk 85‑126. Külastatud 16. jaanuar 2025.  
National Institute of Standards and Technology (NIST), 2012. Eripärane avaldus 800‑30 Reviisor 1: Juhend riskianalüüsi läbiviimiseks. Gaithersburg, MD: USA Kommertsiministeerium. Külastatud 16. jaanuar 2025.  
Zetter, K., 2014. Ennustamatult Stuxneti vaade, maailma esimene digitaalne relv. *WIRED Magazine*. Külastatud 16. jaanuar 2025.  

Cite this [Copy citation]
```