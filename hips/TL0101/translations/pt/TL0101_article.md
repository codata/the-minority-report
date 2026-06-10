```markdown
### Definição
Malware, termo genérico para diferentes formas de **software malicioso**, é projetado para infiltrar e infectar computadores, geralmente sem o conhecimento do proprietário (ITU, 2008).

### Referência Primária
ITU, 2008. *Estudo da União Internacional de Telecomunicações sobre os Aspectos Financeiros da Segurança de Rede: Malware e Spam*. União Internacional de Telecomunicações (ITU). Acesso em 31 de outubro de 2024.

### Anotações
#### Descrição Científica
Malware é a junção de *malicious software*. Refere‑se a software destinado a causar danos, interromper operações ou obter acesso não autorizado a sistemas, redes ou dispositivos. Abrange vários tipos de software nocivo, cada um com características e métodos de propagação específicos.

Malware costuma ser categorizado em **famílias** (um tipo particular com características únicas) e **variantes** (uma versão diferente de código dentro de uma família) (ITU, 2008).

**Tipos principais de malware:**
- **Vírus**: se anexam a programas legítimos e se propagam de dispositivo a dispositivo quando esses programas são executados.  
- **Worms (vermes)**: se replicam para espalhar-se para outros sistemas sem precisar de um programa hospedeiro.  
- **Trojan horses (cavalos de Tróia)**: se disfarçam de software benéfico para enganar usuários a executá‑los, comprometendo o sistema.  
- **Ransomware**: criptografa dados e exige pagamento em troca das chaves de descriptografia.  
- **Spyware**: coleta informações de forma oculta monitorando atividades dos usuários.  
- **Wiper (apagador)**: apaga ou corrompe permanentemente dados armazenados em máquinas infectadas.  
- **Rootkits**: permitem acesso não autorizado escondendo sua presença dentro do sistema.  

A história do malware remonta aos anos 80, quando surgiram os primeiros (Milošević, 2014). Incidentes notáveis incluem o *Morris Worm* (1988) e o ataque ransomware *WannaCry* (2017). Malware pode ser entregue por múltiplos vetores, como anexos de e‑mail (especialmente em ataques de phishing), sites maliciosos, downloads de software infectado ou via vulnerabilidades de rede.  

Hoje, atacantes usam inteligência artificial para criar malware avançado, como *polimórfico*, que altera seu código para escapar de medidas de segurança tradicionais. Além disso, o **malware sem arquivo** é uma ameaça crescente, pois escapa de antivírus tradicionais (Liu et al., 2024). Diferente do malware padrão que depende de arquivos ou executáveis, o malware sem arquivo explora ferramentas do sistema legítimo e aproveita arquivos, aplicações e serviços existentes para implementar atividades maliciosas.

**Exemplo de incidente:**
O *worm* Stuxnet, descoberto em 2010, foi projetado para sabotar instalações nucleares do Irã, destacando o potencial de armas cibernéticas causarem danos físicos e perturbar a segurança nacional (Zetter, 2014).

Agentes maliciosos recorrem ao malware pela sua versatilidade e eficácia. Malware continua sendo uma das formas mais comuns de ataque cibernético, com milhões de novas amostras detectadas anualmente (Statista, 2024). Serve diversos propósitos, desde ganho financeiro por ransomware até espionagem e interrupção de serviços.

### Métricas
- Mais de **1 bilhão** de novas variantes de malware foram detectadas globalmente em 2023 (Statista, 2024).

### Convenções e Tratados Multilaterais
Instrumentos legais internacionais que tratam de malware estão incluídos em quadros mais amplos de cibercrime.

- **Convenção de Budapeste sobre Cibercrime** do Conselho da Europa: diretrizes para cooperação internacional no combate à cibercrime, incluindo infrações envolvendo criação, distribuição ou uso de malware.
- **Código de Prática do Processo Pall Mall para Estados** (atualizado em 2025): diálogo inclusivo global para abordar a proliferação e uso irresponsável de ferramentas e serviços de intrusão cibernética comercial.

### Drivers
- Vulnerabilidades de software
- Aumento da dependência digital
- Economia da cibercrime
- Tensões geopolíticas

### Impactos
Ataques de malware podem escalar para perigos nacionais quando visam infraestrutura crítica ou sistemas governamentais. O *worm* Stuxnet exemplifica essa ameaça, demonstrando como armas cibernéticas podem causar danos físicos e perturbar a segurança nacional.

### Contexto Multi‑Hazard
Malware pode causar interrupção significativa de serviços, perdas financeiras, perda de receita, perda ou roubo de dados e inteligência, danos à infraestrutura de TI, danos reputacionais a organizações e indivíduos, além de exigir pagamento de resgates e multas regulatórias. Pode aumentar custos de recuperação e contribuir para a perda de confiança pública em organizações, políticos e setor público.  

Sistemas de software interconectados com sistemas físicos podem ser explorados por malware para abrir outros perigos, como aumento de químicos em instalações de distribuição de água para envenenar populações, manipulando sistemas de água (Sikder et al., 2023).

### Gestão de Risco
Defender contra malware requer, em primeiro lugar, conscientização do usuário, pois a maioria dos malware é ativada por entrada do usuário (ex.: clique em link fraudulento ou comprometido). Medidas técnicas—uso de antivírus e software anti‑malware, atualizações regulares de sistema e patches, segmentação de rede—podem oferecer camadas adicionais de proteção, mas não substituem a conscientização do usuário.

### Monitoramento
O monitoramento de ameaças ocorre em níveis internacional, nacional, setorial e organizacional, onde informações sobre identificação de malware são compartilhadas por diversos mecanismos para mitigar riscos.

### Referências
- União Internacional de Telecomunicações (ITU), 2008. *Estudo da União Internacional de Telecomunicações sobre os Aspectos Financeiros da Segurança de Rede: Malware e Spam*. Genebra: ITU.  
- Liu, S., Peng, G., Zeng, H. e Fu, J., 2024. Uma pesquisa sobre a evolução de ataques sem arquivo e técnicas de detecção. [online] Acesso em 16 de janeiro de 2025.  
- Milošević, N., 2014. História do malware. [online] Acesso em 16 de janeiro de 2025.  
- Sikder, M.N.K., Nguyen, M.B.T., Elliott, E.D. e Batarseh, F.A., 2023. Deep H2O: Detecção de ataques cibernéticos em sistemas de distribuição de água usando aprendizado profundo. *Journal of Water Process Engineering*, 52, 103568. [online] DOI: 10.1016/j.jwpe.2023.103568. Acesso em 16 de janeiro de 2025.  
- Statista, sem data. Número anual de novas variantes de malware detectadas mundialmente de 2019 a 2023. [online] Acesso em 16 de janeiro de 2025.  
- Zetter, K., 2014. Um olhar sem precedentes em Stuxnet, a primeira arma digital do mundo. *Wired*. [online] Acesso em 16 de janeiro de 2025.
```