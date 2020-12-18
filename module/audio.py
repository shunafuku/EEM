import subprocess


def res_audio(audio_path) -> None:
    subprocess.call("aplay -D hw:1 " + str(audio_path), shell=True)
