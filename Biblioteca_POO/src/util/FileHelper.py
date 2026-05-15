package util;

import model.Autor;
import model.Libro;

import java.io.IOException;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.List;

public class ArchivoHelper {
    private ArchivoHelper() {
    }

    public static void guardarLibros(String ruta, List<Libro> libros) throws IOException {
        if (ruta == null || ruta.isBlank()) {
            throw new IllegalArgumentException("La ruta no puede estar vacia");
        }
        if (libros == null) {
            throw new IllegalArgumentException("La lista de libros no puede ser nula");
        }

        Path path = Paths.get(ruta);
        if (path.getParent() != null) {
            Files.createDirectories(path.getParent());
        }

        List<String> lineas = new ArrayList<>();
        for (Libro libro : libros) {
            lineas.add(formatearCampo(libro.getIsbn()) + ";" + formatearCampo(libro.getTitulo()) + ";"
                    + formatearCampo(libro.getAutor().getNombre()) + ";"
                    + formatearCampo(libro.getAutor().getNacionalidad()));
        }

        Files.write(path, lineas, StandardCharsets.UTF_8);
    }

    public static List<Libro> cargarLibros(String ruta) throws IOException {
        if (ruta == null || ruta.isBlank()) {
            throw new IllegalArgumentException("La ruta no puede estar vacia");
        }

        Path path = Paths.get(ruta);
        List<Libro> libros = new ArrayList<>();

        if (!Files.exists(path)) {
            return libros;
        }

        for (String linea : Files.readAllLines(path, StandardCharsets.UTF_8)) {
            if (linea == null || linea.isBlank()) {
                continue;
            }

            String[] partes = linea.split(";", -1);
            if (partes.length < 4) {
                continue;
            }

            try {
                Autor autor = new Autor(partes[2], partes[3]);
                libros.add(new Libro(partes[0], partes[1], autor));
            } catch (IllegalArgumentException ignored) {
                // Se omiten lineas invalidas para no romper toda la carga.
            }
        }

        return libros;
    }

    private static String formatearCampo(String valor) {
        return valor.replace(";", ",").trim();
    }
}
