package ejercicio01_fiuba;

import java.util.ArrayList;

public class Main {
    public static void main(String[] args) {
        // 1. Creamos las Materias (codigo, nombre, creditos, obligatoria)
        Materia m1 = new Materia(1, "Analisis I", 10, true);
        Materia m2 = new Materia(2, "Algebra I", 8, true);
        Materia m3 = new Materia(3, "Algoritmos y Programacion I", 6, true);
        Materia m4 = new Materia(4, "Taller de Informatica", 4, false); // Optativa
        Materia m5 = new Materia(5, "Seminario de Etica", 2, false);   // Optativa

        // 2. Creamos la Carrera (Pide 24 creditos para recibirse)
        // Pasamos una lista vacía al principio para ir agregando con el método
        Carrera ingenieria = new Carrera("Ingenieria Informatica", 24, new ArrayList<>());
        ingenieria.agregarMateria(m1);
        ingenieria.agregarMateria(m2);
        ingenieria.agregarMateria(m3);
        ingenieria.agregarMateria(m4);
        ingenieria.agregarMateria(m5);

        // 3. Creamos al Usuario
        Usuario alumno = new Usuario("Charly");

        System.out.println("--- ESTADO INICIAL ---");
        verificarEstado(alumno, ingenieria);

        // 4. Simulamos avance: Aprueba Analisis y las dos optativas
        System.out.println("\n--- DESPUES DE ALGUNAS MATERIAS ---");
        alumno.agregarMateriaAprobada(m1); // 10 (Oblig)
        alumno.agregarMateriaAprobada(m4); // 4 (Opt)
        alumno.agregarMateriaAprobada(m5); // 2 (Opt)
        // Total: 16 creditos. Faltan obligatorias y creditos.
        verificarEstado(alumno, ingenieria);

        // 5. Caso critico: Tiene los creditos pero le falta una obligatoria
        System.out.println("\n--- CASO 'FALTA OBLIGATORIA' ---");
        alumno.agregarMateriaAprobada(m2); // 16 + 8 = 24 creditos.
        // ¡Ya tiene los 24! Pero le falta Algoritmos (m3) que es obligatoria.
        verificarEstado(alumno, ingenieria);

        // 6. Final feliz: Aprueba la ultima obligatoria
        System.out.println("\n--- FINAL FELIZ ---");
        alumno.agregarMateriaAprobada(m3); // Suma 6 mas = 30 creditos.
        verificarEstado(alumno, ingenieria);
    }

    // Metodo auxiliar para no repetir tantos System.out.println
    public static void verificarEstado(Usuario u, Carrera c) {
        System.out.println("Alumno: " + u.getNombre());
        System.out.println("Creditos en " + c.getNombre() + ": " + u.consultarCreditos(c));
        System.out.println("¿Esta Graduado?: " + (u.consultarEstadoGraduacion(c) ? "SI! 🎉" : "Todavia no... 📚"));
    }
}