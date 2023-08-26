# Tutorial de Python para la FIIPI

[Python](https://www.python.org/) es un lenguaje de programación de propósito general. Puede usarse para clientes o servidores, y en general contiene librerías y extensiones para todo tipo de tareas. Sus usos más destacados podrían ser en la inteligencia artificial y la ciencia de datos.

Python es un lenguaje interpretado (no se compila), lo que lo hace muy útil para trabajar de manera interactiva y generar rápidamente prototipos y scripts. Facilita la interacción con programas escritos en otros lenguajes de programación y se ejecuta en las principales plataformas.

El lenguaje es dinámicamente tipado y soporta múltiples paradigmas de programación: procedural, orientado a objetos, funcional, entre otros.

> Este tutorial supone que el lector ya sabe programar en otro lenguaje. No es un tutorial exhaustivo, solo introduce algunos de los conceptos de base que se consideraron necesarios para poder empezar a usar Python. La [documentación](https://docs.python.org/3/) es extensa y deberá ser revisada cuidadosamente si se desea obtener un conocimiento completo del lenguaje.

## Instalación y ejecución

Puede instalarse rápidamente utilizando los instaladores oficiales en https://www.python.org/downloads/.

> En Ubuntu, por ejemplo, se puede instalar simplemente abriendo un terminal, y ejecutando: ```sudo apt install python3```.

Una vez instalado puede iniciar un terminal interactivo con el comando `python3`.

> Dependiendo de su sistema, la ejecución podrá ser con el comando *py*, *python*, *python2* o *python3* (puede haber otras alternativas).

En la consola podrá ingresar cualquier instrucción python válida, y esta se ejecutará y emitirá su resultado inmediatamente.

La forma como se ejecuta un programa Python generalmente es ingresando las instrucciones en un archivo y guardándolo con extensión *.py*. Luego se puede ejecutar dicho programa desde el terminal: `python3 miprog.py`.

El típico programa "Hola mundo" en Python sería algo así:

```python
print('Hola mundo !!!')
```

Un archivo python que se puede ejecutar directamente, como se ha indicado, suele llamarse un *script*.

---
**Ejercicios**

Instale python en su sistema y verifique mediante el programa "Hola mundo" presentado.
- Ejecute `print('Hola mundo !!!')` directamente desde la consola
- Cree el archivo *miprog.py*, escriba dentro de él la instrucción y ejecútelo desde la consola como script
---

## Conda: entornos virtuales

Python cuenta con una enorme cantidad de paquetes o librerías de funciones, cada una de ellas en múltiples versiones. Las librerías se suelen desarrollar usando a su vez otras librerías, y en muchas ocasiones estas "dependencias" entre librerías son tales que requieren versiones muy específicas para funcionar. Cualquier cambio de versión, por ejemplo al actualizar una librería existente o instalar una nueva, puede ocasionar que su programa deje de funcionar.

Para evitar este problema, se suele utilizar entornos virtuales, que aislan los paquetes y sus versiones de aquellos en otros entornos. De esta manera, si se necesita trabajar con un set específico de librerías, solo hace falta crear un nuevo entorno virtual donde se instalará exactamente lo que se necesita, sin afectar al resto de entornos.

Varias utilidades existen para administrar entornos virtuales: [Conda](https://docs.conda.io/), [venv](https://docs.python.org/3/library/venv.html) o [virtualenv](https://virtualenv.pypa.io/). Todos cumplen la función indicada, pero aquí se hablará un poco más de Conda, que se puede considerar casi como un estándar.

### Instalación

La mejor manera de contar con Conda es instalando [Miniconda](https://docs.conda.io/en/latest/miniconda.html), que proporciona la funcionalidad de base

> sin congestionar su sistema con cientos de megas en software que probablemente no utilizará, que sería el caso si usa [Anaconda](https://www.anaconda.com/), también muy popular

En general Conda se manipula desde una consola, sobre todo para la creación de entornos e instalación de paquetes.

> NOTA: en Windows, la manera recomendada de administrar Conda es mediante la utilidad "Anaconda Prompt" (que se instala con Miniconda). En Linux se puede usar cualquier consola.

### Comandos más usados

- `conda create -n <nombre-entorno> <lista-paquetes>` crea un nuevo entorno con nombre `<nombre-entorno>`, instalando en el mismo los paquetes en `<lista-paquetes>`. `<lista-paquetes>` puede ir vacío, pero en general se suele iniciar al menos con `python`:
    - `conda create -n mientorno python`, ó
    - `conda create -n mientorno python=3.10`, si quiere una versión específica de cualquier paquete
- `conda remove -n <nombre-entorno> --all`, elimina el entorno indicado, con todos sus paquetes
- `conda env list`, presenta un listado de todos los entornos existentes
- `conda activate <nombre-entorno>`, activa el entorno indicado para trabajar con él
- `conda deactivate`, desactiva el entorno actual
- `conda install <lista-paquetes>`, instala los paquetes indicados en el entorno, a pesar de que suele utilizarse más `pip install ...`
- `conda update conda`, actualiza el sistema Conda
- `conda update --all`, actualiza todos los paquetes en el entorno

---
**Ejercicios**

Instale miniconda y verifique creando dos entornos
- uno con la última versión de python
- otro con la versión 3.8
- cambie entre los tres entornos existentes y
    - liste los paquetes instalados,
    - ejecute el intérprete python
    - verifique la versión de python y cierre el intérprete
---

## Entorno de desarrollo o IDE

Trabajar en un proyecto manipulando los archivos uno por uno mediante un terminal puede ser muy tedioso y proclive a errores.

En general se utiliza algún tipo de entorno de desarrollo o IDE (Integrated Development Environment), de los que hay varios y para todos los gustos, como por ejemplo: [VSCode](https://code.visualstudio.com/), [Jupyter Notebook](https://jupyter.org/) o [Google Colab](https://colab.research.google.com/). Cualquiera de ellos (y hay muchos más) funciona bien, sin embargo, en los casos en que se presente o proponga ejercicios en este tutorial, se preferirá el uso de Google Colab, que es un entorno gratuito en línea (solo necesita una cuenta Google) que se ejecuta en una máquina virtual en la nube con muy buenas prestaciones, que inclusive permite usar una GPU para IA. Alternativamente se usará VSCode. 

### Google Colab

Para poder usar Colab se necesita una cuenta Google, un browser y dirigirse a la URL de [Google Colab](https://colab.research.google.com/).

> Su cuenta *icam.fr* funciona perfectamente

Colab utiliza para los scripts el formato de [Jupyter Notebook](https://jupyter.org/), que son archivos con extensión *.ipynb* conocidos como notebooks. Un notebook se crea con `File\New notebook` y trabaja con el concepto de celdas. Un notebook puede tener varias celdas, de las que hay dos tipos:
- Celdas de texto, que se crean con `Insert\Text cell`, y que permiten *documentar* su trabajo, explicando lo   que se está haciendo y aclarando su código en general. Estas celdas usan el formato [Markdown](https://www.markdownguide.org/), que no es más que texto, al que se puede dar un formato simple. Estas celdas son solo informativas y no afectan la ejecución del script.
- Celdas de código, que se crean con `Insert\Code cell`, y que constituirán su programa. Aquí va el código ejecutable en lenguaje Python. El código de su programa puede estar distribuido en varias celdas de código, no necesariamente contiguas. A las celdas de código es necesario ejecutarlas explícitamente, con los comandos del menu `Runtime`.
> Es constumbre intercalar celdas de texto con celdas de código, para explicar claramente cada parte de su programa

Google Colab se ejecuta en máquinas virtuales en la nube, de manera que es independiente del poder de cómputo de su computador. Sin embargo, no se garantiza la entrega de recursos a los usuarios, de manera que las capacidades del entorno pueden variar de una ejecución a otra.

Una gran ventaja de Colab es que proporciona varios entornos de ejecución, solo en CPU o con una GPU incluida. Por defecto se utiliza solo CPU, pero si desea también GPU, por ejemplo para trabajos de Inteligencia Artificial, puede modificarlo en `Runtime\Change runtime type`.

> Contar con una GPU es una de las grandes fortalezas de Colab. Puede incluso trabajar con modelos no muy grandes de [LLM](https://en.wikipedia.org/wiki/Large_language_model)

Un detalle a tomar en cuenta es que las sesiones de trabajo de Colab tienen un tiempo de caducidad, de manera que si deja inactiva su sesión mucho tiempo, o si excede un uso de 12 horas (más o menos), su entorno se desconectará y reseteará a cero.

Esta caducidad de las sesiones implica que en cada nuevo uso deberá instalar todas las librerías requeridas nuevamente.

Al instalar librerías, estás se cargan en la máquina virtual, lo que implica que se usa el ancho de banda de la nube y no el su máquina local, lo cual puede ser una ventaja si en su lugar de trabajo tiene un ancho de banda limitado.

Para instalar las librerías deberá utilizar:
```
!pip install <librerias>
```
Preste atención al `!` al inicio del comando. Esto indica que la instrucción se ejecutará en la consola general de la máquina virtual y no en el ambiente Python

Dado que todos los archivos con los que vaya a trabajar deberán estar en la máquina virtual, en lugar de cargarlos uno a uno, puede ser preferible conectar su Google Drive con Colab, para lo que puede utilizar este comando:

```python
from google.colab import drive
drive.mount('/content/drive')
```

Sus notebooks serán guardados también en Drive automáticamente (o con `File\Save`), en el directorio `Colab Notebooks`.

---
**Ejercicios**

Solo para verificar:
- Ingrese a Colab y confirme que está logeado con su cuenta
- Cree un nuevo notebook con el nombre "holaMundo.ipynb"
- Cree una celda de texto con el título "Hola mundo"
- Cree una celda de código con la instrucción para imprimir "hola mundo" y ejecútela
- Monte su Drive
- Verifique que está guardado su notebook
---

### VSCode

[Visual Studio Code](https://code.visualstudio.com/) es un entorno local que deberá descargar e instalar. Es un entorno genérico, de manera que deberá instalar también los plugins que necesite para su trabajo, yendo a `View\Extensions`. En este caso busque la extensión *Python*.

Para trabajar abra el directorio con su código mediante `File\Open Folder` y active el entorno Conda respectivo.

Para activar el entorno Conda oprima primero `Ctrl+Shift+P` y luego seleccione `Python: Select Interpreter`. Luego escoga el entorno apropiado.

---
**Ejercicios**

Para comprobar que VSCode esté bien instalado en su sistema:
- Abra el archivo *miprog.py* que creó anteriormente
- Ejecútelo en cada uno de los 2 entornos Conda que creó previamente
---

## Paquetes y módulos

Python posee una enorme cantidad de paquetes (o librerías de código), los cuales deben ser instalados en su sistema según la necesidad del trabajo a realizarse. Los paquetes se encuentran mayoritariamente en el [Python Package Index](https://pypi.org/), y para instalarlos se utiliza el comando `pip` ([package installer for Python](https://pip.pypa.io/)). Por ejemplo, si se desea instalar el paquete [SciPy](https://scipy.org/) (para trabajos científicos y de ingeniería), se puede usar en un terminal `pip install scipy`. Luego se deberá importar la funcionalidad de interés del paquete, dentro del script donde vaya a utilizarse: `import scipy`.

Python viene con un set importante de paquetes ya incluidos. Revise la documentación de la [Standard Library](https://docs.python.org/3/tutorial/stdlib.html).

Los paquetes pueden estar constituidos de otros paquetes, o subpaquetes, y especialmente de módulos.

Los paquetes y subpaquetes forman una estructura de árbol, con un directorio raíz, el paquete principal, y posiblemente varios subdirectorios, por cada uno de los subpaquetes.

Dentro de cada paquete o subpaquete, se encuentran los módulos, que son archivos *.py* donde se halla el código de interés en la forma de funciones u objetos.

En general, cuando se importa un paquete, realmente se importa uno o varios módulos de dicho paquete. Por ejemplo, si deseamos usar la función *rotate*, para girar una imagen deberíamos importar el módulo *interpolation*, dentro del subpaquete *ndimage*, a su vez dentro del paquete *scipy*:

```python
from scipy.ndimage import interpolation as intp
```

y así podremos ejecutar la función requerida (cualquier función dentro del módulo realmente), por ejemplo con:

```python
intp.rotate(img, 45)
```

> El *as* en el import, permite usar un alias para el módulo, en este caso *intp*; caso contrario, al ejecutar la función deberíamos llamarla con el nombre completo del módulo (un poco largo en este caso). A pesar de ser útil, no es obligatorio!

> **¡Atención!** Existen algunas variaciones en la forma de importar funcionalidad. En general refiérase a la documentación del paquete para estar seguro.  

### Módulos personales

Con el tiempo se suele acumular código personal, en una serie de funciones u objetos que se van generando. Estas funciones normalmente deben estar dentro de módulos (archivos *.py*).

Para poder reutilizar esta funcionalidad dentro de los nuevos scripts que vamos generando, también hay que importar estos módulos.

Dado que no forman parte de ningún paquete oficial, y por ende no han sido instalados en el sistema, nuestro entorno no sabe donde encontrarlos!

Dos formas pueden ser las más prácticas para poderlos importar:

- ponga una copia de los módulos que va a importar en el mismo directorio que contiene el script que va a ejecutar,
- indique en su script el directorio donde se encuentran estos módulos:
    ```python
    import sys
    sys.path.append('/path/al/directorio')
    ```
Cualquiera sea el mecanismo utilizado, deberá importar los módulos en su script antes de poderlos utilizar. Hágalo utilizando el nombre del archivo (sin la extensión .py):

```python
import nombredearchivo as mimod
```

### `__name__`

Dado que cualquier archivo *.py* puede ser considerado un módulo e importado, hay un pequeño problema que se puede suscitar: cualquier instrucción que no esté dentro de una función, se ejecutará automáticamente al importar el módulo. Esto puede provocar sorpresas desagradables.

Supongamos que tiene el archivo `hola.py`, el cual desea importar. Supongamos también que dicho archivo tiene el siguiente código:

```python
def miFuncion1():
    print('Estoy en miFuncion1')

def miFuncion2():
    print('Estoy en miFuncion2')

print('Estoy en el módulo hola.py')
```

Para importar este módulo, usará en su script (por ejemplo), `import hola`. Al ejecutarse el `import`, aparecerá en la consola: `Estoy en el módulo hola.py`, dado que la instrucción `print` que no está dentro de ninguna función, será ejecutada automáticamente.

Evitar este problema es sencillo, pero requiere ser metódico cuando se crean los scripts, e incluir todo el código que no está en una función, y que no se quiere ejecutar al importar, dentro de un bloque `if` como en el siguiente ejemplo:

```python
def miFuncion1():
    print('Estoy en miFuncion1')

def miFuncion2():
    print('Estoy en miFuncion2')

if __name__ = "__main__":
    print('Estoy en el módulo hola.py')
```

Lo que se encuentra dentro de esta estructura `if __name__ = "__main__":`, sólo se ejecutará si el archivo se invoca directamente, como por ejemplo desde la consola con `python3 hola.py`, y nunca al importarlo como módulo.
