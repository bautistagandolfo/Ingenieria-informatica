package ejercicio01_fiuba;

import java.util.List;

public class Carrera {

    private String nombre;
    private int creditosMinimos;
    private List<Materia> materias;

    public Carrera (String nombre, int creditosMinimos, List <Materia> materias) {
        this.nombre = nombre;
        this.creditosMinimos = creditosMinimos;
        this.materias = materias;
    }

    public boolean equals(Object obj){
        if (this == obj){
            return true;
        }

        if (obj == null || getClass() != obj.getClass()) {
            return false;
        }
        Carrera otraCarrera = (Carrera) obj;

        return this.nombre == otraCarrera.nombre;
    }
    public String getNombre() {
        return this.nombre;
    }
    public int getCreditosMinimos() {
        return this.creditosMinimos;
    }

    public List<Materia> getMaterias() {
        return this.materias;
    }

    public void agregarMateria(Materia m) {
        boolean esta = false;
        for (Materia materia : materias) {
            if (materia.getCodigo() == m.getCodigo()){
                esta = true;
            }
        }

        if (!esta){
            this.materias.add(m);
        }
    }

    public boolean estaGraduado(List<Materia> aprobadasAlumno) {
        for (Materia materia : materias){
            boolean elAlumnoLaTiene = false;
            for (Materia materiaAlumno : aprobadasAlumno){
                if (materia.getCodigo() == materiaAlumno.getCodigo()){
                    elAlumnoLaTiene = true;
                    break;
                }
            }


            if (materia.isObligatoria() && !elAlumnoLaTiene){
                return false;
            }
        }


        return calcularCreditosObtenidos(aprobadasAlumno) >= this.creditosMinimos;
    }

    public int calcularCreditosObtenidos(List<Materia> aprobadasAlumno){
        int total = 0;
        for (Materia materia : aprobadasAlumno){
            if (this.materias.contains(materia)){
                total += materia.getCreditos();
            }
        }

        return total;
    }
}
