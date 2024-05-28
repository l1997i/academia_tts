# Academia TTS

This python package provides tools to convert PPTX slide notes to audio files and embed them into the slides. This can be particularly useful for creating narrated presentations automatically.

## Install from pip
To install the package using pip, run:

```bash
pip install academia-tts
```

## Build from scratch

Or, you can build the package from scratch with:

```bash
git clone https://github.com/l1997i/academia_tts
pip install .
```

## How to Use

Ensure you **have a GPU available**, as the current implementation **requires CUDA** for generating audio from text.


### Embedding Audio into PPTX

To embed audio into the slides of a PowerPoint file based on the notes in each slide, use the following command:

```bash
tts_pptx example.pptx
```

This command will:

1.	Extract the notes from each slide in the example.pptx file.
2.	Generate audio files from the extracted notes.
3.	Embed the generated audio files into the corresponding slides.
4.	Save the modified PowerPoint file as output_<current_time>.pptx.

### Generating Audio Files from PPTX Notes

To generate audio files from the notes of each slide in a PowerPoint file, use the following command:

```bash
tts_output_wav example.pptx
```

This command will:

1.	Extract the notes from each slide in the example.pptx file.
2.	Generate audio files from the extracted notes.
3.	Save the generated audio files in a directory named output_wav_<current_time>.


## Troubleshooting

- If you encounter an error related to CUDA, make sure you are running the tool on a machine with a GPU and that CUDA is properly installed.
- Ensure the provided `pptx`` file path is correct and the file is accessible.
