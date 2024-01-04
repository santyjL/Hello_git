# HEllo git 

el codigo no es el mejor , solo este es de prueba para aprender las bases de como funciona github con git 
>gracias por leer

# todo lo aprendido

# comandos :

### touch:

no es de git pero sirve para agregar un fichero o carpeta oculta en la terminal de la siguiente forma : touch .gitignore

### git :

muestra las principales combinaciones de git

### git add :

Agrega el fichero a la rama se llamaria con git add {rama}

### git commit :

guarda el fichero y lo junta en el historia de la carpeta se llama con git commit -m 'comentario obligatorio del fichero'

### git status :

muestra datos del la carpeta como cuantos commit hay guardados o cuales archivos no lo estan

### git init :

Crea un repositorio nuevo repositorio donde se pueden guardar y revisar nuevos ficheros

### git branch:

cambia el nombre del arbol , inicial mente es master , genericamente se cambia a main de la siguiente forma git branch -m main

> ### git branch {nueva rama}:
>
> tambien sirve para crear nuevas ramas de arbol

> ### git branch -d {rama}:
>
> para eliminar la rama cuando se termina de usar

### git log:

muestra el historial de los repositorios junto a sus comentarios se puede llamar haci como esta escrito y de formas variadas

> ### git log --graph:
>
> muestra las conexiones de cada rama

> ### git log --graph --pretty=oneline:
>
> muestra las conexiciones con solo una linea de diferencia

> ### git log --graph --decorate --oneline:
>
> elimina los bash para que sea mucho mas legible y con solo una linea de diferencia los ficheros

### git checkout:

regresa a una vercion del fichero llamado , se llama con git checkout {nombre del ficeho}

### git reset:

regresa al ultimo fichero guardado

> ### git reset --hard:
>
> este pide el fichero y lo que hace es regresar al fichero y eliminar los que van despues de el , solo se usaria en casos de cagada extremas , se llama : git reset --hard {bash}

### git config --global alias.{name} 'ejecucion' :

si encuentras una configuracion que uses mucho puedes crear un alia ejemplo : git config --global alias.tree 'git log --graph --pretty=oneline' ahora en lugar de llamar todo , solo llamas al alias que ejecutara esa funciones

### touch .gitignore:

añade gitgnore al repositorio , este permite oculta archivos a ojos de git

### git diff:

muestra los ultimos cambios sin la necesidad de usar un commit tambien puede mostrar cambios de ramas con git diff {rama}

### git riflog:

sirve para ver todos lo que se a hecho en el repositorio , y si usas un reset --hard puedes usarlo para buscar el fichero a regresar y volver a usar el reset --hard {fichero optenido}

### git tag:

sirve para documentar partes muy importantes por ejemplos verciones completas y si hay varios tag podemos ir de tag y tag con: git checkout tags/nombre del tag ,

los tag se definen con git tag {nombre} (hacerlo cuando se termina de guardar datos)

### git switch {nombre de rama} :

sirve para moverse de una rama a otra

### git merge:

unifica las ramas , juntando todos los cambios , se llama haci : git merge {rama a unificar} , no puedes poner la rama en la que estas tienes que poner otra rama

### git stach:

es para guardar datos de forma temporar si por ejemplo cambias de ramas o va a dejar el progreso a media para guardarlo de forma solo local , recomendado para equipos se llama para recuperar con git stach pop

> ### git stach drop :
>
> para eliminar los stach guardados

### git push:

el git push es para subir un repositorio a github si es que ya esta creado de la siguiente forma : git push -u origin {rama} . tambien sirve para actualizarlo

### git fetch:

te actualiza los cambios segun github sin descargarte los datos solo ver la documentacion de los comits con git log

### git pull :

el git pull es para subir como el fetch te trae la documentacion pero tambien te da los datos cambiados a tu local

### git clone:

para clonar un repositorio con : git clone {ssh or https} y se creara una nueva carpeta con todo

# git-flow

### git flow init

inicializa el flow en el codigo git

### git flow feature start {name}:

crea la rama feature

### git flow feature finish {name}:

elimina la rama y guarda todo el la rama develop

### git flow release start {tag}

crea un tag con un release , que es el momento antes de subirlo a main , es como una capa de seguridad para evitar problemas y revisar el codigo una vez mas

>### git flow release finish {tag}
> tambien es recomendable cerrar en kraken o la interfaz grafica de momento
