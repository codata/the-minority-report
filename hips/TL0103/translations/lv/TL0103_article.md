```markdown
### Definīcija

Uzlabota draudze tiek radīta, ja pretinieks ar izsmalcinātu ekspertīzi un būtiskajiem resursiem izmanto vairākus uzbrukuma vektorus (piemēram, cyber, fiziskā un klēpšana), lai radītu iespējas sasniegt savus mērķus (NIST, 2012).

### Primārās atsauces

Nacionālais standartu un tehnoloģiju institūts (NIST), 2012. “Risku novērtēšanas vadlīnijas.” DOI:10.6028/NIST.SP.800-30r1. Pieejams 25. janvāris 2025.

### Papildu zinātniskā apraksts

Izsmalcināta pastāvīgā draudze (APT) kriptotehnikā attiecas uz ilgu un mērķtiecīgu kiberuzbrukumu, kurā, bieži, neautorizēts lietotājs piekļūst tīklam un paliek neatpazīstams ilgu laiku. APT galvenais mērķis parasti ir novērot tīkla aktivitāti, vēstīt datus vai izraisīt traucējumus, nevis izraisīt tūlītēju bojājumu. Šī draudze tiek uzskatīta par izsmalcinātu, pateicoties izmantotajām izsmalcinātām tehnoloģijām, un pastāvīgu, jo tiek pastāvīgi centieni sasniegt konkrētu mērķi.

Vienā no visaušākajām atzītošajām APT incidentiem bija Titan Rain uzbrukumi 2003.–2006. gadā, kad uzbrukēji iepludināja ASV aizsardzības tīklus, lai iegūtu sensitīvas informācijas (Council of Foreign Relations, 2005). Stuxnet vīrusa atklāšana 2010. gadā atklāja APT spējību izraisīt fizisko bojājumu, mērķējot uz Īranas atomas centrifugēm (Zetter, 2014). Cits ievērojams piemērs ir Operation Aurora uzbrukums 2009. gadā, kas mērķēja vairākas uzņēmumus, tostarp Google, lai piekļūtu intelektuālās īpašuma un aktivistu e-pasta kontiem (Council of Foreign Relations, 2010). Jaunākie incidents, piemēram, SolarWinds (2020) un Nobelium kampaņas (2022), parāda attīstījošas APT tehnoloģijas, mērķējot uz piegādes ķēdēm un mākonīšanas infrastruktūru (Ghanbari et al., 2024).

APT izmanto daudzveidīgu tehnoloģiju komplektu, lai sasniegtu savus mērķus. Šie uzbrukumi tiek veidoti atbilstoši mērķa raksturlielumiem un, tādējādi, var pieņemt daudzus veidus. Parasti tie sākas ar intrūzijām uz mērķa sistēmas, izmantojot spear‑phishing, nullas dienas uzbrukumus (nezināmas drošības kļūdas) vai citas izsmalcinātas tehnoloģijas, lai iepludinātu sistēmas bez atpazīšanas. Pēc ienākšanas uzbrukēji var palikt klusīgi, uzraugot trafiku un savācot informāciju, vai izmantot laterālo pārvietošanu, lai pārvietotos tīklā, izmantojot privileģu pacelšanu, lai piekļūtu sensitīviem reģioniem. Pastāvība tiek nodrošināta, izvietojot atpakaļdveres un rootkit, ļaujot turpināt piekļuvi un datus eksfiltrēt bez drošības alarms.

Malaizīgie aktieri, īpaši valsts grupas un organizēti kiberuzbrukuma noziedznieki, bieži balstās uz APT, jo tās ir efektīvas, lai sasniegtu ilgtermiņa stratēģiskus mērķus. Lai gan mazāk bieži nekā masveida mērķētie uzbrukumi, piemēram, rēķināšanas programmatūra, APT pārstāv ievērojamu daļu no augstākā ietekmes kiberincidentiem. Viņu sarežģītība un potenciāls izraisīt būtiskas bojājumus padara tās par iecienītākajām metodēm izspiedēšanas, intelektuālās īpašuma nozagšanas vai sabotāžas veikšanai.

### Metricas un numurālie ierobežojumi

Nav pieejami.

### Galvenie atbilstīgi ES Nacionālā konvencija / daudzpusīgais traktāts

Internacionālie tiesību instruments, kas aptver APT, ietver plašāku kiber‑drošības un kiberizbrūku ietvaru. Budapešas konvencija par kiberizbrūkiem sniedz bāzi starptautiskai sadarbībai pretī kiberizbrūkiem, ieskaitot APT.

UN resolūcijas par kiberdrošību mudinās dalībvalstis pieņemt pasākumus, lai aizsargātu kritiskās infrastruktūras un veicinātu informācijas apmaiņu, lai novērstu kiberdraudējumus. Tomēr trūkums, kas koncentrējas tikai uz APT, norāda uz izaicinājumiem, lai pieņemtu šādus izsmalcinātos un mainīgus draudējumus pasaulē. Tādēļ, ja APT bieži tiek izpildītas valstisko aktīvu, to regulējumu būtu jāievēro starptautiskajā publiskajā tiesību jomā.

### Ietekme

Nav pieejami.

### Multihazard konteksts

Nav pieejami.

### Risku pārvaldība

Apsverot APT pretinieku, ir sarežģīta uzdevums, ņemot vērā laika, resursu un pūļu daudzumu, ko uzbrukējs ir gatavs iztērēt, lai pabeigtu operāciju. Turklāt, ņemot vērā daudzveidīgu pieeju, ko APT var pieņemt, ir grūti noteikt vispārīgos uzlabojumus, lai samazinātu risku. Komplekss un attīstās APT raksturs prasa pielāgotu un adaptīvu aizsardzības pieeju, jo neviens vienkāršs risinājums nav spējīgs pārvaldīt visas iespējamās draudes. Tādējādi organizācijām jāievieš vairākas stratēģijas, lai nodrošinātu robustu aizsardzību.

Saskaņā ar Asharani et al. (2019), aizsardzības stratēģijas pret izsmalcinātajām pastāvīgajām draudēm (APT) tiek sadalītas trīs galvenajās grupās: uzraudzība, noteikšana un mazināšana. Katrs spēlē kritisku lomu, lai samazinātu neautorizētas piekļuves risku.

#### Uzraudzība

Metodes: ietver ugunsmūrus un antivīrusu programmatūru, lai novērotu dažādus sistēmas posmus. Uzlabotie ugunsmūri spēj analizēt trafiku atpazīstamiem kaitīgajiem modeļiem un parādījumiem, kā arī izmantot uzvedības analīzi, lai noteiktu neparastas aktivitātes. Turklāt CPU izmantošana ir svarīga, jo neparasti parādītos uzbrukuma aktivitātes var liecināt par aizdomīgu uzvedību.

#### Noteikšana

Ietver dažādus anomaliju noteikšanas pasākumus, piemēram, statisko analīzi, neironu tīklus un mašīnmācīšanās pieejas (Hodge & Austin et al., 2004). Šie rīki palīdz identificēt APT, kas pastāv ilgāk nekā vidējais termins. Piemēram, IDS var analizēt tīkla trafiku, lai atklātu neparastas aktivitātes un brīdinātu drošības komandu par potenciālām draudiem.

#### Mazināšana

APT mazināšana tiek sasniegta ar reaktīviem un proaktīviem pieejām. Reaktīvie metodes ietver iespējamo uzbrukuma ceļu un uzbrukuma vektoru noteikšanu noteiktā brīdī, paredzēt kritiskos reģionus un novērtēt to smagumu. Proaktīvās stratēģijas, savukārt, koncentrējas uz klēpšanu uzbrukējiem. Šie rīki cenšas vilcināt intrūzīvus un liecināt par to, lai mainītu uzbrukuma stratēģiju, tādējādi samazinot draudze ietekmi.

### Atsauces

Alshamrani, A., Myneni, S., Chowdhary, A. un Huang, D., 2019. *Pētījums par izsmalcinātajām pastāvīgajām draudēm: tehnoloģijas, risinājumi, izaicinājumi un pētniecības iespējas.* IEEE Communications Surveys & Tutorials, vol. 21, no. 2, pp. 1851‑1877, 2021.  

*(pārējās atsauces kā iepriekš).*

```