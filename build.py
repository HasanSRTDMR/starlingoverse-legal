# Yasal sayfaları üretir: python3 build.py   (çıktı: bu klasördeki .html dosyaları)
DEV = "[GELİŞTİRİCİ ADI]"
MAIL = "[İLETİŞİM E-POSTASI]"
DATE_TR, DATE_EN = "20 Kasım 2026", "November 20, 2026"
APP = "Starlingoverse"

CSS = """:root{color-scheme:dark}*{box-sizing:border-box}
body{margin:0;font:16px/1.65 system-ui,-apple-system,'Segoe UI',Roboto,sans-serif;color:#EFF6FF;background:linear-gradient(180deg,#060F36,#0B1F63 55%,#1B2AA0) fixed;min-height:100vh}
main{max-width:780px;margin:0 auto;padding:32px 20px 80px}
h1{font-size:2rem;line-height:1.2;margin:.2em 0 .1em;background:linear-gradient(90deg,#58F0BE,#38D6E6,#8A9BFF);-webkit-background-clip:text;background-clip:text;color:transparent}
h2{font-size:1.2rem;margin:1.8em 0 .4em;color:#58F0BE}
p,li{color:#DCE6FF}a{color:#8FD8FF}
.meta{color:#9fb3e8;font-size:.9rem}
nav{display:flex;gap:14px;flex-wrap:wrap;margin:0 0 18px;font-size:.95rem}
.card{background:rgba(255,255,255,.07);border:1px solid rgba(255,255,255,.14);border-radius:18px;padding:16px 18px;margin:14px 0}
footer{margin-top:48px;color:#9fb3e8;font-size:.85rem}
.btns{display:grid;gap:12px;margin-top:22px}.btns a{display:block;padding:16px 18px;border-radius:16px;background:rgba(255,255,255,.08);border:1px solid rgba(255,255,255,.18);text-decoration:none;font-weight:600}"""

def page(lang, fname, title, body, other):
    nav_tr = f'<a href="index.html">Ana sayfa</a><a href="gizlilik.html">Gizlilik Politikası</a><a href="kosullar.html">Kullanım Koşulları</a><a href="{other[0]}">English</a>'
    nav_en = f'<a href="index.html">Home</a><a href="privacy.html">Privacy Policy</a><a href="terms.html">Terms of Use</a><a href="{other[0]}">Türkçe</a>'
    nav = nav_tr if lang == 'tr' else nav_en
    return f'<!doctype html><html lang="{lang}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{title} – {APP}</title><meta name="robots" content="index,follow"><style>{CSS}</style></head><body><main><nav>{nav}</nav><h1>{title}</h1>{body}<footer>© 2026 {DEV} · {APP}</footer></main></body></html>'

PRIV_TR = f"""<p class="meta">Yürürlük tarihi: {DATE_TR} · Uygulama: {APP} (Android)</p>
<div class="card"><b>Kısaca:</b> {APP} için hesap açmazsın. Öğrenme verilerin yalnızca kendi cihazında durur, bizim sunucularımıza gönderilmez. Ücretsiz sürümde Google AdMob reklamları gösterilir; reklam sistemi Google tarafından işletilir. Ödemeler Google Play üzerinden yapılır.</div>
<h2>1. Veri sorumlusu</h2><p>{DEV} ("biz"). İletişim: <a href="mailto:{MAIL}">{MAIL}</a></p>
<h2>2. Hesap ve kişisel bilgiler</h2><p>Uygulamayı kullanmak için ad, e-posta, telefon veya benzeri hiçbir kişisel bilgi vermen gerekmez. Biz bu tür bilgileri toplamayız ve sunucularımızda kullanıcı verisi tutmayız.</p>
<h2>3. Cihazında saklanan veriler</h2><p>Uygulama; seçtiğin hedefleri ve günlük çalışma süresini, ders ve alıştırma geçmişini (doğru/yanlış cevaplar, ipuçları, tekrar zamanlaması), XP, seri ve rozet bilgilerini ve abonelik durumunu <b>yalnızca cihazında</b> saklar. Bu veriler bize iletilmez. Uygulama içindeki <i>Profil → Ayarlar ve veri → Tüm verimi sil</i> seçeneğiyle öğrenme verini silebilir, uygulamayı kaldırarak tüm yerel verileri temizleyebilirsin.</p>
<h2>4. Reklamlar (Google AdMob)</h2><p>Ücretsiz kullanımda banner, geçiş ve ödüllü reklamlar gösterilir. Reklamları <b>Google AdMob</b> sunar. Reklam gösterimi, ölçümü ve sahtekârlık önleme için Google; reklam kimliğini (Android Advertising ID), IP adresini, cihaz ve uygulama bilgilerini ve reklamlarla etkileşimini işleyebilir. Bu işleme Google'ın sorumluluğundadır; ayrıntılar: <a href="https://policies.google.com/technologies/ads">policies.google.com/technologies/ads</a> ve <a href="https://support.google.com/admob/answer/6128543">AdMob veri kullanımı</a>.</p>
<p>Avrupa Ekonomik Alanı, Birleşik Krallık ve ilgili bölgelerde, uygulama ilk açılışta Google'ın onay (UMP) formunu gösterir; reklam tercihini orada seçebilir ve dilediğin zaman değiştirebilirsin. Kişiselleştirilmiş reklamları Android <i>Ayarlar → Google → Reklamlar</i> bölümünden kapatabilir veya reklam kimliğini sıfırlayabilirsin.</p>
<h2>5. Abonelik ve ödemeler (Google Play)</h2><p>Premium abonelik satın alma, yenileme ve iptal işlemleri <b>Google Play</b> tarafından yürütülür. Kart veya ödeme bilgilerini görmeyiz ve saklamayız. Uygulama yalnızca aboneliğinin aktif olup olmadığını Google Play'den öğrenir ve bunu cihazında tutar.</p>
<h2>6. Üçüncü taraf hizmetler</h2><ul><li>Google AdMob (reklamlar) – Google LLC</li><li>Google Play Billing (abonelik ödemeleri) – Google LLC</li></ul><p>Başka bir analiz, izleme veya hata raporlama hizmeti kullanmıyoruz.</p>
<h2>7. Çocuklar</h2><p>{APP} 13 yaşın altındaki çocuklara yönelik değildir ve bilerek çocuklardan veri toplamayız. Bir çocuğun uygulamayı kullandığını fark edersen bize yaz.</p>
<h2>8. Saklama süresi ve güvenlik</h2><p>Öğrenme verilerin, sen silene veya uygulamayı kaldırana kadar cihazında kalır. Verilerimizi sunucuda tutmadığımız için aktarım veya sunucu kaynaklı ihlal riski yoktur; cihazının ekran kilidi ve güncellemelerini kullanmanı öneririz.</p>
<h2>9. Haklarınız (KVKK ve GDPR)</h2><p>Kişisel verilerinin işlenip işlenmediğini öğrenme, bilgi talep etme, düzeltme, silme ve itiraz etme haklarına sahipsin (6698 sayılı KVKK md. 11; AEA/BK'de GDPR). Biz kişisel veri toplamadığımız için çoğu hak, cihazındaki verileri silerek kullanılır. Google'ın işlediği reklam verileriyle ilgili talepler için Google'a başvurabilirsin. Diğer talepler için: <a href="mailto:{MAIL}">{MAIL}</a>. Türkiye'de ayrıca Kişisel Verileri Koruma Kurumu'na şikâyet hakkın saklıdır.</p>
<h2>10. Değişiklikler</h2><p>Bu politikayı güncelleyebiliriz. Önemli değişiklikleri bu sayfada ve yürürlük tarihinde göstereriz.</p>
<h2>11. İletişim</h2><p><a href="mailto:{MAIL}">{MAIL}</a></p>"""

PRIV_EN = f"""<p class="meta">Effective date: {DATE_EN} · App: {APP} (Android)</p>
<div class="card"><b>In short:</b> You don't create an account for {APP}. Your learning data stays on your own device and is not sent to our servers. The free version shows Google AdMob ads, which Google operates. Payments are handled by Google Play.</div>
<h2>1. Controller</h2><p>{DEV} ("we"). Contact: <a href="mailto:{MAIL}">{MAIL}</a></p>
<h2>2. Accounts and personal information</h2><p>You don't need to provide a name, email address, phone number or similar information to use the app. We don't collect such information and we don't keep user data on our servers.</p>
<h2>3. Data stored on your device</h2><p>The app stores your chosen goals and daily study time, lesson and exercise history (correct/incorrect answers, hints, review schedule), XP, streak and badge information, and subscription status <b>only on your device</b>. This data is not sent to us. You can delete learning data via <i>Profile → Settings and data → Delete all my data</i>, or remove all local data by uninstalling the app.</p>
<h2>4. Ads (Google AdMob)</h2><p>The free version shows banner, interstitial and rewarded ads served by <b>Google AdMob</b>. To deliver, measure and secure ads, Google may process your advertising ID (Android Advertising ID), IP address, device and app information and your interaction with ads. This processing is Google's responsibility; see <a href="https://policies.google.com/technologies/ads">policies.google.com/technologies/ads</a> and <a href="https://support.google.com/admob/answer/6128543">how AdMob uses data</a>.</p>
<p>In the European Economic Area, the UK and other relevant regions, the app shows Google's consent form (UMP) on first launch; you can choose your ad preferences there and change them at any time. You can turn off personalized ads or reset your advertising ID in Android <i>Settings → Google → Ads</i>.</p>
<h2>5. Subscriptions and payments (Google Play)</h2><p>Purchasing, renewing and cancelling the Premium subscription is handled by <b>Google Play</b>. We never see or store your card or payment details. The app only learns from Google Play whether your subscription is active and keeps that status on your device.</p>
<h2>6. Third-party services</h2><ul><li>Google AdMob (ads) – Google LLC</li><li>Google Play Billing (subscription payments) – Google LLC</li></ul><p>We use no other analytics, tracking or crash-reporting services.</p>
<h2>7. Children</h2><p>{APP} is not directed to children under 13 and we do not knowingly collect data from children. If you believe a child is using the app, contact us.</p>
<h2>8. Retention and security</h2><p>Your learning data stays on your device until you delete it or uninstall the app. Because we keep no server-side user data, there is no server-side breach risk; we recommend using your device's screen lock and updates.</p>
<h2>9. Your rights (GDPR / Turkish KVKK)</h2><p>You have the right to know whether your personal data is processed, to request information, rectification, erasure and to object. Because we don't collect personal data, most rights are exercised by deleting the data on your device. For advertising data processed by Google, contact Google. For other requests: <a href="mailto:{MAIL}">{MAIL}</a>. You may also lodge a complaint with your local data protection authority.</p>
<h2>10. Changes</h2><p>We may update this policy. Material changes will be shown on this page along with the effective date.</p>
<h2>11. Contact</h2><p><a href="mailto:{MAIL}">{MAIL}</a></p>"""

TERMS_TR = f"""<p class="meta">Yürürlük tarihi: {DATE_TR}</p>
<h2>1. Hizmet</h2><p>{APP}, Türkçe konuşanlar için çevrimdışı çalışan bir İngilizce öğrenme uygulamasıdır. Uygulamayı indirerek bu koşulları kabul etmiş olursun.</p>
<h2>2. Ücretsiz ve Premium</h2><p>Bazı bölümler ücretsizdir ve reklam içerir. <b>Premium</b> abonelik tüm bölümlerin kilidini açar ve reklamları kaldırır.</p>
<h2>3. Abonelik, yenileme ve iptal</h2><ul><li>Planlar haftalık, aylık ve yıllıktır; fiyatlar satın alma ekranında ve Google Play'de ülkene göre görünür.</li><li>Yıllık planda uygun kullanıcılara 7 günlük ücretsiz deneme sunulabilir. Deneme bitmeden iptal etmezsen abonelik, görüntülenen ücretle başlar.</li><li>Abonelikler, dönem bitmeden en az 24 saat önce iptal edilmedikçe <b>otomatik yenilenir</b>.</li><li>İptal: Google Play → Profil → Ödemeler ve abonelikler → Abonelikler → {APP}. Uygulamayı silmek aboneliği iptal etmez.</li><li>İadeler Google Play iade politikasına tabidir.</li><li>Fiyat değişikliklerinde Google Play seni önceden bilgilendirir.</li></ul>
<h2>4. Eğitim içeriği hakkında</h2><p>Dersler, kelimeler ve hikâyeler eğitim amaçlıdır ve yapay zekâ desteğiyle hazırlanmıştır; hata veya eksik içerebilir. Resmî sınav veya profesyonel çeviri için tek başına dayanak olarak kullanılmamalıdır. Hata bulursan bize bildir.</p>
<h2>5. Kabul edilebilir kullanım</h2><p>Uygulamayı tersine mühendislikle çözmeye, aboneliği veya reklam sistemini atlatmaya, otomatik araçlarla reklamlara tıklamaya veya yasa dışı amaçla kullanmaya izin verilmez.</p>
<h2>6. Fikrî mülkiyet</h2><p>Uygulamanın tasarımı, kodu, içeriği ve markası {DEV}'e aittir. Sana kişisel, devredilemez, ticari olmayan bir kullanım lisansı verilir.</p>
<h2>7. Sorumluluğun sınırı</h2><p>Uygulama "olduğu gibi" sunulur. Yasaların izin verdiği ölçüde, uygulamanın kullanımından doğan dolaylı zararlardan sorumlu değiliz. Tüketici mevzuatından doğan zorunlu haklarınız saklıdır.</p>
<h2>8. Değişiklikler ve fesih</h2><p>Koşulları ve uygulamayı güncelleyebiliriz. Koşullara aykırı kullanımda erişimi sonlandırma hakkımız saklıdır.</p>
<h2>9. Uygulanacak hukuk</h2><p>Bu koşullar Türkiye Cumhuriyeti hukukuna tabidir; tüketici işlemlerinde tüketici hakem heyetleri ve mahkemelerin yetkisi saklıdır.</p>
<h2>10. İletişim</h2><p><a href="mailto:{MAIL}">{MAIL}</a> · <a href="gizlilik.html">Gizlilik Politikası</a></p>"""

TERMS_EN = f"""<p class="meta">Effective date: {DATE_EN}</p>
<h2>1. Service</h2><p>{APP} is an offline language-learning app for Turkish speakers learning English. By downloading the app you agree to these terms.</p>
<h2>2. Free and Premium</h2><p>Some sections are free and include ads. A <b>Premium</b> subscription unlocks all sections and removes ads.</p>
<h2>3. Subscriptions, renewal and cancellation</h2><ul><li>Plans are weekly, monthly and yearly; prices are shown on the purchase screen and in Google Play for your country.</li><li>The yearly plan may include a 7-day free trial for eligible users. If you don't cancel before the trial ends, the subscription starts at the displayed price.</li><li>Subscriptions <b>renew automatically</b> unless cancelled at least 24 hours before the end of the current period.</li><li>Cancel: Google Play → Profile → Payments &amp; subscriptions → Subscriptions → {APP}. Uninstalling the app does not cancel a subscription.</li><li>Refunds are subject to Google Play's refund policy.</li><li>Google Play will notify you of price changes in advance.</li></ul>
<h2>4. About the learning content</h2><p>Lessons, words and stories are educational and were prepared with AI assistance; they may contain errors or omissions. They should not be relied on alone for official exams or professional translation. Please report mistakes to us.</p>
<h2>5. Acceptable use</h2><p>You may not reverse engineer the app, circumvent the subscription or ad system, click ads with automated tools, or use the app for unlawful purposes.</p>
<h2>6. Intellectual property</h2><p>The app's design, code, content and brand belong to {DEV}. You receive a personal, non-transferable, non-commercial licence to use it.</p>
<h2>7. Limitation of liability</h2><p>The app is provided "as is". To the extent permitted by law we are not liable for indirect damages arising from its use. Your mandatory consumer rights remain unaffected.</p>
<h2>8. Changes and termination</h2><p>We may update these terms and the app. We may end access for use that violates these terms.</p>
<h2>9. Governing law</h2><p>These terms are governed by the laws of the Republic of Türkiye; mandatory consumer-protection jurisdiction rules remain unaffected.</p>
<h2>10. Contact</h2><p><a href="mailto:{MAIL}">{MAIL}</a> · <a href="privacy.html">Privacy Policy</a></p>"""

INDEX = f"""<p class="meta">{APP} · İngilizceyi bir yıldız yolculuğu gibi öğren / Learn English like a journey among the stars</p>
<div class="btns"><a href="gizlilik.html">Gizlilik Politikası (Türkçe)</a><a href="privacy.html">Privacy Policy (English)</a><a href="kosullar.html">Kullanım Koşulları (Türkçe)</a><a href="terms.html">Terms of Use (English)</a></div>"""

files = {
 'index.html': page('tr','index.html',APP,INDEX,('index.html',)),
 'gizlilik.html': page('tr','gizlilik.html','Gizlilik Politikası',PRIV_TR,('privacy.html',)),
 'privacy.html': page('en','privacy.html','Privacy Policy',PRIV_EN,('gizlilik.html',)),
 'kosullar.html': page('tr','kosullar.html','Kullanım Koşulları',TERMS_TR,('terms.html',)),
 'terms.html': page('en','terms.html','Terms of Use',TERMS_EN,('kosullar.html',)),
}
for n,c in files.items(): open(n,'w',encoding='utf-8').write(c)
open('.nojekyll','w').write('')
print('ok', list(files))
