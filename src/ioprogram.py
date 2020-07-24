import pytesseract as tess
import os, fnmatch
import solver
from PIL import Image


# Prosedur untuk mencetak sudoku kebentuk string
# Disimpan dalam bentuk string untuk memudahkan penulisan di file eksternal
def printSudoku(sudoku):
    res = ""   
    for i in range(9):
        for j in range(8):
            res += str(sudoku[i][j]) + ' '
        res += str(sudoku[i][8]) + "\n"
    return res

# Prosedur untuk mencetak koordinat 5 pada sudoku
# Disimpan dalam bentuk string untuk memudahkan penulisan di file eksternal
def printKoordinatLime(sudoku):
    res = ""
    for i in range(9):
        for j in range(9):
            if (sudoku[i][j] == 5):
                res += "(" + str(i+1) + ", " + str(j+1) + ") "
    return res

# Prosedur untuk mengubah txt menjadi sudoku berbentuk array 2 dimensi
def textToGrid(path):
    arr = []
    with open(path, 'r') as f:
        #untuk setiap baris pada file eksternal membuat baris baru pada array
        for row in f:
            arr.append(row.split())
    for i in range(9):
        for j in range(9):
            if (arr[i][j] == '#'):
                arr[i][j] = 0
            else:
                arr[i][j] = int(arr[i][j])
    return arr

def pngToGrid(path):
    tess.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

    img = Image.open(path)
    width, height = img.size
    arr = [[0 for i in range(9)] for i in range(9)]

    img = img.crop((1, 1, width - 1, height - 1))

    for i in range(9):
        for j in range(9):
            left = 32 * j + 4
            top = 32 * i + 2.5
            right = left + 32 - 9
            bottom = top + 32 - 7

            img1 = img.crop((left, top, right, bottom))
            text = tess.image_to_string(img1, config='--psm 10 --oem 3 -c tessedit_char_whitelist=0123456789')
            
            if (text == ''):
                arr[i][j] = 0
            else:
                arr[i][j] = int(text)  

    return arr 

