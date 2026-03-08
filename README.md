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
* **Status Kelulusan:** Lulus dengan predikat Sangat Memuaskan (Skilled/Advanced)
* **Sertifikat:** https://www.dicoding.com/certificates/4EXG19LNDPRL