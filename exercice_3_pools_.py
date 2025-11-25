# Ejercicio - Tenemos unos archivos de texto y queremos contar muy rapido (concurrencia) cuantas palabras o letras hay
from multiprocessing import Pool, cpu_count
import os, pytest, re

def file_len(file_url: str) -> int:
    try:
        with open(file_url) as f:
            content = f.read()
            words=content.split()
            letters = sum([len(re.sub(r'[^a-zA-Z]', '', w)) for w in words])
            return f.name, len(words), letters
    except Exception as e:
        print(e)
        return 0,0,0
        

if __name__ == "__main__":
    # current_directory = Path(".")
    # txt_files = [file for file in current_directory.iterdir() 
    #                 if file.is_file() and file.suffix == ".txt"]
    files = [f"files_exercice_3/file{i}.txt" for i in range(10)]
    p = Pool(cpu_count()-1)
    with p as pool:
        results = pool.map(file_len, files)
        
    for res in results:
        print("File len: ",res)
        

def test_smoke():
    filename = "test_temp.txt"
    with open(filename, "w", encoding="utf-8") as f:
        f.write("Hola mundo\nPython 123\n")

    try:
        path, words, letters = file_len(filename)
        assert path == filename
        assert words == 4
        assert letters == 15

    finally:
        if os.path.exists(filename):
            os.remove(filename)
 