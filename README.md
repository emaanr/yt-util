# YouTube Utilities

    Small GUI application to perform some utilities related to YouTube.

# Table of Contents

- [YouTube Utilities](#youtube-utilities)
- [Table of Contents](#table-of-contents)
  - [Reason](#reason)
  - [Modules Used](#modules-used)
    - [`tk`](#tk)
    - [`pytube`](#pytube)
    - [`logging`](#logging)
    - [`argparse`](#argparse)
    - [`os`](#os)
    - [`re`](#re)
    - [`math`](#math)
  - [Stack](#stack)
  - [Use Guide](#use-guide)
  - [Notes](#notes)

## Reason

It can be helpful to know how much content is in a YouTube Playlist as well as how quickly you can get through it on various Playback Speeds. This is a feature I often find myself wanting, but YouTube doesn't natively support anything like this on their GUI. Additionally, I've gotten into listening to Podcasts recently so I wanted to include some way to parse the transcripts to make note-taking easier or to make the podcasts readable as well since sitting through an episode can be time consuming and inaccessible at times.

## Modules Used

- `tk`
- `pytube`
- `logging`
- `argparse`
- `os`
- `re`
- `math`

### `tk`

```
pip install tk
```

### `pytube`

```
pip install pytube
```

### `logging`

- Part of Python Standard Library, just need to `import`.

### `argparse`

- Part of Python Standard Library, just need to `import`.

### `os`

- Part of Python Standard Library, just need to `import`.

### `re`

- Part of Python Standard Library, just need to `import`.

### `math`

- Part of Python Standard Library, just need to `import`.

## Stack

- `Back End` Python
- `Front End` Tkinter
- `Data` PyTube

## Use Guide

To be updated once the application is finished.

## Notes

Ran into some issues with PyTube version 15.0.0 when trying to get video transcript. In order to ensure your fork/clone of this repo works, make the following change to the PyTybe `captions.py` file, specifically the `def xml_caption_to_srt(self, xml_captions: str) -> str` function which needs to be entirely replaced with the following code in order to work: [Issue #1085](https://github.com/pytube/pytube/issues/1085#issuecomment-950327958) via community contribution.

Also, used this regex code written by community member: [pgngp](https://stackoverflow.com/a/51073232).
