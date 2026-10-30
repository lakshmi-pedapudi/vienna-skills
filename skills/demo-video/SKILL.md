---
name: demo-video
description: Use when making a product demo, explainer, walkthrough or launch video: a short video of how a product, system or method works, built from raw footage, from screens rebuilt in HTML, or both. Routes the work to the video-use and HyperFrames skills and sets the evidence rules for what may appear on screen. Triggers: "/demo-video", "demo video", "explainer video", "product walkthrough video", "launch video", "turn this into a video".
---

# Demo Video

## Overview

A thin house layer over two open-source tools that Claude Code drives directly:

| Tool | Skills it installs | What it does | Licence |
|------|--------------------|--------------|---------|
| video-use (browser-use) | `video-use` | Edits raw footage by conversation: cuts filler and dead air, grades colour, adds fades, burns subtitles, adds overlays | MIT |
| HyperFrames (HeyGen) | `hyperframes`, `hyperframes-cli`, `hyperframes-registry`, `media-use` | Builds video from HTML/CSS scenes that headless Chrome renders frame by frame to MP4 | Apache-2.0 |

This skill picks the route, owns the storyboard and the evidence rules, and hands each step to those skills.

**Core principle:** a demo video is evidence in motion. Anything shown as working must work, and anything rebuilt for the video must read as an illustration, not a recording.

## When to Use

- A product demo, walkthrough or launch clip for a customer, partner, funder or internal audience.
- An explainer of a method or architecture (animated diagrams, step-by-step flows).
- A recorded backup for a live demo.
- Not for: slide decks (`/deck`), static pages (`/artifact`).

## Inputs

- The audience and what they should believe at the end.
- Footage (screen recordings, talking head), or screenshots and a product URL, or only a description of the flow.
- Any numbers to show, each with its source.

## Outputs

- `storyboard.md`: numbered scenes with on-screen text, voiceover line and source.
- `preview.mp4` per scene and for the whole, then `final.mp4`.

## Workflow

**Setup (once per laptop).** `tools/video/setup.sh` in this repo clones both tools at pinned commits, links their skills into `~/.claude/skills`, and installs video-use's Python dependencies. It is safe to re-run, and it prints what is still missing: ffmpeg and ffprobe on the PATH; Node 22+ (HyperFrames runs through `npx hyperframes`); an ElevenLabs API key in `<video-use>/.env` (video-use transcribes with ElevenLabs Scribe; never commit the key). Run video-use helpers with its own environment: `uv run --project ~/.local/share/claude-vendor/video-use python helpers/<name>.py`.

**Pick the route.**

```
footage exists (screen recording, talking head)     no footage (a flow, an idea, a UI story)
                │                                                  │
            video-use                                      HyperFrames scenes
   transcript → cuts → grade → subtitles          storyboard → one scene at a time
                │                                                  │
                └──────── overlays and title cards via HyperFrames ┘
                                         ▼
                               preview.mp4 → review → final.mp4
```

1. **Real product, working flow:** record the screen, then edit with video-use. This is the only route that proves the product works.
2. **Method or architecture explainer:** HyperFrames scenes.
3. **Polished tour of a UI:** HyperFrames rebuilds the screens in HTML with an animated cursor. It is an illustration (Quality Standards, rule 2).

**Build.**

1. Ask two checkpoint questions: who watches it and what they should believe at the end; how long (default 60 to 90 seconds).
2. Write `storyboard.md` and get it approved before building anything.
3. Build one scene at a time. Render a preview of each and show it before starting the next.
4. Voiceover: a free local voice (`npx hyperframes tts`, Kokoro on device) by default; a paid voice only when the person asks for it.
5. Assemble, render the full preview, run the review below, and render `final.mp4` only after a pass finds nothing.

## Quality Standards

**Evidence rules.**

1. **No invented numbers on screen.** Every metric, count or result comes from a named source. A missing number stays out of the video.
2. **Rebuilt screens are illustrations.** A scene that shows a UI rebuilt in HTML must not pass as a live recording. Add a small "Illustrative" label, or use a real recording for any claim that something works.
3. **No sensitive data in frames.** No customer data, patient data, credentials, internal hostnames or real identifiers. Use synthetic data in rebuilt screens and scrub recordings before editing.
4. **Know where the media goes.** video-use sends the footage's audio to ElevenLabs. Do not send recordings that hold confidential speech or data; transcribe locally (`npx hyperframes transcribe`) or re-record.
5. **Licences for external use.** Free tiers of some voice services forbid commercial use. Use the local voice, or a paid plan the person has confirmed.
6. **Third-party marks.** Do not reproduce another company's product UI or logo in a public video without the right to do so.

**Review loop.** Watch the full preview against this list; fix and re-render until a pass finds nothing:

- Each scene matches the approved storyboard; nothing was added that was not approved.
- Captions are readable, never hidden by overlays, and in sync with speech.
- No cut inside a word; no audio pop at cuts.
- Every on-screen number traces to its source; every rebuilt screen is labelled.
- No sensitive data in any frame (step through frames, do not only play the video).

## Reference Guides

The tool skills carry their own references: `video-use` (`SKILL.md`, `helpers/`), `hyperframes` (render contract and work loop), `hyperframes-cli`, `hyperframes-registry` (about 450 ready-made blocks), `media-use` (voice, music, images, transcripts).

## Limitations

- HyperFrames renders what the HTML shows; it does not record or verify the real product.
- video-use needs footage and an ElevenLabs key; it does not generate video from nothing.
- Both tools are pinned upstream code. Bump the pins in `tools/video/setup.sh` deliberately; `setup.sh --latest` prints the upstream HEADs.

## Troubleshooting

| Symptom | Fix |
|---------|-----|
| `video-use` or `hyperframes` skill not found | Run `bash tools/video/setup.sh` from this repo |
| `npx hyperframes` fails | Install Node 22+ |
| Transcription fails | Add `ELEVENLABS_API_KEY` to `<video-use>/.env` |
| Helper import errors (`librosa`, `numpy`) | Run helpers through `uv run --project <video-use dir>` |
