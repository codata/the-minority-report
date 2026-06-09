> ### Definition
> Een *toedieningskettingaanval* (leverancierskettingaanval) is een gebeurtenis waarbij producten, diensten of technologie die u ontvangt, zijn gecompromitteerd of aangetast, en vervolgens worden ingezet om uw eigen systemen te infiltreren en verder te compromitteren. (ICO, geen datum)
> 
> ### Primary reference(s)
> Information Commissioner’s Office (ICO), geen datum, *Supply Chain Attack*. Toegang 25 januari 2025.
> 
> ### Annotations
> #### Extra wetenschappelijke beschrijving
> In de cyber‑security verwijzen *toedieningskettingaanvallen* naar het uitbuiten van beveiligingszwaktes binnen de toedieningsketting van een organisatie om haar systemen en netwerken te infiltreren. Aanvallers richten zich op minder beveiligde onderdelen van de toedieningsketting – zoals externe leveranciers, fabrikanten of dienstverleners, waaronder cloud‑aanbieders – met als doel het einddoel te compromitteren door te profiteren van de onderlinge verbondenheid van moderne digitale ecosystemen. Deze methode maakt het mogelijk traditionele beveiligingsmaatregelen te omzeilen door vertrouwde relaties te exploiteren.
> 
> De geschiedenis van *toedieningskettingaanvallen* is geëvolueerd parallel aan de toenemende complexiteit van wereldwijde supply‑netwerken. Enkele opvallende vroege gevallen zijn de aanval op RSA Security in 2011, waarbij aanvallers *SecurID*‑tokens via een leverancier compromitteerden om defensiecontractanten te infiltreren (Greenberg, 2021). De SolarWinds‑aanval in 2020 illustreerde het ernstige effect van dergelijke inbreuken. In dit incident voegde geavanceerde bedreigingsacteurs kwaadaardige code toe aan de software‑updates van het bedrijf, wat talloze overheids- en private organisaties wereldwijd beïnvloedde en de inherente kwetsbaarheden van supply‑kettingen benadrukte (Williams, 2020).
> 
> ### Techniques
> * **Software‑updates manipuleren** (zoals in de SolarWinds‑aanval).  
> * **Code‑repositories compromitteren**.  
> * **Hardware‑componenten besmetten** tijdens productie.  
> * **Exploiteren van kwetsbaarheden in derde‑partij‑services**.  
> * **Malware in legitieme updates injecteren** of via achterdeuren in hardware‑apparaten.
> 
> Organisaties vertrouwen vaak op derde‑partij‑service‑providers voor het beheren van hun cloud‑omgevingen; dit heeft aanvallers aangemoedigd zich te richten op deze aanbieders via *identiteitsgebaseerde aanvallen*. Deze aanvallen benutten de uitgebreide permissies die vaak aan service‑provider‑accounts worden verleend, met toegang tot meerdere klantomgevingen. Deze onderling verbonden toegang verhoogt het potentiële schade‑effect, waardoor service‑providers een aantrekkelijk doelwit vormen (Microsoft, 2023).
> 
> ### Open‑source software
> Een van de meest significante *toedieningskettingaanvallen* komt voort uit open‑source software. Open‑source‑gemeenschappen bieden talrijke modules en pakketten die wereldwijd door bedrijven worden gebruikt, inclusief die in supply‑kettingen. Omdat open‑source‑software vaak geen duidelijke eigendom of gegarandeerde beveiliging heeft, introduceren ze regelmatig kwetsbaarheden in de beveiligingsarchitectuur (Forbes, 2022).
> 
> ### Code‑signing en updates
> Software‑leveranciers verspreiden updates via gecentraliseerde servers om hun producten te onderhouden en te verbeteren. Bedreigingsacteurs kunnen dit proces uitbuiten door het netwerk van de leverancier te infiltreren en malware in een update te plaatsen of te wijzigen om onbevoegde controle te verkrijgen. *Codesignering* is een cruciaal mechanisme voor het verifiëren van authenticiteit en integriteit van software; aanvallers ondermijnen dit door zelf‑gesigneerde certificaten, misconfiguraties of het compromitteren van signeringssystemen. Door vertrouwde leveranciers te imiteren en kwaadaardige code in updates te verwerken, kunnen aanvallers zeer misleidende en schadelijke aanvallen uitvoeren (NIST, 2021). In 2023 compromitteerden aanvallers de desktop‑app van 3CX via geïnfecteerde installatie‑programma’s, verspreiden malware via een veelgebruikt VoIP‑systeem (FortiGuard, 2023).
> 
> ### Risk Management
> Beschermen tegen *toedieningskettingaanvallen* vereist een alomvattende aanpak:  
> 1. **Rigoureuze leveranciers‑screening** – grondige beoordeling van leveranciers en hun beveiligingspraktijken.  
> 2. **Strenge beveiligingsnormen** – implementatie van verbindende normen voor software en hardware.  
> 3. **Continue monitoring** – real‑time observatie van verdachte activiteiten binnen de keten.  
> 4. **Samenwerking** – bevordering van kennis‑deling tussen organisaties en partners.  
> 5. **Third‑Party Risk Assessment** – testen van software vóór implementatie, eisen aan vendors om te voldoen aan specifieke beveiligingsbeleid, implementatie van een Content Security Policy (CSP) om uitvoerbare bronnen in de browser te beheren, en gebruik van Subresource Integrity (SRI) om verdachte JavaScript‑inhoud te detecteren.  
> 6. **Zero Trust** – continue verificatie en monitoring van alle gebruikers (medewerkers, contractors, vendors) binnen het netwerk.  
> 7. **DevSecOps** – integratie van beveiliging in elke fase van de ontwikkeling, waardoor real‑time beveiligingsoperaties worden ondersteund en naadloos aansluiten op bedrijfsdoelen (GitLab, geen datum).
> 
> ### Metrics and numeric limits
> Niet van toepassing.
> 
> ### Key relevant UN convention / multilateral treaty
> De internationale juridische instrumenten die *toedieningskettingaanvallen* behandelen, vallen onder bredere cyber‑security en cybercrime‑kaders. De Budapest‑conventie van de Raad van Europa biedt richtlijnen voor internationale samenwerking bij het bestrijden van cybercrime, inclusief overtredingen die *toedieningskettingaanvallen* kunnen omvatten.
> 
> ### Drivers
> Deze aanvallen, die het uitbuiten of wijzigen van software, hardware of applicaties van derden omvatten, vormen een aanzienlijke uitdaging voor organisaties.
> 
> ### Impacts
> Fraude, diefstal
> 
> ### Multi-hazard context
> Niet van toepassing
> 
> ### Monitoring
> Niet van toepassing
> 
> ### References
> * Cloudflare, geen datum. *What is supply chain attack?* Toegang 16 januari 2025.  
> * Forbes, 2022. *Mitigating the risk of supply chain attacks in the age of cloud computing*. Toegang 15 januari 2025.  
> * FortiGuard Labs, 2023. *Threat Signal Report: Supply Chain Attack Through 3CX Desktop App*. Toegang 15 januari 2025.  
> * GitLab, geen datum. *What is DevSecOps?* Toegang 16 januari 2025.  
> * Greenberg, A., 2021. *The Full Story of the Stunning RSA Hack Can Finally Be Told*. Toegang 15 januari 2025.  
> * Information Commissioner’s Office (ICO), geen datum. *Supply chain attacks*. Toegang 15 januari 2025.  
> * Microsoft, 2023. *Announcing Microsoft Defender for Cloud Capabilities to Counter Identity-Based Supply Chain Attacks*. Microsoft Tech Community. Toegang 15 januari 2025.  
> * National Institute of Standards and Technology (NIST), 2021. *Defending Against Software Supply Chain Attacks*. Toegang 16 januari 2025.  
> * Williams, J., 2020. *What You Need to Know About the SolarWinds Supply-Chain Attack*. SANS Institute.