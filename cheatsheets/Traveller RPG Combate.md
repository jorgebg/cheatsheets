width: 100

# COMBATE: Tiempos

~~~
width: 50
footer: * Reglas de Cepheus Engine


## Iniciativa

### Comienzo del combate

Chequeo de **`DES`** o **`INT`**. El **Efecto** resultante es la **Iniciativa**. Se mantiene durante todo el combate.

**Emboscadas**: Se modifica la Iniciativa **solo durante la primera ronda**:

- Emboscadores: +6
- Emboscados: −6

**Táctica**: Mientras no sea emboscado, un Viajero de cada bando puede hacer un chequeo de Táctica, aplicando el Efecto a todos los miembros de su bando.

**Alcance**: En la mayoría de los combates, los Viajeros comienzan a alcance Medio (11-50m)

### Rondas

Se actúa por orden de **Iniciativa**. En caso de empate, el que tenga el mayor valor de `DES` va primero. Si aun así siguen empatados, entonces actúan a la vez.

**Apresurarse***: Recibe +2 a su Iniciativa durante esa ronda, pero todas sus acciones reciben un MD −1.
No puede apresurarse varias veces en la misma ronda.

**Demorarse***: Actúa mas tarde, incluso interrumpiendo las acciones de los demás.
Su Iniciativa pasará a tener el valor del turno en el que actúa.
Si al final de la ronda no ha actuado, puede actuar el primero en la siguiente ronda, y su Iniciativa pasará a ser un punto más alto que la Iniciativa más alta.

~~~
width: 50

## Plazos

Cada ronda dura 6 segundos.

| Plazo | Incremento | Ejemplo |
|:---|---|---|
| 1D segundos | Un segundo | Atacar, saltar |
| 1D turnos | Un turno | Seis segundos  |
| 1D x 10 segundos | Diez segundos | Redireccionar energía, abrir canales de comunicación |
| 1D minutos | Un minuto | Primeros Auxilios, Aterrizaje seguro, tareas técnicas básicas |
| 1D x 10 minutos | Diez minutos | Tareas técnicas más complejas, registrar un área |
| 1D horas | Una hora | Construir un refugio, atravesar la espesura salvaje |
| 1D x 4 horas | Cuatro horas | Investigar un problema |
| 1D x 10 horas | Diez horas | Reparar una nave dañada |
| 1D días | Un día | Peinar una ciudad en busca de una persona desaparecida |

**Actuar más rápido**: MD −2 por cada nivel reducido.

**Actuar más lento**: MD +2 por cada nivel aumentado.

---

### Acciones Extendidas

Son chequeos que requieren más tiempo que un único turno de combate.

Si se recibe daño durante una acción extendida, se debe realizar un chequeo de la habilidad usada con el daño recibido como MD negativo. Si falla, este turno de trabajo no contará. Si el Efecto es de -6 o menos, tendrá que volver a empezar.


~~~

width: 100

# COMBATE: Acciones

~~~
width: 20

## Acciones por turno

<div markdown="1" align="center">
**1 acción Mayor** y **1 acción Menor**

o bien

**3 acciones Menores**
</div>

Pueden también realizar cualquier cantidad de **Reacciones** y **acciones Gratuitas**.

---

### Acciones Gratuitas

Acciones que pueden realizarse rápidamente.

Ejemplos: gritar un aviso o pulsar un botón.


~~~
width: 40
## Acciones Mayores


**Atacar**: Chequeo de la habilidad apropiada.


|Ataque|MD Attributo|Habilidad
|:---|---|---|
|Cuerpo a Cuerpo|`FUE` o `DES`|Combate CaC|
|Disparar|`DES`|Armas de Fuego o<br/>Armas Pesadas|
|Lanzar|`DES`|Atletismo (destreza)|

Si tiene éxito, tira el daño indicado en el arma mas lo siguientes modificadores:

|Daño|
|:---|
|`+` Efecto del ataque (excepto armas Destructivas)|
|`+` MD de `FUE` (si es Cuerpo a Cuerpo)|
|`−` Armadura del objetivo|
|`−` Cobertura del objetivo (si está totalmente cubierto)|

Un ataque de Efecto de 6+ siempre inflige al menos 1 punto de daño.

**Miscelánea**: Un Viajero puede hacer un chequeo de habilidad o algo diferente como acción Mayor cuando requiera su total atención,
concentración, acciones físicas o mentales complicadas, o
una combinación de ellas. Ejemplos:

- Aplicar primeros auxilios a un compañero herido.
- Tratar de esquivar el sistema de seguridad para obtener acceso a un búnker.
- Solicitar un ataque de artillería.

~~~
width: 40

## Acciones Menores

**Mover**:  6 metros (½ en terreno difícil, ¼ tumbado). Por cada 10m completos con relación al atacante, ataques a distancia recibidos sufren -1 MD.

**Cambiar de posición**: Ponerse en pie, agacharse o tumbarse.

**Desenfundar**

**Recargar**

**Apuntar**: +1 MD a impactar (+2 MD con mira láser). Acumulable hasta +6. Tienen que ser acciones consecutivas, no se pueden hacer otras acciones.

**Liderazgo**: Chequeo de Liderazgo. El Efecto es el número de Ventajas que puede otorgar a cualquier chequeo de
habilidad (incluyendo ataques) a otros combatientes de su mismo bando.
Si el Efecto es negativo, el
bando opuesto puede imponer un número de Desventajas
igual al Efecto. Debe ser capaz de comunicarse libremente con los demás. Puede ser una acción Mayor si las órdenes son complejas.

**Miscelánea**: Acciones que no requieran plena atención, concentración o acciones físicas o mentales complicadas.
Ejemplos:

- Encontrar una buena posición de disparo.
- Identificar el equipamiento utilizado por un enemigo.
- Recoger algo del suelo o de una superficie cercana.

~~~

width: 30

# COMBATE: Acciones

~~~

width: 70

# COMBATE: Ataques

~~~
width: 30

## Reacciones

Se realizan fuera del turno como reacción a ataques enemigos.

Cada Reacción infringe MD-1 en su siguiente conjunto de acciones.

**Parada** (Ataques CaC): Penalización igual a su Combate CaC a la tirada de ataque del enemigo.

**Esquivar** (Ataques CaC y a Distancia): Penalización igual a su MD de `DES` o Atletismo (destreza) a la tirada de ataque del enemigo.

**Buscar cobertura** (Ataques a Distancia): Similar a esquivar, pero se lanzará al suelo y, con suerte,
detrás de algo sólido. No podrá actuar en su siguiente turno.

- Con cobertura: Infligirá un MD-2 en la
tirada de ataque a cada atacante que le tenga como objetivo en este turno de combate y puede beneficiarse del bono por cobertura a
su Armadura. Puede cubrirse tras cualquier objeto dentro de un radio de
1,5 metros de su posición actual.
- Sin cobertura: Inflingirá MD-1 a cualquier tirada
de ataque en su contra por considerarse un objetivo tumbado.

~~~
width: 40

## Heridas

El Daño se aplica a los atributos. Los MD de los atributos se recalculan y se utiliza el valor dañado hasta ser curados.

Primero se aplica a la `RES` del objetivo. Cuando `RES` llegue a 0, se aplica a la `FUE` o `DES` del objetivo, en función de la localización del impacto:

,,,
1D,Localización, Atributo
1,Cabeza,`DES`
2,Brazos,`FUE`
3-5,Torso,`FUE`
6,Piernas,`FUE`
,,,

Si la `FUE` o la `DES` es reducida a 0, cae inconsciente. Si los tres atributos físicos se reducen a 0, muere.

### Inconsciencia

Debe realizar un chequeo de `RES` cada minuto. Si tiene éxito, recupera la conciencia. Si falla, debe esperar otro minuto antes de intentarlo de nuevo, esta vez con un MD+1 acumulativo.

## Primeros Auxilios

Restaura un número de puntos de atributo iguales al Efecto del chequeo de Medicina. Los puntos restaurados por los primeros auxilios se dividen según se desee entre todos los atributos físicos dañados. Los primeros auxilios deben iniciarse dentro de los primeros minutos tras la lesión. La tarea lleva 1D6 minutos.

~~~
width: 30

## Modificadores al disparar

### Distancia

|Alcance|MD|Rango|
|:---|---:|---|
|Corto  |+1|0% y 50%|
|Largo  |−1|100% y 200%|
|Extremo|−2|200% y 400%|

### Posición

|Objetivo|MD|
|:---|---|
|Rápido|−1 por cada 10 m|
|En cobertura|−2|
|Tumbado|−1|

Atacar a una localización específica del objetivo: MD −2 (MD −6 si disparando en Automático)

---

## Esconderse

Si el objetivo está totalmente oculto detrás de la cobertura (sin realizar ningún ataque), obtiene un bono a la armadura:

|Cobertura|Bono|
|:---|---|
|Vegetación| +2|
|Tronco de un árbol| +6|
|Muro de piedra| +8|
|Vehículo civil| +10|
|Vehículo blindado| +15|
|Fortificaciones| +20|

~~~
width: 100

# COMBATE: Cuerpo a Cuerpo

~~~
width: 30

## Combate personal

Dos combatientes a menos de 2m se consideran trabados en combate personal:

- Pueden atacar en combate CaC.
- Ninguno de ellos pueden atacar a otro objetivo salvo aquel con el que estén trabados en combate personal.
- Solo pueden utilizarse armas a distancia de una sola mano (pistolas) y pueden ser parada en combate personal (desviando el arma).
- Armas a distancia grandes (rifles) solo pueden utilizarse como garrotes.
- Si uno de los combatientes se desplaza, su enemigo puede realizar un ataque inmediato con MD+2.

~~~
width: 40

## Forcejear

En combate personal, un Viajero puede intentar agarrar o contener a su enemigo en vez de simplemente golpearle.

Chequeo opuesto de Combate CaC (desarmado) contra su objetivo usando su MD de `FUE` o `DES`. El ganador de esta tirada puede escoger una de las siguientes opciones:

- Derribar a su oponente.
- Desarmar a su oponente. Si el Efecto es de 6+, puede coger el arma de su oponente.
- Lanzar a su oponente 1D metros, causando 1D daño. Esta opción termina automáticamente con el forcejeo.
- Infligir daño igual a 2+ el Efecto del chequeo de Combate CaC, ignorando cualquier armadura.
- Infligir daño usando una pistola o un arma de filo pequeña.
- Escapar y alejarse (como una acción de movimiento normal), terminando con el forcejeo.
- Arrastrar a su oponente hasta 3 metros.
- Continuar con el forcejeo sin ningún otro efecto.

Mientras este envuelto en un forcejeo, el Viajero no puede hacer nada excepto chequeos opuestos de Combate CaC (desarmado).

~~~
width: 30


## Dos Armas

Si un Viajero está usando dos armas a la vez, puede atacar con ambas en el mismo turno de combate. Sin embargo, no puede apuntar con ninguna y sufrirá MD-2 en cada una de las tiradas de ataque. Esta penalización no se aplica si el Viajero porta dos armas, pero solo ataca con una.

