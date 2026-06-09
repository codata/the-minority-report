### Definición
Un **ataque de cadena de suministro** ocurre cuando los productos, servicios o tecnologías que una organización recibe han sido comprometidos y, a su vez, se utilizan para infiltrarse y comprometer sus propios sistemas (ICO, sin fecha).

### Referencia principal(s)
ICO, sin fecha, **Ataques de cadena de suministro**. Accedido 25 de enero de 2025.

### Anotaciones
#### Descripción científica adicional
En **ciberseguridad**, los ataques de cadena de suministro implican la explotación de vulnerabilidades de seguridad dentro de la cadena de suministro de una organización para infiltrarse en sus sistemas y redes. Los atacantes apuntan a elementos menos seguros de la cadena de suministro—como **proveedores externos, proveedores** o **proveedores de servicios** (incluidos los **proveedores de servicios en la nube**)—con el objetivo de comprometer el objetivo final aprovechando la interconexión de los ecosistemas digitales modernos. Este método permite a los atacantes eludir las medidas de seguridad tradicionales al aprovechar las relaciones de confianza.

La historia de los ataques de cadena de suministro ha evolucionado junto con la creciente complejidad de las redes de suministro globales. Casos notables incluyen el ataque de 2011 a RSA Security, donde los atacantes comprometieron **tokens SecurID** a través de un proveedor para penetrar a **contratistas de defensa** (Greenberg, 2021). Más recientemente, el ataque SolarWinds 2020 demostró el impacto severo de tales brechas. En ese incidente, actores de amenaza sofisticados insertaron **código malicioso** en las **actualizaciones de software** de la compañía, afectando a numerosas **organizaciones gubernamentales y privadas** en todo el mundo y destacando las vulnerabilidades inherentes a las cadenas de suministro (Williams, 2020).

Varios **técnicas** se emplean en ataques de cadena de suministro:
- manipulación de **actualizaciones de software** (por ejemplo, el ataque SolarWinds),
- comprometer **repositorios de código**,
- infectar **componentes de hardware** durante la fabricación,
- explotar **vulnerabilidades** en servicios de terceros.

Los atacantes pueden insertar **código malicioso** en actualizaciones de software legítimas o aprovechar **puertas traseras** en dispositivos de hardware para obtener acceso no autorizado.

Muchas organizaciones dependen de **proveedores externos** para administrar sus entornos en la nube, lo que ha llevado a los atacantes a enfocarse en estos proveedores en una forma única de ataque de cadena de suministro: **ataques basados en la identidad de los proveedores de servicios**. Estos ataques explotan los amplios permisos que a menudo se otorgan a las **cuentas de proveedores de servicios**, que pueden tener acceso a múltiples entornos de clientes. Este acceso interconectado aumenta el potencial de impacto de una brecha, haciendo a los proveedores de servicios un objetivo atractivo (Microsoft, 2023).

Una de las más significativas fuentes de ataques de cadena de suministro proviene del **software de código abierto**. Las comunidades de código abierto ofrecen numerosos **módulos** y **paquetes** ampliamente utilizados por empresas en todo el mundo, incluidas aquellas en las cadenas de suministro. Sin embargo, debido a que el software de código abierto a menudo carece de propiedad clara y seguridad garantizada, suele introducir vulnerabilidades en las **arquitecturas de seguridad** (Forbes, 2022).

Otra técnica prominente en ataques de cadena de suministro incluye secuestrar actualizaciones y comprometer la **firma de código**. Los vendedores de software distribuyen rutinariamente actualizaciones desde servidores centralizados para mantener y mejorar sus productos. Los actores de amenaza pueden explotar este proceso infiltrándose en la red del proveedor para insertar malware en una actualización o modificarla para obtener control no autorizado sobre la funcionalidad del software. La firma de código, un mecanismo usado para verificar la **autenticidad e integridad** del software, es otro objetivo crítico. Los actores maliciosos socavan este proceso usando **certificados autofirmados**, explotando controles de acceso mal configurados o comprometiendo sistemas de firma. Al hacerse pasar por proveedores confiables y embeber código malicioso en actualizaciones, los atacantes pueden ejecutar con éxito ataques muy engañosos y dañinos (NIST, 2021).

En 2023, los atacantes comprometieron la aplicación de escritorio de **3CX** a través de instaladores infectados, propagando malware a través de un sistema de **voz sobre IP** (VoIP) ampliamente utilizado (Fortiguard, 2023).

Los actores maliciosos dependen cada vez más de ataques de cadena de suministro debido a su alto impacto y la dificultad de detección. La complejidad de las cadenas de suministro modernas y la dependencia de proveedores externos crean numerosas oportunidades de explotación, haciendo que los ataques de cadena de suministro sean una preocupación significativa en la **ciberseguridad**. Al mismo tiempo, estos ataques suelen ser dirigidos; por lo tanto, solo actores con mayores recursos y capacidades pueden (usualmente) ejecutarlos.

### Métricas y límites numéricos
No aplica.

### Convención clave relevante de la ONU / tratado multilateral
Los instrumentos legales internacionales que abordan los ataques de cadena de suministro se incluyen dentro de los marcos más amplios de ciberseguridad y ciberdelincuencia. La **Convención de la ONU de Budapest sobre Ciberdelincuencia** proporciona directrices para la cooperación internacional en la lucha contra la ciberdelincuencia, incluidos delitos que pueden involucrar ataques de cadena de suministro.

### Conductores
Estos ataques, que implican la explotación o alteración de software, hardware o aplicaciones de terceros, plantean un desafío significativo para las organizaciones.

### Impactos
- fraude  
- robo

### Contexto multi‑riesgo
No aplica.

### Gestión de riesgo
Defenderse contra ataques de cadena de suministro requiere un enfoque integral que incluya la **evaluación rigurosa de proveedores**, la implementación de **normas de seguridad estrictas**, el **monitoreo continuo** y la fomento de la **colaboración** entre organizaciones y sus socios. Dado que muchos ataques dependen de proveedores externos con dependencias complejas en sus herramientas y servicios, lograr una protección completa puede ser difícil. Sin embargo, las organizaciones pueden adoptar estrategias proactivas para defenderse contra los **vectores de amenaza** comunes (Cloudflare, sin fecha).

**Ejecutar una Evaluación de Riesgo de Terceros**: implica probar el software de terceros antes de la implementación, exigir a los proveedores que cumplan con políticas de seguridad específicas, implementar una **Política de Seguridad de Contenido (CSP)** para controlar los recursos ejecutables en el navegador y usar **Integridad de Recursos Secundarios (SRI)** para detectar contenido de JavaScript sospechoso.

**Implementar Confianza Cero**: garantiza que todos los usuarios—empleados, contratistas y proveedores—se verifiquen y monitoricen continuamente dentro de la red de la organización. Al verificar la identidad y los privilegios de usuarios y dispositivos, Confianza Cero impide que los atacantes exploten credenciales de usuario legítimas robadas para infiltrarse en la organización.

**DevSecOps**: La seguridad de la cadena de suministro aprovecha DevSecOps para defenderse contra ataques al descubrir primero todos los componentes, obtener visibilidad de la cadena de suministro y asegurar los **componentes de aplicaciones nativas en la nube**. Al integrar la seguridad a lo largo del proceso de desarrollo, DevSecOps garantiza la implementación en tiempo real de operaciones de seguridad mientras se alinea sin problemas con los objetivos comerciales (GitLab, sin fecha).

### Monitoreo
No aplica.

### Referencias
- Cloudflare, sin fecha. *¿Qué es un ataque de cadena de suministro?* Accedido 16 de enero de 2025.  
- Forbes, 2022. *Mitigar el riesgo de ataques de cadena de suministro en la era de la computación en la nube.* Accedido 15 de enero de 2025.  
- FortiGuard Labs, 2023. *Informe de señales de amenaza: Ataque de cadena de suministro a través de la aplicación de escritorio de 3CX.* Accedido 15 de enero de 2025.  
- GitLab, sin fecha. *¿Qué es DevSecOps?* Accedido 16 de enero de 2025.  
- Greenberg, A., 2021. *La historia completa del asombroso hack de RSA que finalmente se puede contar.* Accedido 15 de enero de 2025.  
- Información de la Oficina del Comisionado (ICO), sin fecha. *Ataques de cadena de suministro.* Accedido 15 de enero de 2025.  
- Microsoft, 2023. *Anunciando las capacidades de Microsoft Defender for Cloud para contrarrestar los ataques de cadena de suministro basados en identidad.* Comunidad técnica de Microsoft. Accedido 15 de enero de 2025.  
- Instituto Nacional de Estándares y Tecnología (NIST), 2021. *Defenderse contra ataques de cadena de suministro de software.* Accedido 16 de enero de 2025.  
- Williams, J., 2020. *Lo que necesita saber sobre el ataque de cadena de suministro de SolarWinds.* Instituto SANS.