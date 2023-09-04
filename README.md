# Tutorial de Python para la FIIPI

[Python](https://www.python.org/) es un lenguaje de programación de propósito general. Puede usarse para clientes o servidores, y en general contiene librerías y extensiones para todo tipo de tareas. Sus usos más destacados podrían ser en la inteligencia artificial y la ciencia de datos.

Python es un lenguaje interpretado (no se compila), lo que lo hace muy útil para trabajar de manera interactiva y generar rápidamente prototipos y scripts. Facilita la interacción con programas escritos en otros lenguajes de programación y se ejecuta en las principales plataformas.

El lenguaje es dinámicamente tipado y soporta múltiples paradigmas de programación: procedural, orientado a objetos, funcional, entre otros.

> Este tutorial supone que el lector ya sabe programar en otro lenguaje. No es un tutorial exhaustivo, solo introduce algunos de los conceptos de base que se consideraron necesarios para poder empezar a usar Python. La [documentación](https://docs.python.org/3/) es extensa y deberá ser revisada cuidadosamente si se desea obtener un conocimiento completo del lenguaje.

---
# Contenido

### [Sesión 1](#instalación-y-ejecución)

- Entorno, instalación, configuración y ejecución
    - Python, Conda, VSCode, Google Colab
    - paquetes/librerías
    - imports

### [Sesión 2](#sintaxis)

- Sintaxis
    - Instrucciones, indentación, comentarios
- Datos
    - Identificadores
    - Variables: declaración, asignación
    - Tipos de datos, números, strings y strings formateadas
- Colecciones
    - Listas, tuplas, sets, diccionarios
    - índices, rebanadas

### [Sesión 3](#estructuras-de-control)

- Estructuras de control
    - If..., match, while, for
    - ranges

### [Sesión 4](#archivos)

- Archivos
    - lectura,escritura, ...

### [Sesión 5](#funciones)

- Funciones
    - definición y declaración
    - parámetros: variables, optativos, nombrados
    - alcance
    - lambdas
- Excepciones

### [Sesiones 6 y 7](#clases)

- Clases y objetos
    - constructores
    - campos, métodos, alcance
    - Fundamentos de herencia

### Sesión 8

- Fundamentos de Sockets TCP
    - clientes, servidores

### Sesión 9

- Fundamentos de HTTP
    - http.server (cgi)
    - Fundamentos de Flask
- Fundamentos de HTML
- Fundamentos de CSS

### Sesión 10

- Fundamentos de BDD (NoSQL)
    - Json
    - TinyDB
    - Fundamentos de  Redis

### Evaluación
- se definirá una sesión posterior para una evaluación práctica

---

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

if __name__ == "__main__":
    print('Estoy en el módulo hola.py')
```

Lo que se encuentra dentro de esta estructura 
```if __name__ == "__main__":```
sólo se ejecutará si el archivo se invoca directamente, como por ejemplo desde la consola con `python3 hola.py`, y nunca al importarlo como módulo.

******

## Sintaxis

### Instrucciones, líneas y comentarios

Un programa Python está dividido en líneas, y salvo ciertos casos, una instrucción (statement) debe encontrarse en una sola línea. Ciertas instrucciones compuestas como *if* y *for* ocuparán de manera natural varias líneas.

Si alguna instrucción de una línea necesita dividirse en varias líneas, puede usarse el backslash `\`:

```python
... dia > 1 \ 
and hora < 12 \ 
and ...
```

Para ingresar comentarios se usa el símbolo de numeral `#`. Un comentario puede encontrarse al final de una línea, salvo cuando esta termina en `\`.

### Indentación

La indentación es fundamental en Python, no solo para facilitar la visualización sino para determinar la agrupación de instrucciones o bloques. Para indentar se usa espacios o tabulaciones, pero se debe tener mucho cuidado al mezclarlas en un mismo archivo ya que puede generar errores si se lo hace de manera inconsistente. En general se recomienda usar espacios.

La primera línea de un archivo de código no puede estar indentada, y el número de espacios en un bloque de código debe ser consistente.

Un pequeño ejemplo:

```python
i = 1
while(i <= 2): # bloque i
    print("El valor de i es " + str(i))
    i = i + 1
    j = 1
    while(j <= 2): # bloque j
        print("El valor de j es " + str(j))
        j = j + 1
    k = 1
    while(k <= 2): # bloque k
        print("El valor de k es " + str(k))
        k = k + 1
l = 1
while(l <= 2): # bloque l
    print("El valor de l es " + str(l))
    l = l + 1    
```

Si ejecuta este ejemplo obtendrá:

```
El valor de i es 1
El valor de j es 1
El valor de j es 2
El valor de k es 1
El valor de k es 2
El valor de i es 2
El valor de j es 1
El valor de j es 2
El valor de k es 1
El valor de k es 2
El valor de l es 1
El valor de l es 2
```

> Los bloques j y k se encuentran dentro del bloque i, pero son independientes entre ellos: se encuentran al mismo nivel. Los bloques i y l también son independientes entre ellos al encontrarse al mismo nivel

Los bloques `while` del ejemplo anterior están todos correctamente indentados. A continuación un ejemplo mal indentado que emitiría un error:

```python
i = 1
while(i <= 2):
print("El valor de i es " + str(i))
i = i + 1
```

El error sería:

```
line 3
    print("El valor de i es " + str(i))
    ^
IndentationError: expected an indented block after 'while' statement on line 2
```

 Otro ejemplo de mala indentación:

```python
i = 1
while(i <= 2):
  print("El valor de i es " + str(i))
    i = i + 1
```

El error sería:

```
line 4
    i = i + 1
IndentationError: unexpected indent
```

### Identificadores y variables

Los identificadores de métodos, variables, clases, etc., pueden utilizar los caracteres: A-Z a-z _ y 0-9 (pero 0-9 no puede ser el primer caracter!)

> El sistema define indicadores que inician y terminan con doble guión bajo `__*__`, razón por la que se desaconseja usar este patrón (podría colgar la ejecución).

Las variables se crean la primera vez que se usan en el código y no hace falta ninguna declaración explícita. Al ser un lenguaje dinámicamente tipado, una variable pueden recibir cualquier tipo de valor en cualquier momento. Se puede usar asignamiento múltiple de variables en una instrucción:

```python
# asignamiento simple
a = 1
# asignamiento múltiple
a, b, c = 1, 2, 3 #a = 1, b = 2, c = 3
```

## Tipos de datos

Los tipos de datos integrados (built-in) son:

```
Texto: str
Numéricos: int, float, complex
Colecciones: list, tuple, range
Mapping Type: dict
Set Types: set, frozenset
Boolean Type: bool
Binary Types: bytes, bytearray, memoryview
```

Se puede obtener el tipo del dato en una variable con `type(<variable>)`

### Strings

Las cadenas de texto o strings, pueden representarse sea dentro de comillas simples(`'...'`) o dobles (`"..."`); se recomienda preferir las comillas simples.

Esta flexibilidad es bienvenida cuando es necesario incluir en el texto comillas simples o dobles, dado que podremos evitar usar caracteres de escape, que pueden volver al texto difícil de leer.

- Si se necesita comillas dobles incluidas en el texto, entonces la string estará dentro de comillas simples: `'Necesito "dobles" en el texto'` --> Necesito "dobles" en el texto

- Si se necesita comillas simples incluidas en el texto, entonces la string estará dentro de comillas dobles: `"Necesito 'simples' en el texto"` --> Necesito 'simples' en el texto

Las strings también pueden presentarse en múltiples líneas, para lo que se usa comillas triples (sean simples o dobles):

```python
a = '''Estoy
en múltiples
líneas'''

# ó...

b = """Estoy
en múltiples
líneas"""

```
Para concatenar strings o valores en general, cuando estos están en variables, hay varias alternativas:

- la clásica, utilizando el '+': `'uno ' + 'dos ' + 'tres'` --> uno dos tres

- simplemente poniendo las strings juntas: `'uno ' 'dos ' 'tres'` --> uno dos tres
> Esta opción no funciona con variables !

- utilizar strings "formateadas", las cuales permiten sobretodo inyectar fácilmente dentro de una string el valor de variables. La string se debe definir con el prefijo f: `f'Esta en una string formateada'`. Dentro de la string se puede incrustar variables dentro de símbolos de llaves: `f'Nombre: {fName}, Apellido: {lName}`. Ej:

```python
fName = 'Diego'
lName = 'Ordóñez'
print(f'Nombre: {fName}, Apellido: {lName}')
# Produce: Nombre: Diego, Apellido: Ordóñez
```

### Listas

Es una de las colecciones más usadas y flexibles. Admiten cualquier tipo de elemento, puede haber elementos duplicados, y los elementos mantienen el orden en que fueron ingresados. Una lista puede modificarse en cualquier momento. Se puede acceder a los elementos por índice y se puede extraer una rebanada (slice) de una lista. Para crear una lista se usa corchetes:

```python
a = [1, 2, 'a', 'x']
```
> En Python no hay arreglos, se usan las listas.

Algunas operaciones relevantes en una lista pueden ser:

- para saber cuántos elementos hay en una lista se puede usar `len(<lista>)`
- para añadir un elemento al final de la lista se usa `<lista>.append(<elemento>)`
- para insertar un elemento en un cierto índice se usa `<lista>.insert(<índice>, <elemento>)`
- para añadir una colección al final de una lista se usa `<lista>.extend(<colección>)`
- para recuperar y quitar el elemento al final de la lista se usa `<lista>.pop()`. Si añade un índice a pop puede hacerlo con cualquier elemento. Para retirar el primero de la lista usaría `pop(0)`

> Si analiza estas operaciones, verá que facilmente se puede usar una lista como un stack o una cola.

> OJO: si su colección tiene un solo elemento, es necesario definirla con una coma final, para que no haya confusiones con otro tipo de expresiones. Ej: `a = [1,]`. Esto aplica para todo tipo de colecciones: lista, tupla, ...

#### Indices y rebanadas (slice)

Se puede acceder a los caracteres de una colección en general, strings incluidas, por índice. Si se usa valores negativos como índice se puede acceder desde el último elemento o caracter:

```python
a = 'Diego' # o, por ejemplo: a = ['D', 'i', 'e', 'g', 'o']
a[0] # D
a[1] # i
a[-1] # o
a[-2] # g
```

Este ejemplo indica los índices de todos los elementos de una lista, tanto en positivo como negativo:
```
 +---+---+---+---+---+
 | D | i | e | g | o |
 +---+---+---+---+---+
   0   1   2   3   4   
  -5  -4  -3  -2  -1
```

Se puede también "rebanar" una parte de una colección o string:

```python
a = 'Diego'
a[:] # Diego
a[1:3] # ie
a[:3] # Die
a[2:] # ego
a[-2:] # go
a[:-2] # Die
```

Especificando:
- el primer elemento, antes de `:` es el índice del inicio (*start*) de la rebanada
    > *start* incluye o inicia desde el índice indicado. Si no se pone nada se asume el primer elemento
- el segundo elemento, luego de `:` es el índice del final (*stop*) de la rebanada.
    > *stop* NO incluye o no llega hasta el índice indicado. Si no se pone nada se asume el último elemento incluido

Las rebanadas pueden tener también un tercer parámetro (*step*) que permite definir si nos "saltaremos" algunos elementos de la rebanada, o el orden en que se toman. El valor por defecto es 1, que indica que tomamos todos los elementos en el orden típico izquierda-derecha
```python
a = 'Diego'
a[::] # Diego
a[0:5:1] # Diego
a[0:5:2] # Deo
a[1:5:3] # io
```

Si *step* es negativo cambiamos el orden en que se recogen los elementos de la rebanada, de derecha a izquierda.
> Se verá, sin embargo, que algunos casos pueden resultar poco claros
```python
a = 'Diego'
a[::-1] # ogeiD (típico para invertir una lista)
a[::-2] # oeD
a[0::-1] # D
a[0:5:-1] # ''
a[5:0:-1] # 'ogei'
a[5::-1] # 'ogeiD'
a[-1:-6:-1] # ogeiD
```

> Esto aplica para todo tipo de colecciones indexadas como string (colección de caracteres), lista y tupla.

---
**Ejercicios**

- Ejecute todos los ejemplos de rebanadas para confirmar que son correctos
- A partir de la siguiente colección:
    - `a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]`
- ...cómo puede obtener esta nueva colección:
    - `[1, 3, 5, 7, 9, 20, 18, 16, 14, 12]`
---

### Tuplas

Son colecciones inmutables: es como una lista, pero una vez creada no se puede cambiar nada. Para crear una tupla (tuple) se usa paréntesis:

```python
a = (1, 2, 'a', 'x')
```

### Sets

Son colecciones que no admiten duplicados y que no garantizan ningún orden. No se puede acceder a sus elementos por índice y no se pueden modificar, pero se admite añadir y eliminar elementos. Para crear un set se usa llaves:

```python
a = {1, 2, 'a', 'x'}
```

### Diccionarios (Mapas)

Los diccionarios o mapas permiten guardar elementos en pares clave:valor. La clave permiten recuperar un valor y no se puede tener claves duplicadas. Los elementos pueden modificarse, añadirse o eliminarse. Para crear un diccionario se usa llaves:

```python
a = {"nombre": "Diego", "apellido": "Ordóñez", "id": 1234}
a["id"] # 1234
a["id"] = 5678 # ahora id = 5678
a["otro"] = "nuevo" # añade el elemento "otro":"nuevo"
a.pop("apellido") # elimina el elemento "apellido":"Ordóñez"
```

---
**Ejercicios**

- A partir del siguiente diccionario:
    - `d = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6}`
- ... obtenga este diccionario:
    - `{'a': 1, 'b': 9, 'd': 4, 'e': 5, 'f': 6, 'g': 8}`
---

***

## Estructuras de control

### If, Elif, Else

`if` toma la forma:

```python
if <condición>:
    <bloque-if-true>
```

`elif` toma la forma:

```python
if <condición>:
    <bloque-if-true>
elif <condición>:
    <bloque-elif-true>
elif <condición>:
    <bloque-elif-true>
# puede haber varios bloques elif
```

`else` toma la forma:

```python
if <condición>:
    <bloque-if-true>
elif <condición>:
    <bloque-elif-true>
# puede haber 0 o más bloques elif
else:
    <bloque-else>
```

```python
# Cambie el valor de num y pruebe
num = 1
if num == 1 :
    print('uno')
elif num == 2 :
    print('dos')
elif num == 3:
    print('tres')
else :
    print('otro número')

```

### Match

Equivalente a *switch* en otros lenguajes:

```python
match <variable>:
    case <valor1>:
        <bloque-si-valor1>
    case <valor2>:
        <bloque-si-valor2>
    # los case que se necesite
    case _:
        <bloque-si-nada-más-se-ejecutó>
```

> El guión bajo en el case final captura cualquier valor, es el caso por defecto!

```python
# Cambie el valor de num y pruebe
num = 1
match num :
    case 1:
        print('uno')
    case 2:
        print('dos')
    case 3:
        print('tres')
    case _ :
        print('otro número')

```

### While

`while` toma la forma:

```python
while <condición>:
    <bloque-while-true>
```

```python
i = 0
j = 5
while i < j:    
    print(f'paso {i+1} de {j}')
    i = i + 1
```

### For

`for` se usa para iterar sobre una colección y su forma de base es:

```python
for <variable> in <colección>:
    <bloque-por-cada-elemento>
```

```python
for i in [1, 2, 3, 4, 5]:
    print(f'paso {i} de 5')
```

`break` se usa para terminar el lazo en cualquier momento:

```python
for <variable> in <colección>:
    <bloque-por-cada-elemento>
    if <condición> : break
    <bloque-por-cada-elemento>
```
> si `<condición>` es verdadera, se sale del lazo inmediatamente

`continue` se usa para terminar la iteración inmeditamente e iniciar la siguiente iteración:

```python
for <variable> in <colección>:
    <bloque-por-cada-elemento>
    if <condición> : continue
    <bloque-por-cada-elemento>
```

> si `<condición>` es verdadera, se termina la iteración sin ejecutar el segundo bloque y se inicia la siguiente iteración

`range(...)` se usa para generar una colección con una serie numérica que puede usar con `for`:

```python
for <variable> in range(ini, fin, salto):
    <bloque-por-cada-elemento>
```

```python
for i in range(1, 6):
    print(f'paso {i} de 5')
```

Ejemplos de colecciones producidas con range:

```python
range(2, 8, 2) # [2, 4, 6]
range(2, 5) # [2, 3, 4]
range(4) # [0, 1, 2, 3]
```

`else` se puede usar para ejecutar un bloque al finalizar el lazo:

```python
for <variable> in <colección>:
    <bloque-por-cada-elemento>
else:
    <bloque-al-finalizar>
```
> si el lazo finaliza por un `break`, no se ejecuta el `else`

---
**Ejercicios**

Cree un programa que permita adivinar un número entre 1 y 100. El programa genera un número aleatorio y el usuario debe ingresar el número adecuado por el terminal. El programa emitirá mensajes de ayuda como "muy alto", "muy bajo" o "adivinó !!!".

> Puede resultarle muy útil las funciones: 
> - [input()](https://www.w3schools.com/python/ref_func_input.asp)
> - [randint()](https://www.w3schools.com/python/ref_random_randint.asp)

---

## Archivos

Los archivos son la principal manera de guardar información a largo plazo, de manera que es esencial saber procesarlos.

Para trabajar con un archivo primero hay que abrirlo, y para ello existen cuatro modos básicos:

- `r`, read o lectura, que no modifica el archivo
- `w`, write o escritura, que reemplaza el contenido del archivo
- `a`, append o añadir, que añade contenido al final del archivo (es solo un modo más de escritura)
- `x`, exclusive o creación exclusiva

### Crear archivos

Un archivo se crea y guarda, inicialmente, en el disco duro de su equipo. Para crearlos ábralos en modo exclusivo, de esta manera si ya existe un archivo con dicho nombre, habrá un error, en lugar de reemplazar el archivo. Cuando ya no use el archivo ciérrelo.

```python
file = open('nuevo.txt', 'x')
file.close()
```

> Si abre el archivo en modo escritura también se creará si no existe

### Leer archivos

Los archivos no son más que una colección de bytes o caracteres. Los archivos de texto se abren en modo lectura así:

```python
reader = open('dog_breeds.txt', 'r')
```

y luego se leen, por ejemplo:

```python
# todo el archivo de una sola
a = reader.read()
reader.close()
print(a)
```

```python
# línea por línea
line = None
while line != '':
    line = reader.readline()
    print(line)
reader.close()
```

```python
# todas las líneas, dentro de una lista
lines = reader.readlines()
reader.close()
print(lines)
```

### Escribir en un archivo

Abra el archivo en modo escritura:

```python
writer = open('nuevo.txt', 'w')
```

y escriba en él usando el método `write` cuantas veces sea necesario:

```python
writer.write('Hola ')
writer.write('mundo !')
writer.close()
```

---
**Ejercicios**

- Abra el archivo *antes.txt*, cuyo contenido es:
    ```
    12345
    67890
    12345
    67890
    ```

    modifíquelo para que su contenido sea:

    ```
    09876
    54321
    09876
    54321
    ```

    Y guárdelo en el archivo *despues.txt*

- Modifique su programa de adivinar números para incluir un "log":
    - por cada ejecución añada al archivo una línea con la fecha y hora de inicio, y el número que se debe adivinar
    - por cada intento añada una línea con el índice del intento (si es el primero, segundo, tercero, ... intento), y con el número ingresado por el usuario

---

*****

## Funciones

Las funciones son síncronas por defecto, se definen con `def` y se ejecutan por nombre, seguido de paréntesis con argumentos internos. Los argumentos se tratan como posicionales por defecto. Si la función debe devolver un valor se usa `return`:

```python
#definición
def <nombre-función>(<parámetros>):
    <bloque-de la función>
    return <valor> #el return es optativo

#ejecución
<nombre-función>(<parámetros>) 
```

```python
#definición
def aToThePowerOfB(a, b):
    result = 1
    for i in range(1,b+1):
        result *= a
    return result

#ejecución
value = aToThePowerOfB(2, 4)
print(value)
```

Si no se sabe el número exacto de argumentos que una función deberá recibir, se puede declarar un solo parámetro precedido de un asterisco(*), el cual será tratado como una lista de argumentos en el cuerpo de la función:

```python
#definición
def mi_funcion(*args):
    for arg in args:
        print(arg)

#ejecuciones válidas
mi_funcion(1)
mi_funcion(1, 2)
mi_funcion(1, 2, 3) #... así sucesivamente
```

Los argumentos pueden tratarse como nombrados y se los puede enviar de la forma *nombre=valor*. En este caso no importa el orden en que se envíen:

```python
#definición
def mi_funcion(uno, dos):
    <bloque-de la función>

#ejecuciones válidas
mi_funcion(uno = 1, dos = 2)
mi_funcion(dos = 2, uno = 1)
```

Si no se sabe el número exacto de argumentos nombrados que una función deberá recibir, se puede declarar un solo parámetro precedido de dos asteriscos(**), el cual será tratado como un diccionario de argumentos en el cuerpo de la función.

Los parámetros pueden ser optativos si se los define con un valor por defecto, y solo pueden ir al final de la lista:

```python
#definición
def mi_funcion(uno, dos = 2):
    <bloque-de la función>

#ejecuciones válidas
mi_funcion(1) # dos = 2
mi_funcion(1, 4) # dos = 4
```

#### Alcance

En Python las variables son globales si se "declaran" (asignan valor por primera vez) fuera de las funciones, en el primer nivel del código. Una variable global puede ser usada dentro de una función.

Las variables declaradas dentro de una función son locales, y no pueden ser usadas fuera de dicha función.

Puede haber problemas si dentro de una función se trata de cambiar el valor de una variable global, como por ejemplo con un `miVariable += 1`. El compilador se quejará, pensando que la variable es local y no tiene ningún valor actual. Para resolver esto, dentro de la función es necesario declararla con `global` antes de usarla: `global miVariable`:

```python
miVariable = 0
def miFuncion():
    global miVariable # pruebe a comentar esta línea
    miVariable += 1

miFuncion()
print(miVariable)
```

### Lambdas

Una función lambda es una pequeña función anónima que puede ejecutar una sola expresión y devuelve el resultado de dicha expresión. Se define con `lambda`. Una lambda puede guardarse en una variable o devolverse en una función:

```python
lambda <parametros>: <expresión>

#ejemplos
x = lambda a: a * 2
x(3) # 6

def f(n):
    return lambda a: a * n
x = f(2)
x(3) # 6
```

## Try (excepciones)

`try` permite capturar y tratar excepciones que puedan producirse en un bloque de código. Generalmente va atada a la palabra clave `except`:

```python
try:
    <bloque-resguardado>
except <excepcion-a-capturar>:
    <bloque-si-hay-excepción>
```

Si ocurre una excepción en el `try`, se salta directamente al `except`. Si no ocurre una excepción en el try, nunca se ejecuta el `except`. Puede haber varios bloques `except`, uno por cada tipo de excepción que se desee capturar.

```python
# este ejemplo siempre dará error
num = input("Enter number:")

if num > 1:
  print('no hubo error')
else:
  print('tampoco hubo error')
```

```python
# en cambio este ejemplo...
num = input("ingrese un número:")
try:
  if num > 1:
    print('no hubo error')
  else:
    print('tampoco hubo error')
except:
  if int(num) > 1:
    print('capturado error > 1')
  else:
    print('capturado error =< 1')
```

Opcionalmente puede haber un bloque `else` al final de todos los `except`, que se ejecutará solo si el `try` finaliza sin generar ninguna excepción:

```python
try:
    <bloque-resguardado>
except <excepcion-a-capturar>:
    <bloque-si-hay-excepción>
else:
    <bloque-si-NO-hay-excepción>
```

También se puede añadir al final de todo un bloque `finally` que se ejecutará siempre, haya o no haya excepciones:

```python
try:
    <bloque-resguardado>
except <excepcion-a-capturar>:
    <bloque-si-hay-excepción>
else:
    <bloque-si-NO-hay-excepción>
finally:
    <bloque-que-siempre-se-ejecuta>
```

---
**Ejercicios**

Modifique su programa para adivinar números de la siguiente manera:

- Cree una función principal que arranque su programa y que reciba como argumentos el rango de valores con el que trabajará
- Cree una función que reciba y controle el `input` del usuario, verificando que haya ingresado un número válido. Mientras no sea así, se le volverá a pedir que ingrese un número. La función devolverá el número en el formato correcto (int)
- Cree una función que registre el log del sistema. La función deberá recibir como argumentos: el archivo donde se guarda el log (el cual deberá haber sido abierto previamente) y el mensaje que se desea registrar en el log
    - su mensaje debería tener al menos
        - al arrancar el sistema, el timestamp y el número que se va a adivinar
        - por cada intento, el número ordinal del intento y el número ingresado por el usuario
- integre estas funciones en su programa

> En el archivo `adivinar.py` tiene una plantilla de referencia que puede utilizar y modificar según su interpretación del problema. Abra la plantilla directamente en [Google Colab](https://colab.research.google.com/drive/1FVqXEjMkyT6LBRfzaVVnEV2bDvPGF-Ub) (Recuerde hacer `File\Save a copy in Drive` antes de empezar a modificar el archivo)

> Si, luego de haberlo intentado por su cuenta, quiere ver otra solución posible, vaya al archivo [adivinarResuelto.py](adivinarResuelto.py)
---

## Clases

Una clase permite definir nuevos tipos de objetos y se crea con la palabra clave `class`:

```python
class <nombre-clase>:
    <bloque-de-instrucciones>
```

Las instrucciones dentro de una clase suelen ser inicialización de variables estáticas o definición de funciones. Ej:

```python
class Persona:
    nombre = 'Diego'

    def getNombre():
        return 'Mi nombre es ' + Persona.nombre
```

> En este caso tanto la variable como el método son estáticos y pueden ser accedidos como `Persona.nombre` o `Persona.getNombre()`

Si se desea crear objetos de instancia, para las variables esto es automático: el valor de la variable estática se copia a la variable de la instancia con el msmo nombre. En el caso de los métodos de instancia, estos deben llevar `self` como primer (o único) argumento. `self` hace referencia a la instancia del objeto que se ha creado.

> El nombre "self" es una convención, la variable podría tener otro nombre, pero esto podría llevar a confusión, de manera que se recomienda usar "self".

```python
class Persona:
    nombre = 'Diego'

    def getNombre(self):
        return 'Mi nombre es ' + self.nombre
```

Para crear una nueva instancia de una clase se usa su nombre seguido de paréntesis:

```python
p = Persona()
p.getNombre() # Mi nombre es Diego
```

> Atención! las variables estáticas y las de instancia son independientes. Al crear la instancia se copian los datos desde las variables estáticas, pero a partir de ahí dejan de estar ligadas. Pruebe el siguiente código y verá:

```python
class Persona:
    nombre = 'Diego'

p = Persona()
print(Persona.nombre)
print(p.nombre)
p.nombre = 'María'
print(Persona.nombre)
print(p.nombre)
Persona.nombre = 'Juan'
print(Persona.nombre)
print(p.nombre)
```

Se puede inicializar una instancia de clase con su método `__init__` (es el "constructor"):

```python
class Persona:
    def __init__(self, nombre):
        self.nombre = nombre
    def getNombre(self):
        return 'Mi nombre es ' + self.nombre

p = Persona('María')
p.getNombre() # Mi nombre es María
```

> Las variables de clase no hace falta declararlas. Se crean en cuanto se usan la primera vez: `self.nombre = nombre`

### Alcance

Las variables de clase en Python son siempre públicas, no existen variables privadas. Sin embargo, una convención es indicar que una variable debe ser tratada como privada, poniendo un guión bajo al inicio de su nombre: `_privada` (igual se puede acceder a la variables desde fuera!).

### Herencia

Si desea que su nueva clase herede las propiedades de otra, indique la clase madre entre paréntesis:

```python
class Persona(Humano):
    ...
```

En Python existe la herencia múltiple:

```python
class Persona(Humano, Animal, SerVivo):
    ...
```

> Al buscar alguna propiedad, primero se busca en Persona, luego en Humano (y sus clases madre), luego en Animal (y sus clases madre) y así sucesivamente.

### Documentación

Se puede incluir documentación en una clase poniéndola en comillas triples (simples o dobles):

```python
class Persona(Humano):
    '''Esta es mi documentación de clase'''
    ...
```
 La documentación se accede con la propiedad `__doc__`: `Persona.__doc__` o `p.__doc__`

