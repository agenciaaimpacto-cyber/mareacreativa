# Marea Creativa — contexto inicial

Notas de arranque de este proyecto (17 de septiembre de 2026), para no perder contexto entre sesiones.

**Repositorio:** [github.com/agenciaaimpacto-cyber/mareacreativa](https://github.com/agenciaaimpacto-cyber/mareacreativa) (público, creado 2026-09-18).
**Sitio en vivo:** [marea-creativa.netlify.app](https://marea-creativa.netlify.app) (Netlify, deploy automático desde `main`, publicado 2026-09-18).

**Pendiente antes de que el sitio sea visible al público:** quedó con "Netlify visitor access" activado (redirige a un login de Netlify en vez de mostrar el sitio) — Danny tiene que desactivarlo en Site configuration → Sharing/Access control de este sitio específico en Netlify. Sin esto, nadie puede ver el sitio salvo quien tenga acceso a la cuenta Netlify.

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
- **Estado: hecho el 18 de septiembre de 2026.** Danny copió los archivos reales a la carpeta; quedaron como `assets/logo.png` y `assets/banner-referencia.png`.

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

## Sitio + motor de contenido (construido el 18 de septiembre de 2026)
Estructura del sitio, estática (HTML/CSS, sin build step, mismo esquema que Seguros/Radar Comercial):
- `index.html`, `servicios.html`, `casos.html`, `sobre-nosotros.html`, `contacto.html` — sitio público.
- `casos.html`: a propósito muestra un estado vacío honesto ("preferimos no inventar resultados") en vez de casos falsos — Marea Creativa recién está empezando y no hay clientes reales todavía. Se activa cuando exista el primer caso medible.
- `descargas.html` (no indexada, `noindex,nofollow`, sin link en el menú): página donde Danny descarga carruseles y guiones para publicar/grabar él mismo. Dos pestañas (Carruseles / Guiones), checkboxes "marcar como publicado/grabado" guardados en localStorage, botón de descarga por carrusel completo. Mismo patrón que `carruseles.html` en Seguros.
- `contenido/banco-contenido.md`: el banco de contenido evergreen (6 pilares: espejo, historias antes/después, mitos, detrás de cámara, aspiracional, resultados — ver sección de Estrategia de contenido arriba) con ángulos de ejemplo y lista de oficios para rotar. **Regla de honestidad explícita ahí:** ningún carrusel/guión puede presentar cifras o testimonios como reales hasta que existan de verdad (pilares 2 y 6 quedan "apagados" hasta el primer cliente real).
- `carrusel-tools/generate_carousel.py`: adaptado de Seguros/Radar Comercial, mismo formato de `slides.json` (tipos hook/text/stat/proof/cta, marcado `**palabra**` = resaltado), con paleta navy (#0B1F3A fondo) + cyan (#4FC3E0 acento) y marca "MAREA CREATIVA". Se corrigió un bug menor heredado del script original (una coma pegada a texto en negrita quedaba con un espacio de más — ej. "vendes ,").
- `guion-tools/generate_guion.py`: generador nuevo (no existía en ningún otro proyecto de Danny). Toma un JSON (formato, pilar, hook, desarrollo, cta, notas de producción) y genera un `.txt` con estructura Hook (primeros 3s) → Desarrollo → CTA, más la nota de formato correspondiente. Duración objetivo ya integrada: cámara 30-45s, voz en off 45-60s.
- `carruseles/2026-09-18/` y `guiones/2026-09-18/`: primer lote de ejemplo (3 carruseles — uno por pilar espejo/mitos/detrás de cámara — y 2 guiones, uno por formato) generado para aprobar el estilo antes de automatizar, mismo paso que se siguió en Seguros/Radar Comercial.
- Repo git local inicializado con un primer commit (`git init` + commit), pero **todavía no hay repo remoto en GitHub ni sitio en Netlify** — eso requiere que Danny decida/autorice ese paso (crear repo público, instalar la GitHub App con permiso de escritura, conectar Netlify), igual que se hizo para Seguros y Radar Comercial.

**Contacto real (confirmado el 18 de septiembre de 2026):** WhatsApp +56 9 4013 0088, Instagram [@mareacreativamkt](https://instagram.com/mareacreativamkt) — ya reemplazados en las 5 páginas del sitio.

## Pendiente / por definir
- **Crear el repo en GitHub + sitio en Netlify** y automatizar la rutina diaria (misma receta que Seguros/Radar Comercial, ver esa sección más abajo) — pendiente de decisión/autorización de Danny.
- Oferta de servicio concreta: precios, qué incluye la gestión de campañas, proceso de onboarding de un cliente nuevo.
- Activar los pilares 2 (historias antes/después) y 6 (resultados reales) del banco de contenido cuando exista el primer cliente con resultados medibles.

## Cómo seguir
Al abrir una sesión de Claude Code en esta carpeta, este archivo da el contexto — se puede pedir directamente "sigamos con Marea Creativa" y continuar desde acá.
