import os
from openpyxl import load_workbook 


path=r'파일경로' #파일 경로입력하기(이미지들 모인 곳)
file_names = os.listdir(path)

load_wb = load_workbook(r"파일경로\엑셀제목.xlsx", data_only=True) #엑셀 파일 경로, 이름
load_ws = load_wb['엑셀 시트 이름'] #엑셀 시트 이름
get_cells = load_ws['D2':'D800'] #엑셀의 어느 위치 이름들로 바꿔줄 건지

for i in range(799):
    if 'zip' in file_names[i]: #압축파일일 경우
        os.rename(path+file_names[i],path+str(get_cells[i][0].value)+'.zip')
    else: #이미지(jpg형식)일 경우
        os.rename(path + file_names[i], path + str(get_cells[i][0].value) + '.jpg')
