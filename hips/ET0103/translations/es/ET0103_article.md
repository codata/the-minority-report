```markdown
### Definición
Una **flaque solar** es una explosión súbita y de gran magnitud en el Sol caracterizada por la liberación rápida de energía, que resulta en la emisión de radiación electromagnética a través de todas las longitudes de onda y en un aumento inmediato de brillo en una porción de la superficie solar. El estallido de energía electromagnética viaja a la velocidad de la luz; por lo tanto, cualquier efecto sobre el lado iluminado de la atmósfera externa de la Tierra ocurre al mismo tiempo que el evento es observado (NOAA Space Weather Prediction Center, 2023).

### Referencia primaria
NOAA Space Weather Prediction Center, 2023. **Flaques solares (caídas radio)**. Accedido el 31 de enero de 2025.

### Anotaciones
#### Descripción científica adicional
Las flaques solares ocurren predominantemente en **regiones activas** del Sol, caracterizadas por la presencia de campos magnéticos intensos, a menudo asociados con **manchas solares**. Cuando estos campos magnéticos cambian y evolucionan, pueden alcanzar un estado de inestabilidad, lo que resulta en la liberación de energía en diversas formas. Una de las manifestaciones primarias de esta liberación es observada como flaques solares, que implican la emisión de radiación electromagnética. Las flaques son más probables durante periodos de alta actividad solar y a menudo están acompañadas de **ejecciones de masa coronal (CME)**. Se clasifican según su intensidad, determinada principalmente por la luminosidad en rayos X y medida en la banda 1‑8 Å (0.1‑0.8 nm). Hay cinco categorías de flaques, que van desde la más débil a la más fuerte: A, B, C, M y X (Hanslmeier, 2007; Schrijver, 2009). La intensidad de las flaques se obtiene de sensores de rayos X y ultravioleta extremo (EUV) instalados en satélites GOES (Thiemann et al., 2019; Machol et al., 2020).  
Cuando la región activa correspondiente está orientada hacia la Tierra, una flaque intensa, típicamente de clase X y ocasionalmente M, puede provocar perturbaciones significativas en la ionosfera del lado iluminado de la Tierra. Estas perturbaciones pueden causar distorsiones de señal y desvanecimientos radio debido a la absorción aumentada de ondas de radio en la ionosfera baja, específicamente en la **zona D** y la zona **E** inferior.  
En condiciones regulares, las ondas de radio de alta frecuencia (HF) soportan la comunicación a larga distancia refractándose a través de las capas superiores de la ionosfera. Sin embargo, durante una flaque solar poderosa, la ionización aumenta en la ionosfera baja, particularmente en la zona D y la zona E inferiores. Este fenómeno puede llevar a la degradación o absorción completa de señales de radio HF, resultando en un desvanecimiento radio que afecta predominantemente la banda de frecuencia de 3 a 30 MHz.  
Los estallidos radio se asocian con las flaques solares. El retraso en el registro de sus diferentes frecuencias de radio en la órbita de la Tierra se debe al movimiento radial del origen. Los grandes estallidos duran de 10 a 20 minutos en promedio. Las tormentas de ruido radio de mayor duración, con niveles de radiación persistentes y variables, se originan en grupos de manchas solares, áreas de campos magnéticos grandes e intensos. Un **estallido radio solar (SRB)** puede influir en los señales de los Sistemas Globales de Navegación por Satélite (GNSS) a través de interferencias directas de ondas de radio.

### Métricas y límites numéricos
Las intensidades de las flaques solares abarcan un rango amplio y se clasifican según la emisión pico en la banda 0.1‑0.8 nm de rayos X (soft X‑ray) del XRS de NOAA/GOES. Las flaques se clasifican mediante una escala de cinco niveles introducida por la Administración Nacional Oceánica y Atmosférica de EE. UU. (NOAA) en 1999. La escala está en revisión y se presenta a continuación. Los niveles de flujo de rayos X comienzan con el nivel **A** (≥ 10⁻⁸ W m⁻²). El siguiente nivel, diez veces mayor, es el nivel **B** (≥ 10⁻⁷ W m⁻²), seguido por las flaques **C** (≥ 10⁻⁶ W m⁻²), **M** (≥ 10⁻⁵ W m⁻²) y finalmente las flaques **X** (≥ 10⁻⁴ W m⁻²) (NOAA, 2023).

#### Escala de Impacto
| Nivel | Descripción física | Frecuencia media | Frecuencia por ciclo | Impacto en HF | Impacto en navegación |
|-------|---------------------|------------------|----------------------|---------------|-----------------------|
| R 5 | **Extremo** – Ceguera radio completa (HF) en todo el lado iluminado de la Tierra durante varias horas. | 1 ciclo = 11 años | < 1 por ciclo | Contacto HF perdido | Señales de navegación de baja frecuencia interrumpidas; errores de posicionamiento en horas prolongadas. |
| R 4 | **Severo** – Ceguera radio HF en la mayor parte del lado iluminado de la Tierra durante 1‑2 h. | 10⁻³ W m⁻² (X10) | 8 por ciclo (≈ 8 días/ciclo) | Contacto HF perdido | Ocurren fallos de señal de navegación de baja frecuencia; posibles breves interferencias en GNSS. |
| R 3 | **Fuerte** – Ceguera radio HF a gran escala, pérdida de contacto de ~1 h. | 10⁻⁴ W m⁻² (X1) | 175 por ciclo (≈ 140 días/ciclo) | Contacto HF degradado | Señales de navegación de baja frecuencia afectadas por ~1 h. |
| R 2 | **Moderado** – Ceguera HF limitada, pérdida de contacto de minutos. | 5 × 10⁻⁵ W m⁻² (M5) | 350 por ciclo (≈ 300 días/ciclo) | Contacto HF parcialmente perdido | Señales de navegación de baja frecuencia degradadas por minutos. |
| R 1 | **Menor** – Degradación ligera de HF, pérdida ocasional. | 10⁻⁵ W m⁻² (M1) | 2000 por ciclo (≈ 950 días/ciclo) | Contacto HF ligeramente degradado | Señales de navegación de baja frecuencia afectadas brevemente. |

Los centros de clima espacial designados por la Organización de Aviación Civil Internacional (OACI) deben proporcionar a las aerolíneas avisos sobre condiciones anómalas de comunicación HF cuando la intensidad de una flaque solar exceda 10⁻⁴ W m⁻² (MOD) y 10⁻³ W m⁻² (SEV) (OACI, 2019).

### Convención/memorial de la ONU relevante
No aplica; sin embargo, las normas relacionadas con la aviación caen bajo la coordinación de la OACI.

### Conductores
- **Actividad solar**: las flaques solares están asociadas con regiones activas y manchas solares. Se activan por eventos de reconexión magnética en la corona solar. Los periodos de alta actividad, con mayor número de manchas solares, generan mayor probabilidad de flaques.

### Impactos
- **Disrupciones en comunicación radio**: las flaques emiten estallidos intensos de rayos X y EUV, incrementando la ionización en la ionosfera baja y provocando absorción y degradación de ondas de radio HF (3‑30 MHz), afectando la aviación, la navegación marítima y los servicios de emergencia.
- **Interferencia en GNSS**: las flaques generan interferencia de radiofrecuencia que afecta los sistemas GNSS (GPS, GLONASS, BEIDOU, GALILEO), provocando inexactitud de posicionamiento y pérdida de señal.
- **Interferencia de estallidos radio**: los estallidos pueden saturar sistemas terrestres (telefonía móvil, radares de aviación, transmisores/receivers) y provocar interrupciones de 90 min en el espacio aéreo sueco en 2015.
- **Daño a satélites**: las partículas energéticas solares pueden dañar los sistemas electrónicos de satélites, interrumpir comunicaciones, monitorización meteorológica y recopilación de datos científicos. También representan riesgo para astronautas durante EVAs.

### Contexto multi‑hazard
La figura siguiente resume las interacciones comunes entre flaques solares y otros peligros. Este dato debe usarse con cautela y no debe ser la única base para la gestión del riesgo en desastres, ya que algunas interacciones pueden no incluirse.

### Gestión del riesgo
- **Monitoreo de clima espacial**: los servicios de clima espacial monitorizan la actividad solar y brindan alertas y pronósticos de posibles flaques solares.  
- **Predicciones de desvanecimiento radio**: la intensidad de una flaque puede medirse con sensores de rayos X y UV, permitiendo predecir el impacto potencial en la propagación de ondas de radio.  
- **Sistemas de comunicación de respaldo**: se pueden emplear frecuencias alternativas, modos de comunicación o redes redundantes menos afectadas por cambios ionosféricos.  
- **Monitoreo de integridad GNSS**: los usuarios pueden instalar sistemas que detecten anomalías en las señales GNSS y alerten a los operadores.

### Monitoreo
Los servicios de clima espacial miembros de los **International Space Environment Services (ISES)** ofrecen sistemas de alerta a usuarios específicos en sus países. Los centros de clima espacial designados por la OACI aconsejan a las aerolíneas sobre flaques solares y desvanecimientos radio.

### Referencias
*(La lista completa de referencias se mantiene igual, con el formato adecuado en el documento original.)*
```