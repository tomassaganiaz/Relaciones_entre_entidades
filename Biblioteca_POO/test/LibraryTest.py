import model.Autor;
import model.Libro;
import model.Usuario;
import service.BibliotecaService;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;

public class BiblioteTest {
    public static void main(String[] args) throws IOException {
        BibliotecaService biblioteca = new BibliotecaService();
        Libro libro = new Libro("1", "El principito", new Autor("Antoine de Saint-Exupery", "Francia"));
        Usuario usuario = new Usuario("U1", "Luis");

        biblioteca.agregarLibro(libro);
        biblioteca.prestarLibro("1", usuario);

        if (libro.isDisponible()) {
            throw new AssertionError("El libro deberia quedar no disponible despues del prestamo");
        }

        biblioteca.devolverLibro("1");

        if (!libro.isDisponible()) {
            throw new AssertionError("El libro deberia quedar disponible despues de la devolucion");
        }

        if (biblioteca.buscarLibroPorIsbn("1") == null) {
            throw new AssertionError("El libro deberia encontrarse por ISBN");
        }

        assertThrows(() -> biblioteca.agregarLibro(
                new Libro("1", "Otro libro", new Autor("Autor repetido", "Argentina"))),
                "Deberia fallar al agregar un ISBN duplicado");

        biblioteca.prestarLibro("1", usuario);
        assertThrows(() -> biblioteca.prestarLibro("1", usuario),
                "Deberia fallar al prestar un libro que ya no esta disponible");
        biblioteca.devolverLibro("1");

        Path archivoTemporal = Files.createTempFile("biblioteca", ".txt");
        try {
            biblioteca.guardarLibros(archivoTemporal.toString());

            BibliotecaService bibliotecaRecargada = new BibliotecaService();
            bibliotecaRecargada.cargarLibros(archivoTemporal.toString());

            Libro libroRecargado = bibliotecaRecargada.buscarLibroPorIsbn("1");
            if (libroRecargado == null) {
                throw new AssertionError("El libro deberia existir despues de cargar desde archivo");
            }
            if (!libroRecargado.isDisponible()) {
                throw new AssertionError("El libro cargado deberia quedar disponible");
            }
            if (!bibliotecaRecargada.listarPrestamos().isEmpty()) {
                throw new AssertionError("Los prestamos deberian reiniciarse al recargar libros");
            }
        } finally {
            Files.deleteIfExists(archivoTemporal);
        }

        System.out.println("Pruebas basicas y validaciones OK");
    }

    private static void assertThrows(Runnable accion, String mensaje) {
        try {
            accion.run();
            throw new AssertionError(mensaje);
        } catch (IllegalArgumentException | IllegalStateException expected) {
            // Excepcion esperada.
        }
    }
}
