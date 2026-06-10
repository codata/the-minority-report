### Definition
Pažangi grėsmė yra sukuriama priešininko su išplėstine kompetencija ir dideliais ištekliais, leidžiant, kad jis per daugybės skirtingų atakų kryptų (pvz., kibernetinė, fizinė ataka ir apgaulė) sukurtų galimybes pasiekti savo tikslus (NIST, 2012).

### Primary reference(s)
National Institute for Standards and Technology, 2012. *Guide for Conducting Risk Assessments*. DOI:10.6028/NIST.SP.800-30r1. Prieigos data: 2025‑01‑25.

### Annotations
#### Additional Scientific Description  
Pažangi pastovioji grėsmė (APT) kibernetikoje reiškia ilgo ir tikslinio kibernetinės atakos, kai dažnai neleistinas naudotojas įgaliotas prieigą prie tinklo ir lieka nepastebėtas ilgam laikui. Pagrindinis APT tikslas dažniausiai yra stebėti tinklo veiklą, pavogti duomenis ar sukelti trikdžius, o ne sukelti tiesioginių žalų. Ši grėsmė laikoma „pažanga“ dėl išplėstinių technikų, naudojamų pažeidžiamumų išnaudojimui, ir „pastovumo“ dėl nuolatinės pastangos pasiekti konkrečią tikslą.

Pirmieji atpažinti APT atvejai buvo „Titan Rain“ atakos (2003‑2006), kai atakos įsilaužė į JAV gynybos tinklus ir pavogė jautrią informaciją (Council of Foreign Relations, 2005). 2010‑metų „Stuxnet“ virmas pasižymėjo dideliu eskalavimu, parodydamas APT galimybę sukelti fizinę žalą, nukreipiantį į Iranų branduolių centrų centrifugas (Zetter, 2014). Kitas žymus pavyzdys – „Operation Aurora“ ataka (2009), kuri atskleidė kelių įmonių, įskaitant „Google“, tinklus, siekiant prieigą prie intelektinės nuosavybės ir aktyvistų el. pašto sąskaitų (Council of Foreign Relations, 2010). Neseniai atvejai, tokie kaip „SolarWinds“ (2020) ir „Nobelium“ kampanijos (2022), iliustruoja evoliucionuojančias APT technikas, orientuotas į tiekimo grandinės ir debesų infrastruktūros sistemą (Ghanbari et al., 2024).

APT naudoja įvairius metodus siekdama savo tikslų. Šios atakos orientuojamos pagal jų tikslų ypatybes, todėl jos gali turėti įvairių formų. Dažniausiai jos prasideda su įsilaužimu į tikslią sistemą, naudojant „spear‑phishing“, nulio dienos pažeidžiamumus (nežinomas saugumo trūkumas) ar kitus pažangius metodus, kad užsilaužtų nepastebimai. Įsilaužę į sistemą, atakos grupės gali:

* likti tyliai, stebėti srautą ir rinkti informaciją, arba
* naudotis lateraliniu judėjimu, naviguodamos tinklu, ir privilegijų didinimu, kad gautų prieigą prie jautrių sričių.

Pastovumas palaikomas per slaptų prieigos taškų ir rootkitų diegimą, leidžiant nuolatinę prieigą ir duomenų išsiliejimą be saugumo alarmų suketimų.

Kibernetiniai nusikaltėliai, ypač valstybės grupės ir organizuoti kibernetiniai nusikaltėliai, dažnai pasitelkia APT dėl jų efektyvumo siekiant ilgalaikių strateginių tikslų. Nors mažiau dažni nei masiniai kryptiniai atakos, tokios kaip „ransomware“, APT sudaro reikšmingą dalį didelės įtakos kibernetinių incidentų. Jos sudėtingumas ir galimybė sukelti didelę žalą padaro jas įdomiomis šnipinėjimui, intelektinės nuosavybės vagystei ar sabotavimui.

#### Metrics and Numeric Limits
Not applicable.

#### Key Relevant UN Convention / Multilateral Treaty
Tarptautiniai teisės instrumentai, apimantys kibernetinės saugos ir kibernetinės nusikaltimų kėlimą, įskaitant „Budapest“ konvenciją, suteikia pagrindą tarptautinei bendradarbiavimui kovoje su kibernetiniais nusikaltimais, įskaitant APT. Pasaulinės Organizacijos resolicijos skatina valstybų narėms įgyvendinti priemones, apsaugant kritinę infrastruktūrą ir skatindamos informacijos mainus tam, kad būtų užkirstas kelias kibernetiniams grėsmių. Tačiau trūksta specifinių sutarties, skirta tik APT, todėl kyla sunkumų, susijusių su šių pažangių, evoliucionuojančių grėsmių valdymu pasaulinėje masteliu. Kadangi APT dažniausiai atliekama valstybės veiksniais, jų reglamentavimas priklauso nuo tarptautinio viešojo teisinio kės.

#### Drivers
Not applicable.

#### Impacts
Not applicable.

#### Multi-hazard Context
Not applicable.

### Risk Management
APTs apsaugoti yra sudėtinga užduotis, atsižvelgiant į laiką, išteklius ir pastangas, kurias atakos grupė skiria savo veiklai. Be to, atsižvelgiant į įvairius APT strateginius metodus, sunku nustatyti universalias strategijas, veikiančias visiems atvejams. APT sudėtingumas ir nuolatinis vystymasis reikalauja pritaikyto ir adaptacijos apsaugos, nes vienas sprendimas negali aprėpti visų galimų grėsmių. Todėl organizacijoms reikia integruoti kelias strategijas, kad užtikrintų patikimą apsaugą.

Pagal Asharani et al. (2019), apsaugos strategijos prieš pažangias pastovias grėsmes (APT) klasifikuojamos į tris pagrindines grupes: stebėjimas, aptikimas ir mažinimas. Kiekviena grupė atlieka svarbų vaidmenį, siekiant sumažinti neleistinos prieigos riziką.

#### Monitoring Methodologies
Naudojamos tokios priemonės kaip ugniasieniai ir antivirusinė programinė įranga, stebint įvairius tinklo sistemos komponentus. Pažangūs ugniasieniai gali analizuoti srautą žinomų kenkėjiškų šablonų ir parašų, taip pat naudoti elgesio analizę, kad aptiktų neįprastą veiklą. Taip pat svarbu stebėti CPU naudojimą, nes neįprasti naudojimo modeliai gali rodyti įtartiną veiklą.

#### Detection Methodologies
Apima įvairius anomalių aptikimo metodus, tokias kaip statinė analizė, neuroniniai tinklai ir mašininis mokymasis. Šios metodikos padeda aptikti APT, kurie išlaiko išankstinį vidutinį laiko tarpą. Pavyzdžiui, įsilaužimo aptikimo sistema (IDS) gali analizuoti tinklo srautą, kad nustatytų neįprastą veiklą ir įspėtų saugumo komandą apie galimą grėsmę.

#### Mitigation Methodology
APT mažinimas pasiekiamas per reagavimą ir proaktyvumą. Reagavimo metodai apima potencialių atakų kelių ir pažeidžiamumų identifikavimą konkrečioje akimirkos metu, kritinių sričių prognozavimą ir jų rimtumo vertinimą. Proaktyvūs strategijos orientuojasi į apgaulę, siekdamos išvengti įsilaužimo, nukreipdamos ataką, kad sumažintų jos poveikį.

### Monitoring
Not applicable

### References
Alshamrani, A., Myneni, S., Chowdhary, A. ir Huang, D., 2019. „Aprašymas pažangių pastovių grėsmių: Technikos, sprendimai, iššūkiai ir tyrimų galimybės“. *IEEE Communications Surveys & Tutorials*, vol. 21, no. 2, ss. 1851‑1877. Pasiektas 2025‑01‑16.  

Brandão, P.R. ir Limonova, V., 2021. „Apsaugos metodologijos pažangių pastovių grėsmių (APT) apsaugai“. *American Journal of Applied Sciences*, 2021. DOI:10.3844/ajassp.2021.207.212. Pasiektas 2025‑01‑16.  

Council on Foreign Relations (CFR), 2005. „Titan Rain“. Pasiektas 2025‑01‑16.  

Council on Foreign Relations (CFR), 2010. „Operation Aurora“. Pasiektas 2025‑01‑16.  

Ghanbari, H., Koskinen, K. ir Wei, Y., 2024. „Nuo SolarWinds iki Kaseya: Tiekimo grandinės atakų augimas skaitmeniniame pasaulyje“. *Journal of Information Technology Teaching Cases*, 0(0). DOI:10.1177/20438869241299823. Pasiektas 2025‑01‑16.  

Hodge, V.J. ir Austin, J., 2004. „Išskirtinių duomenų aptikimo metodologijų tyrimas“. *Artificial Intelligence Review*, 22, ss. 85‑126. Pasiektas 2025‑01‑16.  

National Institute of Standards and Technology (NIST), 2012. *Special Publication 800-30 Revision 1: Guide for Conducting Risk Assessments*. Gaithersburg, MD: U.S. Department of Commerce. Pasiektas 2025‑01‑16.  

Zetter, K., 2014. „Neįprasta požiūris į Stuxnet, pirmąjį pasaulinį skaitmeninį ginklą“. *WIRED Magazine*. Pasiektas 2025‑01‑16.  

Cite this [Copy citation]