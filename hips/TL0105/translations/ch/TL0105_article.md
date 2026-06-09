### Definition  
供应链攻击是指通过对供应链中产品、服务或技术的渗透或破坏，使其被用于渗透并进一步危害组织自身系统的行为（信息专员办公室，未注明日期）。  

### Primary reference(s)  
信息专员办公室（ICO），未注明日期，《供应链攻击》。访问时间：2025‑01‑25。  

### Annotations  
#### 额外的科学描述  
在网络安全领域，供应链攻击指利用组织供应链中的安全弱点渗透其系统和网络。攻击者聚焦于供应链中安全性较低的环节（如第三方供应商、云服务提供商等），借助现代数字生态系统的互联性突破最终目标。此方法使攻击者可通过利用受信任关系绕过传统安全措施。供应链攻击的历史与全球供应网络日益复杂并行演变。早期案例包括 2011 年 RSA Security 的攻击，攻击者通过供应商侵入 SecurID 令牌以渗透防御承包商（Greenberg，2021）。2020 年 SolarWinds 攻击展示了此类渗透的严重影响——威胁行动者将恶意代码注入软件更新，影响全球众多政府与私营机构，凸显了供应链固有的脆弱性（Williams，2020）。  

供应链攻击采用多种技术：  
- 篡改软件更新（如 SolarWinds 攻击）  
- 破坏代码仓库  
- 在制造过程中感染硬件组件  
- 利用第三方服务漏洞  

攻击者可将恶意代码插入合法软件更新，或利用硬件设备后门获取未经授权访问。  

许多组织依赖第三方服务提供商管理云环境，导致攻击者将重点放在这些提供商上，形成独特的身份基础供应链攻击。此类攻击利用服务提供商账户的广泛权限，可能访问多客户环境，提升潜在危害（Microsoft，2023）。  

另一重要来源是开源软件。开源社区提供众多模块与包，被全球企业广泛使用。因缺乏明确所有权与安全保障，开源软件经常将漏洞注入安全架构（Forbes，2022）。  

劫持更新与破坏代码签名亦是关键技术。软件供应商通过集中服务器分发更新，威胁行动者可渗透供应商网络注入恶意软件或修改更新以获取未授权控制。代码签名用于验证软件真实性与完整性，是攻击目标之一。恶意行为者通过自签名证书、配置错误的访问控制或破坏签名系统来破坏此流程。通过冒充受信任供应商并嵌入恶意代码，攻击者可执行高度欺骗且具破坏性的攻击（NIST，2021）。  

2023 年，攻击者通过感染的安装程序入侵 3CX 桌面应用，借此在广泛使用的 VoIP 系统中传播恶意软件（FortiGuard，2023）。恶意行为者日益依赖供应链攻击，因其高影响力与检测难度。现代供应链的复杂性和对第三方提供商的依赖为利用提供了众多机会，使供应链攻击成为网络安全的重要关注点。与此同时，供应链攻击通常高度针对性，只有资源与能力更高的攻击者（通常）能执行此类攻击。  

### Metrics and numeric limits  
不适用。  

### Key relevant UN convention / multilateral treaty  
涉及供应链攻击的国际法律工具包含在更广泛的网络安全与网络犯罪框架内。欧洲理事会的布达佩斯网络犯罪公约为打击网络犯罪（包括可能涉及供应链攻击的罪行）提供国际合作指南。  

### Drivers  
供应链攻击通过利用或更改第三方软件、硬件或应用程序，给组织带来重大挑战。  

### Impacts  
- 欺诈  
- 盗窃  

### Multi‑hazard context  
不适用。  

### Risk Management  
防御供应链攻击需综合方法：  
1. **严格审查供应商**：在部署前测试第三方软件，要求供应商遵守安全政策。  
2. **实施内容安全策略（CSP）**：控制浏览器中可执行资源。  
3. **使用子资源完整性（SRI）**：检测可疑 JavaScript 内容。  
4. **实施零信任（Zero Trust）**：持续验证与监控所有用户与设备，防止利用被盗凭据渗透。  
5. **采用 DevSecOps**：在整个开发生命周期内集成安全，提升供应链可见性与云原生应用组件安全。  

### Monitoring  
不适用。  

### References  

- Cloudflare（未注明日期）。What is supply chain attack? 访问时间：2025‑01‑16。  
- Forbes（2022）。Mitigating the risk of supply chain attacks in the age of cloud computing。访问时间：2025‑01‑15。  
- FortiGuard Labs（2023）。Threat Signal Report: Supply Chain Attack Through 3CX Desktop App。访问时间：2025‑01‑15。  
- GitLab（未注明日期）。What is DevSecOps? 访问时间：2025‑01‑16。  
- Greenberg, A.（2021）。The Full Story of the Stunning RSA Hack Can Finally Be Told。访问时间：2025‑01‑15。  
- Information Commissioner’s Office (ICO)（未注明日期）。Supply chain attacks。访问时间：2025‑01‑15。  
- Microsoft（2023）。Announcing Microsoft Defender for Cloud Capabilities to Counter Identity-Based Supply Chain Attacks。Microsoft Tech Community。访问时间：2025‑01‑15。  
- National Institute of Standards and Technology (NIST)（2021）。Defending Against Software Supply Chain Attacks。访问时间：2025‑01‑16。  
- Williams, J.（2020）。What You Need to Know About the SolarWinds Supply‑Chain Attack。SANS Institute。  

---