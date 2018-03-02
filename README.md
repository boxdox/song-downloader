# Song-Downloader
---
*Note: Code is very poor, but functional xD. Don't blame me for anything, I was bored, thus this puked code was produced. Nonetheless, it WORKS! If you can improve the code, don't hesitate to open a pull request.*

With a basic usage of regex and some youtube-to-mp3 magic, this script can download any song for you.

Note: For popular songs, just the name of song will be enough, but for unpopular songs (or songs which are similarly named to other songs, please add the name of artist anywhere xD)

## Usage
There are two ways to use this script:
1. Use `song-downloader.py` and then enter your query in the following prompt.
2. Or if you are lazy like me, use command line arguments:
`song-downloader.py name of any song no need to worry about dashes or spaces`

Here's a gif (cause I CAN!)
<p align=center><img class="shadow" src="https://raw.githubusercontent.com/vaibhavkandwal/song-donwloader/master/usage.gif" /></p>

## Limitations
Sometimes, the downloading file results in some kb (kilobytes). This is because the youtube-to-mp3 is still converting the file and the script asks for download (I have added a time delay, still it doesn't work sometimes. _FACEPALM_).

In such cases, just re-run the script, it will overwrite the previous bad file.

Also, if the naming of the file is incorrect, please correct it yourself xD. Just kidding. I have this on my feature list.

## License
To be clear, this is just for educational purpose only. I don't recommend you to download your music library with this file. Also, it's only 128kbps quality (maybe even lower).

## To be added features:
1. List all results from YouTube before downloading.
2. Add a progress bar while downloading.
3. Custom output directory.
4. System-wide installation with pip.
5. Pip package, maybe :P
