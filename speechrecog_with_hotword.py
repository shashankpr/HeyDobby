import os
import speech_recognition as sr
import uuid

from wit_module import wit_module

r = sr.Recognizer()
m = sr.Microphone()

ROOT = os.getcwd()
snowboy_location = os.path.join(ROOT, "snowboy")
snowboy_hotword = ["Dobby_S.pmdl"]
snowboy_params = (snowboy_location, snowboy_hotword)

def generate_session_id():
    session_id = uuid.uuid4()
    return session_id

def speech_text():

    wit_object = wit_module.CallWit()
    try:
        print("A moment of silence, please...")
        with m as source: r.adjust_for_ambient_noise(source)
        print("Set minimum energy threshold to {}".format(r.energy_threshold))
        while True:
            print("Say something!")
            with m as source: audio = r.listen(source, snowboy_configuration = snowboy_params)
            print("Got it! Now to recognize it...")
            try:
                # recognize speech using Google Speech Recognition
                response = r.recognize_google(audio)
                print(response.encode("utf-8"))
                session_id = generate_session_id()
                wit_object.handle_message(session_id=session_id, user_query=response)

                # we need some special handling here to correctly print unicode characters to standard output
                # if str is bytes:  # this version of Python uses bytes for strings (Python 2)
                #     print(u"You said {}".format(value).encode("utf-8"))
                # else:  # this version of Python uses unicode for strings (Python 3+)
                #     print("You said {}".format(value))
            except sr.UnknownValueError:
                print("Oops! Didn't catch that")
            except sr.RequestError as e:
                print("Uh oh! Couldn't request results from Google Speech Recognition service; {0}".format(e))
    except KeyboardInterrupt:
        pass

speech_text()
