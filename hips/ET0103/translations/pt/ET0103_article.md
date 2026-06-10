```markdown
### Definição
Uma *erupção solar* é uma explosão súbita e de grande magnitude no Sol caracterizada pela liberação rápida de energia, resultando na emissão de radiação eletromagnética em todas as faixas de comprimento de onda e no aumento rápido de brilho em uma parte da superfície solar. A explosão de energia eletromagnética viaja na velocidade da luz, portanto qualquer efeito sobre o lado iluminado da atmosfera externa da Terra ocorre simultaneamente ao evento observado (Centro de Previsão de Clima Espacial da NOAA, 2023).

### Referência Primária
- Centro de Previsão de Clima Espacial da NOAA, 2023. **ERUPÇÕES SOLARES (BLACKOUTS DE RÁDIO)**. Acesso em 31 de janeiro de 2025.

### Anotações
#### Descrição científica adicional
Erupções solares ocorrem predominantemente em **regiões ativas** no Sol, que são caracterizadas pela presença de campos magnéticos intensos, frequentemente associados a grupos de manchas solares. Conforme esses campos magnéticos mudam e evoluem, podem atingir um estado de instabilidade, resultando na liberação de energia em várias formas. Uma das manifestações principais dessa liberação de energia é observada como erupção solar, envolvendo a emissão de radiação eletromagnética.

Erupções são mais prováveis de ocorrer durante períodos de alta atividade solar e são frequentemente acompanhadas por ejeções de massa coronal (CME). Elas são classificadas com base em sua intensidade, determinada principalmente pela luminosidade de raios‑X e medida na banda 1‑8 Å (0,1‑0,8 nm). Existem cinco categorias de erupções, variando do mais fraco ao mais forte: **A, B, C, M, X** (Hanslmeier, 2007; Schrijver, 2009). A informação sobre a intensidade das erupções é obtida a partir de sensores de raios‑X e ultra‑violeta extremo instalados em satélites GOES (Thiemann et al., 2019; Machol et al., 2020).

Sob condições favoráveis de observação, quando a região ativa correspondente está voltada para a Terra, uma erupção intensa, tipicamente de classe **X** e ocasionalmente **M**, pode levar a distúrbios significativos na ionosfera do lado iluminado da Terra. Esses distúrbios podem causar distorções de sinal e *fadeouts* de rádio devido à maior absorção de ondas de rádio na ionosfera inferior, especificamente nas **regiões D** e **E** inferiores.

Sob condições regulares, ondas de rádio HF suportam comunicação de longa distância refratando através das camadas superiores da ionosfera. Contudo, durante uma erupção solar poderosa, a ionização aumenta na ionosfera inferior, particularmente nas regiões D e E inferiores. Esse fenômeno pode levar à degradação ou absorção completa das ondas de rádio HF, resultando em um *fadeout* de rádio que afeta predominantemente a faixa de frequência 3‑30 MHz.

Estalos de rádio são associados a erupções solares. O atraso na registração de suas diferentes frequências de rádio na órbita da Terra é devido ao movimento de afastamento da fonte. Grandes estalos duram em média 10‑20 minutos. Tempestades de ruído de rádio mais longas, de níveis de radiação altos e variáveis, originam em grupos de manchas solares, áreas de campos magnéticos intensos. Um **Estalo Radio Solar (ERS)** pode influenciar os sinais de GNSS por interferências diretas de ondas de rádio.

#### Métricas e Limites Numéricos
A intensidade das erupções solares cobre uma ampla gama e é classificada em termos de pico de emissão na banda espectral 0,1‑0,8 nm (raios X suaves) do XRS NOAA/GOES. Erupções solares são classificadas usando uma escala de cinco níveis introduzida pela Administração Nacional Oceânica e Atmosférica dos EUA (NOAA) em 1999. A escala está atualmente em revisão e apresentada abaixo. Os níveis de fluxo de raios‑X começam com o nível **A** (≥ 10⁻⁸ W m⁻²). O próximo nível, dez vezes maior, é o nível **B** (≥ 10⁻⁷ W m⁻²), seguido pelos **C** (10⁻⁶ W m⁻²), **M** (10⁻⁵ W m⁻²) e finalmente **X** (≥ 10⁻⁴ W m⁻²) (NOAA, 2023).

### Escala de Intensidade
| Nível | Fluxo de raios‑X (W m⁻²) | Efeito físico | Frequência média (1 ciclo = 11 anos) |
|-------|--------------------------|---------------|--------------------------------------|
| **R5** | > 10⁻³ | Blackout de HF completo no lado iluminado da Terra, duração de horas. | < 1 por ciclo |
| **R4** | > 10⁻⁴ | Blackout de HF na maioria do lado iluminado, duração 1‑2 h. | 8 dias por ciclo |
| **R3** | > 10⁻⁵ | Blackout amplo de HF, perda de contato ~1 h. | 140 dias por ciclo |
| **R2** | > 10⁻⁶ | Blackout limitado de HF, perda de contato dezenas de minutos. | 300 dias por ciclo |
| **R1** | > 10⁻⁷ | Degradação leve de HF, perda ocasional de contato. | 950 dias por ciclo |

> **Obs.:** Centros de clima espacial designados pela ICAO devem fornecer alertas a aviões quando a intensidade de uma erupção solar exceder 10⁻⁴ W m⁻² (MOD) e 10⁻³ W m⁻² (SEV) (ICAO, 2019).

### Condutores
- **Atividade solar**: Erupções solares estão associadas a regiões ativas e manchas solares no Sol. Períodos de alta atividade, caracterizados por maior número de manchas solares, têm maior probabilidade de gerar erupções.

### Impactos
1. **Interrupções de comunicação por rádio**  
   Erupções solares emitem estalos intensos de radiação eletromagnética (raios‑X e EUV), aumentando a ionização na ionosfera inferior. Isso eleva a absorção e degradação de ondas de rádio HF (3‑30 MHz), prejudicando comunicações de longa distância essenciais para aviação, navegação marítima e serviços de emergência.

2. **Interferência em GNSS**  
   Estalos de rádio podem interferir diretamente nos sinais transmitidos por sistemas GNSS (GPS, GLONASS, BeiDou, Galileo), provocando imprecisões de posicionamento e sincronização, e potencial perda total de sinal.

3. **Interferência em radióstimas**  
   Estalos de rádio podem saturar sistemas de telefonia móvel, radares de monitoramento aéreo e outros transmissores/recebedores, como observado em 2015 em centros de controle de tráfego aéreo na Suécia.

4. **Danificação de satélites**  
   Radiações intensas podem danificar sistemas eletrônicos de satélites, interrompendo comunicações, monitoramento meteorológico e coleta de dados científicos. Partículas energéticas solares também representam risco à saúde de astronautas em atividades extraveiculares.

### Contexto Multi‑Risco
A figura abaixo resume as interações comuns entre erupções solares e outros riscos. A informação deve ser usada com cautela e não deve ser a única base para a Gestão de Risco em Desastres, pois algumas interações podem não ter sido incluídas. Eventos que ocorrem simultaneamente no espaço ou no tempo não necessariamente se amplificam ou se relacionam de forma direta.

*(Figura não incluída)*

### Gestão de Risco
- **Monitoramento do clima espacial**: Serviços de clima espacial monitoram a atividade solar e fornecem alertas e previsões de erupções solares potenciais.
- **Previsão de fadeout de rádio**: A intensidade de uma erupção pode ser medida por sensores de raios‑X e UV, permitindo prever o impacto na propagação de ondas de rádio.
- **Sistemas de comunicação de backup**: Empresas e indústrias podem implementar sistemas redundantes, alternando frequências, modos de comunicação ou redes menos afetadas por mudanças na ionosfera.
- **Monitoramento de integridade GNSS**: Usuários de GNSS podem usar sistemas de monitoramento de integridade para detectar anomalias ou interferências nos sinais.

### Monitoramento
Serviços de clima espacial, membros da International Space Environment Services (ISES), oferecem sistemas de alerta a usuários específicos em seus países. Centros de clima espacial designados pela ICAO aconselham companhias aéreas sobre erupções solares e fadeouts de rádio.

### Referências
- AMS, 2018. *Radio blackout*. American Meteorological Society (AMS). Acesso em 31 de janeiro de 2025.
- Australian Bureau of Meteorology, n.d. *Space Weather and the Aviation Sector*. Acesso em 31 de janeiro de 2025.
- Chakraborty, S., J. Ruohoniemi, J. B. H. Baker e N. Nishitani, “Characterization of short-wave fadeout seen in daytime SuperDARN ground scatter observations”, *Radio Science*, vol. 53, n.º 4, 2018.
- Hanslmeier, A., 2007. *Space Weather-An Overview*. Acesso em 24 fevereiro de 2025.
- International Civil Aviation Organization, 2019. *Manual on Space Weather Information in Support of International Air Navigation (Doc 10100)*. Relatório técnico; ICAO: Montreal, Canada.
- Kataoka, R., 2022. *Solar Radio Burst*. Capítulo 2 – Disturbed space weather. Extreme Space Weather, 31‑64. Acesso em 31 de janeiro de 2025.
- Machol, J. L., Eparvier, F. G., Viereck, R. A., Woodraska, D. L., Snow, M., Thiemann, E., … & Reinard, A. A., 2020. “GOES‑R series solar X‑ray and ultraviolet irradiance”. In *The GOES‑R Series* (pp. 233‑242). Elsevier.
- NOAA, 2019. *Solar flares (Radio blackouts)*. Centro de Previsão de Clima Espacial, NOAA. Acesso em 31 de janeiro de 2025.
- NOAA, n.d. *NOAA Space Weather Scales*. Centro de Previsão de Clima Espacial, NOAA. Acesso em 31 de janeiro de 2025.
- Royal Academy of Engineering, 2013. *Extreme Space Weather: Impacts on Engineered systems and Infrastructure*. Acesso em 31 de janeiro de 2025.
- Schumer, E. A., 2009. “Improved modeling of midlatitude D-region ionospheric absorption of high frequency radio signals during solar x‑ray flares”, vol. AFIT/DS/ENP/09/J01, Ohio: United States Air Force, Wright‑Patterson Air Force Base.
- Thiemann, E. M., Eparvier, F. G., Woodraska, D., Chamberlin, P. C., Machol, J., Eden, T., … & Woods, T. N., 2019. “The GOES‑R EUVS model for EUV irradiance variability”. *Journal of Space Weather and Space Climate*, 9, A43.
- UK CAA, 2020. *Impacts of space weather on aviation*. UK Civil Aviation Authority (UK CAA). Acesso em 31 de janeiro de 2025.
```

> *Este documento fornece uma tradução técnica e contextualizada das informações de risco associadas a erupções solares, adaptada ao padrão de vocabulário controlado de Redução de Risco de Desastres.*