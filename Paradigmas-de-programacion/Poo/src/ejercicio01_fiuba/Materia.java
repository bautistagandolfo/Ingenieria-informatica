package ejercicio01_fiuba;

public class Materia {
    private int codigo;
    private String nombre;
    private int creditos;
    private boolean obligatoria;

    public Materia (int codigo, String nombre, int creditos, boolean obligatoria) {

        this.codigo = codigo;
        this.nombre = nombre;
        this.creditos = creditos;
        this.obligatoria = obligatoria;
    }

    public boolean equals(Object obj){
        if (this == obj){
            return true;
        }

        if (obj == null || getClass() != obj.getClass()) {
            return false;
        }
        Materia otraMateria = (Materia) obj;

        return this.codigo == otraMateria.codigo;
    }

    public int getCodigo() {
        return this.codigo;
    }

    public String getNombre() {
        return this.nombre;
    }

    public int getCreditos() {
        return this.creditos;
    }

    public boolean isObligatoria() {
        return this.obligatoria;
    }



}
