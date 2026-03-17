package ejercicio01_fiuba;

import java.util.ArrayList;
import java.util.List;

public class Usuario {

    private String nombre;
    private List<Carrera> carreras;
    private List<Materia> aprobadas;

    public Usuario (String nombre){
        this.nombre = nombre;
        this.aprobadas = new ArrayList<>();
        this.carreras = new ArrayList<>();
    }

    public String getNombre() {
        return this.nombre;
    }
    public List<Carrera> getCarreras() {
        return this.carreras;
    }

    public List<Materia> getMateriasAprobadas(){
        return this.aprobadas;
    }

    public void agregarCarrera(Carrera c){
        if (!this.carreras.contains(c)){
            this.carreras.add(c);
        }
    }

    public void agregarMateriaAprobada(Materia m){
        if (!this.aprobadas.contains(m)){
            this.aprobadas.add(m);
        }
    }

    public int consultarCreditos(Carrera c){
        return c.calcularCreditosObtenidos(this.aprobadas);
    }

    public boolean consultarEstadoGraduacion(Carrera c){
        return c.estaGraduado(this.aprobadas);
    }
}
