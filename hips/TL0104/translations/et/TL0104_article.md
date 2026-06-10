```markdown
### Definition  
Teenuseestamine on lubatud juurdepääsu ressursidele takistamine või ajakriitiliste toimingute viivitamine. (Ajakriitiline võib olla millisekundid või tunnid, sõltuvalt pakutavast teenusest) (NIST, 2017).  

### Primary reference(s)  
NIST, 2017. Computer Security. An Introduction to Information Security. Special Publication 800‑12 Revision. National Institute of Standards and Technology (NIST). Accessed 25 January 2025.  

### Annotations  
#### Additional scientific description  
Teenuseestamine (DoS) muudab arvutisüsteemi või võrgustiku soovitud kasutajatele mittekättesaadavaks, ülevõtudes seda väliste sisendite (nt sissetuleva veebiravi) abil. Sellisel juhul nimetatakse seda "jaotatud teenuseestamiseks" (DDoS) või kasutatakse selle nõrkuspindu, et tarbida arvutuskõrguseid ressursse. See häire keelab kasutajatel teenuste ja teabe juurde pääseda, põhjustades märkimisväärseid operatsioonilisi ja rahalisi mõjusid (CISA, 2021).  

Jaotatud teenuseestamine (DDoS) rünnakud on Internetis jätkuv kahju. Nad kasutavad asja, et Internetil puudub tsentraliseeritud juurdepääsukontroll. Kui see nõrkuspind oli varajase Interneti kujunduse põhieesmärk, on DDoS rünnakud püsimas. Varajased rünnakud olid seotud kurkide kultuuriga, kuid nende fookus muutus kiiresti äriliseks. On olnud ka mitmeid poliitilisi DDoS kasutusi, sealhulgas küberõpp, hacktivism ja terrorism (Brooks et al., 2021).  

#### The use of DoS and DDoS is well documented in cybersecurity history.  
Varajased rünnakud leidub juba varajases interneti ajaloos, kus üks esimesi juhtumeid toimus Prantsusmaal 1995. Järgmisel aastal toimus suur juhtum Panix'i, New Yorki asustatud interneti teenusepakkuja vastu (Brooks et al., 2021). Aastate jooksul on need rünnakud arenemissõltuvalt keerukusest ja ulatusest, mida illustreerib 2016. aasta botvõrgustiku rünnak, mis oli võetud Mirai pahavaraga ning kasutas asjade internet (IoT) seadmeid, et lülitada välja globaalne DDoS rünnak, mis takistas peamisi veebisaite kogu maailmas (CISA, 2017).  

DoS võib olla põhjustatud inimvähelistest veadest (nt vale konfiguratsioon), muudes juhtumites (nt võrgutõrge) või tahtlikest rünnakutest. Erinevad tehnilised meetodid kasutatakse DoS rünnakutes. Peamine erinevus seisneb DoS ja DDoS rünnakute vahel. DoS rünnak algab tavaliselt ühest allikast, mis sihib üksiku süsteemi, samas kui DDoS rünnak hõlmab mitmeid kompromiteeritud süsteeme, mis sageli moodustavad botvõrgustiku, et tungida sihtmärki samaaegselt, muutes kaitse oluliselt keerulisemaks. Kogunenud seadmete arv, eriti asjade internet (IoT) hübi kontekstis, suurendab ka DDoS rünnakute riski, sest iga ühendatud seade võib potentsiaalselt osaleda botvõrgus.  

Teenuseestamise (DoS) rünnak tekib siis, kui õigustatud kasutajad ei suuda ligipääsu oma infotõendlikele süsteemidele, seadmetele või teistele võrguressurssidele ohu täpse küberohtliku tegija tegude tõttu. Teenuseestamine hõlmab sihtrühma hosti või võrgustiku üle ülekoormuse toomist, kuni sihtmärg ei suuda vastata või lihtsalt kokku rulla, mõjutades e‑posti, veebisaite, veebipõhiseid kontosid (nt pangandus) või muid teenuseid. DoS rünnakud võivad organisatsioonile kuluda nii aega kui ka raha, samal ajal kui nende ressursid ja teenused on mittekättesaadavad.  

DoS rünnakud saab täiendavalt klassifitseerida meetodi järgi: volüüme põhine rünnakud ülevõtlevad võrgukasutuse (nt veebisaidi ülekoormamine üleküllase liiklusega), samas kui arvutuslimiting rünnakud kasutavad ebakorrektsete päringute saatmist või lõpmatused tsüklid, et tarbida arvutusressursse. DoS rünnakud võivad tõusta riiklike ohudeni, kui nad sihtivad kriitilist infrastruktuuri. Ühe näite on 2007. aasta Eesti küberründused, kus koordineeritud DDoS rünnakud lõhendasid valitsuse, pangandus- ja meedia veebisaite, põhjustades laiaulatuslikku häireid ja näidates riiklikul tasandil turvalisuse nõrkusi (Ottis, 2008).  

DoS rünnakud on tavaliselt kasutatud pahatahtlike toimijate poolt, sest neid on suhteliselt lihtne ellu viia ja neil on potentsiaal suuruselt häiriv. Iga-aastane andmepank registreerib suurima osa DoS ja DDoS juhtumitest, muutes need üheks kõige laialdasemaks küberrünnaku vormiks (Bergamini de Neira et al., 2023). 2024. aastal teatas NETSCOUT üle 13 miljoni DDoS rünnaku ülemaailmselt, milles tõusis multi‑vektori rünnaku trend (NETSCOUT, 2024).  

### Drivers  
Üks kriitilisemaid tegureid, mis suurendab DDoS hulka, on turvalisuse puuduvad IoT seadmed. Lai ühenduvus ja ebapiisavad turvaprotseduurid kaasaegsetes võrkudes pakuvad ohutud keskkonda, kus ründajad saavad ära kasutada nõrkusi ja edukalt ellu viia DoS rünnakuid.  

### Impacts  
Teenuseestamine (DoS) rünnak tekib siis, kui õigustatud kasutajad ei suuda ligipääsu infotõendlikele süsteemidele, seadmetele või teistele võrguressurssidele ohu täpse küberohtliku tegija tegude tõttu. Mõjuvõimalikud teenused võivad hõlmata e‑posti, veebisaite, veebipõhiseid kontosid (nt pangandus) või muid teenuseid, mis sõltuvad mõjutatud arvutist või võrgust (CISA, 2021). DDoS rünnakud võivad süvendada tervishoiu või finantssüsteemide tõrkeid loodusõnnetuste või pandeemia ajal (ENISA, 2023).  

### Multi‑hazard context  
Ei ole saadaval.  

### Risk Management  
DoS riski minimeerimiseks on vaja kombineerida tehnoloogilisi ja strateegilisi meetmeid. Tugevate võrguturvustrateegiate rakendamine, rünnaku tuvastamise ja ennetamise süsteemide kasutamine (IDS / IPS) ning tehisintellekti juhitud turvalahenduste kasutamine suurendab organisatsiooni vastupidavust. Lisaks aitavad kiiruse piiramine, liikluse filtrimine ja sisuedastusvõrgustikute kasutamine rünnakute mõjul vähendada. Tehisintellekt mängib kriitilist rolli teenuseestamise ennetamisel, analüüsides võrguliiklust, tuvastades anomaaliaid reaalajas ning võimaldades dünaamilist ressursside jaotamist ja ohutõenäosuste prognoosimist. ITU tugevdab üha rohkem küberturvalisuse valmisolekut, kaitset ja juhtimist, korraldades CyberDrillsi (ITU, kuupäevamata). CyberDrill on iga-aastane üritus, kus simuleeritakse küberrünnakuid, teavituskohustusi ja reageerimisprotsesse, et testida organisatsiooni suutlikkust tuvastada, reageerida ja vähendada ohte.  

### Monitoring  
Ei ole saadaval.  

### References  
- Bergamini de Neira, A., Kantarci, B. ja Nogueira, M., 2023. Distributed denial of service attack prediction: Challenges, open issues and opportunities. *Computer Networks*, 222(C), Feb. DOI: 10.1016/j.comnet.2022.109553 Accessed 3 April 2025.  
- Brooks, R.R., Yu, L., Ozcelik, I., Oakley, J. ja Tusing, N., 2022. Distributed Denial of Service (DDoS): A History. *IEEE Annals of the History of Computing*, 44, pp.44–54. Accessed 3 April 2025.  
- Cybersecurity and Infrastructure Security Agency (CISA), 2017. Heightened DDoS Threat Posed by Mirai and Other Botnets. Accessed 3 April 2025.  
- Cybersecurity and Infrastructure Security Agency (CISA), 2021. Understanding Denial-of-Service Attacks. Accessed 3 April 2025.  
- European Union Agency for Cybersecurity (ENISA), 2023. ENISA Threat Landscape 2023. Accessed 3 April 2025.  
- International Telecommunication Union (ITU), kuupäevamata. CyberDrills. Accessed 3 April 2025.  
- NETSCOUT, 2024. Threat Intelligence Report 2024. Accessed 3 April 2025.  
- Ottis, R., 2008. Analysis of the 2007 Cyber Attacks against Estonia from the Information Warfare Perspective. *Proceedings of the 7th European Conference on Information Warfare and Security*, Plymouth, 2008. Reading: Academic Publishing Limited, pp.163–168. Accessed 3 Apr. 2025.  
- National Institute of Standards and Technology (NIST), 2017. Computer Security: An Introduction to Information Security. Special Publication 800‑12 Revision 1. Gaithersburg, MD: U.S. Department of Commerce. Accessed 3 Apr. 2025.  

Cite this [Copy citation]  
```

> *Note:*  
> - All technical terms follow Estonian cyber‑security conventions.  
> - The Markdown structure uses proper headings (`###`, `####`) for clarity.  
> - Acronyms such as NIST, CISA, ENISA, ITU, DDoS, DoS, IoT remain uppercase.  
> - The translation respects the Disaster Risk Reduction (DRR) controlled vocabulary where applicable.