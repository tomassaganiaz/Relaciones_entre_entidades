package service;

import model.Libro;
import model.Prestamo;
import model.Usuario;
import util.ArchivoHelper;

import java.io.IOException;
import java.time.LocalDate;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class BibliotecaService {
    private final List<Libro> libros;
    private final List<Prestamo> prestamos;

    public BibliotecaService() {
        this.libros = new ArrayList<>();
        this.prestamos = new ArrayList<>();
    }

    public void agregarLibro(Libro libro) {
        if (libro == null) {
            throw new IllegalArgumentException("El libro no puede ser nulo");
        }

        if (buscarLibroPorIsbn(libro.getIsbn()) != null) {
            throw new IllegalArgumentException("Ya existe un libro con ese ISBN");
        }

        libros.add(libro);
    }

    public Libro buscarLibroPorIsbn(String isbn) {
        String isbnNormalizado = normalizarTexto(isbn, "El ISBN no puede estar vacio");

        for (Libro libro : libros) {
            if (libro.getIsbn().equalsIgnoreCase(isbnNormalizado)) {
                return libro;
            }
        }
        return null;
    }

    public List<Libro> listarLibros() {
        return Collections.unmodifiableList(libros);
    }

    public List<Prestamo> listarPrestamos() {
        return Collections.unmodifiableList(prestamos);
    }

    public Prestamo prestarLibro(String isbn, Usuario usuario) {
        if (usuario == null) {
            throw new IllegalArgumentException("El usuario no puede ser nulo");
        }

        Libro libro = buscarLibroPorIsbn(isbn);
        if (libro == null) {
            throw new IllegalArgumentException("No existe un libro con ese ISBN");
        }

        if (!libro.isDisponible()) {
            throw new IllegalStateException("El libro no esta disponible");
        }

        libro.setDisponible(false);
        Prestamo prestamo = new Prestamo(libro, usuario, LocalDate.now());
        prestamos.add(prestamo);
        return prestamo;
    }

    public void devolverLibro(String isbn) {
        Prestamo prestamoActivo = buscarPrestamoActivo(isbn);

        if (prestamoActivo == null) {
            throw new IllegalStateException("No hay un prestamo activo para ese libro");
        }

        prestamoActivo.registrarDevolucion(LocalDate.now());
        prestamoActivo.getLibro().setDisponible(true);
    }

    public void guardarLibros(String ruta) throws IOException {
        ArchivoHelper.guardarLibros(ruta, libros);
    }

    public void cargarLibros(String ruta) throws IOException {
        List<Libro> librosCargados = ArchivoHelper.cargarLibros(ruta);

        libros.clear();
        libros.addAll(librosCargados);

        // Como los prestamos no se persisten, se reinicia la disponibilidad para evitar
        // libros bloqueados despues de una recarga.
        for (Libro libro : libros) {
            libro.setDisponible(true);
        }
        prestamos.clear();
    }

    private Prestamo buscarPrestamoActivo(String isbn) {
        String isbnNormalizado = normalizarTexto(isbn, "El ISBN no puede estar vacio");

        for (Prestamo prestamo : prestamos) {
            if (prestamo.getLibro().getIsbn().equalsIgnoreCase(isbnNormalizado) && prestamo.estaActivo()) {
                return prestamo;
            }
        }
        return null;
    }

    private String normalizarTexto(String valor, String mensaje) {
        if (valor == null || valor.isBlank()) {
            throw new IllegalArgumentException(mensaje);
        }
        return valor.trim();
    }
}
