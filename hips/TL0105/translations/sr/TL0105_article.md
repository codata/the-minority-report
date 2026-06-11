### Definition  
Napad na lanac snabdevanja je kada proizvodi, usluge ili tehnologije koje se isporučuju imaju prodor ili su kompromitovani, te se te kompromitovane komponente koriste za infiltraciju i dalji napad na sopstvene sisteme (ICO, bez datuma).

### Primary reference(s)  
ICO, bez datuma, Napad na lanac snabdevanja. Pristupeno 25. januara 2025.

### Annotations  
#### Additional scientific description  
U oblasti sajber‑bezbednosti, napadi na lanac snabdevanja se odnose na iskorišćavanje sigurnosnih slabosti unutar lanca snabdevanja organizacije kako bi se infiltrisali u njene sisteme i mreže. Napadači ciljaju manje sigurne elemente lanca snabdevanja – kao što su dobavljači treće strane, dobavljači ili pružaoci usluga, uključujući oblakne provajdere – sa ciljem kompromitovanja krajnjeg cilja putem međusobne povezanosti modernih digitalnih ekosistema. Ovaj metod omogućava napadačima da zaobiđu tradicionalne sigurnosne mere kroz pouzdane veze. Istorija napada na lanac snabdevanja razvila se paralelno sa rastućom složenosti globalnih mreža snabdevanja. Značajni rani primeri uključuju napad 2011. na RSA Bezbednost, gde su napadači kompromitovali SecurID tokene putem dobavljača kako bi provalili u odbrambene izvođače (Greenberg, 2021). Sadašnji primer 2020. napada SolarWinds demonstrirao je ozbiljan uticaj takvih prodora. U tom incidentu su sofisticirani akteri ubacili zlonamerni kod u softverska ažuriranja kompanije, utičući na brojne vladine i privatne organizacije širom sveta i ističući ranjivosti inherentne lancima snabdevanja (Williams, 2020).  
Različite tehnike se primenjuju u napadima na lanac snabdevanja. One uključuju manipulaciju softverskim ažuriranjima (kao u napadu SolarWinds), kompromitovanje repozitorija koda, zaražavanje hardverskih komponenti tokom proizvodnje, i iskorišćavanje ranjivosti u uslugama treće strane. Napadači mogu ugraditi zlonamerni kod u legitimna softverska ažuriranja ili iskoristiti skriveni ulaz u hardverskim uređajima kako bi stekli neovlašćeni pristup.  
Mnoge organizacije zavise od dobavljača treće strane za upravljanje svojim cloud okruženjima, što je navelo napadače da se fokusiraju na ove provajdere u jedinstvenoj formi napada baziranih na identitetu. Ovi napadi iskorišćavaju opsežne dozvole koje se često daju nalogovima pružalaca usluga, koji mogu imati pristup više klijentskih okruženja. Ova međusobna povezanost povećava potencijalni uticaj kompromitovanja, čineći pružaoce usluga privlačnim ciljem (Microsoft, 2023).  
Jedan od najznačajnijih napada na lanac snabdevanja potiče iz softvera otvorenog koda. Komunity otvorenog koda nude brojne module i pakete široko korišćene od strane preduzeća širom sveta, uključujući one u lancima snabdevanja. Međutim, jer softver otvorenog koda često nema jasnu vlasničku strukturu i garantovanu bezbednost, često uvodi ranjivosti u bezbednosne arhitekture (Forbes, 2022). Druga značajna tehnika u napadima na lanac snabdevanja uključuje preuzimanje ažuriranja i kompromitovanje potpisivanja koda. Softverski dobavljači redovno distribuiraju ažuriranja sa centralizovanih servera kako bi održali i unapredili svoje proizvode. Akteri zlonamerne moći mogu iskoristiti ovaj proces infiltracijom mreže dobavljača kako bi ugradili zlonamerni softver u ažuriranje ili ga izmenili da bi stekli neovlašćenu kontrolu nad funkcionalnošću softvera. Potpisivanje koda, mehanizam koji se koristi za verifikaciju autentičnosti i integriteta softvera, takođe je ključna meta. Zlonamerni akteri ometaju ovaj proces korišćenjem samopotpisanih sertifikata, iskorišćavanjem pogrešno konfigurisanih kontrola pristupa ili kompromitovanjem sistema za potpisivanje. Pretvaranjem se u pouzdane dobavljače i ugradnjom zlonamernog koda u ažuriranja, napadači mogu uspešno izvršiti izuzetno zavodljive i štetne napade (NIST, 2021). U 2023. napadači su kompromitovali 3CX‑ovu desktop aplikaciju putem zaraženih instalatora, šireći zlonamerni softver kroz široko korišćeni VoIP sistem (Fortiguard, 2023).  
Zlonamerni akteri sve više zavise od napada na lanac snabdevanja zbog njihovog visokog uticaja i težine detekcije. Složenost modernih lanaca snabdevanja i zavisnost od dobavljača treće strane stvaraju brojne prilike za iskorišćavanje, čime napadi na lanac snabdevanja predstavljaju značajnu zabrinutost u sajber‑bezbednosti. Istovremeno, napadi na lanac snabdevanja su često ciljani. Stoga, samo akteri sa većim resursima i sposobnostima mogu (obično) sprovođenje takvih napada.

### Metrics and numeric limits  
Nije primenljivo.

### Key relevant UN convention / multilateral treaty  
Međunarodni pravni instrumenti koji se bave napadima na lanac snabdevanja obuhvaćeni su širim okvirima sajber‑bezbednosti i cyber‑zločina. Konvencija Budimpešta o sajber‑zločinu Saveta Evrope pruža smernice za međunarodnu saradnju u borbi protiv cyber‑zločina, uključujući prekršaje koji mogu uključivati napade na lanac snabdevanja.

### Drivers  
Ovi napadi, koji uključuju iskorišćavanje ili modifikovanje softvera, hardvera ili aplikacija treće strane, predstavljaju značajan izazov za organizacije.

### Impacts  
Prevade, krađe

### Multi-hazard context  
Nije primenljivo

### Risk Management  
Odbrana od napada na lanac snabdevanja zahteva sveobuhvatan pristup koji uključuje rigorozno proveravanje dobavljača, primenu strogih sigurnosnih standarda, kontinuirano praćenje i promovisanje saradnje između organizacija i njihovih partnera. Pošto mnogi napadi zavise od eksternih dobavljača sa složenim zavisnostima u njihovim alatima i uslugama, postizanje potpunog zaštitnog okvira može biti teško. Ipak, organizacije mogu primeniti proaktivne strategije za odbranu od uobičajenih vektora napada (Cloudflare, bez datuma). Izvršavanje procene rizika treće strane: To uključuje testiranje softverskog dobavljača pre distribucije, zahtev za dobavljače da se pridržavaju specifičnih sigurnosnih politika, implementaciju politike sigurnosti sadržaja (CSP) za kontrolu izvršnih resursa u pretraživaču, i upotrebu integriteta podređenih resursa (SRI) za otkrivanje sumnjivog JavaScript sadržaja. Implementacija Zero Trust: Zero Trust osigurava da svi korisnici — zaposleni, izvođači i dobavljači — stalno verifikuju i nadgledaju unutar mreže organizacije. Verifikacijom identiteta i privilegija korisnika i uređaja, Zero Trust sprečava napadače da iskoriste ukradene legitimne korisničke kredencijale za infiltraciju organizacije. DevSecOps: Sigurnost lanca snabdevanja koristi DevSecOps za odbranu od napada tako što prvo otkriva sve komponente, dobija vidljivost u lanac snabdevanja, i osigurava cloud‑native komponente aplikacije. Integrisanjem bezbednosti kroz razvojni proces, DevSecOps osigurava real‑time implementaciju bezbednosnih operacija uz istovremenu usklađenost sa poslovnim ciljevima (GitLab, bez datuma).

### Monitoring  
Nije primenljivo

### References  
- Cloudflare, bez datuma. Šta je napad na lanac snabdevanja? Pristupeno 16. januara 2025.  
- Forbes, 2022. Ublažavanje rizika napada na lanac snabdevanja u doba cloud računanja. Pristupeno 15. januara 2025.  
- FortiGuard Labs, 2023. Izveštaj o prijetnji: Napad na lanac snabdevanja putem 3CX Desktop aplikacije. Pristupeno 15. januara 2025.  
- GitLab, bez datuma. Šta je DevSecOps? Pristupeno 16. januara 2025.  
- Greenberg, A., 2021. Puna priča o zapanjujućem RSA hakovanju. Pristupeno 15. januara 2025.  
- Information Commissioner’s Office (ICO), bez datuma. Napadi na lanac snabdevanja. Pristupeno 15. januara 2025.  
- Microsoft, 2023. Objavljivanje Microsoft Defender for Cloud mogućnosti za otpor na napade bazirane na identitetu u lancu snabdevanja. Microsoft Tech Community. Pristupeno 15. januara 2025.  
- National Institute of Standards and Technology (NIST), 2021. Odbrana od napada na lanac snabdevanja softvera. Pristupeno 16. januara 2025.  
- Williams, J., 2020. Šta trebate znati o SolarWinds napadu na lanac snabdevanja. SANS Institute.  

---