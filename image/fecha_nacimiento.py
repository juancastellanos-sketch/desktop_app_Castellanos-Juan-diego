import tkinter as tk
from tkinter import ttk
from tkinter import PhotoImage

# ---------------- FUNCION PARA CREAR VENTANAS ----------------
def crear_ventana(titulo, contenido):
    ventana = tk.Toplevel()
    ventana.title(titulo)
    ventana.geometry("600x450")
    ventana.configure(bg="#F4F6F7")

    ttk.Label(
        ventana,
        text=titulo,
        font=("Arial", 16, "bold")
    ).pack(pady=15)
    texto = tk.Text(
        ventana,
        wrap="word",
        font=("Arial", 11),
        bg="white"
    )
    texto.pack(expand=True, fill="both", padx=20, pady=10)
    texto.insert("1.0", contenido)
    texto.config(state="disabled")
    image= PhotoImage(file= "desktop-app_Castellanos_Juan_diego/1000012201.jpg")
    image_label= tk.Label(frame, image=image)
    image_label()

# ---------------- VENTANA PRINCIPAL ----------------
root = tk.Tk()
root.title("Mi Proyecto Personal - Tkinter")
root.geometry("500x600")
root.configure(bg="#D6EAF8")

ttk.Label(
    root,
    text="PROYECTO PERSONAL\n10 VENTANAS",
    font=("Arial", 18, "bold"),
    anchor="center"
).pack(pady=20)

# ---------------- CONTENIDO ----------------
info = [
("1. Lugar y fecha de nacimiento",
"""Nombre: [juan diego]

Lugar de nacimiento: [bucaramanga, colombia]
Fecha de nacimiento: [29/05/2010]

Datos importantes:
- colombiano
- 16 años
- san gil santander
"""),

("2. Datos médicos relevantes",
"""Grupo sanguíneo: [Ej. O+]

Alergias:
- [penicilina / por que me da fiebre, dolor de cabeza,mareo y vomito ]

Condiciones médicas:
- [Información]

Contacto de emergencia:
- [juan diego y 3138073772]
"""),

("3. Información familiar",
"""Padre: [jaime alberto]

Madre: [Ana Milena]

Hermanos:
- [2 y sara isabella,adriana lucia]

Valores familiares:
- Respeto
- Honestidad
- Apoyo mutuo
- ayudar a las personas necesitadas
- solucionar las cosas dialogando

"""),

("4. Proceso educativo",
"""Institución actual:
- [san jose de guanenta]

Otras instituciones:
- [institucion educativa la esperanza]

Logros académicos:
- [buen desempeño en quimica y matematicas]
- [participacion en clase]
"""),

("5. Mis amigos",
"""Mejores amigos:
- [gabriel hernando gualdron castellanos]
- [javier esteban rodriguez aparicio]
- [estiben mauricio delgado bermudez]
- [andres felipe mejia ospina]
- [laura juliana gualdron castellanos]
- [miguel angel mancilla]
- [ana gabriela gomes rojas]
- [anggy yuliana fuentes]
- [gabriela velazquez solano]
- [aranza sofia rojas montilla]
- [juliana marcela ruiz primitiva]
- [johan sebastian gil arias]
- [samir cudris mujica]
- [yuliana delgado bermudez]
- [javier felipe luque]
- [arnulfo castellanos castellanos]
- [yuly jacqueline aguas]
- [andres felipe bueno sanchez]
Actividades que compartimos:
- Estudiar
- Deportes
- Videojuegos
- Salidas
"""),

("6. Hobbies y tiempo libre",
"""Mis hobbies favoritos:
- Leer
- Escuchar música
- Jugar fútbol
- hablar con mis amigos
- editar videos para mi canal de tiktok

Tiempo libre:
- Practicar ejercicio
- Aprender nuevas habilidades
- entrenar boxeo en la cuadra de mi casa
- jugar futbol
- salir con mis amigos y mi novia al centro comercial
- escuchar cumbias 
- lavar mi carro
- ayudar a mi familia en la casa
- ver peliculas y series
- jugar videojuegos
- jugar xboox en mi casa con mis amigos
- salir a pasear con mi madre
- salir a parchar con mis amigos a la villa olimpica
"""),

("7. Horario semanal 24/7",
"""Lunes a Viernes

6:00  Levantarme
7:00  Colegio
13:30 Almuerzo
15:00 colegio
18:00 entrenamiento de futbol
20:00 tareas
22:00 Dormir

Sábado y domingo:
- Familia
- Descanso
- Proyectos personales
-salidas con amigos y mi novia al centro comercial
"""),

("8. Preparación Saber 2026",
"""Objetivo: Obtener un puntaje superior a [3.5].

Estrategia:
- 2 horas diarias de matemáticas
- Lectura crítica 30 min
- Inglés 30 min
- Simulacro cada sábado
- Revisar errores cada domingo
"""),

("9. Proyecto de vida 2031",
"""Meta profesional:
- Graduarme de [Carrera]

Metas personales:
- Tener estabilidad económica
- estar en la sub 20 de futbol en bucaramanga
- ser arquero profesional del bucaramanga
- Viajar
- Crear mi propio emprendimiento
"""),

("10. Tema libre",
"""TEMA: la inteligencia artificial

¿Por qué me interesa?

La inteligencia artificial está transformando la educación, la medicina y la tecnología. Me gustaría aprender programación para desarrollar soluciones que ayuden a las personas.
""")
]

# ---------------- BOTONES ----------------
for titulo, contenido in info:
    ttk.Button(
        root,
        text=titulo,
        command=lambda t=titulo, c=contenido: crear_ventana(t, c)
    ).pack(fill="x", padx=40, pady=6)

ttk.Label(
    root,
    text="Desarrollado en Python + Tkinter",
    font=("Arial", 9)
).pack(side="bottom", pady=15)

root.mainloop()
        
        



