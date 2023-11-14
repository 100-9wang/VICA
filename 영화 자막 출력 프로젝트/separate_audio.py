#spleeter 모델 활용 환경음과 입력소리 분리 
#subprocess lib은 파이썬에서 쉘 명령 실행 가능하게 해줌
import subprocess
import os
import shutil

def separate_audio(file_name):
    command = 'spleeter separate -p spleeter:2stems -o output output_audio/'+ file_name
    # command = 'spleeter separate -p spleeter:2stems -o output output_audio/extracted_audio.wav'
    subprocess.run(command, shell=True)

    from_path = 'output/' + file_name.split(".")[0] + '/'
    to_path = 'output_audio/'
    files = ['vocals.wav', 'accompaniment.wav']
    rename_files = ['vocal.wav', 'environment.wav']
    for i in range(2):
        shutil.move(from_path + files[i], to_path + rename_files[i].split('.')[0] + '/' + rename_files[i])
    os.rmdir('output/' + file_name.split(".")[0])
    os.rmdir('output')
    print("---- Finish Audio Seperate ----")