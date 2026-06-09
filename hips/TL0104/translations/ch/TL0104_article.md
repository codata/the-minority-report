```markdown
### Definition
拒绝服务（Denial of Service, DoS）是阻止授权用户访问资源或延迟关键时间操作的行为（关键时间可为毫秒亦可为小时，取决于所提供的服务）(NIST, 2017)。

### Primary reference(s)
NIST, 2017. Computer Security. An Introduction to Information Security. Special Publication 800‑12 Revision. National Institute of Standards and Technology (NIST). Accessed 25 January 2025.

### Annotations
#### Additional scientific description
拒绝服务攻击（DoS）通过向计算机系统或网络注入外部流量（例如进入的网络流量）使其对预期用户不可用。在此过程中，往往会出现分布式拒绝服务（DDoS），或利用其漏洞耗尽计算资源。该中断导致用户无法访问服务和信息，造成显著的运营和财务影响（CISA, 2021）。分布式拒绝服务攻击在互联网上仍然是持久的麻烦。它们利用互联网缺乏集中访问控制的事实。由于这一脆弱性是早期互联网的核心设计决定，DDoS攻击一直存在。早期攻击与黑客文化相关，但其焦点很快转向商业利用。也出现了多种政治用途的DDoS，包括网络战争、黑客激进主义和恐怖主义（Brooks 等，2021）。DoS 与 DDoS 的使用在网络安全史中有充分记录。早期攻击可追溯至早期互联网时代，其中第一起事件发生在1995年的法国，随后一年在纽约市的互联网服务提供商 Panix 上发生重大事件（Brooks 等，2021）。多年后，这些攻击在复杂性和规模上不断演变，2016 年由 Mirai 恶意软件驱动的僵尸网络攻击就是一个例子，该攻击利用物联网设备发动大规模 DDoS，扰乱全球主要网站（CISA, 2017）。DoS 可能由人为错误（如错误配置）、其他事件（如电源中断）或有意攻击造成。不同技术被用于 DoS 攻击。主要区别在于 DoS 与 DDoS 攻击。DoS 攻击通常来自单一源头针对系统，而 DDoS 攻击涉及多个受感染系统，常形成僵尸网络，同时淹没目标，使防御更具挑战。连接设备数量的增加——尤其是在物联网热潮背景下——也在提高 DDoS 发生风险，因为每个连接设备都有可能成为僵尸网络的一部分。拒绝服务（DoS）攻击发生时，合法用户因恶意网络威胁行为者的行为无法访问信息系统、设备或其他网络资源。拒绝服务状态用流量淹没目标主机或网络，直到目标无法响应或直接崩溃，影响电子邮件、网站、在线账户（如银行）或其他服务。DoS 攻击会使组织在资源和服务无法访问期间付出时间和金钱成本。DoS 攻击可按方法进一步分类：基于量的攻击压倒网络带宽（如用过量流量淹没网站），而利用计算限制的攻击则发送结构错误的请求或启动无限循环以耗尽计算资源。DoS 攻击可升级为国家级风险，当它们针对关键基础设施时。2007 年对爱沙尼亚的协调 DDoS 攻击就是一个先例，破坏了政府、银行和媒体网站，导致广泛中断并凸显了国家层面的脆弱性（Ottis, 2008）。DoS 攻击由于易于执行且可能造成显著破坏，被恶意行为者广泛使用。每年，数据记录大量 DoS 和 DDoS 事件，使其成为最常见的网络攻击形式之一（Bergamini de Neira 等，2023）。2024 年，NETSCOUT 报告全球超过 1300 万起 DDoS 攻击，且多向量攻击趋势上升（NETSCOUT, 2024）。

### Drivers
最关键的因素之一是未受保护的物联网设备的普及。现代网络中广泛的连接性和不足的安全协议为攻击者提供了肥沃的土壤，能够利用漏洞并发动成功的 DoS 攻击。

### Impacts
拒绝服务（DoS）攻击发生时，合法用户因恶意网络威胁行为者的行为无法访问信息系统、设备或其他网络资源。受影响的服务可能包括电子邮件、网站、在线账户（如银行）或其他依赖受影响计算机或网络的服务（CISA, 2021）。DDoS 攻击在自然灾害或疫情期间可加剧医疗或金融系统故障（ENISA, 2023）。

### Multi-hazard context
暂无

### Risk Management
降低 DoS 风险需要技术和战略措施相结合。实施健全的网络安全协议、使用入侵检测与预防系统，并采用人工智能驱动的安全解决方案，可提升组织韧性。此外，速率限制、流量过滤和内容分发网络等策略有助于减轻攻击影响。人工智能还可以在检测和响应中发挥关键作用，实时识别异常、过滤恶意流量、动态分配资源并基于模式预测潜在威胁。ITU 通过在地区和国际层面开展网络演习，提高成员国的网络安全准备、保护和事件响应能力（ITU, 无日期）。网络演习是一年一度的活动，模拟网络攻击、信息安全事件或其他破坏类型，以测试组织的网络能力，从检测事件到适当响应并最小化相关影响。通过网络演习，参与者可验证政策、计划、程序、流程和能力，以实现准备、预防、响应、恢复和业务连续性。

### Monitoring
暂无

### References
Bergamini de Neira, A., Kantarci, B. and Nogueira, M., 2023. Distributed denial of service attack prediction: Challenges, open issues and opportunities. Computer Networks, 222(C), Feb. DOI: 10.1016/j.comnet.2022.109553 Accessed 3 April 2025.

Brooks, R.R., Yu, L., Ozcelik, I., Oakley, J. and Tusing, N., 2022. Distributed Denial of Service (DDoS): A History. IEEE Annals of the History of Computing, 44, pp.44–54. Accessed 3 April 2025.

Cybersecurity and Infrastructure Security Agency (CISA), 2017. Heightened DDoS Threat Posed by Mirai and Other Botnets. Accessed 3 April 2025.

Cybersecurity and Infrastructure Security Agency (CISA), 2021. Understanding Denial-of-Service Attacks. Accessed 3 April 2025.

European Union Agency for Cybersecurity (ENISA), 2023. ENISA Threat Landscape 2023. Accessed 3 April 2025.

International Telecommunication Union (ITU), no date. CyberDrills. Accessed 3 April 2025.

NETSCOUT, 2024. Threat Intelligence Report 2024. Accessed 3 April 2025.

Ottis, R., 2008. Analysis of the 2007 Cyber Attacks against Estonia from the Information Warfare Perspective. In: Proceedings of the 7th European Conference on Information Warfare and Security, Plymouth, 2008. Reading: Academic Publishing Limited, pp.163–168. Accessed 3 Apr. 2025.

National Institute of Standards and Technology (NIST), 2017. Computer Security: An Introduction to Information Security. Special Publication 800-12 Revision 1. Gaithersburg, MD: U.S. Department of Commerce. Accessed 3 Apr. 2025.

Cite this [Copy citation]
```