# Módulo de Gestión de Inventario y Alertas de Stock Bajo

**Asignatura:** 2626-UEA-L-UFPTI-011-B  
**Grupo:** N° 14  
**Integrantes:** 
Michael Jose Bagui Muñoz, Kenneth Rafael Guerrero Rojas, David Leonel Suarez Suarez.

## 📌 Descripción del Módulo
Este módulo atiende los requerimientos **RF-02**, **RF-03** y **RF-06** del SRS:
1. Registrar productos con sus umbrales de stock mínimo.
2. Actualizar existencias de forma segura (previene stocks negativos).
3. Monitorear y generar alertas automáticas cuando el stock sea menor o igual al umbral mínimo.

---

## 🔀 Flujo de Trabajo con Ramas (GitHub Flow)
Usamos el flujo **GitHub Flow**:
- `main`: Rama principal siempre estable y lista para producción.
- `feature/nombre-tarea`: Ramas de trabajo temporales para nuevas funcionalidades.

### Comandos para colaborar:
1. Crear una rama: `git checkout -b feature/nombre-funcionalidad`
2. Guardar cambios: `git commit -m "Mensaje descriptivo del cambio"`
3. Subir rama: `git push origin feature/nombre-funcionalidad`
4. Abrir **Pull Request (PR)** hacia `main` y verificar que el CI pase con check verde (✔).