from gtts import gTTS

quote = "On April 22, 2020, Jainapse was selected as the official supply company of \
        aiboucher support business hosted by science technology information communication industry promotion agency. \
        Aiboucher support business is a policy that allows small venture companies to raise corporate competitive competitive, \
        up to 3 billion won in the company that wants to implement ai technology. Issuance of the cheoleul."

file_name = "jainapse_intro_eng.mp3"

tts = gTTS(text=quote, lang="en")

tts.save(file_name)
