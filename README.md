# K9 Piper Voice
It has taken many hours over the last nine months to create a quality training set, but this repo contains two small neural based Piper Text To Speech (TTS) models that makes your Raspberry Pi sound just like K9. Unlike earlier efforts this will run quickly and locally on the Raspberry Pi. This is thanks to Michael Hanson's excellent Piper software.

The examples below were generated using the original model that was trained to 1,000 Epochs, but probably overfitted the training set. The alternative model was only trained for around 300 Epochs, and feels slightly more understandable, but is still clearly K9.

## Examples

### Rule 1
https://github.com/hopkira/k9_piper_voice/assets/5486945/faccfa9a-dd0d-465e-8e67-b28cb14bb0fe

### Rule 2
https://github.com/hopkira/k9_piper_voice/assets/5486945/8288f45d-9661-473c-ab21-c2065e168f1d

### Rule 3
https://github.com/hopkira/k9_piper_voice/assets/5486945/cebb2143-87e4-435a-9703-f7b4c4af1d64

## Instructions to use

To use the voice you will need to install [Piper software](https://github.com/rhasspy/piper) for the Raspberry Pi. To do this, you can download a binary release:

* [amd64](https://github.com/rhasspy/piper/releases/download/v1.2.0/piper_amd64.tar.gz) (64-bit desktop Linux)
* [arm64](https://github.com/rhasspy/piper/releases/download/v1.2.0/piper_arm64.tar.gz) (64-bit Raspberry Pi 4)
* [armv7](https://github.com/rhasspy/piper/releases/download/v1.2.0/piper_armv7.tar.gz) (32-bit Raspberry Pi 3/4)

Once this is done you can clone this repository.  You can then try out the model using:

```sh
echo 'I am kay nine mark five and I am a very good dog.' | \
  ./piper -m /path/to/k9_piper_voice/k9_model.onnx --output_file test.wav
```
