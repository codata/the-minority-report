```markdown
### Definizione

Il malware è un termine sintetico per le diverse forme di software malevole progettato per infiltrarsi e infettare i computer, solitamente senza la consapevolezza del proprietario (ITU, 2008).

### Riferimento principale

ITU, 2008. *Studio ITU sugli aspetti finanziari della sicurezza delle reti: Malware e Spam*. International Telecommunication Union (ITU). Accesso 31 ottobre 2024.

### Annotazioni

#### Descrizione scientifica aggiuntiva

Il malware è un portmanteau di “malicious software”. Si riferisce a software progettato per causare danni, interrompere le operazioni o ottenere accesso non autorizzato a sistemi informatici, reti o dispositivi. Comprende vari tipi di software dannoso, ognuno con caratteristiche specifiche e metodi di propagazione. Il malware è spesso classificato in “famiglie” (che indicano un tipo specifico di malware con caratteristiche uniche) e “varianti” (di solito una versione diversa di codice in una particolare famiglia) (International Telecommunication Union, 2008).

**Tipi di malware:**
- **Virus:** si attaccano a programmi legittimi e si propagano da dispositivo a dispositivo quando tali programmi sono eseguiti.
- **Worms:** si replicano per diffondersi a altri sistemi senza necessità di un programma host.
- **Cavallo di Troia:** si mascherano come software benigni per ingannare gli utenti a eseguirli, compromettendo così il sistema.
- **Ransomware:** i criminali informatici cifrano i dati e richiedono pagamento in cambio delle chiavi di decrittazione.
- **Spyware:** raccoglie informazioni in modo clandestino monitorando le attività degli utenti.
- **Programma di cancellazione (wiper):** elimina o corrompe permanentemente i dati memorizzati su macchine infettate.
- **Rootkit:** consente accesso non autorizzato nascondendo la propria presenza all’interno del sistema.

La storia del malware risale almeno agli anni ’80, quando furono creati i primi esempi (Milošević, 2014). Incidenti notevoli includono il Morris Worm nel 1988, che disturbò una parte significativa dell’internet primordiale, e l’attacco ransomware WannaCry nel 2017, che colpì organizzazioni in tutto il mondo.

Il malware può essere distribuito attraverso molteplici vettori, come allegati email (in particolare nel contesto di attacchi di phishing), siti web malevoli, download di software infetti, o tramite vulnerabilità di rete. Oggi gli aggressori possono sfruttare l’intelligenza artificiale per creare malware avanzati, come quelli polimorfi, che possono alterare il loro codice per sfuggire alla rilevazione da parte delle misure di sicurezza tradizionali. Inoltre, il malware fileless (senza file) è una minaccia crescente grazie alla sua capacità di sfuggire alla rilevazione dai tradizionali programmi antivirus (Liu et al., 2024). A differenza del malware standard che dipende da file o eseguibili, il malware fileless sfrutta gli strumenti di sistema legittimi e sfrutta file, applicazioni e servizi di sistema esistenti per implementare attività malevole. Il malware fileless può entrare nei sistemi attraverso molteplici vettori, come email di phishing, siti web compromessi o attacchi di watering hole. Una volta ottenuto l'accesso, può rubare informazioni sensibili e diffondere l’infezione in tutta la rete verso pericoli nazionali e internazionali quando altri sistemi sono bersaglio deliberatamente o altrimenti, ad esempio fornitori terzi che vengono bersaglio, o uno dei loro fornitori o subfornitori. Un precedente è lo worm Stuxnet scoperto nel 2010, progettato per sabotare le strutture nucleari dell’Iran. Questo malware sofisticato ha evidenziato il potenziale delle armi informatiche di causare danni fisici e disturbare la sicurezza nazionale (Zetter, 2014).

I malintenzionati si affidano frequentemente al malware grazie alla sua versatilità e efficacia. Il malware rimane una delle forme più comuni di attacco informatico, con milioni di nuovi campioni di malware rilevati annualmente (Statista, 2024). Serve a vari scopi, dal guadagno finanziario tramite ransomware alla spionaggio e al disturbo dei servizi.

### Metriche e limiti numerici

Oltre 1 miliardo di nuove varianti di malware sono state rilevate globalmente nel 2023 (Statista, 2024).

### Convenzione/Trattato UN rilevante

Gli strumenti legali internazionali che trattano il malware sono inclusi nei più ampi quadri di cybercrime. La Convenzione di Budapest sul cybercrime del Consiglio d’Europa fornisce linee guida per la cooperazione internazionale nella lotta contro il cybercrime, inclusi i reati che coinvolgono la creazione, la distribuzione o l’uso di malware. Il Codice di Prassi del Processo Pall Mall per gli Stati aggiornato 2025 è un dialogo globale inclusivo per affrontare la proliferazione e l’uso irresponsabile di strumenti e servizi di intrusione informatica commerciale.

### Motivazioni

- Vulnerabilità del software  
- Aumento della dipendenza digitale  
- Economia del cybercrime  
- Tensioni geopolitiche  

### Impatto

Gli attacchi di malware possono escadere a pericoli nazionali quando mirano all’infrastruttura critica o ai sistemi governativi. Un precedente è lo worm Stuxnet scoperto nel 2010, progettato per sabotare le strutture nucleari dell’Iran. Questo malware sofisticato ha evidenziato il potenziale delle armi informatiche di causare danni fisici e disturbare la sicurezza nazionale.

### Contesto multi‑pericolo

Il malware può causare una significativa interruzione dei servizi, perdita finanziaria, potenziale perdita di entrate, perdita o furto di dati e intelligence, perdita o danni all’infrastruttura IT, danni reputazionali alle organizzazioni e agli individui, e può comportare significativi pagamenti di risarcimento e multe regolamentari. Possono inoltre aumentare i costi di recupero. Inoltre, gli impatti di un attacco di malware di successo possono contribuire alla perdita di fiducia pubblica nelle organizzazioni, nei politici e nel settore pubblico. Esiste anche la minaccia di ulteriori sfruttamenti se le informazioni vengono compromesse. I sistemi software sono interconnessi con i sistemi fisici. Il malware può essere utilizzato per abilitare l'accesso a sistemi che possono aprire altri pericoli come aumentare i prodotti chimici nelle strutture di distribuzione dell’acqua per avvelenare grandi parti della popolazione alterando i sistemi dell’acqua. Ciò è stato tentato in Florida (2021), California (2021), Israele (2020) e USA (2016) (Sikder et al., 2023).

### Gestione del rischio

Difendersi dal malware richiede, prima di tutto, la consapevolezza dell’utente poiché la maggior parte del malware è attivata dopo un input generato dall’utente (come cliccare su link fraudolenti o compromessi). Le misure tecniche, tra cui l’uso di software antivirus e anti‑malware, aggiornamenti regolari del sistema e patch, e la segmentazione della rete, possono fornire ulteriori livelli di protezione ma non dovrebbero essere considerati come un’alternativa alla consapevolezza dell’utente.

### Monitoraggio

Il monitoraggio delle minacce è svolto a livelli internazionali, nazionali, settoriali e organizzativi dove le informazioni sull’identificazione del malware sono condivise tramite vari meccanismi per mitigare i rischi.

### Riferimenti

International Telecommunication Union (ITU), 2008. *Studio ITU sugli aspetti finanziari della sicurezza delle reti: Malware e Spam*. Ginevra: ITU.  

Liu, S., Peng, G., Zeng, H. e Fu, J., 2024. *A survey on the evolution of fileless attacks and detection techniques*. [online] Accessed 16 January 2025.  

Milošević, N., 2014. *History of malware*. [online] Accessed 16 January 2025.  

Sikder, M.N.K., Nguyen, M.B.T., Elliott, E.D. e Batarseh, F.A., 2023. *Deep H2O: Cyber-attacks detection in water distribution systems using deep learning*. *Journal of Water Process Engineering*, 52, 103568. [online]. DOI: 10.1016/j.jwpe.2023.103568. Accessed 16 January 2025.  

Statista, no date. *Annual number of new malware variants detected worldwide from 2019 to 2023*. [online] Accessed 16 January 2025.  

Zetter, K., 2014. *An unprecedented look at Stuxnet, the world's first digital weapon*. *Wired*. [online] Accessed 16 January 2025.
```