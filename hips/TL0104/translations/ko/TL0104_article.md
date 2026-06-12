### 정의  
서비스 거부 공격은 자원에 대한 허가된 접근을 차단하거나 급박한 작업을 지연시키는 현상이다. (급박한은 밀리초에서 몇 시간까지 있을 수 있다) (NIST, 2017).  

### Primary reference(s)  
NIST, 2017. Computer Security. An Introduction to Information Security. Special Publication 800-12 Revision. National Institute of Standards and Technology (NIST). Accessed 25 January 2025.  

### Annotations  
#### Additional scientific description  
서비스 거부 공격(DoS)은 외부 입력(예: 들어오는 웹 트래픽)으로 컴퓨터 시스템이나 네트워크를 압도해 대상 사용자가 서비스를 이용할 수 없게 만든다. 이때 공격을 분산 서비스 거부 공격(DDoS)이라고 부르기도 하며, 취약점을 악용해 계산 자원을 고갈시키는 방식으로 진행될 수 있다. 이로 인해 사용자에게 서비스와 정보를 차단하고 운영과 재정에 큰 영향을 미친다 (CISA, 2021).  

분산 서비스 거부 공격은 인터넷에서 지속적인 골칫거리이며, 인터넷이 중앙 집중식 접근 제어를 갖지 않는다는 사실을 이용한다. 초기 인터넷 설계 시 이 취약점이 핵심 설계 요소로 남았기 때문에 DDoS 공격은 계속되어 왔다. 초기 공격은 해커 문화와 연관되었으나, 빠르게 상업적 악용으로 초점이 옮겨졌다. 또한 사이버 전쟁, 해크티비즘, 테러리즘 등 정치적 목적에서도 DDoS가 활용되었다 (Brooks et al, 2021).  

DoS와 DDoS의 역사는 사이버 보안 분야에서 잘 문서화되어 있다. 초기 인터넷 시대에도 이미 DoS 공격이 발생했으며, 1995년 프랑스에서 첫 사건이 일어나고 1996년 뉴욕에 기반을 둔 인터넷 서비스 제공업체 Panix에 대한 주요 사건이 이어졌다 (Brooks et al, 2021). 수년간 이러한 공격은 복잡성과 규모가 진화했으며, 2016년 Mirai 악성코드에 의해 구동된 봇넷 공격이 IoT 기기를 활용해 전 세계 주요 웹사이트를 마비시킨 사례가 대표적이다 (CISA, 2017).  

DoS는 인간 오류(예: 잘못된 구성), 기타 사고(예: 정전), 또는 고의적 공격으로 발생할 수 있다. DoS 공격에는 여러 기법이 사용된다. 주요 구분은 DoS와 DDoS의 차이이다. DoS 공격은 일반적으로 단일 출처에서 시스템을 대상으로 하지만, DDoS 공격은 다수의 손상된 시스템이 봇넷을 형성해 동시에 표적을 포화시켜 방어를 훨씬 어렵게 만든다. IoT 기기의 폭발적인 연결로 인해 각 기기가 봇넷의 일부가 될 수 있으므로 DDoS 공격 위험이 증가한다.  

서비스 거부 상태는 합법 사용자가 악의적인 사이버 위협 행위자의 행동으로 인해 정보 시스템, 장치 또는 기타 네트워크 자원에 접근할 수 없게 되는 상황이다. 서비스 거부 상태는 대상 호스트나 네트워크를 트래픽 과부하로 가득 채워 대상이 응답하지 못하거나 단순히 다운되게 하며, 이메일, 웹사이트, 온라인 계정(예: 은행) 등 다양한 서비스를 방해한다. DoS 공격은 조직의 시간과 자원을 소모시키며 자원과 서비스를 이용할 수 없게 만든다.  

DoS 공격은 방법에 따라 구분될 수 있다. 볼륨 기반 공격은 네트워크 대역폭을 초과시키며(예: 웹사이트에 과도한 트래픽을 보낸다), 계산 자원을 고갈시키는 공격은 잘못된 요청을 보내거나 무한 루프를 시작해 자원을 소모한다. DoS 공격은 핵심 인프라를 목표로 할 경우 국가 위험으로 확장될 수 있다. 예를 들어 2007년 에스토니아에 대한 사이버 공격은 조정된 DDoS 공격으로 정부, 은행, 미디어 웹사이트를 마비시켜 국가 수준에서 광범위한 혼란과 취약점을 드러냈다 (Ottis, 2008).  

DoS 공격은 실행이 상대적으로 쉽고 큰 혼란을 일으킬 수 있어 악의적 행위자에게 자주 이용된다. 매년 DoS와 DDoS 사건이 대규모로 보고되어 가장 흔한 사이버 공격 형태 중 하나가 되었다 (Bergamini de Neira et al, 2023). 2024년 NETSCOUT는 전 세계에서 1,300만 건이 넘는 DDoS 공격을 보고했으며, 다중 벡터 공격이 증가하는 추세를 보이고 있다 (NETSCOUT, 2024).  

### Drivers  
분산 서비스 거부 공격이 증가하는 가장 중요한 요인은 보안이 부족한 사물인터넷 기기의 확산이다. 현대 네트워크의 광범위한 연결성과 불충분한 보안 프로토콜은 공격자가 취약점을 악용해 DoS 공격을 실행할 수 있는 비옥한 토양을 제공한다.  

### Impacts  
서비스 거부 공격은 합법 사용자가 정보 시스템, 장치 또는 기타 네트워크 자원에 접근할 수 없게 만든다. 영향을 받는 서비스에는 이메일, 웹사이트, 온라인 계정(예: 은행) 등과 같이 대상 컴퓨터 또는 네트워크에 의존하는 서비스가 포함된다 (CISA, 2021). 분산 서비스 거부 공격은 자연 재해나 팬데믹 시 의료 또는 금융 시스템의 실패를 악화시킬 수 있다 (ENISA, 2023).  

### Multi-hazard context  
Not Available  

### Risk Management  
DoS 위험을 최소화하려면 기술적 조치와 전략적 조치가 결합돼야 한다. 강력한 네트워크 보안 프로토콜을 구현하고, 침입 탐지 및 방지 시스템을 활용하며, AI 기반 보안 솔루션을 채택하면 조직의 회복력을 높일 수 있다. 또한 비율 제한, 트래픽 필터링, 콘텐츠 배포 네트워크(CDN) 사용 등은 공격의 영향을 완화하는 데 도움이 된다.  

인공지능은 DoS 방어에 결정적인 역할을 할 수 있다. AI 시스템은 네트워크 트래픽을 분석해 이상 징후를 식별하고 실시간 탐지 및 대응을 가능하게 하며, 악성 트래픽을 필터링하고 리소스를 동적으로 할당하며 패턴과 행동을 기반으로 잠재적 위협을 예측한다. ITU는 지역 및 국제 수준에서 사이버 드릴을 수행함으로써 회원국의 사이버 보안 준비, 보호 및 사고 대응 능력을 향상시킨다 (ITU, no date). 사이버 드릴은 매년 진행되는 이벤트로, 사이버 공격, 정보 보안 사고 또는 기타 유형의 혼란을 시뮬레이션해 조직의 사이버 역량을 테스트한다. 사이버 드릴을 통해 참여자는 정책, 계획, 절차, 프로세스 및 준비, 예방, 대응, 복구 및 운영 연속성을 가능하게 하는 역량을 검증할 수 있다.  

### Monitoring  
Not Available  

### References  
Bergamini de Neira, A., Kantarci, B. and Nogueira, M., 2023. Distributed denial of service attack prediction: Challenges, open issues and opportunities. Computer Networks, 222(C), Feb. DOI: 10.1016/j.comnet.2022.109553 Accessed 3 April. 2025.  
Brooks, R.R., Yu, L., Ozcelik, I., Oakley, J. and Tusing, N., 2022. Distributed Denial of Service (DDoS): A History. IEEE Annals of the History of Computing, 44, pp.44–54. Accessed 3 April 2025.  
Cybersecurity and Infrastructure Security Agency (CISA), 2017. Heightened DDoS Threat Posed by Mirai and Other Botnets. Accessed 3 April 2025.  
Cybersecurity and Infrastructure Security Agency (CISA), 2021. Understanding Denial-of-Service Attacks. Accessed 3 April 2025.  
European Union Agency for Cybersecurity (ENISA), 2023. ENISA Threat Landscape 2023. Accessed 3 April 2025.  
International Telecommunication Union (ITU), no date. CyberDrills. Accessed 3 April 2025.  
NETSCOUT, 2024. Threat Intelligence Report 2024. Accessed 3 April 2025.  
Ottis, R., 2008. Analysis of the 2007 Cyber Attacks against Estonia from the Information Warfare Perspective. In: Proceedings of the 7th European Conference on Information Warfare and Security, Plymouth, 2008. Reading: Academic Publishing Limited, pp.163–168. Accessed 3 Apr. 2025.  
National Institute of Standards and Technology (NIST), 2017. Computer Security: An Introduction to Information Security. Special Publication 800-12 Revision 1. Gaithersburg, MD: U.S. Department of Commerce. Accessed 3 Apr. 2025.  
Cite this [Copy citation]