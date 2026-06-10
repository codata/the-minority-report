```markdown
### Definition
Palvelunestohyökkäys (DoS) on luvattoman pääsyn estäminen tietojärjestelmiin tai verkko­resursseihin, tai tärkeiden toiminnot viivästyttäväksi tekeminen. (Tärkeitä toimintoja voi tarkoittaa millisekunteja tai tunteja, riippuen tarjotusta palvelusta) (NIST, 2017).

### Primary reference(s)
NIST, 2017. Computer Security. An Introduction to Information Security. Special Publication 800‑12 Revision. National Institute of Standards and Technology (NIST). Accessed 25 January 2025.

### Annotations
**Lisätietoa**  
Palvelunestohyökkäys (DoS) tekee tietokone‑ tai verkko­järjestelmästä tai verkosta käytettävissä käyttäjilleen ylikuormittamalla sen ulkoisilla syötteillä (esim. saapuva verkkoliikenne). Tällöin tapahtuma tunnetaan myös nimellä hajautettu palvelunestohyökkäys (DDoS) tai se voi olla hyödyntäminen järjestelmän haavoittuvuuksista resurssien loppuun kuluttamiseksi. Tämä häiriö kieltää käyttäjien pääsyn palveluihin ja tietoihin, aiheuttaen merkittäviä operatiivisia ja taloudellisia vaikutuksia (CISA, 2021).  
Hajautetut palvelunestohyökkäykset (DDoS) ovat pysyvä ongelma Internetissä. Ne hyödyntävät sitä, että Internetissä ei ole keskitettyä pääsynhallintaa. Koska tämä haavoittuvuus oli alkuaikaisen Internetin keskeinen suunnittelupäätös, DDoS‑hyökkäykset ovat säilyneet. Varhaiset hyökkäykset liittyivät hacker‑kulttuuriin, mutta painopiste vaihtui nopeasti kaupalliseen hyödyntämiseen. DDoS‑hyökkäyksiä on myös käytetty poliittisesti, mukaan lukien kybertaistelu, hacktivismi ja terrorismi (Brooks et al., 2021).  
DoS‑ ja DDoS‑hyökkäysten historia on hyvin dokumentoitu kyberturvallisuuden historiassa. Varhaiset hyökkäykset näkyvät jo varhaisessa Internet‑ajoissa; ensimmäinen tapaus tapahtui Ranskassa 1995, ja seuraavana vuonna merkittävä tapaus tapahtui Panixille, New Yorkin kaupungissa sijaitsevalle internet‑palveluntarjoajalle (Brooks et al., 2021). Vuosien saatossa hyökkäykset ovat kehittyneet monimutkaisuudessa ja mittakaavassa, kuten 2016‑aikaisessa botnet‑hyökkäyksessä, jossa Mirai‑tartunta hyödyntää IoT‑laitteita massiivisen DDoS‑hyökkäyksen käynnistämiseen, häiritäen suuria verkkosivustoja maailmanlaajuisesti (CISA, 2017).  
DoS voi johtua ihmisvirheistä (kuten väärä määritys), muista tapahtumista (kuten virtavuostoa) tai tahallisista hyökkäyksistä. Hyökkäyksiä toteutetaan monella tavalla. Pääasiallinen ero DoS‑ ja DDoS‑hyökkäysten välillä on lähteiden määrä: DoS‑hyökkäys syntyy yleensä yhdestä lähteestä, kun taas DDoS‑hyökkäys käyttää useita kompromittoituneita järjestelmiä, usein muodostaa botverkko, ja kaataa kohteen samanaikaisesti, mikä tekee puolustuksesta huomattavasti haastavampaa.  
IoT‑laitteiden kasvava määrä lisää riskiä DDoS‑hyökkäyksille, koska jokainen yhteydessä oleva laite voi potentiaalisesti liittyä botverkkoon. Palvelunestohyökkäys tapahtuu, kun lailliset käyttäjät eivät voi käyttää tieto­järjestelmiä, laitteita tai muita verkko­resursseja, koska haitallinen kyberuhka‑aktiivi toimii. Tällöin kohde­verkko tai isäntä täytetään liikenteellä, kunnes kohde ei voi vastata tai kaatuu, vaikuttaen sähköpostiin, verkkosivustoihin, online‑tileihin (esim. pankkitileihin) tai muihin palveluihin. DoS‑hyökkäykset voivat maksaa organisaatiolle aikaa ja rahaa, kun resurssit ja palvelut ovat käyttökelvottomia.  

DoS‑hyökkäykset voidaan luokitella menetelmän mukaan: volyymipohjaiset hyökkäykset ylikuormittavat verkon kaistanleveyden (esim. verkkosivuston ylikuormitus liiallisella liikenteellä), kun taas tietokoneen rajoitteita hyödyntävät hyökkäykset lähettävät virheellisiä pyyntöjä tai aloittavat loputtomat silmukat kuluttamaan prosessointitehoa. DoS‑hyökkäykset voivat eskaloida kansallisiin vaaroihin, kun ne kohdistuvat kriittiseen infrastruktuuriin. Esimerkiksi 2007‑tapaus Estoniassa, jossa koordinoidut DDoS‑hyökkäykset katkaisivat hallituksen, pankit ja mediasektorin toiminnan, johti laajaan häiriöön ja korosti kansallisen tason haavoittuvuuksia (Ottis, 2008). DoS‑hyökkäykset ovat yleisesti hyödynnettävissä huonollisista toimijoista niiden helpon toteutuksen ja merkittävän häiriön vuoksi. Jokainen vuosi data rekisteröi suuren määrän DoS‑ ja DDoS‑tapahtumia, jolloin ne ovat yksi yleisimmistä kyber‑hyökkäyksistä (Bergamini de Neira et al., 2023). Vuonna 2024 NETSCOUT raportoi yli 13 miljoonaa DDoS‑hyökkäystä globaalisti, ja monivektoriset hyökkäykset ovat nousseet trendiksi (NETSCOUT, 2024).

### Drivers
Yksi tärkeimmistä tekijöistä DDoS‑hyökkäysten lisääntymiseen on turvattomien IoT‑laitteiden proliferointi. Laaja yhteysmahdollisuus ja riittämättömät turvatavaukset nykyaikaisissa verkoissa tarjoavat hedelmällisen alustan hyökkääjille hyödyntää haavoittuvuuksia ja käynnistää menestyksekkäitä DoS‑hyökkäyksiä.

### Impacts
Palvelunestohyökkäys (DoS) estää laillisten käyttäjien pääsyn tieto­järjestelmiin, laitteisiin tai muihin verkko­resursseihin. Vaikutettavat palvelut voivat sisältää sähköpostin, verkkosivustot, online‑tilit (esim. pankkitilit) tai muut järjestelmiin riippuvat palvelut (CISA, 2021). DDoS‑hyökkäykset voivat pahentaa terveydenhuollon tai talous­järjestelmän vikoja luonnon‑katastrofien tai pandemioiden aikana (ENISA, 2023).

### Multi-hazard context
Ei saatavilla

### Risk Management
DoS‑hyökkäysten riskin vähentäminen edellyttää teknologisten ja strategisten toimenpiteiden yhdistämistä. Vahvojen verkko­turvallisuus­protokollien käyttöönotto, tunkeutumisen tunnistus‑ ja ehkäisyjärjestelmien (IDPS) hyödyntäminen ja tekoälypohjaisten suojausratkaisujen ottaminen mukaan vahvistavat organisaation kestävyystasoa. Lisäksi strategiat, kuten nopeusrajoitus, liikenteen suodatus ja sisällönjakelus verkostojen (CDN) käyttö, auttavat lieventämään hyökkäysten vaikutusta. Tekoäly voi myös auttaa suojaamaan DoS‑hyökkäyksiltä. Tekoälyjärjestelmät analysoivat verkon liikennettä poikkeavuuksien tunnistamiseksi, mikä mahdollistaa reaaliaikaisen havaitsemisen ja vasteen, vahvistaa kykyä suodattaa haitallista liikennettä, allokoida resursseja dynaamisesti ja ennakoida uhkia mallien ja käyttäytymisten perusteella. ITU parantaa kyberturvallisuuden valmiutta, suojausta ja hätä­vastauksia jäsen­valtioille, järjestäen CyberDrills‑harjoituksia alueellisella ja kansainvälisellä tasolla (ITU, date). CyberDrill on vuosittainen tapahtuma, jossa simuloidaan kyber­hyökkäyksiä, tietoturvatapahtumia tai muita häiriö­tyyppejä testatakseen organisaation kyberturvallisuustoimintaa, tunnistaakseen uhka­tiedustelun ja reagoinnin. CyberDrills‑harjoituksissa osallistujat voivat vahvistaa politiikoita, suunnitelmia, menettelytapoja, prosesseja ja kykyjä, jotka mahdollistavat valmistelun, ehkäisyn, vasteen, palauttamisen ja jatkuvuuden.

### Monitoring
Ei saatavilla

### References
Bergamini de Neira, A., Kantarci, B. ja Nogueira, M., 2023. Distributed denial of service attack prediction: Challenges, open issues and opportunities. Computer Networks, 222(C), Feb. DOI: 10.1016/j.comnet.2022.109553 Accessed 3 April 2025.  
Brooks, R.R., Yu, L., Ozcelik, I., Oakley, J. ja Tusing, N., 2022. Distributed Denial of Service (DDoS): A History. IEEE Annals of the History of Computing, 44, pp.44–54. Accessed 3 April 2025.  
Cybersecurity and Infrastructure Security Agency (CISA), 2017. Heightened DDoS Threat Posed by Mirai and Other Botnets. Accessed 3 April 2025.  
Cybersecurity and Infrastructure Security Agency (CISA), 2021. Understanding Denial-of-Service Attacks. Accessed 3 April 2025.  
European Union Agency for Cybersecurity (ENISA), 2023. ENISA Threat Landscape 2023. Accessed 3 April 2025.  
International Telecommunication Union (ITU), no date. CyberDrills. Accessed 3 April 2025.  
NETSCOUT, 2024. Threat Intelligence Report 2024. Accessed 3 April 2025.  
Ottis, R., 2008. Analysis of the 2007 Cyber Attacks against Estonia from the Information Warfare Perspective. In: Proceedings of the 7th European Conference on Information Warfare and Security, Plymouth, 2008. Reading: Academic Publishing Limited, pp.163–168. Accessed 3 Apr. 2025.  
National Institute of Standards and Technology (NIST), 2017. Computer Security: An Introduction to Information Security. Special Publication 800‑12 Revision 1. Gaithersburg, MD: U.S. Department of Commerce. Accessed 3 Apr. 2025.  

Cite this [Copy citation]
```

This final translation uses consistent Finnish terminology, correct grammatical structures, and preserves the original meaning while fitting the controlled vocabulary for disaster risk reduction.