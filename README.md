# GPT2xHoudini_experiment
Edited by Racelar Ho, 20/09/2020
## preparations 
`*if you want to keep training the data`
1. **Tensorflow-gpu==1.12.0**
2. ``` conda create -n tensorflow python=3.6```
3. ``` conda activate tensorflow```
    * (***Ubuntu tested***) ``` pip3 install tensorflow==1.12.0``` || ```pip3 install tensorflow-gpu==1.12.0``` 
    * (***Windows tested-01***)``` pip install tensorflow==1.12.0``` || ```pip install tensorflow-gpu==1.12.0```
    * (***Windows tested-02 [recommend]***)``` conda install tensorflow=1.12.0``` 
4. ```pip3 install -r requirements.txt```
5. ```python download_model.py 117M```
6.  ```python train.py --dataset DitionaryAE.npz --sample_every 50 --sample_num 3 --learning_rate 0.0001 --batch-size 1```

## Note
1. `checkpoint/run1` is employed **`117M`**;
2. `--batch-size` is employed **`1`** || if the tested GPU's compute capacity is around 6.1 (GTX 1050, 1060, 1070, 1080Ti, TitanX TitanXp), --batch-size need to assign with **``1``**;

## issue report
1. **CUDA version in-compatible || CUDA = 10.0**
`2020-09-20 14:23:14.150572: W tensorflow/stream_executor/platform/default/dso_loader.cc:59] Could not load dynamic library 'cudart64_101.dll'; dlerror: cudart64_101.dll not found
2020-09-20 14:23:14.158934: I tensorflow/stream_executor/cuda/cudart_stub.cc:29] Ignore above cudart dlerror if you do not have a GPU set up on your machine.`
2. **Tensorflow-regex** `Traceback (most recent call last):
  File "train.py", line 14, in <module>
    import model, sample, encoder
  File "H:\00_my-proj\01_DL-ML\01_text\01_openai\04_GPT2xHoudini_experiment\GPT2xHoudini_experiment\src\encoder.py", line 5, in <module>
    import regex as re
  File "G:\Software_ANACONDA\envs\tensorflow\lib\site-packages\regex.py", line 394, in <module>
    import _regex_core
  File "G:\Software_ANACONDA\envs\tensorflow\lib\site-packages\_regex_core.py", line 21, in <module>
    import _regex
ImportError: DLL load failed: The specified module could not be found.`
3. **Must only use Tensorflow-1.12.0** 
` from tensorflow.contrib.training import HParams
ModuleNotFoundError: No module named 'tensorflow.contrib'` 

> Contrib does not exist in 2.0 or later. If we need `contrib` we have to use `1.15`, although we recommend upgrading code to the contrib alternatives (since they are being actively maintained by an owner, unlike `contrib` which doesn't have an owner to fix issues)
