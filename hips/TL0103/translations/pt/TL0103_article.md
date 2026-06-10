```markdown
### Definição
Uma **ameaça avançada** é criada por um adversário com níveis sofisticados de experiência e recursos significativos, permitindo que, por meio de múltiplos vetores de ataque (por exemplo, cibernético, físico e de decepção), gere oportunidades para alcançar seus objetivos (NIST, 2012).

### Referência Principal
Instituto Nacional de Padrões e Tecnologia (NIST), 2012. **Guia para a realização de avaliações de risco**. DOI:10.6028/NIST.SP.800-30r1. Acessado 25 de janeiro de 2025.

### Anotações
A **Ameaça Persistente Avançada (APT)** em cibersegurança refere‑se a um ataque cibernético prolongado e direcionado, onde, muitas vezes, um usuário não autorizado obtém acesso a uma rede e permanece indetectado por um período prolongado. O objetivo principal das APTs costuma ser observar a atividade da rede, furtar dados ou causar perturbações, em vez de infligir danos imediatos. Essa ameaça é considerada “avançada” devido às técnicas sofisticadas empregadas para explorar vulnerabilidades, e “persistente” pela continuação do esforço para atingir um objetivo específico.

Um dos primeiros incidentes reconhecidos de APT foi o ataque Titan Rain entre 2003 e 2006, onde atacantes infiltraram redes de defesa dos EUA para roubar informações sensíveis (Council of Foreign Relations 2005). A descoberta da *Stuxnet* em 2010 marcou uma escalada significativa, demonstrando a capacidade das APTs de causar dano físico ao atacar os centrífugos nucleares do Irã (Zetter 2014). Outro exemplo notável é o ataque Operation Aurora em 2009, que alvos múltiplas empresas, incluindo o Google, para acessar propriedade intelectual e contas de e‑mail de ativistas (Council of Foreign Relations 2010). Incidentes recentes, como SolarWinds (2020) e as campanhas Nobelium (2022), exemplificam a evolução das técnicas de APT direcionadas a cadeias de suprimentos e infra‑estrutura de nuvem (Ghanbari et al., 2024).

As APTs empregam uma variedade multifacetada de técnicas para atingir seus objetivos. Estes ataques são projetados em torno das características de seus alvos e, portanto, podem assumir muitas formas. Frequentemente, eles começam com intrusão no sistema alvo usando spear‑phishing, vulnerabilidades de dia zero ou outras técnicas avançadas para infiltrar sistemas sem ser detectado. Uma vez dentro, os atacantes podem permanecer silenciosos, monitorando tráfego e reunindo informações, ou usar movimento lateral para navegar pela rede, empregando escalada de privilégios para acessar áreas sensíveis. A persistência é mantida por meio do deployment de backdoors e rootkits, permitindo acesso contínuo e exfiltração de dados sem disparar alarmes de segurança.

Atores maliciosos, especialmente grupos de Estado e criminosos cibernéticos organizados, frequentemente recorrem a APTs devido à sua eficácia em alcançar metas estratégicas de longo prazo. Embora menos comuns que ataques massivos como ransomware, as APTs representam uma parcela significativa de incidentes cibernéticos de alto impacto. Sua complexidade e potencial de dano substancial as tornam métodos preferidos para espionagem cibernética, roubo de propriedade intelectual ou sabotagem.

### Métricas e Limites Numéricos
Não aplicável.

### Convenção/Tratado Multilateral Relevante
Os instrumentos legais internacionais que abordam as APTs estão incluídos em frameworks mais amplos de cibersegurança e criminosidade cibernética. A Convenção de Budapeste sobre Crimes Cibernéticos da União Europeia fornece base para cooperação internacional no combate a crimes cibernéticos, incluindo aqueles que envolvem APTs.

As resoluções da ONU sobre cibersegurança encorajam os Estados-membros a adotar medidas para proteger a infraestrutura crítica e promover a troca de informações para prevenir ameaças cibernéticas. No entanto, a ausência de tratados específicos focados apenas em APTs destaca desafios na abordagem de ameaças sofisticadas e evolutivas globalmente.

Como as APTs são frequentemente conduzidas por atores de Estado, sua regulação caberia ao âmbito do Direito Público Internacional.

### Drivers
Não aplicável.

### Impacts
Não aplicável.

### Multi‑hazard Context
Não aplicável.

### Gestão de Risco
Defender contra uma APT é uma tarefa complexa, considerando o tempo, recursos e esforço que o atacante está disposto a investir para cumprir sua operação. Além disso, dado o diverso conjunto de abordagens que uma APT pode adotar, é difícil prescrever estratégias a priori que minimizem o risco em todos os casos. A natureza complexa e evolutiva das APTs requer uma abordagem de defesa adaptativa e sob medida, pois nenhuma solução única pode lidar com todas as ameaças potenciais. Em vez disso, as organizações devem integrar múltiplas estratégias para garantir proteção robusta. De acordo com Asharani et al. (2019), as estratégias de defesa contra APTs são categorizadas em três grupos principais: monitoramento, detecção e mitigação. Cada um desempenha um papel crítico na redução do risco de acesso não autorizado.

#### Metodologias de Monitoramento
Envolvem o uso de ferramentas como firewalls e antivírus para observar diversas partes do sistema. Firewalls avançados são capazes de analisar tráfego em busca de padrões maliciosos conhecidos e assinaturas, além de empregar análise comportamental para detectar atividade anormal. A monitorização do uso da CPU também é importante, pois padrões incomuns de utilização de recursos podem indicar comportamento suspeito.

#### Metodologias de Detecção
Incluem o uso de diversas técnicas de detecção de anomalias, como análise estática, redes neurais e abordagens de aprendizado de máquina (Hodge e Austin et al., 2004). Essas técnicas ajudam a identificar APTs que persistem ao longo do médio e longo prazo. Por exemplo, um Sistema de Detecção de Intrusão (IDS) pode analisar o tráfego de rede para identificar atividade incomum e alertar equipes de segurança sobre potenciais ameaças.

#### Metodologia de Mitigação
A mitigação de APT pode ser alcançada por abordagens reativas e proativas. Métodos reativos envolvem a identificação de potenciais caminhos de ataque e vulnerabilidades em um dado momento, a previsão de áreas críticas e a avaliação de sua severidade. Estratégias proativas, por outro lado, concentram‑se em enganar os atacantes. Essas técnicas visam desviar intrusos e fazê‑los alterar suas estratégias de ataque, reduzindo assim o impacto da ameaça.

### Monitoramento
Não aplicável.

### Referências
- Alshamrani, A., Myneni, S., Chowdhary, A. & Huang, D., 2019. *A survey on advanced persistent threats: Techniques, solutions, challenges, and research opportunities*. In IEEE Communications Surveys & Tutorials, vol. 21, no. 2, pp. 1851–1877. DOI:10.1109/COMST.2019.2891891. Acessado 16 jan. 2025.
- Brandão, P.R. & Limonova, V., 2021. *Defense methodologies for advanced persistent threats (APTs)*. American Journal of Applied Sciences, 2021. DOI:10.3844/ajassp.2021.207.212. Acessado 16 jan. 2025.
- Conselho de Relações Exteriores (CFR), 2005. *Titan Rain*. Acessado 16 jan. 2025.
- Conselho de Relações Exteriores (CFR), 2010. *Operation Aurora*. Acessado 16 jan. 2025.
- Ghanbari, H., Koskinen, K. & Wei, Y., 2024. *From SolarWinds to Kaseya: The rise of supply chain attacks in a digital world*. Journal of Information Technology Teaching Cases, 0(0). DOI:10.1177/20438869241299823. Acessado 16 jan. 2025.
- Hodge, V.J. & Austin, J., 2004. *A survey of outlier detection methodologies*. Artificial Intelligence Review, 22, pp. 85–126. Acessado 16 jan. 2025.
- Instituto Nacional de Padrões e Tecnologia (NIST), 2012. *Special Publication 800‑30 Revision 1: Guide for Conducting Risk Assessments*. Gaithersburg, MD: U.S. Department of Commerce. Acessado 16 jan. 2025.
- Zetter, K., 2014. *An unprecedented look at Stuxnet, the world’s first digital weapon*. WIRED Magazine. Acessado 16 jan. 2025.
```

*All headings have been converted to Markdown format, legacy formatting removed, and terminology has been aligned with the Controlled Vocabulary for Disaster Risk Reduction in Portuguese.*