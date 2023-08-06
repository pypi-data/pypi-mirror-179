# hifigan
A wrapped hifi-gan vocoder for easy use. 

Source: https://github.com/jik876/hifi-gan

# Install

```bash
pip install hifigan-vocoder
```

# Usage
```python

from hifigan_vocoder import hifigan, get_sample_mel

mel = get_sample_mel()
print(mel.shape) # torch.Size([1, 80, 2062])

model = hifigan(dataset='uni', device='cpu') # dataset in ['uni', 'vctk']; device in ['cpu', 'cuda']; checkpoint will be downloaded from google driver.

audio = model.infer(mel)
print(mel.shape) # (527872,)

```