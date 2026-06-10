```markdown
# Määritelmä
Edistynyt uhka syntyy vastustajalta, jolla on edistyneet osaamistasot ja merkittävät resurssit, mikä mahdollistaa useiden eri hyökkäysvektorien (esim. kiber-, fyysinen ja harhautus) hyödyntämisen tavoitteiden saavuttamiseksi (NIST, 2012).

## Ensisijaiset viittaukset
National Institute for Standards and Technology, 2012. *Guide for conducting risk assessments*. DOI:10.6028/NIST.SP.800-30r1. Käytetty 25. tammikuuta 2025.

## Lisäselvitys
Edistynyt pysyvä uhka (APT) kyberturvallisuudessa viittaa pitkäaikaiseen ja kohdennettuun kyberhyökkäykseen, jossa usein valtuuttamaton käyttäjä saa pääsyn verkkoon ja pysyy tunnistamattomana pidemmän aikaa. APT:n pääasiallinen tavoite on tyypillisesti verkon toiminnan tarkkailu, tietojen varastaminen tai häiriöiden aiheuttaminen, eikä välitöntä vahinkoa tuottaminen. Uhkaksi katsotaan *edistynyt*, koska hyödyntäminen tapahtuu kehittyneiden tekniikoiden avulla, ja *pysyvä*, koska tavoitteen saavuttamiseksi on jatkuvaa ponnistelua.

Yksi varhaisimmista tunnistetuista APT‑tapahtumista oli Titan Rain -hyökkäykset vuosina 2003–2006, joissa hyökkääjät murtoivat Yhdysvaltain puolustusverkkoja ja varastivat arkaluonteisia tietoja (Council of Foreign Relations 2005). Stuxnet‑käärmeen löytö vuonna 2010 merkitsi merkittävää eskaloitumista, osoittaen APT:n kykyä aiheuttaa fyysistä vahinkoa kohdistamalla Iranin ydinpyörremerkkien keskiöitä (Zetter 2014). Toinen merkittävä esimerkki on Operation Aurora -hyökkäys vuonna 2009, joka kohdistui useisiin yrityksiin, mukaan lukien Google, ja tarjosi pääsyn älylliseen omaisuuteen ja aktivistien sähköpostitileihin (Council of Foreign Relations 2010). Viimeaikaiset tapaukset, kuten SolarWinds (2020) ja Nobeliumin kampanjat (2022), havainnollistavat kehittyvien APT‑tekniikoiden soveltamista toimitusketjujen ja pilvi-infrastruktuurin kohdistamiseen (Ghanbari et al., 2024).

APT:t käyttävät monipuolista tekniikoiden kirjastoa tavoitteidensa saavuttamiseksi. Hyökkäykset suunnitellaan kohteiden ominaisuuksien mukaan ja voivat siksi esiintyä monissa eri muodoissa. Usein ne alkavat kohteen järjestelmän sisäänpääsyllä käyttäen tarkennettua phishing‑hyökkäystä, zero‑day‑haavoittuvuuksia (tuntemattomia turvallisuusaukkoja) tai muita edistyneitä tekniikoita tuntemattomien järjestelmien sisäänpääsyyn. Sisään päästyään hyökkääjät voivat joko pysyä hiljaisina, valvoa liikennettä ja kerätä tietoa, tai käyttää vaakasuoraa liikkumista verkon läpi ja oikeuksien laajentamista arkaluonteisiin alueisiin. Pysyvyys ylläpidetään käyttämällä taustaportteja ja rootkitteja, mikä mahdollistaa jatkuvan pääsyn ja tietojen uloskulun ilman turvallisuusvirheiden hälyttämistä.

Haitalliset toimijat, erityisesti valtiolliset ryhmät ja organisoidut kiberrikolliset, käyttävät usein APT:ta niiden tehokkuuden vuoksi pitkäaikisten strategisten tavoitteiden saavuttamiseksi. Vaikka massatavoitteiset hyökkäykset, kuten ransomeva, ovat harvinaisempia, APT:t muodostavat merkittävän osan korkean vaikutuksen kyberongelmista. Komplikaatiot ja mahdollisuudet merkittävään vahinkoon tekevät niistä suositut menetelmät spionoinnissa, älyllisen omaisuuden varastamisessa tai sabotoinnissa.

## Mittarit ja numeeriset rajat
Ei sovellettavissa.

## Kansainväliset sopimukset / monimutkaiset sopimukset
Kansainväliset oikeudelliset instrumentit APT:iin sisältyvät laajempien kyberturvallisuus- ja kyberrikollisuuskehyksiin. Euroopan neuvoston *Budapestin kyberrikollisuussopimus* tarjoaa pohjan kansainväliselle yhteistyölle kyberrikollisuutta torjumisessa, mukaan lukien APT:iin liittyvät rikolliset. Yhdistyneiden Kansakuntien kyberturvallisuuslaitokset kannustavat jäsenvaltioita omaksumaan toimenpiteitä kriittisen infrastruktuurin suojaamiseksi ja tietojen vaihtoa ehkäistäkseen kyberuhkia. Kuitenkin APT:iin keskittyvien sopimusten puuttuminen korostaa globaalin yhteistyön haasteita, kun käsitellään tällaisia kehittyneitä ja jatkuvasti muuttuvia uhkia.

Koska APT:t toteutetaan usein valtiollisten toimijoiden toimesta, niiden säätely kuuluu kansainvälisen julkisen oikeuden soveltamisalaan.

## Ajurit
Ei sovellettavissa.

## Vaikutukset
Ei sovellettavissa.

## Moniarvon konteksti
Ei sovellettavissa.

## Riskienhallinta
APT:n torjuminen on monimutkainen tehtävä, kun otetaan huomioon hyökkääjän halukkuus käyttää aikaa, resursseja ja ponnisteluja toiminnan toteuttamiseksi. Lisäksi APT:n monipuoliset lähestymistavat tekevät esityksistä vaikeita ennalta määritelläkseen riskin minimointia kaikissa tapauksissa. APT:n monimutkaisuuden ja kehittyvyyden vuoksi tarvitaan räätälöity ja sopeutuva puolustusstrategia, koska yksi ratkaisu ei riitä kaikkiin mahdollisiin uhkiin. Organisaatioiden on sen sijaan integroitava useita strategioita varmistamaan vahva suojaus. Asharani et al. (2019) mukaan APT:ien torjuntaan kuuluvat kolme pääryhmää: valvonta, havaitseminen ja lieventäminen. Jokainen näistä on ratkaisevassa roolissa valtuuttamattoman pääsyn riskin pienentämisessä.

### Valvonta
Valvontamenetelmät käyttävät työkaluja, kuten palomuurit ja virustorjunta, ja seurantaa järjestelmän eri osissa. Edistyneet palomuurit pystyvät analysoimaan liikennettä tunnetuille haitallisille kuvioille ja signaaleille sekä käyttäytymisanalyysia käyttäen poikkeavia toimintoja havaitsemaan. Lisäksi suoritinkäytön seuranta on tärkeää, koska epätavalliset resurssien käyttö voi viitata epäilyttävään toimintaan.

### Havaitseminen
Havaitsemassa hyödynnetään erilaisia poikkeavuushavainnaustekniikoita, kuten staattista analyysiä, neuroverkkoja ja koneoppimista (Hodge & Austin et al., 2004). Nämä tekniikat auttavat tunnistamaan APT:it, jotka pysyvät keskimääräisen tai pitkän aikavälin aikana. Esimerkiksi *törmäyshälytysjärjestelmä* (IDS) voi analysoida verkon liikennettä ja tunnistaa epätavallisia toimintoja sekä ilmoittaa mahdollisista uhkista.

### Lieventäminen
APT:n lieventäminen voidaan saavuttaa reaktiivisesti ja proaktiivisesti. Reaktiiviset toimet sisältävät mahdollisten hyökkäyspolkujen ja haavoittuvuuksien tunnistamisen hetkellä, kriittisten alueiden ennakoinnin ja niiden vakavuuden arvioinnin. Proaktiiviset strategiat puolestaan keskittyvät hyökääjien harhauttamiseen. Nämä tekniikat pyrkivät viemään hyökkääjät pois alkuperäisistä hyökkäyssuunnitelmista, mikä vähentää uhkan vaikutusta.

## Seuranta
Ei sovellettavissa.

## Viitteet
- Alshamrani, A., Myneni, S., Chowdhary, A. & Huang, D. (2019). *A survey on advanced persistent threats: Techniques, solutions, challenges, and research opportunities*. IEEE Communications Surveys & Tutorials, 21(2), 1851‑1877. DOI:10.1109/COMST.2019.2891891.  
- Brandao, P.R. & Limonova, V. (2021). *Defense methodologies for advanced persistent threats (APTs)*. American Journal of Applied Sciences, 2021. DOI:10.3844/ajassp.2021.207.212.  
- Council on Foreign Relations (CFR). (2005). *Titan Rain*.  
- Council on Foreign Relations (CFR). (2010). *Operation Aurora*.  
- Ghanbari, H., Koskinen, K. & Wei, Y. (2024). *From SolarWinds to Kaseya: The rise of supply chain attacks in a digital world*. Journal of Information Technology Teaching Cases, 0(0). DOI:10.1177/20438869241299823.  
- Hodge, V.J. & Austin, J. (2004). *A survey of outlier detection methodologies*. Artificial Intelligence Review, 22, 85‑126.  
- National Institute of Standards and Technology (NIST). (2012). *Special Publication 800‑30 Revision 1: Guide for Conducting Risk Assessments*. Gaithersburg, MD: U.S. Department of Commerce.  
- Zetter, K. (2014). *An unprecedented look at Stuxnet, the world’s first digital weapon*. WIRED Magazine.  
```