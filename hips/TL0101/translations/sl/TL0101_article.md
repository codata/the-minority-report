```markdown
# Definition

**Malware** (zlonamerna programska oprema) je povzetni izraz za različne oblike zlonamerne programske opreme, namenjene vdoru in okužbi računalnikov, običajno brez vednosti lastnika (ITU, 2008).

## Primary reference(s)

ITU, 2008. *ITU Study on the Financial Aspects of Network Security: Malware and Spam*. International Telecommunication Union (ITU). Accessed 31 October 2024.

## Annotations

### Additional scientific description

Malware je kombinacija besed **“malicious software”**. Pomeni programsko opremo, namenjeno povzročanju škode, motenj delovanja ali pridobivanju nepooblaščenega dostopa do računalniških sistemov, omrežij ali naprav. Vključuje različne vrste zlonamerne programske opreme, vsaka s svojimi značilnostmi in načini širjenja. 

- **Virusi** – pripenjajo se k legitimnim programom in se prenašajo iz naprave na napravo, ko se ti programi izvajajo.  
- **Črpi** – kopirajo se, da bi se razširili na druge sisteme brez potrebe po gostiteljskem programu.  
- **Trojanski konji** – prekrivajo se kot brezskrbna programska oprema, da bi uporabnike prevarali in izzvali izvršitev, s čimer kompromitirajo sistem.  
- **Izhiljevalni program** – kibernetski kriminalisti šifrirajo podatke in zahtevajo plačilo v zameno za ključe za dešifriranje.  
- **Špijunska programska oprema** – skrivaj zbira informacije s spremljanjem dejavnosti uporabnikov.  
- **Wiper** – trajno izbrisi ali pokvari podatke shranjene na okuženih računalnikih.  
- **Rootkit** – omogoča nepooblaščen dostop z skrivnim skritjem svoje prisotnosti v sistemu.  

Zgodovina zlonamerne programske opreme sega vsaj do 80-ih, ko so bili ustvarjeni prvi primeri (Milošević, 2014). Značilne incidente vključujejo črpel *Morris* v 1988, ki je motil velik delež zgodnjega interneta, in bolj nedavne napade *WannaCry* v 2017, ki so prizadeli organizacije po vsem svetu.  

Malware se lahko dostavlja preko več vektorjev:  

- priloge e‑pisa (zlasti v kontekstu phishing napadov);  
- zlonamerne spletne strani;  
- prenos okuženega programa;  
- prek omrežnih ranljivosti.  

Napadalci danes izkoriščajo umetno inteligenco za ustvarjanje napredne zlonamerne programske opreme, kot so **polimorfni malware** – lahko spremenijo svojo kodo, da se izognejo odkrivanju s tradicionalnimi varnostnimi ukrepi.  

Poleg tega je **brezdatotenska zlonamerna programska oprema** vedno večja grožnja zaradi svoje sposobnosti izogibanja odkrivanju s tradicionalnimi protivirusnimi programi (Liu et al., 2024). V nasprotju s standardno zlonamerno programsko opremo, ki je odvisna od datotek ali izvedljivih programov, brezdatotenska malware izkorišča legitimne sisteme, aplikacije in storitve za izvajanje zlonamernih dejavnosti.

Brezdatotenska malware lahko vstopi v sisteme preko več vektorjev, kot so phishing e‑pisi, kompromitirane spletne strani ali napadi vodnih jam. Ko pridobi dostop, lahko ukrade občutljive informacije in razširi okužbo po omrežju, kar lahko povzroči **nacionalne in mednarodne nevarnosti**, ko so ciljani drugi sistemi namerno ali slučajno – na primer dobavitelji tretjih strani, njihov dobavitelj oziroma poddobavitelj.

**Primer:** črpel *Stuxnet* (odkrit leta 2010) je bil zasnovan za sabotažo iranskih jedrskih objektov. Ta sofisticirana zlonamerna programska oprema izpostavila potencial kibernetskih orožij, da povzročijo fizično škodo in motijo nacionalno varnost (Zetter, 2014).

Malware ostaja ena izmed najpogostejših oblik kibernetskih napadov, z milijoni novih vzorcev, odkritih letno (Statista, 2024). Služi različne namene: od finančne dobežbe preko izsiljevalnega programa do špijunaže in motenj storitev.

## Metrics and numeric limits

- Pre več kot **1 milijarda** novih variacij zlonamerne programske opreme je bilo zaznanih po vsem svetu v letu 2023 (Statista, 2024).

## Key relevant UN convention / multilateral treaty

- **Budimpeštanska konvencija o kibernetski kaznivi** (Council of Europe) zagotavlja smernice za mednarodno sodelovanje pri boju proti kibernetski kaznivi, vključno z kaznami, ki vključujejo ustvarjanje, distribucijo ali uporabo zlonamerne programske opreme.  
- **Pall Mall Process Code of Practice for States** (posodobljena 2025) predstavlja globalno vključujoči dialog za obravnavo proliferacije in neodgovorne uporabe komercialnih kibernetskih vdornih orodij in storitev.

## Drivers

- Ranljivosti programske opreme  
- Povečanje digitalne odvisnosti  
- Ekonomija kibernetske kaznivega dejanja  
- Geopolitične napetosti  

## Impacts

- Zlonamerne napade lahko eskalirajo v **nacionalne nevarnosti**, ko ciljajo kritične infrastrukture ali državne sisteme.  
- Primer: črpel *Stuxnet* (odkrit 2010) je bil zasnovan za sabotažo iranskih jedrskih objektov, kar je izpostavilo potencial kibernetskih orožij, da povzročijo fizično škodo in motijo nacionalno varnost.

## Multi‑hazard context

Zlonamerne napade lahko povzročijo:

- pomembne motnje storitev  
- finančne izgube, izgubo prihodkov  
- izgubo podatkov in oborožitev  
- izgubo ali škodo na IT infrastrukturi  
- ugrožitev ugleda organizacij in posameznikov  
- izplačila izsiljevalnih programov ter regulativne kazni  
- povečanje stroškov za obnovo  

Poročaj o uspešnem zlonamernem napadu lahko prispeva k izgubi javnega zaupanja v organizacije, politiko in javni sektor. Obstaja tudi grožnja nadaljnjega izkoriščanja, če je informacija kompromitirana.  

Programski sistemi so medsebojno povezani z fizičnimi sistemi. Zlonamerna programska oprema se lahko uporabi za omogočanje dostopa do sistemov, ki lahko odprejo druge nevarnosti – na primer povečanje kemikalij v vodnih distribucijskih sistemih za otroženje velikega dela prebivalstva z manipulacijo vodnih sistemov. To je bilo poskušano v Floridi (2021), Kaliforniji (2021), Izraelju (2020) in ZDA (2016) (Sikder et al., 2023).

## Risk Management

- Obramba proti zlonamerni programski opremi zahteva prvo ozaveščanje uporabnika; večina zlonamerne programske opreme se aktivira po uporabniškem vhodu (npr. klik na goljufivo ali kompromitirano povezavo).  
- Tehnične ukrepe, vključno z antivirusnimi in anti‑malware programi, redno posodobitvami sistema in popravki ter segmentacijo omrežja, lahko zagotovijo dodatne zaščitne sloje, vendar ne smejo nadomestiti ozaveščanja uporabnika.

## Monitoring

- Spremljanje groženj se izvaja na mednarodni, nacionalni, sektorni in organizacijski ravni, kjer se informacije o identifikaciji zlonamerne programske opreme delijo preko različnih mehanizmov za zmanjšanje tveganj.

## References

1. International Telecommunication Union (ITU), 2008. *ITU Study on the Financial Aspects of Network Security: Malware and Spam*. Geneva: ITU.  
2. Liu, S., Peng, G., Zeng, H. & Fu, J., 2024. *A survey on the evolution of fileless attacks and detection techniques*. Online. Accessed 16 January 2025.  
3. Milošević, N., 2014. *History of malware*. Online. Accessed 16 January 2025.  
4. Sikder, M.N.K., Nguyen, M.B.T., Elliott, E.D. & Batarseh, F.A., 2023. *Deep H2O: Cyber‑attacks detection in water distribution systems using deep learning*. Journal of Water Process Engineering, 52, 103568. DOI: 10.1016/j.jwpe.2023.103568. Online. Accessed 16 January 2025.  
5. Statista, no date. *Annual number of new malware variants detected worldwide from 2019 to 2023*. Online. Accessed 16 January 2025.  
6. Zetter, K., 2014. *An unprecedented look at Stuxnet, the world’s first digital weapon*. Wired. Online. Accessed 16 January 2025.  

*© 2026 – Controlled Vocabulary for Disaster Risk Reduction (sl)*
```