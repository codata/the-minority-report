```markdown
### Definition

Piegādes nomākšana (DoS) ir autorizētas piekļuves resursiem atteikšana vai laika kritisku operāciju aizkavēšana. Laika kritiskums var būt milisekundes vai stundas, atkarībā no nodrošināto pakalpojuma (NIST, 2017).

### Primary reference(s)

NIST, 2017. *Computer Security. An Introduction to Information Security.* Special Publication 800‑12 Revision. National Institute of Standards and Technology (NIST). 25. janvāris 2025.

### Annotations

#### Additional scientific description

Piegādes nomākšana (DoS) padara datoru sistēmu vai tīklu nepieejamu paredzētajiem lietotājiem, pārslodžot to ar ārējiem ievadiem (piemēram, ienākošo tīmekļa trafiku). Šādā gadījumā tā tiek saukta par izplatītu Piegādes nomākšanu (DDoS) vai izmanto tās ievainojamības, lai iztukšotu aprēķināšanas resursus. Šī traucēšana nomāk lietotājiem piekļuvi pakalpojumiem un informācijai, radot būtiskas operatīvas un finanšu sekas (CISA, 2021).

Izplatīta Piegādes nomākšana (DDoS) uzbrukumi joprojām ir pastāvīga traucējuma avota Interneta tīklā. Tie izmantos faktu, ka Internets trūkst centralizēta piekļuves kontroles. Tā kā šī ievainojamība bija pamata dizaina lēmums agrīnajā Interneta stadijā, DDoS uzbrukumi ir saglabājušies. Agrīnās uzbrukumu izveidotāji bija saistīti ar hakeru kultūru, bet viņu fokuss ātri pārcēla uz komerciālu iznedzināšanu. Turklāt ir bijuši vairāki politiskie DDoS uzbrukumu piemēri, tostarp kiberkaras, hacktivismu un terorismu (Brooks et al., 2021).

DoS un DDoS lietošanas dokumentācija ir plaši zināma kiberbezpečnosti vēsturē. Agrīni uzbrukumi ir atklāti jau agrīnajā Interneta ērijā, ar vienu no pirmajiem incidentiem, kas notika Francijā 1995. gadā, un nākamajā gadā notika liels incidentis pret Panix, Jaungalas ielas, Ārthijas interneta pakalpojumu sniedzēju (Brooks et al., 2021). Gadu gaitā šie uzbrukumi ir attīstījušies gan sarežģītībā, gan mērogā, piemēram, 2016. gada botnet uzbrukums, kas balstījās uz Mirai ļaunprogrammu, kas izmantoja Interneta lietu (IoT) ierīces, lai uzsāktu milzīgu DDoS uzbrukumu, traucējot svarīgus interneta portālus visā pasaulē (CISA, 2017).

DoS var rasties no cilvēka kļūdām (piemēram, nepareizās konfigurācijās), citiem incidentiem (piemēram, enerģijas izslēgšanas) vai apzinātiem uzbrukumiem. Dažādas tehnikas tiek izmantotas DoS uzbrukumos. Galvenais atšķirības punkt ir starp DoS un DDoS uzbrukumiem. DoS uzbrukums parasti rodas no vienas avota, kas mērķē uz sistēmu, savukārt DDoS uzbrukums ietver vairākus kompromitētus sistēmas, kas bieži veido botnet, lai vienlaikus plūstošā mērķa uzbrukumu, padarot aizsardzību ievērojami grūtāku. Palielinoties savienoto ierīču skaitam — īpaši IoT boom kontekstā — palielinās arī DDoS uzbrukumu risks, jo katra savienotā ierīce var kļūt par botnet daļu.

Piegādes nomākšanas (DoS) uzbrukums notiek, kad legitimie lietotāji neizkļūst pie informācijas sistēmas, ierīcēm vai citām tīkla resursiem, pateicoties ļaunprātīgā kiberuzbrukuma aktieris darbībām. Piegādes nomākšanas stāvoklis plūstošā pārmērīgu trafiku uz mērķa hosta vai tīklu, līdz tas nevar reaģēt vai vienkārši avārijo, ietekmējot e-pastu, tīmekļa vietnes, tiešsaistes kontus (piemēram, banku) vai citus pakalpojumus. DoS uzbrukumi var radīt organizācijai gan laika, gan naudas zudumus, kamēr tās resursi un pakalpojumi ir nepieejami.

DoS uzbrukumi var tikt papildus klasificēti pēc metodes: volumēri, kas pārmērīgi slauj tīkla platdarbības (piemēram, tīmekļa vietnes pārpludināšana ar pārmērīgu trafiku), un uzbrukumi, kas izmanto aprēķināšanas ierobežojumus, sūtot sliktus pieprasījumus vai uzsākot bezgalīgas ciklu, lai iztukšotu aprēķināšanas resursus. DoS uzbrukumi var paaugstināties uz nacionāliem riskiem, ja tie mērķē uz kritisko infrastruktūru. Piemēram, 2007. gada kiberuzbrukumi uz Estonu, kur koordinēti DDoS uzbrukumi ir slēdzis valdības, banku un mediju tīmekļa vietnes, radot plašu traucējumus un uzsvērot nacionālu līmeņa ievainojamības (Ottis, 2008).

DoS uzbrukumi bieži tiek izmantoti ļaunprātīgiem aktieriem, pateicoties tiem vienkāršajam izpildes procesa un potenciālajam nozīmīgam traucējumam. Katru gadu dati parāda lielu Dažādu DoS un DDoS incidentu skaitu, padarot tos par vienu no visbiežākajiem kiberuzbrukuma veidiem (Bergamini de Neira et al., 2023). 2024. gadā NETSCOUT ziņoja par pārsvarām 13 miljoniem DDoS uzbrukumu visā pasaulē, ar pieaugošu tendenci uz daudzveidīgām uzbrukuma formām (NETSCOUT, 2024).

### Drivers

Viens no viskritiskākajiem faktoriem, kas palielina DDoS, ir nepiesardzīgu IoT ierīču paplašināšanās. Plašā savienojamība un nepietiekamas drošības protokoli mūsdienu tīklos rada labvēlīgus apstākļus uzbrukumu veikšanai un DDoS uzbrukuma veidošanai.

### Impacts

Piegādes nomākšanas (DoS) uzbrukums notiek, kad legitimie lietotāji neizkļūst pie informācijas sistēmas, ierīcēm vai citām tīkla resursiem, pateicoties ļaunprātīgā kiberuzbrukuma aktieris darbībām. Ietekmētie pakalpojumi var ietvert e-pastu, tīmekļa vietnes, tiešsaistes kontus (piemēram, banku) vai citus pakalpojumus, kas balstās uz ietekmēto datoru vai tīklu. (CISA, 2021). DDoS uzbrukumi var pastiprināt veselības aprūpes vai finanšu sistēmas kļūdas dabu dabas katastrofās vai pandēmijās (ENISA, 2023).

### Risk Management

DoS risku mazināšana ietver tehnoloģisko un stratēģisko pasākumu kombināciju. Ieviešot robustus tīkla drošības protokolus, izmantojot iiešanas atklāšanas un novēršanas sistēmas, kā arī adoptējot AI balstītus drošības risinājumus, tiek uzlabota organizācijas izturība. Turklāt stratēģijas, piemēram, tempo ierobežošana, trafika filtrēšana un saturs piegādes tīkla izmantošana, palīdz mazināt uzbrukumu ietekmi. Mākslīgā intelekta rīki spēlē kritisku lomu, lai aizsargātu pret DoS. AI sistēmas var analizēt tīkla trafiku, identificēt anomālijas, nodrošināt reāllaika noteikšanu un reakciju, uzlabot spēju filtrēt ļaunprātīgu trafiku, dinamiskā resursu sadale un potenciālo draudu prognozēšanu, balstoties uz modeļiem un uzvedību.

ITU uzlabo kiberbezpečnosti gatavību, aizsardzību un incidentu reakciju iespējas Īpašu valstu kopienai, veicot CyberDrills reģionālā un starptautiskā līmenī (ITU, n. datums). CyberDrills ir gada pasākums, kurā tiek simulēti kiberuzbrukumi, informācijas drošības incidenti vai citi traucējumu veidi, lai pārbaudītu organizācijas kiberspējības – no incidentu noteikšanas līdz atbilstošai reakcijai un ietekmes mazināšanai. CyberDrills ļauj dalībniekiem pārbaudīt politiku, plānus, procedūras, procesus un spējību, kas nodrošina sagatavošanos, novēršanu, reakciju, atgūšanu un darbības turpmākajai izturēšanos.

### Monitoring

Nav pieejams.

### References

Bergamini de Neira, A., Kantarci, B. and Nogueira, M., 2023. *Distributed denial of service attack prediction: Challenges, open issues and opportunities.* Computer Networks, 222(C), Feb. DOI: 10.1016/j.comnet.2022.109553. 3. aprīlī 2025.

Brooks, R.R., Yu, L., Ozcelik, I., Oakley, J. and Tusing, N., 2022. *Distributed Denial of Service (DDoS): A History.* IEEE Annals of the History of Computing, 44, pp.44–54. 3. aprīlī 2025.

Cybersecurity and Infrastructure Security Agency (CISA), 2017. *Heightened DDoS Threat Posed by Mirai and Other Botnets.* 3. aprīlī 2025.

Cybersecurity and Infrastructure Security Agency (CISA), 2021. *Understanding Denial-of-Service Attacks.* 3. aprīlī 2025.

European Union Agency for Cybersecurity (ENISA), 2023. *ENISA Threat Landscape 2023.* 3. aprīlī 2025.

International Telecommunication Union (ITU), no date. *CyberDrills.* 3. aprīlī 2025.

NETSCOUT, 2024. *Threat Intelligence Report 2024.* 3. aprīlī 2025.

Ottis, R., 2008. *Analysis of the 2007 Cyber Attacks against Estonia from the Information Warfare Perspective.* In: Proceedings of the 7th European Conference on Information Warfare and Security, Plymouth, 2008. Reading: Academic Publishing Limited, pp.163–168. 3. aprīlī 2025.

National Institute of Standards and Technology (NIST), 2017. *Computer Security: An Introduction to Information Security.* Special Publication 800‑12 Revision 1. Gaithersburg, MD: U.S. Department of Commerce. 3. aprīlī 2025.

```

---