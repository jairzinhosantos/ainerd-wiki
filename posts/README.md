# Posts

Escritura corta que se publica en [jairzinhosantos.com/posts](https://jairzinhosantos.com/posts). Cada post es un archivo Markdown en esta carpeta; el sitio lo convierte en una página al construirse. No hay panel de administración: el editor es este repositorio.

## Escribir un post

1. Crea `posts/<slug>.md` (minúsculas, números y guiones, por ejemplo `por-que-cambie-mi-tesis.md`). Puedes copiar [`_template.md`](_template.md), que muestra todo lo que admite el motor, o desde el repo del sitio: `npm run post:new -- "Título"`.
2. Completa la cabecera:

   ```yaml
   ---
   title: Título del post
   date: 2026-11-06          # fecha de publicación, ordena la lista
   excerpt: Una o dos frases para la lista y la vista previa social.
   tag: Thesis               # opcional, un tema
   cover: covers/mi-post.png # opcional; relativo a posts/ o una URL https
   status: draft             # draft mientras escribes, published para salir
   updated: 2026-11-10       # opcional
   ---
   ```

3. Escribe el cuerpo en Markdown. Pon las imágenes, SVG, GIF y videos en `posts/media/<slug>/` y las portadas en `posts/covers/`. Un párrafo con solo una imagen se vuelve figura con pie (el `"título"` de la imagen). Un párrafo con solo una URL de YouTube se vuelve un video incrustado. Los bloques ```` ```mermaid ```` se dibujan como diagramas. Las notas al pie usan `[^1]`.
4. Previsualiza en local desde el repo del sitio, con los borradores incluidos:

   ```sh
   npm start          # http://localhost:4200
   npm run write      # vuelve a renderizar esta carpeta cada vez que guardas
   ```

   `npm run write` necesita la ruta de este checkout, como argumento o en `.env` (`AINERD_CONTENT_DIR`).
5. Cuando esté listo, cambia `status: published` y haz push a `main`. El workflow [`notify-site`](../.github/workflows/notify-site.yml) avisa al sitio, que regenera el contenido y Netlify publica en unos minutos.

## Reglas del motor

- Los archivos que no sean `<slug>.md` en minúsculas (este README, `_template.md`) se ignoran.
- `status: draft` nunca se publica, aunque esté en `main`.
- Las portadas PNG o JPG se usan también como imagen social; con SVG o sin portada el sitio genera una tarjeta automáticamente.
- Videos: `mp4`, `webm` o `mov` cortos (unos MB) van en `media/`; los largos, en YouTube.
