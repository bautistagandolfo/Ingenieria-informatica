package ejercicio02_chat;

import java.util.ArrayList;
import java.util.List;

public class Conversacion {
    private String involucrado1;
    private String involucrado2;
    private List<Mensaje> historialDeMensajes;

    // El constructor recibe a los dos que se van a hablar
    public Conversacion(String p1, String p2) {
        this.involucrado1 = p1;
        this.involucrado2 = p2;
        // Importante: inicializamos la lista aca para que no sea null
        this.historialDeMensajes = new ArrayList<>();
    }

    // El metodo que hablamos para guardar el objeto Mensaje completo
    public void agregarMensaje(Mensaje nuevoMensaje) {
        this.historialDeMensajes.add(nuevoMensaje);
    }

    // Este es el "filtro" que hablamos para encontrar el chat correcto
    public boolean perteneceA(String u1, String u2) {
        boolean opcionDirecta = involucrado1.equals(u1) && involucrado2.equals(u2);
        boolean opcionInvertida = involucrado1.equals(u2) && involucrado2.equals(u1);

        return opcionDirecta || opcionInvertida;
    }

    public List<Mensaje> getHistorialDeMensajes() {
        return historialDeMensajes;
    }
}