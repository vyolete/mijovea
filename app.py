import streamlit as st

def main():
    st.set_page_config(page_title="Blog Multitemático", layout="wide")
    st.sidebar.title("Categorías")
    
    menu = {
        "Inicio": inicio,
        "Adultos": adultos,
        "Tecnología": tecnologia,
        "Salud": salud,
        "Diversión y Ocio": diversion,
        "Cine": cine,
        "Música": musica,
        "Restaurantes": restaurantes,
        "Recetas": recetas,
        "Naturaleza": naturaleza
    }
    
    choice = st.sidebar.radio("Selecciona una categoría", list(menu.keys()))
    menu[choice]()

def inicio():
    st.title("Bienvenidos al Blog Multitemático")
    st.write("Aquí encontrarás contenido interesante sobre diversas temáticas.")

def adultos():
    st.title("Vida Adulta: Retos y Consejos")
    st.write("La vida adulta trae consigo responsabilidades, pero también oportunidades de crecimiento.")
    st.write("Consejo: Organiza tus finanzas personales y prioriza el bienestar mental.")

def tecnologia():
    st.title("Últimas Tendencias Tecnológicas")
    st.write("La inteligencia artificial, el metaverso y la computación cuántica están revolucionando el mundo.")

def salud():
    st.title("Salud y Bienestar")
    st.write("La prevención y el autocuidado son clave para una vida saludable. Mantén hábitos de ejercicio y buena alimentación.")

def diversion():
    st.title("Diversión y Ocio")
    st.write("Descubre actividades recreativas para desconectarte y disfrutar del tiempo libre.")

def cine():
    st.title("Recomendaciones de Cine")
    st.write("Desde clásicos del cine hasta los últimos estrenos, aquí encontrarás las mejores recomendaciones.")

def musica():
    st.title("Explorando el Mundo de la Música")
    st.write("Descubre nuevos géneros, artistas y playlists para cada ocasión.")

def restaurantes():
    st.title("Guía de Restaurantes")
    st.write("Los mejores lugares para disfrutar de una buena comida, desde cocina gourmet hasta comida rápida.")

def recetas():
    st.title("Recetas Fáciles y Deliciosas")
    st.write("Aprende a cocinar platos sencillos con ingredientes accesibles.")

def naturaleza():
    st.title("Conexión con la Naturaleza")
    st.write("Explora destinos naturales, actividades al aire libre y consejos para cuidar el medio ambiente.")

if __name__ == "__main__":
    main()
