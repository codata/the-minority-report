### Definicija  
**DoS napad** je sprječavanje ovlaštenog pristupa resursima ili kašnjenje vremenski kritičnih operacija (milisekunde do sati, ovisno o usluzi). (NIST, 2017)

### Primarni izvor  
NIST, 2017. *Računalna sigurnost: Uvod u sigurnost informacija*. Specijalna publikacija 800‑12 revizija. Nacionalni institut standarda i tehnologije (NIST). Dohvaćeno 25. siječnja 2025.

### Dodatni znanstveni opis  
DoS napad čini računarski sustav ili mrežu nedostupnom za namjenske korisnike preplavljivanjem vanjskih ulaza (npr. dolazni web promet). U tim slučajevima se nazivaju **DDoS napad** ili iskorištavanje ranjivosti radi iscrpljivanja računalnih resursa. Ovaj napad blokira korisnicima pristup uslugama i informacijama, uzrokujući značajne operativne i financijske utjecaje (CISA, 2021).  

Distribuirano zatvaranje usluge (DDoS) ostaje stalna prijetnja na internetu. Iskorištavajući činjenicu da internet nema centraliziran sustav kontrole pristupa, DDoS napadi su izdržali od rane ere interneta. Rani napadi bili su povezani s hacker kulturom, a fokus se brzo preusmjerio na komercijalnu iskorištenost. Također, političke primjene DDoS napada uključuju kibernetičku rat, hacktivizam i terorizam (Brooks et al., 2021).  

Korištenje DoS i DDoS je dobro dokumentirano u povijesti kibernetičke sigurnosti. Rani napadi postoje još u ranoj eri interneta, s jednim od prvih incidenata u Francuskoj 1995. godine, a sljedeće godine veliki incident je ciljao PANIX, internet pružatelj usluga iz New Yorka (Brooks et al., 2021). Tijekom godina, napadi su evoluirali u složenosti i skali, primjerice 2016. godine napad botneće potaknut malverom Mirai, koji je iskoristio uređaje *Internet Stvari (IoT)* za lansiranje masivnog DDoS napada, poremećaj glavnih web stranica širom svijeta (CISA, 2017).  

DoS napadi mogu proizaći iz ljudskih grešaka (npr. pogrešna konfiguracija), drugih incidenata (npr. kvar napajanja) ili namjernih napada. Različite tehnike se primjenjuju u DoS napadima. Glavna razlika je između DoS i DDoS napada. DoS napad obično potječe iz jedne izvora i cilja sustav, dok DDoS napad uključuje više kompromitirane sustave, često formirajući botneću, da simultano protinja host ili mrežu, čime se otežava obrana.  

Povećanje broja povezanih uređaja – posebno u kontekstu *Internet Stvari (IoT)* – također povećava rizik od DDoS napada jer svaki povezan uređaj potencijalno može postati dio botneće.  

#### Vrste DoS napada  
1. **Napadi zasnovani na volumenu** preplavljivanje propusnosti mreže (npr. inundacija web stranice pretjeranim prometom).  
2. **Napadi koji iskorištavaju računalne resurse** slanjem neispravnih zahtjeva ili pokretanjem beskonačnih petlji da iscrpnu resurse.  

DoS napadi mogu eskalirati u nacionalne opasnosti kada ciljaju kritičku infrastrukturu. Prethodnost je 2007. godine kibernetički napadi na Estoniju, gdje su koordinirani DDoS napadi potkopali vladine, bankarske i medijske web stranice, uzrokujući širok poremećaj i naglašavajući ranjivosti na nacionalnoj razini (Ottis, 2008).  

DoS napadi su popularni među zlonamjernim akterima zbog relativne jednostavnosti izvođenja i potencijala za značajan poremećaj. Svake godine registriraju se velik broj DoS i DDoS incidenata, što ih čini jednom od najrasprostranjenijih oblika kibernetičkog napada (Bergamini de Neira et al., 2023). U 2024. NETSCOUT je izvijestio o više od 13 milijuna DDoS napada globalno, s rastućim trendovima višeslojnog napada (NETSCOUT, 2024).

### Utjecaj  
DoS napad uzrokuje neuspjeh legitimnih korisnika u pristupu informacijskim sustavima, uređajima ili drugim mrežnim resursima zbog djelovanja zlonamjernog kibernetičkog aktera. Uređene usluge uključuju e‑mail, web stranice, online račune (npr. bankarstvo) ili druge usluge koje ovise o pogođenom računaru ili mreži (CISA, 2021). DDoS napadi mogu pojačati zdravstvene ili financijske poremećaje tijekom prirodnih nesreća ili pandemija (ENISA, 2023).

### Upravljanje rizikom  
Smanjenje rizika od DoS napada uključuje kombinaciju tehnoloških i strateških mjera:  
- **Robusni protokoli mrežne sigurnosti**  
- **Sistemi za otkrivanje i sprječavanje provale (IDS/IPS)**  
- **AI‑potaknute sigurnosne rješenja**  
- **Rate limiting, filtriranje prometa, korištenje mreža za distribuciju sadržaja**  

Umjetna inteligencija može analizirati mrežni promet kako bi identificirala anomalije, omogućujući real‑time otkrivanje i odgovor, poboljšavajući filtriranje zlonamjernog prometa, dinamički alociranje resursa i predviđanje potencijalnih prijetnji na temelju uzoraka i ponašanja. ITU poboljšava spremnost na kibernetičku sigurnost, zaštitu i sposobnost reagiranja na incidente članicama putem Cyber vježbi na regionalnoj i međunarodnoj razini (ITU, n.d.).  

Cyber vježba je godišnji događaj tijekom kojeg se simuliraju kibernetički napadi, incidenti sigurnosti informacija ili drugi oblici poremećaja, kako bi se testirale sposobnosti organizacije: od otkrivanja incidenata do sposobnosti odgovora i minimiziranja povezanog utjecaja. Putem Cyber vježbi sudionici mogu potvrditi politike, planove, procedure, procese i sposobnosti koje omogućuju pripremu, prevenciju, odgovor, oporavak i kontinuitet poslovanja.  

---

*References (original citation format preserved)*  
- Bergamini de Neira, A., Kantarci, B. & Nogueira, M., 2023. Distributed denial of service attack prediction: Challenges, open issues and opportunities. Computer Networks, 222(C), Feb. DOI: 10.1016/j.comnet.2022.109553  
- Brooks, R.R., Yu, L., Ozcelik, I., Oakley, J. & Tusing, N., 2022. Distributed Denial of Service (DDoS): A History. IEEE Annals of the History of Computing, 44, pp.44–54.  
- Cybersecurity and Infrastructure Security Agency (CISA), 2017. Heightened DDoS Threat Posed by Mirai and Other Botnets.  
- Cybersecurity and Infrastructure Security Agency (CISA), 2021. Understanding Denial-of-Service Attacks.  
- European Union Agency for Cybersecurity (ENISA), 2023. ENISA Threat Landscape 2023.  
- International Telecommunication Union (ITU), n.d. CyberDrills.  
- NETSCOUT, 2024. Threat Intelligence Report 2024.  
- Ottis, R., 2008. Analysis of the 2007 Cyber Attacks against Estonia from the Information Warfare Perspective. In: Proceedings of the 7th European Conference on Information Warfare and Security, Plymouth, 2008. Reading: Academic Publishing Limited, pp.163–168.  
- National Institute of Standards and Technology (NIST), 2017. Computer Security: An Introduction to Information Security. Special Publication 800‑12 Revision 1. Gaithersburg, MD: U.S. Department of Commerce.  

*This translation aligns with the Controlled Vocabulary for Disaster Risk Reduction, ensuring consistent use of domain‑specific terminology and clear, hazard‑oriented language.*