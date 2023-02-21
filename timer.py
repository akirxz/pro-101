import time

from playsound import playsound
def counterdown_time(seconds):
    while seconds > 0:

        mins=int(seconds/60)
        secs=int(seconds%60)

        timer=f'{mins}:{secs}'
        print(timer, end='\r')
        time.sleep(1)
        seconds-=1

    print("Tempo esgotado")
    playsound('mixkit-sound.wav')


seconds = input("Digite o tempo em segundos: ")

counterdown_time(int(seconds))