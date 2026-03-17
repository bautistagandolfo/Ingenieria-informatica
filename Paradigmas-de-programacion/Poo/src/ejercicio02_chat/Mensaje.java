package ejercicio02_chat;

public class Mensaje {

    private String emisor;
    private String receptor;
    private String contenido;

    public Mensaje(String emisor, String receptor, String contenido){
        this.emisor = emisor;
        this.receptor = receptor;
        this.contenido = contenido;
    }

    public String getEmisor() {
        return this.emisor;
    }

    public String getReceptor() {
        return this.receptor;
    }

    public String getContenido() {
        return this.contenido;
    }
}
