```markdown
### Definizione
Un **attacco alla catena di fornitura** è un evento in cui i prodotti, i servizi o le tecnologie che un'organizzazione riceve sono stati violati o compromessi e vengono successivamente utilizzati per infiltrarsi e compromettere ulteriormente i propri sistemi. (ICO, nessuna data)

### Riferimenti principali
- ICO, nessuna data, *Attacchi alla catena di fornitura*. Accesso 25 gennaio 2025.

### Annotazioni
#### Descrizione scientifica aggiuntiva
In cybersecurity, gli **attacchi alla catena di fornitura** si riferiscono allo sfruttamento delle debolezze di sicurezza all'interno della **catena di fornitura** di un'organizzazione per infiltrarsi nei suoi sistemi e nelle sue reti. Gli aggressori puntano a elementi meno sicuri della catena di fornitura, come **fornitori terzi**, **fornitori** o **provider di servizi cloud**, con l'obiettivo di compromettere la destinazione finale sfruttando l'**interconnessione** degli ecosistemi digitali moderni. Questo metodo consente agli aggressori di bypassare le misure di sicurezza tradizionali sfruttando le relazioni di fiducia.

La storia degli **attacchi alla catena di fornitura** è evoluta parallelamente alla crescente complessità delle reti di fornitura globali. Gli incidenti più significativi includono l'attacco del 2011 a RSA Security, dove gli aggressori hanno compromesso i token SecurID tramite un fornitore per violare i contractor difensivi (Greenberg, 2021). Più recentemente, l'attacco del 2020 a SolarWinds ha dimostrato l'impatto grave di tali violazioni. In questo incidente, actor di minaccia sofisticati hanno inserito codice malevolo negli aggiornamenti software dell'azienda, colpendo numerose organizzazioni governative e private a livello globale e evidenziando le vulnerabilità intrinseche nelle catene di fornitura (Williams, 2020).

### Tecniche comuni
- **Manipolazione degli aggiornamenti software** (es. SolarWinds).  
- **Compromissione dei repository di codice**.  
- **Infezione dei componenti hardware durante la produzione**.  
- **Sfruttamento delle vulnerabilità nei servizi di terze parti**.

Gli aggressori possono inserire codice malevolo negli aggiornamenti software legittimi o sfruttare backdoor nei dispositivi hardware per ottenere accesso non autorizzato.

#### Attacchi basati sull'identità
Molte organizzazioni dipendono dai provider di servizi cloud, portando gli aggressori a focalizzarsi su questi provider in forme uniche di attacco alla catena di fornitura: **attacchi basati sull'identità**. Questi attacchi sfruttano i **permessi estesi** spesso concessi agli account dei provider di servizi, che possono accedere a più ambienti clienti. L'accesso interconnesso aumenta l'impatto potenziale di una compromissione, rendendo i provider di servizi un obiettivo attraente (Microsoft, 2023).

#### Software open‑source
Una delle più significative minacce della catena di fornitura proviene dal software open‑source. Le comunità open‑source offrono numerosi **moduli** e **pacchetti** ampiamente usati dalle imprese globalmente, inclusi quelli presenti nelle catene di fornitura. Tuttavia, poiché il software open‑source spesso manca di proprietà chiara e di garanzie di sicurezza, introduce frequentemente vulnerabilità nelle **architetture di sicurezza** (Forbes, 2022).

#### Firma del codice e aggiornamenti
Un'altra tecnica prominente include l’**hijacking degli aggiornamenti** e la compromissione della **firma del codice**. I venditori di software distribuiscono regolarmente aggiornamenti da server centralizzati per mantenere e migliorare i loro prodotti. Gli attori di minaccia possono sfruttare questo processo infiltrando la rete del venditore per inserire malware in un aggiornamento o modificarlo per ottenere il controllo non autorizzato sulla funzionalità del software. La firma del codice, meccanismo usato per verificare l’autenticità e l’integrità del software, è un altro obiettivo critico. Gli attori malevoli indeboliscono questo processo utilizzando certificati auto‑firmati, sfruttando controlli di accesso mal configurati o compromettendo i sistemi di firma. Impersonando fornitori di fiducia e incorporando codice malevolo negli aggiornamenti, gli aggressori possono eseguire con successo attacchi altamente ingannevoli e dannosi (NIST, 2021).

Nel 2023, gli attori hanno compromesso l’app desktop di 3CX attraverso installatori infetti, diffusendo malware tramite un ampiamente usato sistema VoIP (Fortiguard, 2023).

### Motivo di diffusione
Gli attori malevoli si affidano sempre più agli attacchi alla catena di fornitura a causa del loro alto impatto e della difficoltà di rilevamento. La complessità delle catene di fornitura moderne e la dipendenza da fornitori di terze parti offrono numerose opportunità di sfruttamento, rendendo gli attacchi alla catena di fornitura una preoccupazione significativa in cybersecurity. Inoltre, gli attacchi alla catena di fornitura sono spesso mirati; pertanto, solo gli attori con risorse e capacità superiori possono (di solito) condurli.

### Impatti
- Frode  
- Furto  

### Gestione del rischio
Difendersi dagli **attacchi alla catena di fornitura** richiede un approccio completo che includa:
1. **Vetting rigoroso dei fornitori**  
2. **Implementazione di standard di sicurezza severi**  
3. **Monitoraggio continuo**  
4. **Collaborazione tra organizzazioni e partner**

Poiché molti attacchi dipendono da fornitori esterni con dipendenze complesse nei loro strumenti e servizi, raggiungere una protezione completa può essere difficile. Tuttavia, le organizzazioni possono adottare strategie proattive per difendersi dai vettori di attacco più comuni (Cloudflare, nessuna data).

#### Valutazione del rischio di terze parti
- Testare il software di terze parti prima del deployment  
- Richiedere ai fornitori di rispettare specifiche politiche di sicurezza  
- Implementare una **Content Security Policy (CSP)** per controllare le risorse eseguibili nel browser  
- Usare la **Subresource Integrity (SRI)** per rilevare contenuti JavaScript sospetti  

#### Zero Trust
Il modello **Zero Trust** garantisce che tutti gli utenti—dipendenti, contractor e fornitori—siano continuamente verificati e monitorati all’interno della rete aziendale. Verificando l’identità e i privilegi di utenti e dispositivi, Zero Trust previene che gli aggressori sfruttino credenziali legittime rubate per infiltrarsi nell'organizzazione.

#### DevSecOps
La sicurezza della catena di fornitura sfrutta **DevSecOps** per difendersi dagli attacchi, iniziando con la scoperta di tutti i componenti, ottenendo visibilità sulla catena di fornitura e proteggendo i componenti delle applicazioni cloud‑native. Integrando la sicurezza in ogni fase dello sviluppo, DevSecOps garantisce un deployment di sicurezza in tempo reale allineato ai requisiti aziendali (GitLab, nessuna data).

### Riferimenti
- Cloudflare, nessuna data, *What is supply chain attack?* Accesso 16 gennaio 2025.  
- Forbes, 2022, *Mitigating the risk of supply chain attacks in the age of cloud computing*. Accesso 15 gennaio 2025.  
- FortiGuard Labs, 2023, *Threat Signal Report: Supply Chain Attack Through 3CX Desktop App*. Accesso 15 gennaio 2025.  
- GitLab, nessuna data, *What is DevSecOps?* Accesso 16 gennaio 2025.  
- Greenberg, A., 2021, *The Full Story of the Stunning RSA Hack Can Finally Be Told*. Accesso 15 gennaio 2025.  
- Information Commissioner’s Office (ICO), nessuna data, *Supply chain attacks*. Accesso 15 gennaio 2025.  
- Microsoft, 2023, *Announcing Microsoft Defender for Cloud Capabilities to Counter Identity-Based Supply Chain Attacks*. Microsoft Tech Community. Accesso 15 gennaio 2025.  
- National Institute of Standards and Technology (NIST), 2021, *Defending Against Software Supply Chain Attacks*. Accesso 16 gennaio 2025.  
- Williams, J., 2020, *What You Need to Know About the SolarWinds Supply-Chain Attack*. SANS Institute.

> **Nota**: Tutti i termini tecnici sono conformi al vocabolario controllato per la riduzione del rischio di disastro (DRR) e rispettano le specifiche di traduzione discipline‑specifica.
```