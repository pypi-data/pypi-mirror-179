# Modularizador
For explanations in english, scroll down *(Explica&#x00E7;&otilde;es em ingl&ecirc;s no final)*.

Instale com
> !pip install modularizador

Ap&oacute;s importado no Jupyter Notebook, permite importar arquivos .ipynb como se fossem arquivos .py, inclusive os que est&atilde;o em subpastas.

Exemplo de uso:
1. Na pasta do seu projeto, use seu Jupyter Notebook para criar o arquivo main.ipynb, depois crie um arquivo chamado **somador.ipynb** e coloque ele dentro de uma subpasta chamada **pacotes**.
```
'----Pasta do seu projeto
    |   main.ipynb
    |
    '---pacotes
            somador.ipynb
```
2. Crie uma fun&#x00E7;&atilde;o chamada soma dentro do arquivo somador.ipynb:

```python
def soma(a, b):
    return a + b
```
3. Agora, a partir de main.ipynb, &eacute; s&oacute; importar o modularizador e voc&ecirc; poder&aacute; importar tamb&eacute;m o somador.ipynb:

```python
import modularizador
from pacotes import somador
somador.soma(2, 3)
>>> 5
```

O c&oacute;digo utilizado nesta biblioteca para obter o resultado acima foi extra&iacute;do [desta p&aacute;gina](https://jupyter-notebook.readthedocs.io/en/stable/examples/Notebook/Importing%20Notebooks.html) da documenta&#x00E7;&atilde;o do Jupyter Notebook. 
Daqui para baixo vamos nos referir a ele como *o script*, ou como *modularizador.py*.
---
A biblioteca modularizador conta ainda com 3 fun&#x00E7;&otilde;es &uacute;teis: **ativa()**, **desativa()** e **status_startup()**.
* ##### ativa()

```python
import modularizador
modularizador.ativa()
```
Insere *o script* na pasta startup do ipython, tornando desnecess&aacute;rio importar a biblioteca modularizador a partir das pr&oacute;ximas vezes que voc&ecirc; abrir um projeto. O efeito durar&aacute; enquanto *modularizador.py* estiver na pasta startup, portanto fechar seu Jupyter Notebook n&atilde;o o desfar&aacute;. 

No exemplo anterior, se voc&ecirc; j&aacute; tivesse, em algum momento do passado, realizado o procedimento de ativa&#x00E7;&atilde;o logo acima, poderia, em seu novo projeto, importar pacotes/somador.ipynb sem a necessidade de importar o modularizador. Simplesmente assim:
```python
from pacotes import somador
somador.soma(2, 3)
>>> 5
```
* ##### desativa()
```python
import modularizador
modularizador.desativa()
```
Remove *o script modularizador.py* da pasta startup do ipyton, tirando do seu Jupyter Notebook a capacidade de importar arquivos .ipynb sem importar manualmente o modularizador em cada projeto.

* ##### status_startup()
```python
import modularizador
modularizador.status_startup()
```
Apenas informa se *o script modularizador.py* est&aacute; na pasta startup do ipyton. I.e., se est&aacute; ou n&atilde;o ativo o recurso que permite a importa&#x00E7;&atilde;o de arquivos .ipynb sem a necessidade de importar a biblioteca modularizador explicitamente em cada projeto.

&Eacute; s&oacute; isso. Abaixo est&atilde;o as mesmas explica&#x00E7;&otilde;es acima em ingl&ecirc;s.

---
---
---
---
---
## == Explanations in english ==

Install with
> !pip install modularizador

After importing modularizador on Jupyter Notebook, you'll be able to import .ipynb files as if they were .py files, even those inside subfolders.

Usage example:
1. Inside your project directory, use your Jupyter Notebook to create main.ipynb, then create **summer.ipynb** and put it inside a subfolder named **packages**.
```
'----Diretório do seu projeto
    |   main.ipynb
    |
    '---pacotes
            somador.ipynb
```
2. Define a function named add inside summer.ipynb:

```python
def add(a, b):
    return a + b
```
3. Now, inside main.ipynb, import modularizador and you'll become able to import summer.ipynb too afterwards:

```python
import modularizador
from packages import summer
summer.add(2, 3)
>>> 5
```

The code that makes this possible was extracted from [this page](https://jupyter-notebook.readthedocs.io/en/stable/examples/Notebook/Importing%20Notebooks.html) of Jupyter Notebook's documentation. 
From now on, we will refer to it either as *the script* or as *modularizador.py*.
---
The modularizador library has 3 useful methods: **ativa()**, **desativa()** and **status_startup()**.
* ##### ativa()

```python
import modularizador
modularizador.ativa()
```
Ativa means activate. This method inserts *the script* in ipython's startup, making it unnecessary to explicitly import modularizador everytime you open a new Jupyter Notebook project from now on. This effect will last as long as *modularizador.py* remains in the startup folder, so closing your Jupyter Notebook won't undo it. 

In our last example, had you activated modularizador somewhen in the past, you would be able to import packages/summer.ipynb without having to import modularizador first. Just like:
```python
from packages import summer
summer.add(2, 3)
>>> 5
```
* ##### desativa()
```python
import modularizador
modularizador.desativa()
```
Desativa means deactivate. This method removes *the script (modularizador.py)* from ipython's startup folder, making your Jupyter Notebook unable to import .ipynb without manually importing modularizador priorly in each project again.

* ##### status_startup()
```python
import modularizador
modularizador.status_startup()
```
Just tells you whether or not *the script (modularizador.py)* is in ipython's startup folder. I.e., whether modularizador is active and hence allowing you to import .ipynb without the need to explicitly import modularizador beforehand in your projects or not.
