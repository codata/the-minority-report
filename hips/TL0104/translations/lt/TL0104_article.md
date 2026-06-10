### Definition  
Paslaugų atmetimas (DoS) – tai autorizuotos prieigos užkirsti kelią prie išteklių arba laiko kritinių operacijų vėlinimas. (Laiko kritinis gali būti milisekundės arba valandos, priklausomai nuo teikiamos paslaugos) (NIST, 2017).  

### Primary reference(s)  
NIST, 2017. Kompiuterio saugumas. Įvadas į informacijos saugumą. Speciali publikacija 800‑12 revizija. Nacionalinis standartų ir technologijų institutas (NIST). Priėjta 25 sausio 2025.  

### Annotations  
#### Additional scientific description  
Paslaugų atmetimas (DoS) užkels kompiuterinę sistemą ar tinklą nuo jos numatytų vartotojų, perviršindamas ją išoriniais įvedimais (pvz., ateinantis tinklo srautas), kuris vėliau įgauna pavadinimą „Platinamas paslaugų atmetimas“ (DDoS) arba išnaudojant jo pažeidžiamumus išpildant kompiuterinius išteklius. Šis sutrikimas trukdo vartotojams prieiti prie paslaugų ir informacijos, sukeldamas reikšmingus veiklos ir finansinius padarinius (CISA, 2021).  

Platinamas paslaugų atmetimas (DDoS) atakuoja tvirtą tinklo struktūrą, nes internetas neturi centralizuotos prieigos kontrolės. Tai buvo pagrindinė ankstyvojo interneto dizaino sprendimo dalis, todėl DDoS atakų poveikis išlaikė ilgą laiką. Ankstyvojo interneto etapo atakos dažnai buvo susijusios su hakerių kultūra, bet greitai pereidavo prie komercinio išnaudojimo. Taip pat buvo keli politiniai DDoS naudojimo pavyzdžiai, įskaitant kibernetinę karą, hacktivizmą ir terorizmą (Brooks et al., 2021).  

#### Use  
DoS ir DDoS gerai dokumentuoti kibernetinio saugumo istorijoje. Vienas iš pirmųjų atvejų įvyko Prancūzijoje 1995 m., ir 1996 m. įvyko didelis incidentas prieš „Panix“, New York City pagrįstą interneto paslaugų teikėją (Brooks et al., 2021). Per metus šios atakos išsivystė sudėtingumo ir mastelio, pavyzdžiui, 2016 m. botnet ataką, sukurtą „Mirai“ malware, kuris išnaudodamas IoT įrenginius, sukūrė didžiulį DDoS ataką, trukdydamas svarbiausioms svetainėms visame pasaulyje (CISA, 2017).  

DoS gali kilti dėl žmogaus klaidų (pvz., netinkama konfigūracija), kitų incidentų (pvz., elektros sutrikimų) arba ketinimo atakuoti. Įgyvendinamos įvairios technikos. Pagrindinis skirtumas tarp DoS ir DDoS atakų: DoS ataka paprastai kilia iš vieno šaltinio, nukreipiusi į sistemą, o DDoS ataka įtraukia kelis pažeistus sistemas, dažnai formuojančius botnet, kad vienu metu nuplaužtų tikslą, sudėtinginant apsaugą. Didėjantis sujungtų įrenginių skaičius – ypač IoT boom kontekste – taip pat didina riziką, kad DDoS atakų įvykdymas bus, nes kiekvienas sujungtas įrenginys gali tapti botnet dalimi.  

#### Definition  
Paslaugų atmetimo (DoS) ataka įvyksta, kai teisėti vartotojai negali pasiekti informacinių sistemų, įrenginių ar kitų tinklo išteklių dėl kibernetinės grėsmės veiksnių. Paslaugų atmetimo sąlyga užpildo tikslingą hostą ar tinklą su srautu iki taško, kai tikslo įrenginys negali atsakyti arba tiesiog išsijungia, paveikdamas el. paštą, svetaines, internetinius paskyras (pvz., bankininkystę) ar kitas paslaugas. DoS atakos gali kainuoti organizacijai tiek laiko, tiek pinigų, kai jų ištekliai ir paslaugos tampa nepasiekiami.  

#### Classification  
DoS atakos gali būti klasifikuotos pagal metodą:  
- *Volume-based atakos* – viršija tinklo skerspjūvio plotį (pvz., perplaukia svetainę per didelį srautą).  
- *Resource‑exhaustion atakos* – siunčia sugadintas užklausas arba pradeda begalinį ciklą, kad išpildytų kompiuterinius išteklius.  

DoS atakos gali eskaluoti į nacionalinius pavojus, kai jos nukreipia į kritinę infrastruktūrą. Pavyzdys: 2007 m. kibernetiniai atakų Ēstā, kur koordinuotos DDoS atakos sustabdė valdžios, bankų ir žiniasklaidos svetaines, sukeldamos plačią sutrikimą ir parodydamos pažeidžiamumus nacionaliniu lygiu (Ottis, 2008).  

#### Incidents  
DoS atakų dažnai naudojama dėl jų patogumo ir galimybės sukelti didelį sutrikimą. Kiekvienais metais duomenys registruoja didelį DoS ir DDoS atvejų skaičių, leidžiant tai vienam iš dažniausiai pasitaikančių kibernetinių atakų (Bergamini de Neira et al., 2023). 2024 m. NETSCOUT pranešė, kad pasaulyje vyksta daugiau nei 13 milijonų DDoS atakų, padidėjusio kelių vectorų atakų tendencijoms (NETSCOUT, 2024).  

#### Drivers  
Vienas iš svarbiausių veiksnių, kuris prisideda prie DDoS didėjimo, yra nesaugiai IoT įrenginių plitimas. Išsami sąveika ir nepakankamos saugumo protokolų šiuolaikinėse tinkluose suteikia puikią aplinką atakų atlikimui, išnaudojant pažeidžiamumus.  

#### Impacts  
Paslaugų atmetimo (DoS) ataka įvyksta, kai teisėti vartotojai negali pasiekti informacinių sistemų, įrenginių ar kitų tinklo išteklių dėl kibernetinės grėsmės veiksnių. Poveikiais gali būti el. paštas, svetainės, internetinės paskyros (pvz., bankininkystė) ar kitos paslaugos, kurios priklauso nuo paveikto kompiuterio ar tinklo (CISA, 2021). DDoS atakos gali sustiprinti sveikatos priežiūros ar finansų sistemų gedimus natūralių gamtos nelaimių ar pandemijų metu (ENISA, 2023).  

#### Multi‑hazard context  
Nėra.  

#### Risk Management  
Mažinant DoS riziką derinant technologinius ir strateginius veiksmus:  
- Įgyvendinti patikimus tinklo saugumo protokolus,  
- Naudoti įsilaužimo aptikimo ir prevencijos sistemas,  
- Priimti dirbtinio intelekto pagrindu veikiančias saugumo sprendimus.  
Papildomai strategijos, tokios kaip greičio ribojimas, srauto filtravimas ir turinio pristatymo tinklų (CDN) naudojimas, gali sumažinti atakų poveikį. Dirbtinis intelektas gali analizuoti tinklo srautą, kad aptiktų anomalijas, leidžiančias realaus laiko aptikimą ir reagavimą, pagerintų kenkėjiško srauto filtravimą, dinamiškai paskirstydamas išteklius ir prognozuojant potencialias grėsmes pagal modelius ir elgesį. ITU pagerina kibernetinės saugos pasiruošimą, apsaugą ir incidentų reagavimą Vartotojų valstybėms, organizuojant „CyberDrill“ regioniniu ir tarptautiniu lygmeniu (ITU, nenurodytas). „CyberDrill“ – metinis renginys, kuriame simuliuojami kibernetiniai atakos, informacijos saugos incidentai ar kiti sutrikimų tipai, siekiant išbandyti organizacijos kibernetinės galimybės, nuo aptikimo incidento iki tinkamo reagavimo ir susijusio poveikio minimizavimo. Per „CyberDrill“ dalyviai gali patvirtinti politikas, planus, procedūras, procesus ir galimybes, leidžiančias paruošti, prevenciją, reagavimą, atkūrimą ir tęstinumą operacijų.  

#### Monitoring  
Nėra.  

#### References  
Bergamini de Neira, A., Kantarci, B. ir Nogueira, M., 2023. Platinamo paslaugų atmetimo atakų prognozė: iššūkiai, atvertos problemos ir galimybės. *Computer Networks*, 222(C), balandžio. DOI: 10.1016/j.comnet.2022.109553 Priėjta 3 balandžio 2025.  

Brooks, R.R., Yu, L., Ozcelik, I., Oakley, J. ir Tusing, N., 2022. Platinamas paslaugų atmetimas (DDoS): istorija. *IEEE Annals of the History of Computing*, 44, s.44–54. Priėjta 3 balandžio 2025.  

Cybersecurity and Infrastructure Security Agency (CISA), 2017. Padidintas DDoS grėsmės pavojaus dėl Mirai ir kitų botnetų. Priėjta 3 balandžio 2025.  

Cybersecurity and Infrastructure Security Agency (CISA), 2021. Įtartinumas dėl paslaugų atmetimo atakų. Priėjta 3 balandžio 2025.  

European Union Agency for Cybersecurity (ENISA), 2023. ENISA grėsmių kraštovaizdis 2023. Priėjta 3 balandžio 2025.  

International Telecommunication Union (ITU), nenurodytas. *CyberDrills*. Priėjta 3 balandžio 2025.  

NETSCOUT, 2024. Grėsmių informacijos ataskaita 2024. Priėjta 3 balandžio 2025.  

Ottis, R., 2008. Analizė apie 2007 m. kibernetinę ataką prieš Estiją iš informacijos karinės perspektyvos. 7-osios Europos informacijos karo ir saugumo konferencijos leidiniai, Plymouth, 2008. Knyga: Academic Publishing Limited, s.163–168. Priėjta 3 balandžio 2025.  

National Institute of Standards and Technology (NIST), 2017. Kompiuterio saugumas: Įvadas į informacijos saugumą. Speciali publikacija 800‑12 revizija 1. Gaithersburg, MD: JAV Prekybos departamento. Priėjta 3 balandžio 2025.  

---