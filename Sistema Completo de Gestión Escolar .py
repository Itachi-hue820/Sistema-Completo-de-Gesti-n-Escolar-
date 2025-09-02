"""

🚧===============================================================================🚧
                    SISTEMA DE GESTIÓN ESCOLAR - VERSIÓN BETA
                        Desarrollado por Paolo - Verano 2025
🚧===============================================================================🚧

"""

# 🎯 ESTADO ACTUAL DEL PROYECTO:
# ✅ Estructura modular básica implementada
# ✅ Menús principales funcionando
# ✅ Sistema de roles implementado
# ✅ Mensajes UX trilingües añadidos (ES/EN/JP)
# 🔄 En proceso de refactorización y limpieza

# 🛠️ PENDIENTES CRÍTICOS PARA FINALIZAR:
# 📋 Todo LIST - NO BORRAR HASTA COMPLETAR:

# 🔴 PRIORIDAD MÁXIMA:
# [ ] Crear función mensaje_no_implementado() para eliminar código repetido
# [ ] Implementar expresión regular para validación de contraseñas
# [ ] Migrar TODOS los diccionarios a archivos JSON separados
# [ ] Arreglar imports rotos entre módulos

# 🟡 PRIORIDAD ALTA:
# [ ] Añadir try/except en lectura de archivos JSON
# [ ] Implementar manejo de errores para inputs críticos
# [ ] Validar que todas las referencias entre archivos funcionen
# [ ] Testear flujos principales sin crashes

# 🟢 MEJORAS FINALES:
# [ ] Documentar funciones principales con docstrings
# [ ] Limpiar comentarios innecesarios
# [ ] Verificar nomenclatura consistente
# [ ] Añadir README.md con instrucciones de uso

# 💡 NOTAS PARA EL DEVELOPER (Paolo futuro):
# - Los mensajes trilingües están OK, no tocar hasta refactor final
# - La estructura modular tiene errores esperados, arreglar con tutorial
# - Copy-paste fue decisión pragmática correcta para esta fase
# - Cuando refactorices: función mensaje_no_implementado() = 1 línea vs 50+

# 📅 DEADLINE OBJETIVO: 31 Agosto 2025

# 🎮 MOTIVACIÓN: Este proyecto abrirá puertas en Japón 🇯🇵
# Cada línea de código es un paso hacia tu sueño!

# 🔥 REMEMBER: "Perfect is the enemy of done" - pero "done" no significa "mal hecho"

# 🏫 Proyecto: Sistema Completo de Gestión Escolar
# 🔧 Python puro | ❌ Sin GUI |
# ❌ Sin DB | ✅ Terminal + Archivos `.json/.txt`

# ----------------------------------------------------

# Mi codigo.

# ✅ FASE 1.

# ----------------------------------------------------

# MAPEO DE IDENTIFICADORES

# Este bloque define todos los diccionarios, funciones y clases
# utilizados en el sistema, con comentarios para entender fácilmente
# su propósito y relación en el proyecto.

# ----------------------------------------------------

# DICCIONARIOS GENERALES

# Estos almacenan datos globales de la aplicación escolar.

# diccionario_eventos = {}              # Almacena eventos escolares importantes
# diccionario_avisos = {}               # Almacena avisos generales para todos
# diccionario_calificaciones = {}       # Guarda las calificaciones de los alumnos
# diccionario_materiales = {}           # Materiales educativos disponibles para descargar
# diccionario_encuestas = {}            # Encuestas escolares y sus resultados

# ----------------------------------------------------

# DICCIONARIOS DE TAREAS POR CLASE

# Cada uno guarda las tareas asignadas a un grupo específico.

# diccionario_tareas_eso_a = {}         # Tareas para 1º-4º ESO grupo A
# diccionario_tareas_eso_b = {}         # Tareas para 1º-4º ESO grupo B
# diccionario_tareas_eso_c = {}         # Tareas para 1º-4º ESO grupo C
# diccionario_tareas_eso_d = {}         # Tareas para 1º-4º ESO grupo D
# diccionario_tareas_bach_a = {}        # Tareas para Bachillerato grupo A
# diccionario_tareas_bach_b = {}        # Tareas para Bachillerato grupo B
# diccionario_tareas_bach_c = {}        # Tareas para Bachillerato grupo C
# diccionario_tareas_bach_d = {}        # Tareas para Bachillerato grupo D

# ----------------------------------------------------

# DICCIONARIOS DE USUARIOS Y MENSAJES

# Contienen datos y mensajes de alumnos, profesores, administradores y dirección.

# diccionario_alumnos_ren1 = {}           # Datos de los alumnos
# diccionario_mensajes_alumnos_ren2 = {}  # Mensajes enviados por los alumnos
# diccionario_profesores_ren3 = {}        # Datos de los profesores
# diccionario_mensajes_profesores_ren4 = {} # Mensajes enviados a los profesores
# diccionario_trabajo = {}                # Trabajos de alumnos enviados a profesores
# diccionario_admin_ren5 = {}             # Datos de administradores
# diccionario_mensajes_admin_ren6 = {}    # Mensajes enviados a administradores
# diccionario_director_ren7 = {}          # Datos del director
# diccionario_mensajes_director_ren8 = {} # Mensajes enviados al director
# diccionario_jefe_estudios_ren9 = {}     # Datos del jefe de estudios
# diccionario_mensaje_jefe_estudios_ren10 = {} # Mensajes enviados al jefe de estudios

# ----------------------------------------------------

# DICCIONARIOS DE CLASES POR CURSO

# Guardan la lista de alumnos de cada clase y curso.

# diccionario_ESO_1_A = {}                # Alumnos de 1º ESO A
# diccionario_ESO_1_B = {}                # Alumnos de 1º ESO B
# diccionario_ESO_1_C = {}                # Alumnos de 1º ESO C
# diccionario_ESO_1_D = {}                # Alumnos de 1º ESO D
# diccionario_ESO_2_A = {}                # Alumnos de 2º ESO A
# diccionario_ESO_2_B = {}                # Alumnos de 2º ESO B
# diccionario_ESO_2_C = {}                # Alumnos de 2º ESO C
# diccionario_ESO_2_D = {}                # Alumnos de 2º ESO D
# diccionario_ESO_3_A = {}                # Alumnos de 3º ESO A
# diccionario_ESO_3_B = {}                # Alumnos de 3º ESO B
# diccionario_ESO_3_C = {}                # Alumnos de 3º ESO C
# diccionario_ESO_3_D = {}                # Alumnos de 3º ESO D
# diccionario_ESO_4_A = {}                # Alumnos de 4º ESO A
# diccionario_ESO_4_B = {}                # Alumnos de 4º ESO B
# diccionario_ESO_4_C = {}                # Alumnos de 4º ESO C
# diccionario_ESO_4_D = {}                # Alumnos de 4º ESO D
# diccionario_Bachiller_1_A = {}          # Alumnos de 1º Bachillerato A
# diccionario_Bachiller_1_B = {}          # Alumnos de 1º Bachillerato B
# diccionario_Bachiller_1_C = {}          # Alumnos de 1º Bachillerato C
# diccionario_Bachiller_1_D = {}          # Alumnos de 1º Bachillerato D
# diccionario_Bachiller_2_A = {}          # Alumnos de 2º Bachillerato A
# diccionario_Bachiller_2_B = {}          # Alumnos de 2º Bachillerato B
# diccionario_Bachiller_2_C = {}          # Alumnos de 2º Bachillerato C
# diccionario_Bachiller_2_D = {}          # Alumnos de 2º Bachillerato D

# ----------------------------------------------------

# CALENDARIOS ESCOLARES

# Guardan la planificación de cada clase.

# diccionario_calendario_A = {}           # Calendario escolar de la clase A
# diccionario_calendario_B = {}           # Calendario escolar de la clase B
# diccionario_calendario_C = {}           # Calendario escolar de la clase C
# diccionario_calendario_D = {}           # Calendario escolar de la clase D

# ----------------------------------------------------

# FUNCIONES Y CLASES DEL SISTEMA

# es_verano_ren1()                        # Comprueba si es verano para apagar la aplicación
# seleccionar_rol()                       # Permite que el usuario elija su rol en el sistema
# Jerarquia(name_ren1: str)               # Clase padre para jerarquía de roles
# Alumno(Jerarquia)                       # Clase para el rol de alumno
# Profesor(Jerarquia)                     # Clase para el rol de profesor
# Director(Jerarquia)                     # Clase para el rol de director
# Jefe_de_estudios(Jerarquia)             # Clase para el rol de jefe de estudios
# Admin(Jerarquia)

# ----------------------------------------------------

# Importaciones.

import time
from datetime import datetime
import re
import json

# ----------------------------------------------------

# Diccionarios extras.

json_eventos = "Eventos.json"

diccionario_eventos: dict = {}

eventos_renombrado = diccionario_eventos


def create_json():
    try:
        with open(json_eventos, "w") as json_eventos_renombrado:
            json.dump(eventos_renombrado, json_eventos_renombrado)
        create_json()
        with open(json_eventos, "r") as json_eventos_renombrado:
            print(json_eventos_renombrado.read())
    except Exception as e:
        print(f"Se ha producido un error: {e}")


json_avisos = "Avisos.json"

diccionario_avisos: dict = {}

avisos_renombrado = diccionario_avisos


def create_json():
    try:
        with open(json_avisos, "w") as json_avisos_renombrado:
            json.dump(avisos_renombrado, json_avisos_renombrado)
        create_json()
        with open(json_avisos, "r") as json_avisos_renombrado:
            print(json_avisos_renombrado.read())
    except Exception as e:
        print(f"Se ha producido un error: {e}")


json_encuestas = "Encuestas.json"

diccionario_encuestas: dict = {}

encuestas_renombrado = diccionario_encuestas


def create_json():
    try:
        with open(json_encuestas, "w") as json_encuestas_renombrado:
            json.dump(encuestas_renombrado, json_encuestas_renombrado)
        create_json()
        with open(json_encuestas, "r") as json_encuestas_renombrado:
            print(json_encuestas_renombrado.read())
    except Exception as e:
        print(f"Se ha producido un error: {e}")


json_calificaciones = "Calificaciones.json"

diccionario_calificaciones: dict = {}

calificaciones_renombrado = diccionario_calificaciones


def create_json():
    try:
        with open(json_calificaciones, "w") as json_calificaciones_renombrado:
            json.dump(calificaciones_renombrado, json_calificaciones_renombrado)
        create_json()
        with open(json_calificaciones, "r") as json_calificaciones_renombrado:
            print(json_calificaciones_renombrado.read())
    except Exception as e:
        print(f"Se ha producido un error: {e}")


json_materiales = "Materiales.json"

diccionario_materiales: dict = {}

materiales_renombrado = diccionario_materiales


def create_json():
    try:
        with open(json_materiales, "w") as json_materiales_renombrado:
            json.dump(materiales_renombrado, json_materiales_renombrado)
        create_json()
        with open(json_materiales, "r") as json_materiales_renombrado:
            print(json_materiales_renombrado.read())
    except Exception as e:
        print(f"Se ha producido un error: {e}")


json_certificado = "Certificados.json"

diccionario_certificado: dict = {}

certificado_renombrado = diccionario_certificado


def create_json():
    try:
        with open(json_certificado, "w") as json_certificado_renombrado:
            json.dump(eventos_renombrado, json_certificado_renombrado)
        create_json()
        with open(json_certificado, "r") as json_certificado_renombrado:
            print(json_certificado_renombrado.read())
    except Exception as e:
        print(f"Se ha producido un error: {e}")


json_compañeros = "Compañeros.json"

diccionario_compañeros_ren10: dict = {}

compañeros_renombrado = diccionario_compañeros_ren10


def create_json():
    try:
        with open(json_compañeros, "w") as json_compañeros_renombrado:
            json.dump(compañeros_renombrado, json_compañeros_renombrado)
        create_json()
        with open(json_compañeros, "r") as json_compañeros_renombrado:
            print(json_compañeros_renombrado.read())
    except Exception as e:
        print(f"Se ha producido un error: {e}")


json_compañeros_mensajes = "Menssajes de compañeros.json"

diccionario_compañeros_mensajes_ren11: dict = {}

compañeros_mensajes_renombrado = diccionario_compañeros_mensajes_ren11


def create_json():
    try:
        with open(json_compañeros_mensajes, "w") as json_compañeros_mensajes_renombrado:
            json.dump(
                compañeros_mensajes_renombrado, json_compañeros_mensajes_renombrado
            )
        create_json()
        with open(json_compañeros_mensajes, "r") as json_compañeros_mensajes_renombrado:
            print(json_compañeros_mensajes_renombrado.read())
    except Exception as e:
        print(f"Se ha producido un error: {e}")


# ----------------------------------------------------

# Tareas eso a.

diccionario_tareas_eso_a: dict = {}

eso_a_renombrado = diccionario_tareas_eso_a

# ----------------------------------------------------

# Tareas eso b.

diccionario_tareas_eso_b: dict = {}

eso_b_renombrado = diccionario_tareas_eso_b

# ----------------------------------------------------

# Tareas eso c.

diccionario_tareas_eso_c: dict = {}

eso_c_renombrado = diccionario_tareas_eso_c

# ----------------------------------------------------

# Tareas eso d.

diccionario_tareas_eso_d: dict = {}

eso_d_renombrado = diccionario_tareas_eso_d

# ----------------------------------------------------

# Tareas bach a.

diccionario_tareas_bach_a: dict = {}

bach_a_renombrado = diccionario_tareas_bach_a

# ----------------------------------------------------

# Tareas bach b.

diccionario_tareas_bach_b: dict = {}

bach_b_renombrado = diccionario_tareas_bach_b

# ----------------------------------------------------

# Tareas bach c.

diccionario_tareas_bach_c: dict = {}

bach_c_renombrado = diccionario_tareas_bach_c

# ----------------------------------------------------

# Tareas bach d.

diccionario_tareas_bach_d: dict = {}

bach_d_renombrado = diccionario_tareas_bach_d

# ----------------------------------------------------

diccionario_encuestas: dict = {}

encuestas_renombrado = diccionario_encuestas

# ----------------------------------------------------

# Diccionarios alumnos.

json_alumnos = "Alumnos.json"

diccionario_alumnos_ren1: dict = {}

alumnos_renombrado = diccionario_alumnos_ren1


def create_json():
    try:
        with open(json_alumnos, "w") as json_alumnos_renombrado:
            json.dump(alumnos_renombrado, json_alumnos_renombrado)
        create_json()
        with open(json_alumnos, "r") as json_alumnos_renombrado:
            print(json_alumnos_renombrado.read())
    except Exception as e:
        print(f"Se ha producido un error: {e}")


diccionario_curso: dict = {}

curso_renombrado = diccionario_curso

json_mensajes_alumnos = "Mensajes de alumnos.json"

diccionario_mensajes_alumnos_ren2: dict = {}

mensajes_alumnos_renombrado = diccionario_mensajes_alumnos_ren2


def create_json():
    try:
        with open(json_mensajes_alumnos, "w") as json_mensajes_alumnos_renombrado:
            json.dump(mensajes_alumnos_renombrado, json_mensajes_alumnos_renombrado)
        create_json()
        with open(json_mensajes_alumnos, "r") as json_mensajes_alumnos_renombrado:
            print(json_mensajes_alumnos_renombrado.read())
    except Exception as e:
        print(f"Se ha producido un error: {e}")


# ----------------------------------------------------

# Diccionarios profes.

json_profesor = "Profesores.json"

diccionario_profesores_ren3: dict = {}

profes_renombrado = diccionario_profesores_ren3


def create_json():
    try:
        with open(json_profesor, "w") as json_profes_renombrado:
            json.dump(profes_renombrado, json_profes_renombrado)
        create_json()
        with open(json_profesor, "r") as json_profes_renombrado:
            print(json_profes_renombrado.read())
    except Exception as e:
        print(f"Se ha producido un error: {e}")


diccionario_mensajes_profesores_ren4: dict = {}

mensajes_profes_renombrado = diccionario_mensajes_profesores_ren4

diccionario_trabajo: dict = {}

trabajo_profes_renombrado = diccionario_trabajo

diccionario_asignatura: dict = {}

asignaturas_profes_renombrado = diccionario_asignatura

# ----------------------------------------------------

# Diccionarios admin.

json_admin = "Admin.json"

diccionario_admin_ren5: dict = {}

admin_renombrado = diccionario_admin_ren5


def create_json():
    try:
        with open(json_admin, "w") as json_admin_renombrado:
            json.dump(admin_renombrado, json_admin_renombrado)
        create_json()
        with open(json_admin, "r") as json_admin_renombrado:
            print(json_admin_renombrado.read())
    except Exception as e:
        print(f"Se ha producido un error: {e}")


json_mensajes_admin = "Admin mensajes.json"

diccionario_mensajes_admin_ren6: dict = {}

mensajes_admin_renombrado = diccionario_mensajes_admin_ren6


def create_json():
    try:
        with open(json_mensajes_admin, "w") as json_mensajes_admin_renombrado:
            json.dump(mensajes_admin_renombrado, json_mensajes_admin_renombrado)
        create_json()
        with open(json_mensajes_admin, "r") as json_mensajes_admin_renombrado:
            print(json_mensajes_admin_renombrado.read())
    except Exception as e:
        print(f"Se ha producido un error: {e}")


# ----------------------------------------------------

# Diccionarios director.

json_director = "Director.json"

diccionario_director_ren7: dict = {}

director_renombrado = diccionario_director_ren7


def create_json():
    try:
        with open(json_director, "w") as json_director_renombrado:
            json.dump(director_renombrado, json_director_renombrado)
        create_json()
        with open(json_director, "r") as json_director_renombrado:
            print(json_director_renombrado.read())
    except Exception as e:
        print(f"Se ha producido un error: {e}")


json_mensajes_director = "Director mensajes.json"

diccionario_mensajes_director_ren8: dict = {}

mensajes_director_renombrado = diccionario_mensajes_director_ren8


def create_json():
    try:
        with open(json_mensajes_director, "w") as json_mensajes_director_renombrado:
            json.dump(mensajes_director_renombrado, json_mensajes_director_renombrado)
        create_json()
        with open(json_mensajes_director, "r") as json_mensajes_director_renombrado:
            print(json_mensajes_director_renombrado.read())
    except Exception as e:
        print(f"Se ha producido un error: {e}")


# ----------------------------------------------------

# Diccionarios Jefe de estudios.

json_jefe_estudios = "Jefe de estudios.json"

diccionario_jefe_estudios_ren9: dict = {}

jefe_de_estudios_renombrado = diccionario_jefe_estudios_ren9


def create_json():
    try:
        with open(json_jefe_estudios, "w") as json_jefe_de_estudios_renombrado:
            json.dump(jefe_de_estudios_renombrado, json_jefe_de_estudios_renombrado)
        create_json()
        with open(json_jefe_estudios, "r") as json_jefe_de_estudios_renombrado:
            print(json_jefe_de_estudios_renombrado.read())
    except Exception as e:
        print(f"Se ha producido un error: {e}")


json_mensaje_jefe_estudios = "Mensajes Jefe de estudios.json"

diccionario_mensaje_jefe_estudios_ren10: dict = {}

mensaje_jefe_de_estudios_renombrado = diccionario_mensaje_jefe_estudios_ren10


def create_json():
    try:
        with open(json_mensaje_jefe_estudios, "w") as json_jefe_de_estudios_renombrado:
            json.dump(jefe_de_estudios_renombrado, json_jefe_de_estudios_renombrado)
        create_json()
        with open(json_mensaje_jefe_estudios, "r") as json_jefe_de_estudios_renombrado:
            print(json_jefe_de_estudios_renombrado.read())
    except Exception as e:
        print(f"Se ha producido un error: {e}")


# ----------------------------------------------------

# Diccionarios 1 de la ESO.

diccionario_ESO_1_A: dict = {}

eso_1_a_renombrado = diccionario_ESO_1_A

diccionario_ESO_1_B: dict = {}

eso_1_b_renombrado = diccionario_ESO_1_B

diccionario_ESO_1_C: dict = {}

eso_1_c_renombrado = diccionario_ESO_1_C

diccionario_ESO_1_D: dict = {}

eso_1_d_renombrado = diccionario_ESO_1_D

# ----------------------------------------------------

# Diccionarios 2 de la ESO.

diccionario_ESO_2_A: dict = {}

eso_2_a_renombrado = diccionario_ESO_2_A

diccionario_ESO_2_B: dict = {}

eso_2_b_renombrado = diccionario_ESO_2_B

diccionario_ESO_2_C: dict = {}

eso_2_c_renombrado = diccionario_ESO_2_C

diccionario_ESO_2_D: dict = {}

eso_2_d_renombrado = diccionario_ESO_2_D

# ----------------------------------------------------

# Diccionarios 3 de la ESO.

diccionario_ESO_3_A: dict = {}

eso_3_a_renombrado = diccionario_ESO_3_A

diccionario_ESO_3_B: dict = {}

eso_3_b_renombrado = diccionario_ESO_3_B

diccionario_ESO_3_C: dict = {}

eso_3_c_renombrado = diccionario_ESO_3_C

diccionario_ESO_3_D: dict = {}

eso_3_d_renombrado = diccionario_ESO_3_D

# ----------------------------------------------------

# Diccionarios 4 de la ESO.

diccionario_ESO_4_A: dict = {}

eso_4_a_renombrado = diccionario_ESO_4_A

diccionario_ESO_4_B: dict = {}

eso_4_b_renombrado = diccionario_ESO_4_B

diccionario_ESO_4_C: dict = {}

eso_4_c_renombrado = diccionario_ESO_4_C

diccionario_ESO_4_D: dict = {}

eso_4_d_renombrado = diccionario_ESO_4_D

# ----------------------------------------------------

# Diccionarios 1 de Bachillerato.

diccionario_Bachiller_1_A: dict = {}

Bachiller_1_a_renombrado = diccionario_Bachiller_1_A

diccionario_Bachiller_1_B: dict = {}

Bachiller_1_b_renombrado = diccionario_Bachiller_1_B

diccionario_Bachiller_1_C: dict = {}

Bachiller_1_c_renombrado = diccionario_Bachiller_1_C

diccionario_Bachiller_1_D: dict = {}

Bachiller_1_d_renombrado = diccionario_Bachiller_1_D

# ----------------------------------------------------

# Diccionarios 2 de Bachillerato.

diccionario_Bachiller_2_A: dict = {}

Bachiller_2_a_renombrado = diccionario_Bachiller_2_A

diccionario_Bachiller_2_B: dict = {}

Bachiller_2_b_renombrado = diccionario_Bachiller_2_B

diccionario_Bachiller_2_C: dict = {}

Bachiller_2_c_renombrado = diccionario_Bachiller_2_C

diccionario_Bachiller_2_D: dict = {}

Bachiller_2_d_renombrado = diccionario_Bachiller_2_D

# ----------------------------------------------------

# Calendarios.

# Calendario clase A .

diccionario_calendario_A: dict = {
    "ESO_A": {
        "Lunes_1": "Matemáticas",
        "Lunes_2": "Lengua Castellana",
        "Lunes_3": "Recreo",
        "Lunes_4": "Inglés",
        "Lunes_5": "Física",
        "Lunes_6": "Educación Física",
        "Martes_1": "Ciencias Naturales",
        "Martes_2": "Geografía e Historia",
        "Martes_3": "Recreo",
        "Martes_4": "Matemáticas",
        "Martes_5": "Tecnología",
        "Martes_6": "Música",
        "Miércoles_1": "Lengua Castellana",
        "Miércoles_2": "Inglés",
        "Miércoles_3": "Recreo",
        "Miércoles_4": "Plástica",
        "Miércoles_5": "Religión / Valores",
        "Miércoles_6": "Matemáticas",
        "Jueves_1": "Ciencias Sociales",
        "Jueves_2": "Tecnología",
        "Jueves_3": "Recreo",
        "Jueves_4": "Matemáticas",
        "Jueves_5": "Educación Física",
        "Jueves_6": "Música",
        "Viernes_1": "Lengua Castellana",
        "Viernes_2": "Inglés",
        "Viernes_3": "Recreo",
        "Viernes_4": "Ciencias Naturales",
        "Viernes_5": "Matemáticas",
        "Viernes_6": "Tecnología",
    }
}

A_renombrado = diccionario_calendario_A

json_calendario_a = "Calendario de la clase A.json"


def create_json():
    try:
        with open(json_calendario_a, "w") as json_A_renombrado:
            json.dump(A_renombrado, json_A_renombrado)
        create_json()
        with open(json_calendario_a, "r") as json_A_renombrado:
            print(json_A_renombrado.read())
    except Exception as e:
        print(f"Se ha producido un error: {e}")


# ----------------------------------------------------

# Calendario clase B .

diccionario_calendario_B: dict = {
    "ESO_B": {
        "Lunes_1": "Lengua Castellana",
        "Lunes_2": "Matemáticas",
        "Lunes_3": "Recreo",
        "Lunes_4": "Biología",
        "Lunes_5": "Educación Física",
        "Lunes_6": "Música",
        "Martes_1": "Física",
        "Martes_2": "Química",
        "Martes_3": "Recreo",
        "Martes_4": "Geografía e Historia",
        "Martes_5": "Tecnología",
        "Martes_6": "Inglés",
        "Miércoles_1": "Matemáticas",
        "Miércoles_2": "Lengua Castellana",
        "Miércoles_3": "Recreo",
        "Miércoles_4": "Plástica",
        "Miércoles_5": "Religión / Valores",
        "Miércoles_6": "Ciencias Naturales",
        "Jueves_1": "Inglés",
        "Jueves_2": "Educación Física",
        "Jueves_3": "Recreo",
        "Jueves_4": "Matemáticas",
        "Jueves_5": "Tecnología",
        "Jueves_6": "Música",
        "Viernes_1": "Ciencias Sociales",
        "Viernes_2": "Biología",
        "Viernes_3": "Recreo",
        "Viernes_4": "Lengua Castellana",
        "Viernes_5": "Matemáticas",
        "Viernes_6": "Física",
    }
}

B_renombrado = diccionario_calendario_B

json_calendario_b = "Calendario de la clase B.json"


def create_json():
    try:
        with open(json_calendario_b, "w") as json_B_renombrado:
            json.dump(B_renombrado, json_B_renombrado)
        create_json()
        with open(json_calendario_b, "r") as json_B_renombrado:
            print(json_B_renombrado.read())
    except Exception as e:
        print(f"Se ha producido un error: {e}")


# ----------------------------------------------------

# Calendario clase C .

diccionario_calendario_C: dict = {
    "ESO_C": {
        "Lunes_1": "Matemáticas",
        "Lunes_2": "Ciencias Naturales",
        "Lunes_3": "Recreo",
        "Lunes_4": "Lengua Castellana",
        "Lunes_5": "Inglés",
        "Lunes_6": "Educación Física",
        "Martes_1": "Tecnología",
        "Martes_2": "Geografía e Historia",
        "Martes_3": "Recreo",
        "Martes_4": "Matemáticas",
        "Martes_5": "Música",
        "Martes_6": "Religión / Valores",
        "Miércoles_1": "Lengua Castellana",
        "Miércoles_2": "Inglés",
        "Miércoles_3": "Recreo",
        "Miércoles_4": "Plástica",
        "Miércoles_5": "Ciencias Sociales",
        "Miércoles_6": "Educación Física",
        "Jueves_1": "Matemáticas",
        "Jueves_2": "Física",
        "Jueves_3": "Recreo",
        "Jueves_4": "Biología",
        "Jueves_5": "Tecnología",
        "Jueves_6": "Música",
        "Viernes_1": "Lengua Castellana",
        "Viernes_2": "Matemáticas",
        "Viernes_3": "Recreo",
        "Viernes_4": "Inglés",
        "Viernes_5": "Educación Física",
        "Viernes_6": "Ciencias Naturales",
    }
}

C_renombrado = diccionario_calendario_C

json_calendario_c = "Calendario de la clase C.json"


def create_json():
    try:
        with open(json_calendario_c, "w") as json_C_renombrado:
            json.dump(C_renombrado, json_C_renombrado)
        create_json()
        with open(json_calendario_c, "r") as json_C_renombrado:
            print(json_C_renombrado.read())
    except Exception as e:
        print(f"Se ha producido un error: {e}")


# ----------------------------------------------------

# Calendario clase D .

diccionario_calendario_D: dict = {
    "ESO_D": {
        "Lunes_1": "Lengua Castellana",
        "Lunes_2": "Matemáticas",
        "Lunes_3": "Recreo",
        "Lunes_4": "Geografía e Historia",
        "Lunes_5": "Educación Física",
        "Lunes_6": "Música",
        "Martes_1": "Física",
        "Martes_2": "Tecnología",
        "Martes_3": "Recreo",
        "Martes_4": "Matemáticas",
        "Martes_5": "Lengua Castellana",
        "Martes_6": "Inglés",
        "Miércoles_1": "Ciencias Naturales",
        "Miércoles_2": "Religión / Valores",
        "Miércoles_3": "Recreo",
        "Miércoles_4": "Plástica",
        "Miércoles_5": "Matemáticas",
        "Miércoles_6": "Educación Física",
        "Jueves_1": "Inglés",
        "Jueves_2": "Lengua Castellana",
        "Jueves_3": "Recreo",
        "Jueves_4": "Tecnología",
        "Jueves_5": "Geografía e Historia",
        "Jueves_6": "Música",
        "Viernes_1": "Matemáticas",
        "Viernes_2": "Biología",
        "Viernes_3": "Recreo",
        "Viernes_4": "Ciencias Sociales",
        "Viernes_5": "Inglés",
        "Viernes_6": "Física",
    }
}

D_renombrado = diccionario_calendario_D

json_calendario_d = "Calendario de la clase D.json"


def create_json():
    try:
        with open(json_calendario_d, "w") as json_D_renombrado:
            json.dump(D_renombrado, json_D_renombrado)
        create_json()
        with open(json_calendario_d, "r") as json_D_renombrado:
            print(json_D_renombrado.read())
    except Exception as e:
        print(f"Se ha producido un error: {e}")


# ----------------------------------------------------

# Preguntas sobre el rol del usuario.


def seleccionar_rol():

    alumno_ren1 = Alumno()
    profesor_ren2 = Profesor()
    director_ren3 = Director()
    jefe_estudios_ren4 = Jefe_de_estudios()
    admin_ren5 = Admin()

    # ----------------------------------------------------

    while True:

        opcions_ren1 = input(
            "Antes de nada digame que rol eres, sin mentir:\n"
            "1) Alumno\n"
            "2) Profesor\n"
            "3) Director\n"
            "4) Jefe de estudios\n"
            "5) Admin\n"
        )

        match opcions_ren1:
            case 1:
                alumno_ren1.jerarquia()
                break
            case 2:
                profesor_ren2.jerarquia()
                break
            case 3:
                director_ren3.jerarquia()
                break
            case 4:
                jefe_estudios_ren4.jerarquia()
                break
            case 5:
                admin_ren5.jerarquia()
                break
            case _:
                print("Opcion invalida, escoga una opcion valida porfavor.")

    # Llama a la funcion.

    seleccionar_rol()


# ----------------------------------------------------

# Clase padre.


class Jerarquia:
    def __init__(self, name_ren1: str):
        self.name = name_ren1


# ----------------------------------------------------

# Funciones para los alumnos.


class Alumno(Jerarquia):

    # ----------------------------------------------------

    # Funcion para apagar el equipo en verano.

    # Esto lo vi por chatgpt para arreglar unas cositas que no sabia.

    def es_verano_ren1():
        hoy_ren1 = datetime.now()
        inicio_verano_ren1 = datetime.date(hoy_ren1.year, 6, 21)
        fin_del_verano_ren1 = datetime.date(hoy_ren1.year, 9, 22)
        if inicio_verano_ren1 == hoy_ren1 and fin_del_verano_ren1 == hoy_ren1:
            print("La aplicacion no funciona en verano.")
            return

    # Llama a la funcion.

    es_verano_ren1()

    # ----------------------------------------------------

    def inicio_sesion_alumno(
        nombre_usuario: str, numero_contrasena: int, curso_usuario: str
    ):

        while True:

            try:
                nombre_usuario = str(input("Cree su nombre de usuario: "))
                if re.findall(r"^[a-z]+[A-Z]+\s+\D+{4,10}*$"):
                    diccionario_alumnos_ren1["name"] = (
                        nombre_usuario  # Esto estaba regular porque no guardaba la clave solo el valor.
                    )
                    diccionario_mensajes_alumnos_ren2["name"] = nombre_usuario
                    # ----------------------------------------------------
                    # Esto lo vi por chatgpt pero lo entendi todo.
                    diccionario_calificaciones["name"] = {
                        "Primera evaluacion": [None],
                        "Segunda evaluacion": [None],
                        "Tercera evaluacion": [None],
                        "Evaluacion final": [None],
                    }
                    # ----------------------------------------------------
                    diccionario_certificado["name"] = {
                        "Certificado asistencias": [None],
                        "Certificado notas": [None],
                        "Certificado matricula": [None],
                    }
                    # ----------------------------------------------------
                    diccionario_materiales["name"] = {
                        "Lengua Castellna": [None],
                        "Lingua Gallega": [None],
                        "Matematicas": [None],
                        "Geografia": [None],
                        "Plastica": [None],
                        "Religion": [None],
                        "Valores": [None],
                        "Proyecto Competencial": [None],
                        "Informatica": [None],
                        "Musica": [None],
                        "Educacion fisica": [None],
                        "Ingles": [None],
                        "Frances": [None],
                        "Fisica y quimica": [None],
                        "Biologia": [None],
                    }
                else:
                    print(f"El usuario: {nombre_usuario}, no es valido.")
                # ----------------------------------------------------
                curso_usuario = str(
                    input(
                        "Increse su curso (Ejemplo: eso_a, eso_b, eso_c, eso_d, bach_a, bach_b , bach_c , bach_d): "
                    )
                ).lower()
                if curso_usuario == eso_a_renombrado:
                    diccionario_tareas_eso_a["curso"] = curso_usuario
                    diccionario_alumnos_ren1["curso"] = (
                        curso_usuario  # Esto estaba regular porque no guardaba la clave solo el valor.
                    )
                if curso_usuario == eso_b_renombrado:
                    diccionario_tareas_eso_b["curso"] = curso_usuario
                    diccionario_alumnos_ren1["curso"] = curso_usuario
                if curso_usuario == eso_c_renombrado:
                    diccionario_tareas_eso_c["curso"] = curso_usuario
                    diccionario_alumnos_ren1["curso"] = curso_usuario
                if curso_usuario == eso_d_renombrado:
                    diccionario_tareas_eso_d["curso"] = curso_usuario
                    diccionario_alumnos_ren1["curso"] = curso_usuario
                if curso_usuario == bach_a_renombrado:
                    diccionario_tareas_bach_a["curso"] = curso_usuario
                    diccionario_alumnos_ren1["curso"] = curso_usuario
                if curso_usuario == bach_b_renombrado:
                    diccionario_tareas_bach_b["curso"] = curso_usuario
                    diccionario_alumnos_ren1["curso"] = curso_usuario
                if curso_usuario == bach_c_renombrado:
                    diccionario_tareas_bach_c["curso"] = curso_usuario
                    diccionario_alumnos_ren1["curso"] = curso_usuario
                if curso_usuario == bach_d_renombrado:
                    diccionario_tareas_bach_d["curso"] = curso_usuario
                    diccionario_alumnos_ren1["curso"] = curso_usuario
                numero_contrasena = int(input("Cree su contraseña: "))
                if re.findall(r"[:alnum:]+(\S+\d+\W+[0-9])+(\S+\d+\W+{8,})"):
                    diccionario_alumnos_ren1["contraseña"] = (
                        numero_contrasena  # Esto estaba regular porque no guardaba la clave solo el valor.
                    )
                    print(
                        f"La contraseña:  {numero_contrasena}, a sido guardado correctamente."
                    )
                else:
                    print(f"La contraseña: {numero_contrasena}, no es valida.")
                time.sleep(1)
                print(f"Bienvenido: {nombre_usuario}.")
                break
            except Exception as e:
                print(f"Se ha producido un error: {e}")

    # Llama a la funcion.

    inicio_sesion_alumno()

    def opciones_alumno():

        while True:

            opcions_ren2 = input(
                "Escoja una de estas opciones:\n"
                "1) Incresar.\n"
                "2) Ver tiempo que falta para que se acabe el cole.\n"
                "3) Enviar mensaje a profesor.\n"
                "4) Entregar tarea.\n"
                "5) Ver tareas asignadas.\n"
                "6) Ver calificaciones.\n"
                "7) Descargar materiales.\n"
                "8) Participar en encuestas.\n"
                "9) Ver horario.\n"
                "10) Ver eventos escolares.\n"
                "11) Actualizar datos personales.\n"
                "12) Solicitar certificado.\n"
                "13) Ver avisos importantes.\n"
                "14) Contactar administración.\n"
                "15) Salir.\n"
            )

            match opcions_ren2:
                case 1:
                    nombre_usuario_1 = input("Introduzca su nombre de usuario: ")
                    if diccionario_alumnos_ren1["name"] == nombre_usuario_1:
                        print(f"Bienvenido: {nombre_usuario_1}.")
                    else:
                        print(f"El nombre: {nombre_usuario_1}, no existe.")
                    numero_contrasena_1 = input("Introduzca su contraseña de usuario: ")
                    if diccionario_alumnos_ren1["contraseña"] == numero_contrasena_1:
                        print("Tu contraseña es correcta.")
                    else:
                        print(f"La contraseña: {numero_contrasena_1}, no existe.")
                    curso_usuario_1 = input("Increse su curso: ")
                    if diccionario_alumnos_ren1["curso"] == curso_usuario_1:
                        print("Tu curso es correcto.")
                    else:
                        print("Tu curso es incorrecto.")
                case 2:
                    dias_lectivos_ren1 = 178
                    dias_restantes_ren1 = dias_lectivos_ren1 - datetime.now()
                    if dias_restantes_ren1 > 0:
                        print(
                            f"El tiempo restante del curso es: {dias_restantes_ren1} -_- "
                        )
                    if dias_restantes_ren1 <= 0:
                        print("El año escolar ya remato disfruta del verano :) ")
                case 3:
                    nombre_usuario_ren1 = input("Cual es su nombre: ")
                    if diccionario_alumnos_ren1["name"] == nombre_usuario_ren1:
                        print("Nombre verificado.")
                    else:
                        print("Nombre incorrecto.")
                    nombre_profe_ren1 = input("Cual es el profe a asignar: ")
                    if (
                        diccionario_profesores_ren3["name"] == nombre_profe_ren1
                    ):  # Esto aun no esta bien implementado porque faltan los nombre de los admins que se acregaran porteriormente.
                        print("Nombre verificado.")
                    else:
                        print("Nombre no encontrado, revise el nombre escrito.")
                    mensaje_alumno_ren1 = input(
                        "Escriba el mensaje a enviar al profesor: "
                    )
                    diccionario_mensajes_profesores_ren4[nombre_profe_ren1] = (
                        f"{nombre_usuario_ren1}: {mensaje_alumno_ren1}."
                    )
                    print("Enviando mensaje...")
                    time.sleep(1)
                    print(f"Mensaje enviado al profesor: {nombre_profe_ren1}.")
                case 4:
                    nombre_usuario_ren2 = input("Cual es su nombre: ")
                    if diccionario_alumnos_ren1["name"] == nombre_usuario_ren2:
                        print("Nombre verificado.")
                    else:
                        print("Nombre incorrecto.")
                    nombre_profe_ren2 = input("Cual es el profe a asignar: ")
                    if (
                        diccionario_profesores_ren3["name"] == nombre_profe_ren2
                    ):  # Esto aun no esta bien implementado porque faltan los nombre de los admins que se acregaran porteriormente.
                        print("Nombre verificado.")
                    else:
                        print("Nombre no encontrado, revise el nombre escrito.")
                    trabajo_alumno_ren1 = input("Envia el trabajo correspondiente: ")
                    diccionario_trabajo[nombre_profe_ren2] = (
                        f"{nombre_usuario_ren2}: {trabajo_alumno_ren1}."
                    )
                    print("Enviando trabajo...")
                    time.sleep(1)
                    print(f"Trabajo enviado al profesor: {nombre_profe_ren2}.")
                case 5:
                    curso_usuario_1 = input(
                        "Increse su curso (Ejemplo: eso_a, eso_b, eso_c, eso_d, bach_a, bach_b , bach_c , bach_d): "
                    ).lower()
                    if diccionario_alumnos_ren1["curso"] == curso_usuario_1:
                        print("Curso verificado.")
                    else:
                        print(f"El curso: {curso_usuario_1} , no existe.")
                    if curso_usuario_1 == eso_a_renombrado:
                        print(f"Tus tareas son estas: {eso_a_renombrado}.")
                    else:
                        print("No hay tareas disponibles.")
                    if curso_usuario_1 == eso_b_renombrado:
                        print(f"Tus tareas son estas: {eso_b_renombrado}.")
                    else:
                        print("No hay tareas disponibles.")
                    if curso_usuario_1 == eso_c_renombrado:
                        print(f"Tus tareas son estas: {eso_c_renombrado}.")
                    else:
                        print("No hay tareas disponibles.")
                    if curso_usuario_1 == eso_d_renombrado:
                        print(f"Tus tareas son estas: {eso_d_renombrado}.")
                    else:
                        print("No hay tareas disponibles.")
                    if curso_usuario_1 == bach_a_renombrado:
                        print(f"Tus tareas son estas: {bach_a_renombrado}.")
                    else:
                        print("No hay tareas disponibles.")
                    if curso_usuario_1 == bach_b_renombrado:
                        print(f"Tus tareas son estas: {bach_b_renombrado}.")
                    else:
                        print("No hay tareas disponibles.")
                    if curso_usuario_1 == bach_c_renombrado:
                        print(f"Tus tareas son estas: {bach_c_renombrado}.")
                    else:
                        print("No hay tareas disponibles.")
                    if curso_usuario_1 == bach_d_renombrado:
                        print(f"Tus tareas son estas: {bach_d_renombrado}.")
                    else:
                        print("No hay tareas disponibles.")
                case 6:
                    if len(diccionario_calificaciones) >= 1:
                        print(f"Tus calificaciones son: {calificaciones_renombrado}")
                    else:
                        print("No hay calificaciones disponibles.")
                case 7:
                    nombre_usuario_1 = input("Introduzca su nombre de usuario: ")
                    if diccionario_alumnos_ren1["name"] == nombre_usuario_1:
                        print(f"Bienvenido: {nombre_usuario_1}.")
                    else:
                        print(f"El nombre: {nombre_usuario_1}, no existe.")
                    numero_contrasena_1 = input("Introduzca su contraseña de usuario: ")
                    if diccionario_alumnos_ren1["contraseña"] == numero_contrasena_1:
                        print("Tu contraseña es correcta.")
                    else:
                        print(f"La contraseña: {numero_contrasena_1}, no existe.")
                    if len(diccionario_materiales) >= 1:
                        print(
                            f"Los materiales disponibles son: {materiales_renombrado}."
                        )
                    else:
                        print("No hay materiales disponibles.")
                case 8:
                    if len(diccionario_encuestas) >= 1:
                        print(f"Las encuestas disponibles son: {encuestas_renombrado}.")
                    else:
                        print("No hay encuestas disponibles.")
                case 9:
                    clase_ren1 = input(
                        "Cual es tu clase (Ejemplo: A, B, C, D): "
                    ).upper()  # Esto lo vi por chatgpt para que quedase mas bonito.
                    if diccionario_alumnos_ren1["curso"] == clase_ren1:
                        print("Tu curso es correcto.")
                    else:
                        print(f"El curso: {clase_ren1}, no existe.")
                    if clase_ren1 == A_renombrado:
                        print(f"Tu calendario es: {A_renombrado}.")
                    elif clase_ren1 == B_renombrado:
                        print(f"Tu calendario es: {B_renombrado}.")
                    elif clase_ren1 == C_renombrado:
                        print(f"Tu calendario es: {C_renombrado}.")
                    elif clase_ren1 == D_renombrado:
                        print(f"Tu calendario es: {D_renombrado}.")
                    else:
                        print(f"El curso: {clase_ren1}, no existe")
                case 10:
                    if len(diccionario_eventos) >= 1:
                        print(f"Los eventos disponibles son: {eventos_renombrado}.")
                    else:
                        print("No hay eventos disponibles.")
                case 11:
                    usuario_ren1 = input("Increse su nombre de usuario: ")
                    if diccionario_alumnos_ren1["name"] == usuario_ren1:
                        del dict[usuario_ren1]
                        print("Nombre eliminado.")
                    else:
                        print("Nombre no encontrado, revise el nombre escrito.")
                    nuevo_nombre_usuario = input(
                        "Introduzca su nuevo nombre de usuario: "
                    )
                    re.findall(r"^[a-z]+[A-Z]+\s+\D+{4,10}*$")
                    diccionario_alumnos_ren1["name"] = nuevo_nombre_usuario
                    print(
                        f"El nuevo nombre: {nuevo_nombre_usuario}, a sido guardado correctamente."
                    )
                    contrasena_ren1 = input("Increse su contraseña: ")
                    if diccionario_alumnos_ren1["contraseña"] == contrasena_ren1:
                        del dict[contrasena_ren1]
                        print("Contraseña eliminada.")
                    else:
                        print("Contraseña no encontrado, revise la contraseña escrita.")
                    nueva_contrasena = input("Introduzca su nueva contraseña: ")
                    if nueva_contrasena is len() == 8:
                        diccionario_alumnos_ren1["contraseña"] = nueva_contrasena
                        print(
                            f"La contraseña: {nueva_contrasena}, a sido guardado correctamente."
                        )
                case 12:
                    nombre_usuario_1 = input("Introduzca su nombre de usuario: ")
                    if diccionario_alumnos_ren1["name"] == nombre_usuario_1:
                        print(f"Bienvenido: {nombre_usuario_1}.")
                    else:
                        print(f"El nombre: {nombre_usuario_1}, no existe.")
                    numero_contrasena_1 = input("Introduzca su contraseña de usuario: ")
                    if diccionario_alumnos_ren1["contraseña"] == numero_contrasena_1:
                        print("Tu contraseña es correcta.")
                    else:
                        print(f"La contraseña: {numero_contrasena_1}, no existe.")
                    if diccionario_certificado:
                        print(
                            f"Tus certificados disponibles son estos siguientes: {certificado_renombrado}."
                        )
                    else:
                        print("No hay certificados disponibles.")
                case 13:
                    if len(diccionario_avisos) >= 1:
                        print(f"Los avisos disponibles son: {avisos_renombrado}.")
                    else:
                        print("No hay avisos disponibles.")
                case 14:
                    nombre_usuario_ren3 = input("Cual es su nombre: ")
                    if diccionario_alumnos_ren1["name"] == nombre_usuario_ren3:
                        print("Nombre verificado.")
                    else:
                        print("Nombre incorrecto.")
                    nombre_admin_ren1 = input("Cual es el admin a asignar: ")
                    if (
                        diccionario_admin_ren5["name"] == nombre_admin_ren1
                    ):  # Esto aun no esta bien implementado porque faltan los nombre de los admins que se acregaran porteriormente.
                        print("Nombre verificado.")
                    else:
                        print("Nombre no encontrado, revise el nombre escrito.")
                    mensaje_alumno_ren2 = input(
                        "Escriba el mensaje a enviar al admin: "
                    )
                    diccionario_mensajes_admin_ren6[nombre_admin_ren1] = (
                        f"{nombre_usuario_ren3}: {mensaje_alumno_ren2}."
                    )
                    print("Enviando mensaje...")
                    time.sleep(1)
                    print(f"Mensaje enviado al admin: {nombre_profe_ren2}.")
                case 15:
                    print("Saliendo del programa...")
                    time.sleep(2)
                    print("Salida del programa exictosa.")
                    break
                case _:
                    print("Opcion invalida, escoga una opcion valida porfavor.")

    # Llama a la funcion.

    opciones_alumno()


# ----------------------------------------------------

# ✅ FASE 2.

# Funciones para los profes.


class Profesor(Jerarquia):

    # ----------------------------------------------------

    def inicio_sesion_profesor(nombre_usuario: str, numero_contrasena: int):

        while True:

            try:
                nombre_usuario = str(input("Cree su nombre de usuario: "))
                re.findall(r"^[a-z]+[A-Z]+\s+\D+{4,10}*$")
                diccionario_profesores_ren3["name"] = (
                    nombre_usuario  # Esto estaba regular porque no guardaba la clave solo el valor.
                )
                diccionario_mensajes_profesores_ren4["name"] = nombre_usuario
                diccionario_compañeros_ren10["name"] = nombre_usuario
                diccionario_compañeros_mensajes_ren11["name"] = nombre_usuario
                numero_contrasena = int(input("Cree su contraseña: "))
                if numero_contrasena is len() == 8:
                    diccionario_profesores_ren3["contraseña"] = (
                        numero_contrasena  # Esto estaba regular porque no guardaba la clave solo el valor.
                    )
                    print(
                        f"La contraseña: {numero_contrasena}, a sido guardado correctamente."
                    )
                else:
                    print(
                        f"La contraseña: {numero_contrasena}, tiene que tener 8 caracteres."
                    )
                asignatura_usuario = str(input("Introduzca su asignatura: "))
                diccionario_asignatura["asignatura"] = (
                    asignatura_usuario  # Añadir ya las asignaturas predeterminadas para no tener ningun problema.
                )
                time.sleep(1)
                print(f"Bienvenido: {nombre_usuario}.")
                break
            except Exception as e:
                print(f"Se ha producido un error: {e}")

    # Llama a la funcion.

    inicio_sesion_profesor()

    # ----------------------------------------------------

    def opciones_profesor():

        while True:

            opcions_ren3 = input(
                "Escoja una de estas opciones:\n"
                "1) Incresar.\n"  # Necesita diccionario , no X
                "2) Crear tarea.\n"  # Necesita diccionario , si 0
                "3) Corregir tarea.\n"  # Necesita diccionario , si 0
                "4) Enviar mensaje a curso.\n"  # Necesita diccionario , si 0
                "5) Enviar mensaje a alumnos.\n"  # Necesita diccionario , si 0
                "6) Crear certificados.\n"  # Necesita diccionario , si 0
                "7) Subir material.\n"  # Necesita diccionario , si 0
                "8) Ver lista de alumnos.\n"  # Necesita diccionario , si 0
                "9) Poner calificación.\n"  # Necesita diccionario , si 0
                "10) Crear examen.\n"  # Necesita diccionario , si 0
                "11) Ver estadísticas.\n"  # Necesita diccionario , si 0
                "12) Enviar aviso a todos los cursos.\n"  # Necesita diccionario , si 0
                "13) Consultar asistencia histórica.\n"  # Necesita diccionario , si 0
                "14) Programar reuniones.\n"  # Necesita diccionario , si 0
                "15) Modificar notas.\n"  # Necesita diccionario , si 0
                "16) Marcar asistencia.\n"  # Necesita diccionario , si 0
                "17) Ver calendario escolar.\n"  # Necesita diccionario , si 0
                "18) Enviar mensaje a admin.\n"  # Necesita diccionario , si 0
                "19) Enviar mensaje a compañero.\n"  # Necesita diccionario , si 0
                "20) Apuntar conflictos.\n"  # Necesita diccionario , si 0
                "21) Progrmar actividad extraescolar.\n"  # Necesita diccionario , si 0
                "22) Salir.\n"  # Necesita diccionario , no X
            )

            match opcions_ren3:
                case 1:
                    nombre_usuario_1 = input("Introduzca su nombre de usuario: ")
                    if diccionario_profesores_ren3["name"] == nombre_usuario_1:
                        print(f"Bienvenido: {nombre_usuario_1}.")
                    else:
                        print(f"El nombre: {nombre_usuario_1}, no existe.")
                    numero_contrasena_1 = input("Introduzca su contraseña de usuario: ")
                    if diccionario_profesores_ren3["contraseña"] == numero_contrasena_1:
                        print("Tu contraseña es correcta.")
                    else:
                        print(f"La contraseña: {numero_contrasena_1}, no existe.")
                    nombre_asignatura_1 = input("Introduzca su asignatura: ")
                    if diccionario_asignatura["asignatura"] == nombre_asignatura_1:
                        print("Tu asigantura es correcta.")
                    else:
                        print(f"La asignatura: {nombre_asignatura_1}, no existe.")
                case 2:
                    # ----------------------------------------------------

                    # Esta function se implementara en un futuro cercano.

                    print(
                        "⚠️ Lo sentimos mucho 🙏 Esta función aún no está implementada en el programa. Estará disponible en un futuro cercano, ¡gracias por tu paciencia! ✨"
                    )
                    time.sleep(1)
                    print(
                        "⚠️ We’re sorry 🙏 This feature is not yet implemented in the system. It will be available soon, thank you for your patience! ✨"
                    )
                    time.sleep(1)
                    print(
                        "⚠️ 申し訳ありません 🙏 この機能はまだ実装されていません。近いうちに利用できるようになりますので、しばらくお待ちください！✨"
                    )
                    # ----------------------------------------------------
                case 3:
                    # ----------------------------------------------------

                    # Esta function se implementara en un futuro cercano.

                    print(
                        "⚠️ Lo sentimos mucho 🙏 Esta función aún no está implementada en el programa. Estará disponible en un futuro cercano, ¡gracias por tu paciencia! ✨"
                    )
                    time.sleep(1)
                    print(
                        "⚠️ We’re sorry 🙏 This feature is not yet implemented in the system. It will be available soon, thank you for your patience! ✨"
                    )
                    time.sleep(1)
                    print(
                        "⚠️ 申し訳ありません 🙏 この機能はまだ実装されていません。近いうちに利用できるようになりますので、しばらくお待ちください！✨"
                    )
                    # ----------------------------------------------------
                case 4:
                    # ----------------------------------------------------

                    # Esta function se implementara en un futuro cercano.

                    print(
                        "⚠️ Lo sentimos mucho 🙏 Esta función aún no está implementada en el programa. Estará disponible en un futuro cercano, ¡gracias por tu paciencia! ✨"
                    )
                    time.sleep(1)
                    print(
                        "⚠️ We’re sorry 🙏 This feature is not yet implemented in the system. It will be available soon, thank you for your patience! ✨"
                    )
                    time.sleep(1)
                    print(
                        "⚠️ 申し訳ありません 🙏 この機能はまだ実装されていません。近いうちに利用できるようになりますので、しばらくお待ちください！✨"
                    )
                    # ----------------------------------------------------
                case 5:
                    nombre_usuario_ren1 = input("Cual es su nombre: ")
                    if diccionario_profesores_ren3["name"] == nombre_usuario_ren1:
                        print("Nombre verificado.")
                    else:
                        print("Nombre incorrecto.")
                    nombre_alumno_ren1 = input("Cual es el alumno a asignar: ")
                    if (
                        diccionario_alumnos_ren1["name"] == nombre_alumno_ren1
                    ):  # Esto aun no esta bien implementado porque faltan los nombre de los admins que se acregaran porteriormente.
                        print("Nombre verificado.")
                    else:
                        print("Nombre no encontrado, revise el nombre escrito.")
                    mensaje_profesor_ren1 = input(
                        "Escriba el mensaje a enviar al alumno: "
                    )
                    diccionario_mensajes_alumnos_ren2[nombre_alumno_ren1] = (
                        f"{nombre_usuario_ren1}: {mensaje_profesor_ren1}."
                    )
                    print("Enviando mensaje...")
                    time.sleep(1)
                    print(f"Mensaje enviado al alumno: {nombre_alumno_ren1}.")
                case 6:
                    # ----------------------------------------------------

                    # Esta function se implementara en un futuro cercano.

                    print(
                        "⚠️ Lo sentimos mucho 🙏 Esta función aún no está implementada en el programa. Estará disponible en un futuro cercano, ¡gracias por tu paciencia! ✨"
                    )
                    time.sleep(1)
                    print(
                        "⚠️ We’re sorry 🙏 This feature is not yet implemented in the system. It will be available soon, thank you for your patience! ✨"
                    )
                    time.sleep(1)
                    print(
                        "⚠️ 申し訳ありません 🙏 この機能はまだ実装されていません。近いうちに利用できるようになりますので、しばらくお待ちください！✨"
                    )
                    # ----------------------------------------------------
                case 7:
                    # ----------------------------------------------------

                    # Esta function se implementara en un futuro cercano.

                    print(
                        "⚠️ Lo sentimos mucho 🙏 Esta función aún no está implementada en el programa. Estará disponible en un futuro cercano, ¡gracias por tu paciencia! ✨"
                    )
                    time.sleep(1)
                    print(
                        "⚠️ We’re sorry 🙏 This feature is not yet implemented in the system. It will be available soon, thank you for your patience! ✨"
                    )
                    time.sleep(1)
                    print(
                        "⚠️ 申し訳ありません 🙏 この機能はまだ実装されていません。近いうちに利用できるようになりますので、しばらくお待ちください！✨"
                    )
                    # ----------------------------------------------------
                case 8:
                    # ----------------------------------------------------

                    # Esta function se implementara en un futuro cercano.

                    print(
                        "⚠️ Lo sentimos mucho 🙏 Esta función aún no está implementada en el programa. Estará disponible en un futuro cercano, ¡gracias por tu paciencia! ✨"
                    )
                    time.sleep(1)
                    print(
                        "⚠️ We’re sorry 🙏 This feature is not yet implemented in the system. It will be available soon, thank you for your patience! ✨"
                    )
                    time.sleep(1)
                    print(
                        "⚠️ 申し訳ありません 🙏 この機能はまだ実装されていません。近いうちに利用できるようになりますので、しばらくお待ちください！✨"
                    )
                    # ----------------------------------------------------
                case 9:
                    # ----------------------------------------------------

                    # Esta function se implementara en un futuro cercano.

                    print(
                        "⚠️ Lo sentimos mucho 🙏 Esta función aún no está implementada en el programa. Estará disponible en un futuro cercano, ¡gracias por tu paciencia! ✨"
                    )
                    time.sleep(1)
                    print(
                        "⚠️ We’re sorry 🙏 This feature is not yet implemented in the system. It will be available soon, thank you for your patience! ✨"
                    )
                    time.sleep(1)
                    print(
                        "⚠️ 申し訳ありません 🙏 この機能はまだ実装されていません。近いうちに利用できるようになりますので、しばらくお待ちください！✨"
                    )
                    # ----------------------------------------------------
                case 10:
                    # ----------------------------------------------------

                    # Esta function se implementara en un futuro cercano.

                    print(
                        "⚠️ Lo sentimos mucho 🙏 Esta función aún no está implementada en el programa. Estará disponible en un futuro cercano, ¡gracias por tu paciencia! ✨"
                    )
                    time.sleep(1)
                    print(
                        "⚠️ We’re sorry 🙏 This feature is not yet implemented in the system. It will be available soon, thank you for your patience! ✨"
                    )
                    time.sleep(1)
                    print(
                        "⚠️ 申し訳ありません 🙏 この機能はまだ実装されていません。近いうちに利用できるようになりますので、しばらくお待ちください！✨"
                    )
                    # ----------------------------------------------------
                case 11:
                    # ----------------------------------------------------

                    # Esta function se implementara en un futuro cercano.

                    print(
                        "⚠️ Lo sentimos mucho 🙏 Esta función aún no está implementada en el programa. Estará disponible en un futuro cercano, ¡gracias por tu paciencia! ✨"
                    )
                    time.sleep(1)
                    print(
                        "⚠️ We’re sorry 🙏 This feature is not yet implemented in the system. It will be available soon, thank you for your patience! ✨"
                    )
                    time.sleep(1)
                    print(
                        "⚠️ 申し訳ありません 🙏 この機能はまだ実装されていません。近いうちに利用できるようになりますので、しばらくお待ちください！✨"
                    )
                    # ----------------------------------------------------
                case 12:
                    # ----------------------------------------------------

                    # Esta function se implementara en un futuro cercano.

                    print(
                        "⚠️ Lo sentimos mucho 🙏 Esta función aún no está implementada en el programa. Estará disponible en un futuro cercano, ¡gracias por tu paciencia! ✨"
                    )
                    time.sleep(1)
                    print(
                        "⚠️ We’re sorry 🙏 This feature is not yet implemented in the system. It will be available soon, thank you for your patience! ✨"
                    )
                    time.sleep(1)
                    print(
                        "⚠️ 申し訳ありません 🙏 この機能はまだ実装されていません。近いうちに利用できるようになりますので、しばらくお待ちください！✨"
                    )
                    # ----------------------------------------------------
                case 13:
                    # ----------------------------------------------------

                    # Esta function se implementara en un futuro cercano.

                    print(
                        "⚠️ Lo sentimos mucho 🙏 Esta función aún no está implementada en el programa. Estará disponible en un futuro cercano, ¡gracias por tu paciencia! ✨"
                    )
                    time.sleep(1)
                    print(
                        "⚠️ We’re sorry 🙏 This feature is not yet implemented in the system. It will be available soon, thank you for your patience! ✨"
                    )
                    time.sleep(1)
                    print(
                        "⚠️ 申し訳ありません 🙏 この機能はまだ実装されていません。近いうちに利用できるようになりますので、しばらくお待ちください！✨"
                    )
                    # ----------------------------------------------------
                case 14:
                    # ----------------------------------------------------

                    # Esta function se implementara en un futuro cercano.

                    print(
                        "⚠️ Lo sentimos mucho 🙏 Esta función aún no está implementada en el programa. Estará disponible en un futuro cercano, ¡gracias por tu paciencia! ✨"
                    )
                    time.sleep(1)
                    print(
                        "⚠️ We’re sorry 🙏 This feature is not yet implemented in the system. It will be available soon, thank you for your patience! ✨"
                    )
                    time.sleep(1)
                    print(
                        "⚠️ 申し訳ありません 🙏 この機能はまだ実装されていません。近いうちに利用できるようになりますので、しばらくお待ちください！✨"
                    )
                    # ----------------------------------------------------
                case 15:
                    # ----------------------------------------------------

                    # Esta function se implementara en un futuro cercano.

                    print(
                        "⚠️ Lo sentimos mucho 🙏 Esta función aún no está implementada en el programa. Estará disponible en un futuro cercano, ¡gracias por tu paciencia! ✨"
                    )
                    time.sleep(1)
                    print(
                        "⚠️ We’re sorry 🙏 This feature is not yet implemented in the system. It will be available soon, thank you for your patience! ✨"
                    )
                    time.sleep(1)
                    print(
                        "⚠️ 申し訳ありません 🙏 この機能はまだ実装されていません。近いうちに利用できるようになりますので、しばらくお待ちください！✨"
                    )
                    # ----------------------------------------------------
                case 16:
                    # ----------------------------------------------------

                    # Esta function se implementara en un futuro cercano.

                    print(
                        "⚠️ Lo sentimos mucho 🙏 Esta función aún no está implementada en el programa. Estará disponible en un futuro cercano, ¡gracias por tu paciencia! ✨"
                    )
                    time.sleep(1)
                    print(
                        "⚠️ We’re sorry 🙏 This feature is not yet implemented in the system. It will be available soon, thank you for your patience! ✨"
                    )
                    time.sleep(1)
                    print(
                        "⚠️ 申し訳ありません 🙏 この機能はまだ実装されていません。近いうちに利用できるようになりますので、しばらくお待ちください！✨"
                    )
                    # ----------------------------------------------------
                case 17:
                    # ----------------------------------------------------

                    # Esta function se implementara en un futuro cercano.

                    print(
                        "⚠️ Lo sentimos mucho 🙏 Esta función aún no está implementada en el programa. Estará disponible en un futuro cercano, ¡gracias por tu paciencia! ✨"
                    )
                    time.sleep(1)
                    print(
                        "⚠️ We’re sorry 🙏 This feature is not yet implemented in the system. It will be available soon, thank you for your patience! ✨"
                    )
                    time.sleep(1)
                    print(
                        "⚠️ 申し訳ありません 🙏 この機能はまだ実装されていません。近いうちに利用できるようになりますので、しばらくお待ちください！✨"
                    )
                    # ----------------------------------------------------
                case 18:
                    nombre_usuario_ren1 = input("Cual es su nombre: ")
                    if diccionario_profesores_ren3["name"] == nombre_usuario_ren1:
                        print("Nombre verificado.")
                    else:
                        print("Nombre incorrecto.")
                    nombre_admin_ren1 = input("Cual es el admin a asignar: ")
                    if (
                        diccionario_admin_ren5["name"] == nombre_admin_ren1
                    ):  # Esto aun no esta bien implementado porque faltan los nombre de los admins que se acregaran porteriormente.
                        print("Nombre verificado.")
                    else:
                        print("Nombre no encontrado, revise el nombre escrito.")
                    mensaje_profesor_ren1 = input(
                        "Escriba el mensaje a enviar al admin: "
                    )
                    diccionario_mensajes_admin_ren6[nombre_admin_ren1] = (
                        f"{nombre_usuario_ren1}: {mensaje_profesor_ren1}."
                    )
                    print("Enviando mensaje...")
                    time.sleep(1)
                    print(f"Mensaje enviado al admin: {nombre_admin_ren1}.")
                case 19:
                    nombre_usuario_ren1 = input("Cual es su nombre: ")
                    if diccionario_profesores_ren3["name"] == nombre_usuario_ren1:
                        print("Nombre verificado.")
                    else:
                        print("Nombre incorrecto.")
                    nombre_compañero_ren1 = input("Cual es el compañero a asignar: ")
                    if (
                        diccionario_compañeros_ren10["name"] == nombre_compañero_ren1
                    ):  # Esto aun no esta bien implementado porque faltan los nombre de los admins que se acregaran porteriormente.
                        print("Nombre verificado.")
                    else:
                        print("Nombre no encontrado, revise el nombre escrito.")
                    mensaje_profesor_ren1 = input(
                        "Escriba el mensaje a enviar al compañero: "
                    )
                    diccionario_compañeros_mensajes_ren11[nombre_compañero_ren1] = (
                        f"{nombre_usuario_ren1}: {mensaje_profesor_ren1}."
                    )
                    print("Enviando mensaje...")
                    time.sleep(1)
                    print(f"Mensaje enviado al compañero: {nombre_compañero_ren1}.")
                case 20:
                    # ----------------------------------------------------

                    # Esta function se implementara en un futuro cercano.

                    print(
                        "⚠️ Lo sentimos mucho 🙏 Esta función aún no está implementada en el programa. Estará disponible en un futuro cercano, ¡gracias por tu paciencia! ✨"
                    )
                    time.sleep(1)
                    print(
                        "⚠️ We’re sorry 🙏 This feature is not yet implemented in the system. It will be available soon, thank you for your patience! ✨"
                    )
                    time.sleep(1)
                    print(
                        "⚠️ 申し訳ありません 🙏 この機能はまだ実装されていません。近いうちに利用できるようになりますので、しばらくお待ちください！✨"
                    )
                    # ----------------------------------------------------
                case 21:
                    # ----------------------------------------------------

                    # Esta function se implementara en un futuro cercano.

                    print(
                        "⚠️ Lo sentimos mucho 🙏 Esta función aún no está implementada en el programa. Estará disponible en un futuro cercano, ¡gracias por tu paciencia! ✨"
                    )
                    time.sleep(1)
                    print(
                        "⚠️ We’re sorry 🙏 This feature is not yet implemented in the system. It will be available soon, thank you for your patience! ✨"
                    )
                    time.sleep(1)
                    print(
                        "⚠️ 申し訳ありません 🙏 この機能はまだ実装されていません。近いうちに利用できるようになりますので、しばらくお待ちください！✨"
                    )
                    # ----------------------------------------------------
                case 22:
                    print("Saliendo del programa...")
                    time.sleep(2)
                    print("Salida del programa exictosa.")
                    break
                case _:
                    print("Opcion invalida, escoga una opcion valida porfavor.")

    # Llama a la funcion.

    opciones_profesor()


# ----------------------------------------------------

# ✅ FASE 3.

# Funciones para el director.


class Director(Jerarquia):

    # ----------------------------------------------------

    def inicio_sesion_director(nombre_usuario: str, numero_contrasena: int):

        while True:

            try:
                nombre_usuario = str(input("Cree su nombre de usuario: "))
                re.findall(r"^[a-z]+[A-Z]+\s+\D+{4,10}*$")
                diccionario_director_ren7["name"] = (
                    nombre_usuario  # Esto estaba regular porque no guardaba la clave solo el valor.
                )
                diccionario_mensajes_director_ren8["name"] = nombre_usuario
                numero_contrasena = int(input("Cree su contraseña: "))
                if numero_contrasena is len() == 8:
                    diccionario_director_ren7["contraseña"] = (
                        numero_contrasena  # Esto estaba regular porque no guardaba la clave solo el valor.
                    )
                    print(
                        f"La contraseña: {numero_contrasena}, a sido guardado correctamente."
                    )
                else:
                    print(
                        f"La contraseña: {numero_contrasena}, tiene que tener 8 caracteres."
                    )
                time.sleep(1)
                print(f"Bienvenido: {nombre_usuario}.")
                break
            except Exception as e:
                print(f"Se ha producido un error: {e}")

    # Llama a la funcion.

    inicio_sesion_director()

    # ----------------------------------------------------

    def opciones_director():

        while True:

            opcions_ren4 = input(
                "Escoja una de estas opciones:\n"
                "1) Incresar.\n"  # Necesita diccionario , no X
                "2) Ver todos los cursos.\n"  # Necesita diccionario , si 0
                "3) Enviar mensaje global.\n"  # Necesita diccionario , si 0
                "4) Asignar profesores a cursos.\n"  # Necesita diccionario , si 0
                "5) Gestionar calendario escolar.\n"  # Necesita diccionario , si 0
                "6) Ver reportes académicos.\n"  # Necesita diccionario , si 0
                "7) Suspender alumno.\n"  # Necesita diccionario , si 0
                "8) Expulsar alumno.\n"  # Necesita diccionario , si 0
                "9) Ver incidencias disciplinarias.\n"  # Necesita diccionario , si 0
                "10) Subir circulares oficiales.\n"  # Necesita diccionario , si 0
                "11) Gestionar infraestructura.\n"  # Necesita diccionario , si 0
                "12) Programar asambleas.\n"  # Necesita diccionario , si 0
                "13) Modificar datos.\n"  # Necesita diccionario , no X
                "14) Enviar mensajes.\n"  # Necesita diccionario , si 0
                "15) Proponer cambio horario.\n"  # Necesita diccionario , si 0
                "16) Salir.\n"  # Necesita diccionario , no X
            )

            match opcions_ren4:
                case 1:
                    # ----------------------------------------------------

                    # Esta function se implementara en un futuro cercano.

                    print(
                        "⚠️ Lo sentimos mucho 🙏 Esta función aún no está implementada en el programa. Estará disponible en un futuro cercano, ¡gracias por tu paciencia! ✨"
                    )
                    time.sleep(1)
                    print(
                        "⚠️ We’re sorry 🙏 This feature is not yet implemented in the system. It will be available soon, thank you for your patience! ✨"
                    )
                    time.sleep(1)
                    print(
                        "⚠️ 申し訳ありません 🙏 この機能はまだ実装されていません。近いうちに利用できるようになりますので、しばらくお待ちください！✨"
                    )
                    # ----------------------------------------------------
                case 2:
                    # ----------------------------------------------------

                    # Esta function se implementara en un futuro cercano.

                    print(
                        "⚠️ Lo sentimos mucho 🙏 Esta función aún no está implementada en el programa. Estará disponible en un futuro cercano, ¡gracias por tu paciencia! ✨"
                    )
                    time.sleep(1)
                    print(
                        "⚠️ We’re sorry 🙏 This feature is not yet implemented in the system. It will be available soon, thank you for your patience! ✨"
                    )
                    time.sleep(1)
                    print(
                        "⚠️ 申し訳ありません 🙏 この機能はまだ実装されていません。近いうちに利用できるようになりますので、しばらくお待ちください！✨"
                    )
                    # ----------------------------------------------------
                case 3:
                    # ----------------------------------------------------

                    # Esta function se implementara en un futuro cercano.

                    print(
                        "⚠️ Lo sentimos mucho 🙏 Esta función aún no está implementada en el programa. Estará disponible en un futuro cercano, ¡gracias por tu paciencia! ✨"
                    )
                    time.sleep(1)
                    print(
                        "⚠️ We’re sorry 🙏 This feature is not yet implemented in the system. It will be available soon, thank you for your patience! ✨"
                    )
                    time.sleep(1)
                    print(
                        "⚠️ 申し訳ありません 🙏 この機能はまだ実装されていません。近いうちに利用できるようになりますので、しばらくお待ちください！✨"
                    )
                    # ----------------------------------------------------
                case 4:
                    # ----------------------------------------------------

                    # Esta function se implementara en un futuro cercano.

                    print(
                        "⚠️ Lo sentimos mucho 🙏 Esta función aún no está implementada en el programa. Estará disponible en un futuro cercano, ¡gracias por tu paciencia! ✨"
                    )
                    time.sleep(1)
                    print(
                        "⚠️ We’re sorry 🙏 This feature is not yet implemented in the system. It will be available soon, thank you for your patience! ✨"
                    )
                    time.sleep(1)
                    print(
                        "⚠️ 申し訳ありません 🙏 この機能はまだ実装されていません。近いうちに利用できるようになりますので、しばらくお待ちください！✨"
                    )
                    # ----------------------------------------------------
                case 5:
                    # ----------------------------------------------------

                    # Esta function se implementara en un futuro cercano.

                    print(
                        "⚠️ Lo sentimos mucho 🙏 Esta función aún no está implementada en el programa. Estará disponible en un futuro cercano, ¡gracias por tu paciencia! ✨"
                    )
                    time.sleep(1)
                    print(
                        "⚠️ We’re sorry 🙏 This feature is not yet implemented in the system. It will be available soon, thank you for your patience! ✨"
                    )
                    time.sleep(1)
                    print(
                        "⚠️ 申し訳ありません 🙏 この機能はまだ実装されていません。近いうちに利用できるようになりますので、しばらくお待ちください！✨"
                    )
                    # ----------------------------------------------------
                case 6:
                    # ----------------------------------------------------

                    # Esta function se implementara en un futuro cercano.

                    print(
                        "⚠️ Lo sentimos mucho 🙏 Esta función aún no está implementada en el programa. Estará disponible en un futuro cercano, ¡gracias por tu paciencia! ✨"
                    )
                    time.sleep(1)
                    print(
                        "⚠️ We’re sorry 🙏 This feature is not yet implemented in the system. It will be available soon, thank you for your patience! ✨"
                    )
                    time.sleep(1)
                    print(
                        "⚠️ 申し訳ありません 🙏 この機能はまだ実装されていません。近いうちに利用できるようになりますので、しばらくお待ちください！✨"
                    )
                    # ----------------------------------------------------
                case 7:
                    # ----------------------------------------------------

                    # Esta function se implementara en un futuro cercano.

                    print(
                        "⚠️ Lo sentimos mucho 🙏 Esta función aún no está implementada en el programa. Estará disponible en un futuro cercano, ¡gracias por tu paciencia! ✨"
                    )
                    time.sleep(1)
                    print(
                        "⚠️ We’re sorry 🙏 This feature is not yet implemented in the system. It will be available soon, thank you for your patience! ✨"
                    )
                    time.sleep(1)
                    print(
                        "⚠️ 申し訳ありません 🙏 この機能はまだ実装されていません。近いうちに利用できるようになりますので、しばらくお待ちください！✨"
                    )
                    # ----------------------------------------------------
                case 8:
                    # ----------------------------------------------------

                    # Esta function se implementara en un futuro cercano.

                    print(
                        "⚠️ Lo sentimos mucho 🙏 Esta función aún no está implementada en el programa. Estará disponible en un futuro cercano, ¡gracias por tu paciencia! ✨"
                    )
                    time.sleep(1)
                    print(
                        "⚠️ We’re sorry 🙏 This feature is not yet implemented in the system. It will be available soon, thank you for your patience! ✨"
                    )
                    time.sleep(1)
                    print(
                        "⚠️ 申し訳ありません 🙏 この機能はまだ実装されていません。近いうちに利用できるようになりますので、しばらくお待ちください！✨"
                    )
                    # ----------------------------------------------------
                case 9:
                    # ----------------------------------------------------

                    # Esta function se implementara en un futuro cercano.

                    print(
                        "⚠️ Lo sentimos mucho 🙏 Esta función aún no está implementada en el programa. Estará disponible en un futuro cercano, ¡gracias por tu paciencia! ✨"
                    )
                    time.sleep(1)
                    print(
                        "⚠️ We’re sorry 🙏 This feature is not yet implemented in the system. It will be available soon, thank you for your patience! ✨"
                    )
                    time.sleep(1)
                    print(
                        "⚠️ 申し訳ありません 🙏 この機能はまだ実装されていません。近いうちに利用できるようになりますので、しばらくお待ちください！✨"
                    )
                    # ----------------------------------------------------
                case 10:
                    # ----------------------------------------------------

                    # Esta function se implementara en un futuro cercano.

                    print(
                        "⚠️ Lo sentimos mucho 🙏 Esta función aún no está implementada en el programa. Estará disponible en un futuro cercano, ¡gracias por tu paciencia! ✨"
                    )
                    time.sleep(1)
                    print(
                        "⚠️ We’re sorry 🙏 This feature is not yet implemented in the system. It will be available soon, thank you for your patience! ✨"
                    )
                    time.sleep(1)
                    print(
                        "⚠️ 申し訳ありません 🙏 この機能はまだ実装されていません。近いうちに利用できるようになりますので、しばらくお待ちください！✨"
                    )
                    # ----------------------------------------------------
                case 11:
                    # ----------------------------------------------------

                    # Esta function se implementara en un futuro cercano.

                    print(
                        "⚠️ Lo sentimos mucho 🙏 Esta función aún no está implementada en el programa. Estará disponible en un futuro cercano, ¡gracias por tu paciencia! ✨"
                    )
                    time.sleep(1)
                    print(
                        "⚠️ We’re sorry 🙏 This feature is not yet implemented in the system. It will be available soon, thank you for your patience! ✨"
                    )
                    time.sleep(1)
                    print(
                        "⚠️ 申し訳ありません 🙏 この機能はまだ実装されていません。近いうちに利用できるようになりますので、しばらくお待ちください！✨"
                    )
                    # ----------------------------------------------------
                case 12:
                    # ----------------------------------------------------

                    # Esta function se implementara en un futuro cercano.

                    print(
                        "⚠️ Lo sentimos mucho 🙏 Esta función aún no está implementada en el programa. Estará disponible en un futuro cercano, ¡gracias por tu paciencia! ✨"
                    )
                    time.sleep(1)
                    print(
                        "⚠️ We’re sorry 🙏 This feature is not yet implemented in the system. It will be available soon, thank you for your patience! ✨"
                    )
                    time.sleep(1)
                    print(
                        "⚠️ 申し訳ありません 🙏 この機能はまだ実装されていません。近いうちに利用できるようになりますので、しばらくお待ちください！✨"
                    )
                    # ----------------------------------------------------
                case 13:
                    # ----------------------------------------------------

                    # Esta function se implementara en un futuro cercano.

                    print(
                        "⚠️ Lo sentimos mucho 🙏 Esta función aún no está implementada en el programa. Estará disponible en un futuro cercano, ¡gracias por tu paciencia! ✨"
                    )
                    time.sleep(1)
                    print(
                        "⚠️ We’re sorry 🙏 This feature is not yet implemented in the system. It will be available soon, thank you for your patience! ✨"
                    )
                    time.sleep(1)
                    print(
                        "⚠️ 申し訳ありません 🙏 この機能はまだ実装されていません。近いうちに利用できるようになりますので、しばらくお待ちください！✨"
                    )
                    # ----------------------------------------------------
                case 14:
                    # ----------------------------------------------------

                    # Esta function se implementara en un futuro cercano.

                    print(
                        "⚠️ Lo sentimos mucho 🙏 Esta función aún no está implementada en el programa. Estará disponible en un futuro cercano, ¡gracias por tu paciencia! ✨"
                    )
                    time.sleep(1)
                    print(
                        "⚠️ We’re sorry 🙏 This feature is not yet implemented in the system. It will be available soon, thank you for your patience! ✨"
                    )
                    time.sleep(1)
                    print(
                        "⚠️ 申し訳ありません 🙏 この機能はまだ実装されていません。近いうちに利用できるようになりますので、しばらくお待ちください！✨"
                    )
                    # ----------------------------------------------------
                case 15:
                    # ----------------------------------------------------

                    # Esta function se implementara en un futuro cercano.

                    print(
                        "⚠️ Lo sentimos mucho 🙏 Esta función aún no está implementada en el programa. Estará disponible en un futuro cercano, ¡gracias por tu paciencia! ✨"
                    )
                    time.sleep(1)
                    print(
                        "⚠️ We’re sorry 🙏 This feature is not yet implemented in the system. It will be available soon, thank you for your patience! ✨"
                    )
                    time.sleep(1)
                    print(
                        "⚠️ 申し訳ありません 🙏 この機能はまだ実装されていません。近いうちに利用できるようになりますので、しばらくお待ちください！✨"
                    )
                    # ----------------------------------------------------
                case 16:
                    print("Saliendo del programa...")
                    time.sleep(2)
                    print("Salida del programa exictosa.")
                    break
                case _:
                    print("Opcion invalida, escoga una opcion valida porfavor.")

    # Llama a la funcion.

    opciones_director()


# ----------------------------------------------------

# ✅ FASE 4.

# Funciones para el Jefe de estudios.


class Jefe_de_estudios(Jerarquia):

    # ----------------------------------------------------

    def inicio_sesion_Jefe_de_estudios(nombre_usuario: str, numero_contrasena: int):

        while True:

            try:
                nombre_usuario = str(input("Cree su nombre de usuario: "))
                re.findall(r"^[a-z]+[A-Z]+\s+\D+{4,10}*$")
                diccionario_jefe_estudios_ren9["name"] = (
                    nombre_usuario  # Esto estaba regular porque no guardaba la clave solo el valor.
                )
                diccionario_mensaje_jefe_estudios_ren10["name"] = nombre_usuario
                numero_contrasena = int(input("Cree su contraseña: "))
                if numero_contrasena is len() == 8:
                    diccionario_jefe_estudios_ren9["contraseña"] = (
                        numero_contrasena  # Esto estaba regular porque no guardaba la clave solo el valor.
                    )
                    print(
                        f"La contraseña: {numero_contrasena}, a sido guardado correctamente."
                    )
                else:
                    print(
                        f"La contraseña: {numero_contrasena}, tiene que tener 8 caracteres."
                    )
                time.sleep(1)
                print(f"Bienvenido: {nombre_usuario}.")
                break
            except Exception as e:
                print(f"Se ha producido un error: {e}")

    # Llama a la funcion.

    inicio_sesion_Jefe_de_estudios()

    # ----------------------------------------------------

    def opciones_Jefe_de_estudios():

        while True:

            opcions_ren4 = input(
                "Escoja una de estas opciones:\n"
                "1) Incresar.\n"  # Necesita diccionario , no X
                "2) Revisar planificación de asignaturas.\n"  # Necesita diccionario , si 0
                "3) Aprobar cambios de horarios.\n"  # Necesita diccionario , si 0
                "4) Supervisar calificaciones.\n"  # Necesita diccionario , si 0
                "5) Ver asistencia global.\n"  # Necesita diccionario , si 0
                "6) Resolver conflictos.\n"  # Necesita diccionario , si 0
                "7) Autorizar actividades extraescolares.\n"  # Necesita diccionario , si 0
                "8) Generar reportes oficiales.\n"  # Necesita diccionario , si 0
                "9) Coordinar exámenes.\n"  # Necesita diccionario , si 0
                "10) Revisar carga docente.\n"  # Necesita diccionario , si 0
                "11) Modificar datos.\n"  # Necesita diccionario , si 0
                "12) Enviar mensajes.\n"  # Necesita diccionario , si 0
                "13) Salir.\n"  # Necesita diccionario , no X
            )

            match opcions_ren4:
                case 1:
                    # ----------------------------------------------------

                    # Esta function se implementara en un futuro cercano.

                    print(
                        "⚠️ Lo sentimos mucho 🙏 Esta función aún no está implementada en el programa. Estará disponible en un futuro cercano, ¡gracias por tu paciencia! ✨"
                    )
                    time.sleep(1)
                    print(
                        "⚠️ We’re sorry 🙏 This feature is not yet implemented in the system. It will be available soon, thank you for your patience! ✨"
                    )
                    time.sleep(1)
                    print(
                        "⚠️ 申し訳ありません 🙏 この機能はまだ実装されていません。近いうちに利用できるようになりますので、しばらくお待ちください！✨"
                    )
                    # ----------------------------------------------------
                case 2:
                    # ----------------------------------------------------

                    # Esta function se implementara en un futuro cercano.

                    print(
                        "⚠️ Lo sentimos mucho 🙏 Esta función aún no está implementada en el programa. Estará disponible en un futuro cercano, ¡gracias por tu paciencia! ✨"
                    )
                    time.sleep(1)
                    print(
                        "⚠️ We’re sorry 🙏 This feature is not yet implemented in the system. It will be available soon, thank you for your patience! ✨"
                    )
                    time.sleep(1)
                    print(
                        "⚠️ 申し訳ありません 🙏 この機能はまだ実装されていません。近いうちに利用できるようになりますので、しばらくお待ちください！✨"
                    )
                    # ----------------------------------------------------
                case 3:
                    # ----------------------------------------------------

                    # Esta function se implementara en un futuro cercano.

                    print(
                        "⚠️ Lo sentimos mucho 🙏 Esta función aún no está implementada en el programa. Estará disponible en un futuro cercano, ¡gracias por tu paciencia! ✨"
                    )
                    time.sleep(1)
                    print(
                        "⚠️ We’re sorry 🙏 This feature is not yet implemented in the system. It will be available soon, thank you for your patience! ✨"
                    )
                    time.sleep(1)
                    print(
                        "⚠️ 申し訳ありません 🙏 この機能はまだ実装されていません。近いうちに利用できるようになりますので、しばらくお待ちください！✨"
                    )
                    # ----------------------------------------------------
                case 4:
                    # ----------------------------------------------------

                    # Esta function se implementara en un futuro cercano.

                    print(
                        "⚠️ Lo sentimos mucho 🙏 Esta función aún no está implementada en el programa. Estará disponible en un futuro cercano, ¡gracias por tu paciencia! ✨"
                    )
                    time.sleep(1)
                    print(
                        "⚠️ We’re sorry 🙏 This feature is not yet implemented in the system. It will be available soon, thank you for your patience! ✨"
                    )
                    time.sleep(1)
                    print(
                        "⚠️ 申し訳ありません 🙏 この機能はまだ実装されていません。近いうちに利用できるようになりますので、しばらくお待ちください！✨"
                    )
                    # ----------------------------------------------------
                case 5:
                    # ----------------------------------------------------

                    # Esta function se implementara en un futuro cercano.

                    print(
                        "⚠️ Lo sentimos mucho 🙏 Esta función aún no está implementada en el programa. Estará disponible en un futuro cercano, ¡gracias por tu paciencia! ✨"
                    )
                    time.sleep(1)
                    print(
                        "⚠️ We’re sorry 🙏 This feature is not yet implemented in the system. It will be available soon, thank you for your patience! ✨"
                    )
                    time.sleep(1)
                    print(
                        "⚠️ 申し訳ありません 🙏 この機能はまだ実装されていません。近いうちに利用できるようになりますので、しばらくお待ちください！✨"
                    )
                    # ----------------------------------------------------
                case 6:
                    # ----------------------------------------------------

                    # Esta function se implementara en un futuro cercano.

                    print(
                        "⚠️ Lo sentimos mucho 🙏 Esta función aún no está implementada en el programa. Estará disponible en un futuro cercano, ¡gracias por tu paciencia! ✨"
                    )
                    time.sleep(1)
                    print(
                        "⚠️ We’re sorry 🙏 This feature is not yet implemented in the system. It will be available soon, thank you for your patience! ✨"
                    )
                    time.sleep(1)
                    print(
                        "⚠️ 申し訳ありません 🙏 この機能はまだ実装されていません。近いうちに利用できるようになりますので、しばらくお待ちください！✨"
                    )
                    # ----------------------------------------------------
                case 7:
                    # ----------------------------------------------------

                    # Esta function se implementara en un futuro cercano.

                    print(
                        "⚠️ Lo sentimos mucho 🙏 Esta función aún no está implementada en el programa. Estará disponible en un futuro cercano, ¡gracias por tu paciencia! ✨"
                    )
                    time.sleep(1)
                    print(
                        "⚠️ We’re sorry 🙏 This feature is not yet implemented in the system. It will be available soon, thank you for your patience! ✨"
                    )
                    time.sleep(1)
                    print(
                        "⚠️ 申し訳ありません 🙏 この機能はまだ実装されていません。近いうちに利用できるようになりますので、しばらくお待ちください！✨"
                    )
                    # ----------------------------------------------------
                case 8:
                    # ----------------------------------------------------

                    # Esta function se implementara en un futuro cercano.

                    print(
                        "⚠️ Lo sentimos mucho 🙏 Esta función aún no está implementada en el programa. Estará disponible en un futuro cercano, ¡gracias por tu paciencia! ✨"
                    )
                    time.sleep(1)
                    print(
                        "⚠️ We’re sorry 🙏 This feature is not yet implemented in the system. It will be available soon, thank you for your patience! ✨"
                    )
                    time.sleep(1)
                    print(
                        "⚠️ 申し訳ありません 🙏 この機能はまだ実装されていません。近いうちに利用できるようになりますので、しばらくお待ちください！✨"
                    )
                    # ----------------------------------------------------
                case 9:
                    # ----------------------------------------------------

                    # Esta function se implementara en un futuro cercano.

                    print(
                        "⚠️ Lo sentimos mucho 🙏 Esta función aún no está implementada en el programa. Estará disponible en un futuro cercano, ¡gracias por tu paciencia! ✨"
                    )
                    time.sleep(1)
                    print(
                        "⚠️ We’re sorry 🙏 This feature is not yet implemented in the system. It will be available soon, thank you for your patience! ✨"
                    )
                    time.sleep(1)
                    print(
                        "⚠️ 申し訳ありません 🙏 この機能はまだ実装されていません。近いうちに利用できるようになりますので、しばらくお待ちください！✨"
                    )
                    # ----------------------------------------------------
                case 10:
                    # ----------------------------------------------------

                    # Esta function se implementara en un futuro cercano.

                    print(
                        "⚠️ Lo sentimos mucho 🙏 Esta función aún no está implementada en el programa. Estará disponible en un futuro cercano, ¡gracias por tu paciencia! ✨"
                    )
                    time.sleep(1)
                    print(
                        "⚠️ We’re sorry 🙏 This feature is not yet implemented in the system. It will be available soon, thank you for your patience! ✨"
                    )
                    time.sleep(1)
                    print(
                        "⚠️ 申し訳ありません 🙏 この機能はまだ実装されていません。近いうちに利用できるようになりますので、しばらくお待ちください！✨"
                    )
                    # ----------------------------------------------------
                case 11:
                    # ----------------------------------------------------

                    # Esta function se implementara en un futuro cercano.

                    print(
                        "⚠️ Lo sentimos mucho 🙏 Esta función aún no está implementada en el programa. Estará disponible en un futuro cercano, ¡gracias por tu paciencia! ✨"
                    )
                    time.sleep(1)
                    print(
                        "⚠️ We’re sorry 🙏 This feature is not yet implemented in the system. It will be available soon, thank you for your patience! ✨"
                    )
                    time.sleep(1)
                    print(
                        "⚠️ 申し訳ありません 🙏 この機能はまだ実装されていません。近いうちに利用できるようになりますので、しばらくお待ちください！✨"
                    )
                    # ----------------------------------------------------
                case 12:
                    # ----------------------------------------------------

                    # Esta function se implementara en un futuro cercano.

                    print(
                        "⚠️ Lo sentimos mucho 🙏 Esta función aún no está implementada en el programa. Estará disponible en un futuro cercano, ¡gracias por tu paciencia! ✨"
                    )
                    time.sleep(1)
                    print(
                        "⚠️ We’re sorry 🙏 This feature is not yet implemented in the system. It will be available soon, thank you for your patience! ✨"
                    )
                    time.sleep(1)
                    print(
                        "⚠️ 申し訳ありません 🙏 この機能はまだ実装されていません。近いうちに利用できるようになりますので、しばらくお待ちください！✨"
                    )
                    # ----------------------------------------------------
                case 13:
                    print("Saliendo del programa...")
                    time.sleep(2)
                    print("Salida del programa exictosa.")
                    break
                case _:
                    print("Opcion invalida, escoga una opcion valida porfavor.")

    # Llama a la funcion.

    opciones_Jefe_de_estudios()


# ----------------------------------------------------

# ✅ FASE 5.

# Funciones para el Admin.


class Admin(Jerarquia):

    # ----------------------------------------------------

    def inicio_sesion_Admin(nombre_usuario: str, numero_contrasena: int):

        while True:

            try:
                nombre_usuario = str(input("Cree su nombre de usuario: "))
                re.findall(r"^[a-z]+[A-Z]+\s+\D+{4,10}*$")
                diccionario_admin_ren5["name"] = (
                    nombre_usuario  # Esto estaba regular porque no guardaba la clave solo el valor.
                )
                diccionario_mensajes_admin_ren6["name"] = nombre_usuario
                numero_contrasena = int(input("Cree su contraseña: "))
                if numero_contrasena is len() == 8:
                    diccionario_admin_ren5["contraseña"] = (
                        numero_contrasena  # Esto estaba regular porque no guardaba la clave solo el valor.
                    )
                    print(
                        f"La contraseña: {numero_contrasena}, a sido guardado correctamente."
                    )
                else:
                    print(
                        f"La contraseña: {numero_contrasena}, tiene que tener 8 caracteres."
                    )
                time.sleep(1)
                print(f"Bienvenido: {nombre_usuario}.")
                break
            except Exception as e:
                print(f"Se ha producido un error: {e}")

    # Llama a la funcion.

    inicio_sesion_Admin()

    # ----------------------------------------------------

    def opciones_Admin():

        while True:

            opcions_ren4 = input(
                "Escoja una de estas opciones:\n"
                "1) Incresar.\n"  # Necesita diccionario , no X
                "2) Crear usuario.\n"  # Necesita diccionario , si 0
                "3) Eliminar usuario.\n"  # Necesita diccionario , si 0
                "4) Editar datos de usuario.\n"  # Necesita diccionario , si 0
                "5) Resetear contraseña.\n"  # Necesita diccionario , si 0
                "6) Gestionar permisos.\n"  # Necesita diccionario , si 0
                "7) Ver logs de actividad.\n"  # Necesita diccionario , si 0
                "8) Respaldar base de datos.\n"  # Necesita diccionario , si 0
                "9) Restaurar base de datos.\n"  # Necesita diccionario , si 0
                "10) Importar/exportar datos.\n"  # Necesita diccionario , si 0
                "11) Gestionar almacenamiento.\n"  # Necesita diccionario , si 0
                "12) Monitorear uso del sistema.\n"  # Necesita diccionario , si 0
                "13) Control de versiones.\n"  # Necesita diccionario , si 0
                "14) Modificar datos.\n"  # Necesita diccionario , si 0
                "15) Enviar mensajes.\n"  # Necesita diccionario , si 0
                "16) Salir.\n"  # Necesita diccionario , no X
            )

            match opcions_ren4:
                case 1:
                    # ----------------------------------------------------

                    # Esta function se implementara en un futuro cercano.

                    print(
                        "⚠️ Lo sentimos mucho 🙏 Esta función aún no está implementada en el programa. Estará disponible en un futuro cercano, ¡gracias por tu paciencia! ✨"
                    )
                    time.sleep(1)
                    print(
                        "⚠️ We’re sorry 🙏 This feature is not yet implemented in the system. It will be available soon, thank you for your patience! ✨"
                    )
                    time.sleep(1)
                    print(
                        "⚠️ 申し訳ありません 🙏 この機能はまだ実装されていません。近いうちに利用できるようになりますので、しばらくお待ちください！✨"
                    )
                    # ----------------------------------------------------
                case 2:
                    # ----------------------------------------------------

                    # Esta function se implementara en un futuro cercano.

                    print(
                        "⚠️ Lo sentimos mucho 🙏 Esta función aún no está implementada en el programa. Estará disponible en un futuro cercano, ¡gracias por tu paciencia! ✨"
                    )
                    time.sleep(1)
                    print(
                        "⚠️ We’re sorry 🙏 This feature is not yet implemented in the system. It will be available soon, thank you for your patience! ✨"
                    )
                    time.sleep(1)
                    print(
                        "⚠️ 申し訳ありません 🙏 この機能はまだ実装されていません。近いうちに利用できるようになりますので、しばらくお待ちください！✨"
                    )
                    # ----------------------------------------------------
                case 3:
                    # ----------------------------------------------------

                    # Esta function se implementara en un futuro cercano.

                    print(
                        "⚠️ Lo sentimos mucho 🙏 Esta función aún no está implementada en el programa. Estará disponible en un futuro cercano, ¡gracias por tu paciencia! ✨"
                    )
                    time.sleep(1)
                    print(
                        "⚠️ We’re sorry 🙏 This feature is not yet implemented in the system. It will be available soon, thank you for your patience! ✨"
                    )
                    time.sleep(1)
                    print(
                        "⚠️ 申し訳ありません 🙏 この機能はまだ実装されていません。近いうちに利用できるようになりますので、しばらくお待ちください！✨"
                    )
                    # ----------------------------------------------------
                case 4:
                    # ----------------------------------------------------

                    # Esta function se implementara en un futuro cercano.

                    print(
                        "⚠️ Lo sentimos mucho 🙏 Esta función aún no está implementada en el programa. Estará disponible en un futuro cercano, ¡gracias por tu paciencia! ✨"
                    )
                    time.sleep(1)
                    print(
                        "⚠️ We’re sorry 🙏 This feature is not yet implemented in the system. It will be available soon, thank you for your patience! ✨"
                    )
                    time.sleep(1)
                    print(
                        "⚠️ 申し訳ありません 🙏 この機能はまだ実装されていません。近いうちに利用できるようになりますので、しばらくお待ちください！✨"
                    )
                    # ----------------------------------------------------
                case 5:
                    # ----------------------------------------------------

                    # Esta function se implementara en un futuro cercano.

                    print(
                        "⚠️ Lo sentimos mucho 🙏 Esta función aún no está implementada en el programa. Estará disponible en un futuro cercano, ¡gracias por tu paciencia! ✨"
                    )
                    time.sleep(1)
                    print(
                        "⚠️ We’re sorry 🙏 This feature is not yet implemented in the system. It will be available soon, thank you for your patience! ✨"
                    )
                    time.sleep(1)
                    print(
                        "⚠️ 申し訳ありません 🙏 この機能はまだ実装されていません。近いうちに利用できるようになりますので、しばらくお待ちください！✨"
                    )
                    # ----------------------------------------------------
                case 6:
                    # ----------------------------------------------------

                    # Esta function se implementara en un futuro cercano.

                    print(
                        "⚠️ Lo sentimos mucho 🙏 Esta función aún no está implementada en el programa. Estará disponible en un futuro cercano, ¡gracias por tu paciencia! ✨"
                    )
                    time.sleep(1)
                    print(
                        "⚠️ We’re sorry 🙏 This feature is not yet implemented in the system. It will be available soon, thank you for your patience! ✨"
                    )
                    time.sleep(1)
                    print(
                        "⚠️ 申し訳ありません 🙏 この機能はまだ実装されていません。近いうちに利用できるようになりますので、しばらくお待ちください！✨"
                    )
                    # ----------------------------------------------------
                case 7:
                    # ----------------------------------------------------

                    # Esta function se implementara en un futuro cercano.

                    print(
                        "⚠️ Lo sentimos mucho 🙏 Esta función aún no está implementada en el programa. Estará disponible en un futuro cercano, ¡gracias por tu paciencia! ✨"
                    )
                    time.sleep(1)
                    print(
                        "⚠️ We’re sorry 🙏 This feature is not yet implemented in the system. It will be available soon, thank you for your patience! ✨"
                    )
                    time.sleep(1)
                    print(
                        "⚠️ 申し訳ありません 🙏 この機能はまだ実装されていません。近いうちに利用できるようになりますので、しばらくお待ちください！✨"
                    )
                    # ----------------------------------------------------
                case 8:
                    # ----------------------------------------------------

                    # Esta function se implementara en un futuro cercano.

                    print(
                        "⚠️ Lo sentimos mucho 🙏 Esta función aún no está implementada en el programa. Estará disponible en un futuro cercano, ¡gracias por tu paciencia! ✨"
                    )
                    time.sleep(1)
                    print(
                        "⚠️ We’re sorry 🙏 This feature is not yet implemented in the system. It will be available soon, thank you for your patience! ✨"
                    )
                    time.sleep(1)
                    print(
                        "⚠️ 申し訳ありません 🙏 この機能はまだ実装されていません。近いうちに利用できるようになりますので、しばらくお待ちください！✨"
                    )
                    # ----------------------------------------------------
                case 9:
                    # ----------------------------------------------------

                    # Esta function se implementara en un futuro cercano.

                    print(
                        "⚠️ Lo sentimos mucho 🙏 Esta función aún no está implementada en el programa. Estará disponible en un futuro cercano, ¡gracias por tu paciencia! ✨"
                    )
                    time.sleep(1)
                    print(
                        "⚠️ We’re sorry 🙏 This feature is not yet implemented in the system. It will be available soon, thank you for your patience! ✨"
                    )
                    time.sleep(1)
                    print(
                        "⚠️ 申し訳ありません 🙏 この機能はまだ実装されていません。近いうちに利用できるようになりますので、しばらくお待ちください！✨"
                    )
                    # ----------------------------------------------------
                case 10:
                    # ----------------------------------------------------

                    # Esta function se implementara en un futuro cercano.

                    print(
                        "⚠️ Lo sentimos mucho 🙏 Esta función aún no está implementada en el programa. Estará disponible en un futuro cercano, ¡gracias por tu paciencia! ✨"
                    )
                    time.sleep(1)
                    print(
                        "⚠️ We’re sorry 🙏 This feature is not yet implemented in the system. It will be available soon, thank you for your patience! ✨"
                    )
                    time.sleep(1)
                    print(
                        "⚠️ 申し訳ありません 🙏 この機能はまだ実装されていません。近いうちに利用できるようになりますので、しばらくお待ちください！✨"
                    )
                    # ----------------------------------------------------
                case 11:
                    # ----------------------------------------------------

                    # Esta function se implementara en un futuro cercano.

                    print(
                        "⚠️ Lo sentimos mucho 🙏 Esta función aún no está implementada en el programa. Estará disponible en un futuro cercano, ¡gracias por tu paciencia! ✨"
                    )
                    time.sleep(1)
                    print(
                        "⚠️ We’re sorry 🙏 This feature is not yet implemented in the system. It will be available soon, thank you for your patience! ✨"
                    )
                    time.sleep(1)
                    print(
                        "⚠️ 申し訳ありません 🙏 この機能はまだ実装されていません。近いうちに利用できるようになりますので、しばらくお待ちください！✨"
                    )
                    # ----------------------------------------------------
                case 12:

                    # ----------------------------------------------------

                    # Esta function se implementara en un futuro cercano.

                    print(
                        "⚠️ Lo sentimos mucho 🙏 Esta función aún no está implementada en el programa. Estará disponible en un futuro cercano, ¡gracias por tu paciencia! ✨"
                    )
                    time.sleep(1)
                    print(
                        "⚠️ We’re sorry 🙏 This feature is not yet implemented in the system. It will be available soon, thank you for your patience! ✨"
                    )
                    time.sleep(1)
                    print(
                        "⚠️ 申し訳ありません 🙏 この機能はまだ実装されていません。近いうちに利用できるようになりますので、しばらくお待ちください！✨"
                    )
                    # ----------------------------------------------------
                case 13:

                    # ----------------------------------------------------

                    # Esta function se implementara en un futuro cercano.

                    print(
                        "⚠️ Lo sentimos mucho 🙏 Esta función aún no está implementada en el programa. Estará disponible en un futuro cercano, ¡gracias por tu paciencia! ✨"
                    )
                    time.sleep(1)
                    print(
                        "⚠️ We’re sorry 🙏 This feature is not yet implemented in the system. It will be available soon, thank you for your patience! ✨"
                    )
                    time.sleep(1)
                    print(
                        "⚠️ 申し訳ありません 🙏 この機能はまだ実装されていません。近いうちに利用できるようになりますので、しばらくお待ちください！✨"
                    )
                    # ----------------------------------------------------
                case 14:
                    # ----------------------------------------------------

                    # Esta function se implementara en un futuro cercano.

                    print(
                        "⚠️ Lo sentimos mucho 🙏 Esta función aún no está implementada en el programa. Estará disponible en un futuro cercano, ¡gracias por tu paciencia! ✨"
                    )
                    time.sleep(1)
                    print(
                        "⚠️ We’re sorry 🙏 This feature is not yet implemented in the system. It will be available soon, thank you for your patience! ✨"
                    )
                    time.sleep(1)
                    print(
                        "⚠️ 申し訳ありません 🙏 この機能はまだ実装されていません。近いうちに利用できるようになりますので、しばらくお待ちください！✨"
                    )
                    # ----------------------------------------------------
                case 15:
                    # ----------------------------------------------------

                    # Esta function se implementara en un futuro cercano.

                    print(
                        "⚠️ Lo sentimos mucho 🙏 Esta función aún no está implementada en el programa. Estará disponible en un futuro cercano, ¡gracias por tu paciencia! ✨"
                    )
                    time.sleep(1)
                    print(
                        "⚠️ We’re sorry 🙏 This feature is not yet implemented in the system. It will be available soon, thank you for your patience! ✨"
                    )
                    time.sleep(1)
                    print(
                        "⚠️ 申し訳ありません 🙏 この機能はまだ実装されていません。近いうちに利用できるようになりますので、しばらくお待ちください！✨"
                    )
                    # ----------------------------------------------------
                case 16:
                    print("Saliendo del programa...")
                    time.sleep(2)
                    print("Salida del programa exictosa.")
                    break
                case _:
                    print("Opcion invalida, escoga una opcion valida porfavor.")

    # Llama a la funcion.

    opciones_Admin()


# ----------------------------------------------------
