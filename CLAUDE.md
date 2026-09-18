# Marea Creativa — contexto inicial

Notas de arranque de este proyecto (17 de septiembre de 2026), para no perder contexto entre sesiones.

## Qué es Marea Creativa
Agencia de publicidad para pequeños negocios y emprendedores, con base en **Panguipulli** — trabajan con negocios en todo Chile. Marea Creativa gestiona campañas para negocios reales: profesionales independientes, técnicos, agentes de seguros, comercios, servicios para el hogar y emprendedores que viven de lo que hacen.

**Servicios (confirmados por el material de marca del 17 de septiembre):**
- Meta Ads (Facebook e Instagram)
- Google Ads (Búsqueda y PMax)
- Embudos y automatizaciones
- Estrategia orientada a resultados

**Propuesta central:** no hace falta ser una gran empresa ni tener presupuestos enormes para empezar a hacer publicidad. El punto de partida siempre es entender el negocio del cliente antes de armar campañas:
- ¿Qué vendes?
- ¿Cuántos clientes necesitas?
- ¿Cuánto puedes invertir?
- ¿Qué tendría que ocurrir para que la publicidad tenga sentido para ti?

A partir de esas respuestas se crean y administran las campañas.

**Idea clave de posicionamiento:** no todos los negocios necesitan cientos de clientes — necesitan los suficientes para alcanzar sus propios objetivos. Ejemplos usados para ilustrar esto:
- Una podóloga: crecer puede significar llenar dos días de agenda.
- Alguien que fabrica portones: conseguir suficientes cotizaciones para mantener trabajo durante el mes.
- Un profesional independiente: conseguir los clientes necesarios para vivir bien de su actividad.

**Nombre y tagline:** 🌊 Marea Creativa — "Marketing que mueve negocios." Línea de servicios en el logo: "Estrategia • Anuncios • Resultados". Frases de campaña ya usadas en material de marca: "Convertimos tu inversión en oportunidades", "Tu negocio en buenas manos".

## Identidad visual (definida el 17 de septiembre de 2026)
- **Logo:** ola estilizada en degradé (celeste claro → turquesa → azul marino oscuro) sobre fondo blanco, con "MAREA CREATIVA" en tipografía sans bold (negro/azul marino) y "CREATIVA" en turquesa. Debajo: "Marketing que mueve negocios" y "Estrategia • Anuncios • Resultados" separados por puntos.
- **Paleta:** azul marino oscuro (texto/fondo principal, tipo #0a1e3d), turquesa/celeste (acento, tipo #1a7a9e — el mismo espíritu que el verde azulado de Seguros pero en clave azul), blanco.
- **Imaginería de referencia:** foto del lago/volcán de Panguipulli como fondo de banners, combinada con foto de profesional trabajando en laptop y tarjetas de métricas superpuestas (ej. "Conversaciones +62%", "Clientes potenciales +286%") — comunica resultados concretos + arraigo local.
- **Pendiente:** guardar los archivos reales del logo y banner de referencia en `assets/` dentro de este proyecto — llegaron pegados en el chat, sin ruta de archivo accesible; pedir a Danny que los copie a `/Users/danny/Marea Creativa/assets/`.

## Nota de idioma
Español neutro/chileno estándar (tú), sin acentos ni voseo argentino, consistente con el resto de los proyectos de Danny.

## Relación con los otros negocios de Danny
Este es un frente de negocio nuevo y separado de los demás proyectos de Danny (ver `~/DannyMeraSeguros`, `~/negocio autos`, `~/RadarComercial`). Danny mantiene cada negocio en su propia carpeta a propósito, para no dispersar el foco. Marea Creativa es, en sí misma, un servicio de publicidad — podría eventualmente vender campañas a los otros negocios de Danny como clientes, pero es un proyecto independiente con su propia identidad de marca.

## Estrategia de contenido (definida el 17 de septiembre de 2026)
El objetivo es conseguir clientes para la agencia (no enseñarles marketing) — conectar con sus dolores y anhelos antes que educarlos. Pilares de contenido acordados:
1. **Contenido "espejo"** — nombra el dolor específico del dueño de negocio (agenda floja, ansiedad de fin de mes, ver a la competencia "movida") sin enseñar nada, solo generar el "esto me lo escribieron a mí".
2. **Historias reales antes/después**, anonimizadas (mismo modelo que los casos de devolución en Seguros).
3. **Desmontar creencias limitantes con empatía** — validar la frustración antes de explicar, nunca en tono de clase.
4. **Detrás de cámara** — mostrar el proceso real de diagnóstico de Marea Creativa, para diferenciarse de "otra agencia con paquetes genéricos".
5. **Contenido aspiracional** — vender la meta modesta y específica (llenar la agenda, un fin de mes sin ansiedad), no crecimiento genérico.
6. **Resultados reales**, aunque sean chicos — screenshots de campañas, cifras concretas, mensajes de agradecimiento.

Tono: conversacional, con oficios reales (podóloga, el que hace portones), nunca "somos expertos en marketing digital".

**Duración de guiones de video (investigado el 17 de septiembre de 2026):** el algoritmo premia tasa de finalización sobre duración exacta, pero hay rangos que funcionan mejor por formato:
- **Hablado a cámara:** 30-45 segundos.
- **Voz en off:** 45-60 segundos (permite narrar sobre visuales/texto en pantalla sin sentirse largo).
- Estructura de guión en ambos casos: hook en los primeros 3 segundos → desarrollo del mensaje central → CTA claro al cierre (comentar, guardar, o escribir por DM).

## Pendiente / por definir
- **Construir el sitio + motor de contenido** (acordado el 17 de septiembre, aún no implementado): un banco de contenido con los pilares de arriba, del cual se generen carruseles diarios (reutilizando `generate_carousel.py` de Radar Comercial/Seguros, con la paleta azul marino/turquesa de Marea Creativa) y guiones de video (hablado a cámara y voz en off) según los parámetros de duración ya definidos. A diferencia de Seguros/Radar Comercial, acá no hay "noticia del día" que investigar — el motor rota ángulos de un banco de contenido evergreen, no despachos diarios verificables.
- Guardar los archivos reales del logo/banner en `assets/` (ver sección de Identidad visual).
- Oferta de servicio concreta: precios, qué incluye la gestión de campañas, proceso de onboarding de un cliente nuevo.

## Cómo seguir
Al abrir una sesión de Claude Code en esta carpeta, este archivo da el contexto — se puede pedir directamente "sigamos con Marea Creativa" y continuar desde acá.
