# search_text_in_files.py
import os
import sys
def search_in_file(file_path, keyword):
 try:
 with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
 for line_num, line in enumerate(file, 1):
 if keyword.lower() in line.lower():
 return True
 return False
 except Exception as e:
 print(f"Error membaca file {file_path}: {e}")
 return False
def search_in_directory(directory, keyword, log_file, show_content=False):
 found_files = []

 for root, dirs, files in os.walk(directory):
 for file in files:
 if file.endswith(".txt"):
 file_path = os.path.join(root, file)
 if search_in_file(file_path, keyword):
 found_files.append(file_path)
with open(log_file, 'a') as log:
 log.write(f"Keyword '{keyword}' ditemukan di file:
{file_path}\n")
 print(f"Keyword '{keyword}' ditemukan di: {file_path}")

if show_content:
 print("Isi file:")
 with open(file_path, 'r', encoding='utf-8',
errors='ignore') as f:
 print(f.read())
 return found_files
if __name__ == "__main__":
 if len(sys.argv) < 4:
 print("Usage: python3 search_text_in_files.py <directory> <keyword>
<log_file> [--show-content]")
 sys.exit(1)
 directory = sys.argv[1]
 keyword = sys.argv[2]
 log_file = sys.argv[3]
 show_content = '--show-content' in sys.argv
 search_in_directory(directory, keyword, log_file, show_content)
