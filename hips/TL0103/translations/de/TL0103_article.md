### Definition  
Eine fortgeschrittene Bedrohung wird von einem Gegner mit ausgefeiltem Fachwissen und erheblichen Ressourcen geschaffen, wodurch er durch die Nutzung mehrerer verschiedener Angriffspfade (z. B. Cyber, physisch und Täuschung) Möglichkeiten schafft, seine Ziele zu erreichen (NIST, 2012).

### Primary reference(s)  
National Institute for Standards and Technology, 2012. *Guide for conducting risk assessments*. DOI: 10.6028/NIST.SP.800-30r1. Zugriff 25. Januar 2025.

### Annotations  

#### Additional scientific description  
Eine **Fortgeschrittene Persistente Bedrohung (APT)** in der Cybersicherheit bezieht sich auf einen verlängerten und gezielten Cyberangriff, bei dem ein unbefugter Benutzer Zugang zu einem Netzwerk erhält und für einen längeren Zeitraum unentdeckt bleibt. Das Hauptziel von APTs ist typischerweise, Netzwerkaktivität zu beobachten, Daten zu stehlen oder Unterbrechungen zu verursachen, anstatt sofortigen Schaden zu verursachen. Diese Bedrohung gilt als „fortgeschritten“, weil ausgefeilte Techniken eingesetzt werden, um Schwachstellen auszunutzen, und als „persistierend“, weil kontinuierliche Anstrengungen unternommen werden, ein spezifisches Ziel zu erreichen.  

Einer der frühesten anerkannten APT‑Vorfälle war der **Titan‑Rain‑Angriff** zwischen 2003 und 2006, bei dem Angreifer in US‑Verteidigungsnetzwerke eindrangen, um sensible Informationen zu stehlen (Council of Foreign Relations 2005). Die Entdeckung des **Stuxnet‑Wurms** 2010 markierte eine bedeutende Eskalation und zeigte die Fähigkeit von APTs, physischen Schaden zu verursachen, indem sie die Kernspinnen (Nuklearzentrierungen) Irsans Zentrifugen angriffen (Zetter 2014). Ein weiteres bemerkenswertes Beispiel ist der **Operation Aurora‑Angriff** 2009, der mehrere Unternehmen, einschließlich Google, angriff, um geistiges Eigentum und E‑Mail‑Konten von Aktivisten zu erlangen (Council of Foreign Relations 2010). Aktuelle Vorfälle, wie **SolarWinds** (2020) und Nobeliums Kampagnen (2022), veranschaulichen die sich entwickelnden APT‑Techniken, die Lieferketten und Cloud‑Infrastruktur anvisieren (Ghanbari et al., 2024).

APTs setzen ein vielseitiges Array von Techniken ein, um ihre Ziele zu erreichen. Diese Angriffe sind auf die Merkmale ihrer Ziele ausgelegt und können daher viele Formen annehmen. Häufig beginnen sie mit einer **Intrusion** in das Ziel des Systems durch gezieltes Phishing (Spear‑Phishing), Zero‑Day‑Schwachstellen (unbekannte Sicherheitslücken) oder andere fortgeschrittene Techniken, um Systeme unentdeckt zu infiltrieren. Sobald sie drinnen sind, können Angreifer entweder still sein, den Verkehr beobachten und Informationen sammeln, oder sie können Lateral Movement nutzen, um sich im Netzwerk zu bewegen und Privilegieneskalation einsetzen, um Zugang zu sensiblen Bereichen zu erhalten. Persistenz wird durch die Bereitstellung von **Hintertüren** und Rootkits aufrechterhalten, die fortlaufenden Zugriff und **Datenausfiltration** ermöglichen, ohne Sicherheitsalarme auszulösen.

Malicious Actors, insbesondere staatliche Gruppen und organisierte Cyberkriminelle, nutzen APTs häufig, weil sie ihre langfristigen strategischen Ziele effektiv verfolgen können. Obwohl sie seltener sind als massenwirksame Angriffe wie Ransomware, stellen APTs einen bedeutenden Anteil hoch‑einflussreicher Cybervorfälle dar. Ihre Komplexität und das Potenzial für erheblichen Schaden machen sie zu bevorzugten Mitteln für Spionage, Diebstahl von geistigem Eigentum oder Sabotage.

#### Metrics and numeric limits  
Nicht anwendbar.

### Key relevant UN convention / multilateral treaty  
Internationale Rechtsinstrumente, die APTs abdecken, sind Teil des Cybersecurity‑ und Cybercrime‑Rahmens. Die **Budapest‑Konvention** des Europarates bietet eine Grundlage für internationale Zusammenarbeit im Kampf gegen Cyberdelikte, einschließlich solcher, die APTs betreffen.  

### Drivers  
Nicht anwendbar.

### Impacts  
Nicht anwendbar.

### Multi-hazard context  
Nicht anwendbar.

### Risk Management  
Der Schutz gegen eine APT ist eine komplexe Aufgabe, die die Zeit, Ressourcen und den Aufwand berücksichtigt, die der Angreifer bereit ist, in die Durchführung einzubringen. Angesichts der vielfältigen Ansätze, die APTs annehmen können, ist es schwierig, voraussehende Strategien zu formulieren, die für alle Fälle anwendbar sind. Die komplexe und sich entwickelnde Natur von APTs erfordert einen maßgeschneiderten und adaptiven Verteidigungsansatz, da keine einzelne Lösung alle potenziellen Bedrohungen abdecken kann. Stattdessen müssen Organisationen mehrere Strategien integrieren, um robuste Schutzmaßnahmen sicherzustellen.  

Nach Asharani et al. (2019) lassen sich Verteidigungsstrategien gegen Fortgeschrittene Persistente Bedrohungen (APTs) in drei Hauptgruppen einteilen: Überwachung, Erkennung und Abschwächung. Jede spielt eine kritische Rolle bei der Minimierung des Risikos unbefugten Zugriffs.  

#### Monitoring Methodologies  
Diese beinhalten die Nutzung von Firewalls und Antiviren‑Software, um verschiedene Teile des Systems zu beobachten. Fortgeschrittene Firewalls sind in der Lage, den Datenverkehr auf bekannte bösartige Muster und Signaturen zu analysieren und gleichzeitig Verhaltensanalysen einzusetzen, um abnormale Aktivitäten zu erkennen. Zusätzlich ist die Überwachung der CPU‑Auslastung wichtig, da ungewöhnliche Muster in der Ressourcennutzung auf verdächtiges Verhalten hinweisen können.  

#### Detection Methodologies  
Hierzu gehören verschiedene Anomalieerkennungsverfahren, wie statische Analyse, neuronale Netze und maschinelles Lernen (Hodge & Austin et al., 2004). Diese Techniken helfen, APTs zu identifizieren, die sich über mittlere bis lange Zeiträume ausbreiten. Ein Intrusion Detection System (IDS) kann den Netzwerkverkehr analysieren, um ungewöhnliche Aktivitäten zu erkennen und Sicherheitsteams vor potenziellen Bedrohungen zu warnen.  

#### Mitigation Methodology  
Die Abschwächung von APTs kann durch reaktive und proaktive Ansätze erreicht werden. Reaktive Methoden beinhalten die Identifizierung potenzieller Angriffspfade und Schwachstellen zu einem gegebenen Zeitpunkt, die Vorhersage kritischer Bereiche und die Bewertung ihrer Schwere. Proaktive Strategien konzentrieren sich hingegen darauf, Angreifer zu täuschen. Diese Techniken zielen darauf ab, Eindringlinge abzulenken und zu veranlassen, ihre Angriffsszenarien zu ändern, was die Auswirkungen der Bedrohung verringert.

### Monitoring  
Nicht anwendbar.

### References  

Alshamrani, A., Myneni, S., Chowdhary, A. und Huang, D., 2019. *A survey on advanced persistent threats: Techniques, solutions, challenges, and research opportunities*. In IEEE Communications Surveys & Tutorials, vol. 21, no. 2, pp. 1851‑1877, 2. Quartal 2019, doi: 10.1109/COMST.2019.2891891. Zugriff 16 Jan. 2025.  

Brandao, P.R. und Limonova, V., 2021. *Defense methodologies for advanced persistent threats (APTs)*. American Journal of Applied Sciences, 2021. DOI: 10.3844/ajassp.2021.207.212. Zugriff 16 Jan. 2025.  

Council on Foreign Relations (CFR), 2005. *Titan Rain*. Zugriff 16 Jan. 2025.  

Council on Foreign Relations (CFR), 2010. *Operation Aurora*. Zugriff 16 Jan. 2025.  

Ghanbari, H., Koskinen, K. und Wei, Y., 2024. *From SolarWinds to Kaseya: The rise of supply chain attacks in a digital world*. Journal of Information Technology Teaching Cases, 0(0). DOI: 10.1177/20438869241299823. Zugriff 16 Jan. 2025.  

Hodge, V.J. und Austin, J., 2004. *A survey of outlier detection methodologies*. Artificial Intelligence Review, 22, pp. 85‑126. Zugriff 16 Jan. 2025.  

National Institute of Standards and Technology (NIST), 2012. *Special Publication 800‑30 Revision 1: Guide for Conducting Risk Assessments*. Gaithersburg, MD: U.S. Department of Commerce. Zugriff 16 Jan. 2025.  

Zetter, K., 2014. *An unprecedented look at Stuxnet, the world’s first digital weapon*. WIRED Magazine. Zugriff 16 Jan. 2025.  

---