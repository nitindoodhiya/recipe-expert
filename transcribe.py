from deepgram import DeepgramClient, PrerecordedOptions 
import yt_dlp as ytDlp
from datetime import datetime

HOST_URL = "https://0b6a-171-50-224-17.ngrok-free.app/public/audios/"
DEEPGRAM_API_KEY = ""

class Transcribe:
    def deepgramTranscribe(self, url):
        try: 
            deepgram = DeepgramClient(DEEPGRAM_API_KEY) 
            options = PrerecordedOptions(
                model="whisper-large", 
                language="en", 
                smart_format=True, 
            )

            audioUrl = {
                "url": url
            }

            response = deepgram.listen.prerecorded.v('1').transcribe_url(audioUrl, options) 
            return response
        except Exception as e: 
            print(f'Exception: {e}') 

    def downloadAudioFromYoutube(self, url):
        output_path = "./public/audios/"
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        filename = f"{timestamp}.mp3"

        options = {
            'format': 'bestaudio/best',
            'extractaudio': True,
            'audioformat': 'mp3',
            'outtmpl': output_path + filename,
        }

        with ytDlp.YoutubeDL(options) as ydl:
            infoDict = ydl.extract_info(url, download=True)

        return filename

    def transcribe(self, videoUrl):
        try:
            downloadedFile = self.downloadAudioFromYoutube(videoUrl)
            print(f"Audio downloaded to: {downloadedFile}")
            url = HOST_URL + downloadedFile
            response = self.deepgramTranscribe(url)
            return response.results.channels[0].alternatives[0].transcript

        except Exception as e:
            print(f'Exception: {e}')
            return None

        