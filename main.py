from youtube_transcript_api import YouTubeTranscriptApi

video_id = 'zaZrWZwKJH4'

try:
    transcript_list = YouTubeTranscriptApi.list_transcripts(video_id)
except Exception as e:
    print(f"Erro ao listar transcrições: {e}")
    exit()

try:
    transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=['en', 'pt'])
    with open('legenda.txt', 'w', encoding='utf-8') as f:
        for item in transcript:
            f.write(item['text'] + ' ')
except Exception as e:
    print(f"Erro ao obter a transcrição: {e}")

if transcript_list:
    try:
        transcript_en = transcript_list.find_transcript(['en'])
        translated_transcript = transcript_en.translate('pt')
        transcript_data = translated_transcript.fetch()
        with open('legenda_pt.txt', 'w', encoding='utf-8') as f:
            for item in transcript_data:
                f.write(item['text'] + ' ')
    except Exception as e:
        print(f"Erro ao traduzir a transcrição: {e}")