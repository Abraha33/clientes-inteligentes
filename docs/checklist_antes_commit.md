# Checklist — Antes de hacer commit

Revisar cada punto antes de compartir el repositorio o hacer un commit.

## Datos sensibles

- [ ] No hay archivos `.xlsx`, `.xls`, `.csv`, `.ods` con datos reales.
- [ ] No hay archivos `.pdf`, `.html`, `.jsonl` con exportaciones reales.
- [ ] No hay archivos comprimidos (`.zip`, `.7z`, `.rar`) con datos internos.
- [ ] No hay NIT / CC / RUC / documentos reales.
- [ ] No hay teléfonos reales.
- [ ] No hay correos electrónicos reales.
- [ ] No hay direcciones exactas reales.
- [ ] No hay saldos reales de clientes.
- [ ] No hay historiales reales de compras.
- [ ] No hay coordenadas exactas de clientes reales.
- [ ] No hay datos fiscales o tributarios reales.

## Credenciales y secretos

- [ ] No hay credenciales de bases de datos.
- [ ] No hay tokens de API (Google Maps, Wappsi, etc.).
- [ ] No hay cookies ni claves privadas.
- [ ] No hay archivos `.env` o `credentials.txt`.
- [ ] No hay `secrets.json` ni archivos similares.
- [ ] No hay `cookies.json` ni `tokens.json`.

## Archivos de ejemplo

- [ ] Los archivos en `data/examples/` son completamente ficticios.
- [ ] Los ejemplos no contienen datos reales camuflados.
- [ ] Los nombres, teléfonos, correos y direcciones son inventados.
- [ ] Los teléfonos usan el prefijo ficticio `3000000000`.
- [ ] Los correos usan exclusivamente `@example.com`.
- [ ] Los documentos usan formato `DOC-DEMO-{N}`.

## Repositorio

- [ ] El repositorio es **público**: no debe contener datos reales.
- [ ] `data/raw/`, `data/manual/`, `data/processed/` y `data/private/` están en `.gitignore`.
- [ ] `git status` no muestra archivos dentro de `data/private/`.
- [ ] El `.gitignore` cubre formatos de exportación comunes (`.xlsx`, `.csv`, `.pdf`, etc.).

## Documentación

- [ ] Los ejemplos en `docs/modelo_datos.md` son ficticios.
- [ ] No se documentan clientes reales en la documentación pública.

## Verificación automatizada

- [ ] Ejecuté `python scripts/validate_no_sensitive_data.py` y no reportó errores.

## Verificación final

- [ ] Ejecuté `git status` para revisar archivos antes del commit.
- [ ] Revisé el diff para confirmar que no hay datos sensibles.
- [ ] Si hay dudas, no comiteo y consulto con el equipo.

---

> **Regla de oro:** Si no estás seguro de si un dato es sensible, trátalo como si lo fuera.
