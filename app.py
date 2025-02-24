import streamlit as st

def main():
    st.set_page_config(page_title="Blog Multitemático", layout="wide")
    st.sidebar.image("https://source.unsplash.com/random/300x200?blog")
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
    st.image("https://source.unsplash.com/random/800x400?welcome")
    st.write("Aquí encontrarás contenido interesante sobre diversas temáticas.")

def adultos():
    st.title("Vida Adulta: Retos y Consejos")
    st.image("https://source.unsplash.com/random/800x400?adulthood")
    st.write("La vida adulta trae consigo responsabilidades, pero también oportunidades de crecimiento.")
    st.write("Consejo: Organiza tus finanzas personales y prioriza el bienestar mental.")
    st.markdown("[Cómo administrar tus finanzas](https://www.bbva.com/es/como-administrar-finanzas-personales/)")
    st.markdown("[5 hábitos para mejorar tu salud mental](https://www.who.int/es)")
    st.markdown("[Cómo equilibrar trabajo y vida personal](https://www.forbes.com/sites/work-life-balance/)")
    st.markdown("[Consejos para el desarrollo profesional](https://www.linkedin.com/learning/)")

def tecnologia():
    st.title("Últimas Tendencias Tecnológicas")
    st.image("https://source.unsplash.com/random/800x400?technology")
    st.write("La inteligencia artificial, el metaverso y la computación cuántica están revolucionando el mundo.")
    st.markdown("[Qué es la inteligencia artificial](https://www.ibm.com/artificial-intelligence)")
    st.markdown("[El futuro del metaverso](https://www.meta.com/metaverse/)")
    st.markdown("[Computación cuántica y sus aplicaciones](https://www.ibm.com/quantum-computing/)")
    st.markdown("[Tendencias tecnológicas para 2025](https://www.gartner.com/en/insights/technology)")

def salud():
    st.title("Salud y Bienestar")
    st.image("https://source.unsplash.com/random/800x400?health")
    st.write("La prevención y el autocuidado son clave para una vida saludable. Mantén hábitos de ejercicio y buena alimentación.")
    st.markdown("[Consejos para una alimentación balanceada](https://www.nutrition.org/)")
    st.markdown("[Ejercicios para mantenerse en forma](https://www.healthline.com/nutrition/best-exercises)")
    st.markdown("[Cómo mejorar tu sueño](https://www.sleepfoundation.org/)")
    st.markdown("[Beneficios de la meditación](https://www.mindful.org/)")

def diversion():
    st.title("Diversión y Ocio")
    st.image("https://source.unsplash.com/random/800x400?fun")
    st.write("Descubre actividades recreativas para desconectarte y disfrutar del tiempo libre.")
    st.markdown("[10 juegos de mesa recomendados](https://boardgamegeek.com/)")
    st.markdown("[Los mejores parques de diversiones](https://www.tripadvisor.com/Attractions)")
    st.markdown("[Ideas para un fin de semana divertido](https://www.lonelyplanet.com/)")
    st.markdown("[Eventos culturales cerca de ti](https://www.eventbrite.com/)")

def cine():
    st.title("Recomendaciones de Cine")
    st.image("https://source.unsplash.com/random/800x400?movies")
    st.write("Desde clásicos del cine hasta los últimos estrenos, aquí encontrarás las mejores recomendaciones.")
    st.markdown("[Top películas del año](https://www.rottentomatoes.com/)")
    st.markdown("[Mejores series en streaming](https://www.netflix.com/)")
    st.markdown("[Premios Oscar y nominaciones](https://www.oscars.org/)")
    st.markdown("[Cine independiente destacado](https://www.sundance.org/)")

def musica():
    st.title("Explorando el Mundo de la Música")
    st.image("https://source.unsplash.com/random/800x400?music")
    st.write("Descubre nuevos géneros, artistas y playlists para cada ocasión.")
    st.markdown("[Top 100 de Billboard](https://www.billboard.com/charts/hot-100)")
    st.markdown("[Los mejores álbumes del año](https://pitchfork.com/)")
    st.markdown("[Festivales de música alrededor del mundo](https://www.musicfestivalwizard.com/)")
    st.markdown("[Historia del rock y pop](https://www.rollingstone.com/)")

def restaurantes():
    st.title("Guía de Restaurantes")
    st.image("https://source.unsplash.com/random/800x400?food")
    st.write("Los mejores lugares para disfrutar de una buena comida, desde cocina gourmet hasta comida rápida.")
    st.markdown("[Los 50 mejores restaurantes del mundo](https://www.theworlds50best.com/)")
    st.markdown("[Dónde comer en tu ciudad](https://www.yelp.com/)")
    st.markdown("[Cocina callejera recomendada](https://www.eater.com/)")
    st.markdown("[Reseñas de restaurantes](https://www.tripadvisor.com/Restaurants)")

def recetas():
    st.title("Recetas Fáciles y Deliciosas")
    st.image("https://source.unsplash.com/random/800x400?cooking")
    st.write("Aprende a cocinar platos sencillos con ingredientes accesibles.")
    st.markdown("[Recetas rápidas y saludables](https://www.allrecipes.com/)")
    st.markdown("[Platos vegetarianos fáciles](https://www.vegetariantimes.com/)")
    st.markdown("[Postres irresistibles](https://www.delish.com/cooking/recipe-ideas/)")
    st.markdown("[Cocina internacional en casa](https://www.saveur.com/)")

def naturaleza():
    st.title("Conexión con la Naturaleza")
    st.image("https://source.unsplash.com/random/800x400?nature")
    st.write("Explora destinos naturales, actividades al aire libre y consejos para cuidar el medio ambiente.")
    st.markdown("[Los mejores parques nacionales](https://www.nps.gov/index.htm)")
    st.markdown("[Senderismo y trekking](https://www.alltrails.com/)")
    st.markdown("[Cómo reducir tu huella ecológica](https://www.earthday.org/)")
    st.markdown("[Destinos ecoturísticos](https://www.ecotourism.org/)")

if __name__ == "__main__":
    main()
