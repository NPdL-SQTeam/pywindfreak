# pywindfreak

Python driver for the [Windfreak Technologies SynthHD Mini](https://windfreaktech.com/product/synthhd-mini/) RF signal generator.

## Installation

Install from a private GitHub repository using a Personal Access Token (PAT):

```bash
pip install git+https://<PAT>@github.com/<username>/pywindfreak.git
```

Replace `<PAT>` with your GitHub Personal Access Token and `<username>` with the repository owner's GitHub username.

> The GitHub repository URL is TBD and will be updated once published.

## Usage

```python
from pywindfreak import SynthHDMini, ReferenceMode

# Pass the bare port name; the driver resolves the full path automatically.
# Examples: "tty.usbmodemXXXX" (macOS), "ttyACM0" (Linux), "COM6" (Windows)
synth = SynthHDMini("COM6")

# On init: rf_enable=False, reference_mode=ReferenceMode.EXTERNAL

synth.reference_mode = ReferenceMode.INTERNAL_27MHZ
synth.frequency = 1e9   # Hz
synth.power = -10.0     # dBm
synth.rf_enable = True

print(synth.frequency)  # 1000000000.0
print(synth.power)      # -10.0

synth.rf_enable = False
synth.close()
```

### `ReferenceMode` values

| Value | Description |
|---|---|
| `ReferenceMode.EXTERNAL` | External reference (default) |
| `ReferenceMode.INTERNAL_27MHZ` | Internal 27 MHz reference |
| `ReferenceMode.INTERNAL_10MHZ` | Internal 10 MHz reference |
