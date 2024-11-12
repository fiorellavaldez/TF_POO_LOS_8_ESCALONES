from preguntaDesempate import preguntaDesempate 
from preguntaRonda import preguntaRonda
import random
from Escalon import Escalon
from Partida import Partida
from Jugador import Jugador
from Tema import Tema

################################################# boceto de lo queseria una partida

#iniciaria el juego nuevo pidiendo a la base de datos una lista con los temas disponibles para jugar

jugador1 = Jugador("j1","1")
jugador2 = Jugador("j2","2")
jugador3 = Jugador("j3","3")
jugador4 = Jugador("j4","4")
jugador5 = Jugador("j5","5")
jugador6 = Jugador("j6","6")
jugador7 = Jugador("j7","7")
jugador8 = Jugador("j8","8")
jugador9 = Jugador("j9","9")

listaJugadores = [jugador1,jugador2, jugador3,jugador4,jugador5,jugador6,jugador7,jugador8,jugador9] #lista de jugadores completa

listaTemas = []

listaTemas.cargarTemas() #este "cargarTemas " baja todos los temas disponibles con todas sus preguntas

#Seleccionamos 8 temas para cada escalon

tema1 = Tema(1,1)
tema2 = Tema(2,2)
tema3 = Tema(3,3)
tema4 = Tema(4,4)
tema5 = Tema(5,5)
tema6 = Tema(6,6)
tema7 = Tema(7,7)
tema8 = Tema(8,8)
tema9 = Tema(9,9)

random.shuffle(listaTemas)
lista8Temas=[tema1, tema2, tema3, tema4, tema5, tema6, tema7, tema8, tema9]

for i in range(8):
    lista8Temas.append(listaTemas(i))

# El escalon seria una clase en si, tendria datos como: participantes activos o eliminados, tema
escalon1 = Escalon()
escalon2 = Escalon()
escalon3 = Escalon()
escalon4 = Escalon()
escalon5 = Escalon()
escalon6 = Escalon()
escalon7 = Escalon()
escalon8 = Escalon()

escalon1.set_jugadores(listaJugadores) # le doy la lista de jugadoes completa al primer escalon

listaEscalones = [escalon1, escalon2, escalon3, escalon4, escalon5, escalon6, escalon7, escalon8]

for i in range(8):
    listaEscalones[i].set_tema(lista8Temas[i]) # Con esto ya tengo un tema para cada escalón

partida = Partida(listaEscalones) #instanciamos el objeto partida con los 8 escalones


#for i in range (listaEscalones):
    
    #iniciamos una ronda
    #ronda1
    
    #le hacemos una pregunta a un jugador, obtenemos si acertó o no 
    #le hacemos una pregunta al siguiente y así hasta completar una pregunta a cada jugador
    
    #ronda2
    #le hacemos una pregunta a un jugador, obtenemos si acertó o no 
    #le hacemos una pregunta al siguiente y así hasta completar una pregunta a cada jugador

    #evaluamos los errores de todos los jugadores y puede suceder lo siguiente

        # TODOS BIEN: Empatan todos los jugadores contenstando bien todas las preguntas de las 2 rondas --> los jugadores van a ronda de pregutna de desempate
        
        # 2 O MAS EMPATADOS: Empatan 2 o mas jugadores en mayor cantidad de errores --> los jugadores empatados van a ronda de pregunta de desempate
        
        # Hay solo un jugador que tiene mas erradas que los demas --> se elimina ese jugador de la lista de jugadores
        
    # se hace un desempate si es necesario entre los jugadores empatados
    
    #en cualquiera de los 3 casos anteriores, se elimina un solo jugador

    # i = escalon
    
def iniciar_partida(partida):
    """
    Procedimiento que recorre los escalones de la partida, ejecutando las rondas y manejando las eliminaciones.
    :param partida: Partida, objeto que contiene los escalones y jugadores
    """
    for escalon in partida.get_escalones():
        print(f"\n--- Comenzando Escalón con tema {(escalon.get_tema()).get_nombreTema()} ---")

        # Ronda 1
        for jugador in escalon.get_jugadores():
            # Simulamos hacerle una pregunta y obtener si acertó (0: no contestó, 1: acertó, 2: falló)
            jugador.set_ronda1(hacer_pregunta(jugador, (escalon.get_tema()).get_preguntas_deronda))  # <------------------ACA NOS QUEDAMOS!!!
        
        # Ronda 2
        for jugador in escalon.get_jugadores():
            jugador.ronda2 = hacer_pregunta(jugador, escalon.tema.preguntas_deronda)

        # Evaluamos los resultados de las dos rondas
        jugadores_a_desempatar = evaluar_jugadores(escalon.jugadores)
        
        # Si hay jugadores empatados (o todos acertaron), hacemos un desempate
        if len(jugadores_a_desempatar) > 1:
            print("Empate detectado. Comenzando ronda de desempate...")
            jugadores_a_eliminar = hacer_desempate(jugadores_a_desempatar, escalon.tema.preguntas_desempate)
        else:
            # Si solo hay un jugador con más errores, lo eliminamos directamente
            jugadores_a_eliminar = jugadores_a_desempatar

        # Eliminamos al jugador correspondiente
        for jugador in jugadores_a_eliminar:
            escalon.eliminar_jugador(jugador)

def hacer_pregunta(jugador, preguntas):
    """
    Simula hacer una pregunta al jugador y devuelve si acertó o no.
    :param jugador: Jugador, objeto de la clase Jugador
    :param preguntas: list, lista de preguntas disponibles
    :return: int, 1 si acertó, 2 si falló
    """
    # Aquí puedes hacer la lógica para elegir una pregunta y obtener una respuesta del jugador
    # Por ahora, simulamos respuestas aleatorias:
    import random
    resultado = random.choice([1, 2])  # 1: acertó, 2: falló
    print(f"{jugador.nombre} responde {'bien' if resultado == 1 else 'mal'} en la ronda.")
    return resultado

def evaluar_jugadores(jugadores):
    """
    Evalúa los resultados de las dos rondas para determinar quiénes van a desempate o quién será eliminado.
    :param jugadores: list, lista de objetos de la clase Jugador
    :return: list, lista de jugadores que deben ir a desempate o el jugador que será eliminado
    """
    jugadores_errados = {}
    
    # Contar los errores de cada jugador (ronda 1 + ronda 2)
    for jugador in jugadores:
        errores = (jugador.ronda1 == 2) + (jugador.ronda2 == 2)
        jugadores_errados[jugador] = errores
    
    # Buscamos los jugadores con el máximo número de errores
    max_errores = max(jugadores_errados.values())
    jugadores_con_max_errores = [jugador for jugador, errores in jugadores_errados.items() if errores == max_errores]
    
    # Si todos acertaron todas las preguntas
    if max_errores == 0:
        print("Todos los jugadores acertaron, van a desempate.")
        return jugadores
    
    # Si hay empate entre dos o más jugadores con el máximo de errores
    if len(jugadores_con_max_errores) > 1:
        print(f"Empate entre {len(jugadores_con_max_errores)} jugadores con más errores.")
        return jugadores_con_max_errores
    
    # Si hay un único jugador con más errores
    print(f"{jugadores_con_max_errores[0].nombre} tiene más errores y será eliminado.")
    return jugadores_con_max_errores

def hacer_desempate(jugadores, preguntas_desempate):
    """
    Simula la ronda de desempate entre los jugadores empatados.
    :param jugadores: list, lista de objetos de la clase Jugador que irán al desempate
    :param preguntas_desempate: list, lista de preguntas de desempate disponibles
    :return: list, lista de un solo jugador que será eliminado
    """
    import random

    # Hacemos preguntas de desempate a los jugadores
    respuestas = {}
    for jugador in jugadores:
        respuesta = random.randint(1, 100)  # Simulamos una respuesta numérica para la pregunta de desempate
        respuestas[jugador] = respuesta
        print(f"{jugador.nombre} responde {respuesta} en la pregunta de desempate.")

    # La respuesta correcta simulada
    respuesta_correcta = random.randint(1, 100)
    print(f"La respuesta correcta era: {respuesta_correcta}")

    # Evaluamos quién estuvo más cerca
    jugador_eliminado = min(jugadores, key=lambda j: abs(respuestas[j] - respuesta_correcta))
    
    print(f"{jugador_eliminado.nombre} estuvo más lejos y será eliminado.")
    return [jugador_eliminado]
