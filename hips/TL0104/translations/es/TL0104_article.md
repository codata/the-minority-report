### Definición

La denegación de servicio es la prevención del acceso no autorizado a recursos o el retraso de operaciones críticas en el tiempo. (El tiempo crítico puede ser milisegundos o puede ser horas, dependiendo del servicio proporcionado) (NIST, 2017).

### Referencia principal(s)

- NIST, 2017. **Seguridad informática. Una introducción a la seguridad de la información.** Publicación Especial 800‑12 Revision. National Institute of Standards and Technology (NIST). Accedido 25 enero 2025.

### Anotaciones

#### Descripción científica adicional

Una **denegación de servicio (DoS)** hace que un sistema informático o red esté indisponible para sus usuarios previstos mediante la sobrecarga con entradas externas (por ejemplo, tráfico web entrante). En estos casos, el ataque lleva el nombre de **denegación de servicio distribuida (DDoS)** o se explotan sus vulnerabilidades para agotar los recursos computacionales. Esta interrupción niega a los usuarios acceso a servicios e información, provocando impactos operativos y financieros significativos (CISA, 2021).

Las **denegaciones de servicio distribuidas (DDoS)** siguen siendo una molestia persistente en Internet. Explotan la falta de control de acceso centralizado que tenía la red. Como esta vulnerabilidad fue una decisión de diseño central en el Internet primitivo, los ataques DDoS han persistido. Los primeros ataques estaban vinculados a la cultura hacker, pero su foco cambió rápidamente a la explotación comercial. También ha habido varios usos políticos de los DDoS, incluyendo ciber‑guerra, hacktivismo y terrorismo (Brooks et al., 2021).

El uso de DoS y DDoS está bien documentado en la historia de la ciberseguridad. Los primeros ataques ya existían en la era temprana de Internet; uno de los primeros incidentes ocurrió en Francia en 1995, seguido al año siguiente por un incidente importante contra Panix, un proveedor de servicios de Internet con sede en Nueva York (Brooks et al., 2021). Con el paso de los años, estos ataques han evolucionado en complejidad y escala, ejemplificados por el ataque botnet de 2016 impulsado por el malware Mirai, que utilizó dispositivos del **Internet de las cosas (IoT)** para lanzar un ataque DDoS masivo, interrumpiendo sitios web importantes en todo el mundo (CISA, 2017).

DoS puede surgir de errores humanos (por ejemplo, configuración incorrecta), otros incidentes (por ejemplo, fallo de energía) o ataques deliberados. Se emplean varias técnicas en los ataques DoS. La distinción principal es entre ataques DoS y DDoS. Un ataque DoS suele originarse en una única fuente que apunta a un sistema, mientras que un ataque DDoS involucra múltiples sistemas comprometidos, a menudo formando un botnet, para inundar el objetivo simultáneamente, lo que dificulta la defensa de manera significativa. El creciente número de dispositivos conectados—especialmente en el contexto del auge del **Internet de las cosas (IoT)**—también aumenta el riesgo de que los DDoS ocurran, ya que cada dispositivo conectado puede potencialmente convertirse en parte de un botnet.

Una **denegación de servicio (DoS)** ocurre cuando usuarios legítimos no pueden acceder a sistemas de información, dispositivos u otros recursos de red debido a las acciones de un actor de amenazas cibernéticas. Una condición de denegación de servicio inunda el host o la red objetivo con tráfico hasta que el objetivo no puede responder o simplemente falla, afectando correo electrónico, sitios web, cuentas en línea (por ejemplo, banca) u otros servicios. Los ataques DoS pueden costar a una organización tanto tiempo como dinero mientras sus recursos y servicios son inaccesibles.

Los ataques DoS pueden clasificarse según el método: ataques basados en volumen abruman el ancho de banda de una red (por ejemplo, inundar un sitio web con tráfico excesivo), mientras que los ataques que explotan limitaciones computacionales envían solicitudes malformadas o inician bucles infinitos para agotar recursos computacionales. Los ataques DoS pueden escalar a riesgos nacionales cuando atacan infraestructuras críticas. Un precedente es los ciberataques de 2007 en Estonia, donde ataques DDoS coordinados paralizaron sitios web gubernamentales, bancarios y de medios, provocando una disrupción generalizada y destacando vulnerabilidades a nivel nacional (Ottis, 2008).

Los ataques DoS son comúnmente empleados por actores maliciosos debido a su relativa facilidad de ejecución y potencial de disrupción significativa. Cada año, los registros de datos registran grandes números de incidentes DoS y DDoS, convirtiéndolos en una de las formas de ciberataque más prevalentes (Bergamini de Neira et al., 2023). En 2024, NETSCOUT informó más de 13 millones de ataques DDoS a nivel mundial, con tendencias crecientes en ataques multi‑vector (NETSCOUT, 2024).

### Drivers

Uno de los factores más críticos que lleva al aumento de los DDoS es la proliferación de dispositivos IoT no seguros. La extensa conectividad y los protocolos de seguridad insuficientes en redes modernas proporcionan un terreno fértil para que los atacantes exploten vulnerabilidades y lancen ataques DoS exitosos.

### Impacts

Una **denegación de servicio (DoS)** ocurre cuando usuarios legítimos no pueden acceder a sistemas de información, dispositivos u otros recursos de red debido a las acciones de un actor de amenazas cibernéticas. Los servicios afectados pueden incluir correo electrónico, sitios web, cuentas en línea (por ejemplo, banca) u otros servicios que dependen de la computadora o red afectada (CISA, 2021). Los ataques DDoS pueden agravar fallos en el sistema sanitario o financiero durante desastres naturales o pandemias (ENISA, 2023).

### Contexto multi‑riesgo

No disponible.

### Gestión del riesgo

La minimización del riesgo de DoS implica una combinación de medidas tecnológicas y estratégicas. La implementación de protocolos robustos de seguridad de red, el uso de sistemas de detección y prevención de intrusiones y la adopción de soluciones de seguridad impulsadas por IA mejora la resiliencia de la organización. Además, estrategias como la limitación de tasa, el filtrado de tráfico y el uso de redes de distribución de contenido ayudan a mitigar el impacto de los ataques. La inteligencia artificial también puede desempeñar un papel crítico en la protección contra DoS. Los sistemas de IA pueden analizar el tráfico de red para identificar anomalías, permitiendo la detección y respuesta en tiempo real, mejorando la capacidad de filtrar tráfico malicioso, asignar recursos dinámicamente y predecir amenazas potenciales basadas en patrones y comportamientos.

La **ITU** mejora la preparación, protección y capacidad de respuesta ante incidentes de ciberseguridad de los Estados Miembros mediante la realización de **CyberDrills** a nivel regional e internacional (ITU, s.f.). Un **CyberDrill** es un evento anual durante el cual se simulan ciberataques, incidentes de seguridad de la información u otros tipos de disrupción para probar las capacidades de ciberseguridad de una organización, desde la detección de incidentes de seguridad hasta la respuesta adecuada y la minimización de cualquier impacto relacionado. A través de **CyberDrills**, los participantes pueden validar políticas, planes, procedimientos, procesos y capacidades que permitan la preparación, prevención, respuesta, recuperación y continuidad de las operaciones.

### Monitoreo

No disponible.

### Referencias

- Bergamini de Neira, A., Kantarci, B. y Nogueira, M., 2023. Predicción de ataques de denegación de servicio distribuida: desafíos, problemas abiertos y oportunidades. *Computer Networks*, 222(C), Feb. DOI: 10.1016/j.comnet.2022.109553. Accedido 3 abril 2025.
- Brooks, R.R., Yu, L., Ozcelik, I., Oakley, J. y Tusing, N., 2022. Denegación de servicio distribuida (DDoS): Una historia. *IEEE Annals of the History of Computing*, 44, pp.44–54. Accedido 3 abril 2025.
- Cybersecurity and Infrastructure Security Agency (CISA), 2017. Amenaza aumentada de DDoS planteada por Mirai y otros botnets. Accedido 3 abril 2025.
- Cybersecurity and Infrastructure Security Agency (CISA), 2021. Entendiendo los ataques de denegación de servicio. Accedido 3 abril 2025.
- European Union Agency for Cybersecurity (ENISA), 2023. Panorama de amenazas ENISA 2023. Accedido 3 abril 2025.
- International Telecommunication Union (ITU), s.f. CyberDrills. Accedido 3 abril 2025.
- NETSCOUT, 2024. Informe de inteligencia de amenazas 2024. Accedido 3 abril 2025.
- Ottis, R., 2008. Análisis de los ciberataques de 2007 contra Estonia desde la perspectiva de la guerra de información. En: Proceedings of the 7th European Conference on Information Warfare and Security, Plymouth, 2008. Reading: Academic Publishing Limited, pp.163–168. Accedido 3 abr. 2025.
- National Institute of Standards and Technology (NIST), 2017. *Seguridad informática: Una introducción a la seguridad de la información*. Publicación Especial 800‑12 Revisión 1. Gaithersburg, MD: Departamento de Comercio de EE. UU. Accedido 3 abr. 2025.