
import librosa
import nussl
import soundfile as sf

# Séparation des sources avec nussl
def separate_audio_nussl(input_path, output_path):
    # Charger l'audio
    audio_signal = nussl.AudioSignal(input_path)


    separator = nussl.separation.non_negative_matrix_factorization.NMF(
        audio_signal, num_sources=2
    )

    # Séparer l'audio en deux sources
    estimates = separator()

    # Sauvegarder les fichiers séparés
    for i, estimate in enumerate(estimates):
        sf.write(f'{output_path}/source_{i}.wav', estimate.audio_data, estimate.sample_rate)

# Analyse et atténuation de la voix masculine
def attenuate_male_voice(input_path, output_path):
    y, sr = librosa.load(input_path, sr=None)

    # Analyse spectrale
    S_full, phase = librosa.magphase(librosa.stft(y))

    # Identifiez les fréquences de la voix masculine (généralement entre 85 et 180 Hz)
    male_voice_indices = (librosa.fft_frequencies(sr=sr) >= 85) & (librosa.fft_frequencies(sr=sr) <= 180)

    # Atténuer les fréquences de la voix masculine
    S_full[male_voice_indices] *= 0.1

    # Reconstituer le signal audio
    y_attenuated = librosa.istft(S_full * phase)

    # Sauvegarder le fichier atténué
    sf.write(output_path, y_attenuated, sr)

# Chemins des fichiers
input_audio_path = 'musique.mp3'
output_dir = 'output'

# Séparer les voix et l'accompagnement
separate_audio_nussl(input_audio_path, output_dir)

# Atténuer la voix masculine dans le fichier de voix séparées
input_voice_path = f'{output_dir}/source_0.wav'  # Assurez-vous que ce chemin correspond au fichier de voix séparées
output_voice_path = f'{output_dir}/vocals_attenuated.wav'
attenuate_male_voice(input_voice_path, output_voice_path)
