class_name LocaleData

## Static translation data for UI strings.
## Separated from locale.gd to keep logic and data apart.

const LOCALE_NAMES: Dictionary = {
	"de": "Deutsch",
	"en": "English",
	"fr": "Français",
	"es": "Español",
	"it": "Italiano",
}

# Translation table: KEY → { locale_code: text }
const TRANSLATIONS: Dictionary = {
	# ── Title Screen ──
	"TITLE": {
		"de": "Die Stille von Graubach",
		"en": "The Silence of Graubach",
		"fr": "Le Silence de Graubach",
		"es": "El Silencio de Graubach",
		"it": "Il Silenzio di Graubach",
	},
	"TITLE_SUBTITLE": {
		"de": "Schwarzwald, November 1923",
		"en": "Black Forest, November 1923",
		"fr": "Forêt-Noire, novembre 1923",
		"es": "Selva Negra, noviembre de 1923",
		"it": "Foresta Nera, novembre 1923",
	},
	"NEW_GAME": {
		"de": "Neues Spiel",
		"en": "New Game",
		"fr": "Nouvelle partie",
		"es": "Nueva partida",
		"it": "Nuova partita",
	},
	"CONTINUE": {
		"de": "Fortsetzen",
		"en": "Continue",
		"fr": "Continuer",
		"es": "Continuar",
		"it": "Continua",
	},
	"LOAD": {
		"de": "Laden",
		"en": "Load",
		"fr": "Charger",
		"es": "Cargar",
		"it": "Carica",
	},
	"SETTINGS": {
		"de": "Einstellungen",
		"en": "Settings",
		"fr": "Paramètres",
		"es": "Ajustes",
		"it": "Impostazioni",
	},
	"QUIT": {
		"de": "Beenden",
		"en": "Quit",
		"fr": "Quitter",
		"es": "Salir",
		"it": "Esci",
	},

	"CREDITS": {
		"de": "Mitwirkende",
		"en": "Credits",
		"fr": "Crédits",
		"es": "Créditos",
		"it": "Crediti",
	},
	"CREDITS_TITLE": {
		"de": "Mitwirkende",
		"en": "Credits",
		"fr": "Crédits",
		"es": "Créditos",
		"it": "Crediti",
	},
	"CREDITS_ENGINE": {
		"de": "Spiel-Engine",
		"en": "Game Engine",
		"fr": "Moteur de jeu",
		"es": "Motor de juego",
		"it": "Motore di gioco",
	},
	"CREDITS_GRAPHICS": {
		"de": "Bildgenerierung",
		"en": "Image Generation",
		"fr": "Génération d'images",
		"es": "Generación de imágenes",
		"it": "Generazione immagini",
	},
	"CREDITS_SD_DESC": {
		"de": "Benutzeroberfläche für Stable Diffusion",
		"en": "User interface for Stable Diffusion",
		"fr": "Interface pour Stable Diffusion",
		"es": "Interfaz para Stable Diffusion",
		"it": "Interfaccia per Stable Diffusion",
	},
	"CREDITS_ANIMAGINE_DESC": {
		"de": "Charakter-Sprites (Oil-Painting-Stil)",
		"en": "Character sprites (oil painting style)",
		"fr": "Sprites de personnages (style peinture à l'huile)",
		"es": "Sprites de personajes (estilo óleo)",
		"it": "Sprite dei personaggi (stile pittura a olio)",
	},
	"CREDITS_JUGGER_DESC": {
		"de": "Hintergrundbilder",
		"en": "Background images",
		"fr": "Images d'arrière-plan",
		"es": "Imágenes de fondo",
		"it": "Immagini di sfondo",
	},
	"CREDITS_REMBG_DESC": {
		"de": "Hintergrundentfernung für Sprites",
		"en": "Background removal for sprites",
		"fr": "Suppression d'arrière-plan pour sprites",
		"es": "Eliminación de fondo para sprites",
		"it": "Rimozione sfondo per sprite",
	},
	"CREDITS_AUDIO": {
		"de": "Audio",
		"en": "Audio",
		"fr": "Audio",
		"es": "Audio",
		"it": "Audio",
	},
	"CREDITS_AUDIOCRAFT_DESC": {
		"de": "Musik- und Soundeffekt-Generierung (MusicGen + AudioGen)",
		"en": "Music and sound effect generation (MusicGen + AudioGen)",
		"fr": "Génération de musique et effets sonores (MusicGen + AudioGen)",
		"es": "Generación de música y efectos de sonido (MusicGen + AudioGen)",
		"it": "Generazione musica ed effetti sonori (MusicGen + AudioGen)",
	},
	"CREDITS_TOOLS": {
		"de": "Programmierung & Tools",
		"en": "Programming & Tools",
		"fr": "Programmation & outils",
		"es": "Programación y herramientas",
		"it": "Programmazione e strumenti",
	},
	"CREDITS_PYTHON_DESC": {
		"de": "Asset-Pipeline (Sprite-Generierung, Audio, Lokalisierung)",
		"en": "Asset pipeline (sprite generation, audio, localization)",
		"fr": "Pipeline d'assets (sprites, audio, localisation)",
		"es": "Pipeline de assets (sprites, audio, localización)",
		"it": "Pipeline asset (sprite, audio, localizzazione)",
	},
	"CREDITS_SCIPY_DESC": {
		"de": "Audio-Verarbeitung und Normalisierung",
		"en": "Audio processing and normalization",
		"fr": "Traitement et normalisation audio",
		"es": "Procesamiento y normalización de audio",
		"it": "Elaborazione e normalizzazione audio",
	},
	"CREDITS_FONTS": {
		"de": "Schriften",
		"en": "Fonts",
		"fr": "Polices",
		"es": "Fuentes",
		"it": "Font",
	},
	"CREDITS_FONTS_DESC": {
		"de": "Windows-Systemschriften",
		"en": "Windows system fonts",
		"fr": "Polices système Windows",
		"es": "Fuentes del sistema Windows",
		"it": "Font di sistema Windows",
	},
	"CREDITS_CREATED_BY": {
		"de": "Erstellt von",
		"en": "Created by",
		"fr": "Créé par",
		"es": "Creado por",
		"it": "Creato da",
	},

	# ── Settings Screen ──
	"SETTINGS_TITLE": {
		"de": "Einstellungen",
		"en": "Settings",
		"fr": "Paramètres",
		"es": "Ajustes",
		"it": "Impostazioni",
	},
	"AUDIO": {
		"de": "Audio",
		"en": "Audio",
		"fr": "Audio",
		"es": "Audio",
		"it": "Audio",
	},
	"MASTER_VOLUME": {
		"de": "Lautstärke",
		"en": "Volume",
		"fr": "Volume",
		"es": "Volumen",
		"it": "Volume",
	},
	"MUSIC": {
		"de": "Musik",
		"en": "Music",
		"fr": "Musique",
		"es": "Música",
		"it": "Musica",
	},
	"EFFECTS": {
		"de": "Effekte",
		"en": "Effects",
		"fr": "Effets",
		"es": "Efectos",
		"it": "Effetti",
	},
	"AMBIENCE": {
		"de": "Ambiente",
		"en": "Ambience",
		"fr": "Ambiance",
		"es": "Ambiente",
		"it": "Ambiente",
	},
	"TEXT": {
		"de": "Text",
		"en": "Text",
		"fr": "Texte",
		"es": "Texto",
		"it": "Testo",
	},
	"TEXT_SPEED": {
		"de": "Textgeschw.",
		"en": "Text Speed",
		"fr": "Vitesse",
		"es": "Velocidad",
		"it": "Velocità",
	},
	"FONT_SIZE": {
		"de": "Schriftgröße",
		"en": "Font Size",
		"fr": "Taille police",
		"es": "Tamaño fuente",
		"it": "Dim. carattere",
	},
	"AUTO_ADVANCE": {
		"de": "  Auto-Weiter (3 Sek.)",
		"en": "  Auto-Advance (3 sec.)",
		"fr": "  Avance auto (3 sec.)",
		"es": "  Avance auto (3 seg.)",
		"it": "  Avanzamento auto (3 sec.)",
	},
	"DISPLAY": {
		"de": "Anzeige",
		"en": "Display",
		"fr": "Affichage",
		"es": "Pantalla",
		"it": "Schermo",
	},
	"FULLSCREEN": {
		"de": "  Vollbild",
		"en": "  Fullscreen",
		"fr": "  Plein écran",
		"es": "  Pantalla completa",
		"it": "  Schermo intero",
	},
	"LANGUAGE": {
		"de": "Sprache",
		"en": "Language",
		"fr": "Langue",
		"es": "Idioma",
		"it": "Lingua",
	},
	"BACK": {
		"de": "Zurück",
		"en": "Back",
		"fr": "Retour",
		"es": "Volver",
		"it": "Indietro",
	},

	# ── Game Scene Quick Menu ──
	"SAVE": {
		"de": "Speichern",
		"en": "Save",
		"fr": "Sauvegarder",
		"es": "Guardar",
		"it": "Salva",
	},
	"LOAD_SHORT": {
		"de": "Laden",
		"en": "Load",
		"fr": "Charger",
		"es": "Cargar",
		"it": "Carica",
	},
	"HISTORY": {
		"de": "Verlauf",
		"en": "History",
		"fr": "Historique",
		"es": "Historial",
		"it": "Cronologia",
	},
	"JOURNAL": {
		"de": "Tagebuch",
		"en": "Journal",
		"fr": "Journal",
		"es": "Diario",
		"it": "Diario",
	},

	# ── Save/Load ──
	"SAVE_TITLE": {
		"de": "Speichern",
		"en": "Save Game",
		"fr": "Sauvegarder",
		"es": "Guardar partida",
		"it": "Salva partita",
	},
	"LOAD_TITLE": {
		"de": "Laden",
		"en": "Load Game",
		"fr": "Charger",
		"es": "Cargar partida",
		"it": "Carica partita",
	},
	"CLOSE": {
		"de": "Schließen",
		"en": "Close",
		"fr": "Fermer",
		"es": "Cerrar",
		"it": "Chiudi",
	},
	"SLOT_EMPTY": {
		"de": "Leer",
		"en": "Empty",
		"fr": "Vide",
		"es": "Vacío",
		"it": "Vuoto",
	},

	# ── History ──
	"HISTORY_TITLE": {
		"de": "Verlauf",
		"en": "History",
		"fr": "Historique",
		"es": "Historial",
		"it": "Cronologia",
	},

	# ── Journal ──
	"JOURNAL_TITLE": {
		"de": "Tagebuch",
		"en": "Journal",
		"fr": "Journal",
		"es": "Diario",
		"it": "Diario",
	},
	"NO_ENTRIES": {
		"de": "Noch keine Einträge.",
		"en": "No entries yet.",
		"fr": "Aucune entrée.",
		"es": "Sin entradas todavía.",
		"it": "Nessuna voce ancora.",
	},

	# ── Ending Screen ──
	"END_HEADER": {
		"de": "- ENDE -",
		"en": "- THE END -",
		"fr": "- FIN -",
		"es": "- FIN -",
		"it": "- FINE -",
	},
	"ENDINGS_DISCOVERED": {
		"de": "Enden entdeckt: %d / 6",
		"en": "Endings discovered: %d / 6",
		"fr": "Fins découvertes : %d / 6",
		"es": "Finales descubiertos: %d / 6",
		"it": "Finali scoperti: %d / 6",
	},
	"RETURN_TO_MENU": {
		"de": "Zum Hauptmenü",
		"en": "Return to Menu",
		"fr": "Menu principal",
		"es": "Menú principal",
		"it": "Menu principale",
	},

	# ── Ending: Seal ──
	"ENDING_SEAL_NAME": {
		"de": "Das Siegel",
		"en": "The Seal",
		"fr": "Le Sceau",
		"es": "El Sello",
		"it": "Il Sigillo",
	},
	"ENDING_SEAL_DESC": {
		"de": "Du hast Großmutters Ritual vollendet und die Entität gebunden.",
		"en": "You completed grandmother's ritual and bound the entity.",
		"fr": "Tu as accompli le rituel de grand-mère et lié l'entité.",
		"es": "Completaste el ritual de la abuela y ataste a la entidad.",
		"it": "Hai completato il rituale della nonna e vincolato l'entità.",
	},
	"ENDING_SEAL_TYPE": {
		"de": "Best",
		"en": "Best",
		"fr": "Meilleure",
		"es": "Mejor",
		"it": "Migliore",
	},

	# ── Ending: Escape ──
	"ENDING_ESCAPE_NAME": {
		"de": "Die Flucht",
		"en": "The Escape",
		"fr": "La Fuite",
		"es": "La Huida",
		"it": "La Fuga",
	},
	"ENDING_ESCAPE_DESC": {
		"de": "Georg opferte sich, damit du entkommen konntest. Das Dorf verschwand hinter dir.",
		"en": "Georg sacrificed himself so you could escape. The village vanished behind you.",
		"fr": "Georg s'est sacrifié pour que tu puisses fuir. Le village a disparu derrière toi.",
		"es": "Georg se sacrificó para que pudieras escapar. El pueblo desapareció tras de ti.",
		"it": "Georg si è sacrificato perché tu potessi fuggire. Il villaggio è svanito dietro di te.",
	},
	"ENDING_ESCAPE_TYPE": {
		"de": "Gut",
		"en": "Good",
		"fr": "Bon",
		"es": "Bueno",
		"it": "Buono",
	},

	# ── Ending: Pact ──
	"ENDING_PACT_NAME": {
		"de": "Der Pakt",
		"en": "The Pact",
		"fr": "Le Pacte",
		"es": "El Pacto",
		"it": "Il Patto",
	},
	"ENDING_PACT_DESC": {
		"de": "Du bist die neue Hüterin. Die Tradition lebt weiter.",
		"en": "You are the new guardian. The tradition lives on.",
		"fr": "Tu es la nouvelle gardienne. La tradition perdure.",
		"es": "Eres la nueva guardiana. La tradición continúa.",
		"it": "Sei la nuova guardiana. La tradizione continua.",
	},
	"ENDING_PACT_TYPE": {
		"de": "Ambivalent",
		"en": "Ambivalent",
		"fr": "Ambivalent",
		"es": "Ambivalente",
		"it": "Ambivalente",
	},

	# ── Ending: Awakening ──
	"ENDING_AWAKENING_NAME": {
		"de": "Das Erwachen",
		"en": "The Awakening",
		"fr": "L'Éveil",
		"es": "El Despertar",
		"it": "Il Risveglio",
	},
	"ENDING_AWAKENING_DESC": {
		"de": "Das Ritual scheiterte. Die Realität zerfiel um dich herum.",
		"en": "The ritual failed. Reality crumbled around you.",
		"fr": "Le rituel a échoué. La réalité s'est effondrée autour de toi.",
		"es": "El ritual fracasó. La realidad se desmoronó a tu alrededor.",
		"it": "Il rituale è fallito. La realtà si è sgretolata intorno a te.",
	},
	"ENDING_AWAKENING_TYPE": {
		"de": "Horror",
		"en": "Horror",
		"fr": "Horreur",
		"es": "Horror",
		"it": "Orrore",
	},

	# ── Ending: Truth ──
	"ENDING_TRUTH_NAME": {
		"de": "Die Wahrheit",
		"en": "The Truth",
		"fr": "La Vérité",
		"es": "La Verdad",
		"it": "La Verità",
	},
	"ENDING_TRUTH_DESC": {
		"de": "Du hast die volle Erkenntnis erlangt. Es gibt Hunderte solcher dünnen Stellen.",
		"en": "You gained full insight. There are hundreds of such thin places.",
		"fr": "Tu as atteint la pleine connaissance. Il existe des centaines de ces passages.",
		"es": "Alcanzaste la plena comprensión. Hay cientos de esos lugares delgados.",
		"it": "Hai raggiunto la piena conoscenza. Esistono centinaia di questi punti sottili.",
	},
	"ENDING_TRUTH_TYPE": {
		"de": "Kosmisch",
		"en": "Cosmic",
		"fr": "Cosmique",
		"es": "Cósmico",
		"it": "Cosmico",
	},

	# ── Ending: Sacrifice ──
	"ENDING_SACRIFICE_NAME": {
		"de": "Das Opfer",
		"en": "The Sacrifice",
		"fr": "Le Sacrifice",
		"es": "El Sacrificio",
		"it": "Il Sacrificio",
	},
	"ENDING_SACRIFICE_DESC": {
		"de": "Aus Liebe nahmst du Konrads Platz als Gefäß ein.",
		"en": "Out of love, you took Konrad's place as the vessel.",
		"fr": "Par amour, tu as pris la place de Konrad en tant que réceptacle.",
		"es": "Por amor, ocupaste el lugar de Konrad como recipiente.",
		"it": "Per amore, hai preso il posto di Konrad come ricettacolo.",
	},
	"ENDING_SACRIFICE_TYPE": {
		"de": "Tragisch",
		"en": "Tragic",
		"fr": "Tragique",
		"es": "Trágico",
		"it": "Tragico",
	},
}
