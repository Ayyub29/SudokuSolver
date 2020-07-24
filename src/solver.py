# Fungsi untuk mencari sel kosong pada sudoku
# input berupa array 2 dimensi yang melambangkan sudoku
# output berupa list yang berisikan lokasi sel kosong (baris,kolom)
# Jika tidak ada yang kosong, return false
def cariSelKosong(sudoku, pos): 
    for bar in range(9): 
        for kol in range(9): 
            if(sudoku[bar][kol]== 0): 
                pos[0]= bar 
                pos[1]= kol 
                return True
    return False
  
# Fungsi untuk mengkonfirmasi sel berisikan angka tertentu dalam suatu baris
# input berupa array 2 dimensi yang melambangkan sudoku, baris yang bersangkutan dan angka tertentu
# output berupa true jika sesuai dan false jika tidak sesuai
def cekdiBaris(sudoku, bar, num): 
    for i in range(9): 
        if(sudoku[bar][i] == num): 
            return True
    return False
  
# Fungsi untuk mengkonfirmasi sel berisikan angka tertentu dalam suatu kolom 
# input berupa array 2 dimensi yang melambangkan sudoku, baris yang bersangkutan dan angka tertentu
# output berupa true jika sesuai dan false jika tidak sesuai
def cekdiKolom(sudoku, kol, num): 
    for i in range(9): 
        if(sudoku[i][kol] == num): 
            return True
    return False
  
# Fungsi untuk mengkonfirmasi sel berisikan angka tertentu dalam suatu kotak 3x3
# input berupa array 2 dimensi yang melambangkan sudoku, kotak 3x3 terkait (dalam baris dan kolom) dan angka terkait
# output berupa true jika sesuai dan false jika tidak sesuai
def cekdiKotak(sudoku, bar, kol, num): 
    for i in range(3): 
        for j in range(3): 
            if(sudoku[i + bar][j + kol] == num): 
                return True
    return False
  
# Fungsi untuk mencek apakah lokasi tertentu bisa diletakkan nomor tertentu
# input berupa array 2 dimensi yang melambangkan sudoku, baris, kolom dan angka terkait
# output berupa true jika sesuai dan false jika tidak sesuai
def cekSelTersedia(sudoku, bar, kol, num): 
    return not cekdiBaris(sudoku, bar, num) and not cekdiKolom(sudoku, kol, num) and not cekdiKotak(sudoku, bar - bar % 3, kol - kol % 3, num) 
  
# Ya ini solvernya
# awalnya mencari dulu sel kosong di sudoku
# lalu di loop dari angka 1 hingga 10 untuk diisi
# program bersifat rekursif
def solve(sudoku): 
        
    pos = [0, 0]

    # mencari sel kosong pada sudoku
    if(not cariSelKosong(sudoku, pos)): 
        return True

    bar = pos[0] 
    kol = pos[1] 
      
    for num in range(1, 10): 
        if(cekSelTersedia(sudoku, bar, kol, num)): 
            sudoku[bar][kol] = num
            # jika sel bisa diletakkan angka tersebut, iterasi lagi 
            if solve(sudoku):
                return True
            # jika tidak, kosongkan sel
            else:
                sudoku[bar][kol] = 0     
    return False 