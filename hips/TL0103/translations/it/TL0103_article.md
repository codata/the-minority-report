### Definizione
Una **Minaccia Persistente Avanzata (APT)** è creata da un avversario con livelli di competenza sofisticata e risorse significative, permettendogli, tramite l’utilizzo di molteplici vettori di attacco (ad es. cibernetico, fisico e inganno), di generare opportunità per raggiungere i propri obiettivi (NIST, 2012).

### Riferimento principale
National Institute for Standards and Technology, 2012. Guide for conducting risk assessments. DOI:10.6028/NIST.SP.800-30r1. Accesso: 25 gennaio 2025.

### Annotazioni
#### Descrizione scientifica aggiuntiva
Una **Minaccia Persistente Avanzata (APT)** nella cibersicurezza si riferisce a un attacco informatico avanzato e prolungato mirato dove, spesso, un utente non autorizzato accede a una rete e rimane non rilevato per un lungo periodo. L’obiettivo principale delle APT è tipicamente osservare l’attività della rete, rubare dati o causare interruzioni, piuttosto che infliggere danni immediati. Questa minaccia è considerata “avanzata” a causa delle tecniche avanzate impiegate per sfruttare vulnerabilità, e “persistente” per l’impegno continuo volto a raggiungere un obiettivo specifico.

Uno degli incidenti più antichi riconosciuti fu l’attacco Titan Rain tra il 2003 e il 2006, dove gli aggressori infiltravano le reti di difesa statunitensi per rubare informazioni sensibili (Council of Foreign Relations 2005). La scoperta del worm Stuxnet nel 2010 segnò un’importante escalation, dimostrando la capacità delle APT di causare danni fisici mirati alle centrifughe nucleari iraniane (Zetter 2014). Un altro esempio notevole è l’attacco Operation Aurora del 2009, che mirava a molte aziende, tra cui Google, per accedere a proprietà intellettuali e conti e-mail di attivisti (Council of Foreign Relations 2010). Recenti incidenti, come SolarWinds (2020) e le campagne di Nobelium (2022), illustrano tecniche APT evolute che colpiscono le catene di approvvigionamento e le infrastrutture cloud (Ghanbari et al., 2024).

Le APT impiegano una vasta gamma di tecniche per raggiungere i propri obiettivi. Questi attacchi sono progettati attorno alle caratteristiche dei loro bersagli e possono assumere molte forme. Spesso, questi iniziano con un'infiltrazione nella rete target tramite spear-phishing, vulnerabilità zero-day o altre tecniche avanzate per infiltrarsi nei sistemi senza essere rilevati. Una volta all'interno, gli aggressori possono rimanere silenziosi, monitorando il traffico e raccogliendo informazioni, o utilizzare il movimento laterale per navigare nella rete, ricorrendo all'escalation dei privilegi per accedere a zone sensibili. La persistenza viene mantenuta mediante il deployment di backdoor e rootkit, consentendo accesso continuo e l'esfiltrazione dei dati senza scatenare allarmi di sicurezza.

Gli attori malevoli, in particolare i gruppi statali e i cybercriminali organizzati, si affidano frequentemente alle APT per la loro efficacia nel raggiungere obiettivi strategici a lungo termine. Mentre gli attacchi ransomware sono più comuni, le APT rappresentano una percentuale significativa di incidenti cibernetici ad alto impatto. La loro complessità e il potenziale di danno sostanziale le rendono i metodi preferiti per lo spionaggio, il furto di proprietà intellettuale o il sabotaggio.

### Metriche e limiti numerici
Non applicabile.

### Convenzione/un trattato UN rilevante
Gli strumenti legali internazionali che affrontano le APT rientrano in cornici più ampie di cibersicurezza e cybercrimine. La Convenzione di Budapest del Consiglio d’Europa sul cybercrimine fornisce una base per la cooperazione internazionale nella lotta contro i reati informatici, inclusi quelli che coinvolgono le APT. Le risoluzioni delle Nazioni Unite sulla cibersicurezza incoraggiano gli Stati membri ad adottare misure per proteggere le infrastrutture critiche e promuovere lo scambio di informazioni per prevenire le minacce informatiche. Tuttavia, l’assenza di trattati specifici focalizzati esclusivamente sulle APT evidenzia le sfide nell’affrontare minacce sofisticate ed evolutive a livello globale.

Dal momento che le APT sono spesso realizzate da attori statali, la loro regolamentazione rientrerebbe nell’ambito del diritto pubblico internazionale.

### Driver
Non applicabile.

### Impatti
Non applicabile.

### Contesto multi-hazard
Non applicabile.

### Gestione del rischio
Difendersi contro una **Minaccia Persistente Avanzata (APT)** è un compito complesso, considerando la quantità di tempo, risorse e sforzi che l’aggressore è disposto a investire per completare la sua operazione. Inoltre, dato l’approccio diversificato che le APT possono adottare, è difficile prescrivere in anticipo strategie per ridurre il rischio applicabili a tutti i casi. La natura complessa ed evolutiva delle APT richiede un approccio di difesa su misura e adattivo, poiché nessuna singola soluzione può affrontare tutte le potenziali minacce. Al contrario, le organizzazioni devono integrare molteplici strategie per garantire una protezione robusta. Secondo Asharani et al. (2019), le strategie di difesa contro le **Minacce Persistenti Avanzate (APT)** si dividono in tre gruppi principali: monitoraggio, rilevamento e mitigazione.

#### Metodologie di monitoraggio
Queste comportano l’utilizzo di strumenti come firewall e antivirus per osservare varie parti del sistema. I firewall avanzati sono in grado di analizzare il traffico alla ricerca di modelli e firme maligne conosciute, oltre a impiegare l’analisi comportamentale per individuare attività anomale. Inoltre, il monitoraggio dell’utilizzo della CPU è importante, poiché schemi insoliti nell’utilizzo delle risorse possono indicare comportamenti sospetti.

#### Metodologie di rilevamento
Queste includono l’impiego di varie tecniche di rilevamento di anomalie, come l’analisi statica, le reti neurali e gli approcci di apprendimento automatico (Hodge and Austin et al., 2004). Tali tecniche aiutano a identificare le APT che persistono a lungo termine. Ad esempio, un Sistema di Rilevazione di Intrusioni (IDS) può analizzare il traffico di rete per individuare attività insolite e avvisare i team di sicurezza di potenziali minacce.

#### Metodologia di mitigazione
La mitigazione delle APT può essere raggiunta tramite approcci reattivi e proattivi. I metodi reattivi coinvolgono l’identificazione di percorsi di attacco e vulnerabilità in un dato momento, la previsione delle aree critiche e la valutazione della loro gravità. Le strategie proattive, al contrario, si concentrano sull’inganno degli aggressori. Tali tecniche mirano a ingannare gli intrusi e costringerli a modificare le proprie strategie di attacco, riducendo così l’impatto della minaccia.

### Monitoraggio
Non applicabile

### Riferimenti
Alshamrani, A., Myneni, S., Chowdhary, A. e Huang, D., 2019. A survey on advanced persistent threats: Techniques, solutions, challenges, and research opportunities. *IEEE Communications Surveys & Tutorials*, vol. 21, no. 2, pp. 1851‑1877, Secondquarter 2019, doi: 10.1109/COMST.2019.2891891. Accesso: 16 gennaio 2025.
Brandao, P.R. e Limonova, V., 2021. Defense methodologies for advanced persistent threats (APTs). *American Journal of Applied Sciences*, 2021. DOI:10.3844/ajassp.2021.207.212. Accesso: 16 gennaio 2025.
Council on Foreign Relations (CFR), 2005. Titan Rain. Accesso: 16 gennaio 2025.
Council on Foreign Relations (CFR), 2010. Operation Aurora. Accesso: 16 gennaio 2025.
Ghanbari, H., Koskinen, K. e Wei, Y., 2024. From SolarWinds to Kaseya: The rise of supply chain attacks in a digital world. *Journal of Information Technology Teaching Cases*, 0(0). DOI: 10.1177/20438869241299823. Accesso: 16 gennaio 2025.
Hodge, V.J. e Austin, J., 2004. A survey of outlier detection methodologies. *Artificial Intelligence Review*, 22, pp. 85‑126. Accesso: 16 gennaio 2025.
National Institute of Standards and Technology (NIST), 2012. Special Publication 800‑30 Revision 1: Guide for Conducting Risk Assessments. Gaithersburg, MD: U.S. Department of Commerce. Accesso: 16 gennaio 2025.
Zetter, K., 2014. An unprecedented look at Stuxnet, the world’s first digital weapon. *WIRED Magazine*. Accesso: 16 gennaio 2025.

Cite this [Copy citation]