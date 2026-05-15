# 📚 Sistema de Biblioteca (POO)

Este proyecto implementa un sistema de biblioteca utilizando **Programación Orientada a Objetos (POO)**.  
El objetivo es modelar entidades relacionadas entre sí y mostrar cómo interactúan mediante objetos, métodos y relaciones.

---

## 🔹 Entidades principales
- **Autor**: puede tener varios libros asociados.  
- **Libro**: pertenece a un autor y puede ser prestado.  
- **Usuario**: puede realizar múltiples préstamos.  
- **Préstamo**: vincula un usuario con un libro en un período de tiempo.  

---

## 🔹 Características implementadas
- Encapsulamiento de atributos.  
- Constructores para inicializar objetos.  
- Métodos para relacionar entidades (`addBook`, `borrowBook`).  
- Organización modular del código en carpetas.  
- Persistencia simple en archivo (`FileHelper`).  
- Prueba de uso en consola (`main.py` o `Main.java`).  
- Tests unitarios (`LibraryTest`).  

---

## 🔹 Organización del proyecto
LibrarySystem/
├── model/          # Clases principales (Book, Author, User, Loan)
├── service/        # Lógica de negocio (LibraryService)
├── app/            # Punto de entrada (main.py / Main.java)
├── util/           # Persistencia simple en archivo (FileHelper)
├── test/           # Pruebas unitarias
├── data/           # Archivos de ejemplo (books.txt)
└── README.md


---

## 🔹 Cómo ejecutar

### Python
Desde la carpeta raíz:
```bash
python app/main.py
