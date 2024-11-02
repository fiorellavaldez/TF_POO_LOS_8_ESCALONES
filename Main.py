from DAOjugador import DAOjugador

jugador_dao = DAOjugador()

# Agregar un jugador
jugador_id = jugador_dao.agregar_jugador('Juan Pérez', 0, True)
print(f"Jugador agregado con ID: {jugador_id}")

# Obtener un jugador
jugador = jugador_dao.obtener_jugador(jugador_id)
print(f"Jugador obtenido: {jugador.nombre_usuario}, {jugador.puntaje}, {jugador.activo}")

# Actualizar un jugador
jugador_dao.actualizar_jugador(jugador_id, puntaje=10)
jugador_actualizado = jugador_dao.obtener_jugador(jugador_id)
print(f"Jugador actualizado: {jugador_actualizado.nombre_usuario}, {jugador_actualizado.puntaje}, {jugador_actualizado.activo}")

# Eliminar un jugador
jugador_dao.eliminar_jugador(jugador_id)
print(f"Jugador con ID {jugador_id} eliminado")