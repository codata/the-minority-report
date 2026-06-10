```markdown
## Definition
Odmietnutie služby je zabránenie autorizovaného prístupu k zdrojom alebo oneskorenie časovo kritických operácií. Časovo kritické môže byť milisekundy alebo hodiny, v závislosti od poskytovanej služby. (NIST, 2017)

## Primary reference(s)
NIST, 2017. Computer Security. An Introduction to Information Security. Special Publication 800‑12 Revision. National Institute of Standards and Technology (NIST). Accessed 25 January 2025.

## Annotations

### Additional scientific description
Odmietnutie služby (DoS) robí počítačový systém alebo sieť neúplne dostupnou pre zamýšľaných používateľov, pretože ho preťažuje externými vstupmi (napr. prichádzajúca webová traffic). V takýchto prípadoch sa nazýva *Rozšírené odmietnutie služby* (DDoS) alebo sa využívajú zraniteľnosti na vyčerpanie výpočtových zdrojov. Toto narušenie odmietne používateľom prístup k službám a informáciám, čo spôsobuje významné prevádzkové a finančné dopady (CISA, 2021).

Distribúcia odmietnutia služby (DDoS) útoky zostávajú trvalým rušivým faktorom na internete. Využívajú fakt, že Internet nemá centralizovanú kontrolu prístupu. Keďže táto zraniteľnosť bola základným dizajn‑rozhodnutím skorého internetu, DDoS útoky pretrvávajú. Úvahy o útokoch sa rýchlo zmenili z kultúry hackerov na komerčné zneužitie. Dôvodom aj politického využitia DDoS sú kybervéža, hacktivizmus a terorizmus (Brooks et al., 2021).

Použitie DoS a DDoS je dobre zdokumentované v histórii kyberbezpečnosti. Prvé prípady sa objavili už v ranom internete, s jedným z prvých incidentov v roku 1995 vo Francúzsku, a nasleduje incident proti Panix, internetovému poskytovateľovi služieb v New Yorku (Brooks et al., 2021). V priebehu rokov sa tieto útoky vyvinuli v komplexnejší a rozsiahlejší. Príkladom je 2016 botnet útok poháňaný Mirai malware, ktorý využil zariadenia Internet of Things (IoT) na vykonanie masívneho DDoS útoku, rušičného na veľkých webových stránkach po celom svete (CISA, 2017).

DoS môže vzniknúť z ľudských chýb (napr. nesprávna konfigurácia), ďalších incidentov (napr. výpadok napájania) alebo úmyselných útokov. Rôzne techniky sú používateľné pri DoS útokoch. Hlavný rozdiel je medzi DoS a DDoS útokmi. DoS útok zvyčajne pochádza z jednej zdroja, zatiaľ čo DDoS útok zahŕňa viac kompromitovaných systémov, často tvoriacich botnet, ktoré súčasne naplavujú cieľ, čo výrazne znižuje obranu. Rastúci počet pripojených zariadení – najmä v kontexte boomu IoT – zvyšuje riziko DDoS útokov, pretože každé pripojené zariadenie môže potenciálne stať sa súčasťou botnetu.

Odmietnutie služby (DoS) útok sa vyskytuje, keď legitímni používatelia nedokážu pristúpiť k informačným systémom, zariadeniam alebo iným sieťovým zdrojom v dôsledku akcií zlého útočníka. Útok zaplavuje cieľový host alebo sieť s traffic, kým cieľ neodreaguje alebo jednoducho zrúti, čím ovplyvňuje e‑mail, webové stránky, online účty (napr. bankové účty) alebo iné služby. DoS útoky môžu organizáciám stáť čas a peniaze, pretože ich zdroje a služby sú nedostupné.  

DoS útoky sa ďalej kategorizujú podľa metódy:
- **Objemové útoky** preťažujú sieťové pásmo (napr. naplnenie webu nadmerným traffic).
- **Útoky využiťou výpočtové obmedzenia** zahŕňajú posielanie poškodených požiadaviek alebo iniciovanie nekonečných cyklov na vyčerpanie výpočtových zdrojov.

DoS útoky môžu eskalovať na národné riziká, keď cielia na kritickú infraštruktúru. Príklad je 2007 kyberútok na Estóniu, kde koordinované DDoS útoky znehodnotili vládne, bankové a mediálne stránky, vyvolávajúc rozsiahle rušenie a upozorňujúc na zraniteľnosti na národnej úrovni (Ottis, 2008). DoS útoky sa bežne používajú zlými útočníkmi kvôli relatívnej jednoduchosti vykonávania a možnosti významného rušenia. Každý rok sa v záznamoch registrujú veľké číslo DoS a DDoS incidentov, čo ich robí jedným z najrozšírenejších foriem kyberútoku (Bergamini de Neira et al., 2023). V roku 2024 NETSCOUT hlásil viac ako 13 miliónov DDoS útokov po celom svete, s rastúcim trendom viacerých útokov (NETSCOUT, 2024).

### Drivers
Jedným z najkritickejších faktorov vedúcich k zvýšeniu DDoS je proliferácia nezabezpečených IoT zariadení. Rozsiahle pripojenie a nedostatočné bezpečnostné protokoly v moderných sieťach poskytujú plodné pole pre útočníkov, ktorí využívajú zraniteľnosti a spúšťajú úspešné DoS útoky.

### Impacts
Odmietnutie služby (DoS) útok sa vyskytuje, keď legitímni používatelia nedokážu pristúpiť k informáciám systémom, zariadeniam alebo iným sieťovým zdrojom v dôsledku akcií zlého útočníka. Služby ovplyvnené môžu zahŕňať e‑mail, webové stránky, online účty (napr. bankové účty) alebo iné služby, ktoré závisia na dotknutom počítači alebo sieti (CISA, 2021). DDoS útoky môžu zhoršiť zdravotnícke alebo finančné systémy počas prírodných katastrof alebo pandémií (ENISA, 2023).

### Multi‑hazard context
N/A

### Risk Management
Minimalizácia rizika DoS zahŕňa kombináciu technologických a strategických opatrení. Implementácia robustných protokolov siete zabezpečenia, využitie systému detekcie vniknutia a prevencie a adopcia riešení bezpečnosti poháňaných AI zvyšuje odolnosť organizácie. Okrem toho stratégie ako obmedzenie rýchlosti, filtrovanie siete a využitie distribučných síť obsahu pomáhajú zmierniť dopad útokov. Umelá inteligencia môže tiež hrať kľúčovú úlohu v ochrane pred DoS. Systémy AI analyzujú sieťový traffic na identifikáciu anomálií, umožňujú reálne odhalenie a reakciu, zlepšujú schopnosť filtrovania zložitých traffic, alokujú zdroje dynamicky a predpovedajú potenciálne hrozby na základe vzorov a správania. ITU zlepšuje pripravenosť kyberbezpečnosti, ochranu a schopnosť riešenia incidentov členských štátov vykonávaním CyberDrills na regionálnej a medzinárodnej úrovni (ITU, no date). CyberDrill je ročná udalosť, počas ktorej sa simulujú kyberútoky, incidenty bezpečnosti informácií alebo iné druhy rušenia na testovanie kyberkompetencií organizácie, od detekcie incidentu až po schopnosť reagovať primerane a minimalizovať akýkoľvek súvislý dopad. Prostredníctvom CyberDrills môžu účastníci overiť politiky, plány, postupy, procesy a schopnosti, ktoré umožňujú prípravu, prevenciu, reakciu, zotavenie a kontinuálnu prevádzku.

### Monitoring
N/A

## References
- Bergamini de Neira, A., Kantarci, B. & Nogueira, M., 2023. Distributed denial of service attack prediction: Challenges, open issues and opportunities. *Computer Networks*, 222(C), Feb. DOI: 10.1016/j.comnet.2022.109553. Accessed 3 April 2025.
- Brooks, R.R., Yu, L., Ozcelik, I., Oakley, J. & Tusing, N., 2022. Distributed Denial of Service (DDoS): A History. *IEEE Annals of the History of Computing*, 44, pp.44–54. Accessed 3 April 2025.
- Cybersecurity and Infrastructure Security Agency (CISA), 2017. Heightened DDoS Threat Posed by Mirai and Other Botnets. Accessed 3 April 2025.
- Cybersecurity and Infrastructure Security Agency (CISA), 2021. Understanding Denial‑of‑Service Attacks. Accessed 3 April 2025.
- European Union Agency for Cybersecurity (ENISA), 2023. ENISA Threat Landscape 2023. Accessed 3 April 2025.
- International Telecommunication Union (ITU), no date. CyberDrills. Accessed 3 April 2025.
- NETSCOUT, 2024. Threat Intelligence Report 2024. Accessed 3 April 2025.
- Ottis, R., 2008. Analysis of the 2007 Cyber Attacks against Estonia from the Information Warfare Perspective. In: *Proceedings of the 7th European Conference on Information Warfare and Security*, Plymouth, 2008. Reading: Academic Publishing Limited, pp.163–168. Accessed 3 Apr. 2025.
- National Institute of Standards and Technology (NIST), 2017. Computer Security: An Introduction to Information Security. Special Publication 800‑12 Revision 1. Gaithersburg, MD: U.S. Department of Commerce. Accessed 3 Apr. 2025.
```

This corrected version aligns with DRR controlled vocabulary standards, uses consistent terminology, proper Markdown structure, and eliminates redundant or non‑geological language.