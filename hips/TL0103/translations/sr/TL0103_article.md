```markdown
### Definition  
Napredna pretnja je stvorena od strane protivnika sa **naprednim nivoima stručnosti** i značajnim resursima, što mu omogućava da, koristeći više različitih **vektora napada** (npr. kibernetički, fizički i **lažna informacija**), generiše mogućnosti za ostvarenje svojih ciljeva (NIST, 2012).

### Primary reference(s)  
Nacionalni institut za standarde i tehnologiju (NIST), 2012. **Priručnik za sprovođenje procena rizika**. DOI:10.6028/NIST.SP.800-30r1. Pristup 25. januara 2025.

### Annotations  
**Napredna trajna pretnja (APT)** u kibernetičkoj bezbednosti predstavlja **dugoročni** i ciljano napad gde neovlašćeni korisnik pristupa mreži i ostaje **neotkriven** duže vreme. Glavni cilj APT‑ova je obično posmatranje mrežnih aktivnosti, krađa podataka ili uzrokovanje prekida, a ne direktno nanosiće štetu.  

Jedan od najranijih prepoznatih APT incidenata bio je „Titan Rain“ napad između 2003. i 2006. godine, kada su napadači infiltrisali američke odbrambene mreže kako bi ukrali osetljive informacije (Council of Foreign Relations, 2005). Otkrivanje Stuxnet čipke 2010. godine označilo je značajan pomak, pokazujući sposobnost APT‑ova da izazovu fizičku štetu ciljajući Iranove nuklearne centrifuge (Zetter, 2014). Još jedan značajan primer je „Operation Aurora“ napad 2009. godine, koji je ciljao više firmi, uključujući Google, radi pristupa intelektualnoj svojini i e‑mail nalogima aktivista (Council of Foreign Relations, 2010). Nedavni incidenati, poput SolarWinds (2020) i kampanja Nobeliuma (2022), ilustriraju evoluciju APT tehnika koje ciljaju lance snabdevanja i cloud infrastrukturu (Ghanbari et al., 2024).  

APT‑ovi koriste multifazni skup tehnika za ostvarivanje ciljeva. Ovi napadi su dizajnirani oko karakteristika ciljeva i stoga mogu imati mnogo oblika. Često počinju intruzijom u ciljanu sistemsku mrežu putem **spear‑phishing**, **zero‑day ranjivosti** (nepoznate sigurnosne propuste) ili drugih naprednih tehnika, čime se sistem infiltrira neotkriven. Jednom kad su unutar, napadači mogu ostati tiho, nadzirati promet i prikupljati informacije, ili mogu koristiti **lateralni pomak** kroz mrežu, upotrebljavajući **eskalaciju privilegija** kako bi pristupili osetljivim oblastima. **Trajnost** se održava instaliranjem **pozadinskih luka** i **rootkit‑a**, omogućavajući stalni pristup i **ekfiltraciju podataka** bez okidanja sigurnosnih alarma.  

Kada se radi o zločinima, **kibernetički kriminalci** i **grupe državnih subjekata** često se oslanjaju na APT‑ove zbog njihove efikasnosti u ostvarivanju dugoročnih strateških ciljeva. Iako su manje česti od masovno ciljanih napada poput ransomware, APT‑ovi predstavljaju značajan deo **visokog uticaja** cyber incidenata. Njihova kompleksnost i potencijal za značajnu štetu čine ih preferiranim metodama za obaveštajnu aktivnost, krađu intelektualne svojine ili sabotaž.  

### Metrics and numeric limits  
*Not applicable.*

### Key relevant UN convention / multilateral treaty  
Međunarodni pravni instrumenti koji se bave APT‑ovima obuhvataju širi okvir kibernetičke bezbednosti i kibernetičkog zločina. **Budapestka konvencija o kibernetičkom zločinu** (Council of Europe) pruža osnovu za međunarodnu saradnju u borbi protiv kibernetičkih krivičnih delatnosti, uključujući i one koje uključuju APT‑ove.  

Ujedinjenih nacija rezolucije o kibernetičkoj bezbednosti podstiču države članice da preduzmu mere za zaštitu kritične infrastrukture i promovišu razmenu informacija kako bi sprečile kibernetičke pretnje. Međutim, nedostatak specifičnih ugovora fokusiranih isključivo na APT‑ove naglašava izazove u globalnom suzbijanju ovih sofisticiranih i dinamičnih pretnji.  

Pošto APT‑ovi često sprovode državni akteri, njihova regulacija bi pripadala okviru **međunarodnog javnog prava**.

### Drivers  
*Not applicable.*

### Impacts  
*Not applicable.*

### Multi-hazard context  
*Not applicable.*

### Risk Management  
Zaštita od APT‑a je složeno zadatak, s obzirom na količinu vremena, resursa i napora koje napadač spreman je da uloži da bi realizovao svoj plan. Pored toga, s obzirom na raznovrsni pristup koji APT‑i mogu preduzeti, teško je unapred definisati strategije koje bi mogle minimizovati rizik u svim slučajevima. Složenost i promenjivi karakter APT‑ova zahtevaju **prilagođenu i adaptivnu odbrambenu strategiju**, jer nijedno rešenje ne može obuhvatiti sve moguće pretnje. Umesto toga, organizacije moraju integrisati više strategija kako bi osigurale robustnu zaštitu.  

Prema Asharani et al. (2019), strategije odbrane protiv Naprednih trajnih pretnji (APT‑ova) klasifikovani su u tri glavna grupe: **monitoring**, **detekcija** i **mitigacija**. Svaka igra ključnu ulogu u minimiziranju rizika od neovlašćenog pristupa.  

#### Monitoring Methodologies  
Ove metode uključuju korišćenje alata kao što su firewall‑i i antivirusni softver za praćenje različitih delova sistema. Napredni firewall‑i mogu analizirati promet za poznate maliciozne obrasce i potpise, kao i primenjivati **analizu ponašanja** kako bi otkrili abnormalne aktivnosti. Pored toga, praćenje **upotrebe CPU‑a** je važno, jer neobični obrasci u iskorišćavanju resursa mogu ukazivati na sumnjivu aktivnost.  

#### Detection Methodologies  
Ove metode obuhvataju upotrebu različitih **detekcija anomalija**, kao što su **statistička analiza**, neuronske mreže i mašinsko učenje (Hodge i Austin et al., 2004). Ove tehnike pomažu u identifikaciji APT‑ova koji persistentno deluju kroz srednji i dugoročni period. Na primer, **sistem detekcije napada (IDS)** može analizirati mrežni promet kako bi otkrio neobične aktivnosti i upozorio timove za bezbednost na moguće pretnje.  

#### Mitigation Methodology  
Mitigacija APT‑a može se postići reaktivnim i proaktivnim pristupima. Reaktivni metode uključuju identifikaciju potencijalnih putanja napada i ranjivosti u određenom trenutku, predviđanje kritičnih oblasti i procenu njihovog ozbiljnosti. Proaktivne strategije, s druge strane, fokusiraju se na izmišljanje napadača. Ove tehnike ciljaju da zavede napadače i podstaknu ih da promene svoje strategije, čime se smanjuje uticaj pretnje.  

### Monitoring  
*Not Applicable*

### References  
- Alshamrani, A., Myneni, S., Chowdhary, A. i Huang, D. (2019). _A survey on advanced persistent threats: Techniques, solutions, challenges, and research opportunities_. IEEE Communications Surveys & Tutorials, 21(2), 1851‑1877.  
- Brandao, P.R. i Limonova, V. (2021). _Defense methodologies for advanced persistent threats (APTs)_. American Journal of Applied Sciences, 2021.  
- Council on Foreign Relations (CFR). (2005). _Titan Rain_.  
- Council on Foreign Relations (CFR). (2010). _Operation Aurora_.  
- Ghanbari, H., Koskinen, K. i Wei, Y. (2024). _From SolarWinds to Kaseya: The rise of supply chain attacks in a digital world_. Journal of Information Technology Teaching Cases, 0(0).  
- Hodge, V.J. i Austin, J. (2004). _A survey of outlier detection methodologies_. Artificial Intelligence Review, 22, 85‑126.  
- National Institute of Standards and Technology (NIST). (2012). _Special Publication 800-30 Revision 1: Guide for Conducting Risk Assessments_. Gaithersburg, MD: U.S. Department of Commerce.  
- Zetter, K. (2014). _An unprecedented look at Stuxnet, the world’s first digital weapon_. WIRED Magazine.  
```

---