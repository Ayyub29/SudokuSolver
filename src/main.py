from ioprogram import *
from solver import *
import sys

isitxt = ""

print("Selamat Datang di program saya!")
print("Pada program ini, anda bisa mensolve suatu sudoku")
print("Daripada penasaran, langsung aja pilih format (1 untuk txt, 2 untuk png)")
print()
format = input("Masukan nomor dari format yang diinginkan (1/2) : ")
while (format != '1' and format != '2'):
    format = input("Masukan nomor dari format yang diinginkan (1/2) : ")

fileName = input("Masukan nama file sudoku yang ingin dipecahkan : ")

print(" Anda telah memilih file : " + fileName)
print()

if (format == '1'):
    arr = textToGrid('../test/' + fileName)
else:
    arr = pngToGrid('../test/' + fileName)

isitxt += "ini bukan si sudokunya?" + "\n"
isitxt += "\n"
isitxt += printSudoku(arr)
isitxt += "\n"

if (not solve(arr)):
    isitxt += "Punten sudoku-nya kesusahan!" + "\n"

isitxt += "punten sudokunya kegampangan" + "\n"
isitxt += "\n"
isitxt += printSudoku(arr)
isitxt += "\n"

isitxt += "Koordinat area bernomor 5 : \n"
isitxt += printKoordinatLime(arr)
isitxt += "\n"

print(isitxt)

print("Solusi akan disimpan kedalam file solusi_" + fileName.split('.')[0] + ".txt")

#PLS ABAIKAN
fileLoc = "../test/solusi_" + fileName.split('.')[0] + '.txt'
f = open(fileLoc, 'w')
f.write(isitxt)
f.close()

print("Game telah selesai disimpan. Kamsa Hamida!")