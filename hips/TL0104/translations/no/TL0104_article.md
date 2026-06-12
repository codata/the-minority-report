### Definisjon  
Denial of Service (DoS) er forhindrelsen av autorisert tilgang til ressurser eller forsinkelsen av tidskrevende operasjoner. (Tidkrevende kan være millisekunder eller timer, avhengig av tjenesten som tilbys) (NIST, 2017).

### Primær referanse  
NIST, 2017. Computer Security. An Introduction to Information Security. Special Publication 800‑12 Revision. National Institute of Standards and Technology (NIST). Accessed 25 January 2025.

### Kommentarer  
#### Ytterligere vitenskapelig beskrivelse  
En **Denial of Service (DoS)** gjør et datasystem eller nettverk utilgjengelig for sine tiltenkte brukere ved å overvelde det med eksterne innkommende trafikk (f.eks. webtrafikk), og kan da kalles **Distributed Denial of Service (DDoS)** eller utnytte sårbarheter for å tømme beregningsressurser.  
**Distributed denial of service (DDoS)**‑angrep forblir en vedvarende plage på Internett. De utnytter faktoren at Internett mangler sentralisert tilgangskontroll. Siden denne sårbarheten var en kjerne‑designbeslutning i den tidlige internett‑perioden, har DDoS‑angrep vedvart. Tidlige angrep var knyttet til hackerkultur, men fokuset endret seg raskt til kommersiell utnyttelse. Det har også vært flere politiske bruksområder for DDoS, inkludert cybersoldat, hacktivisme og terrorisme (Brooks et al., 2021).  
Bruken av DoS og DDoS er godt dokumentert i cybersikkerhetens historie. Tidlige angrep finnes allerede i den tidlige internett‑æraen, med en av de første hendelsene i Frankrike i 1995, etterfulgt året etter av en stor hendelse mot Panix, en internett‑tjenesteleverandør basert i New York City (Brooks et al., 2021). Over årene har disse angrepene utviklet seg i kompleksitet og skala, illustrert av botnet‑angrepet drevet av Mirai‑malware i 2016, som utnyttet Internet of Things (IoT)-enheter for å lansere et massivt DDoS‑angrep som forstyrret store nettsteder over hele verden (CISA, 2017).  
DoS kan skyldes menneskelige feil (som feilkonfigurasjon), andre hendelser (som strømbrudd) eller bevisste angrep. Ulike teknikker benyttes i DoS‑angrep. Hovedforskjellen ligger mellom DoS‑ og DDoS‑angrep. Et DoS‑angrep kommer vanligvis fra en enkelt kilde som retter seg mot et system, mens et DDoS‑angrep involverer flere kompromitterte systemer, ofte som danner et botnet, for å flomme målrettet samtidig, noe som gjør forsvaret betydelig vanskeligere. Det økende antallet tilkoblede enheter – spesielt i forbindelse med IoT‑boom – øker også risikoen for DDoS‑angrep, ettersom hver tilkoblet enhet potensielt kan bli en del av et botnet.  
Et **Denial of Service (DoS)**‑angrep oppstår når legitime brukere ikke kan få tilgang til informasjonssystemer, enheter eller andre nettverksressurser på grunn av handlingene til en ondsinnet cybertrusselaktør. En **Denial of Service**‑tilstand flommer den målrettede verten eller nettverket med trafikk til det ikke lenger kan svare eller krasjer helt, og påvirker e‑post, nettsteder, online‑kontoer (f.eks. banktjenester) eller andre tjenester. DoS‑angrep kan koste en organisasjon både tid og penger mens deres ressurser og tjenester er utilgjengelige.  
DoS‑angrep kan kategoriseres videre etter metode: volumetriske angrep overvelder båndbredden til et nettverk (f.eks. flom av et nettsted med overdrevet trafikk), mens angrep som utnytter beregningsressurser innebærer å sende ødelagte forespørsler eller starte uendelige løkker for å tømme beregningsressurser. DoS‑angrep kan eskalere til nasjonale farer når de retter seg mot kritisk infrastruktur. Et eksempel er 2007‑cyberangrepene mot Estland, der koordinerte DDoS‑angrep ødela statlige, bank- og medienettsteder, og førte til omfattende forstyrrelser og belysning av sårbarheter på nasjonalt nivå (Ottis, 2008).  
DoS‑angrep brukes ofte av ondsinnede aktører på grunn av deres relative enkelhet og potensialet for betydelig forstyrrelse. Hvert år registreres et stort antall DoS‑ og DDoS‑hendelser, noe som gjør dem til en av de mest utbredte formene for cyberangrep (Bergamini de Neira et al., 2023). I 2024 rapporterte NETSCOUT over 13 millioner DDoS‑angrep globalt, med økende trender i multivektor‑angrep (NETSCOUT, 2024).

### Drivere  
En av de mest kritiske faktorene som fører til økningen i DDoS er spredningen av usikrede IoT‑enheter. Den omfattende tilkoblingen og utilstrekkelige sikkerhetsprotokoller i moderne nettverk gir fruktbart terreng for angripere å utnytte sårbarheter og lansere vellykkede DoS‑angrep.

### Påvirkning  
Et **Denial of Service (DoS)**‑angrep oppstår når legitime brukere ikke kan få tilgang til informasjonssystemer, enheter eller andre nettverksressurser på grunn av handlingene til en ondsinnet cybertrusselaktør. Påvirkede tjenester kan inkludere e‑post, nettsteder, online‑kontoer (f.eks. banktjenester) eller andre tjenester som er avhengige av den berørte datamaskinen eller nettverket (CISA, 2021). DDoS‑angrep kan forverre helsesystemer eller finansielle systemer under naturkatastrofer eller pandemier (ENISA, 2023).

### Multi‑hazard‑kontekst  
Ikke tilgjengelig

### Risikostyring  
Minskning av risikoen for DoS innebærer en kombinasjon av teknologiske og strategiske tiltak. Implementering av robuste nettverkssikkerhetsprotokoller, bruk av intrusjonsdeteksjon‑ og forebyggingssystemer, samt adopsjon av AI‑drevne sikkerhetsløsninger forbedrer en organisasjons motstandsdyktighet. I tillegg hjelper strategier som rate limiting, trafikkfiltrering og bruk av content delivery networks med å dempe virkningen av angrep. Kunstig intelligens kan også spille en kritisk rolle i å beskytte mot DoS. AI‑systemer kan analysere nettverkstrafikk for å identifisere anomalier, muliggjøre sanntidsoppdagelse og respons, forbedre evnen til å filtrere ondsinnet trafikk, allokere ressurser dynamisk og forutsi potensielle trusler basert på mønstre og atferd. ITU forbedrer cybersikkerhetsberedskap, beskyttelse og hendelsesresponskapasitet for medlemsstater gjennom CyberDrills på regionalt og internasjonalt nivå (ITU, no date). En CyberDrill er et årlig arrangement der cyberangrep, informasjonssikkerhetshendelser eller andre former for forstyrrelser simuleres for å teste en organisasjons cyberkapasiteter, fra å oppdage en sikkerhetshendelse til evnen til å respondere hensiktsmessig og minimere eventuell tilknyttet påvirkning. Gjennom CyberDrills kan deltakerne validere retningslinjer, planer, prosedyrer, prosesser og kapasiteter som muliggjør forberedelse, forebygging, respons, gjenoppretting og kontinuitet av drift.

### Overvåking  
Ikke tilgjengelig

### Referanser  
Bergamini de Neira, A., Kantarci, B. and Nogueira, M., 2023. Distributed denial of service attack prediction: Challenges, open issues and opportunities. Computer Networks, 222(C), Feb. DOI: 10.1016/j.comnet.2022.109553 Accessed 3 April 2025.  
Brooks, R.R., Yu, L., Ozcelik, I., Oakley, J. and Tusing, N., 2022. Distributed Denial of Service (DDoS): A History. IEEE Annals of the History of Computing, 44, pp.44–54. Accessed 3 April 2025.  
Cybersecurity and Infrastructure Security Agency (CISA), 2017. Heightened DDoS Threat Posed by Mirai and Other Botnets. Accessed 3 April 2025.  
Cybersecurity and Infrastructure Security Agency (CISA), 2021. Understanding Denial-of-Service Attacks. Accessed 3 April 2025.  
European Union Agency for Cybersecurity (ENISA), 2023. ENISA Threat Landscape 2023. Accessed 3 April 2025.  
International Telecommunication Union (ITU), no date. CyberDrills. Accessed 3 April 2025.  
NETSCOUT, 2024. Threat Intelligence Report 2024. Accessed 3 April 2025.  
Ottis, R., 2008. Analysis of the 2007 Cyber Attacks against Estonia from the Information Warfare Perspective. In: Proceedings of the 7th European Conference on Information Warfare and Security, Plymouth, 2008. Reading: Academic Publishing Limited, pp.163–168. Accessed 3 Apr. 2025.  
National Institute of Standards and Technology (NIST), 2017. Computer Security: An Introduction to Information Security. Special Publication 800‑12 Revision 1. Gaithersburg, MD: U.S. Department of Commerce. Accessed 3 Apr. 2025.  
Cite this [Copy citation]