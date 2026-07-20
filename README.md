# Implementasi dan Analisis Pengiriman Data Sensor Kelembapan Secara Aman Menggunakan HTTPS pada Platform Cloud Gratis Supabase

## Deskripsi Proyek

Proyek ini bertujuan untuk mengimplementasikan pengiriman data sensor kelembapan ke platform cloud Supabase menggunakan protokol HTTPS serta menganalisis keamanan komunikasi menggunakan Wireshark.

## Teknologi yang Digunakan

* Python
* Supabase
* HTTPS/TLS
* Wireshark

## Arsitektur Sistem

Data sensor dikirim menggunakan Python melalui REST API Supabase menggunakan protokol HTTPS. Lalu lalu lintas jaringan dianalisis menggunakan Wireshark untuk melihat proses TLS Handshake dan enkripsi data.

## Hasil

* Data berhasil tersimpan pada database Supabase.
* Server memberikan respons HTTP 201 Created.
* Wireshark menunjukkan penggunaan TLSv1.3 dengan proses Client Hello dan Server Hello.
* Isi data tidak dapat dibaca karena telah dienkripsi.

## Dokumentasi

Folder dokumentasi berisi diagram arsitektur, screenshot program, hasil penyimpanan data di Supabase, dan hasil capture Wireshark.
