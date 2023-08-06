# hifigan
A wrapped hifi-gan vocoder for easy use. 

Source: https://github.com/jik876/hifi-gan

# Usage
```python

from hifigan_vocoder import hifigan, get_sample_mel

mel = get_sample_mel(dataset='uni', device='cpu') # dataset in ['uni', 'vctk']
print(mel.shape) # torch.Size([1, 80, 2062])

model = hifigan()
audio = model.infer(mel)
print(mel.shape) # (527872,)

```