package model;

public class Libro {
    private String isbn;
    private String titulo;
    private Autor autor;
    private boolean disponible;

    public Libro(String isbn, String titulo, Autor autor) {
        setIsbn(isbn);
        setTitulo(titulo);
        setAutor(autor);
        this.disponible = true;
    }

    public String getIsbn() {
        return isbn;
    }

    public void setIsbn(String isbn) {
        this.isbn = validarTexto(isbn, "El ISBN no puede estar vacio");
    }

    public String getTitulo() {
        return titulo;
    }

    public void setTitulo(String titulo) {
        this.titulo = validarTexto(titulo, "El titulo no puede estar vacio");
    }

    public Autor getAutor() {
        return autor;
    }

    public void setAutor(Autor autor) {
        if (autor == null) {
            throw new IllegalArgumentException("El autor no puede ser nulo");
        }
        this.autor = autor;
    }

    public boolean isDisponible() {
        return disponible;
    }

    public void setDisponible(boolean disponible) {
        this.disponible = disponible;
    }

    private String validarTexto(String valor, String mensaje) {
        if (valor == null || valor.isBlank()) {
            throw new IllegalArgumentException(mensaje);
        }
        return valor.trim();
    }

    @Override
    public String toString() {
        return "Libro{isbn='" + isbn + "', titulo='" + titulo + "', autor=" + autor
                + ", disponible=" + disponible + "}";
    }
}
