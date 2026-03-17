package ejercicio02_chat;

import java.util.ArrayList;
import java.util.List;

public class aplicacionChat {
    private List<Conversacion> todasLasConversas;

    public aplicacionChat() {
        this.todasLasConversas = new ArrayList<>();
    }

    // Este es el método principal que llama el usuario
    public void enviarMensaje(String emisor, String receptor, String texto) {
        // 1. Buscamos si ya existe el "cajón" para estos dos
        Conversacion conversa = buscarConversacion(emisor, receptor);

        // 2. Si no existe (es null), lo creamos y lo guardamos en la lista global
        if (conversa == null) {
            conversa = new Conversacion(emisor, receptor);
            todasLasConversas.add(conversa);
        }

        // 3. Ahora que estamos seguros de que el cajón existe, creamos el mensaje y lo metemos
        Mensaje nuevo = new Mensaje(emisor, receptor, texto);
        conversa.agregarMensaje(nuevo);
    }

    // El "buscador" que usa el boolean que diseñamos en la otra clase
    private Conversacion buscarConversacion(String u1, String u2) {
        for (Conversacion c : todasLasConversas) {
            if (c.perteneceA(u1, u2)) {
                return c; // Encontró el chat correcto
            }
        }
        return null; // No existe chat previo entre ellos
    }
}
