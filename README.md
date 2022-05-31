## Recognize pattern in image with correlation

> "One image can say more than a thousand word"

### Features:

- Processing image by correlation (segmented by stage)
- Unitary test and Integration test
- Jupyter notebook for experiments and running without Editor/IDE
- Documented
- Clean code and simple design

### Pre Requirements

- Python 3.6+
- PyCharm (recommended)

#### Steps:
- Terminal inside "local virtual env" (venv)
- For install python required libs on env, run:
```commandline
(env)$: pip install -r requirementtxt
```

### Experiment

__Example target image:__    
![alt-text][3]

__Example class patterns:__  
![alt-text](https://github.com/skatesham/image-recognization-by-correlation-python/blob/39bb4755ee62633a5ea72b26e8e91ac0cb0ab599/resources/img/numbers/0.png?raw=true) ![alt-text](https://github.com/skatesham/image-recognization-by-correlation-python/blob/39bb4755ee62633a5ea72b26e8e91ac0cb0ab599/resources/img/numbers/1.png?raw=true) ![alt-text](https://github.com/skatesham/image-recognization-by-correlation-python/blob/39bb4755ee62633a5ea72b26e8e91ac0cb0ab599/resources/img/numbers/2.png?raw=true) ![alt-text](https://github.com/skatesham/image-recognization-by-correlation-python/blob/39bb4755ee62633a5ea72b26e8e91ac0cb0ab599/resources/img/numbers/3.png?raw=true) ![alt-text](https://github.com/skatesham/image-recognization-by-correlation-python/blob/39bb4755ee62633a5ea72b26e8e91ac0cb0ab599/resources/img/numbers/4.png?raw=true) ![alt-text](https://github.com/skatesham/image-recognization-by-correlation-python/blob/39bb4755ee62633a5ea72b26e8e91ac0cb0ab599/resources/img/numbers/5.png?raw=true) ![alt-text](https://github.com/skatesham/image-recognization-by-correlation-python/blob/39bb4755ee62633a5ea72b26e8e91ac0cb0ab599/resources/img/numbers/6.png?raw=true) ![alt-text](https://github.com/skatesham/image-recognization-by-correlation-python/blob/39bb4755ee62633a5ea72b26e8e91ac0cb0ab599/resources/img/numbers/7.png?raw=true) ![alt-text](https://github.com/skatesham/image-recognization-by-correlation-python/blob/39bb4755ee62633a5ea72b26e8e91ac0cb0ab599/resources/img/numbers/8.png?raw=true) ![alt-text](https://github.com/skatesham/image-recognization-by-correlation-python/blob/39bb4755ee62633a5ea72b26e8e91ac0cb0ab599/resources/img/numbers/9.png?raw=true) 

> The result should be the string with the number on the image (987654321).

#### [-> Algorithm execution and explanation with Jupyter Notebook <-][1]

#### Confusion Matriz of class patterns
![alt-text][2]

## How to

__Open jupyter notebook__
```commandline
(env)$: pip install -r requirements-with-jupyter.txt
(env)$: jupyter notebook
```

### Credits
Sham Vinicius Fiorin


[1]: https://github.com/skatesham/image-recognization-by-correlation-python/blob/main/correlation_algorithym_explation.ipynb
[2]: https://github.com/skatesham/image-recognization-by-correlation-python/blob/main/resources/matriz_correlation-1.png?raw=true
[3]: https://github.com/skatesham/image-recognization-by-correlation-python/blob/39bb4755ee62633a5ea72b26e8e91ac0cb0ab599/resources/img/numbers/all_numbers.png?raw=true
