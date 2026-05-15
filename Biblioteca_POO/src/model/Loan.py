package model;

public class Usuario {
    private String id;
    private String nombre;

    public Usuario(String id, String nombre) {
        setId(id);
        setNombre(nombre);
    }

    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = validarTexto(id, "El id del usuario no puede estar vacio");
    }

    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = validarTexto(nombre, "El nombre del usuario no puede estar vacio");
    }

    private String validarTexto(String valor, String mensaje) {
        if (valor == null || valor.isBlank()) {
            throw new IllegalArgumentException(mensaje);
        }
        return valor.trim();
    }

    @Override
    public String toString() {
        return "Usuario{id='" + id + "', nombre='" + nombre + "'}";
    }
}
