# -*- coding: utf-8 -*-
"""
Delilli Hanefi Fıkıh Rehberi - Genişletilmiş Veri Tabanı
"""

CATEGORIES = {
    "💧 Temizlik (Taharet)": {
        "start_page": 38,
        "end_page": 137,
        "description": "İslam'da temizliğin önemi, abdest, gusül, teyemmüm ve özel haller (hayız/nifas) gibi temel taharet konuları.",
        "subtopics": {
            "Abdest (Vudu)": {
                "pages": list(range(60, 80)),
                "summary": """
                **Abdestin Farzları (Hanefi Mezhebine Göre):**
                1. **Yüzü bir kere yıkamak:** Saç bitiminden çene altına, iki kulak memesine kadar olan alanı kapsar.
                2. **Elleri dirseklerle beraber bir kere yıkamak:** Dirsekler de yıkamaya dahildir.
                3. **Başın en az dörtte birini (1/4) meshetmek:** Islak eli başa sürmektir.
                4. **Ayakları topuklarla beraber bir kere yıkamak:** Topuk kemikleri de yıkanmalıdır.
                
                **Abdestin Başlıca Sünnetleri:**
                - Niyet etmek, euzü-besmele ile başlamak.
                - Önce elleri bileklere kadar yıkamak.
                - Ağza (mazmaza) ve burna (istinşak) üçer kere su vermek.
                - Misvak kullanmak.
                - Uzuvları yıkarken sıraya (tertibe) uymak ve sağ taraftan başlamak.
                - Uzuvları üçer defa yıkamak ve araya başka iş sokmadan peş peşe yıkamak (muvalat).
                
                **Abdesti Bozan Durumlar:**
                - Ön ve arkadan çıkan her türlü idrar, dışkı, yel, meni, mezi, vedi vb. sıvılar.
                - Vücudun herhangi bir yerinden çıkan kan, irin veya sarı suyun, çıktığı yerin dışına taşması/akması.
                - Ağız dolusu kusmak (yiyecek, su veya safra).
                - Uzanarak, yaslanarak veya uyuklayarak bilincin kaybolması.
                - Namazda yanındakinin duyacağı kadar yüksek sesle gülmek (kahkaha).
                """
            },
            "Gusül (Boy Abdesti)": {
                "pages": list(range(80, 95)),
                "summary": """
                **Guslün Farzları (Hanefi Mezhebine Göre):**
                1. **Ağza su vermek (Mazmaza):** Boğaza kadar bolca su verip çalkalamak.
                2. **Burna su vermek (İstinşak):** Geniz sızlayacak şekilde burna su çekip temizlemek.
                3. **Bütün vücudu kuru yer kalmayacak şekilde yıkamak:** Göbek deliği, küpe delikleri, saç dipleri ve tırnak araları gibi dar ve hassas noktaların da tamamen ıslanması şarttır.
                
                **Guslün Sünnetleri:**
                - Gusle niyet ve besmele ile başlamak.
                - Önce elleri ve avret yerini yıkamak, vücutta necis bir şey varsa onu temizlemek.
                - Gusülden önce tam bir abdest almak.
                - Bedenine three defa su dökmek: Önce başa, sonra sağ omuza, sonra sol omuza.
                
                **Guslü Gerektiren Haller (Cenabetlik ve Diğer Durumlar):**
                - Şehvetle meninin gelmesi (rüyada ihtilam olunarak veya uyanıkken herhangi bir sebeple).
                - Cinsel ilişki (meni gelmese dahi sünnet yerlerinin birleşmesiyle gusül farz olur).
                - Kadınların adet (hayız) veya lohusalık (nifas) halinin sona ermesi.
                """
            },
            "Teyemmüm": {
                "pages": list(range(95, 107)),
                "summary": """
                **Teyemmümün Meşru Olduğu Haller:**
                - Abdest veya gusül için yeterli suyun bulunmaması (suyun en az 1.8 km mesafede olması).
                - Suyun olmasına rağmen kullanımına mani tıbbi engeller (hastalık, yaranın artma tehlikesi, soğuktan dolayı donma veya ölüm tehlikesi).
                - Suyu elde etmenin tehlikeli olması (düşman korkusu, vahşi hayvan tehlikesi, susuz kalma riski).
                
                **Teyemmümün Farzları:**
                1. **Niyet etmek:** Ne için teyemmüm yapıldığına (abdest veya gusül yerine) niyet etmek şarttır. Niyet olmaksızın sadece toprağa dokunmak teyemmüm yerine geçmez.
                2. **Elleri temiz toprağa iki kez vurmak:**
                   - Birinci vuruşta ellerin iç yüzüyle yüzün tamamını meshetmek.
                   - İkinci vuruşta sağ ve sol kolları dirseklerle beraber meshetmek.
                
                **Teyemmümü Bozan Durumlar:**
                - Abdesti veya guslü bozan her şey teyemmümü de bozar.
                - Teyemmüm etmeyi mübah kılan mazeretin ortadan kalkması (suyun bulunması, hastalığın geçmesi).
                """
            },
            "Mesh Hükümleri": {
                "pages": list(range(107, 115)),
                "summary": """
                **Mestler Üzerine Mesh Etmenin Şartları:**
                - Mestlerin, ayakları abdest alırken yıkanması farz olan yerleriyle birlikte örtmesi gerekir.
                - Mestlerin, abdestli olarak giyilmiş olması şarttır.
                - Mestlerin en az 1 fersah (yaklaşık 5-6 km) yürüyecek kadar dayanıklı olması gerekir.
                - Üzerinde mesh yapılacak mestlerde topuktan aşağı üç el parmağı sığacak genişlikte yırtık olmamalıdır.
                
                **Mesh Süreleri:**
                - Mukimler (yolcu olmayanlar) için mesh süresi 24 saat (1 gün 1 gece)dir.
                - Seferiler (yolcular) için mesh süresi 72 saat (3 gün 3 gece)dir.
                - Süre, mestin giyildiği andan değil, mest giyildikten sonra abdestin ilk bozulduğu andan itibaren başlar.
                
                **Meshi Bozan Durumlar:**
                - Abdesti bozan her durum meshi de bozar.
                - Mestin ayaktan çıkması veya çıkarılması (bir ayak çıksa bile abdest bozulur).
                - Mesh süresinin dolması.
                - Mestin içine su girerek ayağın yarıdan fazlasını ıslatması.
                """
            },
            "Suların Hükümleri": {
                "pages": list(range(115, 122)),
                "summary": """
                **Suların Sınıflandırılması:**
                1. **Mutlak Sular:** Yaratılışındaki tabi halini koruyan, yağmur, kar, deniz, nehir ve kuyu suları. Bu sular hem temiz hem de temizleyicidir.
                2. **Mukayyet Sular:** İçine temiz bir maddenin karışmasıyla tabi ismi değişen sular (gül suyu, et suyu, meyve suyu). Bu sularla necaset temizlenebilir fakat abdest veya gusül alınamaz.
                
                **Temizlik Açısından Sular:**
                - **Temiz ve Temizleyici Olan Sular:** Mutlak sular.
                - **Kullanılmış Su (Ma-i Müstamel):** Abdest veya gusülde kullanılarak bedenden ayrılan su. Hanefi mezhebine göre temizdir fakat temizleyici değildir; yani bu suyla tekrar abdest alınamaz.
                - **Temiz Olmayan Sular:** İçine pislik (necaset) düşen durgun ve az sular. Akarsular veya büyük havuzlar (en az 50 m²) ise rengi, kokusu veya tadı bozulmadıkça necis sayılmaz.
                """
            },
            "Necasetler ve Temizleme Yolları": {
                "pages": list(range(122, 130)),
                "summary": """
                **Necaset Çeşitleri:**
                1. **Necaset-i Galîza (Ağır Pislik):** İdrar, dışkı, leş, akan kan, şarap, domuz eti ve salyası. Namaza engel olan miktar: Katı maddelerde 1 dirhem (yaklaşık 3 gram), sıvılarda ise el ayası kadar bir alandır.
                2. **Necaset-i Hafîfe (Hafif Pislik):** Eti yenen hayvanların idrar ve dışkıları, kümes hayvanı dışındaki kuşların pislikleri. Namaza engel olan miktar: Bulaştığı uzvun veya elbisenin dörtte birinden (1/4) fazlasıdır.
                
                **Temizleme Yolları:**
                - Görünür pisliklerde: Pisliğin kendisinin (aynının) giderilmesi, yıkanması ve temizlenmesiyle olur.
                - Görünmez pisliklerde: Pis bulaşan kumaş veya uzvun en az üç defa yıkanıp her defasında sıkılmasıyla temizlik hasıl olur. Sıkılamayan eşyalar ise su damlaması kesilene kadar üç defa yıkanır.
                """
            },
            "Özel Haller (Hayız, Nifas, İstihâze)": {
                "pages": list(range(130, 137)),
                "summary": """
                **Kadınlara Özgü Haller:**
                1. **Hayız (Adet Hali):** Ergenlik çağındaki sağlıklı kadından gelen periyodik kan. Hanefi mezhebine göre süresi en az 3 gün (72 saat), en fazla 10 gündür. İki hayız arasındaki temizlik süresi en az 15 gündür.
                2. **Nifas (Lohusalık Hali):** Doğumdan sonra gelen kandır. Süresinin en az sınırı yoktur, en fazla süresi ise 40 gündür. 40 günden sonra gelen kan özür (istihaze) sayılır.
                3. **İstihâze (Özür Kanı):** Hayız ve nifas süreleri dışındaki rahim içi damar kanamalarıdır. İbadetlere engel değildir. Bu durumdaki kadın özür sahibi hükmündedir; her namaz vakti için ayrı abdest alır ve vakit çıkınca abdesti bozulur.
                
                **Hayız ve Nifas Halinde Yasak Olan İbadetler:**
                - Namaz kılmak ve oruç tutmak (kılınmayan namazlar kaza edilmez, tutulmayan oruçlar kaza edilir).
                - Kabe'yi tavaf etmek.
                - Kur'an-ı Kerim okumak ve mushafa dokunmak.
                - Cinsel ilişkide bulunmak.
                """
            }
        }
    },
    "🕌 Namaz (Salat)": {
        "start_page": 138,
        "end_page": 301,
        "description": "Namazın farzları, vacipleri, vakitleri, kılınış şekli, cemaat hükümleri, bayram ve cuma namazları gibi geniş fıkhi çerçeve.",
        "subtopics": {
            "Namazın Farzları": {
                "pages": list(range(144, 168)),
                "summary": """
                **Namazın Dışındaki Farzları (Şartları):**
                1. **Hadesten Taharet:** Abdest veya gusül alarak manevi kirlilikten temizlenmek.
                2. **Necasetten Taharet:** Bedenin, elbisenin ve seccadenin maddi pisliklerden temiz olması.
                3. **Setr-i Avret:** Örtülmesi gereken yerleri örtmek (erkeklerde göbek-diz altı, kadınlarda yüz, el ve ayak hariç tüm beden).
                4. **İstikbal-i Kıble:** Kabe yönüne dönmek.
                5. **Vakit:** Kılınacak namazın vaktinin girmiş olması.
                6. **Niyet:** Kılınacak namazı kalben tayin etmek.
                
                **Namazın İçindeki Farzları (Rükünleri):**
                1. **İftitah Tekbiri:** Namaza başlarken "Allahu Ekber" demek.
                2. **Kıyam:** Ayakta durmak.
                3. **Kıraat:** Namazda Kur'an okumak.
                4. **Rükû:** Eğilmek.
                5. **Secde:** Yere kapanmak (iki defa yapılır).
                6. **Kade-i Ahire:** Son rekatta "Ettehiyyatü" okuyacak kadar oturmak.
                """
            },
            "Namazın Vacipleri ve Sünnetleri": {
                "pages": list(range(168, 175)),
                "summary": """
                **Namazın Başlıca Vacipleri:**
                - İlk iki rekatta Fatiha suresini okumak ve Fatiha'ya bir sure veya üç kısa ayet eklemek (Zamm-ı Sure).
                - Farz namazlarda kıraati ilk iki rekata tahsis etmek.
                - Secdede alınla beraber burnu da yere koymak.
                - Üç ve dört rekatlı namazlarda ikinci rekatın sonunda oturmak (İlk oturuş).
                - Oturuşlarda "Ettehiyyatü" duasını okumak.
                - Ta'dil-i erkan üzere kılmak (rükünleri sakinlik içinde yapmak).
                - Namaz sonunda sağa ve sola selam vermek.
                - Vitir namazında Kunut tekbiri almak ve Kunut dualarını okumak.
                
                **Namazın Sünnetleri:**
                - İftitah tekbiri alırken elleri kaldırmak.
                - Sübhaneke okumak, euzü-besmele çekmek.
                - Farz namazlarda rükû ve secde tekbirlerini almak.
                - Rükûda üç defa "Sübhâne rabbiye'l-azîm", secdede üç defa "Sübhâne rabbiye'l-a'lâ" demek.
                """
            },
            "Namazı Bozan ve Mekruh Kılan Durumlar": {
                "pages": list(range(175, 185)),
                "summary": """
                **Namazı Bozan Durumlar:**
                - Namazda konuşmak, birine selam vermek veya selam almak.
                - Dışarıdan bakana namazda olmadığını düşündürecek kadar büyük bir hareket yapmak (Amel-i kesîr).
                - Kıbleden göğsünü çevirmek.
                - Namaz içinde bir şey yiyip içmek (diş arasında kalan nohut büyüklüğündeki şeyi yutmak da bozar).
                - Üflemek, ah çekmek, dünyevi bir acı veya musibetten ötürü sesli ağlamak (hastalık veya ahiret korkusuyla ağlamak bozmaz).
                - Namazda kendi işiteceği kadar gülmek abdesti bozmaz ama namazı bozar; yanındakinin işiteceği kadar gülmek (kahkaha) ise hem abdesti hem namazı bozar.
                
                **Namazın Mekruhları:**
                - Namaz esnasında esnemek, gerinmek veya parmak çıtlatmak.
                - Kıyafeti düzeltmekle veya saçla gereksiz yere oynamak.
                - Gözleri yummak veya yukarıya dikmek (huzur bulmak için yummak mekruh değildir).
                - Secdeye giderken elleri dizlerden önce mazeretsiz yere koymak.
                """
            },
            "Cemaatle Namaz ve İmamet": {
                "pages": list(range(185, 195)),
                "summary": """
                **Cemaatle Namazın Hükmü:**
                - Hanefi mezhebine göre gücü yeten erkekler için beş vakit namazı cemaatle kılmak sünnet-i müekkededir. Cemaatle kılınan namaz, tek başına kılınan namazdan 27 derece daha faziletlidir.
                
                **İmamet Şartları:**
                - İmamın müslüman olması, akıl sağlığının yerinde olması, ergen (baliğ) olması, erkek olması ve namaz geçerli olacak kadar Kur'an-ı Kerim ezberinin olması şarttır.
                
                **İmama Uyan Kimsenin (Muktedi) Durumu:**
                - İmama uyan kimse niyet ederken "Uydum hazır olan imama" der.
                - Hanefi fıkhına göre imama uyan kimse ayaktayken Fatiha veya sure okumaz, sessizce durup imamın kıraatini dinler ("İmamın kıraati cemaatin de kıraatidir" hadisine dayanarak).
                - Rükû ve secdelerdeki tesbihleri uyan kişi kendisi söyler.
                """
            },
            "Yolcu Namazı (Seferilik)": {
                "pages": list(range(195, 205)),
                "summary": """
                **Seferiliğin Şartları:**
                - Hanefi fıkhına göre en az 3 günlük (orta yürüyüşle 18 saatlik, yani yaklaşık 90 km) bir mesafeye gitmek üzere yola çıkmak.
                - Gidilen yerde 15 günden daha az kalmaya niyet etmek. Eğer 15 gün veya daha fazla kalınacaksa seferilik biter, kişi mukim olur.
                
                **Namazların Kısaltılması (Kasr-ı Salat):**
                - Seferi olan kişi 4 rekatlı farz namazları (Öğle, İkindi, Yatsı) **2 rekat** olarak kılar. Bu kısaltma Hanefilerde bir ruhsat değil, azimettir (yani kısaltmak vaciptir; bilerek 4 kılmak mekruhtur).
                - 2 rekatlı farzlar (Sabah) ve 3 rekatlı farzlar (Akşam) ile Vitir namazı aynen kılınır, kısaltılmaz.
                - Yolculuk esnasında müsait olunduğunda sünnet namazlar da kılınır, sıkışık durumlarda terk edilebilir.
                """
            },
            "Secde Çeşitleri (Sehiv, Tilavet, Şükür)": {
                "pages": list(range(205, 215)),
                "summary": """
                **1. Sehiv (Yanılma) Secdesi:**
                - Namazda yanılarak farzın geciktirilmesi veya vacibin terk edilmesi ya da geciktirilmesi durumunda yapılır. Son oturuşta "Ettehiyyatü" okunup sağ tarafa selam verildikten sonra iki secde yapılır, tekrar oturulup dualar okunarak selam verilir.
                
                **2. Tilavet Secdesi:**
                - Kur'an-ı Kerim'deki 14 secde ayetinden birini okuyan veya işiten mükellefin yapması **vaciptir**.
                - Yapılışı: Ayaktan niyetle doğrudan secdeye gidilir. Secdede üç defa "Sübhâne rabbiye'l-a'lâ" denir ve tekbirle ayağa kalkılır. Secdeye giderken ve kalkarken eller kaldırılmaz.
                
                **3. Şükür Secdesi:**
                - Bir nimete kavuşmaktan veya bir musibetten kurtulmaktan dolayı Allah'a şükretmek amacıyla kıbleye dönüp secde etmektir. Müstehaptır. Yapılışı tilavet secdesi gibidir. Namaz içinde yapılması mekruhtur.
                """
            },
            "Cuma, Bayram ve Teravih Namazları": {
                "pages": list(range(215, 230)),
                "summary": """
                **Cuma Namazı:**
                - Cuma namazı hür, mukim, sağlıklı ve erkek olan her mükellefe **farz-ı ayındır**. Cemaatle kılınması şarttır (en az imam hariç 3 kişi).
                - Namazdan önce imamın hutbe okuması şarttır. Hutbe okunurken cemaatin konuşması, namaz kılması veya konuşanı susturması dahi mekruhtur.
                
                **Bayram Namazları:**
                - Ramazan ve Kurban bayramlarında yılda iki defa kılınan 2 rekatlık namazdır. Hanefi mezhebine göre cuma namazı farz olan kişilere bayram namazı kılmak **vaciptir**.
                - Bayram namazlarında diğer namazlardan farklı olarak her rekatta üçer defa fazla tekbir (Zait tekbirler) alınır.
                
                **Teravih Namazı:**
                - Ramazan ayında yatsı namazından sonra kılınan 20 rekatlık namazdır. Kadın ve erkekler için sünnet-i müekkededir. İki veya dört rekatta bir selam verilerek kılınır.
                """
            },
            "Kaza Namazları ve Tertip": {
                "pages": list(range(230, 245)),
                "summary": """
                **Kaza Namazı:**
                - Vaktinde kılınamamış olan farz ve vitir namazlarının sonradan kılınmasına kaza denir. Sünnet namazların kazası olmaz (sadece sabah namazı o günün öğle vaktine kadar kaza edilecekse sünnetiyle birlikte kaza edilebilir).
                - Kaza namazı kılarken "Kaza kılmaya" niyet edilir. Kaza namazları için belirli bir vakit yoktur; ancak kerahat vakitlerinde kılınması caiz değildir.
                
                **Tertip Sahibi Olmak:**
                - Üzerinde vitir dahil 5 vakitten az namaz borcu olan kimseye **Tertip Sahibi** denir. Bu kimsenin kaza namazını kılmadan vakit namazını kılması caiz değildir; namazlar arasında sırayı gözetmesi vaciptir.
                - Kaza namazı borcu 6 vakit veya daha fazlaya ulaştığında tertip düşer ve kişi istediği sırayla kılabilir.
                """
            }
        }
    },
    "🌾 Zekat ve Fıtır Sadakası": {
        "start_page": 302,
        "end_page": 349,
        "description": "Zekatın farz olma şartları, nisap miktarları, zekat verilecek mallar, fitre (sadaka-i fıtır) ve sarf edilecek yerler.",
        "subtopics": {
            "Zekatın Farziyeti ve Nisabı": {
                "pages": list(range(302, 312)),
                "summary": """
                **Zekatın Farz Olmasının Şartları:**
                - Müslüman olmak.
                - Akıl sağlığı yerinde ve ergenlik çağına gelmiş olmak (Hanefi mezhebinde çocukların ve akıl hastalarının mallarından zekat verilmesi farz değildir; velisi öşür hariç zekat vermez).
                - Hür olmak.
                - Tam mülkiyet ve elinde nisap miktarı nami (artıcı) mal bulunması.
                
                **Nisap Miktarı:**
                - Borçlar ve temel ihtiyaçlar (Havâic-i asliye) çıktıktan sonra 80.18 gram altın veya buna denk nakit para ya da ticaret malına sahip olmaktır.
                - Malın üzerinden 1 kameri yıl geçmiş olması şarttır (Havalanü'l-havl).
                """
            },
            "Zekat Verilecek Yerler (Sınıflar)": {
                "pages": list(range(335, 349)),
                "summary": """
                **Zekat Kimlere Verilir? (Tevbe Suresi 60. Ayet):**
                - Fakirler: Nisap miktarından az malı olanlar.
                - Miskinler: Hiçbir şeyi olmayan yoksullar.
                - Borçlular: Borcu elindeki maldan fazla olanlar.
                - Yolda Kalmışlar: Memleketinde zengin olsa da bulunduğu yerde parasız kalanlar.
                - Allah Yolunda Olanlar (Fi sebilillah): İlim talebeleri, cihat edenler.
                
                **Zekat Verilemeyecek Kişiler:**
                - Ana-baba, büyükanne-büyükbaba (Usûl).
                - Çocuklar ve torunlar (Fürû).
                - Eşler birbirine zekat veremez.
                - Dinen zengin sayılan kimseler.
                - Gayrimüslimler (Hanefi mezhebine göre zekat gayrimüslime verilmez, sadece nafile sadakalar verilebilir).
                """
            },
            "Ticaret Malları ve Altın/Gümüş Zekatı": {
                "pages": list(range(312, 320)),
                "summary": """
                **Zekat Oranları:**
                - Altın, gümüş, nakit para ve ticaret mallarında zekat oranı **1/40 (%2.5)** oranındadır.
                
                **Ticaret Malları:**
                - Kar etmek amacıyla satın alınan ve elden çıkarılması planlanan her türlü mal ticaret malıdır.
                - Yıl sonundaki toptan piyasa değeri üzerinden hesaplanır. Dükkanın demirbaş eşyaları (raf, bilgisayar vb.) zekata tabi değildir.
                - Borçlar toplam varlıktan düşülür; kalan miktar nisabın üzerindeyse zekatı verilir.
                """
            },
            "Toprak Ürünleri (Öşür) ve Hayvanların Zekatı": {
                "pages": list(range(320, 332)),
                "summary": """
                **Toprak Ürünleri Zekatı (Öşür):**
                - Yağmur suyuyla sulanan topraklardan alınan mahsulde zekat oranı **1/10 (%10)** dur.
                - Kuyu suyu, kova veya motor gibi masraflı sulamayla elde edilen ürünlerde oran **1/20 (%5)** dir.
                - Öşür için 1 yıl bekleme şartı yoktur; ürün hasat edildiği an verilir. Ebu Hanife'ye göre toprak ürünlerinde nisap şartı yoktur, az veya çok her üründen öşür verilir.
                
                **Hayvanların Zekatı:**
                - Hayvanların zekata tabi olması için yılın çoğunda kırlarda otlayan (saime) cinsten olması gerekir.
                - Koyun ve keçide nisap 40'tır. 40-120 arası için 1 koyun verilir.
                - Sığırda nisap 30'dur. 30 sığır için 1 adet 1 yaşında buzağı verilir.
                """
            },
            "Fıtır Sadakası (Fitre)": {
                "pages": list(range(332, 335)),
                "summary": """
                **Hükmü ve Vacip Olma Şartları:**
                - Fıtır sadakası (fitre), Ramazan bayramına kavuşan ve temel ihtiyaçlarının dışında nisap miktarı mala sahip olan her müslümana **vaciptir**. Zekattan farklı olarak malın nami (artıcı) olması veya üzerinden 1 yıl geçmesi şart değildir.
                - Kişi kendisinin ve ergen olmamış çocuklarının fitresini vermekle yükümlüdür.
                
                **Miktarı ve Ödeme Vakti:**
                - Buğday, arpa, hurma veya kuru üzüm üzerinden hesaplanır. Buğday için yarım sa' (yaklaşık 1.66 kg), diğerleri için bir sa' (yaklaşık 3.33 kg) veya bunların nakit değeri verilir.
                - Bayram sabahı tan yerinin ağarmasıyla vacip olur; ancak bayramdan önce verilmesi müstehaptır.
                """
            }
        }
    },
    "🌙 Oruç (Savm)": {
        "start_page": 350,
        "end_page": 373,
        "description": "Ramazan orucunun farziyeti, niyet vakitleri, orucu bozan ve bozmayan durumlar, kaza, kefaret ve itikaf hükümleri.",
        "subtopics": {
            "Oruç Çeşitleri ve Niyet Hükümleri": {
                "pages": list(range(350, 355)),
                "summary": """
                **Oruç Çeşitleri:**
                - Farz Oruç: Ramazan orucu ve bunun kazası ile keffaret oruçları.
                - Vacip Oruç: Adanan oruçlar (nezir) ve bozulan nafile orucun kazası.
                - Nafile Oruç: Şevval orucu, Aşure orucu vb. sünnet ve müstehap oruçlar.
                
                **Niyet Vakitleri:**
                - **Gündüz Niyeti Caiz Olanlar:** Belirli günlerdeki adak oruçları, nafile oruçlar ve Ramazan orucu için niyet vakti; gün batımından başlar, ertesi günün kaba kuşluk vaktine kadar devam eder.
                - **Geceden Niyet Şart Olanlar:** Ramazan orucunun kazası, keffaret oruçları ve mutlak (zamanı belirlenmemiş) adak oruçları için imsaktan önce (geceden) niyet etmek şarttır.
                """
            },
            "Orucu Bozan Durumlar (Kaza/Kefaret)": {
                "pages": list(range(355, 365)),
                "summary": """
                **Kaza ve Kefaret Gerektiren Haller:**
                - Ramazan orucunu tutarken bilerek ve isteyerek yemek, içmek, gıda veya gıda takviyesi tüketmek, ilaç almak.
                - Bilerek cinsel ilişkide bulunmak.
                - *Kefaret:* 2 ay (60 gün) peş peşe oruç tutmak; buna gücü yetmeyen 60 fakiri sabahlı akşamlı doyurur.
                
                **Sadece Kaza Gerektiren Durumlar:**
                - Besin değeri taşımayan taş, toprak, kağıt, metal para gibi maddeleri yutmak.
                - Kendi isteğiyle ağız dolusu kusmak.
                - Hataen su yutmak (abdest alırken boğazına su kaçması).
                - İmsak vakti geçtiği halde sahur yapmaya devam etmek veya güneş batmadığı halde iftar etmek.
                """
            },
            "Orucu Bozmayan ve Mekruh Kılan Haller": {
                "pages": list(range(365, 370)),
                "summary": """
                **Orucu Bozmayan Durumlar:**
                - Unutarak yemek, içmek veya cinsel ilişkide bulunmak (hatırlayınca hemen ağız temizlenir ve oruca devam edilir).
                - Göze damla damlatmak, sürme çekmek.
                - Kan aldırmak (hacamat).
                - Rüyada ihtilam olmak veya cünüp olarak sabahlamak.
                - Kendi isteği dışında kusmak.
                - Tükürüğünü yutmak.
                
                **Orucun Mekruhları:**
                - Bir şeyi yutmadan tadına bakmak (aşçı veya eşi gibi mazereti olanlar için mekruh değildir).
                - Kan aldırmak gibi vücudu halsiz bırakacak işler yapmak.
                - Abdest alırken ağza ve burna su vermede aşırıya kaçmak.
                """
            },
            "İtikaf İbadeti": {
                "pages": list(range(370, 373)),
                "summary": """
                **İtikafın Tanımı ve Hükmü:**
                - İtikaf, bir mescitte ibadet niyetiyle dış dünyadan ilişkisini keserek belirli bir süre kalmaktır.
                - Ramazan ayının son on gününde itikafa girmek erkekler için sünnet-i kifayedir (mahallede bir kişi yaparsa diğerlerinden sorumluluk düşer). Kadınlar kendi evlerinin namaz kıldıkları bir odasında itikafa girerler.
                
                **Şartları ve İtikafı Bozan Şeyler:**
                - İtikafa giren kimse sadece şer'i (cuma namazı gibi) ve zaruri (tuvalet, abdest gibi) ihtiyaçlar için mescitten çıkabilir. Mazeretsiz bir an bile mescitten çıkmak itikafı bozar.
                - Cinsel ilişkide bulunmak itikafı tamamen bozar.
                """
            }
        }
    },
    "🕋 Hac ve Umre": {
        "start_page": 374,
        "end_page": 586,
        "description": "Haccın farzları, mikat sınırları, ihram yasakları, tavaf, sa'y, Arafat vakfesi ve haccın eda ediliş şekilleri.",
        "subtopics": {
            "Haccın Şartları ve Farzları": {
                "pages": list(range(374, 385)),
                "summary": """
                **Haccın Farz Olma Şartları:**
                - Müslüman olmak, akıllı olmak ve ergen olmak.
                - Hür olmak.
                - Hac ibadetini yapabilecek maddi güce (yol ve azık parasına) sahip olmak.
                - Yol emniyetinin bulunması.
                
                **Haccın Farzları (Rükün ve Şartları):**
                1. **İhram (Şarttır):** Hac veya umreye niyet edip helal olan bazı şeyleri haram kılmaktır.
                2. **Arafat Vakfesi (Rükündür):** Arife günü zeval vaktinden bayram sabahına kadar olan sürede Arafat'ta bulunmak.
                3. **Ziyaret Tavafı (Rükündür):** Bayram günlerinde Kabe'yi usulünce yedi kez dönmektir.
                """
            },
            "Mikat Sınırları ve İhram Hükümleri": {
                "pages": list(range(385, 395)),
                "summary": """
                **Mikat Sınırları:**
                - Mekke dışından (Afak bölgesinden) gelen hacı adaylarının ihramsız geçemeyeceği sınır kapılarıdır. Medine yönünden gelenler için Zülhuleyfe, Şam yönü için Cuhfe, Irak için Zât-ı Irk, Yemen için Yelemlem, Necid için Karnü'l-Menâzil'dir.
                
                **İhram Yasakları:**
                - Dikişli elbise, çorap, eldiven ve üzeri kapalı ayakkabı giymek (erkekler için).
                - Başını örtmek (erkekler için) veya yüzünü örtmek (kadınlar için).
                - Saç, sakal, bıyık veya vücut tüylerini kesmek ya da koparmak.
                - Tırnak kesmek.
                - Koku sürünmek, kokulu sabun kullanmak.
                - Cinsel ilişkide bulunmak veya buna yol açacak davranışlar yapmak.
                - Av hayvanı avlamak veya yeşil bitkileri koparmak.
                """
            },
            "Arafat Vakfesi ve Tavaf Çeşitleri": {
                "pages": list(range(395, 410)),
                "summary": """
                **Arafat Vakfesi:**
                - Haccın en önemli rüknüdür ("Hac Arafat'tır" hadisi gereği). Zilhicce'nin 9. günü (Arife günü) zeval vaktinden bayram sabahı tan yeri ağarana kadar olan sürede Arafat'ta bir an bile bulunmakla farz yerine gelir.
                
                **Tavaf Çeşitleri:**
                - **Kudüm Tavafı:** Mekke dışından gelenlerin yaptığı ilk tavaftır (Sünnettir).
                - **Ziyaret Tavafı:** Haccın rüknü olan farz tavaftır.
                - **Veda (Sader) Tavafı:** Hac ibadeti bitip Mekke'den ayrılırken yapılan son tavaftır (Mekke dışından gelenler için vaciptir).
                - **Umre Tavafı:** Umrenin rüknü olan tavaftır.
                """
            },
            "Hac Yasakları, Cezalar (Dem) ve Umre": {
                "pages": list(range(410, 425)),
                "summary": """
                **İhram Yasakları Cezaları:**
                - **Dem (Koyun veya Keçi Kesmek):** Bir gün boyunca dikişli elbise giymek, başı örtmek, saç veya sakalın dörtte birini tıraş etmek, koku sürünmek veya tırnakların tamamını kesmek durumunda vacip olan cezadır.
                - **Sadaka:** Yasakların daha kısa süreli ihlallerinde ödenen fıtır sadakası miktarı kefarettir.
                
                **Umre İbadeti:**
                - Hac mevsimi dışında ihrama girerek Kabe'yi tavaf etmek ve Safa ile Merve arasında sa'y edip tıraş olarak ihramdan çıkmaktır. Hanefi mezhebine göre ömürde bir defa umre yapmak **sünnet-i müekkededir**.
                """
            }
        }
    },
    "💍 Aile Hukuku (Nikah ve Talak)": {
        "start_page": 587,
        "end_page": 699,
        "description": "Nikah akdinin rükünleri, şahitlik, mehir, süt hısımlığı, boşanma (talak) yetkisi, iddet ve nafaka hükümleri.",
        "subtopics": {
            "Nikah Akdi, Rükünleri ve Şartları": {
                "pages": list(range(587, 598)),
                "summary": """
                **Nikah Akdinin Rükünleri:**
                - **İcap ve Kabul:** Evlenecek olan tarafların veya vekillerinin evlilik iradelerini beyan eden karşılıklı sözleridir.
                
                **Geçerlilik Şartları:**
                - Şahitlerin varlığı: En az 2 akil ve baliğ müslüman erkek veya 1 erkek 2 kadının nikah esnasında hazır bulunması şarttır. Şahitsiz nikah batıldır.
                - Evlenecek kişilerin evlenmelerine dinen bir engelin bulunmaması.
                - Tarafların rızasının bulunması.
                """
            },
            "Evlilik Engelleri (Mahremiyet)": {
                "pages": list(range(598, 608)),
                "summary": """
                **Evlilik Engelleri (Haram Olan Kadınlar):**
                1. **Kan Bağı (Nesep):** Anne, kız evlat, kız kardeş, hala, teyze, erkek ve kız kardeşlerin kızları ile evlenmek ebediyen haramdır.
                2. **Süt Bağı (Rada):** Süt anne, süt kız kardeş ve kan bağıyla haram olanların süt versiyonları. Hanefi mezhebinde emme süresi ilk 30 aydır (iki buçuk yaş). Bu süre içinde bir damla dahi emilse süt hısımlığı oluşur.
                3. **Sıhriyet (Evlilikten Doğan Hısımlık):** Kayınvalide, üvey kız (ilişki gerçekleştikten sonra), gelin ve üvey anne ile evlilik ebediyen haramdır.
                4. **Geçici Engeller:** Başkasıyla evli olmak, putperest olmak, üç talakla boşanıp iddet beklemek.
                """
            },
            "Kadının Hakları ve Mehir": {
                "pages": list(range(608, 620)),
                "summary": """
                **Kadının Evlilikteki Hakları:**
                - Nafaka (mesken, yiyecek, giyecek temini).
                - İyi geçim ve adalet (birden fazla eş durumunda).
                - Mehir hakkı.
                
                **Mehir Hükümleri:**
                - Kadının evlilik sebebiyle almaya hak kazandığı mali değerdir. Hanefi mezhebinde mehrin asgari miktarı 10 dirhemdir (yaklaşık 32 gram gümüş). Üst sınırı yoktur.
                - **Mehr-i Muaccel:** Evlilik anında peşin verilen mehir. Kadın bunu alana kadar kocasının evine gitmeme hakkına sahiptir.
                - **Mehr-i Müeccel:** Ödenmesi sonraya (boşanma veya vefata) ertelenen mehir.
                """
            },
            "Boşanma (Talak) Usulleri ve Çeşitleri": {
                "pages": list(range(637, 660)),
                "summary": """
                **Talak (Boşanma):**
                - Kocanın boşanma yetkisini kullanarak evlilik birliğini sona erdirmesidir. Toplam hak **3 talaktır**.
                - **Sarih Talak:** "Seni boşadım" gibi açık ifadelerle olur, niyet olmasa da boşanma gerçekleşir.
                - **Kinayeli Talak:** "Babanın evine git" gibi dolaylı ifadelerle olur, boşanma niyeti veya durumun karinesi şarttır.
                - **Rici Talak:** Erkeğin iddet süresinde yeni bir nikah yapmadan eşine dönebildiği boşanmadır (1 veya 2 açık boşama ile olur).
                - **Bain Talak:** Evliliğin hemen bittiği, geri dönmek için yeni bir nikahın gerektiği boşanmadır.
                """
            },
            "İddet Bekleme ve Nafaka Hükümleri": {
                "pages": list(range(660, 680)),
                "summary": """
                **İddet Nedir ve Süreleri Nelerdir?**
                - Evliliği sona eren kadının yeni bir evlilik yapabilmek için beklemesi gereken şer'i süredir.
                - **Boşanma İddeti:** Adet gören kadınlar için 3 hayız süresidir. Adet görmeyenler için 3 aydır.
                - **Ölüm İddeti:** Kocası vefat eden kadının bekleme süresi 4 ay 10 gündür.
                - **Hamilelik İddeti:** Hamile kadının iddeti doğum yapmasıyla (vaz-ı haml) sona erer.
                
                **İddet Nafakası:**
                - Boşanma iddeti bekleyen kadının nafaka ve barınma (mesken) ihtiyacını karşılamak kocanın yükümlülüğündedir. Ölüm iddeti bekleyen kadına nafaka verilmez, o mirastan hakkını alır.
                """
            }
        }
    },
    "⚖️ Ticaret ve Muamelat": {
        "start_page": 700,
        "end_page": 1054,
        "description": "Alışveriş akitleri, faiz (riba) yasağı, ortaklık çeşitleri, kısıtlılık (hacr) ve vakıf kurma kuralları.",
        "subtopics": {
            "Alışveriş Akdinin Şartları ve Türleri": {
                "pages": list(range(700, 715)),
                "summary": """
                **Alışverişin Rükünleri:**
                - İcap ve kabul (satıcı ve alıcının karşılıklı rızalarını beyan etmesi).
                
                **Geçerlilik Şartları:**
                - Tarafların akil ve baliğ olması (veya mümeyyiz küçüğün veli izinli olması).
                - Satılan malın dinen değerli (mütekavvim) olması, mevcut olması ve tesliminin mümkün olması. Domuz, içki gibi haram maddeler ticarete konu olamaz.
                - Akitte faiz, aldatma (hile) veya aşırı belirsizlik (garar) bulunmamalıdır.
                """
            },
            "Faiz (Riba) Yasağı ve Çeşitleri": {
                "pages": list(range(740, 755)),
                "summary": """
                **Faiz (Riba) Tanımı ve Hükmü:**
                - Karşılıksız fazlalık içeren her türlü borç veya mal değişimi faizdir ve haramdır.
                
                **Çeşitleri:**
                1. **Riba el-Fadl (Fazlalık Faizi):** Aynı cinsten ölçülebilen (keyli) veya tartılabilen (vezni) iki malın (örneğin altın ile altının) peşin değişiminde ortaya çıkan miktar fazlalığıdır. Eşit olmak zorundadır.
                2. **Riba en-Nesie (Vade Faizi):** Vadeli değişimde vadeden dolayı alınan fazlalıktır.
                - "Altın altınla, gümüş gümüşle, buğday buğdayla, arpa arpayla, hurma hurmayla, tuz tuzla eşit ve peşin olarak değiştirilmelidir" hadisi faizin temelidir.
                """
            },
            "Borçlanma, Kefalet ve Ortaklık Çeşitleri": {
                "pages": list(range(760, 790)),
                "summary": """
                **Borçlanma ve Karz:**
                - Geri ödenmek üzere verilen tüketim ödüncüdür. Borç sözleşmelerinde herhangi bir menfaat veya fazlalık şart koşulursa bu faiz olur.
                
                **Kefalet:**
                - Bir kimsenin borcunu veya şahsını teslim etmeyi kendi üzerine almasıdır. Borçlunun borcu kefilden talep edilebilir.
                
                **Ortaklık (Şirket) Türleri:**
                - **Mufavada Şirketi:** Ortakların sermaye, tasarruf yetkisi ve kar-zararda tamamen eşit olduğu ortaklıktır.
                - **İnan Şirketi:** Ortakların eşit olması şart olmayan, sermaye miktarlarına göre kar paylaşımı yapılan adi ortaklıktır.
                """
            },
            "Vakıf Hukuku": {
                "pages": list(range(995, 1010)),
                "summary": """
                **Vakıf Akdinin Mahiyeti:**
                - Bir malın mülkiyetinin Allah'ın mülkü hükmünde olmak üzere ebedi olarak menfaatlerinin hayır yollarına tahsis edilmesidir.
                
                **Vakfın Şartları:**
                - Vakfedilen malın gayrimenkul olması esastır. Taşınır mallar ancak örfen kabul görüyorsa (kitap, alet vb.) vakfedilebilir.
                - Vakıf ebedi olmalıdır; geçici vakıf kurulamaz.
                - **Bağlayıcılık:** Ebu Hanife'ye göre vakıf bağlayıcı değildir; vakıf kuran hayattayken rücu edebilir. Ancak İmameyn'e (Ebu Yusuf ve İmam Muhammed) göre vakıf tescil edilince bağlayıcı olur ve geri dönülemez. Hanefi mezhebinde fetva İmameyn'in görüşüne göredir.
                """
            }
        }
    },
    "🐑 Kurban ve Avcılık": {
        "start_page": 1055,
        "end_page": 1114,
        "description": "Kurban ibadetinin vacip olma şartları, kurbanlık hayvanların vasıfları ve İslami kesim kuralları.",
        "subtopics": {
            "Kurban İbadetinin Şartları ve Vakti": {
                "pages": list(range(1055, 1062)),
                "summary": """
                **Kurbanın Hükmü:**
                - Hanefi mezhebine göre mukim, hür, akıllı, baliğ ve temel ihtiyaçları dışında nisap miktarı (80.18 gram altın) mala sahip olan her müslümana bayramda kurban kesmek **vaciptir**.
                
                **Kurban Kesim Vakti:**
                - Kurban Bayramı'nın 1. günü bayram namazından sonra başlar, 3. günü akşam güneş batana kadar devam eder. Gece kurban kesmek mekruhtur.
                """
            },
            "Kurbanlık Hayvanlar ve Ortaklık Şartları": {
                "pages": list(range(1062, 1075)),
                "summary": """
                **Kurban Olabilecek Hayvanlar:**
                - Koyun ve Keçi: En az 1 yaşını doldurmuş olmalıdır (koyun 6 aylık olup annesi gibi iri duruyorsa kesilebilir). Sadece 1 kişi adına kesir.
                - Sığır ve Manda: En az 2 yaşını doldurmuş olmalıdır. 1 ila 7 kişi ortaklaşa kesebilir.
                - Deve: En az 5 yaşını doldurmuş olmalıdır. 1 ila 7 kişi ortaklaşa kesebilir.
                
                **Ortaklık Şartları:**
                - Büyükbaş hayvana ortak olanların hepsinin niyetinin ibadet (kurban, adak, akika) olması şarttır. İçlerinden biri et amacıyla ortak olursa hiçbirinin kurbanı geçerli olmaz.
                """
            },
            "İslami Kesim Kuralları ve Avcılık": {
                "pages": list(range(1075, 1100)),
                "summary": """
                **Kesim Kuralları (Zebh):**
                - Hayvanın keskin bir bıçakla eziyet edilmeden kesilmesi sünnettir.
                - Kesim esnasında besmele çekilmesi ("Bismillahi Allahu Ekber" denmesi) **şarttır**. Bilerek besmele terk edilirse hayvanın eti Hanefi mezhebine göre haram olur (unutarak terk edilirse helaldir).
                - Hayvanın nefes borusu, yemek borusu ve iki şah damarının (veya en az birinin) kesilmesi gerekir.
                
                **Avcılık Hükümleri:**
                - Av aleti atılırken veya av köpeği salınırken besmele çekilmesi şarttır.
                - Eğitilmiş av köpeğinin avı öldürmesi helaldir, ancak köpek avdan kendisi yemişse o av yenilmez (köpeğin kendisi için avlandığı anlaşılır).
                """
            }
        }
    },
    "📜 Vasiyet ve Miras (Feraiz)": {
        "start_page": 1115,
        "end_page": 1179,
        "description": "Vasiyet sınırları, mirasın taksimi, pay sahipleri (Ashabü'l-Feraiz) ve engelleri.",
        "subtopics": {
            "Vasiyetin Hükmü ve Sınırları (1/3)": {
                "pages": list(range(1115, 1125)),
                "summary": """
                **Vasiyetin Mahiyeti:**
                - Bir kimsenin ölümünden sonrası için malında bağışlama yoluyla tasarruf etmesidir.
                
                **Sınırları:**
                - Kişi mal varlığının en fazla **üçte birini (1/3)** vasiyet edebilir. Bundan fazlasını vasiyet ederse, vasiyet ancak mirasçıların ölümden sonraki rızalarıyla geçerli olur.
                - **Mirasçıya Vasiyet Yoktur:** Yasal mirasçılardan birine vasiyet yapılamaz. Diğer mirasçılar izin vermedikçe bu vasiyet geçersiz kalır.
                """
            },
            "Miras Paylaşımı (Ashabü'l-Feraiz ve Asabe)": {
                "pages": list(range(1125, 1150)),
                "summary": """
                **Mirasçı Sınıfları:**
                1. **Ashabü'l-Feraiz:** Kur'an'da payları (1/2, 1/4, 1/8, 2/3, 1/3, 1/6) belirlenmiş olanlar (Eşler, anne, baba, kız evlatlar vb.).
                2. **Asabe:** Pay sahiplerinden artan miktarı alan erkek akrabalar.
                
                **Temel Hükümler:**
                - Erkek çocuğun payı kız çocuğun iki katıdır.
                - Çocuk olduğunda eşlerin payları düşer (kocanın payı 1/2'den 1/4'e, kadının payı 1/4'ten 1/8'e iner).
                - **Engeller:** Murisini öldüren katil mirasçı olamaz. Müslüman ile gayrimüslim birbirine mirasçı olamaz.
                """
            }
        }
    }
}

FAQ_DATA = [
    # TAHARAT (10 Fetva)
    {
        "soru": "Diş kanaması abdesti bozar mı?",
        "kategori": "💧 Temizlik (Taharet)",
        "cevap": "Hanefi mezhebine göre tükürükteki kan, tükürüğe eşit veya tükürükten fazla ise abdesti bozar. Eğer kan sarı/açık renkli olup tükürükten az ise abdesti bozmaz.",
        "sayfa": 72
    },
    {
        "soru": "Vücuttan çıkan ve akmayan kan abdesti bozar mı?",
        "kategori": "💧 Temizlik (Taharet)",
        "cevap": "Vücuttan çıkan kan, çıktığı yerin dışına taşmadığı veya akmadığı sürece abdesti bozmaz. Nokta halinde kalan kan abdesti bozmaz.",
        "sayfa": 73
    },
    {
        "soru": "Ağız dolusu kusmak abdesti bozar mı?",
        "kategori": "💧 Temizlik (Taharet)",
        "cevap": "Evet, ağız dolusu (kişinin zorlanmadan ağzında tutamayacağı miktarda) kusmak abdesti bozar. Kusmuk yemek, su veya safra olabilir.",
        "sayfa": 74
    },
    {
        "soru": "Uyuklamak veya yaslanarak uyumak abdesti bozar mı?",
        "kategori": "💧 Temizlik (Taharet)",
        "cevap": "Namaz kılarken ayakta veya rükûda uyumak abdesti bozmaz. Ancak yan yatarak veya bir yere dayanıp, dayandığı şey çekildiğinde düşecek derecede uyumak bilinci yok ettiği için abdesti bozar.",
        "sayfa": 76
    },
    {
        "soru": "Namazda sesli gülmek abdesti bozar mı?",
        "kategori": "💧 Temizlik (Taharet)",
        "cevap": "Evet, rükûlu secdeli bir namazda yanındakilerin duyacağı kadar sesli gülmek (kahkaha) hem namazı hem de abdesti bozar. Cenaze namazında ve secde-i tilavette ise sadece namazı bozar, abdesti bozmaz.",
        "sayfa": 78
    },
    {
        "soru": "Gusül abdestinde göbek deliğini yıkamak farz mıdır?",
        "kategori": "💧 Temizlik (Taharet)",
        "cevap": "Evet, gusülde vücudun dış kısmında yer alan ve yıkanması mümkün olan her noktanın ıslanması farzdır. Göbek deliğinin içi de buna dahildir, kuru kalırsa gusül geçerli olmaz.",
        "sayfa": 82
    },
    {
        "soru": "Ağız ve burun yıkanmadan yapılan gusül geçerli midir?",
        "kategori": "💧 Temizlik (Taharet)",
        "cevap": "Hanefi mezhebine göre gusülde ağza su vermek (mazmaza) ve burna su çekmek (istinşak) farzdır. Bu sebeple ağız ve burun yıkanmadan yapılan gusül geçerli olmaz.",
        "sayfa": 85
    },
    {
        "soru": "Teyemmümde elleri toprağa vururken niyet şart mıdır?",
        "kategori": "💧 Temizlik (Taharet)",
        "cevap": "Evet, teyemmümde niyet farzdır. Niyet etmeksizin sadece toprağa dokunmak veya tozlanmak teyemmüm yerine geçmez. Kişinin abdest veya gusül yerine teyemmüm etmeye niyet etmesi gerekir.",
        "sayfa": 98
    },
    {
        "soru": "Mest üzerine yapılan meshin süresi ne zaman başlar?",
        "kategori": "💧 Temizlik (Taharet)",
        "cevap": "Mesh süresi, mestin giyildiği andan itibaren değil, mest giyildikten sonra abdestin ilk bozulduğu andan itibaren başlar. Mukimler için 24 saat, seferiler için 72 saattir.",
        "sayfa": 110
    },
    {
        "soru": "Tırnaktaki oje abdest veya gusle engel midir?",
        "kategori": "💧 Temizlik (Taharet)",
        "cevap": "Oje, suyun tırnak dokusuna ulaşmasını engelleyen kalın bir tabaka oluşturduğu için abdest ve gusle engeldir. Abdest veya gusül almadan önce tamamen temizlenmesi gerekir.",
        "sayfa": 125
    },

    # NAMAZ (15 Fetva)
    {
        "soru": "Namaz kılarken gözleri yummak caiz midir?",
        "kategori": "🕌 Namaz (Salat)",
        "cevap": "Namazda gözleri yummak tenzihen mekruhtur. Ancak kişinin namazda huşuyu yakalaması veya zihnini dağıtan bir şeyi görmemesi amacıyla gözlerini yumması mekruh sayılmamıştır.",
        "sayfa": 150
    },
    {
        "soru": "Namazda Fatiha suresinden sonra sure okumayı unutursak ne gerekir?",
        "kategori": "🕌 Namaz (Salat)",
        "cevap": "Fatiha'dan sonra zamm-ı sure okumak vaciptir. Unutulması halinde namazın sonunda sehiv secdesi yapılması vacip olur. Eğer bilerek terk edilirse namazın iadesi gerekir.",
        "sayfa": 170
    },
    {
        "soru": "Secde esnasında burnun yere değmesi farz mıdır?",
        "kategori": "🕌 Namaz (Salat)",
        "cevap": "Secdede alnı yere koymak farz, burnu yere koymak ise vaciptir. Bir mazeret olmaksızın burnun yere konulmaması mekruhtur; ancak alın yere konmuşsa namaz geçerlidir.",
        "sayfa": 166
    },
    {
        "soru": "Namazda esnemek namazı bozar mı?",
        "kategori": "🕌 Namaz (Salat)",
        "cevap": "Namazda esnemek namazı bozmaz ancak mekruhtur. Esneme geldiğinde kişi eliyle ağzını kapatmalı ve bunu engellemeye çalışmalıdır.",
        "sayfa": 178
    },
    {
        "soru": "Namazda aklımıza gelen dünyevi düşünceler namazı bozar mı?",
        "kategori": "🕌 Namaz (Salat)",
        "cevap": "Namaz esnasında akla gelen vesvese ve dünyevi düşünceler namazı bozmaz. Ancak namazın sevabını ve huşusunu azaltır. Kişi bu düşüncelerden uzaklaşmaya gayret etmelidir.",
        "sayfa": 182
    },
    {
        "soru": "Cemaatle namaz kılarken cemaatin de Fatiha okuması gerekir mi?",
        "kategori": "🕌 Namaz (Salat)",
        "cevap": "Hanefi mezhebine göre imama uyan cemaatin (muktedi) içinden Fatiha veya başka bir sure okuması mekruhtur. Cemaat sessizce durup imamı dinler. İmamın okuması cemaatin de okuması yerine geçer.",
        "sayfa": 188
    },
    {
        "soru": "Yolculukta namazları kısaltmak isteğe bağlı mıdır?",
        "kategori": "🕌 Namaz (Salat)",
        "cevap": "Hanefi mezhebine göre seferi iken 4 rekatlı farz namazları 2 rekat kılmak vaciptir. Bilerek ve mazeretsiz 4 rekat kılmak mekruhtur. Yani kısaltma isteğe bağlı bir ruhsat değil, şer'i bir zorunluluktur.",
        "sayfa": 198
    },
    {
        "soru": "Tilavet secdesi yaparken selam verilir mi?",
        "kategori": "🕌 Namaz (Salat)",
        "cevap": "Namaz dışındaki tilavet secdesinde secde yapıldıktan sonra doğrulurken selam verilmez. Doğrudan secdeye gidilir, secde yapıldıktan sonra tekbirle ayağa kalkılır.",
        "sayfa": 210
    },
    {
        "soru": "Hutbe okunurken konuşmak veya namaz kılmak caiz midir?",
        "kategori": "🕌 Namaz (Salat)",
        "cevap": "İmam hutbeye çıktığı andan itibaren cemaatin konuşması, selam alıp vermesi veya nafile namaz kılması tahrimen mekruhtur. Cemaat sadece hutbeyi dinlemelidir.",
        "sayfa": 220
    },
    {
        "soru": "Kaza namazları için belirli bir vakit var mıdır?",
        "kategori": "🕌 Namaz (Salat)",
        "cevap": "Hayır, kaza namazları üç kerahat vakti (güneşin doğuşu, batışı ve tam tepedeyken) dışında her zaman kılınabilir. Belirli bir güne veya saate bağlı değildir.",
        "sayfa": 235
    },
    {
        "soru": "Vitir namazında Kunut tekbirini ve duasını unutursak ne gerekir?",
        "kategori": "🕌 Namaz (Salat)",
        "cevap": "Vitir namazında Kunut tekbiri almak ve duayı okumak vaciptir. Unutulduğunda namazın sonunda sehiv secdesi yapılması gerekir.",
        "sayfa": 172
    },
    {
        "soru": "Seferilikte mesafe hesabı kuş uçuşu mu yoksa yol mesafesi mi esas alınır?",
        "kategori": "🕌 Namaz (Salat)",
        "cevap": "Seferilikte kişinin gideceği yol mesafesi (karayolu veya kullanılan güzergah) esas alınır, kuş uçuşu mesafe dikkate alınmaz. Bu mesafenin en az 90 km olması gerekir.",
        "sayfa": 196
    },
    {
        "soru": "Namaz kılan birinin önünden geçmek namazı bozar mı?",
        "kategori": "🕌 Namaz (Salat)",
        "cevap": "Namaz kılan birinin önünden geçmek namazı bozmaz. Ancak geçen kişi günahkar olur. Namaz kılan kişinin açık alanda önüne sütre koyması sünnettir.",
        "sayfa": 184
    },
    {
        "soru": "Ta'dil-i erkanı terk etmek namazı bozar mı?",
        "kategori": "🕌 Namaz (Salat)",
        "cevap": "Hanefi mezhebinin hakim görüşüne (Ebu Hanife ve İmam Muhammed) göre ta'dil-i erkan vaciptir. Terk edilmesi namazı bozmaz ama sehiv secdesi gerektirir. Ebu Yusuf'a göre ise farzdır, terk edilirse namaz bozulur.",
        "sayfa": 168
    },
    {
        "soru": "Cenaze namazında rükû ve secde var mıdır?",
        "kategori": "🕌 Namaz (Salat)",
        "cevap": "Hayır, cenaze namazı rükûsuz ve secdesiz olarak ayakta kılınan bir namazdır. Dört tekbir ve kıyamdan ibarettir.",
        "sayfa": 228
    },

    # ZEKAT (10 Fetva)
    {
        "soru": "Borçlu olan bir kimsenin zekat vermesi gerekir mi?",
        "kategori": "🌾 Zekat ve Fıtır Sadakası",
        "cevap": "Kişinin elindeki maldan borçları düşülür. Kalan miktar nisap miktarına (80.18 gram altın değerine) ulaşmıyorsa o kimseye zekat farz olmaz.",
        "sayfa": 305
    },
    {
        "soru": "Temel ihtiyaç sınırına (Havaic-i Asliye) neler girer?",
        "kategori": "🌾 Zekat ve Fıtır Sadakası",
        "cevap": "Kişinin oturduğu ev, ev eşyası, binek arabası, kışlık ve yazlık elbiseleri, mesleki aletleri ve bir yıllık nafaka miktarı temel ihtiyaçtır; bunlardan zekat verilmez.",
        "sayfa": 308
    },
    {
        "soru": "Zekatı gayrimüslim bir ihtiyaç sahibine vermek caiz midir?",
        "kategori": "🌾 Zekat ve Fıtır Sadakası",
        "cevap": "Hanefi mezhebine göre farz olan zekat ve vacip olan fitre sadece müslüman fakirlere verilebilir, gayrimüslimlere verilemez. Gayrimüslimlere ancak nafile sadakalar verilebilir.",
        "sayfa": 338
    },
    {
        "soru": "Bir kimse kendi kayınvalidesine zekat verebilir mi?",
        "kategori": "🌾 Zekat ve Fıtır Sadakası",
        "cevap": "Evet, kayınvalide kişinin usûl (anne-baba) veya fürûundan (çocuklar) olmadığı için fakir olması halinde ona zekat verilebilir. Ancak eşe zekat verilemez.",
        "sayfa": 340
    },
    {
        "soru": "Kira geliri getiren dairelerin zekatı nasıl hesaplanır?",
        "kategori": "🌾 Zekat ve Fıtır Sadakası",
        "cevap": "Kira getiren dairelerin bina değeri üzerinden zekat verilmez. Sadece bu dairelerden elde edilen kira gelirleri diğer birikimlerle birleştirilerek nisaba ulaşıyorsa %2.5 oranında zekatı verilir.",
        "sayfa": 318
    },
    {
        "soru": "Öşür (toprak ürünleri zekatı) verilirken masraflar düşülür mi?",
        "kategori": "🌾 Zekat ve Fıtır Sadakası",
        "cevap": "Ebu Hanife'ye göre toprak ürünlerinde gübre, mazot, işçilik gibi masraflar mahsulden düşülmeden toplam ürün üzerinden öşür verilir. Ancak sulama masrafı varsa oran %10 yerine %5 olarak uygulanır.",
        "sayfa": 322
    },
    {
        "soru": "Alacaklı olunan ama tahsil edilemeyen paranın zekatı verilir mi?",
        "kategori": "🌾 Zekat ve Fıtır Sadakası",
        "cevap": "Geri alınması ümit edilen güçlü alacakların zekatı, tahsil edildikten sonra geçmiş yıllar dahil hesaplanarak ödenir. Tahsilinden ümit kesilen alacakların zekatı ise farz değildir.",
        "sayfa": 314
    },
    {
        "soru": "Çocuğun veya akıl hastasının malından zekat verilir mi?",
        "kategori": "🌾 Zekat ve Fıtır Sadakası",
        "cevap": "Hanefi mezhebine göre çocukların ve akıl hastalarının mallarından zekat verilmesi farz değildir. Velileri onun mallarından zekat ödemekle yükümlü tutulmamıştır (Şafii'nin aksine).",
        "sayfa": 304
    },
    {
        "soru": "Fıtır sadakası (fitre) ne zamana kadar ödenmelidir?",
        "kategori": "🌾 Zekat ve Fıtır Sadakası",
        "cevap": "Fitrenin vacip olma vakti bayram sabahıdır. Bayram namazından önce verilmesi müstehaptır. Bayram günü veya sonrasında da kaza olarak ödenebilir ancak geciktirilmesi mekruhtur.",
        "sayfa": 334
    },
    {
        "soru": "Zekat verirken fakire bunun zekat olduğunu söylemek şart mıdır?",
        "kategori": "🌾 Zekat ve Fıtır Sadakası",
        "cevap": "Hayır, zekat verirken niyetin kalben zekat olması yeterlidir. Karşı tarafa rencide olmaması için borç ödeme, hediye veya bayramlık adı altında verilmesi caizdir.",
        "sayfa": 336
    },

    # ORUÇ (10 Fetva)
    {
        "soru": "Unutarak yiyip içtikten sonra orucun bozulduğunu sanarak yemeye devam edene ne gerekir?",
        "kategori": "🌙 Oruç (Savm)",
        "cevap": "Unutarak yemek orucu bozmaz. Ancak kişi bozulduğunu zannederek bilerek yemeye devam ederse orucu bozulur ve gününe gün kaza etmesi gerekir (kefaret gerekmez).",
        "sayfa": 362
    },
    {
        "soru": "İlaç veya gıda takviyesi amaçlı iğne (enjeksiyon) yaptırmak orucu bozar mı?",
        "kategori": "🌙 Oruç (Savm)",
        "cevap": "Besleyici veya vitamin içerikli aşı ve iğneler orucu bozar ve kaza gerektirir. Gıda amacı taşımayan sadece tedavi amaçlı ağrı kesici iğneler ise orucu bozmaz.",
        "sayfa": 366
    },
    {
        "soru": "Oruçlu iken diş fırçalamak orucu bozar mı?",
        "kategori": "🌙 Oruç (Savm)",
        "cevap": "Macun kullanmadan veya macunun boğaza kaçma riski olmaksızın fırçalamak orucu bozmaz ancak macun kullanmak mekruhtur. Macun veya su boğaza kaçarsa oruç bozulur ve kaza gerekir.",
        "sayfa": 368
    },
    {
        "soru": "Göze damla damlatmak veya sürme çekmek orucu bozar mı?",
        "kategori": "🌙 Oruç (Savm)",
        "cevap": "Hayır, göze damlatılan ilaç veya sürme gözenekler yoluyla boğaza ulaşsa ve tadı hissedilse bile orucu bozmaz. Çünkü göz doğal bir beslenme kanalı değildir.",
        "sayfa": 365
    },
    {
        "soru": "Oruç tutamayacak kadar yaşlı veya hasta olanlar ne yapmalıdır?",
        "kategori": "🌙 Oruç (Savm)",
        "cevap": "Oruç tutmaya gücü yetmeyen yaşlılar ve iyileşme ümidi olmayan hastalar tutamadıkları her gün için bir fidye (bir fakiri bir gün doyuracak miktar veya fitre miktarı nakit) verirler.",
        "sayfa": 370
    },
    {
        "soru": "Astım hastalarının kullandığı sprey orucu bozar mı?",
        "kategori": "🌙 Oruç (Savm)",
        "cevap": "Ağızdan püskürtülen astım spreyi içeriğindeki ilaç parçacıklarının mideye ulaşması sebebiyle orucu bozar. Bu kişilerin fidye vermesi veya iyileşme durumunda kaza etmesi gerekir.",
        "sayfa": 364
    },
    {
        "soru": "Kaza orucu için gündüz niyet edilebilir mi?",
        "kategori": "🌙 Oruç (Savm)",
        "cevap": "Hayır, kaza orucu, keffaret orucu ve mutlak adak oruçları için imsaktan önce (geceden) niyet edilmesi şarttır. Gündüz yapılan niyet bu oruçlar için geçerli değildir.",
        "sayfa": 354
    },
    {
        "soru": "Kusmak hangi durumlarda orucu bozar?",
        "kategori": "🌙 Oruç (Savm)",
        "cevap": "Kişinin kendi isteği dışında kendiliğinden kusması ne kadar olursa olsun orucu bozmaz. Ancak kendi isteğiyle parmak atarak ağız dolusu kusarsa oruç bozulur ve kaza gerekir.",
        "sayfa": 360
    },
    {
        "soru": "Diş kanamasında akan kanı yutmak orucu bozar mı?",
        "kategori": "🌙 Oruç (Savm)",
        "cevap": "Evet, diş etinden çıkan kan tükürükten fazla veya tükürüğe eşit miktarda olur ve yutulursa oruç bozulur ve kaza gerekir. Tükürükten az ise bozmaz.",
        "sayfa": 361
    },
    {
        "soru": "Sahurda ezan okunurken yemeye devam edilebilir mi?",
        "kategori": "🌙 Oruç (Savm)",
        "cevap": "Ezan, imsak vaktinin girdiğini ilan etmek için okunur. Bu sebeple ezan başladığı an yeme ve içmeyi hemen kesmek gerekir. Ezan okunurken yutulan şey orucu bozar ve kaza gerektirir.",
        "sayfa": 353
    },

    # HAC (10 Fetva)
    {
        "soru": "Kadınların tek başına hacca gitmesi caiz midir?",
        "kategori": "🕋 Hac ve Umre",
        "cevap": "Hanefi mezhebine göre Mekke'ye olan mesafe seferilik mesafesinden (90 km) fazla ise kadının yanında kocası veya evlenmesi ebediyen haram olan bir mahremi (oğlu, kardeşi vb.) bulunmadıkça hacca gitmesi caiz değildir.",
        "sayfa": 378
    },
    {
        "soru": "Arafat vakfesini kaçıran bir hacı ne yapmalıdır?",
        "kategori": "🕋 Hac ve Umre",
        "cevap": "Arafat vakfesi haccın en önemli rüknüdür. Arife günü zevalden bayram sabahına kadar vakfe yapamayan kişi o yılki haccı kaçırmış olur. Umre yaparak ihramdan çıkar ve sonraki yıllarda haccını kaza eder.",
        "sayfa": 396
    },
    {
        "soru": "İhramda iken dikişli terlik giyilebilir mi?",
        "kategori": "🕋 Hac ve Umre",
        "cevap": "Erkekler ihramda iken topukları ve üzerini kapatmayan, dikişsiz veya az dikişli açık terlik giymelidir. Tamamen kapalı dikişli ayakkabı giymek yasaktır ve ceza gerektirir.",
        "sayfa": 390
    },
    {
        "soru": "Hacda veda tavafı kimlere vaciptir?",
        "kategori": "🕋 Hac ve Umre",
        "cevap": "Mekke dışından (Mikat sınırlarının dışından) gelen tüm hacılara (Afakilere) veda tavafı yapmak vaciptir. Mekke içinde ikamet edenlere ise vacip değildir.",
        "sayfa": 405
    },
    {
        "soru": "Umre ibadetinin farzları nelerdir?",
        "kategori": "🕋 Hac ve Umre",
        "cevap": "Umrenin iki farzı vardır: İhrama girmek (Şart) ve Kabe'yi tavaf etmek (Rükün). Sa'y etmek ve tıraş olmak ise umrenin vaciplerindendir.",
        "sayfa": 420
    },
    {
        "soru": "İhram yasaklarından dolayı kesilmesi gereken kurban nerede kesilir?",
        "kategori": "🕋 Hac ve Umre",
        "cevap": "Caza kurbanlarının (Dem) Harem bölgesinde (Mekke sınırları içinde) kesilmesi şarttır. Başka ülkelerde veya bölgelerde kesilen ceza kurbanları geçerli olmaz.",
        "sayfa": 412
    },
    {
        "soru": "Mikat sınırını ihramsız geçen kişi ne yapmalıdır?",
        "kategori": "🕋 Hac ve Umre",
        "cevap": "Mikat sınırını ihramsız geçen kişinin geri dönüp mikatta ihrama girmesi gerekir. Eğer dönmeden ihrama girerse ceza olarak bir koyun veya keçi (Dem) kesmesi vacip olur.",
        "sayfa": 388
    },
    {
        "soru": "Hac kurbanı (Hedy) ile normal kurban aynı mıdır?",
        "kategori": "🕋 Hac ve Umre",
        "cevap": "Hayır, Hac kurbanı (Hedy), Kıran veya Temettü haccı yapanların kestikleri şükür kurbanıdır ve Harem bölgesinde kesilir. Normal kurban (Udhiyye) ise bayram günlerinde nisap sahibi her mükellefin kestiği kurbandır.",
        "sayfa": 402
    },
    {
        "soru": "Tavaf esnasında abdesti bozulan ne yapmalıdır?",
        "kategori": "🕋 Hac ve Umre",
        "cevap": "Tavafta abdestli olmak vaciptir. Tavaf yaparken abdesti bozulan kişi tavafı bırakıp abdest alır ve kaldığı şavttan (dönüşten) devam eder. Baştan başlaması da caizdir.",
        "sayfa": 408
    },
    {
        "soru": "Sa'y ibadeti Kabe'nin neresinde yapılır?",
        "kategori": "🕋 Hac ve Umre",
        "cevap": "Sa'y, Kabe'nin hemen yanındaki Safa ve Merve tepeleri arasındaki özel yolda (Mes'a) yapılır. Safa'dan başlanıp Merve'de bitirilir (4 gidiş 3 geliş olmak üzere 7 şavttır).",
        "sayfa": 400
    },

    # AİLE (10 Fetva)
    {
        "soru": "Bir erkek karısını 3 talakla birden boşarsa ne olur?",
        "kategori": "💍 Aile Hukuku (Nikah ve Talak)",
        "cevap": "Hanefi mezhebine göre tek mecliste söylenen 'Seni 3 talakla boşadım' sözüyle 3 talak birden gerçekleşir ve evlilik tamamen biter. Çiftlerin tekrar evlenmesi hülle şartına bağlı hale gelir.",
        "sayfa": 645
    },
    {
        "soru": "Süt hısımlığının oluşması için çocuğun ne kadar emmesi gerekir?",
        "kategori": "💍 Aile Hukuku (Nikah ve Talak)",
        "cevap": "Hanefi mezhebine göre ilk 30 ay (iki buçuk yaş) içinde bir damla dahi olsa sütün mideye ulaşmasıyla süt hısımlığı oluşur. Miktar şartı aranmaz.",
        "sayfa": 602
    },
    {
        "soru": "Mehirsiz kıyılan nikah geçerli midir?",
        "kategori": "💍 Aile Hukuku (Nikah ve Talak)",
        "cevap": "Evet, nikah esnasında mehir belirlenmemiş veya mehir verilmeyeceği şart koşulmuş olsa bile nikah geçerlidir. Ancak kadın mehr-i misil (akranlarının aldığı mehir) almaya hak kazanır.",
        "sayfa": 612
    },
    {
        "soru": "Geçici nikah (mut'a nikahı) caiz midir?",
        "kategori": "💍 Aile Hukuku (Nikah ve Talak)",
        "cevap": "Hayır, belirli bir süreyle sınırlandırılarak kıyılan mut'a veya muvakkat nikahlar Hanefi mezhebine ve ehl-i sünnete göre batıldır, geçersizdir.",
        "sayfa": 595
    },
    {
        "soru": "Boşanan kadının iddet süresi ne kadardır?",
        "kategori": "💍 Aile Hukuku (Nikah ve Talak)",
        "cevap": "Adet gören kadınlar için iddet süresi 3 temizlik dönemi değil, 3 adet (hayız) süresidir. Adet görmeyenler için 3 ay, hamileler için ise doğum yapmaktır.",
        "sayfa": 662
    },
    {
        "soru": "Kocası vefat eden kadının iddet süresi ne kadardır?",
        "kategori": "💍 Aile Hukuku (Nikah ve Talak)",
        "cevap": "Kocası vefat eden kadının iddet süresi hamile değilse 4 ay 10 gündür. Bu süre içinde kadının süslenmesi ve evlilik teklifi alması yasaktır.",
        "sayfa": 665
    },
    {
        "soru": "Nikahta şahitlerin müslüman olması şart mıdır?",
        "kategori": "💍 Aile Hukuku (Nikah ve Talak)",
        "cevap": "Evet, nikah şahitlerinin akil, baliğ ve müslüman olması şarttır. Gayrimüslimlerin şahitliği ile kıyılan nikah geçersizdir.",
        "sayfa": 590
    },
    {
        "soru": "Mahkeme yoluyla boşanan çiftler dinen de boşanmış sayılır mı?",
        "kategori": "💍 Aile Hukuku (Nikah ve Talak)",
        "cevap": "Diyanet İşleri Başkanlığı ve Hanefi fıkhı kurullarının görüşüne göre, resmi mahkemenin boşanma kararı vermesi dinen de 1 bain talak hükmünde boşanma yerine geçer.",
        "sayfa": 655
    },
    {
        "soru": "Üvey kız kardeşle evlenmek caiz midir?",
        "kategori": "💍 Aile Hukuku (Nikah ve Talak)",
        "cevap": "Hayır, üvey kız kardeşle (anne veya babadan biri ortak olan) evlenmek kesinlikle haramdır. Sadece üvey babanın önceki eşinden olan kızı (hiçbir kan veya süt bağı yoksa) ile evlenilebilir.",
        "sayfa": 600
    },
    {
        "soru": "Kadın mehir hakkından vazgeçebilir mi?",
        "kategori": "💍 Aile Hukuku (Nikah ve Talak)",
        "cevap": "Evet, kadın nikah kıyıldıktan sonra veya evlilik sürecinde mehir hakkının tamamından veya bir kısmından kendi rızasıyla vazgeçebilir veya kocasına bağışlayabilir.",
        "sayfa": 618
    },

    # TİCARET (5 Fetva)
    {
        "soru": "Altının altınla vadeli satışı caiz midir?",
        "kategori": "⚖️ Ticaret ve Muamelat",
        "cevap": "Hayır, sarrafiye işlemlerinde altın altınla veya altın gümüşle değiştirilirken işlemin peşin ve elden ele (kabz) yapılması şarttır. Vadeli altın satışı faiz (nesie ribası) kapsamına girer.",
        "sayfa": 745
    },
    {
        "soru": "Kaparo almak caiz midir?",
        "kategori": "⚖️ Ticaret ve Muamelat",
        "cevap": "Evet, yapılan alışveriş sözleşmesinden cayılması halinde geri ödenmek veya fiyattan düşülmek üzere kaparo alınması dinen caizdir.",
        "sayfa": 712
    },
    {
        "soru": "Enflasyon farkını borç ödemesinde talep etmek faiz midir?",
        "kategori": "⚖️ Ticaret ve Muamelat",
        "cevap": "Borç verilen paranın değer kaybını (enflasyon oranındaki değer kaybını) borçludan talep etmek faiz değildir. Bu durum kul hakkı ve adaletin gereğidir.",
        "sayfa": 765
    },
    {
        "soru": "Borsadan hisse senedi almak caiz midir?",
        "kategori": "⚖️ Ticaret ve Muamelat",
        "cevap": "Hisse senedi alınan şirketin faaliyet alanı dinen haram işlerle (alkol, faizli bankacılık, domuz eti üretimi vb.) ilgili değilse ve şirket gerçek bir varlığa sahipse hisse senedi alıp satmak caizdir.",
        "sayfa": 720
    },
    {
        "soru": "Vakfedilen bir gayrimenkul satılabilir mi?",
        "kategori": "⚖️ Ticaret ve Muamelat",
        "cevap": "Hayır, usulüne uygun olarak vakfedilen bir malın satılması, hibe edilmesi veya miras bırakılması kesinlikle yasaktır. Vakıf ebedidir.",
        "sayfa": 1002
    },

    # KURBAN (5 Fetva)
    {
        "soru": "Ortaklardan birinin niyeti et olan kurban geçerli midir?",
        "kategori": "🐑 Kurban ve Avcılık",
        "cevap": "Büyükbaş hayvanda ortaklardan birinin dahi niyeti ibadet dışı (sadece et almak) olursa hiçbir ortağın kurbanı geçerli olmaz. Ortakların tamamının ibadet niyeti olmalıdır.",
        "sayfa": 1068
    },
    {
        "soru": "Taksitle veya kredi kartıyla kurban alınabilir mi?",
        "kategori": "🐑 Kurban ve Avcılık",
        "cevap": "Evet, kişi mülkiyetini üzerine almak şartıyla taksitle veya kredi kartıyla kurbanlık satın alabilir. Kredi kartı borcunu faize bırakmamak şarttır.",
        "sayfa": 1060
    },
    {
        "soru": "Kurban derisi satılabilir mi?",
        "kategori": "🐑 Kurban ve Avcılık",
        "cevap": "Kurban derisi satılıp parası şahsi ihtiyaç için kullanılamaz. Eğer satılırsa parasının tasadduk edilmesi (fakirlere verilmesi) gerekir. Deri, bir hayır kurumuna bağışlanabilir.",
        "sayfa": 1072
    },
    {
        "soru": "Şoklama yöntemiyle (hayvanı bayıltarak) kesim yapmak caiz midir?",
        "kategori": "🐑 Kurban ve Avcılık",
        "cevap": "Hayvan kesilmeden önce ölmemek şartıyla, acısını hafifletmek amacıyla bayıltılarak yapılan kesim caizdir. Kesim anında canlı olması ve besmeleyle kesilmesi şarttır.",
        "sayfa": 1080
    },
    {
        "soru": "Kurban etinden gayrimüslim komşulara verilebilir mi?",
        "kategori": "🐑 Kurban ve Avcılık",
        "cevap": "Evet, vacip veya nafile olarak kesilen kurbanın etinden gayrimüslim komşulara, tanıdıklara ikram etmek veya hediye etmek caizdir.",
        "sayfa": 1070
    },

    # VASIYET (5 Fetva)
    {
        "soru": "Mirasçıya yapılan vasiyet ne zaman geçerli olur?",
        "kategori": "📜 Vasiyet ve Miras (Feraiz)",
        "cevap": "Mirasçılardan birine yapılan vasiyet, vasiyet edenin ölümünden sonra diğer yasal mirasçıların tamamının rızası ve onayı varsa geçerli olur. Tek bir mirasçı bile reddederse vasiyet geçersiz kalır.",
        "sayfa": 1120
    },
    {
        "soru": "Üvey çocuk anne veya babasına mirasçı olabilir mi?",
        "kategori": "📜 Vasiyet ve Miras (Feraiz)",
        "cevap": "Hayır, üvey çocuk ile üvey anne/baba arasında kan bağı olmadığı için yasal mirasçılık ilişkisi kurulmaz. Ancak hayattayken hibe yoluyla veya malın 1/3'ünü aşmayacak vasiyetle mal bırakılabilir.",
        "sayfa": 1135
    },
    {
        "soru": "Gayrimüslim bir akrabaya miras kalır mı?",
        "kategori": "📜 Vasiyet ve Miras (Feraiz)",
        "cevap": "Müslüman ile gayrimüslim arasında mirasçılık ilişkisi yoktur. Müslüman gayrimüslime, gayrimüslim de müslümana mirasçı olamaz. Ancak vasiyet yoluyla (1/3 oranını aşmayacak şekilde) mal bırakılabilir.",
        "sayfa": 1142
    },
    {
        "soru": "Cenaze masrafları mirastan mı karşılanır?",
        "kategori": "📜 Vasiyet ve Miras (Feraiz)",
        "cevap": "Evet, ölen kişinin mirasından ilk olarak cenaze teçhiz ve tekfin masrafları (israfa kaçmadan) karşılanır. Kalan maldan ise sırasıyla borçlar ödenir ve vasiyetler yerine getirilir.",
        "sayfa": 1126
    },
    {
        "soru": "Miras paylaşımında kız ve erkek çocukların oranları nedir?",
        "kategori": "📜 Vasiyet ve Miras (Feraiz)",
        "cevap": "İslam miras hukukunda erkek çocuğun payı, kız çocuğun payının iki katıdır. Bunun sebebi erkeğin evlilikte mehir ödemesi ve ailenin geçim yükümlülüğünü (nafaka) üstlenmesidir.",
        "sayfa": 1130
    }
]
