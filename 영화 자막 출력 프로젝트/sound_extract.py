import os
import moviepy.editor as mp
#ffmpeg를 사용하는 방법도 고려
#spleeter 메모리 문제 -> 9분단위로 나눠 추출

def sound_extract():
    input_path = 'input_moive/'
    output_path = 'output_audio/'
    moive_file = os.listdir(input_path)[0]
    videoclip = mp.VideoFileClip(input_path + moive_file)
    videolength = videoclip.duration
    dur = 0
    num = 0
    while dur+540 < videolength:
        clip = videoclip.subclip(dur, dur+540)
        audioclip = clip.audio
        audioclip.write_audiofile(output_path + 'extracted_audio_' + str(num).rjust(2, '0') + '.mp3')
        dur += 540
        num += 1

    clip = videoclip.subclip(dur, int(videolength)-1)
    audioclip = clip.audio
    audioclip.write_audiofile(output_path + 'extracted_audio_' + str(num).rjust(2, '0') + '.mp3')
    print("---- Finish Audio Extract ----")

    import moviepy.editor as mp

#사용 방법
#videoclip = mp.VideoFileClip(moive_file)
#clip = videoclip.subclip(start, end)
#audioclip = clip.audio
#audioclip.write_audiofile(save_path)