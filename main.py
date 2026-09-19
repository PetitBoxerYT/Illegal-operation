import subprocess
import random
import time

# ============================
# CONFIGURATION DES MODULES
# ============================

CONFIG = {
    "fermeture_programmes": True,
    "popup_systeme": True,
    "delai_aleatoire": True,

    # Modules futurs (désactivés pour l'instant)
    "fenetres_glissantes": False,
    "souris_bouge": False,
    "volume_change": False,
    "notifications_fake": False
}

# Liste blanche des programmes autorisés à fermer
PROGRAMMES_AUTORISES = [
    "vlc.exe",
    "Discord.exe",
    "msedge.exe",
]

# Intervalle de base (si delai_aleatoire = False)
INTERVALLE_FIXE = 10


# ============================
# MODULES
# ============================

# --- Module popup système moderne (WPF) ---
def module_popup(message="Action effectuée", titre="Information"):
    ps_script = f'''
Add-Type -AssemblyName PresentationFramework
[System.Windows.MessageBox]::Show("{message}", "{titre}")
'''
    subprocess.run(["powershell", "-NoProfile", "-Command", ps_script])


# --- Module fermeture aléatoire de programmes ---
def module_fermeture_programmes():
    programme = random.choice(PROGRAMMES_AUTORISES)

    # Vérifier si le programme est lancé
    result = subprocess.run(
        ["tasklist", "/FI", f"IMAGENAME eq {programme}"],
        capture_output=True, text=True
    )

    if programme.lower() in result.stdout.lower():
        subprocess.run(["taskkill", "/IM", programme, "/F"])
        module_popup(f"Illegal operation", "Program closed")
    else:
        module_popup(f"I see that {programme} isn't running.", "Hm...")


# --- Module délai aléatoire ---
def get_delai():
    if CONFIG["delai_aleatoire"]:
        return random.randint(10, 60)
    return INTERVALLE_FIXE


# ============================
# MODULES FUTURS (VIDES POUR L'INSTANT)
# ============================

def module_fenetres_glissantes():
    pass  # sera rempli plus tard

def module_souris_bouge():
    pass  # sera rempli plus tard

def module_volume_change():
    pass  # sera rempli plus tard

def module_notifications_fake():
    pass  # sera rempli plus tard


# ============================
# BOUCLE PRINCIPALE
# ============================

while True:

    if CONFIG["fermeture_programmes"]:
        module_fermeture_programmes()

    if CONFIG["popup_systeme"]:
        module_popup("Module popup exécuté", "Popup système")

    if CONFIG["fenetres_glissantes"]:
        module_fenetres_glissantes()

    if CONFIG["souris_bouge"]:
        module_souris_bouge()

    if CONFIG["volume_change"]:
        module_volume_change()

    if CONFIG["notifications_fake"]:
        module_notifications_fake()

    time.sleep(get_delai())
