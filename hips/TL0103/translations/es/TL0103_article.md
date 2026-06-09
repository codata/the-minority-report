### Definición  
Una amenaza avanzada es creada por un atacante con niveles de especialización avanzados y recursos significativos, permitiéndole, mediante el uso de múltiples vectores de ataque (por ejemplo, cibernético, físico y engaño), generar oportunidades para lograr sus objetivos (NIST, 2012).

### Referencia primaria  
Instituto Nacional de Estándares y Tecnología, 2012. Guía para la realización de evaluaciones de riesgo. DOI:10.6028/NIST.SP.800-30r1. Accedido 25 de enero de 2025.

### Anotaciones  
#### Descripción científica adicional  
Una **Amenaza Persistente Avanzada (APT)** en ciberseguridad se refiere a un ataque cibernético prolongado y dirigido donde, a menudo, un usuario no autorizado accede a una red y permanece sin ser detectado durante un período extendido. El objetivo principal de las APT es observar la actividad de la red, robar datos o provocar interrupciones, en lugar de causar daños inmediatos. Esta amenaza se considera “avanzada” debido a las técnicas sofisticadas empleadas para explotar vulnerabilidades, y “persistente” por el esfuerzo continuo de alcanzar un objetivo específico.

Uno de los incidentes APT más tempranos reconocidos fue el ataque Titan Rain entre 2003 y 2006, donde los atacantes infiltraron redes de defensa estadounidenses para robar información sensible (Council of Foreign Relations, 2005). El descubrimiento del gusano Stuxnet en 2010 marcó una escalada significativa, demostrando la capacidad de las APT de causar daño físico al atacar los centrifugadores nucleares de Irán (Zetter, 2014). Otro ejemplo notable es el ataque Operation Aurora en 2009, que atacó a múltiples empresas, incluidas Google, para acceder a propiedad intelectual y cuentas de correo electrónico de activistas (Council of Foreign Relations, 2010). Incidentes recientes, como SolarWinds (2020) y las campañas de Nobelium (2022), ejemplifican técnicas APT en evolución que atacan cadenas de suministro e infraestructura en la nube (Ghanbari et al., 2024).

Las APT emplean una variedad multifacética de técnicas para lograr sus objetivos. Estos ataques se diseñan según las características de sus objetivos y, por tanto, pueden adoptar muchas formas. Frecuentemente, comienzan con una intrusión en el objetivo del sistema mediante spear-phishing, vulnerabilidades de día cero (fallas de seguridad desconocidas) u otras técnicas avanzadas para infiltrarse en sistemas sin ser detectados. Una vez dentro, los atacantes pueden permanecer en silencio, monitorear el tráfico y recopilar información, o pueden usar movimiento lateral para navegar la red, empleando escalada de privilegios para acceder a áreas sensibles. La persistencia se mantiene desplegando backdoors y rootkits, habilitando acceso continuo y exfiltración de datos sin desencadenar alarmas de seguridad.

Los actores maliciosos, particularmente grupos estatales y cibercriminales organizados, dependen con frecuencia de las APT por su efectividad en lograr metas estratégicas a largo plazo. Aunque son menos comunes que los ataques masivos como ransomware, las APT representan una proporción significativa de incidentes cibernéticos de alto impacto. Su complejidad y potencial de daño sustancial las convierten en métodos preferidos para espionaje, robo de propiedad intelectual o sabotaje.

### Métricas y límites numéricos  
No aplicable.

### Convención / tratado multilateral relevante de la ONU  
Los instrumentos legales internacionales que abordan las APT están incluidos dentro de los marcos más amplios de ciberseguridad y ciberdelincuencia. La Convención de Budapest de la Unión Europea sobre Ciberdelincuencia proporciona una base para la cooperación internacional en la lucha contra delitos cibernéticos, incluidos los que involucran APT. Las resoluciones de la ONU sobre ciberseguridad animan a los Estados miembros a adoptar medidas para proteger la infraestructura crítica y promover el intercambio de información para prevenir amenazas cibernéticas. Sin embargo, la ausencia de tratados específicos centrados exclusivamente en las APT destaca los desafíos para abordar amenazas tan sofisticadas y en evolución a nivel mundial. Dado que las APT son a menudo llevadas a cabo por actores estatales, su regulación recaería bajo el ámbito del Derecho Público Internacional.

### Conductores  
No aplicable.

### Impactos  
No aplicable.

### Contexto multi‑riesgo  
No aplicable.

### Gestión del riesgo  
Defenderse contra una APT es una tarea compleja, considerando la cantidad de tiempo, recursos y esfuerzo que el atacante está dispuesto a invertir para cumplir su operación. Además, dado el enfoque diverso que puede adoptar una APT, es difícil prescribir estrategias a priori para minimizar el riesgo, aplicables a todos los casos. La naturaleza compleja y evolutiva de las APT requiere un enfoque de defensa a medida y adaptable, ya que ninguna solución única puede abordar todas las amenazas potenciales. En su lugar, las organizaciones deben integrar múltiples estrategias para garantizar una protección robusta. Según Asharani et al. (2019), las estrategias de defensa contra Amenazas Persistentes Avanzadas (APT) se clasifican en tres grupos principales: monitorización, detección y mitigación. Cada una juega un papel crítico en minimizar el riesgo de acceso no autorizado.

#### Metodologías de monitorización  
Estas implican el uso de herramientas como cortafuegos y software antivirus para observar diversas partes del sistema. Los cortafuegos avanzados son capaces de analizar el tráfico en busca de patrones y firmas maliciosas conocidas, así como emplear análisis de comportamiento para detectar actividad anómala. Además, la monitorización del uso de CPU es importante, ya que patrones inusuales en la utilización de recursos pueden indicar comportamiento sospechoso.

#### Metodologías de detección  
Estas incluyen el uso de varios métodos de detección de anomalías, como análisis estático, redes neuronales y enfoques de aprendizaje automático (Hodge y Austin et al., 2004). Estas técnicas ayudan a identificar APT que persisten a lo largo del medio a largo plazo. Por ejemplo, un Sistema de Detección de Intrusiones (IDS) puede analizar el tráfico de red para detectar actividad inusual y alertar a los equipos de seguridad sobre posibles amenazas.

#### Metodología de mitigación  
La mitigación de APT se puede lograr mediante enfoques reactivos y proactivos. Los métodos reactivos implican identificar posibles caminos de ataque y vulnerabilidades en un momento dado, predecir áreas críticas y evaluar su severidad. Las estrategias proactivas, por otro lado, se centran en engañar a los atacantes. Estas técnicas buscan confundir a los intrusos y hacer que alteren sus estrategias de ataque, reduciendo así el impacto de la amenaza.

### Monitorización  
No aplicable.

### Referencias  
Alshamrani, A., Myneni, S., Chowdhary, A. y Huang, D. (2019). Una encuesta sobre amenazas persistentes avanzadas: técnicas, soluciones, desafíos y oportunidades de investigación. *IEEE Communications Surveys & Tutorials*, 21(2), 1851‑1877. doi:10.1109/COMST.2019.2891891. Accedido 16 enero 2025.  

Brandão, P. R. y Limonova, V. (2021). Metodologías de defensa para amenazas persistentes avanzadas (APT). *American Journal of Applied Sciences*, 2021. doi:10.3844/ajassp.2021.207.212. Accedido 16 enero 2025.  

Council on Foreign Relations (CFR). (2005). Titan Rain. Accedido 16 enero 2025.  

Council on Foreign Relations (CFR). (2010). Operation Aurora. Accedido 16 enero 2025.  

Ghanbari, H., Koskinen, K. y Wei, Y. (2024). De SolarWinds a Kaseya: el auge de los ataques de cadena de suministro en un mundo digital. *Journal of Information Technology Teaching Cases*, 0(0). doi:10.1177/20438869241299823. Accedido 16 enero 2025.  

Hodge, V. J. y Austin, J. (2004). Una encuesta de metodologías de detección de valores atípicos. *Artificial Intelligence Review*, 22, 85‑126. Accedido 16 enero 2025.  

National Institute of Standards and Technology (NIST). (2012). *Special Publication 800‑30 Revision 1: Guía para la realización de evaluaciones de riesgo*. Gaithersburg, MD: U.S. Department of Commerce. Accedido 16 enero 2025.  

Zetter, K. (2014). Una mirada sin precedentes a Stuxnet, el primer arma digital del mundo. *WIRED Magazine*. Accedido 16 enero 2025.  

---