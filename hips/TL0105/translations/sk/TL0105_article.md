### Definition  
Útok na dodávateľský reťazec je situácia, kedy produkty, služby alebo technológie, ktoré dostávate, boli porušené alebo kompromitované, a následne sa používajú na vniknutie a ďalšie kompromitovanie vašich vlastných systémov (ICO, bez dátumu).

### Primary reference(s)  
ICO, bez dátumu – Útok na dodávateľský reťazec. Prístup 25. januára 2025.

### Annotations  

#### Additional scientific description  
V kybernetike sa útoky na dodávateľský reťazec týkajú využívania bezpečnostných slabín v dodávateľskom reťazci organizácie na infiltráciu jej systémov a sietí. Útočníci cielia na menej bezpečné prvky reťazca – ako sú dodávatelia tretích strán, dodávatelia alebo poskytovatelia služieb, napríklad cloudoví poskytovatelia – s cieľom kompromitovať cieľ pomocou prepojených digitálnych ekosystémov. Tento prístup umožňuje útočníkom obísť tradičné bezpečnostné opatrenia využitím dôveryhodných vzťahov.  

História útokov na dodávateľský reťazec sa vyvíjala paralelne so zvyšujúcou sa zložitosti globálnych dodávateľských sietí. Poznámkové prípady zahŕňajú útok v roku 2011 na RSA Security, kde útočníci kompromitovali tokeny SecurID prostredníctvom dodávateľa na prienik do obranných výkonných kontraktorov (Greenberg, 2021). V poslednej dobe ukázal útok SolarWinds v roku 2020 závažný vplyv takých porušení. V tejto udalosti špičkoví aktéri vložili škodlivý kód do aktualizácií softvéru spoločnosti, čo ovplyvnilo množstvo vládnych a súkromných organizácií po celom svete a zdôraznilo zraniteľnosti inherentné v dodávateľských reťazcoch (Williams, 2020).

#### Techniques  
V útokoch na dodávateľský reťazec sa využívajú rôzne techniky, vrátane:

- **Manipulácia s aktualizáciami softvéru** (napr. SolarWinds).  
- **Kompromitovanie repozitárov kódu**.  
- **Infikácia hardvérových komponentov počas výroby**.  
- **Využívanie zraniteľností v službách tretích strán**.  

Útočníci môžu vložiť škodlivý kód do legitímnych aktualizácií softvéru alebo využiť záložné prístupy v hardvérových zariadeniach na získanie neoprávneného prístupu.

#### Identity‑Based Attacks  
Mnoho organizácií zverejňuje svoje cloudové prostredia podél poskytovateľov služieb tretích strán. Útočníci sa preto zameriavajú na tieto poskytovateľov v rámci unikátneho typu útoku – **útokov založených na identite**. Tieto útoky využívajú rozsiahle oprávnenia, ktoré sú často udelené účtom poskytovateľov služieb a môžu mať prístup k viacerým zákazníckym prostrediam. Tento prepojený prístup zvyšuje potenciálny dopad kompromitácie, čím sa poskytovatelia stávajú atraktívnym cieľom (Microsoft, 2023).

#### Open‑Source Software  
Jedným z najvýznamnejších zdrojov útokov na dodávateľský reťazec je open‑source softvér. Komunity open‑source poskytujú množstvo modulov a balíkov široko používaných firmami po celom svete, vrátane tých, ktoré sú súčasťou dodávateľských reťazcov. Vzhľadom na to, že open‑source softvér často postráda jasné vlastníctvo a garantovanú bezpečnosť, často zavádza zraniteľnosti do bezpečnostných architektúr (Forbes, 2022).

#### Hijacking Updates & Code Signing  
Ďalšou prominentnou technikou sú hijacking aktualizácií a kompromitovanie kódového podpisu. Vývojári softvéru pravidelne distribúujú aktualizácie z centralizovaných serverov na udržiavanie a vylepšovanie svojich produktov. Hrozební aktéri môžu tento proces zneužiť infiltráciou siete dodávateľa na vloženie malvéru do aktualizácie alebo na jej úpravu na získanie neoprávneného kontroly nad funkčnosťou softvéru. Kódový podpis, mechanizmus slúžiaci na overenie autenticity a integrity softvéru, je ďalším kritickým cieľom. Zlovolní aktéri tento proces podkopávajú použitím vlastne-podpisovaných certifikátov, zneužitím nesprávne nakonfigurovaných kontrol prístupu alebo kompromitovaním systémov podpisu. Vytváraním ilúzie dôveryhodných dodávateľov a vložením škodlivého kódu do aktualizácií môžu útočníci úspešne realizovať vysoko klamlivé a škodlivé útoky (NIST, 2021).  

#### 2023 Incident  
V roku 2023 útočníci kompromitovali desktopovú aplikáciu 3CX prostredníctvom infikovaných inštalátorov, čo rozšírilo malvér cez široko používaný VoIP systém (Fortiguard, 2023).

#### Motivation  
Zlovolní aktéri čoraz častejšie využívajú útoky na dodávateľský reťazec kvôli ich vysokému dopadu a obtiažnosti detekcie. Zložitý charakter moderných dodávateľských reťazcov a závislosť na poskytovateľoch tretích strán vytvára množstvo príležitostí pre zneužitie, čo robí útoky na dodávateľský reťazec významným problémom v kybernetickej bezpečnosti. Vzhľadom na to, že útoky sú často cieľové, ich vykonanie je obmedzené na aktérov s vyššími zdrojmi a schopnosťami (zvyčajne).

---

### Metrics and numeric limits  
Neplatné.

### Key relevant UN convention / multilateral treaty  
Medzinárodné právne nástroje riešujúce útoky na dodávateľský reťazec sú súčasťou širších rámcov kybernetickej bezpečnosti a kyberkriminality. Konvencia Budapešťská Európskej rady o kyberkriminalite poskytuje smernice pre medzinárodnú spoluprácu pri boji proti kyberkriminalite, vrátane trestných činov, ktoré môžu zahŕňať útoky na dodávateľský reťazec.

### Drivers  
Tieto útoky, ktoré zahrňajú využitie alebo zmeny softvéru, hardvéru alebo aplikácií tretích strán, predstavujú významnú výzvu pre organizácie.

### Impacts  
- **Podvod**  
- **Krádež**

### Risk Management  
Obrana proti útokom na dodávateľský reťazec vyžaduje komplexný prístup, ktorý zahŕňa dôkladné overenie dodávateľov, zavedenie prísnych bezpečnostných štandardov, neustále monitorovanie a podporu spolupráce medzi organizáciami a ich partnermi. Keďže mnoho útokov závisí na externých dodávateľoch s komplexnými závislosťami v ich nástrojoch a službách, dosiahnutie úplnej ochrany môže byť náročné. Organizácie však môžu prijať proaktívne stratégie na obranu proti bežným útokom (Cloudflare, bez dátumu).  

#### Running a Third‑Party Risk Assessment  
- **Testovanie softvéru tretích strán pred nasadením**.  
- **Požadovanie dodávateľmi súladu s konkrétnymi bezpečnostnými politikami**.  
- **Implementácia politiky bezpečnosti obsahu (CSP)** na kontrolu vykonateľných zdrojov v prehliadači.  
- **Použitie integrity podriadených zdrojov (SRI)** na odhalenie podozrivého JavaScriptu.

#### Implementing Zero Trust  
Zero Trust zabezpečuje, že všetci používatelia – zamestnanci, kontraktori a dodávatelia – sú neustále overovaní a monitorovaní v sieti organizácie. Overením identity a práv používateľov a zariadení Zero Trust zabraňuje útočníkom v zneužití odcudzených legitimných prihlasovacích údajov na infiltráciu organizácie.

#### DevSecOps  
Bezpečnosť dodávateľského reťazca využíva DevSecOps na obranu proti útokom tým, že najprv objaví všetky komponenty, získa prehľad o dodávateľskom reťazci a zabezpečí cloud‑native aplikačné komponenty. Integráciou bezpečnosti do celého vývojového procesu DevSecOps zabezpečuje okamžité nasadenie bezpečnostných operácií a hladké sladenie s obchodnými cieľmi (GitLab, bez dátumu).

### Monitoring  
Neplatné.

### References  

- Cloudflare, bez dátumu. *What is a supply chain attack?* Prístup 16. januára 2025.  
- Forbes, 2022. *Mitigating the risk of supply chain attacks in the age of cloud computing.* Prístup 15. januára 2025.  
- FortiGuard Labs, 2023. *Threat Signal Report: Supply Chain Attack Through 3CX Desktop App.* Prístup 15. januára 2025.  
- GitLab, bez dátumu. *What is DevSecOps?* Prístup 16. januára 2025.  
- Greenberg, A., 2021. *The Full Story of the Stunning RSA Hack Can Finally Be Told.* Prístup 15. januára 2025.  
- Information Commissioner’s Office (ICO), bez dátumu. *Supply chain attacks.* Prístup 15. januára 2025.  
- Microsoft, 2023. *Announcing Microsoft Defender for Cloud Capabilities to Counter Identity-Based Supply Chain Attacks.* Microsoft Tech Community. Prístup 15. januára 2025.  
- National Institute of Standards and Technology (NIST), 2021. *Defending Against Software Supply Chain Attacks.* Prístup 16. januára 2025.  
- Williams, J., 2020. *What You Need to Know About the SolarWinds Supply‑Chain Attack.* SANS Institute.  
- Cite this [Copy citation]