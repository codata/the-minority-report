```markdown
### Definition
Hizmet reddi (DoS), yetkili erişimin engellenmesi veya zaman‑kritik işlemlerin geciktirilmesiyle karakterize edilen bir güvenlik durumudur. (Zaman‑kritik, milisaniye ile saat arasında değişebilir, sunulan hizmete bağlıdır) (NIST, 2017).

### Primary reference(s)
NIST, 2017. Bilgisayar Güvenliği. Bilgi Güvenliğine Giriş. Özel Yayın 800‑12 Revizyonu. Ulusal Standartlar ve Teknoloji Enstitüsü (NIST). 25 Ocak 2025 tarihinde erişildi.

### Annotations
#### Additional scientific description
Bir Hizmet Reddi (DoS) saldırısı, bir bilgisayar sistemini veya ağı, aşırı dış girdilerle (örneğin, gelen web trafiği) taşırarak hedef kullanıcılar için erişilemez hale getirir. Bu durumda, saldırı adı Dağıtılmış Hizmet Reddi (DDoS) olarak bilinir veya sistemdeki açıklar kullanılarak hesaplama kaynakları tükenir. Saldırı, kullanıcıların hizmetlere ve bilgilere erişimini engeller, bu da önemli operasyonel ve mali etkilere yol açar (CISA, 2021).

DDoS saldırıları, İnternet'te merkezi erişim kontrolü eksikliği nedeniyle sürekli bir rahatsızlık kaynağıdır. Bu zayıflık, erken dönem İnternet tasarımının temel bir kararıydı, bu yüzden DDoS saldırıları devam etmektedir. Erken saldırılar hacker kültürüyle ilgiliyken, odakları hızla ticari istismar yönüne kaydı. Ayrıca, cyberwar, hacktivizm ve terörizm gibi politik kullanım örnekleri de bulunmaktadır (Brooks ve diğ., 2021).

DoS ve DDoS kullanımı, siber güvenlik tarihine iyi bir şekilde belgelenmiştir. Erken saldırılar, 1995 yılında Fransa’da başlayan bir olay ve sonraki yıl New York merkezli internet servis sağlayıcısı Panix'e yönelik büyük bir olay ile erken internet döneminde zaten mevcuttu (Brooks ve diğ., 2021). Yıllar içinde bu saldırılar, 2016 Mirai kötü amaçlı yazılımıyla güçlendirilmiş bot ağı saldırısı gibi karmaşıklık ve ölçek bakımından evrimleşmiştir; bu saldırı, Nesnelerin İnterneti (IoT) cihazlarını kullanarak dünya çapında büyük bir DDoS saldırısı başlatmış ve önemli web sitelerini etkilemiştir (CISA, 2017).

DoS, insan hatalarından (örneğin, yanlış yapılandırma), diğer olaylardan (örneğin, güç kesintisi) veya kasıtlı saldırılardan kaynaklanabilir. DoS saldırılarında kullanılan çeşitli teknikler vardır. Temel fark, DoS ve DDoS saldırıları arasındadır. DoS saldırısı genellikle tek bir kaynaktan başlar ve bir sistemi hedef alırken, DDoS saldırısı, birçok ele geçirilmiş sistemi (genellikle bir bot ağı oluşturur) aynı anda hedefe doldurarak savunmayı çok daha zorlaştırır.

İnternet of Things (IoT) patlaması bağlamında özellikle bağlı cihaz sayısının artması, her bir bağlı cihazın potansiyel olarak bir bot ağı parçası olabileceği için DDoS riskini artırmaktadır.

Hizmet reddi koşulu, geçerli kullanıcıların, kötü niyetli bir siber tehdit aktörünün eylemleri nedeniyle bilgi sistemlerine, cihazlara veya diğer ağ kaynaklarına erişememesine yol açar. Bir Hizmet Reddi saldırısı, hedef host veya ağı aşırı trafikle doldurarak hedefin yanıt verememesine veya basitçe çökmesine yol açar, e-posta, web siteleri, çevrimiçi hesaplar (örneğin, bankacılık) veya diğer hizmetleri etkiler. DoS saldırıları, organizasyonun hem zaman hem de para kaybına yol açarken kaynaklarının ve hizmetlerinin erişilemez kalmasına neden olur.

DoS saldırıları, hacim‑tabanlı saldırılar (örneğin, bir web sitesini aşırı trafikle doldurarak) ve hesaplama sınırlamalarını hedefleyen saldırılar (bozuk istekler göndererek veya sonsuz döngü başlatarak) olarak iki kategoriye ayrılabilir.

DoS saldırıları, kritik altyapıyı hedef aldığında ulusal tehlikeye dönüşebilir. Örneğin, 2007 yılında Estonya'ya yönelik koordine edilmiş DDoS saldırıları, hükümet, bankacılık ve medya web sitelerini çökertmiş, yaygın bir aksaklık yaratmış ve ulusal düzeyde zayıflıkları vurgulamıştır (Ottis, 2008). DoS saldırıları, nispeten kolay yürütülmeleri ve önemli bir bozulma potansiyeli nedeniyle kötü niyetli aktörler tarafından yaygın olarak kullanılmaktadır. Her yıl, veri kayıtları, DoS ve DDoS olaylarının büyük sayıda gerçekleştiğini gösterir; bu nedenle, siber saldırıların en yaygın formlarından biridir (Bergamini de Neira ve diğ., 2023). 2024 yılında NETSCOUT, küresel olarak 13 milyondan fazla DDoS saldırısı rapor etmiş ve çok‑vektör saldırılar trendinin yükseldiğini bildirmiştir (NETSCOUT, 2024).

#### Drivers
DDoS’in artışının en kritik faktörlerinden biri, güvenli olmayan IoT cihazlarının yayılmasıdır. Modern ağlarda yaygın bağlantı ve yetersiz güvenlik protokolleri, saldırganların zayıflıkları istismar etmeleri ve başarılı DoS saldırıları başlatmaları için verimli bir zemin sunar.

#### Impacts
Hizmet reddi saldırısı, geçerli kullanıcıların bilgi sistemlerine, cihazlara veya diğer ağ kaynaklarına erişememesine yol açar. Etkilenen hizmetler, e-posta, web siteleri, çevrimiçi hesaplar (örneğin, bankacılık) veya ilgili bilgisayar veya ağlara dayanan diğer hizmetleri içerebilir (CISA, 2021). DDoS saldırıları, doğal afetler veya pandemiler sırasında sağlık veya finansal sistem arızalarını artırabilir (ENISA, 2023).

#### Multi‑hazard context
Mevcut değildir.

#### Risk Management
DoS riskini minimize etmek, teknolojik ve stratejik önlemlerin kombinasyonunu gerektirir. Sağlam ağ güvenliği protokolleri uygulamak, sızma tespit ve önleme sistemleri kullanmak ve yapay zeka destekli güvenlik çözümlerini benimsemek, bir organizasyonun dirençliliğini artırır. Ayrıca, hız sınırlama, trafik filtreleme ve içerik dağıtım ağları kullanma gibi stratejiler saldırıların etkisini azaltmaya yardımcı olur. Yapay zeka, siber tehditleri anında tespit edip yanıt vermek, kötü niyetli trafiği filtreleme yeteneğini artırmak, kaynakları dinamik olarak tahsis etmek ve desen ve davranışlara dayalı olarak potansiyel tehditleri öngörmek için kritik bir rol oynar. ITU, üye devletlerin siber güvenlik hazırlık, koruma ve olay müdahalesi kapasitelerini bölgesel ve uluslararası düzeyde “Siber Uygulamalar” düzenleyerek artırır (ITU, tarih yok). Siber Uygulama, yıllık bir etkinlik olup, siber saldırılar, bilgi güvenliği olayları veya diğer türdeki aksaklıklar simüle edilerek bir organizasyonun siber yetenekleri test edilir; bir güvenlik olayı tespit etmekten yanıt vermeye ve herhangi bir ilişkili etkiyi minimize etmeye kadar tüm adımlar değerlendirilir. Siber Uygulamaları sayesinde katılımcılar, politika, plan, prosedür, süreç ve yeteneklerin, hazırlık, önleme, yanıt, kurtarma ve operasyon sürekliliği süreçlerini destekleyip desteklemediğini doğrular.

#### Monitoring
Mevcut değildir.

### References
Bergamini de Neira, A., Kantarci, B. ve Nogueira, M., 2023. Dağıtılmış Hizmet Reddi Saldırı Tahmini: Zorluklar, Açık Sorunlar ve Fırsatlar. *Computer Networks*, 222(C), Şub. DOI: 10.1016/j.comnet.2022.109553 (3 Nisan 2025 tarihine erişildi).  
Brooks, R.R., Yu, L., Özceliği, I., Oakley, J. ve Tusing, N., 2022. Dağıtılmış Hizmet Reddi (DDoS): Bir Tarihçe. *IEEE Annals of the History of Computing*, 44, s.44–54 (3 Nisan 2025 tarihine erişildi).  
Cybersecurity and Infrastructure Security Agency (CISA), 2017. Mirai ve Diğer Bot Ağı Tarafından Artırılan DDoS Tehditleri. (3 Nisan 2025 tarihine erişildi).  
Cybersecurity and Infrastructure Security Agency (CISA), 2021. Hizmet Reddi Saldırılarını Anlamak. (3 Nisan 2025 tarihine erişildi).  
European Union Agency for Cybersecurity (ENISA), 2023. ENISA Tehdit Manzarası 2023. (3 Nisan 2025 tarihine erişildi).  
International Telecommunication Union (ITU), tarih yok. Siber Uygulamalar. (3 Nisan 2025 tarihine erişildi).  
NETSCOUT, 2024. Tehdit Zekası Raporu 2024. (3 Nisan 2025 tarihine erişildi).  
Ottis, R., 2008. 2007 Estonya Siber Saldırılarının Bilgi Savaşı Perspektifinden Analizi. *Proceedings of the 7th European Conference on Information Warfare and Security*, Plymouth, 2008. Reading: Academic Publishing Limited, s.163–168 (3 Nisan 2025 tarihine erişildi).  
National Institute of Standards and Technology (NIST), 2017. Bilgisayar Güvenliği: Bilgi Güvenliğine Giriş. Özel Yayın 800‑12 Revizyonu 1. Gaithersburg, MD: ABD Ticaret Bakanlığı (3 Nisan 2025 tarihine erişildi).
```