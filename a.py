from youtube_transcript_api import YouTubeTranscriptApi

def transcription(video_id):
    # Set your proxy here
    YouTubeTranscriptApi._proxy = 'http://46.47.197.210	3128'

    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        return transcript
    except Exception as e:
        print("Transcript fetch failed 💔:", e)
        return None

tr=transcription('HvWlcpf48x4')
print (tr)

#https://www.youtube.com/watch?v=FqOi3NsT8cY&t=14s
# 34.81.72.31	80	TW	Taiwan	elite proxy	yes	no	5 secs ago
# #####72.10.160.172	28327	CA	Canada	elite proxy	no	yes	5 secs ago
# 46.47.197.210	3128	RU	Russian Federation	elite proxy		no	5 secs ago
# 139.59.1.14	80	IN	India	anonymous		no	5 secs ago
# 159.203.61.169	3128	CA	Canada	anonymous		no	5 secs ago
# 161.35.70.249	8080	DE	Germany	anonymous		no	5 secs ago
# 14.225.240.23	8562	VN	Vietnam	elite proxy		no	5 secs ago
# 31.47.42.140	1080	IR	Iran	anonymous	yes	no	5 secs ago
# 8.222.197.104	1080	SG	Singapore	elite proxy		no	5 secs ago
#https://www.youtube.com/watch?v=HvWlcpf48x4