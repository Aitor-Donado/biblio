**Objetivo**: Implementar un sistema de ventas online usando:

- **Herencia** (clases base y derivadas).
- **Encapsulamiento** (atributos/métodos protegidos/privados).
- **Abstracción** (clases/métodos abstractos).
- **Polimorfismo** (mismo método con comportamientos distintos).

---

### **Descripción del Problema**

Una tienda online vende productos de tres categorías:

1. **Electrónicos** (tienen garantía en meses).
2. **Ropa** (tienen talla y color).
3. **Alimentos** (tienen fecha de caducidad).

Todos los productos comparten:

- ID, nombre, precio, stock.
- Método **`mostrar_info()`** (abstracto, cada subclase lo implementa).
- Método **`aplicar_descuento()`** (polimorfismo, cada producto aplica descuentos distintos).

La tienda también maneja **usuarios**:

- **Clientes** (pueden comprar productos).
- **Administradores** (pueden añadir/eliminar productos).

---

### **Requisitos**

1. **Clase abstracta `Producto`**:
    - Atributos: **`_id`**, **`_nombre`**, **`_precio`**, **`_stock`** (encapsulados).
    - Método abstracto **`mostrar_info()`**.
    - Método **`aplicar_descuento(porcentaje)`** (default: 5%).
2. **Subclases de `Producto`**:
    - **`Electronico`**: Añade **`_garantia_meses`**. Descuento fijo adicional del 10%.
    - **`Ropa`**: Añade **`_talla`**, **`_color`**. Descuento máximo del 20%.
    - **`Alimento`**: Añade **`_fecha_caducidad`**. No aplica descuentos.
3. **Clase `Usuario`**:
    - Atributos: **`_id`**, **`_nombre`**, **`_email`** (encapsulados).
4. **Subclases de `Usuario`**:
    - **`Cliente`**: Método **`comprar_producto(producto, cantidad)`**.
    - **`Administrador`**: Método **`agregar_producto(inventario, producto)`**.
5. **Polimorfismo**:
    - **`aplicar_descuento()`** se comporta distinto en cada producto.

### **Ejercicio: Sistema de Ventas Online con POO**

**Objetivo**: Implementar un sistema de ventas online usando:

- **Herencia** (clases base y derivadas).
- **Encapsulamiento** (atributos/métodos protegidos/privados).
- **Abstracción** (clases/métodos abstractos).
- **Polimorfismo** (mismo método con comportamientos distintos).

---

### **Descripción del Problema**

Una tienda online vende productos de tres categorías:

1. **Electrónicos** (tienen garantía en meses).
2. **Ropa** (tienen talla y color).
3. **Alimentos** (tienen fecha de caducidad).

Todos los productos comparten:

- ID, nombre, precio, stock.
- Método `mostrar_info()` (abstracto, cada subclase lo implementa).
- Método `aplicar_descuento()` (polimorfismo, cada producto aplica descuentos distintos).

La tienda también maneja **usuarios**:

- **Clientes** (pueden comprar productos).
- **Administradores** (pueden añadir/eliminar productos).

---

### **Requisitos**

1. **Clase abstracta `Producto`**:
    - Atributos: `_id`, `_nombre`, `_precio`, `_stock` (encapsulados).
    - Método abstracto `mostrar_info()`.
    - Método `aplicar_descuento(porcentaje)` (default: 5%).
2. **Subclases de `Producto`**:
    - `Electronico`: Añade `_garantia_meses`. Descuento fijo adicional del 10%.
    - `Ropa`: Añade `_talla`, `_color`. Descuento máximo del 20%.
    - `Alimento`: Añade `_fecha_caducidad`. No aplica descuentos.
3. **Clase `Usuario`**:
    - Atributos: `_id`, `_nombre`, `_email` (encapsulados).
4. **Subclases de `Usuario`**:
    - `Cliente`: Método `comprar_producto(producto, cantidad)`.
    - `Administrador`: Método `agregar_producto(inventario, producto)`.
5. **Polimorfismo**:
    - `aplicar_descuento()` se comporta distinto en cada producto.



---

### **Preguntas/Extensiones (para evaluar)**

1. **Encapsulamiento**: ¿Por qué `__garantia_meses` en `Electronico` es privado?
2. **Polimorfismo**: ¿Cómo se comporta `aplicar_descuento()` en cada subclase?
3. **Abstracción**: ¿Qué pasa si no se implementa `mostrar_info()` en una subclase?
4. **Herencia**: ¿Cómo reutiliza `Ropa` los atributos de `Producto`?

**Respuestas**:

1. Porque solo la clase `Electronico` debe gestionar la garantía.
2. En `Electronico` añade 10% extra, en `Ropa` limita el descuento, y en `Alimento` no hace nada.
3. Error, porque es un método abstracto.
4. Usando `super().__init__()` para heredar `id`, `nombre`, etc.
