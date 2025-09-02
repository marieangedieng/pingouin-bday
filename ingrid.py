import streamlit as st
import requests
from streamlit_lottie import st_lottie
import streamlit.components.v1 as components

# --- Page config ---------------------------------------------
st.set_page_config(page_title="Joyeux anniversaire Ingrid 🎉", layout="wide")

# --- Helpers -------------------------------------------------


def get_lottie_url(url: str):
    """
    Récupère une animation Lottie au format JSON depuis une URL.
    """
    try:
        r = requests.get(url, timeout=6)
        if r.status_code != 200:
            return None
        return r.json()
    except Exception:
        return None


def set_background_image(url: str):
    """
    Définit un fond d'écran pour l'application en utilisant du CSS.
    """
    st.markdown(
        f"""
        <style>
       .stApp {{
            background: url('{url}');
            background-size: cover;
            background-attachment: fixed;
            background-position: center;
        }}
       .stApp > header {{
            background-color: transparent;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )


# --- Configuration & ressources ------------------------------
GOJO_BACKGROUND_URL = "https://images2.alphacoders.com/136/1360490.jpeg"
BIRTHDAY_LOTTIE = "https://assets10.lottiefiles.com/packages/lf20_tiv728a3.json"
SIDES_LOTTIE = "https://assets6.lottiefiles.com/packages/lf20_xwif8yng.json"  # small decorative animation

set_background_image(GOJO_BACKGROUND_URL)

lottie_json = get_lottie_url(BIRTHDAY_LOTTIE)
sides_lottie = get_lottie_url(SIDES_LOTTIE)

# --- Stylish overlay + side animations (CSS + HTML) ---------
page_html = """
<style>
/* Central translucent panel */
.center-panel{
  max-width:900px;
  margin:40px auto;
  padding:28px;
  border-radius:16px;
  backdrop-filter: blur(6px);
  background: rgba(255,255,255,0.5); /* 50% transparent */
  color: #000; /* texte noir */
  box-shadow: 0 12px 40px rgba(0,0,0,0.18);
}

/* Title */
.h1-title{font-size:38px;font-weight:800;text-align:center;margin:0 0 6px}
.h1-sub{font-size:16px;text-align:center;margin-bottom:14px}

/* Animated side rails */
.side-rail{
  position: fixed;
  top: 0;
  bottom: 0;
  width: 120px;
  pointer-events:none; /* ne bloque pas les interactions */
  display:flex;align-items:center;justify-content:center;flex-direction:column;
}
.side-left{left:6px}
.side-right{right:6px}

.rail-bar{
  width:18px;height:160px;border-radius:12px;margin:18px 0;
  background: linear-gradient(180deg, rgba(214,61,134,0.9), rgba(255,184,75,0.9));
  box-shadow: 0 6px 18px rgba(0,0,0,0.12);
  animation: slideUpDown 4s ease-in-out infinite;
  opacity:0.95;
}

.rail-bar:nth-child(2){
  animation-duration:3.2s; transform: scale(0.92);
}
.rail-bar:nth-child(3){
  animation-duration:4.8s; transform: scale(0.8);
}

@keyframes slideUpDown{
  0%{ transform: translateY(0) }
  50%{ transform: translateY(-26px) scale(1.03) }
  100%{ transform: translateY(0) }
}

/* floating shapes behind text for extra motion */
.floating {
  position:absolute; border-radius:50%; opacity:0.18; filter: blur(12px);
}
.f1{ width:200px;height:200px; background: #ffd1dc; left:6%; top:10%; animation: floaty 8s ease-in-out infinite }
.f2{ width:140px;height:140px; background:#c8f7ff; right:8%; top:60%; animation: floaty 10s ease-in-out infinite }
@keyframes floaty{
  0%{ transform: translateY(0) }
  50%{ transform: translateY(-28px) }
  100%{ transform: translateY(0) }
}

/* responsive */
@media (max-width:900px){ .side-rail{display:none} .center-panel{margin:18px;padding:18px} }
</style>

<div class='floating f1'></div>
<div class='floating f2'></div>

<div class='side-rail side-left'>
  <div class='rail-bar'></div>
  <div class='rail-bar'></div>
  <div class='rail-bar'></div>
</div>

<div class='side-rail side-right'>
  <div class='rail-bar'></div>
  <div class='rail-bar'></div>
  <div class='rail-bar'></div>
</div>

<div class='center-panel'>
  <div style='text-align:center'>
    <div class='h1-title'>🎉 Joyeux Anniversaire, Ingrid — Pingouin !</div>
    <div class='h1-sub'>26 ans — que cette année soit la plus douce ✨</div>
  </div>
</div>

"""

st.markdown(page_html, unsafe_allow_html=True)

# --- Now render the content inside the Streamlit layout -------------
with st.container():
        st.markdown(
            """
            <div style='
                background: rgba(255,255,255,0.5); 
                backdrop-filter: blur(6px); 
                padding: 20px; 
                border-radius: 12px; 
                text-align: center; 
                color: #000; 
                font-size: 20px;
                font-weight:400;
                text-align:center
            '>
                <strong>🎁 À ma sœur adorée, ma meilleure amie, Ingrid — Pingouin :</strong>
                <br><br>
                Un nouvel an s'ajoute à ta collection — et à 26 ans, tu n'as jamais été aussi rayonnante.
                Chaque jour passé à tes côtés est une aventure, une leçon, un fou rire.
                Je te souhaite un anniversaire aussi doux et merveilleux que toi, rempli d'amour, de joie et de tout le bonheur du monde.
                <br><br>
                Que cette nouvelle année t'apporte de la réussite, des rêves qui se réalisent, et des moments inoubliables.
                <br><br>
                Avec tout mon amour,
                <br>
                ❤️ Pingouin
            </div>
            """,
            unsafe_allow_html=True,
        )

# small CTA + confetti when user presses
col1, col2, col3 = st.columns([2, 3, 2])
with col2:
    if st.button(" Clique - ici et patiente 2 secs pour un cadeau 🎂", use_container_width=True):
        # balloons built-in
        st.balloons()
        # also run a confetti snippet for a short burst
        components.html(
            """
            <script src='https://cdn.jsdelivr.net/npm/canvas-confetti@1.5.1/dist/confetti.browser.min.js'></script>
            <script>
              (function(){
                var duration = 1800;
                var end = Date.now() + duration;
                (function frame(){
                  confetti({ particleCount: 10, origin: { x: Math.random(), y: Math.random() * 0.6 } });
                  if (Date.now() < end) requestAnimationFrame(frame);
                })();
              })();
            </script>
            """,
            height=120,
        )

# show decorative side Lottie animations anchored to the fixed rails
if sides_lottie:
    # embed via components.html with absolute positioning inside the rails
    sides_html = f"""
    <div style='position:fixed;left:12px;top:8vh;width:96px;pointer-events:none;opacity:0.95'>
      <!-- left decorative -->
      <div id='leftLottie'></div>
    </div>
    <div style='position:fixed;right:12px;top:8vh;width:96px;pointer-events:none;opacity:0.95'>
      <!-- right decorative -->
      <div id='rightLottie'></div>
    </div>
    <script src='https://cdnjs.cloudflare.com/ajax/libs/bodymovin/5.9.6/lottie.min.js'></script>
    <script>
      const left = document.getElementById('leftLottie');
      const right = document.getElementById('rightLottie');
      // fetch the json and load into two small lotties
      fetch('{SIDES_LOTTIE}').then(r=>r.json()).then(data=>{{
        lottie.loadAnimation({{container:left, renderer:'svg', loop:true, autoplay:true, animationData:data}});
        lottie.loadAnimation({{container:right, renderer:'svg', loop:true, autoplay:true, animationData:data}});
      }}).catch(e=>console.warn('lottie load failed', e));
    </script>
    """
    components.html(sides_html, height=10)

# final small footnote
st.markdown("<div style='text-align:center;margin-top:14px;color:#111;font-size:13px'>Astuce: modifie le message et reclique sur le bouton pour rejouer les animations.</div>", unsafe_allow_html=True)
