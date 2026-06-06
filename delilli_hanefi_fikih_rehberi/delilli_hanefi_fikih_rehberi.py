# -*- coding: utf-8 -*-
"""
Delilli Hanefi Fıkıh Rehberi - Streamlit Arayüzü
"""

import streamlit as st
import json
import os
import re
import random

# 1. SAYFA YAPILANDIRMASI
st.set_page_config(
    page_title="Delilli Hanefi Fıkıh Rehberi",
    page_icon="🕌",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. PREMIUM CSS TASARIMI (Yeşil ve Altın Temalı Glassmorphism)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700;800&family=Amiri:ital,wght@0,400;0,700;1,400&family=Playfair+Display:ital,wght@0,600;1,400&display=swap');
    
    /* Global Font Settings */
    html, body, [class*="css"] {
        font-family: 'Outfit', sans-serif;
    }
    
    h1, h2, h3 {
        font-family: 'Playfair Display', serif;
        color: #D4AF37 !important; /* Gold */
    }
    
    /* Sidebar Styling */
    [data-testid="stSidebar"] {
        background-color: #0B291B !important;
    }
    [data-testid="stSidebar"] .stMarkdown p, [data-testid="stSidebar"] span, [data-testid="stSidebar"] label {
        color: #E2E8F0 !important;
    }
    [data-testid="stSidebar"] h1, [data-testid="stSidebar"] h2, [data-testid="stSidebar"] h3, [data-testid="stSidebar"] h4, [data-testid="stSidebar"] h5, [data-testid="stSidebar"] h6 {
        color: #D4AF37 !important;
    }
    
    /* Custom Card Design */
    .fikih-card {
        background: rgba(255, 255, 255, 0.03);
        border-radius: 16px;
        box-shadow: 0 4px 30px rgba(0, 0, 0, 0.2);
        backdrop-filter: blur(10px);
        -webkit-backdrop-filter: blur(10px);
        border: 1px solid rgba(212, 175, 55, 0.15); /* Soft Gold border */
        padding: 30px;
        margin-bottom: 25px;
        transition: transform 0.3s ease, border-color 0.3s ease, box-shadow 0.3s ease;
    }
    
    .fikih-card:hover {
        transform: translateY(-3px);
        border-color: rgba(212, 175, 55, 0.5);
        box-shadow: 0 8px 40px rgba(13, 92, 58, 0.3);
    }
    
    /* Title badge */
    .title-badge {
        display: inline-block;
        background: linear-gradient(135deg, #0D5C3A 0%, #073B24 100%);
        color: #D4AF37;
        font-weight: 600;
        padding: 6px 16px;
        border-radius: 30px;
        font-size: 13px;
        border: 1px solid rgba(212, 175, 55, 0.3);
        margin-bottom: 15px;
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    
    /* Quran/Hadith quote styling */
    .delil-box {
        background-color: rgba(212, 175, 55, 0.05);
        border-left: 4px solid #D4AF37;
        padding: 20px;
        border-radius: 0 12px 12px 0;
        margin: 20px 0;
        font-style: italic;
        color: #E2E8F0;
    }
    
    .arabic-text {
        font-family: 'Amiri', serif;
        font-size: 26px;
        line-height: 1.8;
        color: #F8FAFC;
        direction: rtl;
        text-align: right;
        padding: 10px;
        margin: 10px 0;
    }
    
    /* Highlight searched word */
    .highlight {
        background-color: rgba(212, 175, 55, 0.3) !important;
        color: #FFFFFF !important;
        padding: 2px 4px;
        border-radius: 4px;
        font-weight: bold;
    }
    
    /* Custom buttons */
    .stButton>button {
        background: linear-gradient(135deg, #0D5C3A 0%, #073B24 100%) !important;
        color: #D4AF37 !important;
        border: 1px solid rgba(212, 175, 55, 0.4) !important;
        padding: 8px 20px !important;
        border-radius: 8px !important;
        transition: all 0.3s ease !important;
        font-weight: 600 !important;
    }
    
    .stButton>button:hover {
        background: linear-gradient(135deg, #D4AF37 0%, #AA841C 100%) !important;
        color: #073B24 !important;
        border-color: #073B24 !important;
        box-shadow: 0 4px 15px rgba(212, 175, 55, 0.4) !important;
        transform: translateY(-1px) !important;
    }
    
    /* Category tag list */
    .cat-tag {
        display: inline-block;
        background-color: rgba(13, 92, 58, 0.2);
        color: #34D399;
        padding: 4px 12px;
        border-radius: 8px;
        font-size: 12px;
        font-weight: 500;
        border: 1px solid rgba(52, 211, 153, 0.2);
        margin-right: 8px;
        margin-bottom: 8px;
    }
    
    .source-banner {
        background: linear-gradient(135deg, rgba(13, 92, 58, 0.15) 0%, rgba(7, 59, 36, 0.15) 100%);
        border: 1px dashed rgba(212, 175, 55, 0.4);
        padding: 15px;
        border-radius: 12px;
        margin-top: 20px;
        text-align: center;
        font-size: 13px;
        color: #94A3B8;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. VERİ YÜKLEME (JSON Kütüphanesi)
@st.cache_data
def veriyi_yukle():
    json_path = 'Delilleriyle Hanefi Fıkhı.json'
    if not os.path.exists(json_path):
        st.error(f"Hata: '{json_path}' dosyası bulunamadı! Lütfen önce PDF'i JSON'a dönüştürün.")
        return None
    try:
        with open(json_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception as e:
        st.error(f"Veri yüklenirken hata oluştu: {e}")
        return None

data = veriyi_yukle()

# 4. FIKIH REHBERİ YEREL
from fiqh_data import CATEGORIES, FAQ_DATA



# 6. YARDIMCI FONKSİYONLAR
def metin_vurgula(metin, arama_terimi):
    """Metin içindeki arama terimini CSS ile vurgular."""
    if not arama_terimi:
        return metin
    try:
        # Case-insensitive replacement using regex
        pattern = re.compile(re.escape(arama_terimi), re.IGNORECASE)
        # Highlight pattern
        vurgulu = pattern.sub(lambda m: f'<mark class="highlight">{m.group(0)}</mark>', metin)
        return vurgulu
    except Exception:
        return metin

def markdown_to_html(text):
    """Temel markdown bold ve bullet yapılarını HTML formatına çevirir."""
    if not text:
        return ""
    # Clean leading/trailing whitespaces per line to prevent markdown code block detection
    lines = [line.strip() for line in text.split('\n')]
    processed_text = '\n'.join(lines)
    processed_text = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', processed_text)
    
    # Process list tags
    lines = processed_text.split('\n')
    in_list = False
    html_lines = []
    for line in lines:
        if line.startswith('- '):
            if not in_list:
                html_lines.append('<ul style="margin-top: 5px; margin-bottom: 5px; padding-left: 20px;">')
                in_list = True
            content = line[2:]
            html_lines.append(f'<li>{content}</li>')
        else:
            if in_list:
                html_lines.append('</ul>')
                in_list = False
            html_lines.append(line)
    if in_list:
        html_lines.append('</ul>')
    return '\n'.join(html_lines)

# 7. YAN MENÜ (SIDEBAR)
st.sidebar.image("https://cdn-icons-png.flaticon.com/512/2904/2904843.png", width=90)
st.sidebar.title("Hanefi Fıkıh Rehberi")
st.sidebar.caption("📖 Delilli İlmihal Uygulaması")

menu = st.sidebar.radio(
    "Menü Seçimi:",
    ["🏠 Ana Sayfa", "📚 Fıkıh Rehberi (Konular)", "🔍 Gelişmiş Arama", "💡 Günün Fıkhi Kaidesi", "❓ Fetvalar (Soru-Cevap)"]
)

st.sidebar.markdown("---")

# Kaynak Bilgisi (Zorunlu İstek)
st.sidebar.markdown("""
<div style="background-color: rgba(212, 175, 55, 0.1); border: 1px solid #D4AF37; padding: 12px; border-radius: 10px; text-align: center;">
    <h5 style="color: #D4AF37; margin: 0 0 5px 0; font-family: 'Playfair Display', serif;">📖 Veri Kaynağı</h5>
    <p style="font-size: 12px; color: #E2E8F0; margin: 0; line-height: 1.4;">
        Bu uygulamadaki tüm fıkhi bilgiler ve kaynak metinler 
        <b>Esad Muhammed</b> ve <b>Said es-Sağirci</b>'nin 
        <i>"Delilleriyle Hanefi Fıkhı"</i> (1216 Sayfa) adlı eserinden derlenmiştir.
    </p>
</div>
""", unsafe_allow_html=True)

# 8. SAYFA İÇERİKLERİ

if menu == "🏠 Ana Sayfa":
    # Hero Bölümü
    st.markdown("""
    <div class="fikih-card" style="text-align: center; background: linear-gradient(135deg, rgba(13, 92, 58, 0.4) 0%, rgba(7, 36, 22, 0.4) 100%);">
        <span class="title-badge">HÜKÜM VE DELİL BİR ARADA</span>
        <h1 style="font-size: 42px; margin-top: 10px;">🕌 Delilli Hanefi Fıkıh Rehberi</h1>
        <p style="font-size: 18px; color: #CBD5E1; max-width: 800px; margin: 15px auto; line-height: 1.6;">
            Hanefi mezhebinin temel fıkhi görüşlerini, delilleri (ayet ve hadisler) ile birlikte inceleyin. 
            Günlük hayatınızda ihtiyacınız olan ilmihal bilgilerine modern ve kullanışlı bir arayüzle ulaşın.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # 3'lü Özellik Grid
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="fikih-card" style="height: 100%;">
            <h3 style="margin-top:0;">📚 Fıkıh Kitaplığı</h3>
            <p style="color: #94A3B8; font-size:14px; line-height:1.5;">
                Temizlik, Namaz, Oruç, Zekat, Hac, Aile ve Muamelat gibi temel fıkıh başlıklarını 
                Hanefi mezhebinin en saygın delil kitaplarından biriyle sayfa sayfa doğrulayarak okuyun.
            </p>
        </div>
        """, unsafe_allow_html=True)
        
    with col2:
        st.markdown("""
        <div class="fikih-card" style="height: 100%;">
            <h3 style="margin-top:0;">🔍 Arama Motoru</h3>
            <p style="color: #94A3B8; font-size:14px; line-height:1.5;">
                1216 sayfalık dev eserde saniyeler içinde arama yapın. İlgili kavramın veya kaidenin geçtiği 
                sayfaları, delilleriyle ve çevresiyle birlikte anında görüntüleyin.
            </p>
        </div>
        """, unsafe_allow_html=True)
        
    with col3:
        st.markdown("""
        <div class="fikih-card" style="height: 100%;">
            <h3 style="margin-top:0;">💡 Günün Hükmü & Delili</h3>
            <p style="color: #94A3B8; font-size:14px; line-height:1.5;">
                Her gün Hanefi fıkhından yeni bir hukuki ve ibadi kaideyi öğrenin. Hükümlerin Kur'an ve Sünnet'teki 
                delillerine hızlıca göz atarak fıkhi bilincinizi geliştirin.
            </p>
        </div>
        """, unsafe_allow_html=True)
        
    st.write("---")
    
    # Eser Bilgisi ve Künye
    st.subheader("📖 Eser Künyesi ve Hakkında")
    st.markdown("""
    <div class="fikih-card">
        <div style="display: flex; gap: 20px; align-items: center; flex-wrap: wrap;">
            <div style="flex: 1; min-width: 300px;">
                <h4 style="color: #D4AF37; margin-top:0;">Delilleriyle Hanefi Fıkhı (el-Fıkhu'l-Hanefiyyu ve Edilletuhû)</h4>
                <p style="color: #CBD5E1; font-size:15px; line-height:1.6;">
                    Bu eser, çağdaş fıkıh alimlerinden <b>Esad Muhammed Said es-Sağirci</b> tarafından kaleme alınmıştır. 
                    Hanefi mezhebinin ibadet, muamelat ve aile hukuku alanındaki tüm görüşlerini ve fetvalarını, 
                    ayet-i kerimeler ve sahih hadis-i şerifler ışığında delillendirerek sunan en kapsamlı çalışmalardan biridir.
                </p>
                <span class="cat-tag">✍️ Yazar: Esad Muhammed Said es-Sağirci</span>
                <span class="cat-tag">📄 Sayfa Sayısı: 1216</span>
                <span class="cat-tag">⚖️ Mezhep: Hanefi</span>
                <span class="cat-tag">🇹🇷 Türkçe Çeviri: Karınca & Polen Yayınları</span>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

elif menu == "📚 Fıkıh Rehberi (Konular)":
    st.title("📚 Konularına Göre Hanefi Fıkhı Rehberi")
    st.write("Aşağıdan bir fıkıh başlığı seçerek o konuya dair özet ilmihal bilgilerine ulaşabilir ve eserdeki ilgili sayfalara göz atabilirsiniz.")
    
    # Konu Seçimi
    selected_cat = st.selectbox(
        "Lütfen İncelemek İstediğiniz Fıkıh Konusunu Seçin:",
        list(CATEGORIES.keys())
    )
    
    cat_info = CATEGORIES[selected_cat]
    
    st.markdown(f"""
    <div class="fikih-card" style="border-left: 5px solid #D4AF37;">
        <span class="title-badge">{selected_cat}</span>
        <p style="font-size: 16px; color: #E2E8F0; margin-top: 10px;">{cat_info['description']}</p>
        <span class="cat-tag">📖 Kitap Sayfa Aralığı: Sayfa {cat_info['start_page']} - {cat_info['end_page']}</span>
    </div>
    """, unsafe_allow_html=True)
    
    # Alt Konu Sekmeleri
    subtopics = cat_info["subtopics"]
    sub_names = list(subtopics.keys())
    
    if sub_names:
        tabs = st.tabs(sub_names)
        for idx, sub_name in enumerate(sub_names):
            with tabs[idx]:
                sub_info = subtopics[sub_name]
                st.markdown("### 📝 İlmihal Özeti")
                st.markdown(f"<div class='delil-box'>{markdown_to_html(sub_info['summary'])}</div>", unsafe_allow_html=True)
    else:
        st.info("Bu kategori için henüz alt başlık tanımlanmamış. Sayfa aralığına göre arama motorunu kullanabilirsiniz.")

elif menu == "🔍 Gelişmiş Arama":
    st.title("🔍 İlmihal Özetlerinde Gelişmiş Arama")
    st.write("Fıkıh rehberindeki özet ilmihal metinleri ve konuları içerisinde arama yapın.")
    
    search_query = st.text_input("Aramak İstediğiniz Kavramı Yazın (Örn: abdest, rükû, niyet, zekat, mehir):").strip()
    
    if search_query:
        results = []
        for cat_name, cat_val in CATEGORIES.items():
            for sub_name, sub_info in cat_val["subtopics"].items():
                # Hem alt konu başlığında hem de özet metninde ara
                if search_query.lower() in sub_name.lower() or search_query.lower() in sub_info["summary"].lower():
                    # Eşleşen kısmı bulmak için snippet oluşturalım
                    summary_text = sub_info["summary"]
                    idx = summary_text.lower().find(search_query.lower())
                    if idx != -1:
                        start = max(0, idx - 100)
                        end = min(len(summary_text), idx + len(search_query) + 100)
                        snippet = summary_text[start:end].replace('\n', ' ')
                        if start > 0:
                            snippet = "..." + snippet
                        if end < len(summary_text):
                            snippet = snippet + "..."
                    else:
                        # Eğer sadece başlıkta eşleştiyse ilk 150 karakteri göster
                        snippet = summary_text[:150].replace('\n', ' ') + "..."
                    
                    results.append({
                        "kategori": cat_name,
                        "alt_kategori": sub_name,
                        "pages": sub_info["pages"],
                        "summary": summary_text,
                        "snippet": snippet
                    })
        
        st.subheader(f"📊 Arama Sonuçları (Toplam {len(results)} konu eşleşti)")
        
        if not results:
            st.info("Arama kriterinize uygun konu veya açıklama bulunamadı. Lütfen farklı kelimeler deneyin.")
        else:
            for idx, res in enumerate(results):
                header = f"📚 {res['kategori']} > {res['alt_kategori']} (Sayfa {min(res['pages'])} - {max(res['pages'])})"
                with st.expander(header):
                    # Snippet ve tam metni göster
                    highlighted_snippet = metin_vurgula(res['snippet'], search_query)
                    highlighted_full = metin_vurgula(res['summary'], search_query)
                    
                    highlighted_snippet_html = markdown_to_html(highlighted_snippet)
                    highlighted_full_html = markdown_to_html(highlighted_full)
                    
                    st.markdown(f"**Eşleşen Kısım:** <br><div style='padding: 10px; background-color: rgba(255,255,255,0.05); border-radius: 5px; margin-bottom: 10px;'>{highlighted_snippet_html}</div>", unsafe_allow_html=True)
                    st.markdown("**Tam İlmihal Özeti:**")
                    st.markdown(f"<div class='delil-box'>{highlighted_full_html}</div>", unsafe_allow_html=True)

elif menu == "💡 Günün Fıkhi Kaidesi":
    st.title("💡 Günün Fıkhi Kaidesi (Rastgele İlmihal Özeti)")
    st.write("Hanefi fıkhı rehberinden seçilmiş rastgele bir ilmihal konusu ve detaylı özeti.")
    
    # Tüm alt konuları topla
    all_subtopics = []
    for cat_name, cat_val in CATEGORIES.items():
        for sub_name, sub_val in cat_val["subtopics"].items():
            all_subtopics.append({
                "kategori": cat_name,
                "baslik": sub_name,
                "summary": sub_val["summary"],
                "pages": sub_val["pages"]
            })
            
    # Session state ile günün kaidesini sakla
    if "daily_rule" not in st.session_state or not isinstance(st.session_state.daily_rule, dict) or "summary" not in st.session_state.daily_rule:
        st.session_state.daily_rule = random.choice(all_subtopics)
        
    if st.button("🔄 Başka Bir İlmihal Özeti Getir"):
        st.session_state.daily_rule = random.choice(all_subtopics)
        
    rule = st.session_state.daily_rule
    
    st.markdown(f"""
    <div class="fikih-card" style="border-top: 5px solid #D4AF37;">
        <span class="title-badge">{rule['kategori']}</span>
        <h3 style="margin-top: 10px;">{rule['baslik']}</h3>
        <span class="cat-tag" style="margin-bottom: 15px; display: inline-block;">📖 Kitap Sayfaları: {min(rule['pages'])} - {max(rule['pages'])}</span>
        <div class="delil-box" style="margin-top: 10px;">
            {markdown_to_html(rule['summary'])}
        </div>
    </div>
    """, unsafe_allow_html=True)

elif menu == "❓ Fetvalar (Soru-Cevap)":
    st.title("❓ Sıkça Sorulan Sorular ve Hanefi Fetvaları")
    st.write("Günlük hayatta sıkça karşılaşılan fıkhi soruların Hanefi mezhebine göre cevapları ve 'Delilleriyle Hanefi Fıkhı' kitabındaki sayfa referansları.")
    
    # Display questions in cards
    for idx, faq in enumerate(FAQ_DATA):
        with st.expander(f"❓ {faq['soru']}"):
            st.markdown(f"<span class='cat-tag'>{faq['kategori']}</span> <span class='cat-tag'>📄 Sayfa Referansı: {faq['sayfa']}</span>", unsafe_allow_html=True)
            st.markdown(f"""
            <div class="delil-box" style="margin-top: 10px;">
                {faq['cevap']}
            </div>
            """, unsafe_allow_html=True)
