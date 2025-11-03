# ============================================
# 🐟 SISTEM PAKAR DIAGNOSA PENYAKIT IKAN MOLLY
# Dengan Forward Chaining & Multi Diagnosis
# ============================================

import ipywidgets as widgets
from IPython.display import display, HTML, clear_output

display(HTML("<h2 style='color:#0073e6'>🐠 Sistem Pakar Diagnosa Penyakit Ikan Molly</h2>"))
display(HTML("<p><b>Petunjuk:</b> Centang semua gejala yang kamu amati, lalu klik <b>Diagnosa</b>.</p>"))

# ---- BASIS PENGETAHUAN ----
rules = [
    {
        "gejala": ["ikan menggosok tubuh ke kaca", "ada bintik putih di tubuh", "napas cepat"],
        "penyakit": "White Spot (Ichthyophthirius multifiliis)",
        "solusi": "Naikkan suhu ke 30°C, tambahkan garam ikan 1 sdm/5L air, dan aerasi kuat."
    },
    {
        "gejala": ["sirip rusak atau sobek", "ikan sering berdiam di dasar akuarium", "warna tubuh pucat"],
        "penyakit": "Fin Rot (Busuk Sirip)",
        "solusi": "Ganti air 50%, tambahkan metil biru, dan jaga kualitas air tetap bersih."
    },
    {
        "gejala": ["perut ikan membesar", "ikan sulit berenang seimbang", "ikan lesu"],
        "penyakit": "Dropsy (Pembengkakan)",
        "solusi": "Pisahkan ikan sakit, gunakan antibiotik khusus ikan, dan perbaiki sirkulasi air."
    },
    {
        "gejala": ["ikan mengambang di permukaan", "napas cepat", "ikan lesu"],
        "penyakit": "Kekurangan Oksigen",
        "solusi": "Tambahkan aerator, kurangi kepadatan ikan, dan periksa suhu air."
    },
    {
        "gejala": ["ikan lesu", "warna tubuh pucat", "tidak mau makan"],
        "penyakit": "Stres atau Kualitas Air Buruk",
        "solusi": "Ganti sebagian air, tambahkan garam ikan sedikit, dan hindari perubahan suhu drastis."
    },
    {
        "gejala": ["tubuh ikan tampak berbulu putih", "sirip menempel pada badan", "ikan berenang tidak seimbang"],
        "penyakit": "Jamur Kulit (Fungal Infection)",
        "solusi": "Gunakan obat anti jamur ikan, karantina ikan sakit, dan bersihkan akuarium."
    },
    {
        "gejala": ["ikan membuka mulut terus menerus", "mengap di permukaan", "sirip tidak aktif"],
        "penyakit": "Kekurangan Oksigen Parah",
        "solusi": "Segera tambahkan aerator dan periksa filter atau pompa udara."
    },
    {
        "gejala": ["ikan sering bersembunyi", "sirip menguncup", "warna tubuh gelap"],
        "penyakit": "Infeksi Bakteri Ringan",
        "solusi": "Gunakan antibiotik dosis rendah, jaga pH dan suhu air tetap stabil."
    },
    {
        "gejala": ["ikan berenang terbalik", "perut menggembung", "tidak mau makan"],
        "penyakit": "Swim Bladder Disorder (Gangguan Kantung Renang)",
        "solusi": "Puasa 2 hari, beri makanan berserat tinggi (seperti kacang polong rebus)."
    },
    {
        "gejala": ["ikan sering naik turun permukaan", "ada lendir di tubuh", "napas cepat"],
        "penyakit": "Keracunan Amonia atau Nitrit",
        "solusi": "Ganti air 70%, tambahkan filter biologis, dan periksa kadar amonia."
    }
]

# ---- Daftar Gejala ----
daftar_gejala = sorted(set(sum([r["gejala"] for r in rules], [])))
checkboxes = [widgets.Checkbox(value=False, description=g) for g in daftar_gejala]
button = widgets.Button(description="🔍 Diagnosa", button_style='info')
output = widgets.Output()

# ---- Fungsi Diagnosa ----
def diagnosa(b):
    clear_output(wait=True)
    display(HTML("<h2 style='color:#0073e6'>🐠 Hasil Diagnosa Ikan Molly</h2>"))
    
    fakta = [cb.description for cb in checkboxes if cb.value]
    if not fakta:
        display(HTML("<p style='color:red;'>⚠️ Pilih minimal satu gejala terlebih dahulu!</p>"))
        for cb in checkboxes:
            display(cb)
        display(button)
        return

    hasil_kemungkinan = []
    
    for rule in rules:
        cocok = len(set(fakta) & set(rule["gejala"]))
        total = len(rule["gejala"])
        persen = (cocok / total) * 100
        if persen > 0:
            hasil_kemungkinan.append({
                "penyakit": rule["penyakit"],
                "persentase": persen,
                "solusi": rule["solusi"]
            })
    
    if hasil_kemungkinan:
        hasil_kemungkinan = sorted(hasil_kemungkinan, key=lambda x: x["persentase"], reverse=True)
        
        display(HTML("<h3 style='color:#333;'>🧩 Semua Kemungkinan Penyakit Berdasarkan Gejala:</h3>"))
        for h in hasil_kemungkinan:
            warna = "#c8f7c5" if h["persentase"] >= 70 else "#fff7c2" if h["persentase"] >= 40 else "#ffe6e6"
            display(HTML(f"""
            <div style='background:{warna};padding:10px;margin:6px 0;border-radius:10px;width:80%;'>
                <b>{h['penyakit']}</b><br>
                <i>Tingkat Keyakinan:</i> {h['persentase']:.1f}%<br>
                <b>Solusi:</b> {h['solusi']}
            </div>
            """))
    else:
        display(HTML("""
        <div style='background:#ffe6e6;padding:15px;border-radius:10px;width:70%;'>
            <h3 style='color:#cc0000'>⚠️ Tidak ditemukan penyakit yang cocok.</h3>
            <p>Perlu pengamatan lebih lanjut atau gejala tambahan.</p>
        </div>
        """))

    display(HTML("<hr><p><b>Gejala yang dipilih:</b> " + ", ".join(fakta) + "</p>"))
    
    # Tampilkan ulang input
    for cb in checkboxes:
        display(cb)
    display(button)

button.on_click(diagnosa)

# ---- Tampilan Awal ----
for cb in checkboxes:
    display(cb)
display(button)
