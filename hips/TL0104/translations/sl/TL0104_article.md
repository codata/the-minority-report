### Definition  
Zavrtnitev storitev je preprečevanje pooblaščenega dostopa do virov ali zakasnitev časovno kritičnih operacij. (Časovno kritično lahko pomeni milisekunde ali ure, odvisno od storitve.) (NIST, 2017).

### Primary Reference(s)  
NIST, 2017. Računalniška varnost. Uvod v varnost informacij. Special Publication 800‑12 Revision. Nacionalni zavod za standarde in tehnologijo (NIST). Dostopano 25. januar 2025.

### Annotations  
#### Additional Scientific Description  
Zavrtnitev storitev (DoS) naredi računalniški sistem ali omrežje nedostopno za namenjene uporabnike z zasedenjem z zunanjimi vhodnimi podatki (npr. prihodnji spletni promet). V takih primerih se uporablja izraz razpršena zavrnitev storitev (DDoS) ali izkoriščanje ranljivosti za izčrpavanje računalnih virov. Ta motnja zavrne uporabnike iz dostopa do storitev in informacij, kar povzroči znatne operativne in finančne posledice (CISA, 2021).

Razpršeni napadi DDoS ostajajo vztrajen moteč element na internetu. Izkoriščajo dejstvo, da internet nima centraliziranega nadzora dostopa. Ker je bila ta ranljivost osnovna zasnovna odločitev zgodnjega interneta, so napadi DDoS vztrajali. Zgodnji napadi so bili povezani z kulturo hakkerjev, a je njihova osredotočenost kmalu spremenjena v komercialno izkoriščanje. Prav tako je bilo več političnih uporabe DDoS, vključno s kibernetsko vojno, hacktivizmom in terorizmom (Brooks et al., 2021).

Uporaba DoS in DDoS je dobro dokumentirana v zgodovini kibernetske varnosti. Zgodnji napadi so bili zaznani že v zgodnji dobi interneta, pri čemer je bil en izmed prvih incidentov v Franciji leta 1995, naslednji pa je bil velik incident proti Panixu, internetni ponudnik v New Yorku (Brooks et al., 2021). S časom so se napadi razširili po kompleksnosti in obsegu, kar se kaže v napadu z botnetom leta 2016, ki ga je poganjal zlonamerni program Mirai in izkoriščal naprave internet stvari (IoT) za velik DDoS napad, ki je prekinil glavne spletne strani po vsem svetu (CISA, 2017).

DoS lahko nastane zaradi človeških napak (npr. napačne nastavitve), drugih incidentov (npr. izpada napajanja) ali namernih napadov. Uporabljene so različne tehnike. Glavna razlika je med DoS in DDoS napadi. DoS napad običajno izvira iz ene samega vira, ki cilja na sistem, medtem ko DDoS napad vključuje več kompromitiranim sistemom, ki pogosto tvorijo botnet, da hkrati preplavijo cilj, kar zahteva bistveno zahtevnejšo obrambo. Povečano število povezanih naprav – zlasti v kontekstu boom interneta stvari (IoT) – prav tako povečuje tveganje za DDoS napade, saj lahko vsaka povezana naprava postane del botneta.

Zavrtnitev storitev (DoS) napad se pojavi, ko pooblaščeni uporabniki ne morejo dostopati do informacijskih sistemov, naprav ali drugih virov omrežja zaradi dejanj zlonamerne kibernetske napadalke. Stanje zavrtnitve storitev preplavi ciljni gostitelja ali omrežje z prometom, dokler cilj ne more odgovoriti ali se preprosto ne zruši, kar vpliva na e‑pošto, spletne strani, spletne račune (npr. bančništvo) ali druge storitve. DoS napadi lahko organizaciji povzročijo tako časovne kot finančne izgube, medtem ko so njihovi viri in storitve nedostopni.

DoS napadi so mogoče dodatno kategorizirati po metodi: napadi na podlagi volumena preplavljajo širino pasu omrežja (npr. preplavanje spletne strani z pretiranim prometom), medtem ko napadi, ki izkoriščajo računalniške omejitve, vključujejo pošiljanje nepopolnih zahtevanj ali začetne neskončnih zank za izčrpavanje računalnih virov. DoS napadi se lahko povečajo v nacionalne nevarnosti, ko ciljajo kritične infrastrukture. Pretekla primera je leta 2007 kibernetski napadi na Estonijo, kjer so usklajeni DDoS napadi izničili vladne, bančne in medijske spletne strani, kar je povzročilo široke motnje in poudarilo ranljivosti na nacionalni ravni (Ottis, 2008).

DoS napadi jih pogosto uporabljajo zlonamerne akterje zaradi svoje relativne enostavnosti izvedbe in potenciala za pomembne motnje. Vsako leto poročajo podatki o velikem številu incidentov DoS in DDoS, kar jih postavlja med najbolj razširjene oblike kibernetskih napadov (Bergamini de Neira et al., 2023). V letu 2024 je NETSCOUT poročal o več kot 13 milijonih DDoS napadov po vsem svetu, z rastjo trendov v več‑vektorskih napadih (NETSCOUT, 2024).

### Drivers  
Eden izmed najkritičnejših dejavnikov, ki povzroča rast DDoS, je proliferacija neobčutljivih naprav interneta stvari. Obsežna povezanost in nezadostni varnostni protokoli v sodobnih omrežjih nudijo razredno okolje za napadalce, da izkoriščajo ranljivosti in uspešno izvedejo DoS napade.

### Impacts  
Zavrtnitev storitev (DoS) napad se pojavi, ko pooblaščeni uporabniki ne morejo dostopati do informacijskih sistemov, naprav ali drugih virov omrežja zaradi dejanj zlonamerne kibernetske napadalke. Zasegane storitve lahko vključujejo e‑pošto, spletne strani, spletne račune (npr. bančništvo) ali druge storitve, ki se zanašajo na prizadeti računalnik ali omrežje. (CISA, 2021). DDoS napadi lahko poslabšajo zdravstvene ali finančne sistemske odpovedi med naravnimi nesrečami ali pandemijami (ENISA, 2023).

### Multi‑hazard Context  
Ni na voljo

### Risk Management  
Zmanjšanje tveganja DoS vključuje kombinacijo tehnoloških in strateških ukrepov. Uvajanje robustnih protokolov varnosti omrežja, uporaba sistemov zaznavanja in preprečevanja vdora ter sprejemanje varnostnih rešitev, ki jih poganja umetna inteligenca, povečujejo odpornost organizacije. Poleg tega strategije, kot so omejevanje hitrosti, filtriranje prometa in uporaba omrežij za dostavo vsebine, pomagajo ublažiti vpliv napadov. Umetna inteligenca lahko prav tako igra ključno vlogo pri zaščiti pred DoS. AI‑pohajane varnostne rešitve analizirajo promet, da zaznajo anomalije, omogočajo realnočasovno zaznavanje in odziv, izboljšujejo zmožnost filtriranja zlonamernega prometa, dinamično razporejajo vire in napovedujejo potencialne grožnje na podlagi vzorcev in vedenj. ITU izboljšuje pripravljenost na kibernetske napade, zaščito in odzivnost na incidente držav članic z izvajanjem kibernetskih vaj na regionalni in mednarodni ravni (ITU, brez datuma). Kibernetska vaja je letni dogodek, pri katerem se simulirajo kibernetski napadi, incidenti varnosti informacij ali drugi tipi motenj, da se preizkusi zmožnosti organizacije – od zaznavanja do odzivanja in zmanjševanja povezanih posledic. S kibernetskimi vajami lahko udeleženci preverijo politike, načrte, postopke, procese in zmožnosti, ki omogočajo pripravo, preprečevanje, odzivanje, okrevanje in kontinuiteto poslovanja.

### Monitoring  
Ni na voljo

### References  
Bergamini de Neira, A., Kantarci, B. and Nogueira, M., 2023. Distributed denial of service attack prediction: Challenges, open issues and opportunities. Computer Networks, 222(C), Feb. DOI: 10.1016/j.comnet.2022.109553 Dostopano 3. april 2025.  
Brooks, R.R., Yu, L., Ozcelik, I., Oakley, J. and Tusing, N., 2022. Distributed Denial of Service (DDoS): A History. IEEE Annals of the History of Computing, 44, pp.44–54. Dostopano 3. april 2025.  
Cybersecurity and Infrastructure Security Agency (CISA), 2017. Heightened DDoS Threat Posed by Mirai and Other Botnets. Dostopano 3. april 2025.  
Cybersecurity and Infrastructure Security Agency (CISA), 2021. Understanding Denial‑of‑Service Attacks. Dostopano 3. april 2025.  
European Union Agency for Cybersecurity (ENISA), 2023. ENISA Threat Landscape 2023. Dostopano 3. april 2025.  
International Telecommunication Union (ITU), no date. CyberDrills. Dostopano 3. april 2025.  
NETSCOUT, 2024. Threat Intelligence Report 2024. Dostopano 3. april 2025.  
Ottis, R., 2008. Analysis of the 2007 Cyber Attacks against Estonia from the Information Warfare Perspective. In: Proceedings of the 7th European Conference on Information Warfare and Security, Plymouth, 2008. Reading: Academic Publishing Limited, pp.163–168. Dostopano 3. april 2025.  
National Institute of Standards and Technology (NIST), 2017. Computer Security: An Introduction to Information Security. Special Publication 800‑12 Revision 1. Gaithersburg, MD: U.S. Department of Commerce. Dostopano 3. april 2025.