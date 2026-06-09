```markdown
# Dienstweigering (DoS) en Gedistribueerde Dienstweigering (DDoS)

## Definitie
Dienstweigering is het voorkomen van geautoriseerde toegang tot middelen of het vertragen van tijdkritische operaties. *Tijdkritisch* kan milliseconden of uren zijn, afhankelijk van de geleverde dienst (NIST, 2017).

## Primaire referentie(n)
NIST, 2017. Computer Security. An Introduction to Information Security. Special Publication 800-12 Revision. National Institute of Standards and Technology (NIST). Toegang 25 januari 2025.

## Annotaties
### Aanvullende wetenschappelijke beschrijving
Een **Dienstweigering (DoS)** maakt een informatiesysteem of netwerk onbeschikbaar voor de beoogde gebruikers door het te overladen met externe invoer (bijv. inkomend webverkeer). In dergelijke gevallen wordt de aanval vaak aangeduid als **Gedistribueerde Dienstweigering (DDoS)** of wanneer de aanval kwetsbaarheden exploiteert om de computationele middelen op te offeren. Deze verstoring wegniet gebruikers toegang tot diensten en informatie, met aanzienlijke operationele en financiële gevolgen (CISA, 2021).

Gedistribueerde Dienstweigering (DDoS)‑aanvallen blijven een aanhoudende overlast vormen op het Internet. Ze exploiteren het feit dat het Internet geen gecentraliseerde toegangscontrole heeft. Aangezien deze kwetsbaarheid een kernontwerpoverweging was van het vroege Internet, zijn DDoS‑aanvallen persistent gebleven. Oorspronkelijke aanvallen waren gerelateerd aan hacker‑cultuur, maar de focus verschoof snel naar commerciële exploitatie. Er zijn ook meerdere politieke toepassingen van DDoS geweest, waaronder cyberoorlog, hacktivisme en terrorisme (Brooks et al., 2021).

Het gebruik van DoS en DDoS is goed gedocumenteerd in de geschiedenis van cyberbeveiliging. Oorspronkelijke aanvallen kunnen al teruggevoerd worden op de vroege Internet‑tijd, met een van de eerste incidenten die in 1995 in Frankrijk plaatsvond, gevolgd het jaar daarna door een groot incident tegen Panix, een internetserviceprovider uit New York (Brooks et al., 2021). Gedurende de jaren hebben deze aanvallen zich ontwikkeld in complexiteit en schaal, geïllustreerd door de botnet‑aanval van 2016 die werd aangedreven door de Mirai‑malware, waarbij Internet‑van‑de‑Dingen (IoT)‑apparaten werden ingezet om een grootschalige DDoS‑aanval te lanceren die belangrijke websites wereldwijd verstoorde (CISA, 2017).

DoS kan voortkomen uit menselijke fouten (zoals verkeerde configuratie), andere incidenten (zoals stroomuitval) of opzettelijke aanvallen. Verschillende technieken worden ingezet bij DoS‑aanvallen. Het belangrijkste onderscheid ligt tussen DoS‑ en DDoS‑aanvallen. Een DoS‑aanval komt meestal van één bron die een systeem target, terwijl een DDoS‑aanval meerdere gecompromitteerde systemen omvat, vaak een botnet vormt, om het doelwit tegelijkertijd te overspoelen, waardoor verdediging aanzienlijk moeilijker wordt. De toenemende aantallen verbonden apparaten – vooral in de context van de IoT‑boom – verhogen ook het risico op DDoS‑aanvallen, aangezien elk verbonden apparaat potentieel deel kan uitmaken van een botnet.

Een Dienstweigering (DoS)‑aanval treedt op wanneer legitieme gebruikers geen toegang meer hebben tot informatiesystemen, apparaten of andere netwerkbronnen vanwege de acties van een cyberdreigingsactor. Een Dienstweigeringstoestand overspoelt het doelwit met verkeer tot het doelwit niet meer kan reageren of simpelweg crasht, met invloed op e‑mail, websites, online‑accounts (bijv. banking) of andere diensten. DoS‑aanvallen kunnen een organisatie zowel tijd als geld kosten terwijl de middelen en diensten ontoegankelijk zijn.

DoS‑aanvallen kunnen verder worden gecategoriseerd op basis van de methode: volume‑gebaseerde aanvallen overschaduwen de bandbreedte van een netwerk (bijv. een website overspoelen met overmatig verkeer), terwijl aanvallen die computationele beperkingen uitbuiten, malformed verzoeken verzenden of oneindige lussen starten om computationele middelen op te offeren. DoS‑aanvallen kunnen escaleren tot nationale risico’s wanneer ze kritieke infrastructuur targeten. Een precedent is de cyberaanval van 2007 op Estland, waarbij gecoördineerde DDoS‑aanvallen de overheid, bankwezen en mediabedrijven verpletterden, wat wijdverspreide verstoring en kwetsbaarheden op nationaal niveau blootlegde (Ottis, 2008).

DoS‑aanvallen worden veel gebruikt door malafide actoren vanwege hun relatieve eenvoudige uitvoering en potentieel voor significante verstoring. Elk jaar registreert de sector een groot aantal DoS‑ en DDoS‑incidenten, waardoor het een van de meest voorkomende vormen van cyberaanval is (Bergamini de Neira et al., 2023). In 2024 rapporteerde NETSCOUT meer dan 13 miljoen DDoS‑aanvallen wereldwijd, met stijgende trends in multi‑vectoraanvallen (NETSCOUT, 2024).

## Drijfveren
Een van de meest kritische factoren die leidt tot de toename van DDoS is de proliferatie van onbeveiligde IoT‑apparaten. De uitgebreide connectiviteit en onvoldoende beveiligingsprotocollen in moderne netwerken bieden vruchtbare bodem voor aanvallers om kwetsbaarheden te exploiteren en succesvolle DoS‑aanvallen uit te voeren.

## Gevolgen
Een Dienstweigering (DoS)‑aanval treedt op wanneer legitieme gebruikers geen toegang meer hebben tot informatiesystemen, apparaten of andere netwerkbronnen vanwege de acties van een cyberdreigingsactor. Affected services kunnen e‑mail, websites, online‑accounts (bijv. banking) of andere diensten zijn die afhankelijk zijn van het getroffen systeem of netwerk (CISA, 2021). DDoS‑aanvallen kunnen de gezondheidszorg of het financiële systeem verergeren tijdens natuurrampen of pandemieën (ENISA, 2023).

## Risicobeheer
Het minimaliseren van het risico op DoS vereist een combinatie van technologische en strategische maatregelen. Het implementeren van robuuste netwerkbeveiligingsprotocollen, het gebruik van inbraakdetectie‑ en preventiesystemen, en het adopteren van op AI gebaseerde beveiligingsoplossingen vergroten de weerbaarheid van een organisatie. Daarnaast helpen strategieën zoals verkeerslimieten, verkeerfiltering en het inzetten van contentleveringsnetwerken (CDN) om de impact van aanvallen te verminderen. Kunstmatige intelligentie kan ook een cruciale rol spelen bij het beschermen tegen DoS. AI‑systemen kunnen netwerkverkeer analyseren om anomalieën te identificeren, waardoor real‑time detectie en reactie mogelijk wordt, de capaciteit om kwaadaardig verkeer te filteren verbetert, middelen dynamisch wordt toegewezen en potentiële dreigingen op basis van patronen en gedragingen wordt voorspeld.  

Het ITU verbetert de cyberbeveiligingsbereidheid, bescherming en incidentresponscapaciteiten van lidstaten door CyberDrills op regionaal en internationaal niveau te organiseren (ITU, geen datum). Een CyberDrill is een jaarlijks evenement waarin cyberaanvallen, informatiebeveiligingsincidenten of andere verstoringen worden gesimuleerd om de cybercapaciteiten van een organisatie te testen, van het detecteren van een incident tot het adequaat reageren en het minimaliseren van gerelateerde gevolgen. Door middel van CyberDrills kunnen deelnemers beleid, plannen, procedures, processen en capaciteiten valideren die de voorbereiding, preventie, reactie, herstel en continuïteit van de operaties mogelijk maken.

## Monitoring
Niet beschikbaar

## Referenties
Bergamini de Neira, A., Kantarci, B. & Nogueira, M., 2023. Distributed denial of service attack prediction: Challenges, open issues and opportunities. *Computer Networks*, 222(C), Feb. DOI: 10.1016/j.comnet.2022.109553, Toegang 3 april 2025.  
Brooks, R.R., Yu, L., Ozcelik, I., Oakley, J. & Tusing, N., 2022. Distributed Denial of Service (DDoS): A History. *IEEE Annals of the History of Computing*, 44, pp.44–54. Toegang 3 april 2025.  
Cybersecurity and Infrastructure Security Agency (CISA), 2017. Heightened DDoS Threat Posed by Mirai and Other Botnets. Toegang 3 april 2025.  
Cybersecurity and Infrastructure Security Agency (CISA), 2021. Understanding Denial-of-Service Attacks. Toegang 3 april 2025.  
European Union Agency for Cybersecurity (ENISA), 2023. ENISA Threat Landscape 2023. Toegang 3 april 2025.  
International Telecommunication Union (ITU), geen datum. CyberDrills. Toegang 3 april 2025.  
NETSCOUT, 2024. Threat Intelligence Report 2024. Toegang 3 april 2025.  
Ottis, R., 2008. Analysis of the 2007 Cyber Attacks against Estonia from the Information Warfare Perspective. In: Proceedings of the 7th European Conference on Information Warfare and Security, Plymouth, 2008. Reading: Academic Publishing Limited, pp.163–168. Toegang 3 april 2025.  
National Institute of Standards and Technology (NIST), 2017. Computer Security: An Introduction to Information Security. Special Publication 800-12 Revision 1. Gaithersburg, MD: U.S. Department of Commerce. Toegang 3 april 2025.

_Cite this_ [Copy citation]
```