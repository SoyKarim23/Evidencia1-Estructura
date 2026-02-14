from datetime import datetime, timedelta

turnos = ("Mañana", "Tarde", "Noche")

def mostrar_turnos():
    print("Turnos disponibles:")
    i = 1
    for t in turnos:
        print(i, "-", t)
        i += 1

def fecha_valida(fecha_texto):
    try:
        fecha = datetime.strptime(fecha_texto, "%Y-%m-%d")
        hoy = datetime.now()
        limite = hoy + timedelta(days=2)
        if fecha >= limite:
            return True
        else:
            return False
    except:
        return False

def crear_pedido(folio, cliente, fecha, turno, evento):
    return (folio, cliente, fecha, turno, evento)

def mostrar_pedido(p):
    print("\nPedido guardado:")
    print("Folio:", p[0])
    print("Cliente:", p[1])
    print("Fecha:", p[2])
    print("Turno:", p[3])
    print("Evento:", p[4])

print("Sistema de pedidos de catering")

mostrar_turnos()

cliente = input("Nombre del cliente: ")
fecha = input("Fecha del pedido (YYYY-MM-DD): ")

opcion_turno = int(input("Selecciona turno (1-3): "))
turno_seleccionado = turnos[opcion_turno - 1]

evento = input("Nombre del evento: ")

if fecha_valida(fecha):
    pedido = crear_pedido("F001", cliente, fecha, turno_seleccionado, evento)
    mostrar_pedido(pedido)
else:
    print("La fecha no es válida. Debe ser con al menos 2 días de anticipación.")