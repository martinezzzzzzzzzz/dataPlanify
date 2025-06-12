import json
from datetime import datetime, timedelta
import random

def generar_tarea(id_tarea):
    estados = ["completada", "en progreso", "pendiente"]
    prioridades = ["alta", "media", "baja"]
    fecha_inicio = datetime(2025, 1, 1) + timedelta(days=random.randint(0, 150))
    fecha_fin = fecha_inicio + timedelta(days=random.randint(3, 15))
    return {
        "id": id_tarea,
        "titulo": f"Tarea {id_tarea}",
        "descripcion": f"Descripción de la tarea {id_tarea}",
        "fecha_inicio": fecha_inicio.strftime("%Y-%m-%d"),
        "fecha_fin": fecha_fin.strftime("%Y-%m-%d"),
        "estado": random.choice(estados),
        "prioridad": random.choice(prioridades)
    }

def generar_proyecto(id_proyecto, tareas_por_proyecto):
    tareas = [generar_tarea(tid) for tid in range(1, tareas_por_proyecto + 1)]
    fecha_creacion = datetime(2025, 1, 1) + timedelta(days=random.randint(0, 150))
    return {
        "id": id_proyecto,
        "nombre": f"Proyecto {id_proyecto}",
        "descripcion": f"Descripción del proyecto {id_proyecto}",
        "fecha_creacion": fecha_creacion.strftime("%Y-%m-%d"),
        "estado": random.choice(["pendiente", "en progreso", "completado"]),
        "tareas": tareas
    }

def generar_usuario(id_usuario, num_proyectos_por_usuario, tareas_por_proyecto):
    proyectos = [
        generar_proyecto(pid + id_usuario * 1000, tareas_por_proyecto)
        for pid in range(1, num_proyectos_por_usuario + 1)
    ]
    return {
        "id": id_usuario,
        "nombre": f"Usuario{id_usuario}",
        "email": f"usuario{id_usuario}@planify.com",
        "tipo_cuenta": random.choice(["gratis", "básica", "premium"]),
        "fecha_registro": (datetime(2024, 1, 1) + timedelta(days=random.randint(0, 300))).strftime("%Y-%m-%d"),
        "proyectos": proyectos
    }

num_usuarios = 50
num_proyectos_por_usuario = 3
tareas_por_proyecto = 10

usuarios = [generar_usuario(uid, num_proyectos_por_usuario, tareas_por_proyecto) for uid in range(1, num_usuarios + 1)]

data = {
    "status": "success",
    "timestamp": datetime.utcnow().isoformat() + "Z",
    "data": {
        "usuarios": usuarios
    }
}

with open("planify_50usuarios_3proyectos.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("Archivo JSON generado con éxito.")
