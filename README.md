# Taller 3 - Parte 2: Git y Manejo de Versiones

Este taller tiene como objetivo practicar los conceptos básicos de Git revisados en clase. Cada ejercicio le permitirá poner en práctica los conceptos vistos en las diapositivas anteriores.

## Objetivo General
El objetivo principal es reforzar los conocimientos básicos de Git y GitHub, realizando operaciones como creación de repositorios, commits, y manejo de versiones en un repositorio remoto.

---

## Instrucciones

### Punto 0 | Preparación
1. **Retomar trabajo previo**: Utilice el trabajo realizado en la **Parte 1** de este taller.
2. **Instalar Git**: Descargue e instale Git desde [Git-SCM](https://git-scm.com/downloads).

### Punto 1.1 | Crear una cuenta en GitHub
1. Si no tiene una cuenta en GitHub, cree una en [GitHub](https://github.com/).
2. Una vez creada, puede continuar con los siguientes pasos.

### Punto 1.2 | Crear un nuevo repositorio
1. Cree un nuevo repositorio en su perfil de GitHub con el nombre `TALLER3-LOGIN`, donde `LOGIN` es su nombre de usuario.
2. **Nota**: No utilice puntos en el nombre del repositorio.

### Punto 2 | Primera versión
1. Después de crear el repositorio, asocie el proyecto de la **Parte 1** con este repositorio.
2. Puede utilizar los comandos sugeridos por la página del repositorio en GitHub para hacer la conexión inicial.

### Punto 3 | Un pequeño cambio
1. Realice el siguiente cambio en el código:
   - Actualice el límite de ratones para la clase `BoaConstrictor` en la guardería, de manera que el límite sea ahora **20** ratones.
   
### Punto 4 | Crear una nueva versión
1. Después de realizar el cambio en el **Punto 3**, cree un nuevo commit.
   - Utilice el mensaje `nueva versión` para describir este commit.
2. Suba esta nueva versión al repositorio con el comando:

   ```bash
   git push
