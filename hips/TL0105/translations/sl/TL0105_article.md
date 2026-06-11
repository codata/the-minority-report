> ### Definition  
> Napad na dobavno verigo je situacija, ko so izdelki, storitve ali tehnologija, ki jih dobite, bili kompromitirani ali prebojeni, in se nato uporabljajo za infiltracijo ter dodatno kompromitacijo vaših lastnih sistemov. (ICO, brez datuma)  
>   
> ### Primary reference(s)  
> ICO, brez datuma, Napad na dobavno verigo. Dostopno 25. januar 2025.  
>   
> ### Annotations  
> #### Additional scientific description  
> V kibernetskasti varnosti se napadi na dobavno verigo nanašajo na izkoriščanje varnostnih šibkostih znotraj dobavne verige organizacije za infiltracijo sistemov in omrežij. Napadalci ciljajo na manj varne dele dobavne verige – kot so dobavitelji tretje strani, dobavitelji ali storitveni ponudniki, kot so ponudniki oblačnih storitev – z namenom kompromitacije končnega cilja z izkoriščanjem medsebojne povezanosti sodobnih digitalnih ekosistemov. Ta metoda omogoča napadalcem, da obhodijo tradicionalne varnostne ukrepe z izkoriščanjem zaupanja v odnose.  
> Zgodovina napadov na dobavno verigo je napredovala skupaj z naraščajočo kompleksnostjo globalnih dobavnih omrežij. Značilne zgodnje primere vključujejo napad iz leta 2011 na RSA Security, kjer so napadalci kompromitirali tokenje SecurID preko dobavitelja za preboj obrambnih izvajalcev (Greenberg, 2021). Nedavno je napad iz leta 2020 na SolarWinds demonstriral resnično vpliv takih prebojev. V tem incidentu so sofisticirani napadalci vstavili zlonamerno kodo v posodobitve programske opreme podjetja, kar je prizadelo številne vlade in zasebne organizacije po vsem svetu in izpostavilo ranljivosti, vgrajene v dobavne verige (Williams, 2020).  
>  
> **Tehnične tehnike napadov na dobavno verigo** vključujejo:  
> • Spremenjanje posodobitev programske opreme (kot je bilo v napadu SolarWinds).  
> • Kompromitacijo skladišč kode.  
> • Infekcijo strojnih del med proizvodnjo.  
> • Izkoriščanje ranljivosti pri tretjih storitvah.  
> Napadalci lahko vstavijo zlonamerno kodo v zakonite posodobitve ali izkoriščajo nazadnja vrata v strojnih napravah za pridobitev nepooblaščenega dostopa.  
>  
> **Napadi na podlagi identitete** – specialna oblika napadov na dobavno verigo, ki izkorišča obsežna dovoljenja, ki so pogosto dodeljena računom storitvenih ponudnikov. Takšna dovoljenja omogočajo dostop do večih okolij strank, kar povečuje potencialni vpliv kompromitacije. (Microsoft, 2023)  
>  
> **Odprtokodna programska oprema** – ena izmed najpomembnejših virov napadov. Skupnosti odprtokodne programske opreme ponujajo številne module in pakete, ki jih uporablja globalna industrija, vendar zaradi pomanjkanja jasno določenega lastništva in zagotavljene varnosti pogosto uvajajo ranljivosti v varnostne arhitekture. (Forbes, 2022)  
>  
> **Krajstvo posodobitev in podpisovanje kode** – ključna tehnika napadov. Posodobitve programov se razširjajo s centraliziranih strežnikov. Napadalci lahko preidijo omrežje ponudnika in vstavijo zlonamerno kodo v posodobitev ali jo spremenijo za pridobitev nepooblaščene nadzorne oblasti. Signatura kode (code signing) je mehanizem za preverjanje pristnosti in integritete kode. Napadalci kršijo ta proces z uporabo samopodpisanih certifikatov, izkoriščanjem neustrezno konfiguriranih dovoljenj ali kompromitacijo sistemov za podpisovanje.  
>  
> **Vzporedni primeri** – V letu 2023 je napadalca kompromitiralo aplikacijo 3CX prek zaraženih nameščalnikov, kar je razširilo zlonamerno programsko opremo prek široko uporabljenega VoIP sistema (FortiGuard, 2023).  
>  
> **Trendi** – Zvišanje kompleksnosti dobavnih verig in odvisnosti od tretjih ponudnikov ustvarjajo številne priložnosti za izkoriščanje. Zato so napadi na dobavno verigo pomemben dejavnik v kibernetskasti varnosti, ki ga običajno izvajajo le akterji z visokimi viri in zmožnostmi.  
>   
> ### Metrics and numeric limits  
> Neuporabno.  
>   
> ### Key relevant UN convention / multilateral treaty  
> Mednarodni pravni instrumenti, ki se ukvarjajo z napadi na dobavno verigo, so zajeti v širših okvirjih kibernetske varnosti in kibernetske kriminalnosti. Konvencija o kibernetskem kriminalu v Budimpešti (Budapest Convention) Svetovne zveze ponuja smernice za mednarodno sodelovanje pri boju proti kibernetskemu kriminalu, vključno z kaznivi dejanja, ki vključujejo napade na dobavno verigo.  
>   
> ### Drivers  
> Napadi, ki izkoriščajo ali spreminjajo programsko opremo, strojno opremo ali aplikacije tretjih strani, predstavljajo pomemben izziv za organizacije.  
>   
> ### Impacts  
> Dolgovanje, kraja.  
>   
> ### Risk Management  
> Obrana pred napadi na dobavno verigo zahteva celovit pristop, ki vključuje temeljito preverjanje dobaviteljev, uvajanje strogih varnostnih standardov, neprekinjeno spremljanje in spodbujanje sodelovanja med organizacijami in njihovimi partnerji. Ker številne napadi temeljijo na zunanjih dobaviteljih z zapletenimi odvisnostmi v njihovih orodjih in storitvah, je doseganje popolne zaščite težko. Organizacije lahko sprejmejo proaktivne strategije, kot so:  
> • **Tretjičnikova ocena tveganj** – testiranje programske opreme tretjih strani pred uvajanjem, zahteva po skladnosti z varnostnimi politikami in uvajanje politike varnosti vsebine (CSP) ter integritete podrejenih virov (SRI).  
> • **Zero Trust** – zagotavlja, da so vsi uporabniki – zaposleni, izvajalci in dobavitelji – neprekinjeno preverjeni in spremljani v omrežju organizacije.  
> • **DevSecOps** – varnost dobavne verige se uporablja v DevSecOps za odkrivanje vseh komponent, vizualizacijo dobavne verige in zaščito komponent aplikacij, naprednih v oblaku.  
>   
> ### Monitoring  
> Neuporabno.  
>   
> ### References  
> - Cloudflare, brez datuma. Kaj je napad na dobavno verigo? Dostopno 16. januar 2025.  
> - Forbes, 2022. Zmanjševanje tveganja napadov na dobavno verigo v dobi oblačnega računalništva. Dostopno 15. januar 2025.  
> - FortiGuard Labs, 2023. Poročilo o signalih groženj: Napad na dobavno verigo preko aplikacije 3CX Desktop. Dostopno 15. januar 2025.  
> - GitLab, brez datuma. Kaj je DevSecOps? Dostopno 16. januar 2025.  
> - Greenberg, A., 2021. Celotna zgodba o osuplu RSA napadu, ki jo lahko končno razkrije. Dostopno 15. januar 2025.  
> - Information Commissioner’s Office (ICO), brez datuma. Napadi na dobavno verigo. Dostopno 15. januar 2025.  
> - Microsoft, 2023. Objave Microsoft Defender za oblačne zmogljivosti za boj proti napadom na dobavno verigo, ki temeljijo na identiteti. Microsoft Tech Community. Dostopno 15. januar 2025.  
> - National Institute of Standards and Technology (NIST), 2021. Obramba pred napadi na dobavno verigo programske opreme. Dostopno 16. januar 2025.  
> - Williams, J., 2020. Kaj morate vedeti o napadu na dobavno verigo SolarWinds. SANS Institute.  

---