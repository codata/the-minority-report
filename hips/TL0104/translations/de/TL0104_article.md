### Definition  
Dienstverweigerung (DoS) ist die Verhinderung autorisierten Zugangs zu Ressourcen oder die Verzögerung zeitkritischer Operationen. Zeitkritisch kann von Millisekunden bis zu Stunden reichen, je nach dem angebotenen Dienst. (NIST, 2017)

### Primäre Referenz(e)  
NIST, 2017. Computersicherheit: Eine Einführung in die Informationssicherheit. Sonderpublikation 800‑12 Revision. Nationales Institut für Standards und Technologie (NIST). Abgerufen am 25. Januar 2025.

### Anmerkungen  

#### Zusätzliche wissenschaftliche Beschreibung  
Eine Dienstverweigerung (DoS) macht ein Computersystem oder Netzwerk für seine vorgesehenen Benutzer unzugänglich, indem es mit externen Eingaben (z. B. eingehendem Webverkehr) überlastet wird. In solchen Fällen trägt sie den Namen Verteilte Dienstverweigerung (DDoS), wenn mehrere kompromittierte Systeme gleichzeitig den Zielserver überfluten, oder nutzt Schwachstellen aus, um die rechnerischen Ressourcen zu erschöpfen. Diese Unterbrechung verweigert Benutzern den Zugang zu Diensten und Informationen und verursacht erhebliche betriebliche sowie finanzielle Auswirkungen (CISA, 2021).

Verteilte Dienstverweigerung (DDoS) Angriffe bleiben eine persistente Belästigung im Internet. Sie nutzen die Tatsache, dass das Internet keine zentrale Zugangskontrolle besitzt. Da diese Schwachstelle eine Kernentscheidung im frühen Internet war, haben DDoS-Angriffe Bestand. Frühe Angriffe waren mit der Hacker‑Kultur verbunden, jedoch wandelte sich ihr Fokus schnell zu kommerzieller Ausnutzung. Es gab zudem mehrere politische Anwendungen von DDoS, darunter Cyberkrieg, Hacktivismus und Terrorismus (Brooks et al., 2021).

Die Verwendung von DoS und DDoS ist gut dokumentiert in der Cyber‑Security‑Geschichte. Frühe Angriffe lassen sich bereits in der frühen Internet‑Ära nachweisen; eines der ersten Vorfälle ereignete sich 1995 in Frankreich, gefolgt im darauffolgenden Jahr von einem bedeutenden Vorfall gegen Panix, einen Internet‑Dienstanbieter mit Sitz in New York (Brooks et al., 2021). Im Laufe der Jahre haben sich diese Angriffe in Komplexität und Umfang weiterentwickelt, wie das 2016‑Botnet‑Angriff mit dem Mirai‑Malware illustriert, das IoT‑Geräte ausnutzte, um einen massiven DDoS‑Angriff zu starten, der weltweit große Webseiten beeinträchtigte (CISA, 2017).

DoS kann durch menschliche Fehler (z. B. Fehlkonfiguration), andere Zwischenfälle (z. B. Stromausfall) oder gezielte Angriffe entstehen. Verschiedene Techniken werden bei DoS-Angriffen eingesetzt. Die Hauptunterscheidung liegt zwischen DoS- und DDoS-Angriffen: Ein DoS-Angriff stammt in der Regel von einer einzigen Quelle, die ein System angreift, während ein DDoS-Angriff mehrere kompromittierte Systeme nutzt, die oft ein Botnetz bilden, um das Ziel gleichzeitig zu überfluten, was die Verteidigung erheblich erschwert. Die zunehmende Anzahl vernetzter Geräte – insbesondere im Kontext des IoT‑Booms – erhöht ebenfalls das Risiko, dass DDoS-Angriffe auftreten, da jedes vernetzte Gerät potenziell Teil eines Botnetzes werden kann.

Eine Dienstverweigerungsbedingung überflutet den betroffenen Host oder das Netzwerk mit Verkehr, bis das Ziel nicht mehr reagieren kann oder einfach abstürzt, was E‑Mail, Webseiten, Online‑Konten (z. B. Bankkonten) oder andere Dienste betrifft. DoS-Angriffe können einer Organisation sowohl Zeit als auch Geld kosten, während ihre Ressourcen und Dienste nicht zugänglich sind.

DoS-Angriffe lassen sich weiter nach Methode klassifizieren: Volumenbasierte Angriffe überlasten die Bandbreite eines Netzwerks (z. B. durch Überflutung einer Webseite mit übermäßigem Verkehr), während Angriffe, die rechnerische Beschränkungen ausnutzen, manipulierte Anfragen senden oder unendliche Schleifen initiieren, um die rechnerischen Ressourcen zu erschöpfen. DoS-Angriffe können zu nationalen Gefahren eskalieren, wenn sie kritische Infrastruktur anvisieren. Ein Präzedenzfall ist der Cyber‑Angriff 2007 auf Estland, bei dem koordinierte DDoS-Angriffe Regierungs-, Banken‑ und Medien‑Webseiten lahmlegten, was zu weitreichenden Störungen führte und die nationalen Schwachstellen hervorhob (Ottis, 2008).

DoS-Angriffe werden häufig von böswilligen Akteuren eingesetzt, da sie relativ einfach auszuführen sind und erheblichen Schaden verursachen können. Jedes Jahr registrieren Datenbanken große Zahlen an DoS- und DDoS-Vorfällen, was sie zu einer der verbreitetsten Formen von Cyberangriffen macht (Bergamini de Neira et al., 2023). Im Jahr 2024 meldete NETSCOUT über 13 Millionen DDoS-Angriffe weltweit, mit steigenden Trends bei Mehrfache Angriffsvektoren (NETSCOUT, 2024).

### Treiber  
Einer der wichtigsten Faktoren, der die Zunahme von DDoS antreibt, ist die Verbreitung unsicherer IoT‑Geräte. Die umfangreiche Konnektivität und unzureichenden Sicherheitsprotokolle in modernen Netzwerken bieten fruchtbaren Boden für Angreifer, Schwachstellen auszunutzen und erfolgreiche DoS-Angriffe zu starten.

### Auswirkungen  
Eine Dienstverweigerungsbedingung (DoS) tritt ein, wenn legitime Benutzer keinen Zugriff auf Informationssysteme, Geräte oder andere Netzwerkressourcen haben, weil ein böswilliger Cyber‑Bedrohungsakteur handelt. Betroffene Dienste können E‑Mail, Webseiten, Online‑Konten (z. B. Bankkonten) oder andere Dienste sein, die von dem betroffenen Computer oder Netzwerk abhängen (CISA, 2021). DDoS-Angriffe können die Funktionsfähigkeit von Gesundheits‑ oder Finanzsystemen während Naturkatastrophen oder Pandemien verschärfen (ENISA, 2023).

### Mehrfache Gefahrenkontexte  
Nicht verfügbar.

### Risikomanagement  
Die Minimierung des Risikos von DoS erfordert eine Kombination aus technologischen und strategischen Maßnahmen. Die Implementierung robuster Netzwerksicherheitsprotokolle, die Nutzung von Intrusion Detection und Prevention Systemen (IDPS) sowie der Einsatz von KI‑gestützten Sicherheitslösungen erhöhen die Resilienz einer Organisation. Zusätzlich tragen Maßnahmen wie Ratenbegrenzung, Verkehrsfilterung und der Einsatz von Content‑Delivery‑Netzwerken (CDN) zur Abschwächung der Auswirkungen von Angriffen bei. Künstliche Intelligenz kann ebenfalls eine entscheidende Rolle beim Schutz vor DoS spielen. KI‑Systeme analysieren Netzverkehr, um Anomalien zu erkennen, ermöglichen so Echtzeit‑Erkennung und -Reaktion, verbessern die Fähigkeit zur Filterung von schädlichem Verkehr, weisen Ressourcen dynamisch zu und prognostizieren potenzielle Bedrohungen basierend auf Mustern und Verhaltensweisen. Die ITU verbessert die Cyber‑Security‑Bereitschaft, den Schutz und die Reaktionsfähigkeit von Mitgliedsstaaten, indem sie Cyber‑Übungen (CyberDrills) auf regionaler und internationaler Ebene durchführt (ITU, kein Datum). Eine Cyber‑Übung ist ein jährliches Ereignis, bei dem Cyber‑Angriffe, Sicherheitsvorfälle oder andere Störungen simuliert werden, um die Cyber‑Fähigkeiten einer Organisation zu testen – von der Erkennung eines Sicherheitsvorfalls bis zur angemessenen Reaktion und Minimierung jeglicher damit verbundenen Auswirkungen. Durch Cyber‑Übungen können Teilnehmer ihre Richtlinien, Pläne, Verfahren, Prozesse und Fähigkeiten validieren, die die Vorbereitung, Prävention, Reaktion, Wiederherstellung und Kontinuität des Betriebs ermöglichen.

### Monitoring  
Nicht verfügbar.

### Referenzen  
- Bergamini de Neira, A., Kantarci, B. und Nogueira, M., 2023. Distributed denial of service attack prediction: Challenges, open issues and opportunities. *Computer Networks*, 222(C), Feb. DOI: 10.1016/j.comnet.2022.109553. Abgerufen am 3. April 2025.  
- Brooks, R.R., Yu, L., Ozcelik, I., Oakley, J. und Tusing, N., 2022. Distributed Denial of Service (DDoS): A History. *IEEE Annals of the History of Computing*, 44, pp.44–54. Abgerufen am 3. April 2025.  
- Cybersecurity and Infrastructure Security Agency (CISA), 2017. Heightened DDoS Threat Posed by Mirai and Other Botnets. Abgerufen am 3. April 2025.  
- Cybersecurity and Infrastructure Security Agency (CISA), 2021. Understanding Denial-of-Service Attacks. Abgerufen am 3. April 2025.  
- European Union Agency for Cybersecurity (ENISA), 2023. ENISA Threat Landscape 2023. Abgerufen am 3. April 2025.  
- International Telecommunication Union (ITU), kein Datum. CyberDrills. Abgerufen am 3. April 2025.  
- NETSCOUT, 2024. Threat Intelligence Report 2024. Abgerufen am 3. April 2025.  
- Ottis, R., 2008. Analysis of the 2007 Cyber Attacks against Estonia from the Information Warfare Perspective. In: Proceedings of the 7th European Conference on Information Warfare and Security, Plymouth, 2008. Reading: Academic Publishing Limited, pp.163–168. Abgerufen am 3. April 2025.  
- National Institute of Standards and Technology (NIST), 2017. Computer Security: An Introduction to Information Security. Sonderpublikation 800‑12 Revision 1. Gaithersburg, MD: U.S. Department of Commerce. Abgerufen am 3. April 2025.  

---