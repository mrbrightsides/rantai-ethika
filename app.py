import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="RANTAI ETHIKA",
    page_icon="⚖️",
    layout="wide"
)

with st.sidebar:
    st.sidebar.image(
        "https://i.imgur.com/pwYe3ox.png",
        use_container_width=True
    )
    st.sidebar.markdown("📘 **About**")
    st.sidebar.markdown("""
    **ETHIKA** adalah modul Ethics & Bias Checker yang dirancang untuk mendeteksi ketidakseimbangan dataset dan mengevaluasi fairness model secara sederhana dan interaktif. Modul ini tidak hanya memberikan flag dan indikator bias, tetapi juga mengedukasi mahasiswa dengan refleksi kritis tentang dampak sosial dan etis dari bias AI, menjadikan pembelajaran responsible AI lebih hidup dan kontekstual dalam ekosistem Web3.
    
    ---
    #### 🔮 Vision Statement
    
    Menjadi modul etika AI terpercaya yang memberdayakan mahasiswa dan pengembang untuk menciptakan model machine learning yang adil, bertanggung jawab, dan berakar pada nilai-nilai sosial, hukum, dan moral, guna membangun teknologi yang layak dan bermanfaat bagi semua lapisan masyarakat.

    ---
    ### 🌐 RANTAI Pipeline
    
    Keempat modul—EDA, BI, Predictive Modeling, dan ETHIKA—bekerja bersama sebagai bagian dari siklus analitik data yang saling terintegrasi, memastikan alur data dan insight yang mulus dari awal hingga akhir dengan keseimbangan etika dan fairness sebagai pijakan utama.
    
    - Exploratory Data Analysis (EDA) merupakan langkah awal yang mempersiapkan dan memvalidasi data mentah. Dengan analisis statistik dan visualisasi eksploratif, EDA mengidentifikasi pola, anomali, dan kualitas data yang akan menjadi dasar untuk tahap selanjutnya.
    
    - Business Intelligence (BI) menerima data yang sudah bersih dan terstruktur dari EDA untuk membangun dashboard interaktif dan laporan. BI fokus menyediakan visualisasi realtime yang mudah dipahami dan mendukung pengambilan keputusan bisnis secara cepat dan terukur.
    
    - Predictive Modeling (PM) menggunakan data yang sudah tervalidasi dan insight dari BI untuk membuat model prediktif. Output model ini dapat dikembalikan ke dashboard BI untuk memberikan prediksi dan rekomendasi, melengkapi insight historis dengan analisis masa depan.

    - Etika, Bias, Hukum, dan Agama hadir sebagai modul check & balance dalam pipeline ini, mendeteksi ketidakseimbangan dataset dan mengevaluasi fairness model. ETHIKA tidak hanya memberi peringatan bias, tetapi juga mendorong refleksi etis dan tanggung jawab sosial dalam setiap tahapan pengembangan model, memastikan hasil analitik layak secara moral dan sosial untuk digunakan.
    
    > 💡 Pipeline ini membentuk siklus data yang berkelanjutan: dari pemahaman awal (EDA), ke reporting yang actionable (BI), hingga keputusan proaktif berbasis prediksi (PM), serta keseimbangan etika dan fairness (ETHIKA), mendukung keputusan bisnis yang lebih cerdas, responsif, dan bertanggung jawab.
    
    ---
    ### 🧩 Apps Showcase
    Lihat disini untuk semua tools yang kami kembangkan:
    [ELPEEF](https://showcase.elpeef.com/)
    
    ---
    #### 🙌 Dukungan & kontributor
    
    - ⭐ **Star / Fork**: [GitHub repo](https://github.com/mrbrightsides/rantai-ethika)
    - Built with 💙 by [Khudri](https://s.id/khudri)
    - Dukung pengembangan proyek ini melalui: 
      [💖 GitHub Sponsors](https://github.com/sponsors/mrbrightsides) • 
      [☕ Ko-fi](https://ko-fi.com/khudri) • 
      [💵 PayPal](https://www.paypal.com/paypalme/akhmadkhudri) • 
      [🍵 Trakteer](https://trakteer.id/akhmad_khudri)

    Versi UI: v1.0 • Streamlit • Theme Dark
    """)

import streamlit.components.v1 as components

def embed_iframe(src, hide_top_px=100, hide_bottom_px=0, height=800):
    components.html(f"""
    <style>
        @media (max-width: 768px) {{
            .hide-on-mobile {{
                display: none !important;
            }}
            .show-on-mobile {{
                display: block !important;
                padding: 24px 12px;
                background: #ffecec;
                color: #d10000;
                font-weight: bold;
                text-align: center;
                border-radius: 12px;
                font-size: 1.2em;
                margin-top: 24px;
                animation: fadeIn 0.6s ease-in-out;
                box-shadow: 0 4px 12px rgba(0,0,0,0.2);
            }}
        }}
        @media (min-width: 769px) {{
            .show-on-mobile {{
                display: none !important;
            }}
        }}
        @keyframes fadeIn {{
            from {{ opacity: 0; transform: translateY(12px); }}
            to {{ opacity: 1; transform: translateY(0); }}
        }}
    </style>

    <!-- Desktop view -->
    <div class="hide-on-mobile" style="height:{height}px; overflow:hidden; position:relative;">
        <iframe src="{src}" 
                style="width:100%; height:calc(100% + {hide_top_px + hide_bottom_px}px); 
                       border:none; position:relative; top:-{hide_top_px}px;">
        </iframe>
    </div>

    <!-- Mobile fallback -->
    <div class="show-on-mobile">
        📱 Tampilan ini tidak tersedia di perangkat seluler.<br>
        Silakan buka lewat laptop atau desktop untuk pengalaman penuh 💻
    </div>
    """, height=height + hide_top_px + hide_bottom_px)

iframe_url = "https://ethika.elpeef.com/"

# Panggil fungsi
embed_iframe(iframe_url, hide_top_px=5, hide_bottom_px = -105, height=800)
