# Customer Segmentation & Classification: An End-to-End Machine Learning Project

## 📌 Deskripsi Proyek
Proyek ini bertujuan untuk menganalisis dan mengelompokkan perilaku nasabah berdasarkan data transaksi dan demografi, kemudian membangun model prediktif untuk mengklasifikasikan nasabah baru ke dalam segmen yang tepat. Proyek ini sangat relevan untuk kebutuhan **Customer Analytics**, khususnya dalam menentukan strategi pemasaran yang dipersonalisasi.

## 🛠️ Tech Stack
* **Bahasa:** Python
* **Data Manipulation & Analysis:** Pandas, NumPy
* **Data Visualization:** Matplotlib, Seaborn
* **Machine Learning:** Scikit-Learn (K-Means, PCA, Decision Tree, Random Forest, GridSearchCV)

## 📊 Alur Kerja (Workflow)
1. **Exploratory Data Analysis (EDA) & Preprocessing:** Pembersihan data, penanganan *missing values*, dan *encoding* fitur kategorikal.
2. **Unsupervised Learning (Clustering):** Menggunakan **K-Means** dan *Elbow Method* untuk menemukan jumlah klaster optimal. Mengimplementasikan **PCA (Principal Component Analysis)** untuk reduksi dimensi.
3. **Data Interpretation (Inverse Transform):** Mengembalikan data yang telah di-*scale* ke nilai aslinya untuk menemukan persona nyata dari setiap klaster.
4. **Supervised Learning (Classification):** Melatih model **Decision Tree** dan **Random Forest** menggunakan label dari hasil *clustering*. Melakukan *Hyperparameter Tuning* yang menghasilkan akurasi dan F1-Score sebesar 100%.

## 💡 Key Insights (Hasil Segmentasi)
Berdasarkan hasil *Inverse Transform*, ditemukan 2 persona nasabah yang sangat kontras:
* **Cluster 0 (Established Professionals):** Didominasi oleh usia Dewasa (profesi Mayoritas: Dokter). Memiliki saldo rata-rata tertinggi dan sangat berhati-hati dalam bertransaksi (durasi transaksi paling lama).
* **Cluster 1 (Academic/Younger Users):** Didominasi oleh usia Muda (profesi Mayoritas: Mahasiswa). Saldo lebih rendah namun memiliki frekuensi transaksi yang cepat dan nilai transaksi rata-rata yang kompetitif.

## 🚀 Cara Menjalankan Proyek
1. Clone repository ini.
2. Buka file `[Clustering]_Submission_Akhir.ipynb` untuk melihat proses segmentasi.
3. Buka file `[Klasifikasi]_Submission_Akhir.ipynb` untuk melihat proses pemodelan prediktif.


## 🏆 Acknowledgement
Proyek ini merupakan submission akhir untuk kelulusan kelas **"Membangun Model Machine Learning"** yang diselenggarakan oleh **Dicoding Indonesia** bekerja sama dengan **DBS Foundation**.
* **Status Kelulusan:** Lulus
* **Sertifikat:** https://www.dicoding.com/certificates/4EXG19LNDPRL


## ⚠️ Keterbatasan Model & Area Pengembangan (Future Works)
Selama proses *stress-testing* pada model **Random Forest** yang telah di-*deploy*, ditemukan beberapa karakteristik dan batasan dari model ini:

1. **Kuat pada Anomali Transaksional:** Model sangat sensitif dan akurat dalam mendeteksi *fraud* yang bersifat transaksional matematis. Misalnya, model berhasil mendeteksi anomali ketika seorang pelanggan dengan profesi Mahasiswa (Student) melakukan transfer dana yang jumlahnya jauh melebihi sisa saldo di rekeningnya.
2. **Keterbatasan pada Anomali Keamanan Siber (Cybersecurity):** Model saat ini memiliki *blind spot* terhadap skenario pengambilalihan akun (*Account Takeover*). Sebagai contoh, model gagal mendeteksi aktivitas mencurigakan berupa percobaan *login* yang gagal berkali-kali (indikasi *brute-force*). 
3. **Penyebab & Solusi:** Hal ini wajar terjadi karena *imbalanced data* dan kurangnya variasi kasus *cyber-fraud* ekstrem pada dataset BMLP yang digunakan saat *training*. Sebagai pengembangan ke depan, model perlu dilatih ulang (retrain) menggunakan teknik *Synthetic Minority Over-sampling Technique* (SMOTE) atau menyuntikkan data sintetik yang memuat skenario serangan *brute-force*.