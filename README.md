# PetMatch  

¡Perfecto — vamos a profundizar en PetMatch! Voy a darte: visión general, lista de features (mínimo viable + extras), diseño de datos (modelos Django), endpoints de la API (DRF), estructura de frontend (Next.js), UX clave (swipes, filtros), split de tareas para 2 programadores junior, plan de sprints, ejemplos de código (modelos, serializers, endpoints y componentes Next.js), cómo desplegar y ideas de mejora para el portfolio. Todo en un formato práctico para que podáis empezar ya.

PetMatch — resumen

Idea: app tipo “Tinder” para adoptar o encontrar mascotas compatibles. Usuarios ven tarjetas con mascotas (foto, edad, tamaño, personalidad), deslizan (me gusta/no me interesa), y pueden hacer match con refugios o dueños si hay interés. Bucead en UX divertido + diseño limpio para destacar en el portfolio.

MVP (mínimo viable) — features clave

Registro / login (correo + contraseña, JWT).

Perfil de usuario simple (nombre, ubicación, preferencias de mascota).

CRUD de mascotas (para administradores/refugios): nombre, tipo, edad, tamaño, sexo, descripción, fotos, ubicación.

Feed de swipe: tarjetas con información básica + foto principal.

Acción swipe: like / pass.

Lista de matches / favoritos.

Página de detalle de mascota con botón "Contactar".

Búsqueda y filtros básicos (tipo, edad, tamaño, distancia aproximada).

Features opcionales (nice-to-have)

Chat entre usuario y refugio (mensajería básica).

Filtros por “casa ideal” (niños, mascotas, espacio exterior).

Verificación de refugio/usuario.

Recomendaciones basadas en preferencias (simple matching).

Compartir en redes sociales, añadir a favoritos persistentes.

Admin panel con métricas (nº likes, matches).

Stack tecnológico (recomendado)

Backend: Django + Django REST Framework (DRF), PostgreSQL, django-rest-framework-simplejwt para auth, django-storages + S3 (o storage local en desarrollo).

Frontend: Next.js (app/router o pages), React, TailwindCSS, SWR (o React Query) para fetching, react-tinder-card para swipe.

Despliegue: Vercel (Next.js) + Render / Railway / Heroku / Fly.io para Django + managed PostgreSQL.

Extras: Docker para desarrollo local, GitHub Actions para CI (tests).
