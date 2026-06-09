---

### Definition

La **Negazione di servizio (DoS)** è la prevenzione dell'accesso autorizzato alle risorse o il ritardo delle operazioni critiche in termini di tempo. (Il ritardo può essere misurato in millisecondi o ore, a seconda del tempo di risposta del servizio) (NIST, 2017).

### Primary reference(s)

NIST, 2017. **Sicurezza informatica**. Un’introduzione alla sicurezza delle informazioni. **Pubblicazione speciale** 800-12 Revision. National Institute of Standards and Technology (NIST). Accesso 25 gennaio 2025.

### Annotations

#### Additional scientific description

Una **Negazione di servizio (DoS)** rende un sistema informatico o una rete non disponibile per i suoi utenti previsti sovraccaricandolo con input esterni (ad es. traffico web in arrivo). In tali casi il termine può evolvere in **Negazione di servizio distribuita (DDoS)** o nell’esplo​itamento delle vulnerabilità per esaurire le risorse computazionali. Questo disturbo impedisce agli utenti l'accesso ai servizi e alle informazioni, causando impatti operativi e finanziari significativi (CISA, 2021).

Gli attacchi DDoS rimangono un fastidio persistente su Internet. Essi sfruttano il fatto che Internet manca di controllo di accesso centralizzato. Poiché questa vulnerabilità era una decisione di progettazione fondamentale dell’internet primitivo, gli attacchi DDoS sono persistenti. I primi attacchi erano correlati alla cultura hacker, ma il loro focus si è rapidamente spostato sull’esplo​itamento commerciale. Ci sono stati anche numerosi usi politici di DDoS, inclusi guerra cibernetica, hacktivismo e terrorismo (Brooks et al., 2021).

L’uso di DoS e DDoS è ben documentato nella storia della sicurezza informatica. Attacchi primi risalgono all’era dell’internet primitivo, con un primo incidente in Francia nel 1995, seguito l’anno successivo da un grande incidente contro Panix, un provider di servizi Internet con sede a New York City (Brooks et al., 2021). Nel corso degli anni, questi attacchi sono evoluti in termini di complessità e scala, con l’esempio dell’attacco botnet del 2016 alimentato da malware Mirai, che ha sfruttato dispositivi IoT per lanciare un massiccio attacco DDoS, interroppendo principali siti web a livello mondiale (CISA, 2017).

DoS può derivare da errori umani (come configurazioni errate), da altri incidenti (come guasti di alimentazione) o da attacchi deliberati. Diverse tecniche vengono impiegate negli attacchi DoS. La distinzione principale riguarda la differenza tra attacchi DoS e DDoS. Un attacco DoS di solito proviene da una singola fonte che mira a un sistema, mentre un attacco DDoS coinvolge più sistemi compromessi, spesso formando un botnet, per inondare simultaneamente il bersaglio, rendendo la difesa significativamente più difficile. L’aumento del numero di dispositivi connessi – specialmente nel contesto del boom IoT – aumenta anche il rischio di attacchi DDoS poiché ogni dispositivo connesso può potenzialmente diventare parte di un botnet.

Una **condizione di negazione di servizio** inonda l’host o la rete target con traffico finché il bersaglio non può rispondere o semplicemente crasha, influenzando e‑mail, siti web, account online (ad es. bancario) o altri servizi. Gli attacchi DoS possono costare un’organizzazione sia tempo che denaro mentre le sue risorse e servizi sono inaccessibili. Gli attacchi DoS possono essere ulteriormente categorizzati in base al metodo: gli attacchi basati sul volume sopraffanno la banda di una rete (ad es. inondando un sito web con traffico eccessivo), mentre gli attacchi che sfruttano limitazioni computazionali inviano richieste malformate o avviano loop infiniti per esaurire le risorse computazionali.

Gli attacchi DoS possono scalare fino a diventare pericoli nazionali quando mirano a infrastrutture critiche. Un precedente è l’attacco cibernetico del 2007 contro l’Estonia, dove attacchi DDoS coordinati paralizzarono siti governativi, bancari e mediatici, causando disagi diffusi e evidenziando le vulnerabilità a livello nazionale (Ottis, 2008). Gli attacchi DoS sono comunemente impiegati da attori malevoli per via della relativa facilità di esecuzione e del potenziale di grande disastro. Ogni anno si registrano grandi numeri di incidenti DoS e DDoS, rendendoli una delle forme di attacco cibernetico più diffuse (Bergamini de Neira et al., 2023). Nel 2024, NETSCOUT ha riferito oltre 13 milioni di attacchi DDoS a livello globale, con tendenze in aumento di attacchi multi‑vettore (NETSCOUT, 2024).

#### Drivers

Uno dei fattori più critici che porta all’aumento dei DDoS è la proliferazione di dispositivi IoT non sicuri. La connettività estesa e i protocolli di sicurezza insufficienti nelle reti moderne forniscono terreno fertile per gli aggressori a sfruttare vulnerabilità e lanciare attacchi DoS di successo.

#### Impacts

Una **negazione di servizio (DoS)** si verifica quando gli utenti legittimi non possono accedere a sistemi informativi, dispositivi o altre risorse di rete a causa delle azioni di un attore minaccioso informatico malevolo. I servizi colpiti possono includere e‑mail, siti web, account online (ad es. bancario) o altri servizi che dipendono dal computer o dalla rete interessati (CISA, 2021). Gli attacchi DDoS possono aggravare guasti del sistema sanitario o finanziario durante disastri naturali o pandemie (ENISA, 2023).

#### Multi-hazard context

Non disponibile

#### Risk Management

La riduzione del rischio di DoS implica una combinazione di misure tecnologiche e strategiche. L’implementazione di robusti protocolli di sicurezza di rete, l’utilizzo di sistemi di rilevamento e prevenzione delle intrusioni (IDPS) e l’adozione di soluzioni di sicurezza guidate dall’IA migliorano la resilienza dell’organizzazione. Inoltre, strategie come limitazione del tasso, filtraggio del traffico e l’uso di reti di distribuzione di contenuti (CDN) aiutano a mitigare l’impatto degli attacchi. L’intelligenza artificiale può anche svolgere un ruolo cruciale nella protezione contro DoS: i sistemi IA analizzano il traffico di rete per identificare anomalie, permettendo la rilevazione e la risposta in tempo reale, migliorando la capacità di filtrare traffico malevolo, allocando risorse dinamicamente e prevedendo minacce potenziali basate su schemi e comportamenti. L’ITU migliora la prontezza della sicurezza informatica, la protezione e le capacità di risposta a incidenti degli Stati membri mediante l’organizzazione di CyberDrills a livello regionale e internazionale (ITU, no date). Un CyberDrill è un evento annuale durante il quale si simulano attacchi cibernetici, incidenti di sicurezza delle informazioni o altri tipi di discontinuità per testare le capacità cibernetiche di un’organizzazione, dalla capacità di rilevare un incidente di sicurezza alla capacità di rispondere adeguatamente e minimizzare eventuali impatti correlati. Attraverso i CyberDrills, i partecipanti possono convalidare politiche, piani, procedure, processi e capacità che consentono la preparazione, la prevenzione, la risposta, il recupero e la continuità delle operazioni.

#### Monitoring

Non disponibile

---

**References**

- Bergamini de Neira, A., Kantarci, B. & Nogueira, M., 2023. *Distributed denial of service attack prediction: Challenges, open issues and opportunities*. Computer Networks, 222(C), Feb. DOI: 10.1016/j.comnet.2022.109553. Accessed 3 April 2025.
- Brooks, R.R., Yu, L., Ozcelik, I., Oakley, J. & Tusing, N., 2022. *Distributed Denial of Service (DDoS): A History*. IEEE Annals of the History of Computing, 44, pp.44–54. Accessed 3 April 2025.
- Cybersecurity and Infrastructure Security Agency (CISA), 2017. *Heightened DDoS Threat Posed by Mirai and Other Botnets*. Accessed 3 April 2025.
- Cybersecurity and Infrastructure Security Agency (CISA), 2021. *Understanding Denial-of-Service Attacks*. Accessed 3 April 2025.
- European Union Agency for Cybersecurity (ENISA), 2023. *ENISA Threat Landscape 2023*. Accessed 3 April 2025.
- International Telecommunication Union (ITU), no date. *CyberDrills*. Accessed 3 April 2025.
- NETSCOUT, 2024. *Threat Intelligence Report 2024*. Accessed 3 April 2025.
- Ottis, R., 2008. *Analysis of the 2007 Cyber Attacks against Estonia from the Information Warfare Perspective*. In: *Proceedings of the 7th European Conference on Information Warfare and Security*, Plymouth, 2008. Reading: Academic Publishing Limited, pp.163–168. Accessed 3 Apr. 2025.
- National Institute of Standards and Technology (NIST), 2017. *Computer Security: An Introduction to Information Security*. Special Publication 800-12 Revision 1. Gaithersburg, MD: U.S. Department of Commerce. Accessed 3 Apr. 2025.

*© 2026 – Technical Translator Agent.*