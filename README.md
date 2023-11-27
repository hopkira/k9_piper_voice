# K9 Piper Voice
It has taken many hours over many momths to create a training set, but this repo contains a Piper Text To Speech (TTS) model that makes your Raspberry Pi sound just like K9. Unlike earlier efforts this will run locally on the Raspberry Pi. This is thanks to Michael Hanson's excellent Piper software.

## Examples
![Rule][https://github.com/hopkira/k9_piper_voice/raw/main/rule1.mp4)

## Instructions to use

To use the voice you will need to install [Piper software](https://github.com/rhasspy/piper) for the Raspberry Pi. To do this, you can download a binary release:

* [amd64](https://github.com/rhasspy/piper/releases/download/v1.2.0/piper_amd64.tar.gz) (64-bit desktop Linux)
* [arm64](https://github.com/rhasspy/piper/releases/download/v1.2.0/piper_arm64.tar.gz) (64-bit Raspberry Pi 4)
* [armv7](https://github.com/rhasspy/piper/releases/download/v1.2.0/piper_armv7.tar.gz) (32-bit Raspberry Pi 3/4)

Once this is done you can clone this repository.  You can then try out the model using:

```sh
echo 'I am kay nine mark five and I am a very good dog.' | \
  piper -m /path/to/k9_piper_voice/k9_model.onnx --output_file test.wav
```
