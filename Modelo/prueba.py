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
escalon1 = Escalon
escalon2 = Escalon
escalon3 = Escalon
escalon4 = Escalon
escalon5 = Escalon
escalon6 = Escalon
escalon7 = Escalon
escalon8 = Escalon

escalon1.set_jugadores(listaJugadores)

listaEscalones = [escalon1, escalon2, escalon3, escalon4, escalon5, escalon6, escalon7, escalon8]

for i in range(8):
    listaEscalones[i].set_tema(lista8Temas[i]) # Con esto ya tengo un tema para cada escalón

partida = Partida(listaEscalones) #instanciamos el objeto partida con los 8 escalones


































# todo el juego seria una iteracion sobre la lista de 8 escalones

# le doy los jugadores a escalon 1 
escalon1.set_jugadores(listaJugadores)

#les hacemos preguntas a los jugadores y sale quien tiene que ser eliminado

#escalon1.quitarJugador(jugador)
#escalon1.set_jugadorEliminado(jugador)

#terminó el escalon1

escalon2.set_jugadores(escalon1.get_jugadores())
    
    
    
    
    

