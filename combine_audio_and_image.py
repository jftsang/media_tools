#!/usr/bin/env python3
import argparse
from typing import Optional, Sequence

from moviepy.editor import AudioFileClip, ImageClip


def main(argv: Optional[Sequence[str]] = None):
    parser = argparse.ArgumentParser()
    parser.add_argument("--audio", required=True)
    parser.add_argument("--image", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args(argv)

    audio_clip = AudioFileClip(args.audio)
    image_clip = ImageClip(args.image)
    clip = image_clip.set_duration(audio_clip.duration).set_audio(audio_clip)
    clip.write_videofile(args.output, fps=24)


if __name__ == "__main__":
    main()
