### Définition  
Une **attaque de la chaîne d’approvisionnement** se produit lorsqu’un produit, service ou technologie que vous recevez a été violé ou compromis, puis est utilisé pour infiltrer et compromettre davantage vos propres systèmes (ICO, sans date).

### Références principales  
- ICO, sans date, **Attaque de la chaîne d’approvisionnement**. Consulté le 25 janvier 2025.

### Annotations

#### Description scientifique supplémentaire  
En **cybersécurité**, les attaques de la chaîne d’approvisionnement consistent à exploiter les faiblesses de sécurité d’une organisation afin d’infiltrer ses systèmes et réseaux. Les attaquants ciblent les éléments les moins sécurisés de la chaîne, tels que les **fournisseurs tiers**, les **fournisseurs** ou les **fournisseurs cloud**, dans le but de compromettre la cible finale en tirant parti de l’interconnexion des écosystèmes numériques modernes. Cette méthode permet aux attaquants de contourner les mesures de sécurité traditionnelles en exploitant les relations de confiance.  
L’histoire des attaques de la chaîne d’approvisionnement a évolué parallèlement à la complexité croissante des réseaux mondiaux. Les premières instances notables comprennent l’attaque de 2011 sur RSA Security, où les attaquants ont compromis les jetons SecurID via un fournisseur pour infiltrer les entrepreneurs de défense (Greenberg, 2021). Plus récemment, l’attaque SolarWinds de 2020 a démontré l’impact sévère de ces violations. Dans cet incident, des acteurs de menace sophistiqués ont inséré du code malveillant dans les mises à jour logicielles de l’entreprise, affectant de nombreuses organisations gouvernementales et privées à travers le monde et soulignant les vulnérabilités inhérentes aux chaînes d’approvisionnement (Williams, 2020).

#### Techniques courantes  
Les techniques courantes comprennent :  
- sabotage des **mises à jour logicielles** (ex. SolarWinds)  
- compromission des **dépôts de code**  
- infection des **composants matériels** durant la fabrication  
- exploitation des vulnérabilités dans les services tiers.  
Les attaquants peuvent insérer du code malveillant dans des mises à jour légitimes ou exploiter des backdoors dans les dispositifs matériels pour obtenir un accès non autorisé.

#### Attaques basées sur l’identité  
De nombreuses organisations dépendent des **fournisseurs cloud** pour gérer leurs environnements cloud, ce qui a conduit les attaquants à se concentrer sur ces prestataires dans une forme unique d’attaque : **attaque basée sur l’identité**. Ces attaques exploitent les autorisations étendues souvent accordées aux comptes de fournisseurs, qui peuvent accéder à plusieurs environnements clients. Cet accès interconnecté augmente le potentiel d’impact d’une compromission, faisant des fournisseurs une cible attractive (Microsoft, 2023).

#### Logiciel open‑source  
L’une des attaques les plus significatives provient du **logiciel open‑source**. Les communautés open‑source offrent de nombreux modules et paquets largement utilisés par les entreprises dans le monde, y compris ceux dans les chaînes d’approvisionnement. Cependant, faute d’une propriété claire et d’une sécurité garantie, ce type de logiciel introduit fréquemment des vulnérabilités dans les architectures de sécurité (Forbes, 2022).

#### Hijacking et signature de code  
Une autre technique dominante est l’enlèvement des mises à jour et la compromission de la signature de code. Les fournisseurs distribuent régulièrement des mises à jour depuis des serveurs centralisés. Les acteurs de menace peuvent infiltrer le réseau du fournisseur pour insérer un malware dans une mise à jour ou la modifier afin de gagner un contrôle non autorisé. La **signature de code** est un mécanisme de vérification de l’authenticité et de l’intégrité du logiciel. Les attaquants sapent ce processus en utilisant des certificats auto‑signés, en exploitant des contrôles d’accès mal configurés ou en compromettant les systèmes de signature. En se faisant passer pour des fournisseurs de confiance et en incorporant du code malveillant dans les mises à jour, les attaquants peuvent exécuter des attaques hautement trompeuses et destructrices (NIST, 2021). En 2023, les attaquants ont compromis l’application de bureau 3CX via des installateurs infectés, diffusant un malware à travers un système VoIP largement utilisé (Fortiguard, 2023).

#### Motivation des attaquants  
Les acteurs malveillants privilégient les attaques de la chaîne d’approvisionnement en raison de leur impact élevé et de la difficulté de détection. La complexité des chaînes d’approvisionnement modernes et la dépendance vis-à-vis des fournisseurs tiers créent de nombreuses opportunités d’exploitation, faisant de cette forme d’attaque une préoccupation majeure en cybersécurité. Parallèlement, ces attaques sont souvent ciblées ; seuls les acteurs disposant de ressources et de capacités supérieures peuvent les mener à bien.

### Gestion des risques  
Se défendre contre les attaques de la chaîne d’approvisionnement nécessite une approche globale incluant :  
- un contrôle rigoureux des fournisseurs,  
- la mise en œuvre de normes de sécurité strictes,  
- une surveillance continue,  
- la promotion de la collaboration entre organisations et partenaires.  

Étant donné que de nombreuses attaques reposent sur des fournisseurs externes avec des dépendances complexes dans leurs outils et services, atteindre une protection complète est difficile. Cependant, les organisations peuvent adopter des stratégies proactives, telles que :  

#### Évaluation des risques tiers  
- tester les logiciels tiers avant déploiement,  
- exiger que les fournisseurs se conforment à des politiques de sécurité spécifiques,  
- implémenter une **Politique de Sécurité de Contenu (CSP)** pour contrôler les ressources exécutables dans le navigateur,  
- utiliser l’**Intégrité des Sous‑ressources (SRI)** pour détecter un contenu JavaScript suspect.

#### Zero Trust  
Zero Trust garantit que tous les utilisateurs – employés, contractants et fournisseurs – sont continuellement vérifiés et surveillés au sein du réseau de l’organisation. En vérifiant l’identité et les privilèges des utilisateurs et des appareils, Zero Trust empêche les attaquants d’exploiter des identifiants d’utilisateur légitimes volés pour infiltrer l’organisation.

#### DevSecOps  
La sécurité de la chaîne d’approvisionnement exploite DevSecOps pour se défendre contre les attaques en découvrant d’abord tous les composants, en obtenant une visibilité sur la chaîne d’approvisionnement et en sécurisant les composants d’applications cloud‑native. En intégrant la sécurité tout au long du processus de développement, DevSecOps assure le déploiement en temps réel des opérations de sécurité tout en s’alignant sans faille sur les objectifs commerciaux (GitLab, sans date).

### Surveillance  
Non applicable.

### Références  
- Cloudflare, sans date. *What is supply chain attack?* Consulté le 16 janvier 2025.  
- Forbes, 2022. *Mitigating the risk of supply chain attacks in the age of cloud computing.* Consulté le 15 janvier 2025.  
- FortiGuard Labs, 2023. *Threat Signal Report: Supply Chain Attack Through 3CX Desktop App.* Consulté le 15 janvier 2025.  
- GitLab, sans date. *What is DevSecOps?* Consulté le 16 janvier 2025.  
- Greenberg, A., 2021. *The Full Story of the Stunning RSA Hack Can Finally Be Told.* Consulté le 15 janvier 2025.  
- Information Commissioner’s Office (ICO), sans date. *Supply chain attacks.* Consulté le 15 janvier 2025.  
- Microsoft, 2023. *Announcing Microsoft Defender for Cloud Capabilities to Counter Identity-Based Supply Chain Attacks.* Microsoft Tech Community. Consulté le 15 janvier 2025.  
- National Institute of Standards and Technology (NIST), 2021. *Defending Against Software Supply Chain Attacks.* Consulté le 16 janvier 2025.  
- Williams, J., 2020. *What You Need to Know About the SolarWinds Supply‑Chain Attack.* SANS Institute.