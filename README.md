# K9 Piper Voice
This repo contains a Piper model that makes your Raspberry Pi sound just like K9.

To use the voice you will need to install Michael Hansen's [Piper software](https://github.com/rhasspy/piper) for the Raspberry Pi. To do this, you can download a binary release:

* [amd64](https://github.com/rhasspy/piper/releases/download/v1.2.0/piper_amd64.tar.gz) (64-bit desktop Linux)
* [arm64](https://github.com/rhasspy/piper/releases/download/v1.2.0/piper_arm64.tar.gz) (64-bit Raspberry Pi 4)
* [armv7](https://github.com/rhasspy/piper/releases/download/v1.2.0/piper_armv7.tar.gz) (32-bit Raspberry Pi 3/4)

Once this is done you can try out the model using:

```sh
echo 'I am kay nine mark five and I am a very good dog.' | \
  piper -m /path/to/k9_piper_voice/k9_model.onnx --output_file test.wav
```
