import streamlit as st
import pandas as pd
import joblib

# 1. Load Model (Pastikan model .h5 ada di folder yang sama)
try:
    model = joblib.load('tuning_classification.h5') 
except:
    model = joblib.load('explore__Random-Forest__classification.h5')

st.title("Deteksi Anomali Transaksi Bank (Fraud Detection) 💳")

st.markdown("""
<div style="text-align: justify;">
Aplikasi ini merupakan simulasi implementasi <i>Machine Learning</i> untuk mendeteksi transaksi keuangan yang tidak wajar. <br><br>

Model <b>Random Forest</b> di balik aplikasi ini telah dilatih menggunakan data historis perbankan untuk mengenali pola-pola anomali berdasarkan rasio nominal transaksi, durasi, status akun, dan demografi pelanggan. <br><br>

<b>Cara Penggunaan:</b><br>
Ubah parameter pelanggan di <i>sidebar</i> sebelah kiri untuk menguji apakah kombinasi transaksi tersebut masuk dalam kategori <b>Aman (Normal)</b> atau memerlukan pengawasan lebih lanjut <b>(Indikasi Fraud)</b>.
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# --- KAMUS MAPPING (Dari Teks ke Angka untuk Model) ---
map_trans_type = {'Credit': 0, 'Debit': 1}
map_channel = {'ATM': 0, 'Branch': 1, 'Online': 2}
map_occupation = {'Doctor': 0, 'Engineer': 1, 'Retired': 2, 'Student': 3}
map_age_group = {'Dewasa': 0, 'Muda': 1, 'Tua': 2}
map_location = {
    'Albuquerque': 0, 'Atlanta': 1, 'Austin': 2, 'Baltimore': 3, 'Boston': 4, 
    'Charlotte': 5, 'Chicago': 6, 'Colorado Springs': 7, 'Columbus': 8, 'Dallas': 9, 
    'Denver': 10, 'Detroit': 11, 'El Paso': 12, 'Fort Worth': 13, 'Fresno': 14, 
    'Houston': 15, 'Indianapolis': 16, 'Jacksonville': 17, 'Kansas City': 18, 
    'Las Vegas': 19, 'Los Angeles': 20, 'Louisville': 21, 'Memphis': 22, 'Mesa': 23, 
    'Miami': 24, 'Milwaukee': 25, 'Nashville': 26, 'New York': 27, 'Oklahoma City': 28, 
    'Omaha': 29, 'Philadelphia': 30, 'Phoenix': 31, 'Portland': 32, 'Raleigh': 33, 
    'Sacramento': 34, 'San Antonio': 35, 'San Diego': 36, 'San Francisco': 37, 
    'San Jose': 38, 'Seattle': 39, 'Tucson': 40, 'Virginia Beach': 41, 'Washington': 42
}

# 2. Form Input Sidebar dengan UI yang lebih manusiawi (Dropdown Text)
st.sidebar.header("Input Data Pelanggan")

transaction_amount = st.sidebar.number_input("Transaction Amount ($)", min_value=0.0, value=150.0)
customer_age = st.sidebar.number_input("Customer Age", min_value=17, max_value=100, value=25)
transaction_duration = st.sidebar.number_input("Transaction Duration (Detik)", min_value=0.0, value=120.0)
login_attempts = st.sidebar.number_input("Login Attempts", min_value=0, max_value=20, value=1)
account_balance = st.sidebar.number_input("Account Balance ($)", min_value=0.0, value=5000.0)

st.sidebar.markdown("---")
# st.sidebar.subheader("Data Kategorikal")
# User memilih teks di Dropdown
input_trans_type = st.sidebar.selectbox("Transaction Type", list(map_trans_type.keys()))
input_location = st.sidebar.selectbox("Location (City)", list(map_location.keys()))
input_channel = st.sidebar.selectbox("Channel", list(map_channel.keys()))
input_occupation = st.sidebar.selectbox("Customer Occupation", list(map_occupation.keys()))
input_age_group = st.sidebar.selectbox("Age Group", list(map_age_group.keys()))

# 3. Kumpulkan Input (Translate teks yang dipilih jadi angka lewat Kamus Mapping)
input_data = pd.DataFrame({
    'TransactionAmount': [transaction_amount],
    'TransactionType': [map_trans_type[input_trans_type]],
    'Location': [map_location[input_location]],
    'Channel': [map_channel[input_channel]],
    'CustomerAge': [customer_age],
    'CustomerOccupation': [map_occupation[input_occupation]],
    'TransactionDuration': [transaction_duration],
    'LoginAttempts': [login_attempts],
    'AccountBalance': [account_balance],
    'AgeGroup': [map_age_group[input_age_group]]
})

# Tampilan untuk verifikasi (Bisa kamu hapus/komen kalau tidak ingin dimunculkan)
st.subheader("Detail Transaksi yang Sedang Dianalisis:")
st.dataframe(input_data)

# 4. Tombol Eksekusi
if st.button("Lakukan Klasifikasi", type="primary"):
    hasil_prediksi = model.predict(input_data)
    
    st.markdown("---")
    st.subheader("Hasil Klasifikasi:")
    # Sesuaikan pesan dengan definisi label target dataset-mu (Contoh: 1 = Berisiko, 0 = Aman)
    if hasil_prediksi[0] == 1:
        st.error("⚠️ **Kategori 1:** Transaksi Memerlukan Perhatian Khusus (Fraud / Anomali).")
    else:
        st.success("✅ **Kategori 0:** Transaksi Normal / Aman.")