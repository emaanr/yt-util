# This file will contain the functions to be invoked via interactions with the GUI

import os
import re
import math
from pytube import Playlist, YouTube

def get_videos_in_playlist(playlist_id):
    videos_in_playlist = []
    playlist = Playlist(f"https://www.youtube.com/playlist?list={playlist_id}")

    for video in playlist:
        video = YouTube(video)
        videos_in_playlist.append(video)

    return videos_in_playlist

# Return total duration in seconds of videos in playlist
def get_total_duration(videos_in_playlist):
    playlist = videos_in_playlist
    total_dur = 0
    for video in playlist:
        total_dur += video.length
    return total_dur

# Calculate duration in specified unit
def get_duration_in_unit(duration, unit):
    match unit:
        case "seconds":
            seconds = duration
            return f"{seconds} Seconds"
        case "minutes":
            minutes, seconds = divmod(duration, 60)
            return f"{minutes} Minutes, {seconds} Seconds"
        case "hours":
            hours, remainder = divmod(duration, 3600)
            minutes, seconds = divmod(remainder, 60)
            return f"{hours} Hours, {minutes} Minutes, {seconds} Seconds"
        case "days":
            days, remainder = divmod(duration, 86400)
            hours, remainder = divmod(remainder, 3600)
            minutes, seconds = divmod(remainder, 60)
            return f"{days} Days, {hours} Hours, {minutes} Minutes, {seconds} Seconds"
        case "weeks":
            return "That's concerning..."
        case "months":
            return "Whoa there buddy..."
        case "years":
            return "Ain't no way..."
        case "decades":
            return "I respect the commitment, but no..."
        case "century":
            return "R.I.P."


# Apply playback speed to passed duration
def apply_playback_speed(duration, playback_speed):
    match playback_speed:
        case 0.25:
            duration *= 4
        case 0.5:
            duration *= 2
        case 0.75:
            duration *= (4 / 3)
        case 1:
            duration *= 1
        case 1.25:
            duration /= (5 / 4)
        case 1.5:
            duration /= (3 / 2)
        case 1.75:
            duration /= (7 / 4)
        case 2:
            duration /= 2
    return math.ceil(duration)

# Get video transcript
def get_transcript(video):
    video = YouTube(video)
    video.bypass_age_gate()
    captions = video.captions
    caption_track = captions['en']
    
    transcript = ''
    if caption_track:
        caption_track.download('captions', srt=True)
        with open('captions (en).srt', 'r', encoding='utf-8') as file:
            lines = file.readlines()
            for line in lines:
                if re.search('^[0-9]+$', line) is None and re.search('^[0-9]{2}:[0-9]{2}:[0-9]{2}', line) is None and re.search('^$', line) is None:
                    transcript += ' ' + line.rstrip('\n')
                    transcript = transcript.lstrip()
    os.remove('captions (en).srt')
    return transcript

# Export transcript to specified file
def export_transcript(video, output_filename):
    output_filename = f'{output_filename}.md'
    transcript = get_transcript(video)
    with open(output_filename, 'w', encoding='utf-8') as file:
        file.write(transcript)