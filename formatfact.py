from moviepy.editor import VideoFileClip

# Chemin d'accès à la vidéo d'origine
input_video_path = "presentation.mp4"

# Charger la vidéo
clip = VideoFileClip(input_video_path)

# Redimensionner la vidéo en 720p
clip_resized = clip.resize(height=720)

# Chemin d'accès pour sauvegarder la vidéo redimensionnée
output_video_path = "presentation1.mp4"


clip_resized.write_videofile(output_video_path, codec="libx264")
