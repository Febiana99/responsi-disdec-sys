# responsi-disdec-sys

***Nama : Febiana Serao Da Cruz***
***NIM : 235410032***

jawaban :<br>
**1. Pada bagian ini dilakukan implementasi YugabyteDB menggunakan Docker. Selanjutnya dibuat dua tabel dengan struktur bebas, kemudian masing-masing tabel diisi lima data. Dua tabel yang saya buat di sini adalah tabel Mahasiswa dan Tabel Mata Kuliah. Hasil implementasi dibuktikan melalui tampilan container Docker, daftar tabel, dan isi dari setiap tabel menggunakan ysqlsh.**

- Perintah docker ps digunakan untuk menampilkan container Docker yang sedang berjalan. Pada hasil yang ditampilkan, container yugabyte berstatus Up, sehingga dapat disimpulkan bahwa YugabyteDB berhasil dijalankan dan siap digunakan.
  <img width="740" height="150" alt="image" src="https://github.com/user-attachments/assets/f3637cda-a5ae-487e-b17c-2e1c928d3556" />

- Membuat Tabel, Mengisi Data dan Menampilkan Daftar Tabel<br>
<img width="634" height="850" alt="image" src="https://github.com/user-attachments/assets/85da824b-f090-4f50-8248-053c6f991cc9" /><br>
Perintah CREATE TABLE digunakan untuk membuat tabel, INSERT INTO untuk mengisi data, dan \dt untuk menampilakn tabel yang telah dibuat.<br>

- Menampilkan Data Tabel Mahasiswa<br>
<img width="434" height="200" alt="image" src="https://github.com/user-attachments/assets/e213a6c9-c0c1-4114-85b7-11d7fb8d0697" /><br>
Perintah SELECT * FROM mahasiswa digunakan untuk menampilkan seluruh data pada tabel mahasiswa sebagai bukti bahwa data berhasil ditambahkan.<br>

- Menampilkan Data Tabel Mata Kuliah<br>
<img width="421" height="200" alt="image" src="https://github.com/user-attachments/assets/0c93920c-dc5f-47e6-b6f5-0fcd40a04cd8" /><br>
Perintah SELECT * FROM mata_kuliah digunakan untuk menampilkan seluruh data pada tabel mata_kuliah sebagai bukti bahwa data berhasil ditambahkan.<br>

**2. Membuat REST API menggunakan Python yang akan mengekspos data yang telah dibuat tersebut menggunakan Python. Hasil bisa diakses melalui browser atau headless tool (curl) dalam format JSON.<br>**
- Hasil saat menjalankan REST API menggunakan perintah python app.py.<br>
<img width="740" height="200" alt="image" src="https://github.com/user-attachments/assets/b1387eeb-de23-45d6-9fb9-ee447fa932df" /><br>
Perintah python app.py digunakan untuk menjalankan REST API menggunakan Flask sehingga layanan dapat diakses melalui browser.<br>
  
- Hasil saat mengakses endpoint http://127.0.0.1:5000/.<br>
<img width="490" height="170" alt="image" src="https://github.com/user-attachments/assets/bfeba1ba-4463-4416-a561-eebdad755f5d" /><br>
Endpoint / digunakan untuk menampilkan pesan bahwa REST API berhasil dijalankan.<br>

- Hasil saat mengakses endpoint http://127.0.0.1:5000/mahasiswa.<br>
<img width="596" height="570" alt="image" src="https://github.com/user-attachments/assets/0f0377dd-b0eb-4cc7-a724-494a9c95c005" /><br>
Endpoint /mahasiswa digunakan untuk menampilkan seluruh data pada tabel mahasiswa dalam format JSON.<br>

- Hasil saat mengakses endpoint http://127.0.0.1:5000/mata_kuliah.<br>
<img width="600" height="600" alt="image" src="https://github.com/user-attachments/assets/9e78b5cb-4848-4565-beef-d58886905682" /><br>
Endpoint /mata_kuliah digunakan untuk menampilkan seluruh data pada tabel mata_kuliah dalam format JSON.<br>

**3. Memilih blockchain L1 selain Solana. Jelaskan mekanisme konsensus yang digunakan dan buat diagram mekanisme konsensus blockchain tersebut.**
- Blockchain Layer 1 yang Dipilih yaitu Ethereum<br>
Ethereum merupakan salah satu blockchain Layer 1 (L1) yang mendukung pembuatan dan menjalankan smart contract serta aplikasi terdesentralisasi (decentralized applications atau dApps). Berbeda dengan blockchain yang hanya digunakan untuk transaksi aset digital, Ethereum menyediakan platform yang memungkinkan pengembang membangun berbagai aplikasi berbasis blockchain. Sejak tahun 2022, Ethereum menggunakan mekanisme konsensus Proof of Stake (PoS) untuk memvalidasi transaksi dan menjaga keamanan jaringan.

- Mekanisme Konsensus Proof of Stake (PoS)<br>
  Proof of Stake (PoS) merupakan mekanisme konsensus yang memilih validator berdasarkan jumlah aset Ethereum (ETH) yang dikunci (stake) pada jaringan. Validator yang terpilih bertugas memverifikasi transaksi, membuat blok baru, dan memastikan seluruh transaksi yang diproses valid sebelum ditambahkan ke blockchain.<br>
  Proses dimulai ketika pengguna mengirimkan transaksi ke jaringan Ethereum. Selanjutnya, transaksi tersebut diterima oleh validator untuk dilakukan proses verifikasi. Validator yang dipilih berdasarkan mekanisme Proof of Stake akan memeriksa keabsahan transaksi, kemudian menyusun transaksi ke dalam sebuah blok. Setelah blok disetujui oleh validator lain sesuai aturan konsensus, blok tersebut ditambahkan ke blockchain sehingga transaksi menjadi permanen dan tidak dapat diubah.<br>
  Mekanisme Proof of Stake membuat proses validasi menjadi lebih hemat energi dibandingkan Proof of Work (PoW), karena tidak memerlukan proses penambangan menggunakan perangkat keras dengan konsumsi daya yang tinggi. Selain itu, mekanisme ini juga meningkatkan keamanan jaringan karena validator memiliki kepentingan untuk menjaga integritas blockchain sesuai dengan jumlah aset yang dipertaruhkan.

- Diagram Mekanisme Konsensus Ethereum (Proof of Stake)
<img width="390" height="840" alt="image" src="https://github.com/user-attachments/assets/47984fa4-cd79-421e-b022-64569e07083b" />


