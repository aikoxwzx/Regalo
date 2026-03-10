import streamlit as st

# 1. Configuración inicial de la página
st.set_page_config(page_title="Para you", page_icon="💜", layout="centered")

# 2. Inyección de CSS (Fondo morado y efecto de cristal)
estilo_css = """
<style>
.stApp {
    background: linear-gradient(135deg, #2A0845 0%, #6441A5 100%);
    color: white;
}
.glass-card {
    background: rgba(255, 255, 255, 0.1);
    border-radius: 20px;
    padding: 20px;
    box-shadow: 0 4px 30px rgba(0, 0, 0, 0.1);
    backdrop-filter: blur(10px);
    -webkit-backdrop-filter: blur(10px);
    border: 1px solid rgba(255, 255, 255, 0.25);
    margin-bottom: 20px;
    text-align: center;
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
}
h1, h2, h3, p, label, .stMarkdown {
    color: #F3E8FF !important;
}
.stTabs [data-baseweb="tab-list"] {
    gap: 10px;
    background-color: rgba(255, 255, 255, 0.1);
    border-radius: 10px;
    padding: 10px;
}
.stTabs [data-baseweb="tab"] {
    color: #F3E8FF;
}
div[data-baseweb="input"] {
    background-color: rgba(255, 255, 255, 0.1) !important;
    border-radius: 10px;
}
input {
    color: white !important;
}
</style>
"""
st.markdown(estilo_css, unsafe_allow_html=True)

# 3. Encabezado principal
st.markdown('<div class="glass-card"><h1>Para Soysh 💜</h1><p>Navega por las pestañas para descubrir todo...</p></div>', unsafe_allow_html=True)

# --- CREACIÓN DE LAS PESTAÑAS ---
pestaña1, pestaña2, pestaña3 = st.tabs(["✨ Nivel de amor", "🌍 100 Idiomas", "🔐 Cofre Secreto"])

# --- CONTENIDO DE LA PESTAÑA 1 (NUEVA VERSIÓN TIKTOK) ---
with pestaña1:
    st.markdown('<div class="glass-card"><h2>Escribe un número y baja hasta el final...</h2></div>', unsafe_allow_html=True)
    
    # Cuadro de texto para escribir el número (sin límite máximo)
    numero_bajar = st.number_input("Escribe tu número aquí:", min_value=1, value=10, step=1)

    # Contenedor con scroll
    with st.container(height=450):
        # Bucle súper sencillo: "Te amo 1", "Te amo 2", etc.
        for i in range(1, int(numero_bajar) + 1):
            st.markdown(f"<p style='text-align: center; font-size: 18px; margin: 5px;'>Te amo {i} </p>", unsafe_allow_html=True)
        
        # Mensaje al final del recorrido
        st.markdown('<br><div class="glass-card"><h2 style="color: #ff99cc !important;">¡¡Lo conseguistee!! 🎉</h2></div>', unsafe_allow_html=True)


# --- CONTENIDO DE LA PESTAÑA 2 ---
with pestaña2:
    st.markdown('<div class="glass-card"><h2>Elige un número del 1 al 100</h2></div>', unsafe_allow_html=True)
    numero_idiomas = st.slider("¿Cuántos idiomas quieres ver?", min_value=1, max_value=100, value=10, key="slider2")

    idiomas = [
        "Español: Te amo", "Inglés: I love you", "Francés: Je t'aime", "Italiano: Ti amo", "Portugués: Eu te amo",
        "Alemán: Ich liebe dich", "Coreano: Saranghae (사랑해)", "Japonés: Aishiteru (愛してる)", "Mandarín: Wǒ ài nǐ (我爱你)", "Ruso: Ya tebya lyublyu (Я тебя люблю)",
        "Árabe: Ana bahebak", "Hindi: Main tumse pyar karta hoon", "Holandés: Ik hou van jou", "Sueco: Jag älskar dig", "Noruego: Jeg elsker deg",
        "Danés: Jeg elsker dig", "Finés: Minä rakastan sinua", "Polaco: Kocham cię", "Checo: Miluji tě", "Eslovaco: Ľúbim ťa",
        "Húngaro: Szeretlek", "Rumano: Te iubesc", "Búlgaro: Obicham te", "Griego: S'agapo", "Turco: Seni seviyorum",
        "Hebreo: Ani ohev otakh", "Tailandés: Chan rak khun", "Vietnamita: Anh yêu em", "Indonesio: Aku cinta kamu", "Malayo: Saya cintakan awak",
        "Tagalo: Mahal kita", "Hawaiano: Aloha wau ia ʻoe", "Swahili: Nakupenda", "Afrikáans: Ek het jou lief", "Zulú: Ngiyakuthanda",
        "Irlandés: Taim i' ngra leat", "Galés: Rwy'n dy garu di", "Gaélico Escocés: Tha gaol agam ort", "Islandés: Ég elska þig", "Estonio: Ma armastan sind",
        "Letón: Es tevi mīlu", "Lituano: Aš tave myliu", "Ucraniano: Ya tebe kokhayu", "Bielorruso: Ya cyabe kahayu", "Serbio: Volim te",
        "Croata: Volim te", "Bosnio: Volim te", "Macedonio: Te sakam", "Albanés: Të dua", "Armenio: Yes kez sirum yem",
        "Georgiano: Miqvarxar", "Azerbaiyano: Mən səni sevirəm", "Persa: Dooset daram", "Kurdo: Ez te hezdikhem", "Urdu: Mein tumsay pyar karta hon",
        "Bengalí: Ami tomake bhalobashi", "Tamil: Naan unnai kadhalikkiren", "Telugu: Nenu ninnu premistunnanu", "Kannada: Naanu ninnanna preethisuthene", "Malayalam: Njan ninne premikkunnu",
        "Cingalés: Mama oyata adarei", "Nepalí: Ma timilai maya garchhu", "Jemer: Bon sro lanh oon", "Lao: Khoi huk chau", "Birmano: Chit pa de",
        "Tibetano: Nga khyed rang la ga", "Mongol: Bi chamd khairtai", "Kazajo: Men seni jaqsı köremin", "Uzbeko: Men seni sevaman", "Turcomano: Men seni söýýärin",
        "Kirguís: Men seni süýöm", "Tayiko: Man turo dūst medoram", "Pashto: Za ta sara meena kawom", "Somalí: Waan ku jeclahay", "Amárico: Ewedishalehu",
        "Yoruba: Mo nife re", "Igbo: A hurum gi n'anya", "Hausa: Ina sonki", "Shona: Ndinokuda", "Tigrinya: Yefkireki'ye",
        "Malagasy: Tiako ianao", "Samoano: Ou te alofa ia te oe", "Fiyiano: Au domoni iko", "Tahitiano: Ua here vau ia oe", "Maorí: Kei te aroha au ki a koe",
        "Esperanto: Mi amas vin", "Latín: Te amo", "Catalán: T'estimo", "Gallego: Quérote", "Euskera: Maite zaitut",
        "Quechua: Cuyayki", "Guaraní: Rohayhu", "Náhuatl: Nimitztlazohtla", "Maya: In yakumech", "Mapudungun: Piwkeyeyu",
        "Navajo: Ayóó aníníníshní", "Inuktitut: Nagligivaget", "Groenlandés: Asavakit", "Luxemburgués: Ech hunn dech gär", "Maltés: Inhobbok"
    ]

    idiomas_a_mostrar = idiomas[:numero_idiomas]
    texto_idiomas = "<br>".join(idiomas_a_mostrar)
    st.markdown(f'<div class="glass-card"><p style="font-size: 18px; line-height: 1.6;">{texto_idiomas}</p></div>', unsafe_allow_html=True)


# --- CONTENIDO DE LA PESTAÑA 3 ---
with pestaña3:
    st.markdown('<div class="glass-card"><h2> Archivos Encriptados </h2><p>Introduce la contraseña para desencriptar el mensaje final.</p></div>', unsafe_allow_html=True)

    contraseña_correcta = "nuestra_fecha" 
    intento = st.text_input("Contraseña:", type="password")

    if intento == contraseña_correcta:
        st.balloons()
        st.success("¡Acceso concedido!")
        
        st.markdown('<div class="glass-card"><h2>Una sorpresa extra </h2><p>Papi y yo te queremos muchísimo.</p></div>', unsafe_allow_html=True)
        try:
            st.image("izan.jpg", use_container_width=True)
        except:
            st.info("📸 Guarda una foto llamada 'izan.jpg' en esta carpeta.")

        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown('<div class="glass-card"><h2>Llegaste al final... </h2></div>', unsafe_allow_html=True)

        try:
            st.video("video_para_soysh.mp4")
        except:
            st.info("🎵 Pon tu video o canción aquí (guarda un archivo llamado 'video_para_soysh.mp4' en esta carpeta).")

        try:
            with open("carta.txt", "r", encoding="utf-8") as file:
                texto_carta = file.read()
            
            st.download_button(
                label="💌 Descarga tu carta sorpresa aquí",
                data=texto_carta,
                file_name="Para_Soysh.txt",
                mime="text/plain"
            )
        except FileNotFoundError:
            st.info("📝 Crea un archivo llamado 'carta.txt' en esta misma carpeta.")

    elif intento != "":
        st.error("Contraseña incorrecta. Inténtalo de nuevo.")
