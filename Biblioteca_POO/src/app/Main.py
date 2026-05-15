package app;

import model.Autor;
import model.Libro;
import model.Usuario;
import service.BibliotecaService;

public class Main {
    public static void main(String[] args) {
        BibliotecaService biblioteca = new BibliotecaService();

        Autor autor = new Autor("Gabriel Garcia Marquez", "Colombia");
        Libro libro = new Libro("9780307474728", "Cien anos de soledad", autor);
        Usuario usuario = new Usuario("U001", "Ana");

        biblioteca.agregarLibro(libro);
        biblioteca.prestarLibro(libro.getIsbn(), usuario);
        biblioteca.devolverLibro(libro.getIsbn());

        for (Libro item : biblioteca.listarLibros()) {
            System.out.println(item);
        }

        biblioteca.listarPrestamos().forEach(System.out::println);
    }
}
