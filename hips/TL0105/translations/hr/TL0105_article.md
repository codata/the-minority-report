```markdown
### Definicija
Napad lanca opskrbe je kada proizvodi, usluge ili tehnologija koje primate budu kompromitirani ili napadnuti i zatim se koriste za infiltriranje i dodatno kompromitiranje vaših vlastitih sustava (ICO, bez datuma).

### Primarna referenca(e)
ICO, bez datuma, Napad lanca opskrbe. Pristupljeno 25. siječnja 2025.

### Dodatni znanstveni opis
U kibernetičkoj sigurnosti, napadi lanca opskrbe odnose se na iskorištavanje sigurnosnih slabosti unutar lanca opskrbe organizacije kako bi se infiltrirali sustavi i mreže. Napadači ciljaju manje sigurne elemente lanca opskrbe – poput dobavljača treće strane, dobavljača ili pružatelja usluga poput oblak pružatelja usluga – s ciljem kompromitiranja krajnjeg cilja iskorištavanjem međusobne povezanosti modernih digitalnih ekosustava. Ova metoda omogućuje napadačima da zaobiđu tradicionalne sigurnosne mjere iskorištavanjem pouzdanih odnosa.

### Povijest i značajni incidenti
Povijest napada lanca opskrbe evoluirala je paralelno s rastućom složenošću globalnih mreža opskrbe. Značajni rani primjeri uključuju napad iz 2011. na RSA Security, gdje su napadači kompromitirali SecurID tokeni putem dobavljača kako bi probili obrambene poduzeća (Greenberg, 2021). Nedavno je incident 2020. SolarWinds pokrio težinu ovakvih prijetnji. U tom incidentu su sofisticirani prijetni subjekti umetnuli zlonamjerni kod u softverske nadogradnje tvrtke, utječući na brojne vladine i privatne organizacije diljem svijeta i ističući ranjivosti inherentne u lancima opskrbe (Williams, 2020).

### Tehnike napada
Razne tehnike se koriste u napadima lanca opskrbe. Uključuju:
- **Tampering s softverskim nadogradnjama** (npr. SolarWinds napad),
- **Kompromitiranje repozitorija koda**,
- **Infekcija hardverskih komponenti tijekom proizvodnje**,
- **Iskorištavanje ranjivosti trećih strana**.

Napadači mogu umetnuti zlonamjerni kod u legitimne nadogradnje ili koristiti skriveni ulaz u hardverskim uređajima kako bi dobili neovlašten pristup.

### Identitet‑bazirani napadi
Mnoge organizacije ovise o pružateljima usluga treće strane za upravljanje svojim oblacima, što je potaknulo napadače da se fokusiraju na ove pružatelje u jedinstvenoj formi napada baziranog na identitetu. Ti napadi iskorištavaju opsežne dozvole koje se često dodjeljuju računima pružatelja usluga, koji mogu imati pristup više okruženja klijenata. Ovaj međusobni pristup povećava potencijalni utjecaj kompromita, čineći pružatelje usluga privlačnim ciljem (Microsoft, 2023).

### Otvoreni izvorni softver
Jedan od najznačajnijih napada lanca opskrbe potječe od otvorenog izvornog softvera. Otvorene zajednice nude brojne module i pakete široko korištene od strane poduzeća diljem svijeta, uključujući one u lancima opskrbe. Međutim, budući da otvoreni izvorni softver često ne posjeduje jasnu vlasnička prava i garantiranu sigurnost, često uvodi ranjivosti u sigurnosne arhitekture (Forbes, 2022).

### Potpisivanje koda i hijakiranje nadogradnji
Druga prominentna tehnika uključuje hijakiranje nadogradnji i kompromitiranje potpisivanja koda. Softverski dobavljači redovito distribuiraju nadogradnje s centraliziranih poslužitelja kako bi održali i unaprijedili svoje proizvode. Prijetni subjekti mogu iskorištavati ovaj proces infiltriranjem mreže dobavljača kako bi umetnuli zlonamjerni kod u nadogradnju ili je modificirali za neovlašteni kontrolu nad funkcionalnošću softvera. **Potpisivanje koda**, mehanizam koji se koristi za provjeru autentičnosti i integriteta softvera, predstavlja još jedan kritičan cilj. Zlonamjerni subjekti podcijepaju ovaj proces korištenjem samopotpisanih certifikata, iskorištavanjem pogrešno konfiguriranih pristupnih kontrola ili kompromitirajući sustave potpisivanja. Uklanjanjem ovog mehanizma, napadači mogu uspješno izvršiti vrlo zavaravajuće i štetne napade (NIST, 2021).

### 2023. Napad na 3CX
U 2023. napadači su kompromitirali 3CX-ovu desktop aplikaciju putem zaraženih instalatora, šireći zlonamjerni kod kroz široko korišteni VoIP sustav (Fortiguard, 2023).

### Zaključak
Zlonamjerni subjekti sve više se oslanjaju na napade lanca opskrbe zbog njihove visoke učinkovitosti i teškoće u otkrivanju. Složenost modernih lanaca opskrbe i ovisnost o pružateljima treće strane stvaraju brojne prilike za iskorištavanje, čineći napade lanca opskrbe značajnim problemom u kibernetičkoj sigurnosti. Istovremeno, napadi su često ciljani; samo subjekti s većim resursima i sposobnostima ih obično mogu provesti.

### Upravljanje rizikom
Zaštita od napada lanca opskrbe zahtijeva sveobuhvatan pristup koji uključuje rigorozno provjeravanje dobavljača, implementaciju strogih sigurnosnih standarda, kontinuirano praćenje i poticanje suradnje između organizacija i njihovih partnera. Budući da mnogi napadi ovise o vanjskim dobavljačima s kompleksnim ovisnostima, postizanje potpune zaštite može biti teško. Međutim, organizacije mogu usvojiti proaktivne strategije kako bi se branile od uobičajenih vektora napada (Cloudflare, bez datuma).

- **Tretiranje rizika treće strane**: testiranje softvera treće strane prije instalacije, zahtijevanje da dobavljači poštuju specifične sigurnosne politike, implementacija **Politike sigurnosti sadržaja (CSP)** za kontrolu izvršnih resursa u pregledniku, i korištenje **Integriteta potrepština (SRI)** za otkrivanje sumnjivog JavaScript sadržaja.  
- **Implementacija Zero Trust**: Zero Trust osigurava da su svi korisnici – zaposlenici, ugovarači i dobavljači – kontinuirano provjereni i nadzirani unutar mreže organizacije.  
- **DevSecOps**: Sigurnost lanca opskrbe koristi DevSecOps kako bi se branilo od napada, otkrivajući sve komponente, dobivajući vidljivost u lanac opskrbe i osiguravajući cloud‑nativne aplikacijske komponente.

### Reference

- Cloudflare, bez datuma. *What is supply chain attack?* Pristupljeno 16. siječnja 2025.  
- Forbes, 2022. *Mitigating the risk of supply chain attacks in the age of cloud computing.* Pristupljeno 15. siječnja 2025.  
- FortiGuard Labs, 2023. *Threat Signal Report: Supply Chain Attack Through 3CX Desktop App.* Pristupljeno 15. siječnja 2025.  
- GitLab, bez datuma. *What is DevSecOps?* Pristupljeno 16. siječnja 2025.  
- Greenberg, A., 2021. *The Full Story of the Stunning RSA Hack Can Finally Be Told.* Pristupljeno 15. siječnja 2025.  
- Information Commissioner’s Office (ICO), bez datuma. *Supply chain attacks.* Pristupljeno 15. siječnja 2025.  
- Microsoft, 2023. *Announcing Microsoft Defender for Cloud Capabilities to Counter Identity-Based Supply Chain Attacks.* Microsoft Tech Community. Pristupljeno 15. siječnja 2025.  
- National Institute of Standards and Technology (NIST), 2021. *Defending Against Software Supply Chain Attacks.* Pristupljeno 16. siječnja 2025.  
- Williams, J., 2020. *What You Need to Know About the SolarWinds Supply‑Chain Attack.* SANS Institute.
```