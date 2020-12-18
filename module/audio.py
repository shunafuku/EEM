from playsound import playsound
# import pyaudio
# import wave


def res_audio(audio_path) -> None:
    playsound(audio_path)
    # CHUNK = 44100
    # audio = pyaudio.PyAudio()
    # wf = wave.open(audio_file, 'rb')
    # stream = audio.open(
    #     format=audio.get_format_from_width(wf.getsampwidth()),
    #     channels=wf.getnchannels(),
    #     rate=wf.getframerate(),
    #     output=True
    # )
    # data = wf.readframes(CHUNK)
    # while data != b'':
    #     stream.write(data)
    #     data = wf.readframes(CHUNK)
    # stream.close()
    # audio.terminate()
