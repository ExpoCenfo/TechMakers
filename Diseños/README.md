# **Prototipo**

## **Control del Juego Interactivo**

### **Descripción de la Pieza**
El control del juego interactivo es una de las piezas clave en nuestro proyecto. Ha sido diseñado pensando en la usabilidad para niños, con un enfoque en la seguridad y la interactividad.

### **Componentes Principales**
1. **Caja de Acrílico Transparente:**
   - **Propósito:** La caja de acrílico permite a los usuarios visualizar los componentes internos del control, lo cual es particularmente útil en un contexto educativo. Los niños pueden observar cómo funcionan los circuitos y conexiones, brindando una experiencia de aprendizaje más rica.
   - **Diseño:** La caja es resistente y segura, asegurando que los componentes internos estén protegidos mientras se mantienen visibles.

2. **Borde Impreso en 3D:**
   - **Propósito:** El borde de la caja está impreso en 3D y sirve para asegurar la estructura de acrílico. Además, proporciona un agarre cómodo y seguro para las manos pequeñas de los niños.
   - **Importancia:** Este borde no solo refuerza la caja, sino que también contribuye a la ergonomía del control, asegurando que los niños puedan manipularlo fácilmente sin riesgos.

3. **Joystick:**
   - **Propósito:** El joystick permite a los jugadores mover el robot a través de la alfombra interactiva, controlando su dirección en tiempo real.
   - **Importancia:** Este componente es crucial para la interacción del juego, permitiendo que los niños participen activamente en la resolución de los desafíos en la alfombra.

4. **Placa Ideaboard (Emisora):**
   - **Propósito:** Esta placa es responsable de transmitir las señales del joystick al robot en la alfombra mediante la comunicación ESPNOW.
   - **Importancia:** La placa Ideaboard actúa como el cerebro del control, enviando los comandos del jugador al robot para que realice las acciones deseadas.

### **Utilidad e Importancia del Control**
El control ha sido diseñado para ser intuitivo y accesible para niños. A través de este dispositivo, los jugadores pueden interactuar con la alfombra y el robot, tomando decisiones en tiempo real durante el juego. La transparencia de la caja de acrílico permite que los niños se familiaricen con los componentes electrónicos, promoviendo el interés en la tecnología y la ingeniería desde una edad temprana.

### **Diseño Inspirado en Niños**
El control fue creado con un enfoque especial en la experiencia infantil. Los colores, la forma y los materiales utilizados están pensados para ser atractivos y seguros para los niños, fomentando un entorno de juego educativo y divertido.

### **Imagen del Control**
<p align="center">
  <img src="https://github.com/ExpoCenfo/TechMakers/blob/main/Img/1.jpg" alt="Imagen del Control" width="30%" />
  <img src="https://github.com/ExpoCenfo/TechMakers/blob/main/Img/9.png" alt="Imagen 3" width="30%" />
</p>


## **Receptor del Juego Interactivo - El Carro**

### **Descripción del Receptor**
El carro es el encargado de recorrer el tablero interactiva durante el juego. Su diseño se basa en el SumoBot de la Universidad Cenfotec, desarrollado por el Dr. Tomás de Camino Beck. Aunque su inspiración proviene de este modelo, hemos realizado modificaciones específicas para adaptarlo a las necesidades de nuestro proyecto.
![Ilustración 1](https://github.com/ExpoCenfo/TechMakers/blob/main/Img/7.jpg)
### **Modificaciones Realizadas**
- **Parte Inferior del Carro:**
  - Hemos realizado modificaciones en la parte inferior del carro para integrar un lector RFID. Este lector es esencial para la interacción con las tarjetas (stickers) colocadas en la alfombra.
  
- **Integración del RFID:**
  - **Funcionalidad:** Al pasar por las tarjetas, el RFID se activa y permite desbloquear los niveles del juego. En cada nivel, los niños leerán un desafío que deben resolver, lo que añade una capa educativa al juego.
  - **Prototipo:** Actualmente, este es un prototipo funcional que soporta un solo juego. Sin embargo, la visión a largo plazo es que esta plataforma pueda evolucionar para ofrecer reportes de avances y logros de cada niño, accesibles para los padres.
  - ![Sensor RFID](https://github.com/ExpoCenfo/TechMakers/blob/main/Img/6.jpeg)

### **Futuras Implementaciones**
- **Reporte de Avances:**
  - El objetivo es que en futuras versiones del juego, los padres puedan acceder a reportes detallados de los avances y logros de sus hijos, lo que permitiría un seguimiento más cercano del proceso educativo y lúdico.

### **Imagen del Carro**
![Imagen del Carro](https://github.com/ExpoCenfo/TechMakers/blob/main/Img/4.jpg)



