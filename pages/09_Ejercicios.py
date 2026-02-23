import streamlit as st
import numpy as np

# -----------------------------
# EJERCICIO 1: SALUDO SIMPLE
# -----------------------------
st.subheader("Saludo simple")

name = st.text_input("Ingrese su nombre")

if name:
    st.write("Hola", name)

st.divider()


# -----------------------------
# EJERCICIO 2: CALCULADORA
# -----------------------------
st.subheader("Calculadora de Producto")

n1 = st.number_input("Ingrese el primer número:")
n2 = st.number_input("Ingrese el segundo número:")

if st.button("Calcular"):
    resultado = n1 * n2
    st.write("El producto es:", resultado)

    # Ahora sí cumple la rúbrica
    if n1 > 100 or n2 > 100:
        st.warning("Uno de los números ingresados es mayor a 100")

st.divider()


# -----------------------------
# EJERCICIO 3: CONVERTIDOR
# -----------------------------
st.subheader("Convertidor de temperatura")

num = st.number_input("Ingrese la temperatura")
tem = st.radio(
    "Seleccione una conversión",
    ("Celsius a Fahrenheit", "Fahrenheit a Celsius")
)

if st.button("Convertir"):
    if tem == "Celsius a Fahrenheit":
        resultado = num * 9/5 + 32
        st.write("Resultado:", resultado)
    else:
        # CORREGIDO con paréntesis
        resultado = (num - 32) * 5/9
        st.write("Resultado:", resultado)

st.divider()


# -----------------------------
# EJERCICIO 4: GALERÍA
# -----------------------------
st.subheader("Galería de mascotas")

t1, t2, t3 = st.tabs(["Perros", "Gatos", "Aves"])

with t1:
    st.image("https://placedog.net/500")
    if st.button("Me gusta 🐶", key="perro"):
        st.toast("Te gusta esta mascota")

with t2:
    st.image("https://placekitten.com/500/500")
    if st.button("Me gusta 🐱", key="gato"):
        st.toast("Te gusta esta mascota")

with t3:
    st.image("https://loremflickr.com/500/500/bird")
    if st.button("Me gusta 🐦", key="ave"):
        st.toast("Te gusta esta mascota")

st.divider()


# -----------------------------
# EJERCICIO 5: CAJA DE COMENTARIOS
# -----------------------------
st.subheader("Caja de comentarios")

with st.form("form_comentarios"):
    asunto = st.text_input("Asunto")
    comentario = st.text_area("Comentario")
    enviar = st.form_submit_button("Enviar")

    if enviar:
        # Ahora cumple exactamente lo pedido:
        if comentario == "":
            st.warning("Debe escribir un comentario")
        else:
            st.json({"Asunto": asunto})
            st.json({"Comentario": comentario})

st.divider()


# -----------------------------
# EJERCICIO 6: LOGIN SIMULADO
# -----------------------------
st.subheader("Login simulado")

if "logueado" not in st.session_state:
    st.session_state.logueado = False

if st.session_state.logueado:
    st.success("Bienvenido, admin!")

    if st.button("Cerrar sesión"):
        st.session_state.logueado = False
        st.rerun()

else:
    usuario = st.text_input("Usuario")
    password = st.text_input("Password", type="password")

    if st.button("Ingresar"):
        if usuario == "admin" and password == "1234":
            st.session_state.logueado = True
            st.rerun()
        else:
            st.error("Usuario o contraseña incorrectos")

st.divider()


# -----------------------------
# EJERCICIO 7: LISTA DE COMPRAS
# -----------------------------
st.subheader("Lista de Compras")

if "lista" not in st.session_state:
    st.session_state.lista = []

producto = st.text_input("Ingrese el producto")

if st.button("Agregar"):
    if producto:
        st.session_state.lista.append(producto)
        st.rerun()
    else:
        st.warning("Debe ingresar un producto")

if st.session_state.lista:
    st.write("### Tus Productos")
    for i, item in enumerate(st.session_state.lista):
        st.write(f"{i+1}. {item}")

if st.button("Limpiar"):
    st.session_state.lista = []
    st.rerun()

st.divider()


# -----------------------------
# EJERCICIO 8: GRÁFICO INTERACTIVO
# -----------------------------
st.subheader("Gráfico Interactivo")

n = st.slider("Seleccione un número", 10, 100, 10)

if st.button("Regenerar"):
    st.rerun()

datos = np.random.randn(n)
st.line_chart(datos)