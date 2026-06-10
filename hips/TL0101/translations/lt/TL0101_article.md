```markdown
### Definition

Kibernetinė kenkėjiška programinė įranga – santrumpinis terminas, apibūdinantis įvairias
kekšmingos programinės įrangos (malicious software) formas, kurios skirtos įsiskverbti į
kompiuterius ir juos užkrėsti, dažniausiai be savininko žinojimo (ITU, 2008).

### Primary reference(s)

ITU, 2008. *ITU Study on the Financial Aspects of Network Security: Malware and Spam*.
Tarptautinė telekomunikacijų sąjunga (ITU). Prieiga 31 spalio 2024.

### Annotations

#### Additional scientific description

Kibernetinė kenkėjiška programinė įranga yra portmanteaus „malicious software“. Tai
nurodo programinę įrangą, kurią sukūrėme siekiant sukelti žalą, sutrikdyti veiklą ar
gauti neteisėtą prieigą prie kompiuterių sistemų, tinklų ar įrenginių. Ji apima
įvairius kenksmingus programinės įrangos tipus, kiekvienas iš jų turi savo ypatybes ir
platinimo būdus. Kibernetinė kenkėjiška programinė įranga dažnai klasifikuojama į:

- **Familijas** – konkretus kenkėjiškos programinės įrangos tipas su unikaliomis
  ypatybėmis;
- **Variatus** – skirtingos kodo versijos konkrečioje familioje.

Pagrindiniai tipai:

- **Virusai** – prisijungia prie teisėtų programų ir platina duomenis iš įrenginio į
  įrenginį, kai programos vykdomi;
- **Lisi** – kopijuojasi ir platina save į kitas sistemas be host programų;
- **Trojanai** – maskeuoja save kaip gerą programinę įrangą, sukeldami vartotojų
  klaidą vykdyti juos, tuo pačiu pažeidžiant sistemą;
- **Pinigų išpaimimo programinė įranga (ransomware)** – kibernetiniai nusikaltėliai
  užkoduoja duomenis ir reikalauja sumokėjimo, kad atkurti raktų;
- **Spyware** – slaptai rinkia informaciją stebint vartotojų veiklą;
- **Išvalyklė (wiper)** – nuolat pašalina ar sugadina duomenis, saugomus užkrėstomis
  mašinų;
- **Rootkit** – leidžia neleistiną prieigą, slėpdama savo buvimą sistemoje;
- **Failų bejovės kenkėjiška programinė įranga (file‑less malware)** – naudoja
  teisėtas sistemos priemones, vengia duomenų failų, kad išvengtų antivirusinių
  apsaugų.

#### Istorija ir eigą

Kenkėjiškos programinės įrangos istorija siekia bent 80‑ųjų, kai pirmieji virusai
buvė sukurti (Milošević, 2014). Įdomūs įvykiai: *Morris Worm* (1988), kuris
sukėlė didelį pranešimų tinklo sutrikimą, ir *WannaCry* ransomware atakas (2017),
kurios paveikė organizacijas visame pasaulyje. 

Kenkėjiška programinė įranga gali būti perduota keliais keliais:

- el. pašto prisegtuvai (ypač phishing atakose);
- blogi svetainės puslapiai;
- užkrėstų programinės įrangos atsisiuntimai;
- tinklo pažeidimai.

Šiuolaikiniai atakų metodai apima dirbtinio intelekto panaudojimą kuriant pažangius
virusus (polimorfinius), kurie keičia savo kodą, kad išvengtų tradicinių apsaugų.

#### Failų bejovės kenkėjiška programinė įranga

Failų bejovės kenkėjiška programinė įranga (file‑less malware) – auganti grėsmė, nes
jų veikla priklauso nuo teisėtų sisteminių priemonių, kurios neleidžia antivirusiniams
programoms juos aptikti. Ji gali įsilaužti per phishing el. laiškus, pažeistas
svetaines ar *watering hole* atakas. Kai ji pasiekia sistemą, gali:

- pavogti konfidencialią informaciją;
- plisti infekciją visame tinklų.
- sukelti tarptautinius pavojus, kai kitos sistemos bus nukreiptos ranka.

Pavyzdys: *Stuxnet* lis (2010) – sukurtas, kad sugadintų Iranų branduolinės
infrastruktūros įrenginius. Šis pažangus kenkėjiškas programinės įrangos tipas
parodė, kad kibernetinės ginklai gali sukelti fizinę žalą ir sutrikdyti nacionalinį
saugumą (Zetter, 2014).

#### Tiekėjų ryšiai ir rizika

Kenkėjiška programinė įranga dažnai naudojama dėl jos universalumo ir efektyvumo.
Jų dažnumas – milijonai naujų variantų kasmet (Statista, 2024). Tai suteikia galimybę:

- finansiniam pelnui per ransomware;
- šnipinėjimui;
- paslaugų sutrikimams.

#### Poveikiai

Kenkėjiška programinė įranga gali sukelti:

- paslaugų sutrikimus;
- finansinę žalą;
- duomenų praradimą;
- reputacijos pažeidimą;
- didelius kirtimus, įskaitant mokesčių ir reguliatorių baudų.

Jei infekcija pasiekia svarbią infrastruktūrą, gali kilti nacionaliniai pavojai
(analoginis *Stuxnet* atvejis). Be to, kenkėjiškos programinės įrangos ataka
turi potencialą paveikti fizinę aplinką – pavyzdžiui, kenkėjiškai manipuliuoti
vandens tiekimo sistemą, padidinti cheminių medžiagų kiekį, kurie gali būti naudojami
žalingai (Sikder et al., 2023).

### Risk Management

Saugoti nuo kenkėjiškos programinės įrangos reikalauja:

1. Vartotojų sąmoningumo didinimo – daugelyje atveju atakas aktyvuojamos vartotojo
   sąlyga (pavyzdžiui, spustelėjant apgaulingą nuorodą);
2. Techninių priemonių taikymo – antivirusinė ir anti‑malware programinė įranga,
   sistemų atnaujinimai, tinklo segmentacija, papildomos apsaugos sluoksniai.

Vis dėlto, vartotojo sąmoningumas išlieka esminis.

### Monitoring

Grėsmių stebėjimas vyksta tarptautiniu, nacionaliniu, sektoriaus ir organizaciniais
lėniais, kuriose dalijamasi informacija apie kenkėjiškos programinės įrangos
identifikavimą, siekiant sumažinti riziką.

### References

- International Telecommunication Union (ITU), 2008. *ITU Study on the Financial Aspects of Network Security: Malware and Spam*. Genf: ITU.
- Liu, S., Peng, G., Zeng, H. and Fu, J., 2024. *A survey on the evolution of file‑less attacks and detection techniques*. [online] Accessed 16 January 2025.
- Milošević, N., 2014. *History of malware*. [online] Accessed 16 January 2025.
- Sikder, M.N.K., Nguyen, M.B.T., Elliott, E.D. and Batarseh, F.A., 2023. *Deep H2O: Cyber‑attacks detection in water distribution systems using deep learning*. Journal of Water Process Engineering, 52, 103568. DOI: 10.1016/j.jwpe.2023.103568. Accessed 16 January 2025.
- Statista, no date. *Annual number of new malware variants detected worldwide from 2019 to 2023*. [online] Accessed 16 January 2025.
- Zetter, K., 2014. *An unprecedented look at Stuxnet, the world's first digital weapon*. Wired. [online] Accessed 16 January 2025.
```