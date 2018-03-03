# Song-Downloader
---
*Note: Code is very poor, but functional xD. Don't blame me for anything, I was bored, thus this puked code was produced. Nonetheless, it WORKS! If you can improve the code, don't hesitate to open a pull request.*

With a basic usage of regex and some youtube-to-mp3 magic, this script can download any song for you (of course, no magic, it's YouTube).

Note: For popular songs, just the title of song will work. Add artist name to get more precise results for songs that contain common words.

## Usage
There are two ways to use this script:
1. Use `song-downloader.py` and then enter your query in the following prompt.
2. Or if you are lazy like me, use command line arguments:
`song-downloader.py name of any song no need to worry about dashes or spaces`
Example: `song-downloader.py wherever you go bryan adams`

Here's a gif (cause I CAN!)
<p align=center><img src="https://raw.githubusercontent.com/vaibhavkandwal/song-donwloader/master/usage.gif" /></p>

## Limitations
Sometimes, the completed download may seem corrupted (or be of very small size ~ some kb). This is because our script requests file instantly, whereas the server might still be converting it (I have added a time delay, still it doesn't work sometimes. _FACEPALM_).

In such cases, just re-run the script, it will overwrite the previous failed download..

Also, if the naming of the file is incorrect, please correct it yourself xD. Just kidding. I have this on my feature list (maybe available on next update).

## License
To be clear, this is just for educational purpose only. The end user is **solely** responsible for his actions. (Who am I kidding :P). Also, YouTube compresses the audio to 128kbps (=shitty quality audio, for me xD)

## To be added features:
1. List out all possible videos, in case if two songs are similarly named.
2. Add a progress bar while downloading.
3. Custom output directory.
4. System-wide installation with pip, maybe :P.
