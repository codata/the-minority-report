### Definition  
Gelişmiş tehdit, bir saldırganın gelişmiş uzmanlık ve önemli kaynaklara sahip olması, birden fazla saldırı vektörünü (örneğin, siber, fiziksel ve yanıltma) kullanarak hedeflerine ulaşma fırsatları yaratmasıyla oluşur (NIST, 2012).

### Primary Reference(s)  
Ulusal Standartlar ve Teknoloji Enstitüsü (NIST), 2012. **Risk Değerlendirmesi Yapma Kılavuzu.** DOI:10.6028/NIST.SP.800-30r1. 25 Ocak 2025 tarihinde erişildi.

### Annotations  
#### Ek Bilimsel Açıklama  
**Gelişmiş Sürekli Tehdit (APT)**, siber güvenlikte uzun süreli ve hedeflenmiş bir siber saldırıyı ifade eder. Genellikle yetkisiz bir kullanıcı bir ağa giriş yapar ve uzun süre tespit edilmeden kalır. APT’nin ana hedefi genellikle ağ faaliyetlerini gözlemlemek, veriyi çalmak veya kesintiye uğratmaktır; anında hasar vermek yerine iz sürmeyi tercih eder. “Gelişmiş” terimi, açıkları kötüye kullanmak için kullanılan gelişmiş tekniklere, “sürekli” ise belirli bir hedefe ulaşmak için sürekli çaba gösterilmesine atıfta bulunur.

Birincil tanınan APT olaylarından biri 2003‑2006 yılları arasında gerçekleşen **Titan Rain** saldırılarıdır; burada saldırganlar ABD savunma ağlarını hedef alarak hassas bilgileri çaldı (Council of Foreign Relations 2005). **Stuxnet** solucanının 2010’da keşfi, APT’lerin İran’ın nükleer santrallerindeki manyetik merkezleri hedef alarak fiziksel zarar verme kapasitesini gösterdi (Zetter 2014). 2009’da gerçekleşen **Operation Aurora** saldırısı ise Google dahil olmak üzere birden fazla şirketi hedef alarak fikri mülkiyet ve e‑posta hesaplarına erişti (Council of Foreign Relations 2010). **SolarWinds** (2020) ve **Nobelium** kampanyaları (2022) gibi son olaylar, tedarik zinciri ve bulut altyapılarına yönelik gelişen APT tekniklerini örneklemektedir (Ghanbari et al., 2024).

APT’ler, hedeflerinin özelliklerine göre şekillenen çok yönlü teknikler kullanır. Saldırılar genellikle kılıç balıkçılığı, sıfır gün açıkları veya diğer gelişmiş tekniklerle başlar. İçeri girdikten sonra saldırganlar ya sessiz kalıp trafiği izler, veri toplar ya da yan hareket (lateral movement) yaparak ağı dolaşır, ayrıcalık yükseltme (privilege escalation) ile hassas bölgelere erişir. Süreklilik, arka kapılar ve rootkitler kurarak sürdürülür; bu sayede sürekli erişim ve veri sızdırma (data exfiltration) sağlanır.

Devlet aktörleri ve organize siber suç örgütleri, APT’leri uzun vadeli stratejik hedeflere ulaşmada etkili buldukları için sıklıkla kullanır. Büyük ölçekli ransomware gibi saldırılara göre daha az yaygın olsa da, APT’ler yüksek etki olaylarının önemli bir kısmını oluşturur. Karmaşıklıkları ve potansiyel zararları, casusluk, fikri mülkiyet hırsızlığı veya sabotaj için tercih edilen yöntemler haline getirir.

### Metrics and Numeric Limits  
Uygulanabilir.

### Key Relevant UN Convention / Multilateral Treaty  
Siber güvenlik ve siber suç çerçeveleri, **Budapeşte Sözleşmesi** gibi uluslararası hukuk araçlarıyla kapsanır. Budapeşte Sözleşmesi, uluslararası işbirliğini teşvik eder; siber suçları (APT’leri de içeren) önleme amacı taşır. Birleşmiş Milletler siber güvenlik kararları, kritik altyapıyı korumayı ve bilgi alışverişini teşvik etmeyi amaçlar, ancak yalnızca APT’lere odaklanan spesifik bir sözleşme bulunmaz. Devlet aktörlerinin APT’leri düzenlemesi, uluslararası kamu hukukunun kapsamına girer.

### Drivers  
Uygulanabilir.

### Impacts  
Uygulanabilir.

### Multi-hazard Context  
Uygulanabilir.

### Risk Management  
APT’e karşı savunma, saldırganın operasyonunu yürütmek için harcayacağı zaman, kaynak ve çaba miktarını göz önünde bulundurarak karmaşık bir iştir. APT’nin çeşitli yaklaşımları nedeniyle, tüm durumlara önceden belirlenmiş stratejiler uygulanması zorunlu değildir. APT’lerin karmaşık ve evrimsel doğası, tek bir çözümün tüm potansiyel tehditleri kapsayamaması nedeniyle uyarlanabilir bir savunma yaklaşımını gerektirir. Bu nedenle, organizasyonlar güçlü koruma sağlamak için birden fazla stratejiyi entegre etmelidir. Asharani ve arkadaşlarının (2019) çalışması, APT savunma stratejilerini **izleme, tespit ve hafifletme** olmak üzere üç ana gruba ayırır. Her biri yetkisiz erişim riskini azaltmada kritik bir rol oynar.

#### İzleme Metodolojileri  
Güvenlik duvarları ve antivirüs yazılımları gibi araçlar kullanılarak sistemin çeşitli bölümleri izlenir. Gelişmiş güvenlik duvarları, bilinen kötü amaçlı desenleri ve imzaları analiz edebilir, aynı zamanda davranışsal analizle anormal faaliyetleri tespit edebilir. CPU kullanımının izlenmesi, kaynak tüketimindeki anormalliklerin şüpheli davranışı işaret etmesi açısından önemlidir.

#### Tespit Metodolojileri  
Statik analiz, sinir ağları ve makine öğrenmesi yöntemleri (Hodge ve Austin 2004) gibi çeşitli anomali tespiti teknikleri kullanılır. Bu yöntemler, ortalama ila uzun vadede süreklilik gösteren APT’leri tanımlamaya yardımcı olur. Örneğin, **İzinsiz Giriş Tespit Sistemi (IDS)**, ağ trafiğini analiz ederek olağan dışı faaliyetleri tespit eder ve güvenlik ekibini potansiyel tehditlere uyarır.

#### Hafifletme Metodolojisi  
APT hafifletmesi, reaktif ve proaktif yaklaşımlar aracılığıyla gerçekleştirilebilir. Reaktif yöntemler, belirli bir anda olası saldırı yollarını ve açıkları tanımlamak, kritik alanları tahmin etmek ve şiddetini değerlendirmek içerir. Proaktif stratejiler ise saldırganları yanıltmayı hedefler. Bu teknikler, saldırganları yanıltarak saldırı stratejilerini değiştirmelerine ve tehdit etkisini azaltmalarına yol açar.

### Monitoring  
Uygulanabilir.

### References  
- Alshamrani, A., Myneni, S., Chowdhary, A. ve Huang, D., 2019. **Gelişmiş Sürekli Tehditler: Teknikler, Çözümler, Zorluklar ve Araştırma Fırsatları.** IEEE Communications Surveys & Tutorials, 21(2), 1851‑1877. 16 Ocak 2025 tarihinde erişildi.  
- Brandao, P.R. ve Limonova, V., 2021. **Gelişmiş Sürekli Tehditlere Karşı Savunma Metodolojileri (APTs).** American Journal of Applied Sciences, 2021. DOI:10.3844/ajassp.2021.207.212. 16 Ocak 2025 tarihinde erişildi.  
- Council on Foreign Relations (CFR), 2005. **Titan Rain.** 16 Ocak 2025 tarihinde erişildi.  
- Council on Foreign Relations (CFR), 2010. **Operation Aurora.** 16 Ocak 2025 tarihinde erişildi.  
- Ghanbari, H., Koskinen, K. ve Wei, Y., 2024. **SolarWinds'ten Kaseya'ya: Dijital Dünyada Tedarik Zinciri Saldırılarının Yükselişi.** Journal of Information Technology Teaching Cases, 0(0). DOI:10.1177/20438869241299823. 16 Ocak 2025 tarihinde erişildi.  
- Hodge, V.J. ve Austin, J., 2004. **Anomali Tespiti Metodolojilerinin Anketi.** Artificial Intelligence Review, 22, 85‑126. 16 Ocak 2025 tarihinde erişildi.  
- National Institute of Standards and Technology (NIST), 2012. **Özel Yayın 800-30 Revizyon 1: Risk Değerlendirmesi Yapma Kılavuzu.** Gaithersburg, MD: ABD Ticaret Bakanlığı. 16 Ocak 2025 tarihinde erişildi.  
- Zetter, K., 2014. **Stuxnet: Dünyanın İlk Dijital Silahına Berrak Bir Bakış.** WIRED Magazine. 16 Ocak 2025 tarihinde erişildi.  

---