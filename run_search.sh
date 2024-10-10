#!/bin/bash
# Meminta input dari pengguna
echo "Masukkan direktori tempat pencarian akan dilakukan:"
read search_dir
echo "Masukkan kata kunci yang akan dicari:"
read keyword
echo "Masukkan nama file log (misalnya, search_log.txt):"
read log_file
# Menanyakan apakah pengguna ingin mencetak isi file yang ditemukan
echo "Apakah Anda ingin menampilkan isi file yang ditemukan? (y/n)"
read show_content_choice
if [[ $show_content_choice == "y" ]]; then
 python3 search_text_in_files.py "$search_dir" "$keyword" "$log_file" --
show-content
else
 python3 search_text_in_files.py "$search_dir" "$keyword" "$log_file"
fi
echo "Pencarian selesai. Hasil pencarian telah disimpan di $log_file."
