from snowboy import snowboydecoder_audiorecorder
import sys
import signal
import speech_recognition as sr
import os
import uuid
# from matrixio_hal import everloop

from wit_module import wit_module
import set_everloop_color as ec
# import led_rotate as lr

"""
This demo file shows you how to use the new_message_callback to interact with
the recorded audio after a keyword is spoken. It uses the speech recognition
library in order to convert the recorded audio into text.
Information on installing the speech recognition library can be found at:
https://pypi.python.org/pypi/SpeechRecognition/
"""

ec.set_everloop_color()
interrupted = False
end_animation = False

wit_object = wit_module.CallWit()

def generate_session_id():
    session_id = uuid.uuid4()
    return session_id

def audioRecorderCallback(fname):
    r = sr.Recognizer()
    with sr.AudioFile(fname) as source:
        audio = r.record(source)  # read the entire audio file

    print "Understanding what you said ..."
    # recognize speech using Google Speech Recognition
    try:
        # for testing purposes, we're just using the default API key
        # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        # instead of `r.recognize_google(audio)`
        response = r.recognize_google(audio)
        print "You said : {}".format(response)
        session_id = generate_session_id()
        wit_object.handle_message(session_id=session_id, user_query=response)
        ec.set_everloop_color(red=10, blue=5)
    except sr.UnknownValueError:
        print "Google Speech Recognition could not understand audio"
        ec.set_everloop_color(red=10)
    except sr.RequestError as e:
        print "Could not request results from Google Speech Recognition service; {0}".format(e)

    # os.remove(fname)


def detectedCallback():
  sys.stdout.write("recording audio...")
  sys.stdout.flush()

def hotwordDetected():
    ec.set_everloop_color(green=10)
    #snowboydecoder_audiorecorder.play_audio_file()
    print "I'm listening ..."

def signal_handler(signal, frame):
    global interrupted
    interrupted = True


def interrupt_callback():
    #ec.set_everloop_color(red=10)
    global interrupted
    return interrupted

if len(sys.argv) == 1:
    print "Error: need to specify model name"
    print "Usage: python demo.py your.model"
    sys.exit(-1)

model = sys.argv[1]

# capture SIGINT signal, e.g., Ctrl+C
signal.signal(signal.SIGINT, signal_handler)

detector = snowboydecoder_audiorecorder.HotwordDetector(model, sensitivity=0.38)
print "Listening... Press Ctrl+C to exit"
#ec.set_everloop_color(red=10, blue=10)
# main loop
detector.start(detected_callback=hotwordDetected,
               audio_recorder_callback=audioRecorderCallback,
               interrupt_check=interrupt_callback,
               sleep_time=0.08)

ec.set_everloop_color()
detector.terminate()
