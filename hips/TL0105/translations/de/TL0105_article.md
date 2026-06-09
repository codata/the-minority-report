### Definition  
Ein Lieferkettenangriff liegt vor, wenn Produkte, Dienstleistungen oder Technologie, die Sie beziehen, kompromittiert wurden und anschließend zur Infiltration und weiteren Kompromittierung Ihrer eigenen Systeme eingesetzt werden (ICO, kein Datum).

### Primäre Referenz(en)  
Information Commissioner’s Office (ICO), kein Datum, *Supply chain attacks*. Zugegriffen 25. Januar 2025.

### Annotationen  
#### Weitere wissenschaftliche Beschreibung  
In der Cybersicherheit beziehen sich Lieferkettenangriffe auf die Ausnutzung von Sicherheitslücken innerhalb der Lieferkette einer Organisation, um deren Systeme und Netzwerke zu infiltrieren. Angreifer zielen auf weniger sichere Elemente der Lieferkette – wie Drittanbieter, Lieferanten oder Dienstleister, etwa Cloud‑Anbieter – mit dem Ziel, das Endziel durch die vernetzten modernen digitalen Ökosysteme zu kompromittieren. Diese Methode ermöglicht es Angreifern, traditionelle Sicherheitsmaßnahmen zu umgehen, indem sie vertrauenswürdige Beziehungen ausnutzen. Die Geschichte von Lieferkettenangriffen hat sich parallel zur zunehmenden Komplexität globaler Lieferketten entwickelt. Bemerkenswerte frühere Fälle umfassen den 2011‑Angriff auf RSA Security, bei dem Angreifer SecurID‑Token über einen Lieferanten kompromittierten, um Verteidigungsunternehmen zu infiltrieren (Greenberg, 2021). Kürzlich demonstrierte der SolarWinds‑Angriff 2020 die schwerwiegenden Auswirkungen solcher Sicherheitsverletzungen. In diesem Vorfall haben sich hochentwickelte Bedrohungsakteure in die Software‑Updates des Unternehmens eingeschleust, was zahlreiche Regierungs‑ und Privatorganisationen weltweit betraf und die Schwachstellen in Lieferketten hervorhob (Williams, 2020).

Verschiedene Techniken werden bei Lieferkettenangriffen eingesetzt. Diese umfassen das Manipulieren von Software‑Updates (wie im SolarWinds‑Angriff), das Kompromittieren von Code‑Repositorys, das Infizieren von Hardware‑Komponenten während der Fertigung und die Ausnutzung von Schwachstellen in Drittanbieter‑Dienstleistungen. Angreifer können Malware in legitime Software‑Updates einschleusen oder Hintertüren in Hardware‑Geräten nutzen, um unberechtigten Zugriff zu erlangen.

Viele Organisationen verlassen sich auf Drittanbieter, um ihre Cloud‑Umgebungen zu verwalten, was Angreifer dazu veranlasst hat, sich auf diese Anbieter in einer einzigartigen Form von Lieferkettenangriffen – identitätsbasierten Angriffen – zu konzentrieren. Diese Angriffe nutzen die umfangreichen Berechtigungen aus, die häufig Dienstleisterkonten gewährt werden und Zugriff auf mehrere Kundenumgebungen haben. Dieser vernetzte Zugriff erhöht das Potenzial eines Kompromisses und macht Dienstleister zu einem attraktiven Ziel (Microsoft, 2023).

Ein bedeutender Lieferkettenangriff stammt aus der Open‑Source‑Software. Open‑Source‑Communities bieten zahlreiche Module und Pakete, die weltweit von Unternehmen genutzt werden, einschließlich solcher in Lieferketten. Allerdings führt die fehlende klare Eigentümerschaft und garantierte Sicherheit oft dazu, dass Schwachstellen in Sicherheitsarchitekturen eingeführt werden (Forbes, 2022).

Eine weitere prominente Technik in Lieferkettenangriffen ist das Hijacking von Updates und das Kompromittieren von Code‑Signaturen. Software‑Hersteller verteilen routinemäßig Updates von zentralen Servern, um ihre Produkte zu warten und zu verbessern. Bedrohungsakteure können diesen Prozess ausnutzen, indem sie das Netzwerk des Anbieters infiltrieren, um Malware in ein Update einzuschleusen oder es zu manipulieren, um unberechtigte Kontrolle über die Software‑Funktionalität zu erlangen. Die Code‑Signatur, ein Mechanismus zur Überprüfung von Authentizität und Integrität von Software, ist ein weiteres wichtiges Ziel. Schadakteure untergraben diesen Prozess, indem sie selbstsignierte Zertifikate verwenden, fehlerhafte Zugangskontrollen ausnutzen oder Signiersysteme kompromittieren. Durch die Imitation vertrauenswürdiger Anbieter und das Einbetten von Malware in Updates können Angreifer hochgradig täuschende und schädliche Angriffe erfolgreich ausführen (NIST, 2021).

Im Jahr 2023 kompromittierten Angreifer die 3CX‑Desktop‑App durch infizierte Installer, verbreiteten Malware über ein weit verbreitetes VoIP‑System (Fortiguard, 2023).

Schadakteure setzen zunehmend auf Lieferkettenangriffe wegen ihres hohen Einflusses und der Schwierigkeit, sie zu erkennen. Die Komplexität moderner Lieferketten und die Abhängigkeit von Drittanbietern schaffen zahlreiche Möglichkeiten für Ausnutzung, was Lieferkettenangriffe zu einer erheblichen Bedrohung in der Cybersicherheit macht. Gleichzeitig sind Lieferkettenangriffe oft gezielt. Daher können nur Akteure mit höheren Ressourcen und Fähigkeiten (in der Regel) diese durchführen.

### Messwerte und numerische Grenzen  
Nicht anwendbar.

### Wichtige UN‑Konvention / multilateraler Vertrag  
Internationale Rechtsinstrumente zur Bekämpfung von Lieferkettenangriffen sind Teil breiterer Cyber‑ und Cyber‑Kriminalitätsrahmen. Die Budapest‑Konvention der Europarats über Cyber‑Kriminalität bietet Richtlinien für internationale Kooperationen im Kampf gegen Cyber‑Kriminalität, einschließlich Vergehen, die Lieferkettenangriffe einschließen könnten.

### Treiber  
Diese Angriffe, die die Ausnutzung oder Änderung von Drittanbieter‑Software, Hardware oder Anwendungen beinhalten, stellen eine erhebliche Herausforderung für Organisationen dar.

### Auswirkungen  
Betrug, Diebstahl

### Multi‑Hazard‑Kontext  
Nicht anwendbar

### Risikomanagement  
Die Verteidigung gegen Lieferkettenangriffe erfordert einen umfassenden Ansatz, der die gründliche Prüfung von Lieferanten, die Implementierung strenger Sicherheitsstandards, kontinuierliches Monitoring und die Förderung der Zusammenarbeit zwischen Organisationen und ihren Partnern einschließt. Da viele Angriffe auf externe Anbieter mit komplexen Abhängigkeiten in ihren Tools und Dienstleistungen angewiesen sind, ist die Erreichung vollständiger Schutz schwierig. Organisationen können jedoch proaktive Strategien verfolgen, um gängige Angriffsvektoren zu verhindern (Cloudflare, kein Datum).  
**Durchführung einer Drittanbieter‑Risikobewertung:**  
- Prüfung von Drittanbieter‑Software vor der Bereitstellung  
- Verpflichtung der Anbieter, spezifische Sicherheitsrichtlinien einzuhalten  
- Implementierung einer Content Security Policy (CSP) zur Steuerung ausführbarer Ressourcen im Browser  
- Nutzung von Subresource Integrity (SRI), um verdächtige JavaScript‑Inhalte zu erkennen  

**Implementierung von Zero Trust:**  
Zero Trust stellt sicher, dass alle Benutzer – Mitarbeiter, Auftragnehmer und Anbieter – kontinuierlich verifiziert und innerhalb des Netzwerks überwacht werden. Durch die Verifizierung von Identität und Berechtigungen von Benutzern und Geräten verhindert Zero Trust Angreifer, die gestohlene legitime Benutzerdaten ausnutzen, um das Unternehmen zu infiltrieren.

**DevSecOps:**  
Lieferketten‑Sicherheit nutzt DevSecOps, um Angriffe zu verhindern, indem zunächst alle Komponenten entdeckt, Transparenz in die Lieferkette gewonnen und cloud‑native Anwendungen gesichert werden. Durch die Integration von Sicherheit in den gesamten Entwicklungsprozess gewährleistet DevSecOps eine Echtzeit‑Bereitstellung von Sicherheitsoperationen, während sie nahtlos mit Unternehmenszielen übereinstimmt (GitLab, kein Datum).

### Monitoring  
Nicht anwendbar

### Referenzen  
- Cloudflare, kein Datum. *What is supply chain attack?* Zugriff 16. Januar 2025.  
- Forbes, 2022. *Mitigating the risk of supply chain attacks in the age of cloud computing.* Zugriff 15 Jan. 2025.  
- FortiGuard Labs, 2023. *Threat Signal Report: Supply Chain Attack Through 3CX Desktop App.* Zugriff 15. Januar 2025.  
- GitLab, kein Datum. *What is DevSecOps?* Zugriff 16. Jan. 2025.  
- Greenberg, A., 2021. *The Full Story of the Stunning RSA Hack Can Finally Be Told.* Zugriff 15. Januar 2025.  
- Information Commissioner’s Office (ICO), kein Datum. *Supply chain attacks.* Zugriff 15. Januar 2025.  
- Microsoft, 2023. *Announcing Microsoft Defender for Cloud Capabilities to Counter Identity‑Based Supply Chain Attacks.* Microsoft Tech Community. Zugriff 15. Januar 2025.  
- National Institute of Standards and Technology (NIST), 2021. *Defending Against Software Supply Chain Attacks.* Zugriff 16 Jan. 2025.  
- Williams, J., 2020. *What You Need to Know About the SolarWinds Supply‑Chain Attack.* SANS Institute.  

---