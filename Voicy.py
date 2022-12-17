import speech_recognition as sr #음성 인식하는 라이브러리

class Voices:
    def Command(self):
        r = sr.Recognizer() #인스턴스 생성

        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source) #주변 소음이 있는 경우 활성화

            print("Say Command")

            audio = r.listen(source) #음성인식

            print("Recognizing Now....")

            try:
                said = r.recognize_google(audio,language="ko-KR") #said변수에 음성 저장

                print("You said \n" + said)

            except Exception as e:
                print("Error : "+str(e))

        if "이륙" in said:
            said = "이륙"
            return "이륙"

        elif "착륙" in said:
            said = "착륙"
            return "착륙"

        elif "오른쪽" in said:
            said = "오른쪽"
            return "오른쪽"

        elif "왼쪽" in said:
            said = "왼쪽"
            return "왼쪽"

        elif "위" in said:
            said = "위"
            return "위"

        elif "아래" in said:
            said = "아래"
            return "아래"

        elif "앞으로" in said:
            said = "앞으로"
            return "앞으로"

        elif "뒤로" in said:
            said = "뒤로"
            return "뒤로"

        return said

x = Voices()
x.Command()

