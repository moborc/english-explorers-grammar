# English Explorers – Grammar

Läs INSTALLATION.md. Ladda upp innehållet i webb-mappen till GitHub Pages. Ingen Supabase-konfiguration eller elevinloggning behövs.

Kontroller: kör `node tests/verify.cjs` från paketmappen. Testerna använder en liten DOM-adapter och verifierar funktioner; visuell layout behöver kontrolleras i webbläsare.

Grammar använder tillfällig fliklagring (sessionStorage). Frågor och bilder ingår. Redigera make_content.py och content_banks.py, och kör python3 make_content.py från paketmappen för att uppdatera webb/data.js. make_visuals.py återskapar SVG-bilderna. Webb/app.js och webb/styles.css är direkt redigerbara.
