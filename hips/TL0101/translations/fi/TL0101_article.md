*(markdown format with standard headings)*

```markdown
### Definition

Haittaohjelma on yhteisnimi eri muotoisille pahantahtoisille ohjelmistoille, joita suunnitellaan tietokoneiden tunkeutumiseen ja tarttumiseen, yleensä omistajan tiedostamatta (ITU, 2008).

### Primary reference(s)

ITU, 2008. ITU Study on the Financial Aspects of Network Security: Malware and Spam. International Telecommunication Union (ITU). Accessed 31 October 2024.

### Annotations

#### Lisäselvitys

Haittaohjelma on portmanteau‑muoto sanasta *malicious software*. Se viittaa ohjelmistoon, joka on suunniteltu aiheuttamaan vaurioita, häiritsemään toimintoja tai saamaan luvaton pääsy tietokonejärjestelmiin, verkostoihin tai laitteisiin. Se sisältää erilaisia haitallisia ohjelmistotyyppejä, jokaisella omat ominaisuutensa ja leviämistapansa. Haittaohjelma jaetaan usein **suvuihin** (viittaavat tiettyyn haittaohjelman tyyppiin, jolla on ainutlaatuiset ominaisuudet) ja **variantteihin** (yleensä eri versio koodista tietyn suvun sisällä) (International Telecommunication Union, 2008).

Haittaohjelmat voidaan jakaa seuraaviin tyyppeihin:

- **Virukset**: liitetään laillisiin ohjelmiin ja leviävät laitteesta toiseen, kun ne suoritetaan.  
- **Kammio-ohjelmat (worms)**: kopioivat itseään ja leviävät muihin järjestelmiin ilman isäntäohjelmaa.  
- **Troijalaiset**: esitetään hygieenisinä ohjelmina, jotka huijavat käyttäjiä suorittamaan ne, jolloin järjestelmä menettää suojansa.  
- **Lunastusohjelmat (ransomware)**: salastavat tiedot ja vaativat maksun purkukoodille.  
- **Jäljitysohjelmat (spyware)**: kerää tietoa käyttäjien toiminnasta piilostuen.  
- **Tiedon tuhontajat (wipers)**: poistavat tai rikkoavat pysyvästi dataa.  
- **Rootkitit**: mahdollistavat luvattoman pääsyn piilottamalla läsnäolonsa järjestelmässä.  
- **Polymorfiset haittaohjelmat**: muuttavat koodiaan kerta kertaalleen, jotta ne välttävät perinteiset turvatoimet.  
- **Tiedostottomat haittaohjelmat**: eivät riipu tiedostoista tai suoritettavista tiedostoista, vaan hyödyntävät laillisia järjestelmätyökaluja ja olemassa olevia tiedostoja, sovelluksia ja palveluita haitallisten toimien toteuttamiseen.

**Historian** mukaan haittaohjelmien historia ulottuu vähintään 80-luvulle, jolloin ensimmäiset luotiin (Milošević, 2014). Merkittävät tapaukset sisältävät Morris Wormin (1988) ja nykyaikaisen WannaCry‑lunastuksen (2017), jotka vaikuttivat maailmanlaajuisesti.

Haittaohjelmat voidaan toimittaa useiden vektorien kautta: sähköpostiliitetit (erityisesti phishing‑hyökkäyksissä), haitalliset verkkosivustot, tarttuneet ohjelmistolataukset tai verkko‑aukot. Nykyään hyökkääjät käyttävät tekoälyä luodakseen kehittyneitä haittaohjelmia, kuten polymorfisia tai tiedostottomia malwareja, jotka voivat muuttaa koodiaan havaitsemisen välttämiseksi (Liu et al., 2024).

**Stuxnet** – 2010–luotu kammio-ohjelma, joka sabotoi Iranin ydinlaitoksia – on esimerkki kyberaseen (kyberase) fyysisen vahingon aiheuttamisesta ja kansallisen turvallisuuden häiritsemisestä (Zetter, 2014).

Pahantahtoiset toimijat käyttävät haittaohjelmia monipuolisuuden ja tehokkuuden vuoksi. Haittaohjelmat ovat yksi yleisimmistä kyberhyökkäyksen muodoista, ja uusia malwarvariantiä havaitaan vuosittain (Statista, 2024). Ne palvelevat monia tarkoituksia: taloudellista hyötyä lunastuksesta, tiedustelua ja palveluiden häiriöitä.

### Metrics and numeric limits

Yli 1 miljardi uutta haittaohjelma‑varianttia havaittiin globaalisti vuonna 2023 (Statista, 2024).

### Key relevant UN convention / multilateral treaty

Kansainväliset oikeudelliset instrumentit, jotka käsittelevät haittaohjelmia, sisältyvät laajempaan kyberrikollisuus‑kehyksiin. Euroopan neuvoston Budapestin kyberrikollisuus‑kokooppi tarjoaa ohjeita kansainväliselle yhteistyölle kyberrikollisuuden torjumiseksi, mukaan lukien haittaohjelmien luominen, jakaminen tai käyttö. Pall Mall –prosessin koodi‑politiikka, päivitetty 2025, on globaalisti kattava dialogi, joka käsittelee kaupallisten kyberhyökkäysvälineiden leviämistä ja vastuuttomaa käyttöä.

### Drivers

- Ohjelmistovulnerabiliteetit  
- Digitaalinen riippuvuus  
- Kyberrikollisuuden talous  
- Geopoliittiset jännitteet

### Impacts

Haittaohjelma‑hyökkäykset voivat pahentua kansallisiin riskeihin, kun ne kohdistuvat kriittiseen infrastruktuuriin tai hallinnon järjestelmiin. Stuxnet‑kammio on esimerkki kyberaseen fyysisen vahingon aiheuttamisesta (Zetter, 2014).

### Multi‑hazard context

Haittaohjelma voi aiheuttaa merkittävää häiriötä palveluihin, taloudellista menetyksiä, tietojen menetyksiä tai varastamista, IT‑infrastruktuurin vahinkoa, mainehaittoja organisaatioille ja yksilöille, sekä merkittävää lunastuksen maksamista ja sääntelysanktioita. Palautuskustannukset voivat kasvaa. Lisäksi onnistuneen haittaohjelman vaikutukset voivat vahingoittaa julkista luottamusta organisaatioihin, poliitikoihin ja julkiseen sektoriin. Ohjelmistojärjestelmät ovat yhteydessä fyysisiin järjestelmiin, ja haittaohjelmat voivat mahdollistaa pääsyn järjestelmiin, jotka voivat avata muita riskejä, kuten suurten vesijakelu­järjestelmien kemikaalien lisääminen myrkkyä varten. Tällaisia yrityksiä on yritetty Floridassa (2021), Kaliforniassa (2021), Israelissa (2020) ja Yhdysvalloissa (2016) (Sikder et al., 2023).

### Risk Management

Haittaohjelmien torjuminen edellyttää käyttäjätietoisuutta, koska useimmat haittaohjelmat aktivoituvat käyttäjän luomun syötteen (kuten petollinen linkki) jälkeen. Teknisiä toimenpiteitä – kuten virustorjunta- ja anti‑malware‑ohjelmistoja, säännöllisiä järjestelmäpäivityksiä ja verkon segmentointia – voidaan käyttää lisäsuoja‑kerroksina, mutta niitä ei tulisi pitää käyttäjätietoisuuden korvaajana.

### Monitoring

Uhkien seuranta tapahtuu kansainvälisellä, kansallisella, sektorialla ja organisaatiotason tasolla, jossa tietoa haittaohjelmien tunnistamisesta jaetaan riskien lieventämiseksi.

### References

- International Telecommunication Union (ITU), 2008. *ITU Study on the Financial Aspects of Network Security: Malware and Spam*. Geneva: ITU.  
- Liu, S., Peng, G., Zeng, H. & Fu, J., 2024. *A survey on the evolution of fileless attacks and detection techniques*. [online] Accessed 16 January 2025.  
- Milošević, N., 2014. *History of malware*. [online] Accessed 16 January 2025.  
- Sikder, M.N.K., Nguyen, M.B.T., Elliott, E.D. & Batarseh, F.A., 2023. *Deep H2O: Cyber‑attacks detection in water distribution systems using deep learning*. Journal of Water Process Engineering, 52, 103568. [online]. DOI: 10.1016/j.jwpe.2023.103568. Accessed 16 January 2025.  
- Statista, no date. *Annual number of new malware variants detected worldwide from 2019 to 2023*. [online] Accessed 16 January 2025.  
- Zetter, K., 2014. *An unprecedented look at Stuxnet, the world’s first digital weapon*. Wired. [online] Accessed 16 January 2025.
```

---