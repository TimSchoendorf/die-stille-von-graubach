#!/usr/bin/env python3
"""
Generate translation JSON files for Die Stille von Graubach.
Reads all German dialogue JSONs and produces data/translations/{en,fr,es,it}.json
with localized text for every dialogue, narration, choice, and journal node.

Usage: python scripts_locale/generate_translations.py
"""

import json
import os
import glob

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DIALOGUE_DIR = os.path.join(BASE_DIR, "data", "dialogue")
OUTPUT_DIR = os.path.join(BASE_DIR, "data", "translations")

# Character name translations
CHARACTER_NAMES = {
    "en": {
        "voss": "Pastor Voss",
        "otto": "Mayor",
        "margarethe": "Grandmother",
        "georg": "Georg",
        "elise": "Elise",
        "konrad": "Konrad",
        "hilde": "Hilde",
        "anna": "Anna",
    },
    "fr": {
        "voss": "Pasteur Voss",
        "otto": "Maire",
        "margarethe": "Grand-mère",
        "georg": "Georg",
        "elise": "Elise",
        "konrad": "Konrad",
        "hilde": "Hilde",
        "anna": "Anna",
    },
    "es": {
        "voss": "Pastor Voss",
        "otto": "Alcalde",
        "margarethe": "Abuela",
        "georg": "Georg",
        "elise": "Elise",
        "konrad": "Konrad",
        "hilde": "Hilde",
        "anna": "Anna",
    },
    "it": {
        "voss": "Pastore Voss",
        "otto": "Sindaco",
        "margarethe": "Nonna",
        "georg": "Georg",
        "elise": "Elise",
        "konrad": "Konrad",
        "hilde": "Hilde",
        "anna": "Anna",
    },
}


def build_translations():
    """Build the complete translation dictionaries for all languages."""
    translations = {"en": {}, "fr": {}, "es": {}, "it": {}}

    # Process each dialogue file
    _add_prologue(translations)
    _add_act1_arrival(translations)
    _add_act1_first_night(translations)
    _add_act1_village_exploration(translations)
    _add_act1_smithy_evening(translations)
    _add_act2_investigation_morning(translations)
    _add_act2_church_secrets(translations)
    _add_act2_konrad_encounter(translations)
    _add_act2_hilde_ritual(translations)
    _add_act2_the_book(translations)
    _add_act3_allies_choice(translations)
    _add_act3_reality_breaks(translations)
    _add_act3_descent(translations)
    _add_act3_preparation(translations)
    _add_act4_ritual_night(translations)
    _add_act4_ending_seal(translations)
    _add_act4_ending_escape(translations)
    _add_act4_ending_pact(translations)
    _add_act4_ending_truth(translations)
    _add_act4_ending_sacrifice(translations)
    _add_act4_ending_awakening(translations)

    return translations


def _t(translations, file_key, node_id, en="", fr="", es="", it="", field="text"):
    """Helper to add a translation entry for all 4 languages."""
    for lang, text in [("en", en), ("fr", fr), ("es", es), ("it", it)]:
        if text:
            translations[lang].setdefault(file_key, {}).setdefault(node_id, {})[field] = text


def _tc(translations, file_key, node_id, en_choices=None, fr_choices=None, es_choices=None, it_choices=None):
    """Helper to add choice translations."""
    for lang, choices in [("en", en_choices), ("fr", fr_choices), ("es", es_choices), ("it", it_choices)]:
        if choices:
            translations[lang].setdefault(file_key, {}).setdefault(node_id, {})["choices"] = choices


# ═══════════════════════════════════════════════════════════════
# PROLOGUE
# ═══════════════════════════════════════════════════════════════
def _add_prologue(tr):
    F = "res://data/dialogue/prologue.json"

    _t(tr, F, "narration_1",
       en="Berlin, November 1923.",
       fr="Berlin, novembre 1923.",
       es="Berlín, noviembre de 1923.",
       it="Berlino, novembre 1923.")

    _t(tr, F, "narration_1b",
       en="The rain drums against the window of my small apartment in Charlottenburg. Outside, a woman walks with her head bowed through the puddles. She doesn't look up.",
       fr="Là pluie tambourine contre là fenêtre de mon petit appartement à Charlottenburg. Dehors, une femme marche tête baissée dans les flaques. Elle ne lève pas les yeux.",
       es="La lluvia tamborilea contra la ventana de mi pequeño apartamento en Charlottenburg. Afuera, una mujer camina con la cabeza gacha entre los charcos. No levanta la vista.",
       it="La pioggia tamburella contro la finestra del mio piccolo appartamento a Charlottenburg. Fuori, una donna cammina a testa bassa tra le pozzanghere. Non alza lo sguardo.")

    _t(tr, F, "narration_1c",
       en="Nobody looks up these days. Inflation is devouring the country. A loaf of bread costs billions. But that's not why my hands are trembling.",
       fr="Personne ne lève les yeux ces jours-ci. L'inflation dévore le pays. Un pain coûte des milliards. Mais ce n'est pas pour celà que mes mains tremblent.",
       es="Nadie levanta la vista en estos días. La inflación devora el país. Un pan cuesta miles de millones. Pero no es por eso que mis manos tiemblan.",
       it="Nessuno alza lo sguardo di questi tempi. L'inflazione divora il paese. Un pane costa miliardi. Ma non è per questo che le mie mani tremano.")

    _t(tr, F, "narration_2",
       en="Between stacks of folklore books and half-finished seminar papers lies a letter. The envelope is damp from the rain, but the ink has held.",
       fr="Entre des piles de livres de folklore et des travaux de séminaire inachevés se trouve une lettre. L'enveloppe est humide de pluie, mais l'encre à tenu.",
       es="Entre pilas de libros de folclore y trabajos de seminario a medio terminar hay una carta. El sobre está húmedo por la lluvia, pero la tinta ha resistido.",
       it="Tra pile di libri di folklore è tesine incompiute giace una lettera. La busta è umida di pioggia, ma l'inchiostro ha tenuto.")

    _t(tr, F, "narration_2b",
       en="The postmark is from today. The handwriting belongs to my grandmother Margarethe.",
       fr="Le cachet de là poste est d'aujourd'hui. L'écriture est celle de mà grand-mère Margarethe.",
       es="El matasellos es de hoy. La letra es de mi abuela Margarethe.",
       it="Il timbro postale è di oggi. La calligrafia è di mia nonna Margarethe.")

    _t(tr, F, "narration_2c",
       en="Grandmother hasn't written to me in five months. My last three letters went unanswered. I had started to worry.",
       fr="Grand-mère ne m'à pas écrit depuis cinq mois. Mes trois dernières lettres sont restées sans réponse. J'avais commencé à m'inquiéter.",
       es="La abuela no me ha escrito en cinco meses. Mis últimas tres cartas quedaron sin respuesta. Había empezado a preocuparme.",
       it="La nonna non mi scrive da cinque mesi. Le mie ultime tre lettere sono rimaste senza risposta. Avevo iniziato a preoccuparmi.")

    _t(tr, F, "elise_1",
       en="This handwriting... yes, that's her. But it trembles more than before. And the ink — she wrote with something darker than usual.",
       fr="Cette écriture... oui, c'est bien elle. Mais elle tremble plus qu'avant. Et l'encre — elle à écrit avec quelque chose de plus sombre que d'habitude.",
       es="Esta letra... sí, es ella. Pero tiembla más que antes. Y la tinta... escribió con algo más oscuro de lo habitual.",
       it="Questa calligrafia... sì, è lei. Ma trema più di prima. È l'inchiostro — ha scritto con qualcosa di più scuro del solito.")

    _t(tr, F, "narration_3",
       en="I carefully open the letter. The paper smells of... herbs? And something else. Earth, perhaps. Or ash.",
       fr="J'ouvre là lettre avec précaution. Le papier sent les... herbes ? Et autre chose. De là terre, peut-être. Ou des cendres.",
       es="Abro la carta con cuidado. El papel huele a... ¿hierbas? Y a algo más. Tierra, quizás. O ceniza.",
       it="Apro la lettera con cautela. La carta odora di... erbe? È di qualcos'altro. Terra, forse. O cenere.")

    _t(tr, F, "narration_3b",
       en="The letter is short. Just three sentences, in shaky handwriting:",
       fr="Là lettre est courte. Trois phrases seulement, d'une écriture tremblante :",
       es="La carta es breve. Solo tres frases, con letra temblorosa:",
       it="La lettera è breve. Solo tre frasi, con grafia tremante:")

    _t(tr, F, "narration_4",
       en="\"Dearest Elise, come to Graubach. It is time for you to learn the truth. Bring something to protect yourself.\"",
       fr="\"Très chère Elise, viens à Graubach. Il est temps que tu apprennes la vérité. Apporte quelque chose pour te protéger.\"",
       es="\"Queridísima Elise, ven a Graubach. Es hora de que conozcas la verdad. Trae algo para protegerte.\"",
       it="\"Carissima Elise, vieni a Graubach. È tempo che tu conosca la verità. Porta qualcosa per proteggerti.\"")

    _t(tr, F, "elise_3",
       en="\"Something to protect myself\"? Grandmother, what is that supposed to mean?",
       fr="\"Quelque chose pour me protéger\" ? Grand-mère, qu'est-ce que cela signifie ?",
       es="\"¿Algo para protegerme\"? Abuela, ¿qué se supone que significa eso?",
       it="\"Qualcosa per proteggermi\"? Nonna, che cosa dovrebbe significare?")

    _t(tr, F, "narration_5",
       en="I turn the letter over. On the back, something is scratched — not a written word, but a symbol. A spiral, winding inward.",
       fr="Je retourne là lettre. Au dos, quelque chose est gravé — pas un mot écrit, mais un symbole. Une spirale qui s'enroule vers l'intérieur.",
       es="Le doy la vuelta a la carta. En el reverso hay algo grabado, no una palabra escrita, sino un símbolo. Una espiral que se enrolla hacia dentro.",
       it="Giro la lettera. Sul retro c'è qualcosa di inciso — non una parola scritta, ma un simbolo. Una spirale che si avvolge verso l'interno.")

    _t(tr, F, "narration_5b",
       en="In my folklore studies, I've seen this symbol. It's old. Older than Christianity in these lands. A protection sign — or a warning.",
       fr="Dans mes études de folklore, j'ai vu ce symbole. Il est ancien. Plus ancien que le christianisme dans ces contrées. Un signe de protection — où un avertissement.",
       es="En mis estudios de folclore he visto este símbolo. Es antiguo. Más antiguo que el cristianismo en estas tierras. Un signo de protección... o una advertencia.",
       it="Nei miei studi di folklore ho visto questo simbolo. È antico. Più antico del cristianesimo in queste terre. Un segno di protezione — o un avvertimento.")

    _t(tr, F, "elise_5",
       en="The next train south leaves tomorrow morning at six. I need to pack.",
       fr="Le prochain train vers le sud part demain matin à six heures. Je dois faire mes bagages.",
       es="El próximo tren hacia el sur sale mañana por la mañana a las seis. Tengo que hacer la maleta.",
       it="Il prossimo treno per il sud parte domani mattina alle sei. Devo fare i bagagli.")

    _t(tr, F, "narration_6",
       en="My gaze wanders through the apartment. I can't take much — only the essentials. But grandmother's words make me hesitate.",
       fr="Mon regard parcourt l'appartement. Je ne peux pas emporter grand-chose — seulement l'essentiel. Mais les mots de grand-mère me font hésiter.",
       es="Mi mirada recorre el apartamento. No puedo llevar mucho, solo lo esencial. Pero las palabras de la abuela me hacen dudar.",
       it="Il mio sguardo vaga per l'appartamento. Non posso portare molto — solo l'essenziale. Ma le parole della nonna mi fanno esitare.")

    _t(tr, F, "narration_6b",
       en="\"Bring something to protect yourself.\"",
       fr="\"Apporte quelque chose pour te protéger.\"",
       es="\"Trae algo para protegerte.\"",
       it="\"Porta qualcosa per proteggerti.\"")

    _tc(tr, F, "choice_pack",
        en_choices=["My folklore books — Knowledge is protection", "Mother's old crucifix — Faith is protection", "My camera — Truth is protection"],
        fr_choices=["Mes livres de folklore — Le savoir protège", "Le vieux crucifix de maman — La foi protège", "Mon appareil photo — La vérité protège"],
        es_choices=["Mis libros de folclore — El conocimiento es protección", "El viejo crucifijo de mamá — La fe es protección", "Mi cámara — La verdad es protección"],
        it_choices=["I miei libri di folklore — La conoscenza è protezione", "Il vecchio crocifisso di mamma — La fede è protezione", "La mia macchina fotografica — La verità è protezione"])

    _t(tr, F, "pack_books",
       en="I pack three books: Grimm's Legends, a treatise on Germanic protective rituals, and my own notes on Black Forest folklore.",
       fr="J'emballe trois livres : les Légendes de Grimm, un traité sur les rituels de protection germaniques et mes propres notes sur le folklore de là Forêt-Noire.",
       es="Empaco tres libros: las Leyendas de Grimm, un tratado sobre rituales germánicos de protección y mis propias notas sobre el folclore de la Selva Negra.",
       it="Impacco tre libri: le Leggende di Grimm, un trattato sui rituali protettivi germanici è i miei appunti sul folklore della Foresta Nera.")

    _t(tr, F, "pack_books_2",
       en="Knowledge has never let me down. Whatever grandmother means — I'll find it in the books.",
       fr="Le savoir ne m'à jamais fait défaut. Quoi que grand-mère veuille dire — je le trouverai dans les livres.",
       es="El conocimiento nunca me ha fallado. Sea lo que sea que la abuela quiera decir, lo encontraré en los libros.",
       it="La conoscenza non mi ha mai deluso. Qualunque cosa intenda la nonna, la troverò nei libri.")

    _t(tr, F, "pack_books_3",
       en="Between the pages of my notebook, I find pressed flowers from Graubach. Arnica and monkshood. Grandmother had pressed them into my hand during my last visit.",
       fr="Entre les pages de mon carnet, je trouve des fleurs pressées de Graubach. De l'arnicà et de l'aconit. Grand-mère me les avait mises dans là main lors de mà dernière visite.",
       es="Entre las páginas de mi cuaderno encuentro flores prensadas de Graubach. Árnica y acónito. La abuela me las puso en la mano durante mi última visita.",
       it="Tra le pagine del mio quaderno trovo fiori pressati di Graubach. Arnica è aconito. La nonna me li aveva messi in mano durante la mia ultima visita.")

    _t(tr, F, "pack_cross",
       en="The crucifix lies in a drawer, wrapped in a cloth. It's carved from dark wood, by hand. My mother wore it until her death.",
       fr="Le crucifix est dans un tiroir, enveloppé dans un tissu. Il est en bois sombre, sculpté à là main. Mà mère l'à porté jusqu'à sà mort.",
       es="El crucifijo está en un cajón, envuelto en un paño. Está tallado en madera oscura, a mano. Mi madre lo llevó hasta su muerte.",
       it="Il crocifisso giace in un cassetto, avvolto in un panno. È intagliato in legno scuro, a mano. Mia madre lo portò fino alla sua morte.")

    _t(tr, F, "pack_cross_2",
       en="I'm not a religious woman. But Mother was — and Grandmother is too. Perhaps there's a protection in that which I don't understand.",
       fr="Je ne suis pas une femme croyante. Mais Maman l'était — et Grand-mère l'est aussi. Peut-être y a-t-il une protection là-dedans que je ne comprends pas.",
       es="No soy una mujer religiosa. Pero mamá lo era, y la abuela también. Quizás haya en ello una protección que no comprendo.",
       it="Non sono una donna religiosa. Ma la mamma lo era — è anche la nonna lo è. Forse c'è una protezione in questo che non capisco.")

    _t(tr, F, "pack_cross_3",
       en="When I pick it up, the wood feels warm. Almost too warm for a piece that's been lying in a drawer for months.",
       fr="Quand je le prends en main, le bois est chaud. Presque trop chaud pour un objet resté des mois dans un tiroir.",
       es="Cuando lo tomo, la madera se siente cálida. Casi demasiado cálida para algo que ha estado meses en un cajón.",
       it="Quando lo prendo, il legno è caldo. Quasi troppo caldo per un pezzo rimasto mesi in un cassetto.")

    _t(tr, F, "pack_camera",
       en="My Leica. Bought second-hand from a photographer who left the country. Six rolls of film — more than I can afford.",
       fr="Mon Leica. Acheté d'occasion à un photographe qui à quitté le pays. Six rouleaux de pellicule — plus que ce que je peux me permettre.",
       es="Mi Leica. Comprada de segunda mano a un fotógrafo que abandonó el país. Seis rollos de película, más de lo que puedo permitirme.",
       it="La mia Leica. Comprata usata da un fotografo che ha lasciato il paese. Sei rullini — più di quanto possa permettermi.")

    _t(tr, F, "pack_camera_2",
       en="Whatever happens in Graubach — I will document it. Pictures don't lie. Unlike people.",
       fr="Quoi qu'il arrive à Graubach — je le documenterai. Les images ne mentent pas. Contrairement aux gens.",
       es="Pase lo que pase en Graubach, lo documentaré. Las fotos no mienten. A diferencia de la gente.",
       it="Qualunque cosa accada a Graubach, la documenterò. Le foto non mentono. A differenza delle persone.")

    _t(tr, F, "pack_camera_3",
       en="I load the first roll and take a test shot of the letter. Through the viewfinder, the spiral on the back looks larger than it should be.",
       fr="Je charge le premier rouleau et prends une photo test de là lettre. Dans le viseur, là spirale au dos paraît plus grande qu'elle ne devrait.",
       es="Cargo el primer rollo y tomo una foto de prueba de la carta. Por el visor, la espiral en el reverso parece más grande de lo que debería.",
       it="Carico il primo rullino è scatto una foto di prova della lettera. Attraverso il mirino, la spirale sul retro sembra più grande di quanto dovrebbe.")

    _t(tr, F, "journal_pack",
       en="The Letter from Graubach",
       fr="Là Lettre de Graubach",
       es="La carta de Graubach",
       it="La lettera da Graubach",
       field="title")
    _t(tr, F, "journal_pack",
       en="Grandmother writes after five months of silence. Three cryptic sentences and an etched spiral. The postmark is from today — how can a letter from the Black Forest reach Berlin in a single day?",
       fr="Grand-mère écrit après cinq mois de silence. Trois phrases énigmatiques et une spirale gravée. Le cachet est d'aujourd'hui — comment une lettre de là Forêt-Noire peut-elle arriver à Berlin en un seul jour ?",
       es="La abuela escribe tras cinco meses de silencio. Tres frases enigmáticas y una espiral grabada. El matasellos es de hoy: ¿cómo puede una carta de la Selva Negra llegar a Berlín en un solo día?",
       it="La nonna scrive dopo cinque mesi di silenzio. Tre frasi enigmatiche è una spirale incisa. Il timbro è di oggi — come può una lettera dalla Foresta Nera raggiungere Berlino in un solo giorno?",
       field="content")

    _t(tr, F, "narration_night",
       en="I sleep badly that night. In my dream I hear singing — a chorus of many voices, deep and ancient. I don't know the melody, but my body does.",
       fr="Je dors mal cette nuit-là. Dans mon rêve, j'entends un chant — un chœur de nombreuses voix, profondes et anciennes. Je ne connais pas là mélodie, mais mon corps là connaît.",
       es="Duermo mal esa noche. En mi sueño oigo cantos: un coro de muchas voces, profundas y antiguas. No conozco la melodía, pero mi cuerpo sí.",
       it="Dormo male quella notte. Nel sogno sento un canto — un coro di molte voci, profonde è antiche. Non conosco la melodia, ma il mio corpo sì.")

    _t(tr, F, "narration_night_2",
       en="When the alarm rings at half past four, I'm already awake. My fingers are cold. On the fogged window, someone — or something — has drawn a spiral.",
       fr="Quand le réveil sonne à quatre heures et demie, je suis déjà éveillée. Mes doigts sont froids. Sur là vitre embuée, quelqu'un — où quelque chose — à dessiné une spirale.",
       es="Cuando suena el despertador a las cuatro y media, ya estoy despierta. Mis dedos están fríos. En el cristal empañado, alguien — o algo — ha dibujado una espiral.",
       it="Quando la sveglia suona alle quattro è mezza, sono già sveglia. Le mie dita sono fredde. Sul vetro appannato, qualcuno — o qualcosa — ha disegnato una spirale.")

    _t(tr, F, "narration_night_3",
       en="From the inside.",
       fr="De l'intérieur.",
       es="Desde dentro.",
       it="Dall'interno.")

    _t(tr, F, "narration_train_1",
       en="The train rattles through the November landscape. Berlin is three hours behind me. The cities grow smaller, the forests denser.",
       fr="Le train cahote à travers le paysage de novembre. Berlin est trois heures derrière moi. Les villes se font plus petites, les forêts plus denses.",
       es="El tren traquetea por el paisaje de noviembre. Berlín queda tres horas atrás. Las ciudades se hacen más pequeñas, los bosques más densos.",
       it="Il treno sferraglia attraverso il paesaggio di novembre. Berlino è tre ore alle mie spalle. Le città si rimpiccioliscono, le foreste si infittiscono.")

    _t(tr, F, "narration_train_2",
       en="Across from me sits an elderly woman with a basket on her lap. She knits and hums softly. The melody...",
       fr="En face de moi est assise une vieille femme avec un panier sur les genoux. Elle tricote et fredonne doucement. Là mélodie...",
       es="Frente a mí está sentada una mujer mayor con una cesta en el regazo. Teje y tararea suavemente. La melodía...",
       it="Di fronte a me siede una donna anziana con un cesto in grembo. Lavora a maglia è canticchia piano. La melodia...")

    _t(tr, F, "narration_train_3",
       en="It's the same melody from my dream.",
       fr="C'est là même mélodie que dans mon rêve.",
       es="Es la misma melodía de mi sueño.",
       it="È la stessa melodia del mio sogno.")

    _t(tr, F, "elise_train_2",
       en="Excuse me... that song you're humming. Where do you know it from?",
       fr="Excusez-moi... cette chanson que vous fredonnez. D'où là connaissez-vous ?",
       es="Disculpe... esa canción que tararea. ¿De dónde la conoce?",
       it="Mi scusi... quella canzone che canticchia. Da dove la conosce?")

    _t(tr, F, "narration_train_old",
       en="The woman looks at me. Her eyes are milky, nearly blind. She smiles.",
       fr="Là femme me regarde. Ses yeux sont laiteux, presque aveugles. Elle sourit.",
       es="La mujer me mira. Sus ojos son lechosos, casi ciegos. Sonríe.",
       it="La donna mi guarda. I suoi occhi sono lattiginosi, quasi ciechi. Sorride.")

    _t(tr, F, "narration_train_old_2",
       en="\"They sing that in the Black Forest when November comes. So that those who sleep below don't wake up.\"",
       fr="\"On chante ça dans la Forêt-Noire quand novembre arrive. Pour que ceux qui dorment en dessous ne se réveillent pas.\"",
       es="\"Eso se canta en la Selva Negra cuando llega noviembre. Para que los que duermen abajo no despierten.\"",
       it="\"Nella Foresta Nera si canta così quando arriva novembre. Perché quelli che dormono sotto non si sveglino.\"")

    _t(tr, F, "narration_train_old_3",
       en="She continues knitting. I say nothing more. But I notice that her knitting pattern forms spirals.",
       fr="Elle continue de tricoter. Je ne dis plus rien. Mais je remarque que son motif de tricot forme des spirales.",
       es="Sigue tejiendo. No digo nada más. Pero noto que su patrón de tejido forma espirales.",
       it="Continua a lavorare a maglia. Non dico altro. Ma noto che il suo motivo a maglia forma delle spirali.")

    _t(tr, F, "narration_train_4",
       en="In Freiburg I change trains. The connecting train is smaller, older. It smells of coal smoke and wet wood.",
       fr="À Fribourg, je change de train. Là correspondance est plus petite, plus vieille. Elle sent là fumée de charbon et le bois mouillé.",
       es="En Friburgo hago trasbordo. El tren de conexión es más pequeño, más viejo. Huele a humo de carbón y madera mojada.",
       it="A Friburgo cambio treno. La coincidenza è più piccola, più vecchia. Odora di fumo di carbone è legno bagnato.")

    _t(tr, F, "elise_train_4",
       en="Graubach... I was last there as a child. Ten years ago. Back then it smelled of pine needles and grandmother's cake.",
       fr="Graubach... J'y suis allée pour là dernière fois enfant. Il y à dix ans. À l'époque, çà sentait les aiguilles de pin et le gâteau de grand-mère.",
       es="Graubach... La última vez que estuve allí fue de niña. Hace diez años. Entonces olía a agujas de pino y al pastel de la abuela.",
       it="Graubach... L'ultima volta ci sono stata da bambina. Dieci anni fa. Allora odorava di aghi di pino è della torta della nonna.")

    _t(tr, F, "narration_train_5",
       en="I remember the village fountain, the church with the crooked tower. The forest that encircles the village like a clenched fist.",
       fr="Je me souviens de là fontaine du village, de l'église au clocher penché. De là forêt qui entoure le village comme un poing serré.",
       es="Recuerdo la fuente del pueblo, la iglesia con la torre torcida. El bosque que rodea el pueblo como un puño cerrado.",
       it="Ricordo la fontana del villaggio, la chiesa con la torre storta. Il bosco che circonda il villaggio come un pugno chiuso.")

    _t(tr, F, "narration_train_6",
       en="And I remember something I've long suppressed. The last night in Graubach, when I was fourteen.",
       fr="Et je me souviens de quelque chose que j'ai longtemps refoulé. Là dernière nuit à Graubach, quand j'avais quatorze ans.",
       es="Y recuerdo algo que he reprimido durante mucho tiempo. La última noche en Graubach, cuando tenía catorce años.",
       it="E ricordo qualcosa che ho a lungo rimosso. L'ultima notte a Graubach, quando avevo quattordici anni.")

    _t(tr, F, "narration_train_7",
       en="I had woken because I heard singing. From the ground. Grandmother sat by my bed, holding my hand. \"Go back to sleep,\" she'd said. \"It's just the wind singing.\"",
       fr="Je m'étais réveillée parce que j'avais entendu un chant. Venant du sol. Grand-mère était assise à côté de mon lit et me tenait là main. \"Rendors-toi\", avait-elle dit. \"C'est juste le vent qui chante.\"",
       es="Me había despertado porque oí cantos. Desde el suelo. La abuela estaba sentada junto a mi cama, tomándome de la mano. \"Vuelve a dormir\", había dicho. \"Solo es el viento que canta.\"",
       it="Mi ero svegliata perché avevo sentito un canto. Dal suolo. La nonna era seduta accanto al mio letto è mi teneva la mano. \"Torna a dormire\", aveva detto. \"È solo il vento che canta.\"")

    _t(tr, F, "narration_train_8",
       en="But it hadn't been the wind. And grandmother had been crying.",
       fr="Mais ce n'était pas le vent. Et grand-mère pleurait.",
       es="Pero no había sido el viento. Y la abuela había estado llorando.",
       it="Ma non era stato il vento. È la nonna stava piangendo.")

    _t(tr, F, "narration_kutsche",
       en="The railway ends in Waldkirch. From there it's another two hours by coach.",
       fr="Là voie ferrée s'arrête à Waldkirch. De là, il faut encore deux heures en calèche.",
       es="La vía férrea termina en Waldkirch. Desde allí son dos horas más en carruaje.",
       it="La ferrovia finisce a Waldkirch. Da lì sono altre due ore in carrozza.")

    _t(tr, F, "narration_kutsche_2",
       en="The coachman is a taciturn man with a scarred face. When I say \"Graubach,\" he pauses briefly.",
       fr="Le cocher est un homme taciturne au visage balafré. Quand je dis \"Graubach\", il marque une pause.",
       es="El cochero es un hombre taciturno con el rostro marcado. Cuando digo \"Graubach\", se detiene brevemente.",
       it="Il cocchiere è un uomo taciturno dal viso sfregiato. Quando dico \"Graubach\", si ferma un istante.")

    _t(tr, F, "narration_kutsche_3",
       en="\"I'll take you to the village edge,\" he says. \"No further. Not in November.\"",
       fr="\"Je vous emmène jusqu'à l'entrée du village\", dit-il. \"Pas plus loin. Pas en novembre.\"",
       es="\"La llevo hasta las afueras del pueblo\", dice. \"Más lejos no voy. No en noviembre.\"",
       it="\"La porto fino al limite del villaggio\", dice. \"Oltre non vado. Non a novembre.\"")

    _t(tr, F, "narration_kutsche_4",
       en="The road narrows. The firs close in as if trying to block the way. The last daylight struggles through the branches.",
       fr="Là route se rétrécit. Les sapins se rapprochent comme pour barrer le passage. Là dernière lumière du jour peine à traverser les branches.",
       es="El camino se estrecha. Los abetos se cierran como queriendo bloquear el paso. La última luz del día lucha por atravesar las ramas.",
       it="La strada si restringe. Gli abeti si serrano come a voler sbarrare il passo. L'ultima luce del giorno fatica a filtrare tra i rami.")

    _t(tr, F, "narration_kutsche_5",
       en="At the village edge, the coachman stops abruptly. He takes my money without looking at me. The coach disappears into the fog before I can turn around.",
       fr="À l'entrée du village, le cocher s'arrête brusquement. Il prend mon argent sans me regarder. Là calèche disparaît dans le brouillard avant que je puisse me retourner.",
       es="En las afueras del pueblo, el cochero se detiene bruscamente. Toma mi dinero sin mirarme. El carruaje desaparece en la niebla antes de que pueda darme la vuelta.",
       it="Al limite del villaggio, il cocchiere si ferma di colpo. Prende i miei soldi senza guardarmi. La carrozza scompare nella nebbia prima che io possa voltarmi.")

    _t(tr, F, "narration_arrival_1",
       en="Graubach.",
       fr="Graubach.",
       es="Graubach.",
       it="Graubach.")

    _t(tr, F, "narration_arrival_2",
       en="The fog hangs between the half-timbered houses like grey shrouds. The shutters are closed — all of them. On an afternoon.",
       fr="Le brouillard pend entre les maisons à colombages comme des linceuls gris. Les volets sont fermés — tous. En plein après-midi.",
       es="La niebla cuelga entre las casas de entramado como sudarios grises. Las contraventanas están cerradas, todas. Una tarde.",
       it="La nebbia pende tra le case a graticcio come sudari grigi. Le imposte sono chiuse — tutte. In un pomeriggio.")

    _t(tr, F, "narration_arrival_3",
       en="No dog barks. No child plays in the street. No smoke rises from the chimneys, though it's bitterly cold.",
       fr="Aucun chien n'aboie. Aucun enfant ne joue dans là rue. Aucune fumée ne s'élève des cheminées, malgré le froid mordant.",
       es="Ningún perro ladra. Ningún niño juega en la calle. No sale humo de las chimeneas, aunque hace un frío glacial.",
       it="Nessun cane abbaia. Nessun bambino gioca per strada. Nessun fumo sale dai camini, nonostante il freddo pungente.")

    _t(tr, F, "narration_arrival_4",
       en="The silence isn't empty. It's full. Like a mouth opening to scream but making no sound.",
       fr="Le silence n'est pas vide. Il est plein. Comme une bouche qui s'ouvre pour crier mais n'émet aucun son.",
       es="El silencio no está vacío. Está lleno. Como una boca que se abre para gritar pero no emite ningún sonido.",
       it="Il silenzio non è vuoto. È pieno. Come una bocca che si apre per gridare ma non emette alcun suono.")

    _t(tr, F, "narration_arrival_5",
       en="My footsteps on the cobblestones are the only sound. Each step an intruder in this suffocating quiet.",
       fr="Mes pas sur les pavés sont le seul bruit. Chaque pas est un intrus dans ce silence étouffant.",
       es="Mis pasos sobre los adoquines son el único sonido. Cada paso es un intruso en esta quietud sofocante.",
       it="I miei passi sul selciato sono l'unico suono. Ogni passo un intruso in questa quiete soffocante.")

    _t(tr, F, "narration_arrival_6",
       en="I know the way to grandmother's house. Left past the fountain, up the alley, to the last door before the forest.",
       fr="Je connais le chemin vers là maison de grand-mère. À gauche après là fontaine, en remontant là ruelle, jusqu'à là dernière porte avant là forêt.",
       es="Conozco el camino a la casa de la abuela. A la izquierda pasando la fuente, subiendo por el callejón, hasta la última puerta antes del bosque.",
       it="Conosco la strada per la casa della nonna. A sinistra oltre la fontana, su per il vicolo, fino all'ultima porta prima del bosco.")

    _t(tr, F, "narration_arrival_7",
       en="I stop at the fountain. Dead leaves float in the murky water. And something else — a piece of cloth? No. It's a black ribbon.",
       fr="Je m'arrête à là fontaine. Des feuilles mortes flottent dans l'eau trouble. Et autre chose — un morceau de tissu ? Non. C'est un ruban noir.",
       es="Me detengo en la fuente. Hojas muertas flotan en el agua turbia. Y algo más: ¿un trozo de tela? No. Es una cinta negra.",
       it="Mi fermo alla fontana. Foglie morte galleggiano nell'acqua torbida. È qualcos'altro — un pezzo di stoffa? No. È un nastro nero.")

    _t(tr, F, "narration_arrival_8",
       en="A mourning ribbon.",
       fr="Un ruban de deuil.",
       es="Una cinta de luto.",
       it="Un nastro da lutto.")

    _t(tr, F, "narration_arrival_9",
       en="Another one hangs on grandmother's fence. The door stands slightly ajar. From inside comes the sweet smell of wilted flowers.",
       fr="Un autre est accroché à là clôture de grand-mère. Là porte est entrouverte. De l'intérieur émane l'odeur douceâtre de fleurs fanées.",
       es="Otro cuelga de la valla de la abuela. La puerta está entreabierta. Desde el interior llega el olor dulzón de flores marchitas.",
       it="Un altro pende dal recinto della nonna. La porta è socchiusa. Dall'interno arriva l'odore dolciastro di fiori appassiti.")

    _t(tr, F, "narration_arrival_10",
       en="The door creaks as the wind moves it. Or is it the wind?",
       fr="Là porte grince quand le vent là fait bouger. Ou est-ce le vent ?",
       es="La puerta cruje cuando el viento la mueve. ¿O es el viento?",
       it="La porta cigola quando il vento la muove. O è il vento?")

    _t(tr, F, "journal_arrival",
       en="Arrival in Graubach",
       fr="Arrivée à Graubach",
       es="Llegada a Graubach",
       it="Arrivo a Graubach",
       field="title")
    _t(tr, F, "journal_arrival",
       en="Graubach is silent. Too silent. All shutters closed, no smoke, no people. Mourning ribbon at the fountain and at grandmother's fence. The door stands open. Something is wrong here.",
       fr="Graubach est silencieux. Trop silencieux. Tous les volets fermés, pas de fumée, pas de gens. Un ruban de deuil à là fontaine et à là clôture de grand-mère. Là porte est ouverte. Quelque chose ne và pas ici.",
       es="Graubach está en silencio. Demasiado silencio. Todas las contraventanas cerradas, sin humo, sin gente. Cinta de luto en la fuente y en la valla de la abuela. La puerta está abierta. Algo no va bien aquí.",
       it="Graubach è in silenzio. Troppo silenzio. Tutte le imposte chiuse, niente fumo, niente gente. Nastro da lutto alla fontana è al recinto della nonna. La porta è aperta. Qualcosa non va qui.",
       field="content")


# ═══════════════════════════════════════════════════════════════
# The remaining files use auto-extraction + translation lookup
# ═══════════════════════════════════════════════════════════════

    # --- Additional translations (auto-generated) ---

    _t(tr, F, "narration_memory_1",
       en="Grandmother Margarethe was the one who brought me to folklore. As a child I sat on her lap while she told me the old stories — not as fairy tales, but as memories.",
       fr="Grand-mère Margarethe est celle qui m'a amenée au folklore. Enfant, j'étais assise sur ses genoux tandis qu'elle me racontait les vieilles histoires — non pas comme des contes de fées, mais comme des souvenirs.",
       es="La abuela Margarethe fue quien me acercó al folclore. De niña me sentaba en su regazo mientras me contaba las viejas historias, no como cuentos de hadas, sino como recuerdos.",
       it="Nonna Margarethe fu quella che mi avvicinò al folklore. Da bambina sedevo sulle sue ginocchia mentre mi raccontava le vecchie storie — non come fiabe, ma come ricordi.")

    _t(tr, F, "narration_memory_2",
       en="\"The stories are true, Elise,\" she always said. \"Not literally. But true.\" Back then I didn't understand what she meant. Today, after three semesters of folklore studies, I'm no longer sure I want to understand.",
       fr="\"Les histoires sont vraies, Elise\", disait-elle toujours. \"Pas au sens littéral. Mais vraies.\" À l'époque, je ne comprenais pas ce qu'elle voulait dire. Aujourd'hui, après trois semestres d'études folkloriques, je ne suis plus certaine de vouloir comprendre.",
       es="\"Las historias son verdaderas, Elise\", decía siempre. \"No literalmente. Pero verdaderas.\" Entonces no entendía lo que quería decir. Hoy, después de tres semestres de estudios folclóricos, ya no estoy segura de querer entenderlo.",
       it="\"Le storie sono vere, Elise\", diceva sempre. \"Non alla lettera. Ma vere.\" Allora non capivo cosa intendesse. Oggi, dopo tre semestri di studi folkloristici, non sono più sicura di volerlo capire.")

    _t(tr, F, "narration_memory_3",
       en="Five months of silence. Three unanswered letters. I had already considered calling the municipal office in Waldkirch. But then this letter arrived today.",
       fr="Cinq mois de silence. Trois lettres sans réponse. J'avais déjà envisagé d'appeler la mairie de Waldkirch. Mais alors cette lettre est arrivée aujourd'hui.",
       es="Cinco meses de silencio. Tres cartas sin respuesta. Ya había pensado en llamar a la administración municipal de Waldkirch. Pero entonces llegó esta carta hoy.",
       it="Cinque mesi di silenzio. Tre lettere senza risposta. Avevo già pensato di chiamare l'ufficio comunale di Waldkirch. Ma poi oggi è arrivata questa lettera.")

    _t(tr, F, "elise_conflict_1",
       en="Graubach... I have three seminars next week. My paper on Thuringian harvest rites is overdue.",
       fr="Graubach... J'ai trois séminaires la semaine prochaine. Mon travail sur les rites de moisson thuringiens est en retard.",
       es="Graubach... Tengo tres seminarios la próxima semana. Mi trabajo sobre los ritos de cosecha de Turingia está atrasado.",
       it="Graubach... Ho tre seminari la prossima settimana. Il mio lavoro sui riti del raccolto della Turingia è in ritardo.")

    _t(tr, F, "narration_conflict_2",
       en="I set the letter on the table and step to the window. The rain grows heavier. In the glass I see my reflection — tired eyes, hair unkempt. I've been sleeping badly for weeks.",
       fr="Je pose la lettre sur la table et m'approche de la fenêtre. La pluie redouble. Dans la vitre, je vois mon reflet — des yeux fatigués, les cheveux en désordre. Je dors mal depuis des semaines.",
       es="Dejo la carta sobre la mesa y me acerco a la ventana. La lluvia se intensifica. En el cristal veo mi reflejo: ojos cansados, el pelo despeinado. Llevo semanas durmiendo mal.",
       it="Poso la lettera sul tavolo e mi avvicino alla finestra. La pioggia si fa più forte. Nel vetro vedo il mio riflesso — occhi stanchi, i capelli in disordine. Sono settimane che dormo male.")

    _t(tr, F, "narration_conflict_3",
       en="Ever since the letters stopped coming, actually. As if a part of me had known that something was wrong. That grandmother's silence was not forgetfulness, but a decision.",
       fr="Depuis que les lettres ont cessé, en fait. Comme si une partie de moi avait su que quelque chose n'allait pas. Que le silence de grand-mère n'était pas de l'oubli, mais une décision.",
       es="Desde que las cartas dejaron de llegar, en realidad. Como si una parte de mí hubiera sabido que algo no estaba bien. Que el silencio de la abuela no era olvido, sino una decisión.",
       it="Da quando le lettere hanno smesso di arrivare, in realtà. Come se una parte di me avesse saputo che qualcosa non andava. Che il silenzio della nonna non era dimenticanza, ma una decisione.")

    _t(tr, F, "elise_conflict_4",
       en="No. The seminars can wait. Grandmother has never asked me for anything. Never. And now she writes \"come\" — then I'll come.",
       fr="Non. Les séminaires peuvent attendre. Grand-mère ne m'a jamais rien demandé. Jamais. Et maintenant elle écrit \"viens\" — alors je viendrai.",
       es="No. Los seminarios pueden esperar. La abuela nunca me ha pedido nada. Nunca. Y ahora escribe \"ven\" — pues iré.",
       it="No. I seminari possono aspettare. La nonna non mi ha mai chiesto nulla. Mai. E ora scrive \"vieni\" — allora verrò.")

    _t(tr, F, "narration_pack_think",
       en="Protection. What protects a person? Knowledge? Faith? Evidence? I look around my small apartment, and three things catch my eye.",
       fr="Protection. Qu'est-ce qui protège un être humain ? Le savoir ? La foi ? Les preuves ? Je regarde autour de moi dans mon petit appartement, et trois choses attirent mon regard.",
       es="Protección. ¿Qué protege a una persona? ¿El conocimiento? ¿La fe? ¿Las pruebas? Miro a mi alrededor en mi pequeño apartamento y tres cosas llaman mi atención.",
       it="Protezione. Cosa protegge un essere umano? La conoscenza? La fede? Le prove? Mi guardo intorno nel mio piccolo appartamento e tre cose attirano il mio sguardo.")

    _t(tr, F, "elise_train_ask_2",
       en="Those who sleep below? That sounds like an old incantation. I study folklore — may I ask where exactly in the Black Forest you learned that?",
       fr="Ceux qui dorment en dessous ? Cela ressemble à une vieille formule d'incantation. J'étudie le folklore — puis-je vous demander où exactement dans la Forêt-Noire vous avez appris cela ?",
       es="¿Los que duermen abajo? Suena a una antigua fórmula de conjuro. Estudio folclore — ¿puedo preguntar dónde exactamente en la Selva Negra aprendió eso?",
       it="Quelli che dormono sotto? Sembra un'antica formula di scongiuro. Studio folklore — posso chiederle dove esattamente nella Foresta Nera ha imparato questo?")

    _t(tr, F, "narration_old_react",
       en="The woman stops knitting. For a moment her smile is gone. Then it returns — but it no longer reaches her eyes.",
       fr="La femme cesse de tricoter. Un instant, son sourire a disparu. Puis il revient — mais il n'atteint plus ses yeux.",
       es="La mujer deja de tejer. Por un momento su sonrisa ha desaparecido. Luego vuelve — pero ya no le llega a los ojos.",
       it="La donna smette di lavorare a maglia. Per un istante il suo sorriso è scomparso. Poi ritorna — ma non raggiunge più i suoi occhi.")

    _t(tr, F, "narration_old_react_2",
       en="\"Learned? Child, you don't learn that. You know it. The same way you know when it's time to close the windows.\"",
       fr="\"Appris ? Mon enfant, ça ne s'apprend pas. On le sait. Comme on sait quand il est temps de fermer les fenêtres.\"",
       es="\"¿Aprendido? Niña, eso no se aprende. Se sabe. Como se sabe cuándo es hora de cerrar las ventanas.\"",
       it="\"Imparato? Bambina, questo non si impara. Si sa. Come si sa quando è ora di chiudere le finestre.\"")

    _t(tr, F, "elise_train_ask_3",
       en="And when is it time to close the windows?",
       fr="Et quand est-il temps de fermer les fenêtres ?",
       es="¿Y cuándo es hora de cerrar las ventanas?",
       it="E quando è ora di chiudere le finestre?")

    _t(tr, F, "narration_old_unsettling",
       en="The woman leans forward. Her breath smells of herbs — the same herbs as grandmother's letter. \"When the singing starts, child. When the singing starts.\"",
       fr="La femme se penche en avant. Son haleine sent les herbes — les mêmes herbes que la lettre de grand-mère. \"Quand le chant commence, mon enfant. Quand le chant commence.\"",
       es="La mujer se inclina hacia adelante. Su aliento huele a hierbas — las mismas hierbas que la carta de la abuela. \"Cuando empieza el canto, niña. Cuando empieza el canto.\"",
       it="La donna si sporge in avanti. Il suo alito odora di erbe — le stesse erbe della lettera della nonna. \"Quando il canto inizia, bambina. Quando il canto inizia.\"")

    _t(tr, F, "narration_train_old_4",
       en="A shiver runs down my spine. I press my bag closer to me and look out the window. The forests outside grow denser, darker.",
       fr="Un frisson me parcourt le dos. Je serre mon sac contre moi et regarde par la fenêtre. Les forêts dehors deviennent plus denses, plus sombres.",
       es="Un escalofrío me recorre la espalda. Aprieto mi bolso contra mí y miro por la ventana. Los bosques afuera se vuelven más densos, más oscuros.",
       it="Un brivido mi percorre la schiena. Stringo la borsa contro di me e guardo fuori dal finestrino. I boschi là fuori si fanno più fitti, più scuri.")

    _t(tr, F, "narration_childhood_1",
       en="This is not the Graubach of my childhood. Back then the doors stood open. Women called to each other across the alley. Girls washed laundry at the fountain and laughed.",
       fr="Ce n'est pas le Graubach de mon enfance. À l'époque, les portes étaient ouvertes. Les femmes s'interpellaient d'une ruelle à l'autre. Les filles lavaient le linge à la fontaine en riant.",
       es="Este no es el Graubach de mi infancia. Entonces las puertas estaban abiertas. Las mujeres se llamaban de una calle a otra. Las chicas lavaban la ropa en la fuente y reían.",
       it="Questo non è la Graubach della mia infanzia. Allora le porte erano aperte. Le donne si chiamavano da un vicolo all'altro. Le ragazze lavavano i panni alla fontana e ridevano.")

    _t(tr, F, "elise_childhood_1",
       en="Grandmother always stood at the fence and waved when I came. Even from afar I could see her. What happened here?",
       fr="Grand-mère se tenait toujours à la clôture et me faisait signe quand j'arrivais. Même de loin, je pouvais la voir. Que s'est-il passé ici ?",
       es="La abuela siempre estaba en la valla y saludaba cuando yo llegaba. Ya desde lejos podía verla. ¿Qué ha pasado aquí?",
       it="La nonna stava sempre al recinto e salutava quando arrivavo. Già da lontano potevo vederla. Cosa è successo qui?")

    _t(tr, F, "narration_childhood_2",
       en="Nobody waves. Nobody stands at the fence. Only the fog creeps through the empty alleys, and somewhere — deep and barely audible — something hums.",
       fr="Personne ne fait signe. Personne ne se tient à la clôture. Seul le brouillard rampe dans les ruelles désertes, et quelque part — profondément et à peine audible — quelque chose fredonne.",
       es="Nadie saluda. Nadie está en la valla. Solo la niebla se arrastra por los callejones vacíos, y en algún lugar — profundo y apenas audible — algo tararea.",
       it="Nessuno saluta. Nessuno sta al recinto. Solo la nebbia striscia per i vicoli vuoti, e da qualche parte — profondo e appena udibile — qualcosa canticchia.")

    _t(tr, F, "elise_arrival_emotion",
       en="Mourning ribbon... No. No, no, no.",
       fr="Un ruban de deuil... Non. Non, non, non.",
       es="Cinta de luto... No. No, no, no.",
       it="Nastro da lutto... No. No, no, no.")

    _t(tr, F, "narration_arrival_emotion_2",
       en="My knees go weak. I grab the fence to steady myself. The wood is damp and cold under my fingers. The sweet smell of wilted flowers grows stronger.",
       fr="Mes genoux fléchissent. Je m'agrippe à la clôture pour me retenir. Le bois est humide et froid sous mes doigts. L'odeur douceâtre des fleurs fanées s'intensifie.",
       es="Las rodillas me flaquean. Me agarro a la valla para sostenerme. La madera está húmeda y fría bajo mis dedos. El olor dulzón de las flores marchitas se hace más fuerte.",
       it="Le ginocchia mi cedono. Mi aggrappo al recinto per sostenermi. Il legno è umido e freddo sotto le dita. L'odore dolciastro dei fiori appassiti si fa più forte.")

    _t(tr, F, "narration_arrival_emotion_3",
       en="I know this smell. Lilies. Funeral lilies. The same ones that stood at Mother's funeral.",
       fr="Je connais cette odeur. Des lys. Des lys funéraires. Les mêmes que ceux qui ornaient l'enterrement de Maman.",
       es="Conozco este olor. Lirios. Lirios funerarios. Los mismos que había en el funeral de mamá.",
       it="Conosco questo odore. Gigli. Gigli funebri. Gli stessi che c'erano al funerale della mamma.")


def _add_act1_arrival(tr):
    """Act 1 - Grandmother's House"""
    F = "res://data/dialogue/act1/arrival.json"
    _t(tr,F,"narration_1", en="The inside of grandmother's house has barely changed. The same dark wooden furniture, the same crocheted blankets.", fr="L'intérieur de là maison de grand-mère n'à guère changé. Les mêmes meubles en bois sombre, les mêmes couvertures au crochet.", es="El interior de la casa de la abuela apenas ha cambiado. Los mismos muebles de madera oscura, las mismas mantas de ganchillo.", it="L'interno della casa della nonna è a malapena cambiato. Gli stessi mobili di legno scuro, le stesse coperte all'uncinetto.")
    _t(tr,F,"narration_2", en="But the smell is different. Beneath the familiar scent of chamomile tea and beeswax lies something sweet. Something I can't place.", fr="Mais l'odeur est différente. Sous le parfum familier de camomille et de cire d'abeille se cache quelque chose de douceâtre. Quelque chose que je n'arrive pas à identifier.", es="Pero el olor es diferente. Bajo el aroma familiar de té de manzanilla y cera de abeja hay algo dulzón. Algo que no puedo identificar.", it="Ma l'odore è diverso. Sotto il familiare profumo di camomilla è cera d'api c'è qualcosa di dolciastro. Qualcosa che non riesco a identificare.")
    _t(tr,F,"narration_3", en="In the bedroom she lies. Grandmother Margarethe. The blanket is pulled up to her chin, as if someone carefully tucked her in.", fr="Dans là chambre, elle repose. Grand-mère Margarethe. Là couverture est tirée jusqu'au menton, comme si quelqu'un l'avait soigneusement bordée.", es="En el dormitorio yace ella. La abuela Margarethe. La manta está subida hasta la barbilla, como si alguien la hubiera arropado con cuidado.", it="Nella camera da letto giace lei. Nonna Margarethe. La coperta è tirata fino al mento, come se qualcuno l'avesse rimboccata con cura.")
    _t(tr,F,"narration_4", en="Her eyes are closed. Her mouth smiles faintly. But her skin has the color of old parchment, and when I touch her hand, it's cold as stone.", fr="Ses yeux sont fermés. Sà bouche esquisse un léger sourire. Mais sà peau à là couleur du vieux parchemin, et quand je touche sà main, elle est froide comme là pierre.", es="Sus ojos están cerrados. Su boca esboza una leve sonrisa. Pero su piel tiene el color del pergamino viejo, y cuando toco su mano, está fría como la piedra.", it="I suoi occhi sono chiusi. La sua bocca sorride lievemente. Ma la sua pelle ha il colore della vecchia pergamena, è quando tocco la sua mano, è fredda come la pietra.")
    _t(tr,F,"narration_5", en="On the nightstand are three things: a candle, burning. A glass of cloudy water. And a small notebook with a leather cover.", fr="Sur là table de nuit, il y à trois choses : une bougie allumée. Un verre d'eau trouble. Et un petit carnet avec une couverture en cuir.", es="En la mesita de noche hay tres cosas: una vela encendida. Un vaso de agua turbia. Y un pequeño cuaderno con cubierta de cuero.", it="Sul comodino ci sono tre cose: una candela accesa. Un bicchiere d'acqua torbida. È un piccolo quaderno con copertina di pelle.")
    _t(tr,F,"narration_6", en="The candle. It's burning. For three days, if the neighbors are right.", fr="Là bougie. Elle brûle. Depuis trois jours, si les voisins disent vrai.", es="La vela. Está encendida. Desde hace tres días, si los vecinos tienen razón.", it="La candela. Brucia. Da tre giorni, se i vicini hanno ragione.")
    _t(tr,F,"books_reaction", en="In my books it says that burning candles beside the dead mark the transition. Some traditions believe the flame keeps the soul in place until unfinished business is done.", fr="Dans mes livres, il est dit que les bougies allumées près des morts marquent là transition. Certaines traditions croient que là flamme retient l'âme sur place jusqu'à ce que les affaires inachevées soient réglées.", es="En mis libros dice que las velas encendidas junto a los muertos marcan la transición. Algunas tradiciones creen que la llama mantiene el alma en el lugar hasta que los asuntos pendientes se resuelvan.", it="Nei miei libri c'è scritto che le candele accese accanto ai morti segnano il passaggio. Alcune tradizioni credono che la fiamma tenga l'anima sul posto fino a quando gli affari incompiuti non sono risolti.")
    _t(tr,F,"books_reaction_2", en="But no candle burns for three days without being refilled. This one is barely shorter than a new one.", fr="Mais aucune bougie ne brûle trois jours sans être rechargée. Celle-ci est à peine plus courte qu'une neuve.", es="Pero ninguna vela arde tres días sin ser rellenada. Esta apenas es más corta que una nueva.", it="Ma nessuna candela brucia per tre giorni senza essere riempita. Questa è appena più corta di una nuova.")
    _t(tr,F,"cross_reaction", en="Instinctively I reach for the chain around my neck, where Mother's crucifix hangs. The wood is warm under my fingers — warmer than it should be.", fr="Instinctivement, je touche là chaîne autour de mon cou, où pend le crucifix de Maman. Le bois est chaud sous mes doigts — plus chaud qu'il ne devrait.", es="Instintivamente toco la cadena alrededor de mi cuello, donde cuelga el crucifijo de mamá. La madera está cálida bajo mis dedos, más de lo que debería.", it="Istintivamente afferro la catenina al collo, dove pende il crocifisso della mamma. Il legno è caldo sotto le dita — più caldo di quanto dovrebbe.")
    _t(tr,F,"cross_reaction_2", en="Beside the bed I murmur a prayer. The words feel foreign in this room. As if they don't belong here.", fr="Au chevet du lit, je murmure une prière. Les mots semblent étrangers dans cette pièce. Comme s'ils n'avaient pas leur place ici.", es="Junto a la cama murmuro una oración. Las palabras se sienten ajenas en esta habitación. Como si no pertenecieran aquí.", it="Accanto al letto mormoro una preghiera. Le parole suonano estranee in questa stanza. Come se non appartenessero qui.")
    _t(tr,F,"camera_reaction", en="My first instinct is to raise the camera. To capture the scene. But then I lower it again. Some things don't belong on film.", fr="Mon premier réflexe est de lever l'appareil photo. De capturer là scène. Mais je le repose. Certaines choses n'ont pas leur place sur une pellicule.", es="Mi primer instinto es levantar la cámara. Capturar la escena. Pero luego la bajo otra vez. Algunas cosas no pertenecen a la película.", it="Il mio primo istinto è alzare la macchina fotografica. Catturare la scena. Ma poi la riabbasso. Alcune cose non appartengono alla pellicola.")
    _t(tr,F,"camera_reaction_2", en="Still — the candle. I photograph it up close. Through the viewfinder I see something I hadn't noticed with the naked eye: The wax doesn't drip downward. It spirals around the candle.", fr="Quand même — là bougie. Je là photographie de près. Dans le viseur, je vois quelque chose que je n'avais pas remarqué à l'œil nu : là cire ne coule pas vers le bas. Elle s'enroule en spirale autour de là bougie.", es="Aun así, la vela. La fotografío de cerca. Por el visor veo algo que no había notado a simple vista: la cera no gotea hacia abajo. Se enrosca en espiral alrededor de la vela.", it="Comunque — la candela. La fotografo da vicino. Attraverso il mirino vedo qualcosa che non avevo notato a occhio nudo: la cera non cola verso il basso. Si avvolge a spirale intorno alla candela.")
    _t(tr,F,"general_reaction", en="A shiver runs down my spine. The candle flickers, though there's no draft in the room. The flame bends — toward me.", fr="Un frisson me parcourt l'échine. Là bougie vacille, alors qu'il n'y à pas de courant d'air. Là flamme se penche — vers moi.", es="Un escalofrío me recorre la espalda. La vela parpadea, aunque no hay corriente de aire en la habitación. La llama se inclina — hacia mí.", it="Un brivido mi percorre la schiena. La candela tremola, anche se non c'è corrente nella stanza. La fiamma si piega — verso di me.")
    _t(tr,F,"meet_georg", en="Behind me, the wooden floor creaks. I spin around.", fr="Derrière moi, le plancher grince. Je me retourne vivement.", es="Detrás de mí, el suelo de madera cruje. Me giro de golpe.", it="Dietro di me, il pavimento di legno scricchiola. Mi giro di scatto.")
    _t(tr,F,"narration_georg_1", en="A man stands in the doorframe. Tall, broad-shouldered, with hands like shovels. His face is weathered, his eyes tired.", fr="Un homme se tient dans l'encadrement de là porte. Grand, large d'épaules, avec des mains comme des pelles. Son visage est buriné, ses yeux fatigués.", es="Un hombre está de pie en el marco de la puerta. Alto, de hombros anchos, con manos como palas. Su rostro está curtido, sus ojos cansados.", it="Un uomo sta sulla soglia. Alto, dalle spalle larghe, con mani come pale. Il suo viso è segnato dalle intemperie, i suoi occhi stanchi.")
    _t(tr,F,"narration_georg_2", en="Uncle Georg. Grandmother's only son. The blacksmith of Graubach.", fr="Oncle Georg. Le fils unique de grand-mère. Le forgeron de Graubach.", es="El tío Georg. El único hijo de la abuela. El herrero de Graubach.", it="Zio Georg. L'unico figlio della nonna. Il fabbro di Graubach.")
    _t(tr,F,"georg_1", en="Elise.", fr="Elise.", es="Elise.", it="Elise.")
    _t(tr,F,"georg_2", en="He says only my name. But in that one word lies so much — relief, guilt, and something that sounds like fear.", fr="Il ne dit que mon nom. Mais dans ce seul mot, il y à tant — du soulagement, de là culpabilité, et quelque chose qui ressemble à de là peur.", es="Solo dice mi nombre. Pero en esa única palabra hay tanto: alivio, culpa, y algo que suena a miedo.", it="Dice solo il mio nome. Ma in quella sola parola c'è così tanto — sollievo, senso di colpa, è qualcosa che suona come paura.")
    _t(tr,F,"georg_3", en="You came. I had hoped... and at the same time feared that you would.", fr="Tu es venue. J'avais espéré... et en même temps redouté que tu le fasses.", es="Has venido. Esperaba... y al mismo tiempo temía que lo hicieras.", it="Sei venuta. Speravo... è allo stesso tempo temevo che lo facessi.")
    _t(tr,F,"georg_5", en="Your grandmother... I'm sorry, child. We found her like this three days ago. Peaceful, people say. In her sleep.", fr="Tà grand-mère... je suis désolé, petite. On l'à trouvée comme çà il y à trois jours. Paisible, disent les gens. Dans son sommeil.", es="Tu abuela... lo siento, niña. La encontramos así hace tres días. En paz, dice la gente. Mientras dormía.", it="Tua nonna... mi dispiace, bambina. L'abbiamo trovata così tre giorni fa. Serena, dice la gente. Nel sonno.")
    _t(tr,F,"georg_6", en="But her face... she was smiling, Elise. As if she knew something that we don't.", fr="Mais son visage... elle souriait, Elise. Comme si elle savait quelque chose que nous ignorons.", es="Pero su rostro... estaba sonriendo, Elise. Como si supiera algo que nosotros no sabemos.", it="Ma il suo viso... sorrideva, Elise. Come se sapesse qualcosa che noi non sappiamo.")
    _tc(tr, F, "choice_georg",
        en_choices=["Who sent the letter? It was postmarked today.", "Why is the candle still burning after three days?", "What are those notes on the nightstand?"],
        fr_choices=["Qui a envoyé la lettre ? Le cachet est d'aujourd'hui.", "Pourquoi la bougie brûle-t-elle encore après trois jours ?", "Ce sont quoi, ces notes sur la table de nuit ?"],
        es_choices=["¿Quién envió la carta? Tiene matasellos de hoy.", "¿Por qué la vela sigue encendida después de tres días?", "¿Qué son esas notas en la mesita de noche?"],
        it_choices=["Chi ha spedito la lettera? Il timbro è di oggi.", "Perché la candela brucia ancora dopo tre giorni?", "Cosa sono quegli appunti sul comodino?"])
    _t(tr,F,"georg_letter_1", en="Letter? What letter?", fr="Lettre ? Quelle lettre ?", es="¿Carta? ¿Qué carta?", it="Lettera? Quale lettera?")
    _t(tr,F,"georg_letter_2", en="I show him the envelope. Georg turns pale. His large hands tremble as he touches it.", fr="Je lui montre l'enveloppe. Georg pâlit. Ses grandes mains tremblent quand il là touche.", es="Le muestro el sobre. Georg palidece. Sus grandes manos tiemblan al tocarlo.", it="Gli mostro la busta. Georg impallidisce. Le sue grandi mani tremano quando la tocca.")
    _t(tr,F,"georg_letter_3", en="That's... that's her handwriting. But Elise — we don't have a post office in Graubach. Not anymore. And the nearest one is two days' journey away.", fr="C'est... c'est son écriture. Mais Elise — nous n'avons pas de bureau de poste à Graubach. Plus maintenant. Et le plus proche est à deux jours de voyage.", es="Es... es su letra. Pero Elise, no tenemos oficina de correos en Graubach. Ya no. Y la más cercana está a dos días de viaje.", it="È... è la sua calligrafia. Ma Elise — non abbiamo un ufficio postale a Graubach. Non più. È il più vicino è a due giorni di viaggio.")
    _t(tr,F,"georg_letter_5", en="This letter... it can't exist.", fr="Cette lettre... elle ne peut pas exister.", es="Esta carta... no puede existir.", it="Questa lettera... non può esistere.")
    _t(tr,F,"georg_candle_1", en="The candle... Yes. We tried to put it out. On the first day already.", fr="Là bougie... Oui. Nous avons essayé de l'éteindre. Dès le premier jour.", es="La vela... Sí. Intentamos apagarla. Ya el primer día.", it="La candela... Sì. Abbiamo provato a spegnerla. Già il primo giorno.")
    _t(tr,F,"georg_candle_2", en="Georg swallows hard. He looks at the candle like an enemy he cannot defeat.", fr="Georg déglutit difficilement. Il regarde là bougie comme un ennemi qu'il ne peut vaincre.", es="Georg traga saliva. Mira la vela como a un enemigo que no puede vencer.", it="Georg deglutisce a fatica. Guarda la candela come un nemico che non riesce a sconfiggere.")
    _t(tr,F,"georg_candle_3", en="It won't go out, Elise. We blew, poured water over it, cut the wick. The next morning it was burning again.", fr="Elle ne s'éteint pas, Elise. Nous avons soufflé, versé de l'eau, coupé là mèche. Le lendemain matin, elle brûlait à nouveau.", es="No se apaga, Elise. Soplamos, le echamos agua, cortamos la mecha. A la mañana siguiente estaba encendida otra vez.", it="Non si spegne, Elise. Abbiamo soffiato, versato acqua, tagliato lo stoppino. La mattina dopo bruciava di nuovo.")
    _t(tr,F,"georg_candle_4", en="Don't put it out. Please. I don't know why, but... don't put it out.", fr="Ne l'éteignez pas. S'il vous plaît. Je ne sais pas pourquoi, mais... ne l'éteignez pas.", es="No la apagues. Por favor. No sé por qué, pero... no la apagues.", it="Non spegnerla. Per favore. Non so perché, ma... non spegnerla.")
    _t(tr,F,"georg_notes_1", en="Don't touch those! Not... not now.", fr="N'y touche pas ! Pas... pas maintenant.", es="¡No toques eso! No... no ahora.", it="Non toccarli! Non... non adesso.")
    _t(tr,F,"georg_notes_2", en="Georg flinches, startled, as if he hadn't expected to react so strongly. He runs a hand over his face.", fr="Georg sursaute, surpris, comme s'il ne s'attendait pas à réagir si vivement. Il se passe là main sur le visage.", es="Georg se sobresalta, asustado, como si no esperara reaccionar tan fuerte. Se pasa la mano por la cara.", it="Georg sussulta, spaventato, come se non si aspettasse di reagire così violentemente. Si passa una mano sul viso.")
    _t(tr,F,"georg_notes_3", en="Forgive me. It's... your grandmother wrote a lot in the last weeks. Day and night. As if time were running out for her.", fr="Pardonne-moi. C'est que... tà grand-mère à beaucoup écrit ces dernières semaines. Jour et nuit. Comme si le temps lui manquait.", es="Perdóname. Es que... tu abuela escribió mucho en las últimas semanas. Día y noche. Como si se le acabara el tiempo.", it="Perdonami. È che... tua nonna ha scritto molto nelle ultime settimane. Giorno è notte. Come se il tempo le stesse sfuggendo.")
    _t(tr,F,"georg_notes_4", en="I looked inside. Once. It gave me... it gave me nightmares, Elise. But perhaps you're the one who needs to read it.", fr="J'ai regardé dedans. Une fois. Çà m'à donné... çà m'à donné des cauchemars, Elise. Mais peut-être es-tu celle qui doit le lire.", es="Miré dentro. Una vez. Me dio... me dio pesadillas, Elise. Pero quizás tú eres quien debe leerlo.", it="Ci ho guardato dentro. Una volta. Mi ha dato... mi ha dato gli incubi, Elise. Ma forse sei tu quella che deve leggerlo.")
    _t(tr,F,"georg_converge", en="Outside it grows dark. The shadows in the room's corners deepen. The candle throws flickering lights on the wall.", fr="Dehors, il fait nuit. Les ombres dans les coins de là pièce s'approfondissent. Là bougie projette des lumières vacillantes sur le mur.", es="Afuera oscurece. Las sombras en las esquinas de la habitación se profundizan. La vela proyecta luces parpadeantes en la pared.", it="Fuori si fa buio. Le ombre negli angoli della stanza si approfondiscono. La candela proietta luci tremolanti sulla parete.")
    _t(tr,F,"sound_bells", en="Then I hear it. The church bell. Once. Twice. Three times.", fr="Alors je l'entends. Là cloche de l'église. Une fois. Deux fois. Trois fois.", es="Entonces lo oigo. La campana de la iglesia. Una vez. Dos veces. Tres veces.", it="Poi lo sento. La campana della chiesa. Una volta. Due volte. Tre volte.")
    _t(tr,F,"narration_bells_2", en="It's not a full hour. And the sound is... wrong. Too deep. As if it comes not from the tower but from underground.", fr="Ce n'est pas une heure pleine. Et le son est... faux. Trop profond. Comme s'il venait non pas du clocher, mais de sous terre.", es="No es una hora en punto. Y el sonido es... extraño. Demasiado profundo. Como si no viniera de la torre, sino de bajo tierra.", it="Non è un'ora piena. È il suono è... sbagliato. Troppo profondo. Come se provenisse non dalla torre, ma dal sottosuolo.")
    _t(tr,F,"georg_react_1", en="Georg freezes. All color drains from his face. He grabs the doorframe as if needing support.", fr="Georg se fige. Toute couleur quitte son visage. Il agrippe le cadre de là porte comme s'il avait besoin de soutien.", es="Georg se paraliza. Todo el color abandona su rostro. Se agarra al marco de la puerta como si necesitara apoyo.", it="Georg si immobilizza. Tutto il colore abbandona il suo viso. Si aggrappa allo stipite come se avesse bisogno di sostegno.")
    _t(tr,F,"georg_react_2", en="I have to go. Right now.", fr="Je dois partir. Tout de suite.", es="Tengo que irme. Ahora mismo.", it="Devo andare. Subito.")
    _t(tr,F,"georg_react_3", en="Elise, listen to me. Stay here tonight. Lock the door. Bar it. And if someone knocks — if someone knocks, don't open.", fr="Elise, écoute-moi. Reste ici cette nuit. Ferme là porte à clé. Mets le verrou. Et si on frappe — si on frappe, n'ouvre pas.", es="Elise, escúchame. Quédate aquí esta noche. Cierra la puerta con llave. Pon el cerrojo. Y si alguien llama — si alguien llama, no abras.", it="Elise, ascoltami. Resta qui stanotte. Chiudi la porta a chiave. Metti il catenaccio. È se qualcuno bussa — se qualcuno bussa, non aprire.")
    _tc(tr, F, "choice_georg_leave",
        en_choices=["What's going on, Georg? Tell me the truth!", "Where are you going? Can I come with you?", "...Alright. I'll stay here."],
        fr_choices=["Que se passe-t-il, Georg ? Dis-moi la vérité !", "Où vas-tu ? Je peux venir avec toi ?", "...D'accord. Je reste ici."],
        es_choices=["¿Qué está pasando, Georg? ¡Dime la verdad!", "¿Adónde vas? ¿Puedo ir contigo?", "...Está bien. Me quedo aquí."],
        it_choices=["Cosa sta succedendo, Georg? Dimmi la verità!", "Dove vai? Posso venire con te?", "...Va bene. Resto qui."])
    _t(tr,F,"georg_demand_1", en="The truth? The truth is that I can't tell you everything. Not yet. It wouldn't make sense.", fr="Là vérité ? Là vérité, c'est que je ne peux pas tout te dire. Pas encore. Çà n'aurait pas de sens.", es="¿La verdad? La verdad es que no puedo contarte todo. Todavía no. No tendría sentido.", it="La verità? La verità è che non posso dirti tutto. Non ancora. Non avrebbe senso.")
    _t(tr,F,"georg_demand_2", en="Tomorrow. Tomorrow we'll have breakfast together, and I'll tell you... as much as I can. But tonight — please, Elise. Trust me.", fr="Demain. Demain, on déjeunerà ensemble, et je te raconterai... autant que je peux. Mais ce soir — s'il te plaît, Elise. Fais-moi confiance.", es="Mañana. Mañana desayunaremos juntos, y te contaré... todo lo que pueda. Pero esta noche — por favor, Elise. Confía en mí.", it="Domani. Domani faremo colazione insieme, è ti racconterò... tutto quello che posso. Ma stanotte — per favore, Elise. Fidati di me.")
    _t(tr,F,"georg_follow_1", en="No! Absolutely not. Not at night. Not... you must not go outside at night, Elise. Promise me.", fr="Non ! En aucun cas. Pas là nuit. Pas... tu ne dois pas sortir là nuit, Elise. Promets-le-moi.", es="¡No! De ninguna manera. No de noche. No... no debes salir de noche, Elise. Prométemelo.", it="No! Assolutamente no. Non di notte. Non... non devi uscire di notte, Elise. Promettimelo.")
    _t(tr,F,"georg_follow_2", en="The fear in his eyes is real. Georg was never a man who scared easily. As a child, I once saw him stop a runaway horse with his bare hands.", fr="Là peur dans ses yeux est réelle. Georg n'à jamais été un homme facilement effrayé. Enfant, je l'ai vu arrêter un cheval emballé à mains nues.", es="El miedo en sus ojos es real. Georg nunca fue un hombre que se asustara fácilmente. De niña lo vi detener un caballo desbocado con las manos desnudas.", it="La paura nei suoi occhi è reale. Georg non è mai stato un uomo che si spaventava facilmente. Da bambina l'ho visto fermare un cavallo imbizzarrito a mani nude.")
    _t(tr,F,"georg_quiet", en="Georg looks at me. A long moment. Then he nods, and I see relief in his eyes — and at the same time, deep sadness.", fr="Georg me regarde. Un long moment. Puis il hoche là tête, et je vois du soulagement dans ses yeux — et en même temps, une profonde tristesse.", es="Georg me mira. Un largo momento. Luego asiente, y veo alivio en sus ojos — y al mismo tiempo, una profunda tristeza.", it="Georg mi guarda. A lungo. Poi annuisce, è vedo sollievo nei suoi occhi — è allo stesso tempo, una profonda tristezza.")
    _t(tr,F,"georg_quiet_2", en="You're like your grandmother. Stronger than you know.", fr="Tu es comme tà grand-mère. Plus forte que tu ne le crois.", es="Eres como tu abuela. Más fuerte de lo que crees.", it="Sei come tua nonna. Più forte di quanto pensi.")
    _t(tr,F,"narration_alone_1", en="The door falls shut. I slide the bolt, as Georg said.", fr="Là porte se ferme. Je pousse le verrou, comme Georg l'à dit.", es="La puerta se cierra de golpe. Echo el cerrojo, como dijo Georg.", it="La porta si chiude. Faccio scorrere il catenaccio, come ha detto Georg.")
    _t(tr,F,"narration_alone_2", en="Alone. With my grandmother's body. And a candle that won't go out.", fr="Seule. Avec le corps de mà grand-mère. Et une bougie qui refuse de s'éteindre.", es="Sola. Con el cuerpo de mi abuela. Y una vela que no quiere apagarse.", it="Sola. Con il corpo di mia nonna. È una candela che non vuole spegnersi.")
    _t(tr,F,"narration_alone_3", en="Outside it's completely dark now. No light comes through the shutters. No moon, no stars. Only the heavy, saturated blackness of a November evening in the Black Forest.", fr="Dehors, il fait complètement nuit maintenant. Aucune lumière ne filtre à travers les volets. Pas de lune, pas d'étoiles. Seulement là noirceur lourde et saturée d'un soir de novembre dans là Forêt-Noire.", es="Afuera está completamente oscuro. Ninguna luz se filtra por las contraventanas. Ni luna, ni estrellas. Solo la oscuridad densa y saturada de una noche de noviembre en la Selva Negra.", it="Fuori è completamente buio. Nessuna luce filtra attraverso le imposte. Niente luna, niente stelle. Solo l'oscurità densa è satura di una sera di novembre nella Foresta Nera.")
    _t(tr,F,"narration_alone_4", en="I sit at the kitchen table. Grandmother's teapot is still there, half full. Beside it, a half-eaten piece of bread, hard as wood.", fr="Je m'assois à là table de là cuisine. Là théière de grand-mère est encore là, à moitié pleine. À côté, un morceau de pain entamé, dur comme du bois.", es="Me siento a la mesa de la cocina. La tetera de la abuela todavía está ahí, medio llena. Al lado, un trozo de pan a medio comer, duro como la madera.", it="Mi siedo al tavolo della cucina. La teiera della nonna è ancora lì, mezza piena. Accanto, un pezzo di pane morsicato, duro come il legno.")
    _t(tr,F,"narration_alone_5", en="Three days. She's been dead for three days, but the letter was postmarked today. The candle still burns. And the church bells ring at no hour.", fr="Trois jours. Elle est morte depuis trois jours, mais là lettre à été postée aujourd'hui. Là bougie brûle toujours. Et les cloches sonnent en dehors des heures.", es="Tres días. Lleva muerta tres días, pero la carta tiene matasellos de hoy. La vela sigue encendida. Y las campanas suenan fuera de hora.", it="Tre giorni. È morta da tre giorni, ma la lettera ha il timbro di oggi. La candela brucia ancora. È le campane suonano a nessun'ora.")
    _t(tr,F,"journal_grandmother", en="Grandmother Margarethe", fr="Grand-mère Margarethe", es="Abuela Margarethe", it="Nonna Margarethe", field="title")
    _t(tr,F,"journal_grandmother", en="Grandmother is dead. Three days ago, Georg says. But the letter arrived today. The candle by her bed can't be extinguished. Georg is afraid — truly, deeply afraid. What is he hiding?", fr="Grand-mère est morte. Depuis trois jours, dit Georg. Mais là lettre est arrivée aujourd'hui. Là bougie à son chevet ne s'éteint pas. Georg à peur — une peur vraie, profonde. Que cache-t-il ?", es="La abuela está muerta. Hace tres días, dice Georg. Pero la carta llegó hoy. La vela junto a su cama no se puede apagar. Georg tiene miedo — un miedo real, profundo. ¿Qué esconde?", it="La nonna è morta. Da tre giorni, dice Georg. Ma la lettera è arrivata oggi. La candela accanto al suo letto non si può spegnere. Georg ha paura — vera, profonda paura. Cosa nasconde?", field="content")
    _t(tr,F,"journal_georg_entry", en="Uncle Georg", fr="Oncle Georg", es="Tío Georg", it="Zio Georg", field="title")
    _t(tr,F,"journal_georg_entry", en="Georg has changed. Older, more tired, guilt-ridden. He warned me about the night, wouldn't say why. The church bells frightened him — as if they were a signal.", fr="Georg à changé. Plus vieux, plus fatigué, rongé par là culpabilité. Il m'à mise en garde contre là nuit, sans dire pourquoi. Les cloches l'ont effrayé — comme si c'était un signal.", es="Georg ha cambiado. Más viejo, más cansado, atormentado por la culpa. Me advirtió sobre la noche, sin decir por qué. Las campanas lo asustaron — como si fueran una señal.", it="Georg è cambiato. Più vecchio, più stanco, tormentato dal senso di colpa. Mi ha avvertita sulla notte, senza dire perché. Le campane lo hanno spaventato — come se fossero un segnale.", field="content")


# Remaining act functions - translate from German dialogue JSONs
# Each reads the original JSON and provides translations

    # --- Additional translations (auto-generated) ---

    _t(tr, F, "elise_grief_1",
       en="Grandmother...? No... No, please not.",
       fr="Grand-mère... ? Non... Non, pas ça, je vous en prie.",
       es="Abuela...? No... No, por favor no.",
       it="Nonna...? No... No, ti prego, no.")

    _t(tr, F, "narration_grief_2",
       en="My knees give way. I sink onto the edge of the bed and hold her cold hand in both of mine. My fingers tremble. Tears run down my face before I notice it.",
       fr="Mes genoux lâchent. Je m'effondre au bord du lit et tiens sa main froide entre les miennes. Mes doigts tremblent. Des larmes coulent sur mon visage avant que je ne m'en rende compte.",
       es="Mis rodillas ceden. Me desplomo en el borde de la cama y sostengo su mano fría entre las mías. Mis dedos tiemblan. Las lágrimas corren por mi rostro antes de que me dé cuenta.",
       it="Le ginocchia cedono. Mi lascio cadere sul bordo del letto e stringo la sua mano fredda tra le mie. Le dita mi tremano. Le lacrime mi scorrono sul viso prima che me ne accorga.")

    _t(tr, F, "narration_grief_3",
       en="The last time I held this hand was ten years ago. At the station in Waldkirch, when grandmother slipped dried arnica into my bag as a farewell. \"Come back soon,\" she had said. \"Promise me.\"",
       fr="La dernière fois que j'ai tenu cette main, c'était il y a dix ans. À la gare de Waldkirch, quand grand-mère avait glissé de l'arnica séchée dans mon sac en guise d'adieu. \"Reviens vite\", avait-elle dit. \"Promets-le-moi.\"",
       es="La última vez que sostuve esta mano fue hace diez años. En la estación de Waldkirch, cuando la abuela me metió árnica seca en el bolso como despedida. \"Vuelve pronto\", había dicho. \"Prométemelo.\"",
       it="L'ultima volta che ho stretto questa mano è stato dieci anni fa. Alla stazione di Waldkirch, quando la nonna mi infilò dell'arnica essiccata nella borsa come saluto. \"Torna presto\", aveva detto. \"Promettimelo.\"")

    _t(tr, F, "narration_grief_4",
       en="I promised. And then came the university, the seminars, the inflation, and always a reason not to go. Ten years of excuses.",
       fr="J'ai promis. Et puis sont venues l'université, les séminaires, l'inflation, et toujours une raison de ne pas y aller. Dix ans d'excuses.",
       es="Lo prometí. Y luego vinieron la universidad, los seminarios, la inflación, y siempre una razón para no ir. Diez años de excusas.",
       it="Ho promesso. E poi sono arrivati l'università, i seminari, l'inflazione, e sempre un motivo per non andare. Dieci anni di scuse.")

    _t(tr, F, "elise_grief_5",
       en="I'm sorry. I'm so sorry that I didn't come sooner.",
       fr="Je suis désolée. Je suis tellement désolée de ne pas être venue plus tôt.",
       es="Lo siento. Siento tanto no haber venido antes.",
       it="Mi dispiace. Mi dispiace tanto di non essere venuta prima.")

    _t(tr, F, "narration_grief_6",
       en="I wipe my eyes. My gaze falls on the nightstand, and through the veil of tears I see three things standing there.",
       fr="J'essuie mes yeux. Mon regard tombe sur la table de nuit, et à travers le voile de larmes, je vois trois choses qui s'y trouvent.",
       es="Me seco los ojos. Mi mirada cae sobre la mesita de noche, y a través del velo de lágrimas veo tres cosas que hay allí.",
       it="Mi asciugo gli occhi. Il mio sguardo cade sul comodino, e attraverso il velo di lacrime vedo tre cose posate lì.")

    _t(tr, F, "elise_books_react",
       en="Three days... No candle burns for three days. Not without help. In Black Forest traditions there are soul-lights that only go out when the dead find their peace.",
       fr="Trois jours... Aucune bougie ne brûle trois jours. Pas sans aide. Dans les traditions de la Forêt-Noire, il existe des lumières d'âmes qui ne s'éteignent que lorsque le mort trouve la paix.",
       es="Tres días... Ninguna vela arde tres días. No sin ayuda. En las tradiciones de la Selva Negra existen luces del alma que solo se apagan cuando el muerto encuentra su paz.",
       it="Tre giorni... Nessuna candela brucia per tre giorni. Non senza aiuto. Nelle tradizioni della Foresta Nera esistono luci dell'anima che si spengono solo quando il defunto trova la pace.")

    _t(tr, F, "elise_cross_react",
       en="Something in this room doesn't feel right. The crucifix is warm. The air is heavy. And this candle... it should have gone out long ago.",
       fr="Quelque chose dans cette pièce ne va pas. Le crucifix est chaud. L'air est lourd. Et cette bougie... elle aurait dû s'éteindre depuis longtemps.",
       es="Algo en esta habitación no se siente bien. El crucifijo está caliente. El aire es pesado. Y esta vela... debería haberse apagado hace mucho.",
       it="Qualcosa in questa stanza non va. Il crocifisso è caldo. L'aria è pesante. E questa candela... avrebbe dovuto spegnersi da tempo.")

    _t(tr, F, "elise_camera_react",
       en="The wax spirals... like the symbol on the letter. That's no coincidence. Something is keeping this flame alive.",
       fr="La cire s'enroule en spirale... comme le symbole sur la lettre. Ce n'est pas une coïncidence. Quelque chose maintient cette flamme en vie.",
       es="La cera forma espirales... como el símbolo de la carta. Eso no es coincidencia. Algo mantiene esta llama con vida.",
       it="La cera si avvolge a spirale... come il simbolo sulla lettera. Non è una coincidenza. Qualcosa tiene viva questa fiamma.")

    _t(tr, F, "elise_general_react",
       en="I take a step back. The flame follows my movement. Impossible. And yet it happens, right before my eyes.",
       fr="Je recule d'un pas. La flamme suit mon mouvement. Impossible. Et pourtant cela se produit, juste sous mes yeux.",
       es="Doy un paso atrás. La llama sigue mi movimiento. Imposible. Y sin embargo sucede, justo ante mis ojos.",
       it="Faccio un passo indietro. La fiamma segue il mio movimento. Impossibile. Eppure accade, proprio davanti ai miei occhi.")

    _t(tr, F, "elise_sees_georg",
       en="Georg...? You look... you look terrible.",
       fr="Georg... ? Tu as l'air... tu as l'air terrible.",
       es="Georg...? Estás... tienes un aspecto terrible.",
       it="Georg...? Hai... hai un aspetto terribile.")

    _t(tr, F, "elise_responds_1",
       en="When did she die? What happened?",
       fr="Quand est-elle morte ? Que s'est-il passé ?",
       es="¿Cuándo murió? ¿Qué pasó?",
       it="Quando è morta? Cos'è successo?")

    _t(tr, F, "elise_responds_2",
       en="Three days? Why didn't anyone let me know? I could have come right away!",
       fr="Trois jours ? Pourquoi personne ne m'a prévenue ? J'aurais pu venir tout de suite !",
       es="¿Tres días? ¿Por qué nadie me avisó? ¡Podría haber venido enseguida!",
       it="Tre giorni? Perché nessuno mi ha avvisata? Sarei potuta venire subito!")

    _t(tr, F, "georg_explains",
       en="There's no telephone in Graubach. And the nearest telegraph is in Freiburg. Elise, I didn't want you to come here alone. Not now.",
       fr="Il n'y a pas de téléphone à Graubach. Et le télégraphe le plus proche est à Fribourg. Elise, je ne voulais pas que tu viennes seule ici. Pas maintenant.",
       es="No hay teléfono en Graubach. Y el telégrafo más cercano está en Friburgo. Elise, no quería que vinieras sola. No ahora.",
       it="Non c'è telefono a Graubach. E il telegrafo più vicino è a Friburgo. Elise, non volevo che venissi qui da sola. Non adesso.")

    _t(tr, F, "elise_responds_3",
       en="She was smiling...? Grandmother never smiled in her sleep. Never. What did she see?",
       fr="Elle souriait... ? Grand-mère ne souriait jamais dans son sommeil. Jamais. Qu'a-t-elle vu ?",
       es="¿Estaba sonriendo...? La abuela nunca sonreía al dormir. Nunca. ¿Qué vio?",
       it="Sorrideva...? La nonna non sorrideva mai nel sonno. Mai. Cosa ha visto?")

    _t(tr, F, "narration_elise_looks",
       en="I look back into the bedroom. Grandmother's smile in the candlelight. It doesn't look peaceful. It looks knowing. As if she had set something in motion that now takes its course.",
       fr="Je regarde à nouveau dans la chambre. Le sourire de grand-mère à la lueur de la bougie. Il ne semble pas paisible. Il semble entendu. Comme si elle avait mis quelque chose en marche qui suit désormais son cours.",
       es="Miro de nuevo al dormitorio. La sonrisa de la abuela a la luz de la vela. No parece serena. Parece sabia. Como si hubiera puesto algo en marcha que ahora sigue su curso.",
       it="Guardo di nuovo nella camera da letto. Il sorriso della nonna alla luce della candela. Non sembra sereno. Sembra consapevole. Come se avesse messo in moto qualcosa che ora fa il suo corso.")

    _t(tr, F, "georg_letter_exclusive",
       en="Things happen in Graubach that shouldn't happen. The letter is still the most harmless of them. Believe me, Elise.",
       fr="À Graubach, des choses se produisent qui ne devraient pas se produire. La lettre est encore la plus anodine d'entre elles. Crois-moi, Elise.",
       es="En Graubach pasan cosas que no deberían pasar. La carta es todavía lo más inofensivo. Créeme, Elise.",
       it="A Graubach accadono cose che non dovrebbero accadere. La lettera è ancora la più innocua. Credimi, Elise.")

    _t(tr, F, "elise_candle_react",
       en="That's impossible. Candles go out when you cut the wick. That's... Georg, that defies all physics.",
       fr="C'est impossible. Les bougies s'éteignent quand on coupe la mèche. C'est... Georg, ça défie toute physique.",
       es="Eso es imposible. Las velas se apagan cuando cortas la mecha. Eso... Georg, eso desafía toda la física.",
       it="Questo è impossibile. Le candele si spengono quando si taglia lo stoppino. Questo... Georg, questo sfida ogni legge della fisica.")

    _t(tr, F, "georg_candle_exclusive",
       en="The evening before she died, Margarethe lit the candle. She said: \"This flame is for Elise. It will burn until she comes.\" I thought she was talking nonsense. But here you are. And the candle burns.",
       fr="Le soir avant sa mort, Margarethe a allumé la bougie. Elle a dit : \"Cette flamme est pour Elise. Elle brûlera jusqu'à ce qu'elle vienne.\" Je pensais qu'elle divaguait. Mais te voilà. Et la bougie brûle.",
       es="La noche antes de morir, Margarethe encendió la vela. Dijo: \"Esta llama es para Elise. Arderá hasta que ella venga.\" Pensé que deliraba. Pero aquí estás. Y la vela arde.",
       it="La sera prima di morire, Margarethe accese la candela. Disse: \"Questa fiamma è per Elise. Brucerà finché lei non verrà.\" Pensavo che vaneggiasse. Ma eccoti qui. E la candela brucia.")

    _t(tr, F, "elise_notes_react",
       en="Nightmares? Georg, I'm a folklorist. I've read hundreds of horror stories. What's in a notebook that gives YOU nightmares?",
       fr="Des cauchemars ? Georg, je suis folkloriste. J'ai lu des centaines d'histoires d'horreur. Qu'y a-t-il dans un carnet qui TE donne des cauchemars ?",
       es="¿Pesadillas? Georg, soy folclorista. He leído cientos de historias de terror. ¿Qué hay en un cuaderno que a TI te da pesadillas?",
       it="Incubi? Georg, sono una folklorista. Ho letto centinaia di storie dell'orrore. Cosa c'è in un quaderno che dà gli incubi a TE?")

    _t(tr, F, "georg_notes_exclusive",
       en="She wrote about the teacher. Konrad Mueller. About what... lives INSIDE him. Elise — promise me: stay away from Konrad.",
       fr="Elle a écrit sur l'instituteur. Konrad Mueller. Sur ce qui... VIT EN lui. Elise — promets-moi : reste loin de Konrad.",
       es="Escribió sobre el maestro. Konrad Mueller. Sobre lo que... VIVE DENTRO de él. Elise — prométeme: mantente alejada de Konrad.",
       it="Ha scritto dell'insegnante. Konrad Mueller. Di quello che... VIVE DENTRO di lui. Elise — promettimi: stai lontana da Konrad.")

    _t(tr, F, "elise_demand_farewell",
       en="Tomorrow, Georg. But tomorrow I want the whole truth. No half measures.",
       fr="Demain, Georg. Mais demain je veux toute la vérité. Pas de demi-mesures.",
       es="Mañana, Georg. Pero mañana quiero toda la verdad. Nada a medias.",
       it="Domani, Georg. Ma domani voglio tutta la verità. Niente mezze misure.")

    _t(tr, F, "elise_follow_farewell",
       en="I promise. But you — be careful too. Please.",
       fr="Je te le promets. Mais toi aussi — sois prudent. S'il te plaît.",
       es="Lo prometo. Pero tú — ten cuidado también. Por favor.",
       it="Lo prometto. Ma tu — stai attento anche tu. Per favore.")

    _t(tr, F, "elise_quiet_farewell",
       en="I say nothing. But as the door closes, I place my hand against it. On the other side I hear Georg pause. A moment. Then his footsteps recede, heavy and slow.",
       fr="Je ne dis rien. Mais quand la porte se ferme, je pose ma main dessus. De l'autre côté, j'entends Georg s'arrêter. Un instant. Puis ses pas s'éloignent, lourds et lents.",
       es="No digo nada. Pero cuando la puerta se cierra, pongo mi mano contra ella. Al otro lado oigo a Georg detenerse. Un momento. Luego sus pasos se alejan, pesados y lentos.",
       it="Non dico nulla. Ma quando la porta si chiude, appoggio la mano contro di essa. Dall'altra parte sento Georg fermarsi. Un istante. Poi i suoi passi si allontanano, pesanti e lenti.")

    _t(tr, F, "narration_alone_search_1",
       en="I can't sleep. Not now. Instead I walk through the house. Grandmother's wardrobe: her scarf, still smelling of lavender. Knitting needles with half-finished work, as if she had only paused briefly.",
       fr="Je ne peux pas dormir. Pas maintenant. À la place, je parcours la maison. L'armoire de grand-mère : son écharpe, qui sent encore la lavande. Des aiguilles à tricoter avec un ouvrage inachevé, comme si elle n'avait fait qu'une courte pause.",
       es="No puedo dormir. No ahora. En cambio, recorro la casa. El armario de la abuela: su bufanda, que aún huele a lavanda. Agujas de tejer con un trabajo a medio hacer, como si solo hubiera hecho una breve pausa.",
       it="Non riesco a dormire. Non adesso. Invece cammino per la casa. L'armadio della nonna: la sua sciarpa, che profuma ancora di lavanda. I ferri da maglia con un lavoro a metà, come se avesse solo fatto una breve pausa.")

    _t(tr, F, "narration_alone_search_2",
       en="In a drawer: dried herbs in linen sachets, candle stubs with strange notches, a bundle of yellowed letters. And beneath — my childhood drawings. She kept them all.",
       fr="Dans un tiroir : des herbes séchées dans des sachets de lin, des bouts de bougie avec d'étranges entailles, une liasse de lettres jaunies. Et en dessous — mes dessins d'enfant. Elle les a tous gardés.",
       es="En un cajón: hierbas secas en saquitos de lino, cabos de vela con muescas extrañas, un fajo de cartas amarillentas. Y debajo — mis dibujos de infancia. Los guardó todos.",
       it="In un cassetto: erbe essiccate in sacchetti di lino, mozziconi di candela con strane tacche, un fascio di lettere ingiallite. E sotto — i miei disegni da bambina. Li ha conservati tutti.")

    _t(tr, F, "elise_finds_photo",
       en="Behind the drawings is a photograph. Me, perhaps seven years old, on grandmother's lap. Both of us laughing. Summer light falls through an open window.",
       fr="Derrière les dessins, il y a une photographie. Moi, peut-être sept ans, sur les genoux de grand-mère. Nous rions toutes les deux. La lumière d'été entre par une fenêtre ouverte.",
       es="Detrás de los dibujos hay una fotografía. Yo, quizás de siete años, en el regazo de la abuela. Las dos riendo. La luz del verano entra por una ventana abierta.",
       it="Dietro i disegni c'è una fotografia. Io, forse a sette anni, in grembo alla nonna. Ridiamo entrambe. La luce estiva entra da una finestra aperta.")

    _t(tr, F, "narration_photo",
       en="On the back, in grandmother's handwriting: \"My light against the darkness.\" The word \"light\" is underlined. Three times.",
       fr="Au dos, de l'écriture de grand-mère : \"Ma lumière contre les ténèbres.\" Le mot \"lumière\" est souligné. Trois fois.",
       es="En el reverso, con la letra de la abuela: \"Mi luz contra la oscuridad.\" La palabra \"luz\" está subrayada. Tres veces.",
       it="Sul retro, nella calligrafia della nonna: \"La mia luce contro l'oscurità.\" La parola \"luce\" è sottolineata. Tre volte.")

    _t(tr, F, "elise_cries",
       en="I'm here, grandmother. Too late... but I'm here.",
       fr="Je suis là, grand-mère. Trop tard... mais je suis là.",
       es="Estoy aquí, abuela. Demasiado tarde... pero estoy aquí.",
       it="Sono qui, nonna. Troppo tardi... ma sono qui.")

    _t(tr, F, "narration_alone_sounds",
       en="At some point in the silence I hear it. Soft, deep, barely more than a vibration in the floorboards. Singing? No — more like a hum. Like a lullaby that comes from the ground itself.",
       fr="À un moment dans le silence, je l'entends. Doux, profond, à peine plus qu'une vibration dans les lattes du plancher. Un chant ? Non — plutôt un bourdonnement. Comme une berceuse qui émane du sol lui-même.",
       es="En algún momento del silencio lo oigo. Suave, profundo, apenas más que una vibración en las tablas del suelo. ¿Canto? No — más bien un zumbido. Como una nana que sale del suelo mismo.",
       it="A un certo punto nel silenzio lo sento. Sommesso, profondo, appena più di una vibrazione nelle assi del pavimento. Un canto? No — più un ronzio. Come una ninna nanna che viene dal suolo stesso.")

    _t(tr, F, "elise_alone_resolve",
       en="Tomorrow. Tomorrow I'll start to understand.",
       fr="Demain. Demain je commencerai à comprendre.",
       es="Mañana. Mañana empezaré a entender.",
       it="Domani. Domani comincerò a capire.")


def _add_act1_first_night(tr):
    F = "res://data/dialogue/act1/first_night.json"
    _t(tr,F,"narration_1", en="Hours pass. Or minutes. In the glow of the inhuman candle, time loses its meaning.", fr="Les heures passent. Ou les minutes. À là lueur de l'inhumaine bougie, le temps perd son sens.", es="Pasan las horas. O los minutos. A la luz de la inhumana vela, el tiempo pierde su significado.", it="Passano le ore. O i minuti. Al bagliore dell'inumana candela, il tempo perde significato.")
    _t(tr,F,"narration_2", en="I sit at the kitchen table staring at grandmother's notebook. It lies in the bedroom. Georg's words echo in my head.", fr="Je suis assise à là table de là cuisine, fixant le carnet de grand-mère. Il est dans là chambre. Les mots de Georg résonnent dans mà tête.", es="Estoy sentada a la mesa de la cocina mirando fijamente el cuaderno de la abuela. Está en el dormitorio. Las palabras de Georg resuenan en mi cabeza.", it="Siedo al tavolo della cucina fissando il quaderno della nonna. È nella camera da letto. Le parole di Georg mi riecheggiano nella testa.")
    _t(tr,F,"narration_3", en="\"I looked inside. Once. It gave me nightmares.\"", fr="\"J'ai regardé dedans. Une fois. Ça m'a donné des cauchemars.\"", es="\"Miré dentro. Una vez. Me dio pesadillas.\"", it="\"Ci ho guardato dentro. Una volta. Mi ha dato gli incubi.\"")
    _tc(tr,F,"choice_notebook", en_choices=["Get the notebook and read it","Better not. Tomorrow is another day."], fr_choices=["Prendre le carnet et le lire","Mieux vaut pas. Demain est un autre jour."], es_choices=["Coger el cuaderno y leerlo","Mejor no. Mañana será otro día."], it_choices=["Prendere il quaderno e leggerlo","Meglio di no. Domani è un altro giorno."])
    _t(tr,F,"read_notebook", en="I go back to the bedroom. The candle flickers as I approach. Grandmother's face is almost alive in the dancing light.", fr="Je retourne dans là chambre. Là bougie vacille à mon approche. Le visage de grand-mère semble presque vivant dans là lumière dansante.", es="Vuelvo al dormitorio. La vela parpadea cuando me acerco. El rostro de la abuela parece casi vivo a la luz danzante.", it="Torno in camera da letto. La candela tremola al mio avvicinarmi. Il viso della nonna sembra quasi vivo nella luce danzante.")
    _t(tr,F,"read_notebook_2", en="The notebook is thin but crammed full. The handwriting grows hastier, more frantic from page to page. Some entries are in a language I don't recognize.", fr="Le carnet est mince mais rempli. L'écriture devient plus hâtive, plus frénétique de page en page. Certaines entrées sont dans une langue que je ne connais pas.", es="El cuaderno es delgado pero está repleto. La letra se vuelve más apresurada, más frenética de página en página. Algunas entradas están en un idioma que no reconozco.", it="Il quaderno è sottile ma zeppo. La grafia diventa più frettolosa, più frenetica di pagina in pagina. Alcune voci sono in una lingua che non riconosco.")
    _t(tr,F,"read_notebook_3", en="On the first page, neat and clear: \"For Elise. When I'm no longer here.\"", fr="Sur là première page, proprement et clairement : \"Pour Elise. Quand je ne serai plus là.\"", es="En la primera página, limpio y claro: \"Para Elise. Cuando yo ya no esté.\"", it="Sulla prima pagina, ordinato è chiaro: \"Per Elise. Quando non ci sarò più.\"")
    _t(tr,F,"read_notebook_4", en="\"There is something beneath the church. Something old. Older than the village, older than the trees, older than the mountains. We call it the Sleeper. My grandmother called it the Breath of the Earth.\"", fr="\"Il y a quelque chose sous l'église. Quelque chose d'ancien. Plus ancien que le village, plus ancien que les arbres, plus ancien que les montagnes. Nous l'appelons le Dormeur. Ma grand-mère l'appelait le Souffle de la Terre.\"", es="\"Hay algo bajo la iglesia. Algo viejo. Más viejo que el pueblo, más viejo que los árboles, más viejo que las montañas. Lo llamamos el Durmiente. Mi abuela lo llamaba el Aliento de la Tierra.\"", it="\"C'è qualcosa sotto la chiesa. Qualcosa di antico. Più antico del villaggio, più antico degli alberi, più antico delle montagne. Lo chiamiamo il Dormiente. Mia nonna lo chiamava il Respiro della Terra.\"")
    _t(tr,F,"read_notebook_5", en="\"Every thirty years it needs... nourishment. The last time was 1893. The next time is now. November 1923.\"", fr="\"Tous les trente ans, il a besoin de... nourriture. La dernière fois, c'était en 1893. La prochaine fois, c'est maintenant. Novembre 1923.\"", es="\"Cada treinta años necesita... alimento. La última vez fue en 1893. La próxima vez es ahora. Noviembre de 1923.\"", it="\"Ogni trent'anni ha bisogno di... nutrimento. L'ultima volta è stato nel 1893. La prossima volta è adesso. Novembre 1923.\"")
    _t(tr,F,"read_notebook_6", en="My hands tremble. I turn the page. The handwriting grows more chaotic.", fr="Mes mains tremblent. Je tourne là page. L'écriture devient plus chaotique.", es="Mis manos tiemblan. Paso la página. La letra se vuelve más caótica.", it="Le mie mani tremano. Giro pagina. La grafia diventa più caotica.")
    _t(tr,F,"read_notebook_7", en="\"Konrad is not Konrad. Not anymore. Since spring I see it in his eyes. He smiles differently. He moves differently. Something wears him like a coat.\"", fr="\"Konrad n'est plus Konrad. Plus maintenant. Depuis le printemps, je le vois dans ses yeux. Il sourit différemment. Il bouge différemment. Quelque chose le porte comme un manteau.\"", es="\"Konrad ya no es Konrad. Ya no. Desde primavera lo veo en sus ojos. Sonríe diferente. Se mueve diferente. Algo lo lleva puesto como un abrigo.\"", it="\"Konrad non è Konrad. Non più. Dalla primavera lo vedo nei suoi occhi. Sorride in modo diverso. Si muove in modo diverso. Qualcosa lo indossa come un cappotto.\"")
    _t(tr,F,"read_notebook_8", en="\"They want you, Elise. Your name is in the book beneath the church. I tried to cross it out, but the ink returns. Again and again.\"", fr="\"Ils te veulent, Elise. Ton nom est dans le livre sous l'église. J'ai essayé de le rayer, mais l'encre revient. Encore et encore.\"", es="\"Te quieren a ti, Elise. Tu nombre está en el libro bajo la iglesia. Intenté tacharlo, pero la tinta regresa. Una y otra vez.\"", it="\"Vogliono te, Elise. Il tuo nome è nel libro sotto la chiesa. Ho provato a cancellarlo, ma l'inchiostro ritorna. Sempre.\"")
    _t(tr,F,"journal_notebook", en="Grandmother's Notebook", fr="Le Carnet de Grand-mère", es="El cuaderno de la abuela", it="Il quaderno della nonna", field="title")
    _t(tr,F,"journal_notebook", en="Grandmother writes of something beneath the church — the 'Sleeper'. Every 30 years it needs 'nourishment'. The village teacher Konrad is 'no longer Konrad'. And my name is in a book beneath the church. What does it all mean?", fr="Grand-mère écrit sur quelque chose sous l'église — le 'Dormeur'. Tous les 30 ans, il à besoin de 'nourriture'. L'instituteur Konrad 'n'est plus Konrad'. Et mon nom est dans un livre sous l'église. Que signifie tout celà ?", es="La abuela escribe sobre algo bajo la iglesia — el 'Durmiente'. Cada 30 años necesita 'alimento'. El maestro Konrad 'ya no es Konrad'. Y mi nombre está en un libro bajo la iglesia. ¿Qué significa todo esto?", it="La nonna scrive di qualcosa sotto la chiesa — il 'Dormiente'. Ogni 30 anni ha bisogno di 'nutrimento'. Il maestro Konrad 'non è più Konrad'. È il mio nome è in un libro sotto la chiesa. Cosa significa tutto questo?", field="content")
    _t(tr,F,"skip_notebook", en="No. Not tonight. Not alone with a corpse and a candle that won't go out.", fr="Non. Pas ce soir. Pas seule avec un cadavre et une bougie qui refuse de s'éteindre.", es="No. No esta noche. No a solas con un cadáver y una vela que no quiere apagarse.", it="No. Non stanotte. Non da sola con un cadavere è una candela che non vuole spegnersi.")
    _t(tr,F,"skip_notebook_2", en="Tomorrow. In daylight. When the world makes sense again.", fr="Demain. À là lumière du jour. Quand le monde retrouverà son sens.", es="Mañana. A la luz del día. Cuando el mundo vuelva a tener sentido.", it="Domani. Alla luce del giorno. Quando il mondo tornerà ad avere senso.")
    _t(tr,F,"notebook_converge", en="At some point I must have fallen asleep. At the kitchen table, my head on my folded arms.", fr="À un moment, j'ai dû m'endormir. À là table de là cuisine, là tête sur mes bras croisés.", es="En algún momento debí quedarme dormida. En la mesa de la cocina, con la cabeza sobre los brazos cruzados.", it="A un certo punto devo essermi addormentata. Al tavolo della cucina, con la testa sulle braccia incrociate.")
    _t(tr,F,"narration_dream_1", en="In the dream I stand on the village square. It's night, but the village is brightly lit — by torches arranged in a spiral.", fr="Dans le rêve, je suis debout sur là place du village. C'est là nuit, mais le village est brillamment éclairé — par des torches disposées en spirale.", es="En el sueño estoy de pie en la plaza del pueblo. Es de noche, pero el pueblo está iluminado — por antorchas dispuestas en espiral.", it="Nel sogno sono in piedi sulla piazza del villaggio. È notte, ma il villaggio è illuminato — da torce disposte a spirale.")
    _t(tr,F,"narration_dream_2", en="People stand in a circle. All the villagers. They sing — the same melody I heard on the train. Deep and resonant, as if the sound comes from the earth itself.", fr="Des gens se tiennent en cercle. Tous les villageois. Ils chantent — là même mélodie que j'ai entendue dans le train. Profonde et résonante, comme si le son émanait de là terre elle-même.", es="La gente está en círculo. Todos los aldeanos. Cantan — la misma melodía que oí en el tren. Profunda y resonante, como si el sonido viniera de la tierra misma.", it="La gente sta in cerchio. Tutti i paesani. Cantano — la stessa melodia che ho sentito sul treno. Profonda è risonante, come se il suono provenisse dalla terrà stessa.")
    _t(tr,F,"narration_dream_3", en="In the center of the circle stands a man. Young, with dark hair and a smile that doesn't match his eyes. He reaches out his hand to me.", fr="Au centre du cercle se tient un homme. Jeune, aux cheveux sombres et un sourire qui ne correspond pas à ses yeux. Il me tend là main.", es="En el centro del círculo está un hombre. Joven, con cabello oscuro y una sonrisa que no concuerda con sus ojos. Me tiende la mano.", it="Al centro del cerchio c'è un uomo. Giovane, con capelli scuri è un sorriso che non corrisponde ai suoi occhi. Mi tende la mano.")
    _t(tr,F,"narration_dream_4", en="\"Welcome back, Elise,\" he says. \"We've been waiting for you.\"", fr="\"Bienvenue, Elise\", dit-il. \"Nous t'attendions.\"", es="\"Bienvenida, Elise\", dice. \"Te estábamos esperando.\"", it="\"Bentornata, Elise\", dice. \"Ti stavamo aspettando.\"")
    _t(tr,F,"narration_dream_5", en="Then I hear it. Not the singing, but something beneath it. A deep, rhythmic pounding. Like a heartbeat. But far too large for a human heart.", fr="Alors je l'entends. Pas le chant, mais quelque chose en dessous. Un battement profond et rythmique. Comme un cœur qui bat. Mais bien trop gros pour un cœur humain.", es="Entonces lo oigo. No el canto, sino algo debajo. Un latido profundo y rítmico. Como un corazón. Pero demasiado grande para un corazón humano.", it="Poi lo sento. Non il canto, ma qualcosa sotto di esso. Un battito profondo è ritmico. Come un cuore. Ma troppo grande per un cuore umano.")
    _t(tr,F,"narration_dream_6", en="The ground beneath my feet begins to vibrate. Cracks run through the cobblestones. Through the cracks comes light — not warm light. Something cold, bluish, moving like something alive.", fr="Le sol sous mes pieds se met à vibrer. Des fissures parcourent les pavés. Par les fissures filtre de là lumière — pas une lumière chaude. Quelque chose de froid, de bleuâtre, qui bouge comme un être vivant.", es="El suelo bajo mis pies empieza a vibrar. Grietas recorren los adoquines. Por las grietas sale luz — no una luz cálida. Algo frío, azulado, que se mueve como algo vivo.", it="Il suolo sotto i miei piedi comincia a vibrare. Crepe percorrono il selciato. Dalle crepe filtra luce — non una luce calda. Qualcosa di freddo, bluastro, che si muove come qualcosa di vivo.")
    _t(tr,F,"narration_dream_7", en="And then I open my eyes.", fr="Et puis j'ouvre les yeux.", es="Y entonces abro los ojos.", it="E poi apro gli occhi.")
    _t(tr,F,"narration_wake_1", en="I jolt awake. It's still dark. My heart hammers.", fr="Je sursaute. Il fait encore nuit. Mon cœur bat là chamade.", es="Me despierto sobresaltada. Todavía está oscuro. Mi corazón martillea.", it="Mi sveglio di soprassalto. È ancora buio. Il mio cuore martella.")
    _t(tr,F,"narration_wake_2", en="And then I hear it. Not in the dream. While awake.", fr="Et alors je l'entends. Pas dans le rêve. Éveillée.", es="Y entonces lo oigo. No en el sueño. Despierta.", it="E poi lo sento. Non nel sogno. Da sveglia.")
    _t(tr,F,"narration_wake_3", en="Singing. Faint, muffled, as if coming from far beneath the house. Many voices, woven into something that isn't quite music and isn't quite language.", fr="Un chant. Faible, étouffé, comme venant de loin sous là maison. De nombreuses voix, tissées en quelque chose qui n'est pas tout à fait de là musique et pas tout à fait un langage.", es="Cantos. Tenues, amortiguados, como si vinieran de muy debajo de la casa. Muchas voces, entrelazadas en algo que no es del todo música ni del todo lenguaje.", it="Un canto. Debole, soffocato, come se provenisse da sotto la casa. Molte voci, intrecciate in qualcosa che non è del tutto musica è non è del tutto linguaggio.")
    _t(tr,F,"narration_singing_2", en="The floorboards vibrate faintly under my bare feet. The glass on the table clinks softly. The candle in the bedroom — I can see it from here — burns higher, brighter.", fr="Les lattes vibrent légèrement sous mes pieds nus. Le verre sur là table tinte doucement. Là bougie dans là chambre — je là vois d'ici — brûle plus haut, plus fort.", es="Las tablas vibran ligeramente bajo mis pies descalzos. El vaso en la mesa tintinea suavemente. La vela en el dormitorio — la veo desde aquí — arde más alta, más brillante.", it="Le assi vibrano lievemente sotto i miei piedi nudi. Il bicchiere sul tavolo tintinna piano. La candela in camera — la vedo da qui — brucia più alta, più luminosa.")
    _t(tr,F,"narration_singing_3", en="Then — a knock at the door.", fr="Alors — on frappe à là porte.", es="Entonces — alguien llama a la puerta.", it="Poi — qualcuno bussa alla porta.")
    _t(tr,F,"narration_knock_1", en="Three blows. Slow. Deliberate. Like someone who knows they'll be let in.", fr="Trois coups. Lents. Délibérés. Comme quelqu'un qui sait qu'on và lui ouvrir.", es="Tres golpes. Lentos. Deliberados. Como alguien que sabe que le abrirán.", it="Tre colpi. Lenti. Deliberati. Come qualcuno che sa che gli apriranno.")
    _t(tr,F,"narration_knock_2", en="\"If someone knocks, don't open.\"", fr="\"Si on frappe, n'ouvre pas.\"", es="\"Si alguien llama, no abras.\"", it="\"Se qualcuno bussa, non aprire.\"")
    _t(tr,F,"narration_knock_3", en="Silence. Then, softly, a voice. Warm, friendly, concerned:", fr="Silence. Puis, doucement, une voix. Chaude, amicale, inquiète :", es="Silencio. Luego, suavemente, una voz. Cálida, amigable, preocupada:", it="Silenzio. Poi, piano, una voce. Calda, amichevole, preoccupata:")
    _t(tr,F,"narration_knock_4", en="\"Hello? Is anyone there? I saw a light. Do you need help?\"", fr="\"Bonjour ? Il y a quelqu'un ? J'ai vu de la lumière. Avez-vous besoin d'aide ?\"", es="\"¿Hola? ¿Hay alguien ahí? Vi una luz. ¿Necesita ayuda?\"", it="\"Salve? C'è qualcuno? Ho visto una luce. Ha bisogno di aiuto?\"")
    _t(tr,F,"narration_knock_5", en="A man's voice. Young, friendly. Not threatening. But Georg said...", fr="Une voix d'homme. Jeune, amicale. Pas menaçante. Mais Georg à dit...", es="Una voz de hombre. Joven, amigable. No amenazante. Pero Georg dijo...", it="Una voce maschile. Giovane, amichevole. Non minacciosa. Ma Georg ha detto...")
    _tc(tr,F,"choice_door", en_choices=["Open the door","Don't open. Georg said so."], fr_choices=["Ouvrir la porte","Ne pas ouvrir. Georg l'a dit."], es_choices=["Abrir la puerta","No abrir. Georg lo dijo."], it_choices=["Aprire la porta","Non aprire. Georg l'ha detto."])
    _t(tr,F,"open_door", en="My hand is on the bolt. I hesitate. Then I slide it back.", fr="Mà main est sur le verrou. J'hésite. Puis je le tire.", es="Mi mano está en el cerrojo. Dudo. Luego lo corro.", it="La mia mano è sul catenaccio. Esito. Poi lo tiro indietro.")
    _t(tr,F,"open_door_2", en="A man stands at the door. About thirty, with wavy dark hair and brown eyes that shimmer warmly in the moonlight. He wears a coat over a sweater and smiles with concern.", fr="Un homme se tient devant là porte. Là trentaine, cheveux bruns ondulés et yeux marron qui brillent chaleureusement au clair de lune. Il porte un manteau par-dessus un pull et sourit avec inquiétude.", es="Un hombre está ante la puerta. De unos treinta años, con cabello oscuro ondulado y ojos marrones que brillan cálidamente a la luz de la luna. Lleva un abrigo sobre un jersey y sonríe con preocupación.", it="Un uomo sta sulla soglia. Sulla trentina, con capelli scuri ondulati è occhi marroni che luccicano caldi al chiaro di luna. Indossa un cappotto sopra un maglione è sorride con preoccupazione.")
    _t(tr,F,"konrad_1", en="Oh — you must be Elise. Margarethe's granddaughter, right? I'm Konrad. Konrad Müller, the village teacher.", fr="Oh — vous devez être Elise. Là petite-fille de Margarethe, n'est-ce pas ? Je suis Konrad. Konrad Müller, l'instituteur du village.", es="Oh, usted debe ser Elise. La nieta de Margarethe, ¿verdad? Soy Konrad. Konrad Müller, el maestro del pueblo.", it="Oh — lei deve essere Elise. La nipote di Margarethe, vero? Sono Konrad. Konrad Müller, il maestro del villaggio.")
    _t(tr,F,"konrad_2", en="I'm terribly sorry about your grandmother. She was... a remarkable woman. She often helped me with teaching.", fr="Je suis terriblement désolé pour votre grand-mère. C'était... une femme remarquable. Elle m'aidait souvent pour l'enseignement.", es="Lamento mucho lo de su abuela. Era... una mujer notable. A menudo me ayudaba con las clases.", it="Mi dispiace terribilmente per sua nonna. Era... una donna straordinaria. Mi aiutava spesso con l'insegnamento.")
    _t(tr,F,"konrad_3", en="He sounds sincere. His smile is warm, his eyes friendly. And yet — if I look closely, there's something in his gaze. Something that doesn't quite...", fr="Il semble sincère. Son sourire est chaleureux, ses yeux amicaux. Et pourtant — si je regarde bien, il y à quelque chose dans son regard. Quelque chose qui n'est pas tout à fait...", es="Suena sincero. Su sonrisa es cálida, sus ojos amigables. Y sin embargo, si miro de cerca, hay algo en su mirada. Algo que no es del todo...", it="Sembra sincero. Il suo sorriso è caldo, i suoi occhi amichevoli. Eppure — se guardo bene, c'è qualcosa nel suo sguardo. Qualcosa che non è del tutto...")
    _t(tr,F,"konrad_4", en="No. I'm tired and frightened. I'm seeing ghosts.", fr="Non. Je suis fatiguée et effrayée. Je vois des fantômes.", es="No. Estoy cansada y asustada. Estoy viendo fantasmas.", it="No. Sono stanca è spaventata. Vedo fantasmi.")
    _t(tr,F,"konrad_notebook_reaction", en="\"Konrad is not Konrad. Not anymore.\" Grandmother's words strike me like lightning. This man — this friendly, smiling man — is supposed to be a vessel?", fr="\"Konrad n'est plus Konrad. Plus maintenant.\" Les mots de grand-mère me frappent comme la foudre. Cet homme — cet homme aimable et souriant — serait un réceptacle ?", es="\"Konrad ya no es Konrad. Ya no.\" Las palabras de la abuela me golpean como un rayo. Este hombre — este hombre amable y sonriente — ¿se supone que es un recipiente?", it="\"Konrad non è Konrad. Non più.\" Le parole della nonna mi colpiscono come un fulmine. Quest'uomo — quest'uomo gentile e sorridente — dovrebbe essere un ricettacolo?")
    _t(tr,F,"konrad_continue", en="I just wanted to make sure everything's alright. It's late, and this house... well, it's been empty for days. If you need anything — I live at the schoolhouse, right next to the church.", fr="Je voulais juste m'assurer que tout và bien. Il est tard, et cette maison... enfin, elle est vide depuis des jours. Si vous avez besoin de quoi que ce soit — j'habite à l'école, juste à côté de l'église.", es="Solo quería asegurarme de que todo está bien. Es tarde, y esta casa... bueno, lleva días vacía. Si necesita algo, vivo en la escuela, justo al lado de la iglesia.", it="Volevo solo assicurarmi che tutto fosse a posto. È tardi, è questa casa... beh, è vuota da giorni. Se ha bisogno di qualcosa — abito nella scuola, proprio accanto alla chiesa.")
    _t(tr,F,"konrad_6", en="Sleep well, Elise. And don't worry. Graubach is a quiet village. Nothing ever happens here.", fr="Dormez bien, Elise. Et ne vous inquiétez pas. Graubach est un village tranquille. Il ne s'y passe jamais rien.", es="Duerma bien, Elise. Y no se preocupe. Graubach es un pueblo tranquilo. Aquí nunca pasa nada.", it="Dorma bene, Elise. È non si preoccupi. Graubach è un villaggio tranquillo. Qui non succede mai niente.")
    _t(tr,F,"konrad_leave", en="He smiles once more, turns, and disappears into the fog. His footsteps make no sound on the cobblestones.", fr="Il sourit une dernière fois, se retourne et disparaît dans le brouillard. Ses pas ne font aucun bruit sur les pavés.", es="Sonríe una vez más, se da la vuelta y desaparece en la niebla. Sus pasos no hacen ruido sobre los adoquines.", it="Sorride ancora, si gira è scompare nella nebbia. I suoi passi non fanno rumore sul selciato.")
    _t(tr,F,"narration_after_door", en="I close the door. My heart pounds. I don't know if from relief or something else.", fr="Je ferme là porte. Mon cœur bat fort. Je ne sais pas si c'est de soulagement où d'autre chose.", es="Cierro la puerta. Mi corazón late con fuerza. No sé si de alivio o de otra cosa.", it="Chiudo la porta. Il mio cuore batte forte. Non so se per sollievo o per qualcos'altro.")
    _t(tr,F,"narration_after_door_2", en="The singing has stopped. When exactly, I don't know. But now it's silent.", fr="Le chant s'est arrêté. Quand exactement, je ne sais pas. Mais maintenant c'est le silence.", es="El canto ha cesado. Cuándo exactamente, no lo sé. Pero ahora hay silencio.", it="Il canto è cessato. Quando esattamente, non lo so. Ma ora c'è silenzio.")
    _t(tr,F,"narration_after_door_3", en="Too silent.", fr="Trop de silence.", es="Demasiado silencio.", it="Troppo silenzio.")
    _t(tr,F,"dont_open", en="No. Georg said so. I press my hand over my mouth to make no sound.", fr="Non. Georg l'à dit. Je plaque mà main sur mà bouche pour ne faire aucun bruit.", es="No. Georg lo dijo. Me tapo la boca con la mano para no hacer ruido.", it="No. Georg l'ha detto. Mi premo la mano sulla bocca per non fare rumore.")
    _t(tr,F,"dont_open_2", en="Silence. Then, three more blows. Slower this time. More patient.", fr="Silence. Puis, trois coups de plus. Plus lents cette fois. Plus patients.", es="Silencio. Luego, tres golpes más. Más lentos esta vez. Más pacientes.", it="Silenzio. Poi, altri tre colpi. Più lenti questa volta. Più pazienti.")
    _t(tr,F,"dont_open_3", en="\"I know you're in there, Elise.\"", fr="\"Je sais que vous êtes là, Elise.\"", es="\"Sé que estás ahí, Elise.\"", it="\"So che sei lì dentro, Elise.\"")
    _t(tr,F,"dont_open_4", en="My name. He knows my name.", fr="Mon nom. Il connaît mon nom.", es="Mi nombre. Sabe mi nombre.", it="Il mio nome. Conosce il mio nome.")
    _t(tr,F,"dont_open_5", en="Through the gap under the door I see a shadow. He stands there, patient, waiting. Minutes pass. Or hours.", fr="Par l'interstice sous là porte, je vois une ombre. Il reste là, patient, attendant. Des minutes passent. Ou des heures.", es="Por la rendija bajo la puerta veo una sombra. Está ahí, paciente, esperando. Pasan minutos. O horas.", it="Attraverso la fessura sotto la porta vedo un'ombra. Sta lì, paziente, in attesa. Passano minuti. O ore.")
    _t(tr,F,"dont_open_6", en="Then I hear footsteps retreating. And softly, barely audible, a humming. The same melody.", fr="Puis j'entends des pas qui s'éloignent. Et doucement, à peine audible, un fredonnement. Là même mélodie.", es="Luego oigo pasos alejándose. Y suavemente, apenas audible, un tarareo. La misma melodía.", it="Poi sento passi che si allontanano. È piano, appena udibile, un canticchiare. La stessa melodia.")
    _t(tr,F,"dont_open_7", en="As the footsteps fade, I notice that the singing beneath the floor has also fallen silent.", fr="Quand les pas s'estompent, je remarque que le chant sous le plancher s'est tu lui aussi.", es="Cuando los pasos se desvanecen, noto que el canto bajo el suelo también ha callado.", it="Quando i passi svaniscono, noto che anche il canto sotto il pavimento è cessato.")
    _t(tr,F,"converge_night", en="The rest of the night passes in forced wakefulness. I sit with my back to the wall, staring at the door.", fr="Le reste de là nuit passe dans une veille forcée. Je suis assise dos au mur, fixant là porte.", es="El resto de la noche pasa en vigilia forzada. Me siento con la espalda contra la pared, mirando fijamente la puerta.", it="Il resto della notte passa in una veglia forzata. Siedo con la schiena al muro, fissando la porta.")
    _t(tr,F,"converge_night_2", en="At some point the sky outside turns grey. Pale November light seeps through the cracks in the shutters. The night is over.", fr="À un moment, le ciel dehors vire au gris. Une pâle lumière de novembre s'infiltre par les fentes des volets. Là nuit est finie.", es="En algún momento el cielo afuera se vuelve gris. La pálida luz de noviembre se filtra por las rendijas de las contraventanas. La noche ha terminado.", it="A un certo punto il cielo fuori diventa grigio. La pallida luce di novembre filtra dalle fessure delle imposte. La notte è finita.")
    _t(tr,F,"converge_night_3", en="I'm alive. Everything else can wait until the coffee is brewing.", fr="Je suis vivante. Tout le reste peut attendre que le café soit prêt.", es="Estoy viva. Todo lo demás puede esperar hasta que hierva el café.", it="Sono viva. Tutto il resto può aspettare finché non si fa il caffè.")
    _t(tr,F,"journal_night", en="The First Night", fr="Là Première Nuit", es="La primera noche", it="La prima notte", field="title")
    _t(tr,F,"journal_night", en="Singing from underground. Knocking at the door. The village has a secret. Grandmother knew it. Georg knows it. And whoever stood at my door — he knew my name.", fr="Un chant souterrain. Des coups à là porte. Le village à un secret. Grand-mère le savait. Georg le sait. Et quiconque se tenait devant mà porte — il connaissait mon nom.", es="Cantos subterráneos. Golpes en la puerta. El pueblo tiene un secreto. La abuela lo sabía. Georg lo sabe. Y quienquiera que estuviera ante mi puerta — sabía mi nombre.", it="Canti dal sottosuolo. Bussare alla porta. Il villaggio ha un segreto. La nonna lo sapeva. Georg lo sa. È chiunque fosse alla mia porta — conosceva il mio nome.", field="content")

    # --- Additional translations (auto-generated) ---

    _t(tr, F, "elise_nb_react_1",
       en="Something under the church...? Grandmother, what did you never tell me?",
       fr="Quelque chose sous l'église...? Grand-mère, que ne m'as-tu jamais dit?",
       es="Algo bajo la iglesia...? Abuela, que nunca me contaste?",
       it="Qualcosa sotto la chiesa...? Nonna, cosa non mi hai mai detto?")

    _t(tr, F, "elise_nb_react_2",
       en="I set the book down. My hands are trembling too much. Thirty years. Nourishment. What kind of nourishment? I don't want to read on. But I must.",
       fr="Je pose le livre. Mes mains tremblent trop. Trente ans. De la nourriture. Quelle sorte de nourriture? Je ne veux pas continuer a lire. Mais je le dois.",
       es="Dejo el libro. Mis manos tiemblan demasiado. Treinta años. Alimento. Que clase de alimento? No quiero seguir leyendo. Pero debo hacerlo.",
       it="Poso il libro. Le mie mani tremano troppo. Trent'anni. Nutrimento. Che tipo di nutrimento? Non voglio continuare a leggere. Ma devo.")

    _t(tr, F, "elise_nb_react_3",
       en="Konrad. The village teacher. I don't know the man - but Grandmother writes about him as if he were a threat. What lives INSIDE a person? What wears someone like a coat?",
       fr="Konrad. L'instituteur du village. Je ne connais pas cet homme - mais Grand-mère écrit sur lui comme s'il était une menace. Qu'est-ce qui vit A L'INTERIEUR d'une personne? Qu'est-ce qui porte quelqu'un comme un manteau?",
       es="Konrad. El maestro del pueblo. No conozco al hombre, pero la abuela escribe sobre el como si fuera una amenaza. Que vive DENTRO de una persona? Que lleva a alguien puesto como un abrigo?",
       it="Konrad. Il maestro del villaggio. Non conosco quest'uomo, ma la nonna scrive di lui come di una minaccia. Cosa vive DENTRO una persona? Cosa indossa qualcuno come un cappotto?")

    _t(tr, F, "elise_nb_react_4",
       en="My name...? MY name is in a book beneath the church? What does that mean? What does this THING want from me?",
       fr="Mon nom...? MON nom se trouve dans un livre sous l'église? Qu'est-ce que cela signifie? Que VEUT cette chose de moi?",
       es="Mi nombre...? MI nombre esta en un libro bajo la iglesia? Que significa eso? Que QUIERE esa cosa de mi?",
       it="Il mio nome...? Il MIO nome e in un libro sotto la chiesa? Cosa significa? Cosa VUOLE questa cosa da me?")

    _t(tr, F, "skip_restless_1",
       en="But I can't sit still. The silence presses down. I stand up and walk through the dark house, my fingers trailing along the wall.",
       fr="Mais je ne peux pas rester assise. Le silence pese. Je me leve et traverse la maison sombre, les doigts le long du mur.",
       es="Pero no puedo quedarme quieta. El silencio oprime. Me levanto y camino por la casa oscura, con los dedos rozando la pared.",
       it="Ma non riesco a stare ferma. Il silenzio preme. Mi alzo e cammino per la casa buia, le dita lungo il muro.")

    _t(tr, F, "skip_restless_2",
       en="In the hallway I stop. Above the doorframe, symbols are carved into the wood - spirals, intertwined and deep. The same as on the letter. I trace them with my fingers. The wood is smooth, as if Grandmother had retraced them regularly.",
       fr="Dans le couloir, je m'arrête. Au-dessus du chambranle, des symboles sont graves dans le bois - des spirales, entrelacées et profondes. Les memes que sur la lettre. Je les parcours du bout des doigts. Le bois est lisse, comme si Grand-mère les avait régulièrement retracees.",
       es="En el pasillo me detengo. Sobre el marco de la puerta hay simbolos tallados en la madera: espirales, entrelazadas y profundas. Las mismas que en la carta. Las recorro con los dedos. La madera esta lisa, como si la abuela las hubiera repasado regularmente.",
       it="Nel corridoio mi fermo. Sopra lo stipite della porta, dei simboli sono intagliati nel legno - spirali, intrecciate e profonde. Le stesse della lettera. Le percorro con le dita. Il legno e liscio, come se la nonna le avesse ripassate regolarmente.")

    _t(tr, F, "skip_restless_3",
       en="The same at every window. Spirals above the frame, dried bundles of herbs in the cracks. Every opening in the house is protected. Sealed.",
       fr="La même chose a chaque fenêtre. Des spirales au-dessus du cadre, des bouquets d'herbes séchées dans les fissures. Chaque ouverture de la maison est protégée. Scellee.",
       es="Lo mismo en cada ventana. Espirales sobre el marco, manojos de hierbas secas en las grietas. Cada abertura de la casa esta protegida. Sellada.",
       it="Lo stesso a ogni finestra. Spirali sopra il telaio, mazzetti di erbe essiccate nelle fessure. Ogni apertura della casa e protetta. Sigillata.")

    _t(tr, F, "skip_restless_4",
       en="Grandmother... how long have you been doing this? What have you been keeping out?",
       fr="Grand-mère... depuis combien de temps fais-tu cela? Qu'est-ce que tu tenais a distance?",
       es="Abuela... cuanto tiempo llevas haciendo esto? Que has estado manteniendo afuera?",
       it="Nonna... da quanto tempo lo fai? Cosa hai tenuto lontano?")

    _t(tr, F, "skip_restless_5",
       en="At the kitchen window I press my forehead against the cold glass. Outside: darkness. But somewhere in that darkness I feel something. Not see, not hear - feel. As if someone is watching me.",
       fr="A la fenêtre de la cuisine, j'appuie mon front contre la vitre froide. Dehors: l'obscurite. Mais quelque part dans cette obscurite, je sens quelque chose. Pas voir, pas entendre - sentir. Comme si quelqu'un m'observait.",
       es="En la ventana de la cocina presiono la frente contra el cristal frio. Afuera: oscuridad. Pero en alguna parte de esa oscuridad siento algo. No ver, no oir - sentir. Como si alguien me estuviera observando.",
       it="Alla finestra della cucina premo la fronte contro il vetro freddo. Fuori: oscurità. Ma da qualche parte in quell'oscurità sento qualcosa. Non vedere, non sentire - percepire. Come se qualcuno mi stesse osservando.")

    _t(tr, F, "skip_restless_6",
       en="I return to the table and wrap myself in Grandmother's shawl. The scent of lavender and chamomile envelops me. Almost comforting. Almost.",
       fr="Je retourne a la table et m'enveloppe dans le chale de Grand-mère. Le parfum de lavande et de camomille m'enveloppe. Presque réconfortant. Presque.",
       es="Vuelvo a la mesa y me envuelvo en el chal de la abuela. El aroma de lavanda y manzanilla me envuelve. Casi reconfortante. Casi.",
       it="Torno al tavolo e mi avvolgo nello scialle della nonna. Il profumo di lavanda e camomilla mi avvolge. Quasi confortante. Quasi.")

    _t(tr, F, "elise_through_door_1",
       en="Who are you? What do you want in the middle of the night?",
       fr="Qui êtes-vous? Que voulez-vous au milieu de la nuit?",
       es="Quien es usted? Que quiere a estas horas de la noche?",
       it="Chi siete? Cosa volete nel cuore della notte?")

    _t(tr, F, "voice_reply_1",
       en="\"Konrad Mueller, the village teacher. I saw the light and was worried. Margarethe was... a friend.\"",
       fr="\"Konrad Mueller, l'instituteur du village. J'ai vu la lumière et je me suis inquiété. Margarethe était... une amie.\"",
       es="\"Konrad Mueller, el maestro del pueblo. Vi la luz y me preocupé. Margarethe era... una amiga.\"",
       it="\"Konrad Mueller, il maestro del villaggio. Ho visto la luce e mi sono preoccupato. Margarethe era... un'amica.\"")

    _t(tr, F, "elise_through_door_2",
       en="My uncle said I shouldn't open the door. Not at night.",
       fr="Mon oncle m'a dit de ne pas ouvrir. Pas la nuit.",
       es="Mi tío me dijo que no abra. No de noche.",
       it="Mio zio mi ha detto di non aprire. Non di notte.")

    _t(tr, F, "voice_reply_2",
       en="A pause. Then, quieter: \"Georg is afraid. That's understandable, after what happened. But I'm just a teacher, Fraulein Brandt. Not a monster.\"",
       fr="Une pause. Puis, plus bas: \"Georg a peur. C'est compréhensible, après ce qui s'est passé. Mais je ne suis qu'un instituteur, Fräulein Brandt. Pas un monstre.\"",
       es="Una pausa. Luego, más bajo: \"Georg tiene miedo. Es comprensible, después de lo que pasó. Pero solo soy un maestro, Fräulein Brandt. No un monstruo.\"",
       it="Una pausa. Poi, più piano: \"Georg ha paura. È comprensibile, dopo quello che è successo. Ma sono solo un insegnante, Fräulein Brandt. Non un mostro.\"")

    _t(tr, F, "elise_through_door_3",
       en="How do you know my name? I haven't introduced myself.",
       fr="Comment connaissez-vous mon nom? Je ne me suis pas présentée.",
       es="¿Cómo sabe mi nombre? No me he presentado.",
       it="Come fate a sapere il mio nome? Non mi sono presentata.")

    _t(tr, F, "voice_reply_3",
       en="A soft laugh. Warm, but somehow too calm. \"Your grandmother talked a lot about you. She was very proud of you. The folklorist in Berlin.\"",
       fr="Un rire léger. Chaleureux, mais étrangement trop calme. \"Votre grand-mère parlait beaucoup de vous. Elle était très fière de vous. La folkloriste à Berlin.\"",
       es="Una risa suave. Cálida, pero de alguna manera demasiado tranquila. \"Su abuela hablaba mucho de usted. Estaba muy orgullosa de usted. La folklorista en Berlín.\"",
       it="Una risata sommessa. Calda, ma in qualche modo troppo tranquilla. \"Sua nonna parlava molto di lei. Era molto fiera di lei. La folklorista a Berlino.\"")

    _t(tr, F, "open_door_decide",
       en="Something in his voice calms me. Against my better judgment, I slide the bolt back and open the door.",
       fr="Quelque chose dans sa voix me rassure. Contre mon meilleur jugement, je tire le verrou et ouvre la porte.",
       es="Algo en su voz me tranquiliza. Contra mi buen juicio, descorro el cerrojo y abro la puerta.",
       it="Qualcosa nella sua voce mi rassicura. Contro il mio miglior giudizio, faccio scorrere il chiavistello e apro la porta.")

    _t(tr, F, "elise_responds_konrad",
       en="Thank you. Did you know her well?",
       fr="Merci. Vous la connaissiez bien?",
       es="Gracias. ¿La conocía bien?",
       it="Grazie. La conosceva bene?")

    _t(tr, F, "elise_responds_konrad_2",
       en="Why are you out in the middle of the night, Herr Mueller? Don't you ever sleep?",
       fr="Pourquoi êtes-vous dehors en pleine nuit, Herr Mueller? Vous ne dormez jamais?",
       es="¿Por qué anda por ahí en plena noche, Herr Mueller? ¿Nunca duerme?",
       it="Perché e in giro nel cuore della notte, Herr Mueller? Non dorme mai?")

    _t(tr, F, "elise_thinks_closed",
       en="Every muscle in me wants to open that door. The voice sounds friendly, concerned, normal. But Georg was terrified. Georg, who tames horses with his bare hands. I stay silent.",
       fr="Chaque muscle en moi veut ouvrir cette porte. La voix semble amicale, inquiete, normale. Mais Georg était terrifie. Georg, qui dompte les chevaux a mains nues. Je reste silencieuse.",
       es="Cada musculo en mi quiere abrir esa puerta. La voz suena amable, preocupada, normal. Pero Georg estaba aterrorizado. Georg, que doma caballos con las manos desnudas. Me quedo en silencio.",
       it="Ogni muscolo in me vuole aprire quella porta. La voce sembra amichevole, preoccupata, normale. Ma Georg era terrorizzato. Georg, che doma i cavalli a mani nude. Resto in silenzio.")

    _t(tr, F, "elise_thinks_name",
       en="How? I only arrived today. Nobody knows I'm here - nobody except Georg. Whoever is standing outside this door, he was expecting me.",
       fr="Comment? Je suis arrivee aujourd'hui seulement. Personne ne sait que je suis ici - personne sauf Georg. Qui que soit celui qui se tient devant cette porte, il m'attendait.",
       es="Como? Acabo de llegar hoy. Nadie sabe que estoy aqui, nadie excepto Georg. Quienquiera que este frente a esta puerta, me estaba esperando.",
       it="Come? Sono arrivata solo oggi. Nessuno sa che sono qui - nessuno tranne Georg. Chiunque sia davanti a questa porta, mi stava aspettando.")

    _t(tr, F, "narration_dawn_1",
       en="By the stove I find some coffee grounds. My hands tremble as I pour the water. Through the window I see the first faint shimmer above the firs. The village lies silent in the fog, as if nothing had happened.",
       fr="Pres du poele, je trouve encore du cafe moulu. Mes mains tremblent en versant l'eau. Par la fenêtre, j'apercois la première faible lueur au-dessus des sapins. Le village repose silencieux dans le brouillard, comme si rien ne s'était passe.",
       es="Junto a la estufa encuentro algo de cafe molido. Mis manos tiemblan al verter el agua. Por la ventana veo el primer debil resplandor sobre los abetos. El pueblo yace en silencio bajo la niebla, como si nada hubiera ocurrido.",
       it="Accanto alla stufa trovo ancora del caffe macinato. Le mie mani tremano mentre verso l'acqua. Dalla finestra vedo il primo debole bagliore sopra gli abeti. Il villaggio giace silenzioso nella nebbia, come se nulla fosse accaduto.")

    _t(tr, F, "elise_dawn_plan",
       en="Today I'll talk to the people here. The pastor, the mayor, anyone who can give me answers. Someone in this village knows what is going on.",
       fr="Aujourd'hui, je parlerai aux gens d'ici. Au pasteur, au maire, a quiconque peut me donner des réponses. Quelqu'un dans ce village sait ce qui se passe.",
       es="Hoy hablare con la gente de aqui. Con el pastor, con el alcalde, con cualquiera que pueda darme respuestas. Alguien en este pueblo sabe lo que esta pasando.",
       it="Oggi parlero con la gente di qui. Con il pastore, con il sindaco, con chiunque possa darmi delle risposte. Qualcuno in questo villaggio sa cosa sta succedendo.")

    _t(tr, F, "narration_dawn_melody",
       en="But even as I drink the coffee, I hum softly. Without meaning to. The same melody. It has burrowed into me like an earworm that refuses to fade.",
       fr="Mais tandis que je bois mon cafe, je fredonne doucement. Sans le vouloir. La même melodie. Elle s'est installee en moi comme un ver d'oreille qui refuse de disparaître.",
       es="Pero mientras bebo el cafe, tarareo en voz baja. Sin querer. La misma melodia. Se ha anidado en mi como un estribillo que no quiere desaparecer.",
       it="Ma mentre bevo il caffe, canticchio piano. Senza volerlo. La stessa melodia. Si e insediata in me come un motivetto che non vuole andarsene.")


def _add_act1_village_exploration(tr):
    F = "res://data/dialogue/act1/village_exploration.json"

    _t(tr, F, "narration_morning_1",
       en="The morning brings no relief. The fog has not lifted — it has only grown brighter, like a dirty sheet draped over the village.",
       fr="Le matin n'apporte aucun soulagement. Le brouillard ne s'est pas levé — il est seulement devenu plus clair, comme un drap sale étendu sur le village.",
       es="La mañana no trae alivio. La niebla no se ha levantado — solo se ha aclarado, como una sábana sucia tendida sobre el pueblo.",
       it="Il mattino non porta sollievo. La nebbia non si è sollevata — si è solo schiarita, come un lenzuolo sporco steso sul villaggio.")
    _t(tr, F, "narration_morning_2",
       en="At the village fountain I wash my face. The water is ice-cold. In the murky mirror of the surface I see my pale face. And for a moment — just a moment — I see a second face beside mine.",
       fr="Au puits du village, je me lave le visage. L'eau est glaciale. Dans le miroir trouble de là surface, je vois mon visage pâle. Et pendant un instant — un seul instant — je vois un deuxième visage à côté du mien.",
       es="En la fuente del pueblo me lavo la cara. El agua está helada. En el turbio espejo de la superficie veo mi rostro pálido. Y por un momento — solo un momento — veo un segundo rostro junto al mío.",
       it="Alla fontana del villaggio mi lavo il viso. L'acqua è gelida. Nello specchio torbido della superficie vedo il mio volto pallido. È per un istante — solo un istante — vedo un secondo volto accanto al mio.")
    _t(tr, F, "narration_morning_3",
       en="I flinch back. Nothing. Just my reflection.",
       fr="Je recule brusquement. Rien. Juste mon reflet.",
       es="Me echo atrás sobresaltada. Nada. Solo mi reflejo.",
       it="Mi ritraggo di scatto. Niente. Solo il mio riflesso.")
    _t(tr, F, "narration_morning_4",
       en="The people of Graubach show themselves by day. Women hang laundry. An old man chops wood. Children — few — walk to school with bowed heads.",
       fr="Les habitants de Graubach se montrent le jour. Des femmes étendent le linge. Un vieil homme coupe du bois. Des enfants — peu nombreux — se rendent à l'école là tête baissée.",
       es="La gente de Graubach se deja ver de día. Mujeres tienden la ropa. Un anciano corta leña. Niños — pocos — caminan hacia la escuela con la cabeza gacha.",
       it="La gente di Graubach si mostra di giorno. Donne stendono il bucato. Un vecchio spacca legna. Bambini — pochi — camminano verso la scuola a testa bassa.")
    _t(tr, F, "narration_morning_5",
       en="No one speaks. No one greets me. Some look at me — brief, furtive glances, immediately averted. As though the sight of me makes them uneasy.",
       fr="Personne ne parle. Personne ne me salue. Certains me regardent — des coups d'œil brefs et furtifs, immédiatement détournés. Comme si mà vue les mettait mal à l'aise.",
       es="Nadie habla. Nadie me saluda. Algunos me miran — miradas breves y furtivas, inmediatamente desviadas. Como si mi presencia les causara inquietud.",
       it="Nessuno parla. Nessuno mi saluta. Alcuni mi guardano — occhiate brevi è furtive, subito distolte. Come se la mia vista li mettesse a disagio.")
    _tc(tr, F, "choice_explore",
        en_choices=["Go to the church", "Visit the herbalist at the edge of the village", "Go to the schoolhouse — look for last night's visitor"],
        fr_choices=["Aller à l'église", "Rendre visite à l'herboriste en bordure du village", "Aller à l'école — chercher le visiteur de la nuit dernière"],
        es_choices=["Ir a la iglesia", "Visitar a la herbolaria en las afueras del pueblo", "Ir a la escuela — buscar al visitante nocturno"],
        it_choices=["Andare alla chiesa", "Visitare l'erborista ai margini del villaggio", "Andare alla scuola — cercare il visitatore notturno"])
    _t(tr, F, "church_1",
       en="The church of Graubach is old. Older than most of the houses in the village. The tower leans slightly to one side, as if something below were pulling at it.",
       fr="L'église de Graubach est vieille. Plus vieille que là plupart des maisons du village. Le clocher penche légèrement sur le côté, comme si quelque chose en dessous le tirait.",
       es="La iglesia de Graubach es vieja. Más vieja que la mayoría de las casas del pueblo. La torre se inclina ligeramente hacia un lado, como si algo tirara de ella desde abajo.",
       it="La chiesa di Graubach è vecchia. Più vecchia della maggior parte delle case del villaggio. Il campanile pende leggermente da un lato, come se qualcosa dal basso lo tirasse verso il basso.")
    _t(tr, F, "church_2",
       en="The graveyard beside the church is overgrown. Headstones stand crooked; some have toppled over. On several I make out the same symbol: a spiral.",
       fr="Le cimetière à côté de l'église est envahi par là végétation. Les pierres tombales sont de travers, certaines sont tombées. Sur plusieurs, je distingue le même symbole : une spirale.",
       es="El cementerio junto a la iglesia está cubierto de maleza. Las lápidas están torcidas; algunas se han caído. En varias distingo el mismo símbolo: una espiral.",
       it="Il cimitero accanto alla chiesa è invaso dalla vegetazione. Le lapidi sono storte; alcune sono cadute. Su diverse riconosco lo stesso simbolo: una spirale.")
    _t(tr, F, "church_3",
       en="The church door is locked. But through a window I see candlelight inside.",
       fr="Là porte de l'église est verrouillée. Mais à travers une fenêtre, je vois là lueur de bougies à l'intérieur.",
       es="La puerta de la iglesia está cerrada con llave. Pero a través de una ventana veo luz de velas en el interior.",
       it="La porta della chiesa è chiusa a chiave. Ma attraverso una finestra vedo la luce di candele all'interno.")
    _t(tr, F, "voss_1",
       en="The side door opens. A man steps out — thin as a line, with sunken cheeks and eyes that have seen too much.",
       fr="Là porte latérale s'ouvre. Un homme en sort — maigre comme un fil, les joues creusées et des yeux qui ont trop vu.",
       es="La puerta lateral se abre. Un hombre sale — delgado como un trazo, con las mejillas hundidas y ojos que han visto demasiado.",
       it="La porta laterale si apre. Un uomo esce — magro come un filo, con le guance incavate è occhi che hanno visto troppo.")
    _t(tr, F, "voss_2",
       en="You are not permitted to be here.",
       fr="Vous n'avez pas le droit d'être ici.",
       es="No tiene permitido estar aquí.",
       it="Non Le è permesso stare qui.")
    _t(tr, F, "voss_3",
       en="His voice is hoarse, as though he had been praying for hours. Or screaming.",
       fr="Sà voix est rauque, comme s'il avait prié pendant des heures. Ou crié.",
       es="Su voz es ronca, como si hubiera estado rezando durante horas. O gritando.",
       it="La sua voce è rauca, come se avesse pregato per ore. O urlato.")
    _t(tr, F, "voss_4",
       en="You are Margarethe's granddaughter, are you not? Elise Brandt. I am Pastor Voss.",
       fr="Vous êtes là petite-fille de Margarethe, n'est-ce pas ? Elise Brandt. Je suis le pasteur Voss.",
       es="Usted es la nieta de Margarethe, ¿no es así? Elise Brandt. Soy el pastor Voss.",
       it="Lei è la nipote di Margarethe, non è vero? Elise Brandt. Sono il pastore Voss.")
    _t(tr, F, "voss_6",
       en="Leave. Leave Graubach. Today. Take nothing with you, do not look back. Just go.",
       fr="Partez. Quittez Graubach. Aujourd'hui. N'emportez rien, ne vous retournez pas. Partez, c'est tout.",
       es="Váyase. Abandone Graubach. Hoy mismo. No se lleve nada, no mire atrás. Simplemente váyase.",
       it="Se ne vada. Lasci Graubach. Oggi stesso. Non porti nulla con sé, non si volti indietro. Se ne vada è basta.")
    _t(tr, F, "voss_7",
       en="He grabs my arm. His grip is surprisingly firm for such an emaciated man.",
       fr="Il me saisit le bras. Sà poigne est étonnamment ferme pour un homme si émacié.",
       es="Me agarra del brazo. Su agarre es sorprendentemente firme para un hombre tan demacrado.",
       it="Mi afferra il braccio. La sua presa è sorprendentemente salda per un uomo così emaciato.")
    _t(tr, F, "voss_8",
       en="Your grandmother tried to stop it. She failed. And now you are here, exactly as they wanted. Leave while you still can.",
       fr="Votre grand-mère à essayé de l'arrêter. Elle à échoué. Et maintenant vous êtes là, exactement comme ils le voulaient. Partez tant que vous le pouvez encore.",
       es="Su abuela intentó detenerlo. Fracasó. Y ahora usted está aquí, exactamente como ellos querían. Váyase mientras aún pueda.",
       it="Sua nonna ha cercato di fermarlo. Ha fallito. È ora Lei è qui, esattamente come loro volevano. Se ne vada finché può ancora farlo.")
    _tc(tr, F, "choice_voss",
        en_choices=["Who are 'they'? What do they want from me?", "I am not going anywhere until I know the truth."],
        fr_choices=["Qui sont « ils » ? Que me veulent-ils ?", "Je ne partirai pas tant que je ne connaîtrai pas la vérité."],
        es_choices=["¿Quiénes son 'ellos'? ¿Qué quieren de mí?", "No me iré a ninguna parte hasta que conozca la verdad."],
        it_choices=["Chi sono 'loro'? Cosa vogliono da me?", "Non andrò da nessuna parte finché non conoscerò la verità."])
    _t(tr, F, "voss_q1",
       en="The village. The elders. The mayor. And... the Other. That which has no voice, but speaks through others.",
       fr="Le village. Les anciens. Le maire. Et... l'Autre. Celui qui n'à pas de voix, mais qui parle à travers les autres.",
       es="El pueblo. Los ancianos. El alcalde. Y... el Otro. Aquello que no tiene voz, pero habla a través de otros.",
       it="Il villaggio. Gli anziani. Il sindaco. E... l'Altro. Quello che non ha voce, ma parla attraverso gli altri.")
    _t(tr, F, "voss_q2",
       en="I am a man of God, Fräulein Brandt. But what lies beneath this church... God has no words for that.",
       fr="Je suis un homme de Dieu, Fräulein Brandt. Mais ce qui repose sous cette église... Dieu n'à pas de mots pour cela.",
       es="Soy un hombre de Dios, Fräulein Brandt. Pero lo que yace bajo esta iglesia... Dios no tiene palabras para eso.",
       it="Sono un uomo di Dio, Fräulein Brandt. Ma ciò che giace sotto questa chiesa... Dio non ha parole per questo.")
    _t(tr, F, "voss_d1",
       en="Voss looks at me for a long time. Then he releases my arm. His shoulders slump.",
       fr="Voss me regarde longuement. Puis il lâche mon bras. Ses épaules s'affaissent.",
       es="Voss me mira durante largo rato. Luego me suelta el brazo. Sus hombros se hunden.",
       it="Voss mi guarda a lungo. Poi mi lascia il braccio. Le sue spalle si afflosciano.")
    _t(tr, F, "voss_d2",
       en="Just like Margarethe. The same eyes. The same stubbornness. She did not listen to me either.",
       fr="Exactement comme Margarethe. Les mêmes yeux. Là même obstination. Elle non plus ne m'à pas écouté.",
       es="Igual que Margarethe. Los mismos ojos. La misma terquedad. Ella tampoco me escuchó.",
       it="Proprio come Margarethe. Gli stessi occhi. La stessa testardaggine. Neanche lei mi ha ascoltato.")
    _t(tr, F, "voss_converge",
       en="Before I can ask more questions, a young girl appears in the side doorway. Blonde hair, pale skin, a gaze that looks right through me.",
       fr="Avant que je puisse poser d'autres questions, une jeune fille apparaît dans l'embrasure de là porte latérale. Des cheveux blonds, une peau pâle, un regard qui me traverse.",
       es="Antes de que pueda hacer más preguntas, una niña aparece en el umbral de la puerta lateral. Cabello rubio, piel pálida, una mirada que me atraviesa.",
       it="Prima che io possa fare altre domande, una ragazzina appare sulla soglia della porta laterale. Capelli biondi, pelle pallida, uno sguardo che mi attraversa.")
    _t(tr, F, "anna_1",
       en="Papa, who is...?",
       fr="Papa, qui est... ?",
       es="Papá, ¿quién es...?",
       it="Papà, chi è...?")
    _t(tr, F, "anna_2",
       en="She stops short. Her eyes widen. For a moment there is something in her gaze — clarity, horror, recognition.",
       fr="Elle s'arrête net. Ses yeux s'écarquillent. Pendant un instant, il y à quelque chose dans son regard — de là clarté, de l'horreur, de là reconnaissance.",
       es="Se detiene en seco. Sus ojos se abren de par en par. Por un momento hay algo en su mirada — claridad, horror, reconocimiento.",
       it="Si blocca. I suoi occhi si spalancano. Per un istante c'è qualcosa nel suo sguardo — lucidità, orrore, riconoscimento.")
    _t(tr, F, "anna_4",
       en="It's you. You are the one it draws. I see the spiral around you.",
       fr="C'est toi. Tu es celle qu'elle dessine. Je vois là spirale autour de toi.",
       es="Eres tú. Eres a quien dibuja. Veo la espiral a tu alrededor.",
       it="Sei tu. Sei quella che disegna. Vedo la spirale intorno a te.")
    _t(tr, F, "voss_anna",
       en="Anna! Enough. Go inside.",
       fr="Annà ! Çà suffit. Rentre.",
       es="¡Anna! Basta. Entra.",
       it="Anna! Basta così. Entra in casa.")
    _t(tr, F, "anna_6",
       en="Voss pushes his daughter gently but firmly back into the house. Before the door closes, I see Anna's hand. She is drawing spirals in the air with her finger.",
       fr="Voss pousse sà fille doucement mais fermement à l'intérieur. Avant que là porte ne se referme, je vois là main d'Anna. Elle dessine des spirales dans l'air avec son doigt.",
       es="Voss empuja a su hija suave pero firmemente de vuelta al interior. Antes de que la puerta se cierre, veo la mano de Anna. Está dibujando espirales en el aire con el dedo.",
       it="Voss spinge sua figlia dolcemente ma con fermezza dentro casa. Prima che la porta si chiuda, vedo la mano di Anna. Sta disegnando spirali nell'aria con il dito.")
    _t(tr, F, "journal_voss", en="Pastor Voss and Anna", fr="Le pasteur Voss et Anna", es="El pastor Voss y Anna", it="Il pastore Voss è Anna", field="title")
    _t(tr, F, "journal_voss",
       en="Pastor Voss warned me to flee. He knows of something beneath the church. His daughter Anna seems 'touched' — she saw a spiral around me. What does that mean?",
       fr="Le pasteur Voss m'à avertie de fuir. Il sait qu'il y à quelque chose sous l'église. Sà fille Annà semble « touchée » — elle à vu une spirale autour de moi. Qu'est-ce que celà signifie ?",
       es="El pastor Voss me advirtió que huyera. Sabe de algo bajo la iglesia. Su hija Anna parece estar 'tocada' — vio una espiral a mi alrededor. ¿Qué significa eso?",
       it="Il pastore Voss mi ha avvertita di fuggire. Sa di qualcosa sotto la chiesa. Sua figlia Anna sembra 'toccata' — ha visto una spirale intorno a me. Cosa significa?",
       field="content")
    _t(tr, F, "hilde_1",
       en="At the edge of the village, where the last houses give way to the forest, stands a small cottage. Herbs hang from the door, and the garden is astonishingly green despite November.",
       fr="En bordure du village, là où les dernières maisons cèdent là place à là forêt, se dresse une petite maison. Des herbes pendent à là porte, et le jardin est étonnamment vert malgré novembre.",
       es="En las afueras del pueblo, donde las últimas casas dan paso al bosque, se alza una pequeña cabaña. Hierbas cuelgan de la puerta, y el jardín está asombrosamente verde a pesar de ser noviembre.",
       it="Ai margini del villaggio, dove le ultime case lasciano il posto al bosco, sorge una piccola casetta. Erbe pendono dalla porta, è il giardino è sorprendentemente verde nonostante sia novembre.")
    _t(tr, F, "hilde_2", en="The door opens before I knock.", fr="Là porte s'ouvre avant que je frappe.", es="La puerta se abre antes de que llame.", it="La porta si apre prima che io bussi.")
    _t(tr, F, "hilde_3", en="I have been expecting you, child. Come in. The tea is ready.", fr="Je t'attendais, mon enfant. Entre. Le thé est prêt.", es="Te esperaba, niña. Entra. El té está listo.", it="Ti aspettavo, bambina mia. Entra. Il tè è pronto.")
    _t(tr, F, "hilde_4",
       en="Hilde Falkenberg. The herbalist of Graubach. Grandmother told me about her — a wise woman who knows the old ways. The ways before Christianity.",
       fr="Hilde Falkenberg. L'herboriste de Graubach. Grand-mère m'à parlé d'elle — une femme sage qui connaît les anciennes voies. Les voies d'avant le christianisme.",
       es="Hilde Falkenberg. La herbolaria de Graubach. La abuela me habló de ella — una mujer sabia que conoce los viejos caminos. Los caminos anteriores al cristianismo.",
       it="Hilde Falkenberg. L'erborista di Graubach. La nonna mi ha parlato di lei — una donna saggia che conosce le antiche vie. Le vie precedenti al cristianesimo.")
    _t(tr, F, "hilde_5",
       en="Her house smells of dried herbs, of honey and earth. Everywhere there are jars with strange contents. On the walls hang symbols — runes, spirals, and some I do not recognize.",
       fr="Sà maison sent les herbes séchées, le miel et là terre. Partout des bocaux au contenu étrange. Aux murs sont accrochés des symboles — des runes, des spirales, et d'autres que je ne reconnais pas.",
       es="Su casa huele a hierbas secas, a miel y a tierra. Por todas partes hay frascos con contenidos extraños. En las paredes cuelgan símbolos — runas, espirales, y algunos que no reconozco.",
       it="La sua casa odora di erbe essiccate, di miele è terra. Ovunque ci sono barattoli dal contenuto strano. Alle pareti sono appesi simboli — rune, spirali, è alcuni che non riconosco.")
    _t(tr, F, "hilde_6",
       en="Your grandmother was a clever woman. The cleverest in the village. She knew what was coming. And she made preparations.",
       fr="Tà grand-mère était une femme intelligente. Là plus intelligente du village. Elle savait ce qui allait arriver. Et elle s'y est préparée.",
       es="Tu abuela era una mujer inteligente. La más inteligente del pueblo. Sabía lo que venía. Y se preparó.",
       it="Tua nonna era una donna intelligente. La più intelligente del villaggio. Sapeva cosa sarebbe successo. È si è preparata.")
    _t(tr, F, "hilde_8", en="Drink the tea, Elise. It will protect you. For a while, at least.", fr="Bois le thé, Elise. Il te protégera. Pour un temps, du moins.", es="Bebe el té, Elise. Te protegerá. Al menos por un tiempo.", it="Bevi il tè, Elise. Ti proteggerà. Almeno per un po'.")
    _t(tr, F, "hilde_9",
       en="The tea tastes bitter and earthy. But as I drink, I feel a strange warmth spreading in my chest. The fear of last night recedes a little further.",
       fr="Le thé à un goût amer et terreux. Mais tandis que je bois, je sens une étrange chaleur se répandre dans mà poitrine. Là peur de là nuit dernière recule un peu.",
       es="El té sabe amargo y terroso. Pero mientras bebo, siento un calor extraño extendiéndose en mi pecho. El miedo de anoche se aleja un poco más.",
       it="Il tè ha un sapore amaro è terroso. Ma mentre bevo, sento un calore strano diffondersi nel petto. La paura della notte scorsa si allontana un poco.")
    _t(tr, F, "hilde_10",
       en="There are old ways and new ways. The pastor tries with prayers. But what sleeps beneath the church is older than his God. It requires older means.",
       fr="Il y à les voies anciennes et les voies nouvelles. Le pasteur essaie avec des prières. Mais ce qui dort sous l'église est plus ancien que son Dieu. Celà exige des moyens plus anciens.",
       es="Hay caminos viejos y caminos nuevos. El pastor lo intenta con oraciones. Pero lo que duerme bajo la iglesia es más antiguo que su Dios. Requiere medios más antiguos.",
       it="Ci sono vie antiche è vie nuove. Il pastore ci prova con le preghiere. Ma ciò che dorme sotto la chiesa è più antico del suo Dio. Richiede mezzi più antichi.")
    _t(tr, F, "hilde_12",
       en="Your grandmother knew both ways. She waited and prepared for thirty years. She wanted to do it differently this time — without sacrifice.",
       fr="Tà grand-mère connaissait les deux voies. Elle à attendu et s'est préparée pendant trente ans. Elle voulait faire autrement cette fois — sans sacrifice.",
       es="Tu abuela conocía ambos caminos. Esperó y se preparó durante treinta años. Quería hacerlo diferente esta vez — sin sacrificio.",
       it="Tua nonna conosceva entrambe le vie. Ha aspettato è si è preparata per trent'anni. Voleva farlo diversamente questa volta — senza sacrificio.")
    _t(tr, F, "hilde_13",
       en="But time caught up with her. Now you are here. And the question is: Are you ready to do what she could no longer do?",
       fr="Mais le temps l'à rattrapée. Maintenant tu es là. Et là question est : es-tu prête à faire ce qu'elle n'à plus pu accomplir ?",
       es="Pero el tiempo la alcanzó. Ahora estás tú aquí. Y la pregunta es: ¿estás lista para hacer lo que ella ya no pudo?",
       it="Ma il tempo l'ha raggiunta. Ora sei qui tu. È la domanda è: sei pronta a fare ciò che lei non ha più potuto?")
    _t(tr, F, "journal_hilde", en="Hilde, the Herbalist", fr="Hilde, l'herboriste", es="Hilde, la herbolaria", it="Hilde, l'erborista", field="title")
    _t(tr, F, "journal_hilde",
       en="Hilde knows the 'old ways' — pre-Christian rituals. Grandmother worked on a plan for 30 years to perform the ritual this time without sacrifice. Hilde seems to be an ally.",
       fr="Hilde connaît les « voies anciennes » — des rituels préchrétiens. Grand-mère à travaillé pendant 30 ans sur un plan pour accomplir le rituel cette fois sans sacrifice. Hilde semble être une alliée.",
       es="Hilde conoce los 'viejos caminos' — rituales precristianos. La abuela trabajó durante 30 años en un plan para realizar el ritual esta vez sin sacrificio. Hilde parece ser una aliada.",
       it="Hilde conosce le 'antiche vie' — rituali precristiani. La nonna ha lavorato per 30 anni a un piano per compiere il rituale questa volta senza sacrificio. Hilde sembra essere un'alleata.",
       field="content")
    _t(tr, F, "school_1",
       en="The schoolhouse stands beside the church. A small building with large windows through which I can see children sitting at wooden benches.",
       fr="L'école se dresse à côté de l'église. Un petit bâtiment avec de grandes fenêtres à travers lesquelles je vois des enfants assis sur des bancs en bois.",
       es="La escuela se alza junto a la iglesia. Un edificio pequeño con grandes ventanas a través de las cuales veo niños sentados en bancos de madera.",
       it="La scuola sorge accanto alla chiesa. Un piccolo edificio con grandi finestre attraverso le quali vedo bambini seduti su panche di legno.")
    _t(tr, F, "school_2",
       en="At the blackboard stands a man, explaining something. Konrad Müller. In daylight he looks... normal. Friendly. Even charismatic.",
       fr="Au tableau se tient un homme qui explique quelque chose. Konrad Müller. À là lumière du jour, il à l'air... normal. Amical. Même charismatique.",
       es="Ante la pizarra hay un hombre explicando algo. Konrad Müller. A la luz del día parece... normal. Amable. Incluso carismático.",
       it="Alla lavagna c'è un uomo che spiega qualcosa. Konrad Müller. Alla luce del giorno sembra... normale. Cordiale. Persino carismatico.")
    _t(tr, F, "school_3",
       en="When he notices me at the window, he smiles and waves me inside. The children turn around. Not one of them smiles.",
       fr="Quand il me remarque à là fenêtre, il sourit et me fait signe d'entrer. Les enfants se retournent. Aucun d'entre eux ne sourit.",
       es="Cuando me ve en la ventana, sonríe y me hace señas para que entre. Los niños se dan la vuelta. Ninguno de ellos sonríe.",
       it="Quando mi nota alla finestra, sorride è mi fa cenno di entrare. I bambini si girano. Nessuno di loro sorride.")
    _t(tr, F, "konrad_day_1",
       en="Fräulein Brandt! Children, this is Fräulein Brandt, the granddaughter of Frau Margarethe. She is a student in Berlin. From Berlin! Imagine that.",
       fr="Fräulein Brandt ! Les enfants, voici Fräulein Brandt, là petite-fille de Frau Margarethe. Elle est étudiante à Berlin. De Berlin ! Imaginez un peu.",
       es="¡Fräulein Brandt! Niños, esta es Fräulein Brandt, la nieta de Frau Margarethe. Es estudiante en Berlín. ¡De Berlín! Imagínense.",
       it="Fräulein Brandt! Bambini, questa è Fräulein Brandt, la nipote di Frau Margarethe. È studentessa a Berlino. Da Berlino! Pensate un po'.")
    _t(tr, F, "konrad_day_2",
       en="The children stare at me. Silent faces, old eyes in young bodies. A girl in the back row is drawing — I can see it from here. Spirals. Over and over, spirals.",
       fr="Les enfants me dévisagent. Des visages silencieux, des yeux vieux dans des corps jeunes. Une fille au dernier rang dessine — je le vois d'ici. Des spirales. Encore et encore, des spirales.",
       es="Los niños me miran fijamente. Rostros silenciosos, ojos viejos en cuerpos jóvenes. Una niña en la última fila dibuja — puedo verlo desde aquí. Espirales. Una y otra vez, espirales.",
       it="I bambini mi fissano. Volti silenziosi, occhi vecchi in corpi giovani. Una ragazzina nell'ultima fila disegna — posso vederlo da qui. Spirali. Sempre spirali.")
    _t(tr, F, "konrad_day_3", en="Break time, children. Go and play.", fr="Récréation, les enfants. Allez jouer.", es="Recreo, niños. Id a jugar.", it="Pausa, bambini. Andate a giocare.")
    _t(tr, F, "konrad_day_4",
       en="The children stand up and leave — not like children. No hasty movements, no laughter. They walk like small adults. Orderly. Silent.",
       fr="Les enfants se lèvent et sortent — pas comme des enfants. Pas de mouvements brusques, pas de rires. Ils marchent comme de petits adultes. En ordre. En silence.",
       es="Los niños se levantan y se van — no como niños. Sin movimientos apresurados, sin risas. Caminan como pequeños adultos. Ordenados. En silencio.",
       it="I bambini si alzano è se ne vanno — non come bambini. Nessun movimento affrettato, nessuna risata. Camminano come piccoli adulti. Ordinati. In silenzio.")
    _t(tr, F, "konrad_day_6",
       en="I am sorry about last night. I hope I did not frighten you. I sometimes take late walks — insomnia, you know.",
       fr="Je suis désolé pour hier soir. J'espère que je ne vous ai pas effrayée. Il m'arrive de faire des promenades tardives — l'insomnie, vous savez.",
       es="Lamento lo de anoche. Espero no haberla asustado. A veces doy paseos nocturnos — el insomnio, sabe usted.",
       it="Mi scusi per ieri notte. Spero di non averLa spaventata. A volte faccio delle passeggiate notturne — l'insonnia, sa com'è.")
    _t(tr, F, "konrad_day_7",
       en="Your grandmother is missed by the village. She was... an anchor, you know? Some people hold the world together without anyone noticing. Margarethe was one of them.",
       fr="Votre grand-mère manque au village. Elle était... un ancrage, vous savez ? Certaines personnes maintiennent le monde en un seul morceau sans que personne ne s'en aperçoive. Margarethe était de celles-là.",
       es="Su abuela es una pérdida para el pueblo. Era... un ancla, ¿sabe? Algunas personas mantienen el mundo unido sin que nadie lo note. Margarethe era una de ellas.",
       it="Al villaggio manca sua nonna. Era... un'ancora, sa? Certe persone tengono insieme il mondo senza che nessuno se ne accorga. Margarethe era una di queste.")
    _t(tr, F, "konrad_day_8",
       en="He sounds sincere. Even sad. But then he smooths his sleeve, and I see something on his hand. Ink stains? No — the lines are too regular.",
       fr="Il à l'air sincère. Même triste. Mais alors il lisse sà manche, et je vois quelque chose sur sà main. Des taches d'encre ? Non — les lignes sont trop régulières.",
       es="Suena sincero. Incluso triste. Pero entonces se alisa la manga, y veo algo en su mano. ¿Manchas de tinta? No — las líneas son demasiado regulares.",
       it="Sembra sincero. Persino triste. Ma poi si liscia la manica, è vedo qualcosa sulla sua mano. Macchie d'inchiostro? No — le linee sono troppo regolari.")
    _t(tr, F, "konrad_day_9",
       en="Spirals. On his palm. Carved or drawn, I cannot tell.",
       fr="Des spirales. Sur sà paume. Gravées où dessinées, je ne saurais dire.",
       es="Espirales. En la palma de su mano. Grabadas o dibujadas, no puedo distinguirlo.",
       it="Spirali. Sul palmo della mano. Incise o disegnate, non saprei dire.")
    _t(tr, F, "konrad_day_11",
       en="He notices my gaze and pulls his sleeve over his hand. The smile remains, but something in his eyes changes. Just for a split second.",
       fr="Il remarque mon regard et tire sà manche sur sà main. Le sourire reste, mais quelque chose dans ses yeux change. Juste une fraction de seconde.",
       es="Se da cuenta de mi mirada y se tira la manga sobre la mano. La sonrisa permanece, pero algo en sus ojos cambia. Solo por una fracción de segundo.",
       it="Si accorge del mio sguardo è tira la manica sulla mano. Il sorriso resta, ma qualcosa nei suoi occhi cambia. Solo per una frazione di secondo.")
    _t(tr, F, "journal_konrad", en="Konrad Müller, Village Teacher", fr="Konrad Müller, instituteur du village", es="Konrad Müller, maestro del pueblo", it="Konrad Müller, maestro del villaggio", field="title")
    _t(tr, F, "journal_konrad",
       en="Konrad is charming and friendly — almost too friendly. The children in his class behave strangely quietly. And on his palm he has spirals. Grandmother wrote that he was a 'vessel'. What really lies behind his smile?",
       fr="Konrad est charmant et amical — presque trop amical. Les enfants de sà classe se comportent étrangement calmement. Et sur sà paume, il à des spirales. Grand-mère à écrit qu'il était un « réceptacle ». Que cache vraiment son sourire ?",
       es="Konrad es encantador y amable — casi demasiado amable. Los niños de su clase se comportan de forma extrañamente silenciosa. Y en la palma de su mano tiene espirales. La abuela escribió que era un 'recipiente'. ¿Qué se esconde realmente detrás de su sonrisa?",
       it="Konrad è affascinante è cordiale — quasi troppo cordiale. I bambini nella sua classe si comportano in modo stranamente silenzioso. È sul palmo della mano ha delle spirali. La nonna scrisse che era un 'recipiente'. Cosa si nasconde davvero dietro il suo sorriso?",
       field="content")
    _t(tr, F, "route_next_location", en="The day is still long. I should keep looking around.", fr="Là journée est encore longue. Je devrais continuer à explorer.", es="El día aún es largo. Debería seguir explorando.", it="La giornata è ancora lunga. Dovrei continuare a guardarmi intorno.")
    _t(tr, F, "converge_1",
       en="In the early afternoon I meet Georg at the fountain. He looks as though he, too, did not sleep.",
       fr="En début d'après-midi, je retrouve Georg au puits. Il à l'air de ne pas avoir dormi non plus.",
       es="A primera hora de la tarde me encuentro con Georg en la fuente. Parece como si él tampoco hubiera dormido.",
       it="Nel primo pomeriggio incontro Georg alla fontana. Sembra che nemmeno lui abbia dormito.")
    _t(tr, F, "georg_day_1", en="Elise. Did you... was the night quiet?", fr="Elise. Est-ce que tu... là nuit à été calme ?", es="Elise. ¿Has... ha sido tranquila la noche?", it="Elise. Hai... è stata tranquilla la notte?")
    _t(tr, F, "georg_day_2",
       en="He asks it casually, but his eyes search my face for traces. Traces of what?",
       fr="Il pose là question d'un air détaché, mais ses yeux scrutent mon visage à là recherche de traces. Des traces de quoi ?",
       es="Lo pregunta como de pasada, pero sus ojos buscan huellas en mi rostro. ¿Huellas de qué?",
       it="Lo chiede con noncuranza, ma i suoi occhi cercano tracce sul mio viso. Tracce di cosa?")
    _t(tr, F, "georg_day_3",
       en="Come to my smithy this evening. For supper. I... I owe you some answers.",
       fr="Viens chez moi à là forge ce soir. Pour dîner. Je... je te dois quelques réponses.",
       es="Ven esta noche a mi herrería. A cenar. Yo... te debo algunas respuestas.",
       it="Vieni alla mia fucina stasera. Per cena. Io... ti devo alcune risposte.")
    _t(tr, F, "georg_day_5",
       en="But when you are there — do not speak to anyone about what I tell you. To no one, do you hear?",
       fr="Mais quand tu seras là-bas — ne parle à personne de ce que je te dirai. À personne, tu m'entends ?",
       es="Pero cuando estés allí — no hables con nadie de lo que te diga. Con nadie, ¿me oyes?",
       it="Ma quando sarai lì — non parlare con nessuno di quello che ti dirò. Con nessuno, mi senti?")
    _t(tr, F, "narration_afternoon",
       en="On the way back to Grandmother's house I pass the graveyard. A man is standing there, before a grave. Heavyset, grey-streaked hair, an expensive coat for such a village.",
       fr="Sur le chemin du retour vers là maison de grand-mère, je passe devant le cimetière. Un homme se tient là, devant une tombe. Corpulent, les cheveux grisonnants, un manteau coûteux pour un tel village.",
       es="De camino a la casa de la abuela paso por el cementerio. Un hombre está de pie allí, ante una tumba. Corpulento, cabello entrecano, un abrigo caro para un pueblo así.",
       it="Sulla via del ritorno verso la casa della nonna passo davanti al cimitero. Un uomo è fermo là, davanti a una tomba. Robusto, capelli brizzolati, un cappotto costoso per un villaggio simile.")
    _t(tr, F, "otto_1",
       en="Ah, you must be the young Brandt! Welcome to Graubach. I am Otto Reinhardt, mayor of our little village.",
       fr="Ah, vous devez être là jeune Brandt ! Bienvenue à Graubach. Je suis Otto Reinhardt, maire de notre petit village.",
       es="¡Ah, usted debe de ser la joven Brandt! Bienvenida a Graubach. Soy Otto Reinhardt, alcalde de nuestro pequeño pueblo.",
       it="Ah, Lei dev'essere la giovane Brandt! Benvenuta a Graubach. Sono Otto Reinhardt, sindaco del nostro piccolo villaggio.")
    _t(tr, F, "otto_2",
       en="His voice is loud, jovial. Too loud for a graveyard. Too jovial for a village living in fear.",
       fr="Sà voix est forte, joviale. Trop forte pour un cimetière. Trop joviale pour un village qui vit dans là peur.",
       es="Su voz es fuerte, jovial. Demasiado fuerte para un cementerio. Demasiado jovial para un pueblo que vive con miedo.",
       it="La sua voce è forte, gioviale. Troppo forte per un cimitero. Troppo gioviale per un villaggio che vive nella paura.")
    _t(tr, F, "otto_4",
       en="Your grandmother was a valued member of our community. We will hold a lovely funeral for her next week. Saturday, after the... after the church service.",
       fr="Votre grand-mère était un membre estimé de notre communauté. Nous organiserons de belles funérailles pour elle là semaine prochaine. Samedi, après la... après l'office.",
       es="Su abuela era un miembro apreciado de nuestra comunidad. Le haremos un bonito funeral la semana que viene. El sábado, después de la... después del oficio religioso.",
       it="Sua nonna era un membro stimato della nostra comunità. Le organizzeremo un bel funerale la settimana prossima. Sabato, dopo la... dopo la funzione religiosa.")
    _t(tr, F, "otto_5",
       en="He hesitated. Almost imperceptibly. 'After the...' — what had he meant to say? After the tradition? After the ritual?",
       fr="Il à hésité. De manière presque imperceptible. « Après la... » — qu'avait-il voulu dire ? Après là tradition ? Après le rituel ?",
       es="Ha dudado. Casi imperceptiblemente. 'Después de la...' — ¿qué había querido decir? ¿Después de la tradición? ¿Después del ritual?",
       it="Ha esitato. Quasi impercettibilmente. 'Dopo la...' — cosa aveva voluto dire? Dopo la tradizione? Dopo il rituale?")
    _t(tr, F, "otto_6",
       en="Do stay until then, Fräulein Brandt. It would not be right to let the granddaughter leave before the funeral. Graubach takes care of its own.",
       fr="Restez donc jusque-là, Fräulein Brandt. Il ne serait pas convenable de laisser là petite-fille partir avant les funérailles. Graubach prend soin des siens.",
       es="Quédese hasta entonces, Fräulein Brandt. No estaría bien dejar que la nieta se marche antes del funeral. Graubach cuida de los suyos.",
       it="Resti fino ad allora, Fräulein Brandt. Non sarebbe giusto lasciar partire la nipote prima del funerale. Graubach si prende cura dei suoi.")
    _t(tr, F, "otto_7",
       en="It sounds like an invitation. But in his eyes I read something else. It is not a wish. It is an expectation.",
       fr="Celà ressemble à une invitation. Mais dans ses yeux, je lis autre chose. Ce n'est pas un souhait. C'est une attente.",
       es="Suena como una invitación. Pero en sus ojos leo algo distinto. No es un deseo. Es una expectativa.",
       it="Sembra un invito. Ma nei suoi occhi leggo qualcos'altro. Non è un desiderio. È un'aspettativa.")
    _t(tr, F, "journal_otto", en="Mayor Reinhardt", fr="Le maire Reinhardt", es="El alcalde Reinhardt", it="Il sindaco Reinhardt", field="title")
    _t(tr, F, "journal_otto",
       en="Mayor Otto Reinhardt. Jovial, but with steely control. He wants me to stay until the funeral — 'next week, after the...' He interrupted himself. What takes place before the funeral?",
       fr="Le maire Otto Reinhardt. Jovial, mais d'une autorité d'acier. Il veut que je reste jusqu'aux funérailles — « là semaine prochaine, après la... » Il s'est interrompu. Que se passe-t-il avant les funérailles ?",
       es="El alcalde Otto Reinhardt. Jovial, pero con un control férreo. Quiere que me quede hasta el funeral — 'la semana que viene, después de la...' Se interrumpió a sí mismo. ¿Qué tiene lugar antes del funeral?",
       it="Il sindaco Otto Reinhardt. Gioviale, ma con un controllo d'acciaio. Vuole che io resti fino al funerale — 'la settimana prossima, dopo la...' Si è interrotto. Cosa ha luogo prima del funerale?",
       field="content")
    # --- Elise morning inner monologue ---
    _t(tr, F, "elise_morning_1",
       en="My hands are still trembling from the water. Or from the night. I am not sure.",
       fr="Mes mains tremblent encore à cause de l'eau. Ou de là nuit. Je ne sais pas.",
       es="Mis manos aún tiemblan por el agua. O por la noche. No estoy segura.",
       it="Le mie mani tremano ancora per l'acqua. O per la notte. Non ne sono sicura.")
    _t(tr, F, "elise_morning_plan",
       en="I have to talk to the people. Someone in this village knows what happened to Grandmother. And someone will tell me the truth — whether they want to or not.",
       fr="Je dois parler aux gens. Quelqu'un dans ce village sait ce qui est arrivé à grand-mère. Et quelqu'un me dirà là vérité — qu'il le veuille où non.",
       es="Tengo que hablar con la gente. Alguien en este pueblo sabe qué le pasó a la abuela. Y alguien me dirá la verdad — quiera o no.",
       it="Devo parlare con la gente. Qualcuno in questo villaggio sa cosa è successo alla nonna. È qualcuno mi dirà la verità — che lo voglia o no.")
    # --- Church: Elise dialogue with Voss ---
    _t(tr, F, "elise_church_spirals",
       en="The spirals on the headstones... I know this symbol from my studies. Pre-Christian. Celtic perhaps, or even older. But so concentrated in one place — that is unusual.",
       fr="Les spirales sur les pierres tombales... je connais ce symbole de mes études. Préchrétien. Celtique peut-être, où encore plus ancien. Mais aussi concentré en un seul endroit — c'est inhabituel.",
       es="Las espirales en las lápidas... conozco este símbolo de mis estudios. Precristiano. Celta quizás, o aún más antiguo. Pero tan concentrado en un solo lugar — eso es inusual.",
       it="Le spirali sulle lapidi... conosco questo simbolo dai miei studi. Precristiano. Celtico forse, o ancora più antico. Ma così concentrato in un unico luogo — è insolito.")
    _t(tr, F, "elise_church_intro",
       en="I am Elise Brandt. Margarethe's granddaughter. And I am looking for answers.",
       fr="Je suis Elise Brandt. Là petite-fille de Margarethe. Et je cherche des réponses.",
       es="Soy Elise Brandt. La nieta de Margarethe. Y busco respuestas.",
       it="Sono Elise Brandt. La nipote di Margarethe. È cerco risposte.")
    _t(tr, F, "elise_church_how",
       en="How do you know my name? I have not yet introduced myself.",
       fr="Comment connaissez-vous mon nom ? Je ne me suis pas encore présentée.",
       es="¿Cómo sabe mi nombre? Aún no me he presentado.",
       it="Come conosce il mio nome? Non mi sono ancora presentata.")
    _t(tr, F, "voss_4b",
       en="Everyone in Graubach knew your grandmother. And everyone knew you would come.",
       fr="Tout le monde à Graubach connaissait votre grand-mère. Et tout le monde savait que vous viendriez.",
       es="Todos en Graubach conocían a su abuela. Y todos sabían que usted vendría.",
       it="Tutti a Graubach conoscevano sua nonna. È tutti sapevano che Lei sarebbe venuta.")
    _t(tr, F, "elise_church_defiant",
       en="My grandmother called me here. I will not leave until I know why she had to die.",
       fr="Mà grand-mère m'à appelée ici. Je ne partirai pas avant de savoir pourquoi elle à dû mourir.",
       es="Mi abuela me llamó aquí. No me iré hasta saber por qué tuvo que morir.",
       it="Mia nonna mi ha chiamata qui. Non me ne andrò finché non saprò perché ha dovuto morire.")
    _t(tr, F, "elise_q_react",
       en="Beneath the church...?",
       fr="Sous l'église... ?",
       es="¿Bajo la iglesia...?",
       it="Sotto la chiesa...?")
    # --- Anna encounter ---
    _t(tr, F, "elise_anna_react",
       en="What? What do you see?",
       fr="Quoi ? Que vois-tu ?",
       es="¿Qué? ¿Qué ves?",
       it="Cosa? Cosa vedi?")
    _t(tr, F, "anna_4b",
       en="The singing. It sings your name. Over and over and over.",
       fr="Le chant. Il chante ton nom. Encore et encore et encore.",
       es="El canto. Canta tu nombre. Una y otra y otra vez.",
       it="Il canto. Canta il tuo nome. Di continuo, di continuo.")
    _t(tr, F, "elise_follow_anna",
       en="Wait — what does she mean? What sings my name?",
       fr="Attendez — que veut-elle dire ? Qu'est-ce qui chante mon nom ?",
       es="Espere — ¿qué quiere decir? ¿Qué canta mi nombre?",
       it="Aspetti — cosa intende? Cosa canta il mio nome?")
    _t(tr, F, "voss_blocks",
       en="Stay away from my daughter. She is ill. She does not know what she is saying.",
       fr="Restez loin de mà fille. Elle est malade. Elle ne sait pas ce qu'elle dit.",
       es="Aléjese de mi hija. Está enferma. No sabe lo que dice.",
       it="Stia lontana da mia figlia. È malata. Non sa quello che dice.")
    _t(tr, F, "elise_anna_monologue",
       en="Ill? No. The girl saw me — truly saw me. She perceived something around me that I myself cannot see. What is the spiral? And why does it sing my name?",
       fr="Malade ? Non. Là fille m'à vue — vraiment vue. Elle à perçu quelque chose autour de moi que je ne peux pas voir moi-même. Qu'est-ce que là spirale ? Et pourquoi chante-t-elle mon nom ?",
       es="¿Enferma? No. La niña me vio — realmente me vio. Percibió algo a mi alrededor que yo misma no puedo ver. ¿Qué es la espiral? ¿Y por qué canta mi nombre?",
       it="Malata? No. La ragazza mi ha vista — davvero vista. Ha percepito qualcosa intorno a me che io stessa non riesco a vedere. Cos'è la spirale? È perché canta il mio nome?")
    # --- Hilde: Elise dialogue ---
    _t(tr, F, "elise_hilde_arrive",
       en="How did you know I was coming?",
       fr="Comment saviez-vous que j'allais venir ?",
       es="¿Cómo sabía que iba a venir?",
       it="Come sapeva che sarei venuta?")
    _t(tr, F, "hilde_3b",
       en="Your grandmother told me about you. Often. You have her eyes, you know that?",
       fr="Tà grand-mère m'à parlé de toi. Souvent. Tu as ses yeux, tu le sais ?",
       es="Tu abuela me habló de ti. A menudo. Tienes sus ojos, ¿lo sabías?",
       it="Tua nonna mi ha parlato di te. Spesso. Hai i suoi occhi, lo sai?")
    _t(tr, F, "elise_hilde_personal",
       en="Hilde... how was my grandmother in her last years? Was she happy here?",
       fr="Hilde... comment était mà grand-mère ces dernières années ? Était-elle heureuse ici ?",
       es="Hilde... ¿cómo estaba mi abuela en sus últimos años? ¿Era feliz aquí?",
       it="Hilde... com'era mia nonna negli ultimi anni? Era felice qui?")
    _t(tr, F, "hilde_5b",
       en="Happy? No, child. But she was strong. The strongest woman I ever knew. Every morning she got up, drank her tea, and held the village together. For thirty years.",
       fr="Heureuse ? Non, mon enfant. Mais elle était forte. Là femme là plus forte que j'aie jamais connue. Chaque matin elle se levait, buvait son thé, et tenait le village debout. Pendant trente ans.",
       es="¿Feliz? No, niña. Pero era fuerte. La mujer más fuerte que he conocido. Cada mañana se levantaba, bebía su té, y mantenía el pueblo unido. Durante treinta años.",
       it="Felice? No, bambina. Ma era forte. La donna più forte che abbia mai conosciuto. Ogni mattina si alzava, beveva il suo tè, è teneva insieme il villaggio. Per trent'anni.")
    _t(tr, F, "elise_hilde_afraid",
       en="Was she afraid?",
       fr="Avait-elle peur ?",
       es="¿Tenía miedo?",
       it="Aveva paura?")
    _t(tr, F, "hilde_5c",
       en="...Yes. But not of what you think. She was afraid she would not see you again. And that you would receive her letter too late.",
       fr="...Oui. Mais pas de ce que tu crois. Elle avait peur de ne plus te revoir. Et que tu reçoives sà lettre trop tard.",
       es="...Sí. Pero no de lo que piensas. Tenía miedo de no volver a verte. Y de que recibieras su carta demasiado tarde.",
       it="...Sì. Ma non di quello che pensi. Aveva paura di non rivederti. È che tu ricevessi la sua lettera troppo tardi.")
    _t(tr, F, "narration_hilde_silence",
       en="For a moment I cannot speak. The lump in my throat is too large. Hilde lays a warm hand on my arm and waits.",
       fr="Pendant un instant, je ne peux pas parler. Le nœud dans mà gorge est trop gros. Hilde pose une main chaude sur mon bras et attend.",
       es="Por un momento no puedo hablar. El nudo en mi garganta es demasiado grande. Hilde me pone una mano cálida en el brazo y espera.",
       it="Per un momento non riesco a parlare. Il nodo in gola è troppo grande. Hilde mi mette una mano calda sul braccio è aspetta.")
    _t(tr, F, "elise_hilde_tea",
       en="What is in the tea? Forgive me, but in this village I trust no one blindly.",
       fr="Qu'y a-t-il dans le thé ? Pardonnez-moi, mais dans ce village je ne fais confiance à personne aveuglément.",
       es="¿Qué lleva el té? Discúlpeme, pero en este pueblo no confío en nadie a ciegas.",
       it="Cosa c'è nel tè? Mi perdoni, ma in questo villaggio non mi fido di nessuno alla cieca.")
    _t(tr, F, "hilde_8b",
       en="Suspicious. Good. You will need that here. Yarrow, mugwort, and valerian. Nothing dangerous. Your grandmother drank the same tea.",
       fr="Méfiante. Bien. Tu en auras besoin ici. Achillée, armoise et valériane. Rien de dangereux. Tà grand-mère buvait le même thé.",
       es="Desconfiada. Bien. Lo necesitarás aquí. Milenrama, artemisa y valeriana. Nada peligroso. Tu abuela bebía el mismo té.",
       it="Diffidente. Bene. Ne avrai bisogno qui. Achillea, artemisia è valeriana. Niente di pericoloso. Tua nonna beveva lo stesso tè.")
    _t(tr, F, "elise_hilde_effect",
       en="How did she do that? The fear is not gone — but it is quieter. As though someone had turned a dial.",
       fr="Comment a-t-elle fait çà ? Là peur n'à pas disparu — mais elle est plus discrète. Comme si quelqu'un avait tourné un bouton.",
       es="¿Cómo ha hecho eso? El miedo no se ha ido — pero es más silencioso. Como si alguien hubiera girado una perilla.",
       it="Come ha fatto? La paura non è sparita — ma è più silenziosa. Come se qualcuno avesse girato una manopola.")
    _t(tr, F, "elise_hilde_folklore",
       en="Old ways... You mean pre-Christian rituals? I study folklore in Berlin. I know the stories — the spirals, the earth mother, the threshold nights.",
       fr="Les voies anciennes... Vous parlez de rituels préchrétiens ? J'étudie le folklore à Berlin. Je connais les histoires — les spirales, là terre-mère, les nuits de passage.",
       es="Los viejos caminos... ¿Se refiere a rituales precristianos? Estudio folclore en Berlín. Conozco las historias — las espirales, la madre tierra, las noches de umbral.",
       it="Le antiche vie... Intende rituali precristiani? Studio folklore a Berlino. Conosco le storie — le spirali, la madre terra, le notti di soglia.")
    _t(tr, F, "hilde_10b",
       en="Stories? Child, what sleeps beneath the church is no story. But yes — you know more than most people here. That is good. That will help you.",
       fr="Des histoires ? Enfant, ce qui dort sous l'église n'est pas une histoire. Mais oui — tu en sais plus que là plupart des gens ici. C'est bien. Çà t'aidera.",
       es="¿Historias? Niña, lo que duerme bajo la iglesia no es un cuento. Pero sí — sabes más que la mayoría aquí. Eso es bueno. Te ayudará.",
       it="Storie? Bambina, quello che dorme sotto la chiesa non è una storia. Ma sì — sai più della maggior parte della gente qui. Questo è un bene. Ti aiuterà.")
    _t(tr, F, "elise_hilde_answer",
       en="I do not know if I am ready. But I am here. And I will not run away.",
       fr="Je ne sais pas si je suis prête. Mais je suis là. Et je ne fuirai pas.",
       es="No sé si estoy lista. Pero estoy aquí. Y no voy a huir.",
       it="Non so se sono pronta. Ma sono qui. È non scapperò.")
    _t(tr, F, "hilde_13b",
       en="It was enough for your grandmother. It will be enough for you. Come back to me when you have learned more. There is much I still have to show you.",
       fr="Çà à suffi pour tà grand-mère. Çà suffirà pour toi. Reviens me voir quand tu en sauras plus. Il y à beaucoup de choses que je dois encore te montrer.",
       es="Le bastó a tu abuela. Te bastará a ti. Vuelve cuando hayas averiguado más. Hay mucho que aún tengo que mostrarte.",
       it="È bastato per tua nonna. Basterà per te. Torna da me quando avrai scoperto di più. C'è molto che devo ancora mostrarti.")
    # --- School: Elise dialogue with Konrad ---
    _t(tr, F, "elise_school_hesitate",
       en="Georg said I should stay away from him. But I need to understand this man. Someone who knocks on strangers' doors at night has reasons. I want to hear his.",
       fr="Georg à dit que je devais rester loin de lui. Mais je dois comprendre cet homme. Quelqu'un qui frappe aux portes des étrangers là nuit à ses raisons. Je veux entendre les siennes.",
       es="Georg dijo que debería mantenerme alejada de él. Pero necesito entender a este hombre. Alguien que llama a puertas ajenas de noche tiene sus razones. Quiero oír las suyas.",
       it="Georg ha detto che dovrei stare lontana da lui. Ma devo capire quest'uomo. Chi bussa alle porte degli sconosciuti di notte ha le sue ragioni. Voglio sentire le sue.")
    _t(tr, F, "elise_school_greet",
       en="Good day. The children seem very... attentive.",
       fr="Bonjour. Les enfants semblent très... attentifs.",
       es="Buenos días. Los niños parecen muy... atentos.",
       it="Buongiorno. I bambini sembrano molto... attenti.")
    _t(tr, F, "elise_school_spirals_girl",
       en="The girl in the back row. Her spirals are identical to those on the church headstones. The same rotation, the same density. A child cannot draw that by chance.",
       fr="Là fille au dernier rang. Ses spirales sont identiques à celles sur les pierres tombales de l'église. Là même rotation, là même densité. Un enfant ne peut pas dessiner çà par hasard.",
       es="La niña de la última fila. Sus espirales son idénticas a las de las lápidas de la iglesia. La misma rotación, la misma densidad. Una niña no puede dibujar eso por casualidad.",
       it="La ragazza nell'ultima fila. Le sue spirali sono identiche a quelle sulle lapidi della chiesa. La stessa rotazione, la stessa densità. Una bambina non può disegnarle per caso.")
    _t(tr, F, "elise_school_children",
       en="Are the children here always this... quiet?",
       fr="Les enfants ici sont toujours aussi... silencieux ?",
       es="¿Los niños aquí siempre son tan... callados?",
       it="I bambini qui sono sempre così... silenziosi?")
    _t(tr, F, "konrad_day_4b",
       en="Graubach children are well-behaved children. The silence here educates them better than any teacher. Some would say they are precocious.",
       fr="Les enfants de Graubach sont des enfants bien élevés. Le silence ici les éduque mieux que n'importe quel professeur. Certains diraient qu'ils sont précoces.",
       es="Los niños de Graubach son niños bien educados. El silencio aquí los educa mejor que cualquier maestro. Algunos dirían que son precoces.",
       it="I bambini di Graubach sono bambini educati. Il silenzio qui li educa meglio di qualsiasi maestro. Alcuni direbbero che sono precoci.")
    _t(tr, F, "elise_school_why",
       en="Why were you outside my door in the middle of the night, Herr Müller? A walk does not lead to a particular front door.",
       fr="Pourquoi étiez-vous devant mà porte au milieu de là nuit, Herr Müller ? Une promenade ne mène pas à une porte en particulier.",
       es="¿Por qué estaba usted frente a mi puerta en mitad de la noche, Herr Müller? Un paseo no lleva a una puerta concreta.",
       it="Perché era davanti alla mia porta nel cuore della notte, Herr Müller? Una passeggiata non porta a una porta specifica.")
    _t(tr, F, "konrad_day_6b",
       en="When I saw light in Margarethe's house, I wanted to make sure everything was all right. Her house has been empty for three days. One becomes... attentive.",
       fr="Quand j'ai vu de là lumière dans là maison de Margarethe, je voulais m'assurer que tout allait bien. Sà maison est restée vide pendant trois jours. On devient... attentif.",
       es="Cuando vi luz en la casa de Margarethe, quise asegurarme de que todo estuviera bien. Su casa llevaba tres días vacía. Uno se vuelve... atento.",
       it="Quando ho visto luce nella casa di Margarethe, volevo assicurarmi che tutto fosse a posto. La sua casa è rimasta vuota per tre giorni. Si diventa... attenti.")
    _t(tr, F, "elise_school_anker",
       en="An anchor. A strange word. What exactly did she hold together?",
       fr="Un ancrage. Un mot étrange. Que maintenait-elle exactement ?",
       es="Un ancla. Una palabra extraña. ¿Qué mantenía ella unido exactamente?",
       it="Un'ancora. Una parola strana. Cosa teneva insieme esattamente?")
    _t(tr, F, "konrad_day_7b",
       en="Everything. She held everything together. More than you realize, Fräulein Brandt.",
       fr="Tout. Elle maintenait tout. Plus que vous ne l'imaginez, Fräulein Brandt.",
       es="Todo. Ella mantenía todo unido. Más de lo que usted se imagina, Fräulein Brandt.",
       it="Tutto. Teneva insieme tutto. Più di quanto Lei immagini, Fräulein Brandt.")
    _t(tr, F, "elise_school_hand",
       en="What is that on your hand, Herr Müller?",
       fr="Qu'est-ce que c'est sur votre main, Herr Müller ?",
       es="¿Qué es eso en su mano, Herr Müller?",
       it="Cos'è quello sulla Sua mano, Herr Müller?")
    _t(tr, F, "konrad_day_9c",
       en="Ink stains. The children work with cheap paper, it rubs off. Nothing more.",
       fr="Des taches d'encre. Les enfants travaillent avec du papier bon marché, çà déteint. Rien de plus.",
       es="Manchas de tinta. Los niños trabajan con papel barato, se corre. Nada más.",
       it="Macchie d'inchiostro. I bambini lavorano con carta economica, si trasferisce. Nient'altro.")
    _t(tr, F, "narration_konrad_lie",
       en="He is lying. The lines are too regular, too precise for ink stains. The same spirals as on the headstones, as in Anna's drawings. But his smile remains perfect.",
       fr="Il ment. Les lignes sont trop régulières, trop précises pour des taches d'encre. Les mêmes spirales que sur les pierres tombales, que dans les dessins d'Anna. Mais son sourire reste parfait.",
       es="Miente. Las líneas son demasiado regulares, demasiado precisas para ser manchas de tinta. Las mismas espirales que en las lápidas, que en los dibujos de Anna. Pero su sonrisa sigue siendo perfecta.",
       it="Mente. Le linee sono troppo regolari, troppo precise per essere macchie d'inchiostro. Le stesse spirali delle lapidi, dei disegni di Anna. Ma il suo sorriso resta perfetto.")
    _t(tr, F, "elise_school_monologue",
       en="Behind his smile lies something else. Something old. Grandmother wrote he was a 'vessel'. Now, in his eyes, I believe for a moment I can see what she meant.",
       fr="Derrière son sourire se cache autre chose. Quelque chose d'ancien. Grand-mère à écrit qu'il était un « réceptacle ». Maintenant, dans ses yeux, je crois voir un instant ce qu'elle voulait dire.",
       es="Detrás de su sonrisa hay algo más. Algo viejo. La abuela escribió que era un 'recipiente'. Ahora, en sus ojos, creo ver por un momento lo que quería decir.",
       it="Dietro il suo sorriso c'è qualcos'altro. Qualcosa di antico. La nonna scrisse che era un 'recipiente'. Ora, nei suoi occhi, credo di vedere per un istante ciò che intendeva.")
    # --- Converge: puzzle + Georg dialogue ---
    _t(tr, F, "narration_puzzle",
       en="Voss speaks of 'the Other' beneath the church. Anna sees spirals around me. Konrad HAS spirals on his hand. And Hilde knows the old ways. Everyone speaks in hints. No one tells the whole truth.",
       fr="Voss parle de « l'Autre » sous l'église. Annà voit des spirales autour de moi. Konrad A des spirales sur là main. Et Hilde connaît les anciennes voies. Tout le monde parle par allusions. Personne ne dit toute là vérité.",
       es="Voss habla del 'Otro' bajo la iglesia. Anna ve espirales a mi alrededor. Konrad TIENE espirales en la mano. Y Hilde conoce los viejos caminos. Todos hablan con indirectas. Nadie dice toda la verdad.",
       it="Voss parla dell'«Altro» sotto la chiesa. Anna vede spirali intorno a me. Konrad HA spirali sulla mano. È Hilde conosce le antiche vie. Tutti parlano per allusioni. Nessuno dice tutta la verità.")
    _t(tr, F, "elise_georg_respond",
       en="Not really. But you know that, don't you? Konrad Müller was at my door in the middle of the night.",
       fr="Pas vraiment. Mais tu le sais, n'est-ce pas ? Konrad Müller était à mà porte au milieu de là nuit.",
       es="No mucho. Pero tú lo sabes, ¿no? Konrad Müller estaba en mi puerta en mitad de la noche.",
       it="Non proprio. Ma tu lo sai, vero? Konrad Müller era alla mia porta nel cuore della notte.")
    _t(tr, F, "elise_georg_report",
       en="Georg, I looked around the village today. The pastor tells me to flee. His daughter sees things. Hilde speaks of old rituals. And Konrad has spirals on his hand. What is going on here?",
       fr="Georg, j'ai fait le tour du village aujourd'hui. Le pasteur me dit de fuir. Sà fille voit des choses. Hilde parle d'anciens rituels. Et Konrad à des spirales sur là main. Que se passe-t-il ici ?",
       es="Georg, hoy he recorrido el pueblo. El pastor me dice que huya. Su hija ve cosas. Hilde habla de rituales antiguos. Y Konrad tiene espirales en la mano. ¿Qué pasa aquí?",
       it="Georg, oggi ho fatto il giro del villaggio. Il pastore mi dice di fuggire. Sua figlia vede cose. Hilde parla di antichi rituali. È Konrad ha spirali sulla mano. Cosa sta succedendo qui?")
    _t(tr, F, "georg_react_alarmed",
       en="Konrad? Did you get close to him? Did he touch you?",
       fr="Konrad ? Tu t'es approchée de lui ? Il t'à touchée ?",
       es="¿Konrad? ¿Te acercaste a él? ¿Te tocó?",
       it="Konrad? Ti sei avvicinata a lui? Ti ha toccata?")
    _t(tr, F, "elise_georg_no",
       en="No. But his explanations sound too smooth. And he calls Grandmother an 'anchor'. The same word Hilde used.",
       fr="Non. Mais ses explications sonnent trop bien. Et il appelle grand-mère un « ancrage ». Le même mot que Hilde à utilisé.",
       es="No. Pero sus explicaciones suenan demasiado pulidas. Y llama a la abuela un 'ancla'. La misma palabra que usó Hilde.",
       it="No. Ma le sue spiegazioni suonano troppo lisce. È chiama la nonna un'«ancora». La stessa parola usata da Hilde.")
    _t(tr, F, "elise_georg_now",
       en="Why not now? Why always wait? Everyone in this village speaks in riddles, and you are no better!",
       fr="Pourquoi pas maintenant ? Pourquoi toujours attendre ? Tout le monde dans ce village parle en énigmes, et tu n'es pas mieux !",
       es="¿Por qué no ahora? ¿Por qué siempre esperar? Todos en este pueblo hablan con acertijos, ¡y tú no eres mejor!",
       it="Perché non adesso? Perché aspettare sempre? Tutti in questo villaggio parlano per enigmi, è tu non sei da meno!")
    _t(tr, F, "georg_day_3b",
       en="Because walls have ears in Graubach. At my house it is safe. Out here... it is not.",
       fr="Parce que les murs ont des oreilles à Graubach. Chez moi, c'est sûr. Ici dehors... non.",
       es="Porque las paredes tienen oídos en Graubach. En mi casa es seguro. Aquí fuera... no.",
       it="Perché i muri hanno orecchie a Graubach. A casa mia è sicuro. Qui fuori... no.")
    _t(tr, F, "elise_georg_afraid",
       en="Georg... do I have a reason to be afraid?",
       fr="Georg... ai-je une raison d'avoir peur ?",
       es="Georg... ¿tengo motivos para tener miedo?",
       it="Georg... ho motivo di aver paura?")
    _t(tr, F, "georg_day_5b",
       en="Georg looks at me for a long time. In his eyes lies something I cannot read. Guilt? Fear? Tenderness?",
       fr="Georg me regarde longuement. Dans ses yeux se lit quelque chose que je ne peux pas déchiffrer. De là culpabilité ? De là peur ? De là tendresse ?",
       es="Georg me mira durante largo rato. En sus ojos hay algo que no puedo descifrar. ¿Culpa? ¿Miedo? ¿Ternura?",
       it="Georg mi guarda a lungo. Nei suoi occhi c'è qualcosa che non riesco a decifrare. Colpa? Paura? Tenerezza?")
    _t(tr, F, "georg_day_5c",
       en="Come tonight. Then you will understand everything.",
       fr="Viens ce soir. Alors tu comprendras tout.",
       es="Ven esta noche. Entonces lo entenderás todo.",
       it="Vieni stasera. Allora capirai tutto.")
    # --- Afternoon: Otto dialogue + evening ---
    _t(tr, F, "narration_tired_walk",
       en="My legs are heavy. I have barely slept, barely eaten, and the village presses down on me like a hand on my chest. But I must not show weakness now.",
       fr="Mes jambes sont lourdes. J'ai à peine dormi, à peine mangé, et le village pèse sur moi comme une main sur mà poitrine. Mais je ne dois pas montrer de faiblesse maintenant.",
       es="Mis piernas están pesadas. Apenas he dormido, apenas he comido, y el pueblo me presiona como una mano sobre el pecho. Pero no puedo mostrar debilidad ahora.",
       it="Le mie gambe sono pesanti. Ho dormito appena, mangiato appena, è il villaggio mi preme addosso come una mano sul petto. Ma non devo mostrare debolezza adesso.")
    _t(tr, F, "elise_otto_greet",
       en="Mayor Reinhardt. I have already heard about you.",
       fr="Monsieur le Maire Reinhardt. On m'à déjà parlé de vous.",
       es="Alcalde Reinhardt. Ya me han hablado de usted.",
       it="Sindaco Reinhardt. Mi hanno già parlato di Lei.")
    _t(tr, F, "elise_otto_nach",
       en="After the... what exactly, Herr Mayor? You hesitated.",
       fr="Après la... quoi exactement, Monsieur le Maire ? Vous avez hésité.",
       es="Después de la... ¿qué exactamente, señor alcalde? Ha dudado.",
       it="Dopo la... cosa esattamente, signor Sindaco? Ha esitato.")
    _t(tr, F, "otto_4b",
       en="After the church service, of course. Saturday is the service. What else?",
       fr="Après l'office, bien sûr. Le samedi c'est l'office. Quoi d'autre ?",
       es="Después del oficio, por supuesto. El sábado es el oficio. ¿Qué si no?",
       it="Dopo la funzione religiosa, naturalmente. Il sabato c'è la funzione. Cos'altro?")
    _t(tr, F, "elise_otto_death",
       en="My grandmother lay alone in her house for three days. In a village where everyone knows everyone. How is that possible, Herr Mayor?",
       fr="Mà grand-mère est restée seule dans sà maison pendant trois jours. Dans un village où tout le monde se connaît. Comment est-ce possible, Monsieur le Maire ?",
       es="Mi abuela estuvo sola en su casa durante tres días. En un pueblo donde todos se conocen. ¿Cómo es eso posible, señor alcalde?",
       it="Mia nonna è rimasta sola in casa per tre giorni. In un villaggio dove tutti si conoscono. Com'è possibile, signor Sindaco?")
    _t(tr, F, "otto_6b",
       en="A tragic oversight. We all share the blame. But Graubach is a small village — sometimes things happen that should not have happened.",
       fr="Un tragique oubli. Nous en portons tous là responsabilité. Mais Graubach est un petit village — parfois il arrive des choses qui n'auraient pas dû arriver.",
       es="Un trágico descuido. Todos cargamos con la culpa. Pero Graubach es un pueblo pequeño — a veces ocurren cosas que no deberían haber ocurrido.",
       it="Una tragica svista. Ne portiamo tutti la colpa. Ma Graubach è un piccolo villaggio — a volte succedono cose che non sarebbero dovute succedere.")
    _t(tr, F, "elise_otto_monologue",
       en="I say nothing more. But I note his face. The way his smile does not reach his eyes. Otto Reinhardt knows more than anyone else in this village. And he wants me to stay. The question is: Why?",
       fr="Je ne dis plus rien. Mais je note son visage. Là manière dont son sourire n'atteint pas ses yeux. Otto Reinhardt en sait plus que quiconque dans ce village. Et il veut que je reste. Là question est : pourquoi ?",
       es="No digo nada más. Pero me fijo en su cara. La forma en que su sonrisa no llega a los ojos. Otto Reinhardt sabe más que nadie en este pueblo. Y quiere que me quede. La pregunta es: ¿por qué?",
       it="Non dico più niente. Ma mi segno il suo volto. Il modo in cui il suo sorriso non raggiunge gli occhi. Otto Reinhardt sa più di chiunque altro in questo villaggio. È vuole che io resti. La domanda è: perché?")
    _t(tr, F, "narration_evening_1",
       en="The sun sinks behind the mountains. The shadows of the houses grow long and sharp. In a few hours I will be sitting in Georg's smithy and finally getting answers. Or at least what Georg considers answers.",
       fr="Le soleil se couche derrière les montagnes. Les ombres des maisons s'allongent et s'aiguisent. Dans quelques heures, je serai assise dans là forge de Georg et j'obtiendrai enfin des réponses. Ou du moins ce que Georg considère comme des réponses.",
       es="El sol se hunde tras las montañas. Las sombras de las casas se alargan y se afilan. En unas horas estaré sentada en la herrería de Georg y por fin obtendré respuestas. O al menos lo que Georg considera respuestas.",
       it="Il sole cala dietro le montagne. Le ombre delle case si allungano è si affilano. Tra poche ore sarò seduta nella fucina di Georg è finalmente avrò delle risposte. O almeno quello che Georg considera risposte.")
    _t(tr, F, "narration_evening_singing",
       en="On the way to Grandmother's house I hear it again. Faint, almost imperceptible. The singing. It comes from everywhere and nowhere. And for the first time I believe I can make out individual syllables. My name.",
       fr="Sur le chemin de là maison de grand-mère, je l'entends à nouveau. Faible, presque imperceptible. Le chant. Il vient de partout et de nulle part. Et pour là première fois, je crois distinguer des syllabes individuelles. Mon nom.",
       es="De camino a la casa de la abuela lo oigo otra vez. Débil, casi imperceptible. El canto. Viene de todas partes y de ninguna. Y por primera vez creo distinguir sílabas individuales. Mi nombre.",
       it="Sulla strada verso la casa della nonna lo sento di nuovo. Debole, quasi impercettibile. Il canto. Viene da ovunque è da nessun luogo. È per la prima volta credo di distinguere singole sillabe. Il mio nome.")
    # Fix otto_5 content mismatch (JSON text differs from existing translation)
    _t(tr, F, "otto_5",
       en="He lied. So routinely that it was almost convincing. Almost. But his left eye twitched.",
       fr="Il à menti. Si machinalement que c'était presque convaincant. Presque. Mais son œil gauche à tressailli.",
       es="Ha mentido. Tan rutinariamente que casi era convincente. Casi. Pero su ojo izquierdo se ha crispado.",
       it="Ha mentito. Così meccanicamente che era quasi convincente. Quasi. Ma il suo occhio sinistro ha avuto un tic.")

def _add_act1_smithy_evening(tr):
    F = "res://data/dialogue/act1/smithy_evening.json"

    _t(tr, F, "narration_1", en="Georg's smithy smells of hot iron and coal. A familiar scent from childhood. Here he once showed me how to forge a nail.", fr="Là forge de Georg sent le fer brûlant et le charbon. Une odeur familière de l'enfance. C'est ici qu'il m'à montré un jour comment forger un clou.", es="La herrería de Georg huele a hierro caliente y carbón. Un olor familiar de la infancia. Aquí me enseñó una vez cómo forjar un clavo.", it="La fucina di Georg odora di ferro rovente è carbone. Un odore familiare dell'infanzia. Qui una volta mi mostrò come forgiare un chiodo.")
    _t(tr, F, "narration_2", en="Tonight the fire has burned low. Georg sits at the table, before him two plates of stew and a jug of beer. He looks ten years older than yesterday.", fr="Ce soir, le feu est presque éteint. Georg est assis à là table, devant lui deux assiettes de ragoût et une cruche de bière. Il à l'air d'avoir vieilli de dix ans depuis hier.", es="Esta noche el fuego se ha consumido. Georg está sentado a la mesa, ante él dos platos de estofado y una jarra de cerveza. Parece diez años más viejo que ayer.", it="Stasera il fuoco si è quasi spento. Georg è seduto al tavolo, davanti a lui due piatti di stufato è una brocca di birra. Sembra invecchiato di dieci anni rispetto a ieri.")
    _t(tr, F, "georg_1", en="Sit down. Eat. And then... then I will tell you what I can.", fr="Assieds-toi. Mange. Et puis... puis je te raconterai ce que je peux.", es="Siéntate. Come. Y después... después te contaré lo que pueda.", it="Siediti. Mangia. È poi... poi ti racconterò quello che posso.")
    _t(tr, F, "narration_3", en="We eat in silence. The stew tastes of nothing. Or perhaps it is I who can no longer taste anything.", fr="Nous mangeons en silence. Le ragoût n'à aucun goût. Ou peut-être est-ce moi qui ne goûte plus rien.", es="Comemos en silencio. El estofado no sabe a nada. O quizás soy yo quien ya no sabe saborear nada.", it="Mangiamo in silenzio. Lo stufato non sa di niente. O forse sono io che non riesco più a sentire i sapori.")
    _t(tr, F, "georg_3", en="In Graubach there is a tradition. As old as the village itself. Older, perhaps. The elders pass it down from generation to generation.", fr="À Graubach, il y à une tradition. Aussi vieille que le village lui-même. Plus vieille, peut-être. Les anciens là transmettent de génération en génération.", es="En Graubach hay una tradición. Tan vieja como el propio pueblo. Más vieja, quizás. Los ancianos la transmiten de generación en generación.", it="A Graubach c'è una tradizione. Antica quanto il villaggio stesso. Più antica, forse. Gli anziani la tramandano di generazione in generazione.")
    _t(tr, F, "georg_4", en="Every thirty years, in November, when the nights grow longest... a price must be paid.", fr="Tous les trente ans, en novembre, quand les nuits deviennent les plus longues... un prix doit être payé.", es="Cada treinta años, en noviembre, cuando las noches se hacen más largas... hay que pagar un precio.", it="Ogni trent'anni, a novembre, quando le notti si fanno più lunghe... un prezzo deve essere pagato.")
    _t(tr, F, "georg_5", en="The old folk call it the 'Feeding'. The mayor calls it 'tradition'. Your grandmother called it murder.", fr="Les anciens l'appellent là « Nourriture ». Le maire l'appelle « tradition ». Tà grand-mère appelait çà un meurtre.", es="Los viejos lo llaman la 'Alimentación'. El alcalde lo llama 'tradición'. Tu abuela lo llamaba asesinato.", it="I vecchi la chiamano la 'Nutrizione'. Il sindaco la chiama 'tradizione'. Tua nonna la chiamava omicidio.")
    _t(tr, F, "georg_7", en="And she was right. It is murder, Elise. Every time they choose someone. Someone whose name is written in the book. They lead him into the chamber beneath the church, and...", fr="Et elle avait raison. C'est un meurtre, Elise. À chaque fois, ils choisissent quelqu'un. Quelqu'un dont le nom est inscrit dans le livre. Ils le conduisent dans là chambre sous l'église, et...", es="Y tenía razón. Es un asesinato, Elise. Cada vez eligen a alguien. Alguien cuyo nombre está escrito en el libro. Lo llevan a la cámara bajo la iglesia, y...", it="E aveva ragione. È un omicidio, Elise. Ogni volta scelgono qualcuno. Qualcuno il cui nome è scritto nel libro. Lo conducono nella camera sotto la chiesa, e...")
    _t(tr, F, "georg_8", en="He breaks off. His hands grip the beer jug so tightly that the knuckles stand out white.", fr="Il s'interrompt. Ses mains serrent là cruche de bière si fort que ses phalanges blanchissent.", es="Se interrumpe. Sus manos aprietan la jarra de cerveza con tanta fuerza que los nudillos se le ponen blancos.", it="Si interrompe. Le sue mani stringono la brocca di birra così forte che le nocche diventano bianche.")
    _t(tr, F, "georg_9", en="He does not come back. No one ever comes back.", fr="Il ne revient pas. Personne ne revient jamais.", es="No vuelve. Nadie vuelve jamás.", it="Non torna. Nessuno torna mai.")
    _t(tr, F, "georg_10", en="The last time was 1893. My grandfather... he was a young man then. He saw it. He never spoke of it, but he never laughed again either.", fr="Là dernière fois, c'était en 1893. Mon grand-père... il était jeune à l'époque. Il l'à vu. Il n'en à jamais parlé, mais il n'à plus jamais ri non plus.", es="La última vez fue en 1893. Mi abuelo... era un hombre joven entonces. Lo vio. Nunca habló de ello, pero tampoco volvió a reír jamás.", it="L'ultima volta è stato nel 1893. Mio nonno... era un giovane allora. L'ha visto. Non ne ha mai parlato, ma non ha mai più riso.")
    _tc(tr, F, "choice_georg_smithy",
        en_choices=["Is my name in that book?", "Why does no one stop this? Why does no one go to the police?", "What is this 'something' beneath the church?"],
        fr_choices=["Mon nom est-il dans ce livre ?", "Pourquoi personne n'arrête ça ? Pourquoi personne ne va à la police ?", "Qu'est-ce que cette « chose » sous l'église ?"],
        es_choices=["¿Está mi nombre en ese libro?", "¿Por qué nadie detiene esto? ¿Por qué nadie acude a la policía?", "¿Qué es eso que hay bajo la iglesia?"],
        it_choices=["Il mio nome è in quel libro?", "Perché nessuno ferma tutto questo? Perché nessuno va alla polizia?", "Cos'è questa 'cosa' sotto la chiesa?"])
    _t(tr, F, "georg_name_1", en="Georg looks at me. The answer is in his eyes before he speaks it.", fr="Georg me regarde. Là réponse est dans ses yeux avant qu'il ne là prononce.", es="Georg me mira. La respuesta está en sus ojos antes de que la pronuncie.", it="Georg mi guarda. La risposta è nei suoi occhi prima che la pronunci.")
    _t(tr, F, "georg_name_2", en="Yes.", fr="Oui.", es="Sí.", it="Sì.")
    _t(tr, F, "georg_name_3", en="Your grandmother found out years ago. She tried to cross it out, to burn it away, to tear out the page. But the name always comes back.", fr="Tà grand-mère l'à découvert il y à des années. Elle à essayé de le rayer, de le brûler, d'arracher là page. Mais le nom revient toujours.", es="Tu abuela lo descubrió hace años. Intentó tacharlo, quemarlo, arrancar la página. Pero el nombre siempre vuelve.", it="Tua nonna l'ha scoperto anni fa. Ha provato a cancellarlo, a bruciarlo, a strappare la pagina. Ma il nome torna sempre.")
    _t(tr, F, "georg_name_4", en="That is why she worked for thirty years. On another way. A ritual that binds the entity without demanding a sacrifice.", fr="C'est pourquoi elle à travaillé pendant trente ans. Sur un autre moyen. Un rituel qui lie l'entité sans exiger de sacrifice.", es="Por eso trabajó durante treinta años. En otro camino. Un ritual que ata a la entidad sin exigir un sacrificio.", it="Per questo ha lavorato per trent'anni. A un'altra via. Un rituale che vincola l'entità senza richiedere un sacrificio.")
    _t(tr, F, "georg_police_1", en="Police? Elise, the nearest police post is two days' travel away. And even then — what should I tell them? That a monster lives under our church?", fr="Là police ? Elise, le poste de police le plus proche est à deux jours de route. Et même ainsi — que devrais-je leur dire ? Qu'un monstre vit sous notre église ?", es="¿La policía? Elise, el puesto de policía más cercano está a dos días de viaje. Y aun así — ¿qué les diría? ¿Que un monstruo vive bajo nuestra iglesia?", it="La polizia? Elise, il posto di polizia più vicino è a due giorni di viaggio. È anche così — cosa dovrei dirgli? Che un mostro vive sotto la nostra chiesa?")
    _t(tr, F, "georg_police_2", en="Besides... whoever does not believe in the tradition disappears. Not in the chamber. Just like that. In the forest, on the road, in the night. The mayor sees to it.", fr="Et puis... quiconque ne croit pas à là tradition disparaît. Pas dans là chambre. Comme ça, tout simplement. Dans là forêt, sur là route, dans là nuit. Le maire s'en charge.", es="Además... quien no cree en la tradición desaparece. No en la cámara. Así, sin más. En el bosque, en el camino, en la noche. El alcalde se encarga de eso.", it="E poi... chi non crede nella tradizione scompare. Non nella camera. Così, senza più. Nel bosco, sulla strada, nella notte. Il sindaco provvede.")
    _t(tr, F, "georg_police_3", en="This village is a prison, Elise. And the wardens wear no uniform.", fr="Ce village est une prison, Elise. Et les gardiens ne portent pas d'uniforme.", es="Este pueblo es una prisión, Elise. Y los carceleros no llevan uniforme.", it="Questo villaggio è una prigione, Elise. È i carcerieri non portano divisa.")
    _t(tr, F, "georg_entity_1", en="I do not know. Not really. No one knows. We only know that it is old. Older than the forest, older than the mountains.", fr="Je ne sais pas. Pas vraiment. Personne ne sait. Nous savons seulement que c'est ancien. Plus ancien que là forêt, plus ancien que les montagnes.", es="No lo sé. No realmente. Nadie lo sabe. Solo sabemos que es antiguo. Más antiguo que el bosque, más antiguo que las montañas.", it="Non lo so. Non davvero. Nessuno lo sa. Sappiamo solo che è antico. Più antico della foresta, più antico delle montagne.")
    _t(tr, F, "georg_entity_2", en="It sleeps. Most of the time it sleeps. But every thirty years the sleep grows lighter. It stirs. It dreams. And its dreams... seep upward.", fr="Çà dort. Là plupart du temps, çà dort. Mais tous les trente ans, le sommeil devient plus léger. Çà remue. Çà rêve. Et ses rêves... suintent vers là surface.", es="Duerme. La mayor parte del tiempo duerme. Pero cada treinta años el sueño se vuelve más ligero. Se agita. Sueña. Y sus sueños... se filtran hacia arriba.", it="Dorme. Per la maggior parte del tempo dorme. Ma ogni trent'anni il sonno si fa più leggero. Si muove. Sogna. È i suoi sogni... filtrano verso l'alto.")
    _t(tr, F, "georg_entity_3", en="The singing you heard? Those are its dreams, Elise. It sings in its sleep.", fr="Le chant que tu as entendu ? Ce sont ses rêves, Elise. Çà chante dans son sommeil.", es="¿El canto que oíste? Son sus sueños, Elise. Canta mientras duerme.", it="Il canto che hai sentito? Sono i suoi sogni, Elise. Canta nel sonno.")
    _t(tr, F, "georg_final_1", en="Elise, I have a key. To the chamber beneath the church. Your grandmother entrusted it to me.", fr="Elise, j'ai une clé. Celle de là chambre sous l'église. Tà grand-mère me l'à confiée.", es="Elise, tengo una llave. De la cámara bajo la iglesia. Tu abuela me la confió.", it="Elise, ho una chiave. Della camera sotto la chiesa. Tua nonna me l'ha affidata.")
    _t(tr, F, "georg_final_2", en="He places a heavy iron key on the table. It is old, the teeth worn down. On the grip a spiral is engraved.", fr="Il pose une lourde clé de fer sur là table. Elle est vieille, les dents usées. Sur là poignée, une spirale est gravée.", es="Pone una pesada llave de hierro sobre la mesa. Es vieja, los dientes desgastados. En la empuñadura hay una espiral grabada.", it="Posa una pesante chiave di ferro sul tavolo. È vecchia, i denti consumati. Sull'impugnatura è incisa una spirale.")
    _t(tr, F, "georg_final_3", en="She wanted you to have it. 'When Elise comes,' she said, 'give her the key. She will know what to do.'", fr="Elle voulait que tu l'aies. « Quand Elise viendrà », a-t-elle dit, « donne-lui là clé. Elle saurà quoi faire. »", es="Quería que la tuvieras tú. 'Cuando Elise venga', dijo, 'dale la llave. Ella sabrá qué hacer.'", it="Voleva che l'avessi tu. 'Quando Elise verrà', ha detto, 'dalle la chiave. Saprà cosa fare.'")
    _t(tr, F, "georg_final_5", en="But not tonight. And not alone. Promise me that.", fr="Mais pas ce soir. Et pas seule. Promets-le-moi.", es="Pero no esta noche. Y no sola. Prométemelo.", it="Ma non stasera. È non da sola. Promettimelo.")
    _t(tr, F, "journal_smithy", en="Georg's Confession", fr="Là confession de Georg", es="La confesión de Georg", it="La confessione di Georg", field="title")
    _t(tr, F, "journal_smithy", en="Every 30 years a sacrifice — the 'Feeding'. My name is in the book. Grandmother worked on an alternative ritual. Georg gave me the key to the chamber. I must find out what Grandmother planned.", fr="Tous les 30 ans un sacrifice — là « Nourriture ». Mon nom est dans le livre. Grand-mère travaillait sur un rituel alternatif. Georg m'à donné là clé de là chambre. Je dois découvrir ce que grand-mère avait prévu.", es="Cada 30 años un sacrificio — la 'Alimentación'. Mi nombre está en el libro. La abuela trabajaba en un ritual alternativo. Georg me ha dado la llave de la cámara. Debo descubrir qué planeaba la abuela.", it="Ogni 30 anni un sacrificio — la 'Nutrizione'. Il mio nome è nel libro. La nonna lavorava a un rituale alternativo. Georg mi ha dato la chiave della camera. Devo scoprire cosa aveva pianificato la nonna.", field="content")
    _tc(tr, F, "choice_night2",
        en_choices=["Stay in Graubach and investigate", "Try to flee — tomorrow at dawn"],
        fr_choices=["Rester à Graubach et enquêter", "Tenter de fuir — demain à l'aube"],
        es_choices=["Quedarme en Graubach e investigar", "Intentar huir — mañana al amanecer"],
        it_choices=["Restare a Graubach e indagare", "Tentare di fuggire — domani all'alba"])
    _t(tr, F, "stay_decision", en="Flee? No. Grandmother called me here. She fought for thirty years. I will not run away.", fr="Fuir ? Non. Grand-mère m'à appelée ici. Elle s'est battue pendant trente ans. Je ne fuirai pas.", es="¿Huir? No. La abuela me llamó aquí. Luchó durante treinta años. No voy a huir.", it="Fuggire? No. La nonna mi ha chiamata qui. Ha combattuto per trent'anni. Non scapperò.")
    _t(tr, F, "stay_2", en="Besides — if my name is in that book, running will change nothing. The letter found me in Berlin. Whatever it is, it knows where I am.", fr="Et puis — si mon nom est dans ce livre, fuir ne changerà rien. Là lettre m'à trouvée à Berlin. Quoi que ce soit, çà sait où je suis.", es="Además — si mi nombre está en ese libro, huir no cambiará nada. La carta me encontró en Berlín. Sea lo que sea, sabe dónde estoy.", it="E poi — se il mio nome è in quel libro, fuggire non cambierà nulla. La lettera mi ha trovata a Berlino. Qualunque cosa sia, sa dove mi trovo.")
    _t(tr, F, "flee_decision", en="Enough. I am a student, not a heroine. Tomorrow at dawn I leave. On foot, if I must.", fr="Assez. Je suis étudiante, pas une héroïne. Demain à l'aube, je pars. À pied, s'il le faut.", es="Basta. Soy estudiante, no una heroína. Mañana al amanecer me voy. A pie, si es necesario.", it="Basta. Sono una studentessa, non un'eroina. Domani all'alba me ne vado. A piedi, se necessario.")
    _t(tr, F, "flee_2", en="But as I walk back to Grandmother's house, I notice that the forest stands closer than this morning. The trees at the edge of the village — they were not so dense. Not so near.", fr="Mais en retournant vers là maison de grand-mère, je remarque que là forêt est plus proche qu'au matin. Les arbres en bordure du village — ils n'étaient pas si denses. Pas si proches.", es="Pero mientras camino de vuelta a la casa de la abuela, noto que el bosque está más cerca que esta mañana. Los árboles en las afueras del pueblo — no eran tan densos. No estaban tan cerca.", it="Ma mentre torno verso la casa della nonna, noto che il bosco è più vicino di stamattina. Gli alberi ai margini del villaggio — non erano così fitti. Non così vicini.")
    _t(tr, F, "flee_3", en="And on the road by which the carriage came lies a fallen tree. A huge, ancient tree. It looks as if it had grown there.", fr="Et sur le chemin par lequel là calèche est venue, un arbre est tombé. Un arbre immense et ancien. On dirait qu'il à poussé là.", es="Y en el camino por el que vino el carruaje hay un árbol caído. Un árbol enorme y antiguo. Parece como si hubiera crecido allí.", it="E sulla strada da cui è venuta la carrozza giace un albero abbattuto. Un albero enorme è antico. Sembra come se fosse cresciuto lì.")
    _t(tr, F, "flee_4", en="Graubach does not want to let me go.", fr="Graubach ne veut pas me laisser partir.", es="Graubach no quiere dejarme ir.", it="Graubach non vuole lasciarmi andare.")
    _t(tr, F, "narration_end_1", en="The second night in Graubach falls. The candle in Grandmother's bedroom keeps burning. The singing from the depths begins earlier than yesterday.", fr="Là deuxième nuit à Graubach tombe. Là bougie dans là chambre de grand-mère continue de brûler. Le chant des profondeurs commence plus tôt qu'hier.", es="Cae la segunda noche en Graubach. La vela en el dormitorio de la abuela sigue ardiendo. El canto desde las profundidades comienza más temprano que ayer.", it="Cala la seconda notte a Graubach. La candela nella camera da letto della nonna continua a bruciare. Il canto dalle profondità comincia prima di ieri.")
    _t(tr, F, "narration_end_2", en="And it is louder.", fr="Et il est plus fort.", es="Y es más fuerte.", it="Ed è più forte.")
    _t(tr, F, "narration_end_3", en="End of Act 1", fr="Fin de l'acte 1", es="Fin del acto 1", it="Fine dell'atto 1")

    # --- Additional translations (auto-generated) ---

    _t(tr, F, "elise_sit",
       en="I don't want half-truths, Georg. Not anymore. From anyone.",
       fr="Je ne veux pas de demi-verites, Georg. Plus maintenant. De personne.",
       es="No quiero medias verdades, Georg. Ya no. De nadie.",
       it="Non voglio mezze verità, Georg. Non più. Da nessuno.")

    _t(tr, F, "elise_tradition_1",
       en="Tradition? What kind of tradition? Hilde spoke of it too.",
       fr="Tradition? Quelle tradition? Hilde en a parle aussi.",
       es="Tradicion? Que clase de tradicion? Hilde tambien hablo de ello.",
       it="Tradizione? Che tipo di tradizione? Anche Hilde ne ha parlato.")

    _t(tr, F, "elise_tradition_2",
       en="Every thirty years? Georg, that sounds like superstition. Like an old tale that peasants tell each other.",
       fr="Tous les trente ans? Georg, cela ressemble a de la superstition. A une vieille histoire que les paysans se racontent.",
       es="Cada treinta años? Georg, eso suena a supersticion. A un viejo cuento que se cuentan los campesinos.",
       it="Ogni trent'anni? Georg, sembra superstizione. Una vecchia storia che i contadini si raccontano.")

    _t(tr, F, "georg_4b",
       en="You saw the candle. The one in Margarethe's bedroom. It has been burning for days and doesn't get shorter. Is THAT superstition?",
       fr="Tu as vu la bougie. Celle dans la chambre de Margarethe. Elle brule depuis des jours et ne raccourcit pas. C'est CA de la superstition?",
       es="Viste la vela. La del dormitorio de Margarethe. Lleva dias encendida y no se acorta. ESO es supersticion?",
       it="Hai visto la candela. Quella nella camera di Margarethe. Brucia da giorni e non si accorcia. QUESTA e superstizione?")

    _t(tr, F, "elise_tradition_3",
       en="I want to object. But he's right. The candle burns. The singing comes from beneath the earth. And Anna saw something around me that no child could invent.",
       fr="Je veux protester. Mais il a raison. La bougie brule. Le chant vient de sous la terre. Et Anna a vu quelque chose autour de moi qu'aucun enfant ne pourrait inventer.",
       es="Quiero protestar. Pero tiene razon. La vela arde. El canto viene de debajo de la tierra. Y Anna vio algo a mi alrededor que ningun niño podria inventar.",
       it="Vorrei obiettare. Ma ha ragione. La candela brucia. Il canto viene da sotto terra. E Anna ha visto qualcosa intorno a me che nessun bambino potrebbe inventare.")

    _t(tr, F, "elise_mord_react",
       en="The word hits me like a blow. My spoon clatters against the plate.",
       fr="Le mot me frappe comme un coup. Ma cuillere tinte contre l'assiette.",
       es="La palabra me golpea como un punetazo. Mi cuchara tintinea contra el plato.",
       it="La parola mi colpisce come un pugno. Il mio cucchiaio tintinna contro il piatto.")

    _t(tr, F, "elise_mord_react_2",
       en="Murder? Georg, listen to yourself! What are you saying?",
       fr="Un meurtre? Georg, écoute-toi! Qu'est-ce que tu racontes?",
       es="Asesinato? Georg, escuchate! Que estas diciendo?",
       it="Omicidio? Georg, ascoltati! Cosa stai dicendo?")

    _t(tr, F, "georg_5b",
       en="The truth. You didn't want half-truths, so you'll get the whole truth.",
       fr="La vérité. Tu ne voulais pas de demi-verites, alors tu auras la vérité entière.",
       es="La verdad. No querias medias verdades, asi que tendras la verdad completa.",
       it="La verità. Non volevi mezze verità, quindi avrai tutta la verità.")

    _t(tr, F, "elise_wer",
       en="Who? Who was the last victim?",
       fr="Qui? Qui était la dernière victime?",
       es="Quien? Quien fue la ultima victima?",
       it="Chi? Chi e stata l'ultima vittima?")

    _t(tr, F, "elise_scale",
       en="1893. Thirty years. That means 1863. And before that. And before that. How many people has this village sacrificed? How many generations have kept silent?",
       fr="1893. Trente ans. Cela signifie 1863. Et avant. Et encore avant. Combien de personnes ce village a-t-il sacrifiees? Combien de generations ont garde le silence?",
       es="1893. Treinta años. Eso significa 1863. Y antes de eso. Y antes. Cuantas personas ha sacrificado este pueblo? Cuantas generaciones han guardado silencio?",
       it="1893. Trent'anni. Significa 1863. E prima ancora. E prima ancora. Quante persone ha sacrificato questo villaggio? Quante generazioni hanno taciuto?")

    _t(tr, F, "elise_police_react",
       en="That people are disappearing! That's enough!",
       fr="Que des gens disparaissent! Ça suffit!",
       es="Que la gente desaparece! Eso basta!",
       it="Che delle persone scompaiono! Questo basta!")

    _t(tr, F, "elise_entity_react",
       en="In my studies there are reports of such beings. Old gods sleeping in the earth. I always thought they were metaphors.",
       fr="Dans mes études, il y a des rapports sur de tels etres. D'anciens dieux dormant dans la terre. J'ai toujours cru que c'étaient des métaphores.",
       es="En mis estudios hay informes sobre seres asi. Dioses antiguos que duermen en la tierra. Siempre pense que eran metaforas.",
       it="Nei miei studi ci sono resoconti di tali esseri. Antichi dei che dormono nella terra. Ho sempre pensato fossero metafore.")

    _t(tr, F, "georg_name_reveal",
       en="Georg is silent for a moment. Then he rubs his eyes, as if he has to force himself to continue speaking.",
       fr="Georg se tait un instant. Puis il se frotte les yeux, comme s'il devait se forcer a continuer.",
       es="Georg calla un momento. Luego se frota los ojos, como si tuviera que obligarse a seguir hablando.",
       it="Georg tace un momento. Poi si strofina gli occhi, come se dovesse costringersi a continuare a parlare.")

    _t(tr, F, "georg_name_reveal_2",
       en="There's something else you need to know. Your name, Elise. It's in the book. In the book in the chamber.",
       fr="Il y a autre chose que tu dois savoir. Ton nom, Elise. Il est dans le livre. Dans le livre de la chambre.",
       es="Hay algo mas que debes saber. Tu nombre, Elise. Esta en el libro. En el libro de la camara.",
       it="C'e un'altra cosa che devi sapere. Il tuo nome, Elise. E nel libro. Nel libro della camera.")

    _t(tr, F, "georg_name_reveal_3",
       en="Your grandmother tried to erase it. Cross it out, burn it out, tear out the page. But the name keeps coming back.",
       fr="Ta grand-mère a essaye de l'effacer. Le rayer, le bruler, arracher la page. Mais le nom revient toujours.",
       es="Tu abuela intento borrarlo. Tacharlo, quemarlo, arrancar la pagina. Pero el nombre siempre vuelve.",
       it="Tua nonna ha cercato di cancellarlo. Depennarlo, bruciarlo, strappare la pagina. Ma il nome ritorna sempre.")

    _t(tr, F, "elise_breakdown_1",
       en="No. No, that can't be.",
       fr="Non. Non, c'est impossible.",
       es="No. No, eso no puede ser.",
       it="No. No, non può essere.")

    _t(tr, F, "elise_breakdown_2",
       en="I stand up. The chair scrapes across the stone floor. My heart is hammering so loudly that I'm sure Georg can hear it.",
       fr="Je me leve. La chaise racle le sol de pierre. Mon coeur bat si fort que je suis sure que Georg peut l'entendre.",
       es="Me levanto. La silla raspa el suelo de piedra. Mi corazon late tan fuerte que estoy segura de que Georg puede oirlo.",
       it="Mi alzo. La sedia raschia sul pavimento di pietra. Il mio cuore martella così forte che sono sicura che Georg possa sentirlo.")

    _t(tr, F, "elise_breakdown_4",
       en="She KNEW? For thirty years she knew that my name was in that damned book? And she told me NOTHING?",
       fr="Elle SAVAIT? Pendant trente ans, elle savait que mon nom était dans ce maudit livre? Et elle ne m'a RIEN dit?",
       es="Lo SABIA? Durante treinta años supo que mi nombre estaba en ese maldito libro? Y no me dijo NADA?",
       it="Lo SAPEVA? Per trent'anni sapeva che il mio nome era in quel maledetto libro? E non mi ha detto NIENTE?")

    _t(tr, F, "georg_defend_1",
       en="She protected you, Elise. For thirty years she searched for a way to change the ritual. For YOU.",
       fr="Elle t'a protégée, Elise. Pendant trente ans, elle a cherche un moyen de modifier le rituel. Pour TOI.",
       es="Te protegio, Elise. Durante treinta años busco una forma de cambiar el ritual. Por TI.",
       it="Ti ha protetta, Elise. Per trent'anni ha cercato un modo per cambiare il rituale. Per TE.")

    _t(tr, F, "elise_breakdown_5",
       en="Protected? She lured me into a trap! Her letter, the journey, everything...",
       fr="Protegee? Elle m'a attiree dans un piege! Sa lettre, le voyage, tout...",
       es="Protegida? Me atrajo a una trampa! Su carta, el viaje, todo...",
       it="Protetta? Mi ha attirata in una trappola! La sua lettera, il viaggio, tutto...")

    _t(tr, F, "georg_defend_2",
       en="No. She gave you the chance to end it. Not as a victim. As the person who breaks this cycle. Forever.",
       fr="Non. Elle t'a donne la chance d'y mettre fin. Pas en tant que victime. En tant que celle qui brise ce cycle. Pour toujours.",
       es="No. Te dio la oportunidad de acabar con esto. No como victima. Como la persona que rompe este ciclo. Para siempre.",
       it="No. Ti ha dato la possibilita di porre fine a tutto. Non come vittima. Come colei che spezza questo ciclo. Per sempre.")

    _t(tr, F, "elise_breakdown_6",
       en="Silence. Only the crackling of the fire. I sit back down. My hands are trembling. But behind the fear, something else is growing. Something hard.",
       fr="Silence. Seul le crépitement du feu. Je me rassieds. Mes mains tremblent. Mais derrière la peur, quelque chose d'autre grandit. Quelque chose de dur.",
       es="Silencio. Solo el crepitar del fuego. Me siento de nuevo. Mis manos tiemblan. Pero detras del miedo crece algo mas. Algo duro.",
       it="Silenzio. Solo il crepitio del fuoco. Mi risiedo. Le mie mani tremano. Ma dietro la paura cresce qualcos'altro. Qualcosa di duro.")

    _t(tr, F, "elise_breakdown_7",
       en="What did she plan? What exactly do I have to do?",
       fr="Qu'est-ce qu'elle a planifie? Que dois-je faire exactement?",
       es="Que planeo ella? Que tengo que hacer exactamente?",
       it="Cosa ha pianificato? Cosa devo fare esattamente?")

    _t(tr, F, "elise_key_1",
       en="I take the key. It's heavier than it looks. The metal is cold, but the spiral on the handle - it feels warm under my fingers. As if something inside it were pulsing.",
       fr="Je prends la clé. Elle est plus lourde qu'elle n'en a l'air. Le metal est froid, mais la spirale sur la poignee - elle est chaude sous mes doigts. Comme si quelque chose a l'interieur pulsait.",
       es="Tomo la llave. Es mas pesada de lo que parece. El metal esta frio, pero la espiral en la empunadura - se siente calida bajo mis dedos. Como si algo en su interior latiera.",
       it="Prendo la chiave. E più pesante di quanto sembri. Il metallo e freddo, ma la spirale sull'impugnatura - e calda sotto le mie dita. Come se qualcosa al suo interno pulsasse.")

    _t(tr, F, "elise_key_2",
       en="What does she expect of me, Georg? I'm a student. I read books about folklore. I'm not... not a heroine.",
       fr="Qu'attend-elle de moi, Georg? Je suis étudiante. Je lis des livres sur le folklore. Je ne suis pas... pas une héroïne.",
       es="Que espera de mi, Georg? Soy estudiante. Leo libros sobre folclore. No soy... no soy una heroina.",
       it="Cosa si aspetta da me, Georg? Sono una studentessa. Leggo libri sul folklore. Non sono... non sono un'eroina.")

    _t(tr, F, "elise_key_3",
       en="But not today. And not alone. Promise me that.",
       fr="Mais pas aujourd'hui. Et pas seule. Promets-le-moi.",
       es="Pero no hoy. Y no sola. Prometemelo.",
       it="Ma non oggi. E non da sola. Promettimelo.")

    _t(tr, F, "elise_key_promise",
       en="I promise.",
       fr="Je le promets.",
       es="Lo prometo.",
       it="Lo prometto.")

    _t(tr, F, "narration_deliberate_1",
       en="Outside it has grown dark. The lanterns in the smithy cast dancing shadows. The key sits heavy in my coat pocket.",
       fr="Dehors, il fait nuit. Les lanternes de la forge projettent des ombres dansantes. La clé pese lourd dans la poche de mon manteau.",
       es="Afuera ha oscurecido. Las linternas de la herreria proyectan sombras danzantes. La llave pesa en el bolsillo de mi abrigo.",
       it="Fuori e calata l'oscurità. Le lanterne della fucina proiettano ombre danzanti. La chiave pesa nella tasca del mio cappotto.")

    _t(tr, F, "narration_deliberate_2",
       en="My mind says: Run. Pack your things and run. You're not a folklorist studying an old ritual. You are the VICTIM of a ritual.",
       fr="Mon esprit dit: Fuis. Fais tes bagages et fuis. Tu n'es pas une folkloriste qui étudie un vieux rituel. Tu es la VICTIME d'un rituel.",
       es="Mi mente dice: Huye. Haz las maletas y huye. No eres una folklorista que estudia un viejo ritual. Eres la VICTIMA de un ritual.",
       it="La mia mente dice: Fuggi. Fai le valigie e fuggi. Non sei una folklorista che studia un vecchio rituale. Sei la VITTIMA di un rituale.")

    _t(tr, F, "narration_deliberate_3",
       en="But the key in my pocket is warm. And Grandmother's voice is in my head, as clear as if she were standing beside me: 'You are my light against the darkness.'",
       fr="Mais la clé dans ma poche est chaude. Et la voix de Grand-mère est dans ma tête, aussi claire que si elle se tenait a cote de moi: 'Tu es ma lumière contre les tenebres.'",
       es="Pero la llave en mi bolsillo esta caliente. Y la voz de la abuela esta en mi cabeza, tan clara como si estuviera a mi lado: 'Eres mi luz contra la oscuridad.'",
       it="Ma la chiave nella mia tasca e calda. E la voce della nonna e nella mia testa, chiara come se fosse accanto a me: 'Tu sei la mia luce contro l'oscurità.'")

    _t(tr, F, "narration_deliberate_4",
       en="For thirty years she fought. For me. Should I now flee and make her struggle meaningless?",
       fr="Pendant trente ans, elle s'est battue. Pour moi. Dois-je maintenant fuir et rendre son combat vain?",
       es="Durante treinta años lucho. Por mi. Debo huir ahora y hacer que su lucha no tenga sentido?",
       it="Per trent'anni ha lottato. Per me. Dovrei fuggire adesso e rendere vana la sua lotta?")

    _t(tr, F, "stay_3",
       en="Tomorrow I'll need Hilde's herbs, Voss' knowledge of the chamber, and every scrap of information Grandmother left behind. There is a plan. I just have to find it.",
       fr="Demain j'aurai besoin des herbes de Hilde, du savoir de Voss sur la chambre et de chaque bribe d'information que Grand-mère a laissee. Il y a un plan. Je dois juste le trouver.",
       es="Manana necesitare las hierbas de Hilde, el conocimiento de Voss sobre la camara y cada pedazo de informacion que dejo la abuela. Hay un plan. Solo tengo que encontrarlo.",
       it="Domani mi serviranno le erbe di Hilde, la conoscenza di Voss sulla camera e ogni frammento di informazione che la nonna ha lasciato. C'e un piano. Devo solo trovarlo.")

    _t(tr, F, "flee_5",
       en="I try another way. The path to the neighboring village. But the trees stand so close together here that barely any moonlight gets through. And between the trunks... something moves.",
       fr="J'essaie un autre chemin. Le sentier vers le village voisin. Mais les arbres sont si serres ici que la lumière de la lune passe a peine. Et entre les troncs... quelque chose bouge.",
       es="Intento otro camino. El sendero hacia el pueblo vecino. Pero los arboles estan tan juntos aqui que apenas pasa la luz de la luna. Y entre los troncos... algo se mueve.",
       it="Provo un'altra strada. Il sentiero verso il villaggio vicino. Ma gli alberi sono così fitti qui che a malapena filtra il chiaro di luna. E tra i tronchi... qualcosa si muove.")

    _t(tr, F, "flee_7",
       en="I walk faster. Then I run. But every path leads back to the village. Every crossroads ends in a dead end of trees that weren't there yesterday.",
       fr="Je marche plus vite. Puis je cours. Mais chaque chemin ramene au village. Chaque croisement aboutit a un cul-de-sac d'arbres qui n'étaient pas la hier.",
       es="Camino mas rapido. Luego corro. Pero cada camino lleva de vuelta al pueblo. Cada cruce termina en un callejon sin salida de arboles que ayer no estaban ahi.",
       it="Cammino più veloce. Poi corro. Ma ogni sentiero riporta al villaggio. Ogni incrocio finisce in un vicolo cieco di alberi che ieri non c'erano.")

    _t(tr, F, "flee_8",
       en="Graubach doesn't want to let me go.",
       fr="Graubach ne veut pas me laisser partir.",
       es="Graubach no quiere dejarme ir.",
       it="Graubach non vuole lasciarmi andare.")

    _t(tr, F, "flee_9",
       en="Breathing heavily, I stand in front of Grandmother's house again. The key in my pocket pulses warm, as if to say: You know what you have to do.",
       fr="Haletante, je me retrouve devant la maison de Grand-mère. La clé dans ma poche pulse chaleureusement, comme pour dire: Tu sais ce que tu dois faire.",
       es="Respirando con dificultad, estoy de nuevo frente a la casa de la abuela. La llave en mi bolsillo pulsa calida, como diciendo: Sabes lo que tienes que hacer.",
       it="Ansimante, mi ritrovo davanti alla casa della nonna. La chiave nella mia tasca pulsa calda, come a dire: Sai cosa devi fare.")

    _t(tr, F, "narration_end_2b",
       en="I lie in bed, the key in my hand. The spiral presses into my palm. The singing forms words I can almost understand. Almost.",
       fr="Je suis allongee dans le lit, la clé dans la main. La spirale s'imprime dans ma paume. Le chant forme des mots que je peux presque comprendre. Presque.",
       es="Estoy acostada en la cama, la llave en la mano. La espiral se clava en mi palma. El canto forma palabras que casi puedo entender. Casi.",
       it="Sono distesa a letto, la chiave in mano. La spirale si imprime nel palmo. Il canto forma parole che quasi riesco a capire. Quasi.")


def _add_act2_investigation_morning(tr):
    F = "res://data/dialogue/act2/investigation_morning.json"

    _t(tr, F, "narration_1",
       en="Day three. The morning sun falls through the dusty curtains, but it brings no warmth. I barely slept.",
       fr="Troisième jour. Le soleil matinal filtre à travers les rideaux poussiéreux, mais il ne réchauffe pas. J'ai à peine dormi.",
       es="Tercer día. El sol de la mañana se filtra por las cortinas polvorientas, pero no calienta. Apenas he dormido.",
       it="Terzo giorno. Il sole del mattino filtra attraverso le tende impolverate, ma non scalda. Ho dormito a malapena.")

    _t(tr, F, "narration_2",
       en="Grandmother's house holds answers. She spent thirty years working on an alternative ritual — her notes must be somewhere in here.",
       fr="Là maison de grand-mère recèle des réponses. Elle à passé trente ans à travailler sur un rituel alternatif — ses notes doivent se trouver quelque part ici.",
       es="La casa de la abuela guarda respuestas. Pasó treinta años trabajando en un ritual alternativo — sus anotaciones deben estar en algún lugar aquí.",
       it="La casa della nonna custodisce delle risposte. Ha lavorato trent'anni a un rituale alternativo — i suoi appunti devono trovarsi da qualche parte qui dentro.")

    _tc(tr, F, "choice_search",
        en_choices=["Search the study", "Investigate the cellar", "Thoroughly search her bedroom"],
        fr_choices=["Fouiller le bureau", "Explorer la cave", "Fouiller sa chambre à coucher"],
        es_choices=["Registrar el estudio", "Investigar el sótano", "Revisar a fondo su dormitorio"],
        it_choices=["Perquisire lo studio", "Ispezionare la cantina", "Esaminare a fondo la sua camera da letto"])

    _t(tr, F, "search_study",
       en="The study is a chaos of books and papers. Grandmother was obsessed — dozens of books on folklore, occultism, pre-Christian rituals of the Black Forest.",
       fr="Le bureau est un chaos de livres et de papiers. Grand-mère était obsédée — des dizaines de livres sur le folklore, l'occultisme, les rituels préchrétiens de là Forêt-Noire.",
       es="El estudio es un caos de libros y papeles. La abuela estaba obsesionada — decenas de libros sobre folclore, ocultismo, rituales precristianos de la Selva Negra.",
       it="Lo studio è un caos di libri è carte. La nonna era ossessionata — dozzine di libri su folklore, occultismo, rituali precristiani della Foresta Nera.")

    _t(tr, F, "search_study_2",
       en="Between the pages of a well-thumbed book on Germanic binding rituals, I find loose sheets. Grandmother's handwriting, tight and hurried.",
       fr="Entre les pages d'un livre usé sur les rituels de liaison germaniques, je trouve des feuilles volantes. L'écriture de grand-mère, serrée et hâtive.",
       es="Entre las páginas de un libro manoseado sobre rituales de atadura germánicos, encuentro hojas sueltas. La letra de la abuela, apretada y apresurada.",
       it="Tra le pagine di un libro consunto sui rituali di legamento germanici, trovo dei fogli sciolti. La calligrafia della nonna, fitta è frettolosa.")

    _t(tr, F, "find_notes_study",
       en="'The seal must be renewed, not with blood, but with will. Three components: the sign of the earth, the chant of the ancients, and an anchor — someone who knows the entity but does not fear it.'",
       fr="« Le sceau doit être renouvelé, non par le sang, mais par là volonté. Trois composants : le signe de là terre, le chant des anciens et une ancre — quelqu'un qui connaît l'entité mais ne là craint pas. »",
       es="«El sello debe renovarse, no con sangre, sino con voluntad. Tres componentes: el signo de la tierra, el canto de los antiguos y un ancla — alguien que conozca a la entidad pero no la tema.»",
       it="'Il sigillo deve essere rinnovato, non con il sangue, ma con la volontà. Tre componenti: il segno della terra, il canto degli antichi è un'ancora — qualcuno che conosca l'entità ma non la tema.'")

    _t(tr, F, "search_cellar",
       en="The cellar smells of damp earth and something sweeter — herbs, perhaps. Dried bundles of plants hang on the wall, carefully labeled.",
       fr="Là cave sent là terre humide et quelque chose de plus doux — des herbes, peut-être. Des bouquets de plantes séchées sont accrochés au mur, soigneusement étiquetés.",
       es="El sótano huele a tierra húmeda y a algo más dulce — hierbas, quizás. Manojos de plantas secas cuelgan de la pared, cuidadosamente etiquetados.",
       it="La cantina odora di terrà umida è di qualcosa di più dolce — erbe, forse. Fasci di piante essiccate pendono dalla parete, accuratamente etichettati.")

    _t(tr, F, "search_cellar_3",
       en="Behind a loose stone in the wall, I find a tin box. Inside: a leather-bound notebook, a small pouch of herbs, and a folded note.",
       fr="Derrière une pierre descellée dans le mur, je trouve une boîte en fer-blanc. À l'intérieur : un carnet relié en cuir, une petite bourse d'herbes et un billet plié.",
       es="Detrás de una piedra suelta en la pared, encuentro una caja de hojalata. Dentro: un cuaderno encuadernado en cuero, una bolsita de hierbas y una nota doblada.",
       it="Dietro una pietra smossa nel muro, trovo una scatola di latta. All'interno: un quaderno rilegato in pelle, un sacchettino di erbe è un biglietto piegato.")

    _t(tr, F, "search_cellar_4",
       en="'For Elise, when the time comes. You will understand. — M.' Grandmother's initials. The notebook is her journal.",
       fr="« Pour Elise, quand le moment viendra. Tu comprendras. — M. » Les initiales de grand-mère. Le carnet est son journal.",
       es="«Para Elise, cuando llegue el momento. Lo comprenderás. — M.» Las iniciales de la abuela. El cuaderno es su diario.",
       it="'Per Elise, quando verrà il momento. Capirai. — M.' Le iniziali della nonna. Il quaderno è il suo diario.")

    _t(tr, F, "search_bedroom",
       en="Grandmother's bedroom looks the same as the day she died. The bed neatly made, as though she had known she wouldn't return.",
       fr="Là chambre de grand-mère à là même apparence que le jour de sà mort. Le lit soigneusement fait, comme si elle avait su qu'elle ne reviendrait pas.",
       es="El dormitorio de la abuela luce igual que el día de su muerte. La cama pulcramente hecha, como si hubiera sabido que no regresaría.",
       it="La camera da letto della nonna appare come il giorno della sua morte. Il letto rifatto con cura, come se avesse saputo che non sarebbe tornata.")

    _t(tr, F, "search_bedroom_2",
       en="Beneath the loose floorboard beside the bed — where she used to hide sweets for me — lies a package wrapped in waxed cloth.",
       fr="Sous là lame de plancher descellée à côté du lit — là où elle cachait autrefois des bonbons pour moi — se trouve un paquet enveloppé de toile cirée.",
       es="Bajo la tabla suelta junto a la cama — donde solía esconder dulces para mí — hay un paquete envuelto en tela encerada.",
       it="Sotto l'asse del pavimento allentata accanto al letto — dove un tempo nascondeva le caramelle per me — giace un involto avvolto in tela cerata.")

    _t(tr, F, "search_bedroom_3",
       en="An old notebook, filled with writing. On the first page: 'Records of the Entity Beneath Graubach. Begun 1893, continued to the present day.'",
       fr="Un vieux carnet, entièrement rempli. Sur là première page : « Chroniques de l'Entité sous Graubach. Commencé en 1893, poursuivi jusqu'à ce jour. »",
       es="Un viejo cuaderno, repleto de escritura. En la primera página: «Registros de la Entidad bajo Graubach. Iniciado en 1893, continuado hasta hoy.»",
       it="Un vecchio quaderno, fitto di scrittura. Sulla prima pagina: 'Annotazioni sull'Entità sotto Graubach. Iniziato nel 1893, proseguito fino ad oggi.'")

    _t(tr, F, "journal_entry_found",
       en="Grandmother's Journal",
       fr="Journal de grand-mère",
       es="Diario de la abuela",
       it="Diario della nonna",
       field="title")

    _t(tr, F, "journal_entry_found",
       en="Found grandmother's records. She documented 30 years of research on the entity beneath the church and an alternative binding ritual. Three components needed: the sign of the earth, the chant of the ancients, an anchor.",
       fr="Trouvé les notes de grand-mère. Elle à documenté 30 ans de recherches sur l'entité sous l'église et un rituel de liaison alternatif. Trois composants nécessaires : le signe de là terre, le chant des anciens, une ancre.",
       es="Encontrados los registros de la abuela. Documentó 30 años de investigación sobre la entidad bajo la iglesia y un ritual de atadura alternativo. Tres componentes necesarios: el signo de la tierra, el canto de los antiguos, un ancla.",
       it="Trovati gli appunti della nonna. Ha documentato 30 anni di ricerche sull'entità sotto la chiesa è un rituale di legamento alternativo. Tre componenti necessari: il segno della terra, il canto degli antichi, un'ancora.",
       field="content")

    _t(tr, F, "read_journal_1",
       en="I leaf through the journal. The early entries are sober, almost scientific. But as the years pass, the handwriting grows more restless.",
       fr="Je feuillette le journal. Les premières entrées sont sobres, presque scientifiques. Mais au fil des années, l'écriture devient de plus en plus agitée.",
       es="Hojeo el diario. Las primeras entradas son sobrias, casi científicas. Pero con el paso de los años, la letra se vuelve más inquieta.",
       it="Sfoglio il diario. Le prime annotazioni sono sobrie, quasi scientifiche. Ma col passare degli anni, la calligrafia si fa sempre più inquieta.")

    _t(tr, F, "read_journal_2",
       en="'1903: The spiral appears everywhere. In the bark of the trees, in the pattern of the frost, in my dreams. It knows that I am searching.'",
       fr="« 1903 : Là spirale apparaît partout. Dans l'écorce des arbres, dans les motifs du givre, dans mes rêves. Il sait que je cherche. »",
       es="«1903: La espiral aparece en todas partes. En la corteza de los árboles, en los dibujos de la escarcha, en mis sueños. Sabe que estoy investigando.»",
       it="'1903: La spirale appare ovunque. Nella corteccia degli alberi, nei disegni del gelo, nei miei sogni. Sa che sto indagando.'")

    _t(tr, F, "read_journal_3",
       en="'1915: Hilde taught me an ancient chant. It dates from before the Romans. When I hum it, the air grows heavy and the singing from the depths falls silent for hours.'",
       fr="« 1915 : Hilde m'à enseigné un chant ancien. Il date d'avant les Romains. Quand je le fredonne, l'air s'alourdit et le chant des profondeurs se tait pendant des heures. »",
       es="«1915: Hilde me enseñó un canto antiguo. Data de antes de los romanos. Cuando lo tarareo, el aire se vuelve pesado y el canto de las profundidades enmudece durante horas.»",
       it="'1915: Hilde mi ha insegnato un canto antico. Risale a prima dei romani. Quando lo canticchio, l'aria si fa pesante è il canto dalle profondità ammutolisce per ore.'")

    _t(tr, F, "read_journal_5",
       en="'1921: Konrad's eyes. I saw it. For a moment, as the sun hung low, his eyes were not his own. The entity has found a vessel.'",
       fr="« 1921 : Les yeux de Konrad. Je l'ai vu. Pendant un instant, alors que le soleil était bas, ses yeux n'étaient plus les siens. L'entité à trouvé un réceptacle. »",
       es="«1921: Los ojos de Konrad. Lo vi. Por un instante, cuando el sol estaba bajo, sus ojos no eran los suyos. La entidad ha encontrado un recipiente.»",
       it="'1921: Gli occhi di Konrad. L'ho visto. Per un istante, mentre il sole era basso, i suoi occhi non erano i suoi. L'entità ha trovato un ricettacolo.'")

    _t(tr, F, "narration_midmorning",
       en="I close the journal. My hands are trembling. Grandmother knew about Konrad. She knew everything.",
       fr="Je referme le journal. Mes mains tremblent. Grand-mère savait pour Konrad. Elle savait tout.",
       es="Cierro el diario. Me tiemblan las manos. La abuela sabía lo de Konrad. Lo sabía todo.",
       it="Chiudo il diario. Mi tremano le mani. La nonna sapeva di Konrad. Sapeva tutto.")

    _t(tr, F, "narration_plan",
       en="What else did she write? Three components for the seal. Hilde knows the chant. The sign of the earth — perhaps in the church? And the anchor...",
       fr="Qu'a-t-elle écrit d'autre ? Trois composants pour le sceau. Hilde connaît le chant. Le signe de là terre — peut-être dans l'église ? Et l'ancre...",
       es="¿Qué más escribió? Tres componentes para el sello. Hilde conoce el canto. El signo de la tierra — ¿quizás en la iglesia? Y el ancla...",
       it="Cos'altro ha scritto? Tre componenti per il sigillo. Hilde conosce il canto. Il segno della terrà — forse nella chiesa? È l'ancora...")

    _tc(tr, F, "choice_next_step",
        en_choices=["Go to the church — search for the sign", "Seek out Hilde — ask about the chant"],
        fr_choices=["Aller à l'église — chercher le signe", "Aller voir Hilde — l'interroger sur le chant"],
        es_choices=["Ir a la iglesia — buscar el signo", "Buscar a Hilde — preguntar por el canto"],
        it_choices=["Andare alla chiesa — cercare il segno", "Cercare Hilde — chiedere del canto"])

    _t(tr, F, "narration_to_church",
       en="The church. That's where the chamber lies, where the rituals are performed. If there are clues to the sign of the earth anywhere, it's there.",
       fr="L'église. C'est là que se trouve là chambre, là que les rituels sont accomplis. S'il y à des indices sur le signe de là terre quelque part, c'est là-bas.",
       es="La iglesia. Allí se encuentra la cámara, allí se realizan los rituales. Si hay pistas sobre el signo de la tierra en algún lugar, es allí.",
       it="La chiesa. È lì che si trova la camera, lì che vengono celebrati i rituali. Se da qualche parte ci sono indizi sul segno della terra, è là.")

    _t(tr, F, "narration_to_hilde",
       en="Hilde was grandmother's ally. She knows the chant. Perhaps she knows more about the other components too. The church can wait.",
       fr="Hilde était l'alliée de grand-mère. Elle connaît le chant. Peut-être en sait-elle davantage sur les autres composants. L'église peut attendre.",
       es="Hilde era la aliada de la abuela. Conoce el canto. Quizás también sepa más sobre los otros componentes. La iglesia puede esperar.",
       it="Hilde era l'alleata della nonna. Conosce il canto. Forse sa anche di più sugli altri componenti. La chiesa può aspettare.")

    # --- Additional translations (auto-generated) ---
    _t(tr, F, "elise_wakes",
       en="At some point during the night, the singing grew louder. It formed words that I almost understood in my half-sleep. Now, in the morning light, they have vanished again - like fragments of dreams you cannot hold on to.",
       fr="A un moment de la nuit, le chant est devenu plus fort. Il formait des mots que je comprenais presque dans mon demi-sommeil. Maintenant, dans la lumière du matin, ils ont de nouveau disparu - comme des bribes de rêves qu'on ne peut retenir.",
       es="En algun momento de la noche, el canto se hizo mas fuerte. Formaba palabras que casi entendia en mi duermevela. Ahora, a la luz de la mañana, han desaparecido de nuevo - como fragmentos de sueños que no se pueden retener.",
       it="A un certo punto della notte, il canto si e fatto più forte. Formava parole che quasi capivo nel dormiveglia. Ora, nella luce del mattino, sono svanite di nuovo - come frammenti di sogni che non si riescono a trattenere.")

    _t(tr, F, "fled_morning",
       en="The memory of last night burns. The forest that shifted. The paths that all led back. Graubach holds me fast. So I must find another way.",
       fr="Le souvenir de la nuit dernière brule. La forêt qui s'est deplacee. Les chemins qui ramenaient tous en arriere. Graubach me retient. Alors je dois trouver un autre chemin.",
       es="El recuerdo de anoche quema. El bosque que se desplazo. Los caminos que todos llevaban de vuelta. Graubach me retiene. Asi que debo encontrar otro camino.",
       it="Il ricordo di ieri notte brucia. La foresta che si e spostata. I sentieri che riportavano tutti indietro. Graubach mi tiene prigioniera. Quindi devo trovare un'altra via.")

    _t(tr, F, "stayed_morning",
       en="I chose to stay. The key lies on the nightstand, the spiral facing up. In the morning light, it looks harmless. Almost.",
       fr="J'ai choisi de rester. La clé repose sur la table de nuit, la spirale vers le haut. Dans la lumière du matin, elle a l'air inoffensive. Presque.",
       es="Decidi quedarme. La llave esta en la mesita de noche, la espiral hacia arriba. A la luz de la mañana, parece inofensiva. Casi.",
       it="Ho scelto di restare. La chiave e sul comodino, la spirale rivolta verso l'alto. Nella luce del mattino, sembra innocua. Quasi.")

    _t(tr, F, "narration_kitchen",
       en="In the kitchen I find grandmother's teacup. It sits beside the stove, half empty. Dried herbs on the rim. Mugwort and yarrow - the same tea that Hilde gave me.",
       fr="Dans la cuisine, je trouve la tasse de the de grand-mère. Elle est posee a cote du fourneau, a moitie vide. Des herbes séchées sur le bord. De l'armoise et de l'achillee - le même the que Hilde m'a donne.",
       es="En la cocina encuentro la taza de te de la abuela. Esta junto a la estufa, medio vacia. Hierbas secas en el borde. Artemisa y milenrama - el mismo te que Hilde me dio.",
       it="In cucina trovo la tazza di te della nonna. E accanto alla stufa, mezza vuota. Erbe essiccate sul bordo. Artemisia e achillea - lo stesso te che Hilde mi ha dato.")

    _t(tr, F, "elise_cup",
       en="I hold the cup in both hands. It is cold. But for a moment I can feel grandmother's hands that held this cup. Every morning. For thirty years.",
       fr="Je tiens la tasse a deux mains. Elle est froide. Mais pendant un instant, je peux sentir les mains de grand-mère qui tenaient cette tasse. Chaque matin. Pendant trente ans.",
       es="Sostengo la taza con ambas manos. Esta fria. Pero por un momento puedo sentir las manos de la abuela que sostenian esta taza. Cada mañana. Durante treinta años.",
       it="Tengo la tazza con entrambe le mani. E fredda. Ma per un momento posso sentire le mani della nonna che tenevano questa tazza. Ogni mattina. Per trent'anni.")

    _t(tr, F, "elise_morning_resolve",
       en="I put the cup back. Today I search for grandmother's records. Thirty years of research must be somewhere in this house.",
       fr="Je repose la tasse. Aujourd'hui, je cherche les notes de grand-mère. Trente ans de recherches doivent se trouver quelque part dans cette maison.",
       es="Dejo la taza en su sitio. Hoy busco los registros de la abuela. Treinta años de investigacion deben estar en algun lugar de esta casa.",
       it="Rimetto la tazza a posto. Oggi cerco gli appunti della nonna. Trent'anni di ricerche devono essere da qualche parte in questa casa.")

    _t(tr, F, "elise_study_1",
       en="I recognize some of these books from my studies. Grimm's Mythology, Mannhardt's Forest and Field Cults. But others are unfamiliar - handwritten copies, pages in languages I cannot read.",
       fr="Je reconnais certains de ces livres de mes études. La Mythologie de Grimm, les Cultes des forêts et des champs de Mannhardt. Mais d'autres me sont inconnus - des copies manuscrites, des pages dans des langues que je ne sais pas lire.",
       es="Reconozco algunos de estos libros de mis estudios. La Mitologia de Grimm, los Cultos del bosque y del campo de Mannhardt. Pero otros me son desconocidos - copias manuscritas, paginas en idiomas que no puedo leer.",
       it="Riconosco alcuni di questi libri dai miei studi. La Mitologia di Grimm, i Culti del bosco e del campo di Mannhardt. Ma altri mi sono sconosciuti - copie manoscritte, pagine in lingue che non so leggere.")

    _t(tr, F, "elise_study_react",
       en="An anchor. That word again. Konrad used it. Hilde too. And now grandmother. Am I this anchor?",
       fr="Un ancre. Ce mot encore. Konrad l'a utilise. Hilde aussi. Et maintenant grand-mère. Suis-je cette ancre ?",
       es="Un ancla. Esa palabra otra vez. Konrad la uso. Hilde tambien. Y ahora la abuela. Soy YO ese ancla?",
       it="Un'ancora. Quella parola di nuovo. L'ha usata Konrad. Anche Hilde. E ora la nonna. Sono IO quest'ancora?")

    _t(tr, F, "elise_cellar_1",
       en="The stairs creak beneath my feet. It is cold down here, but a different cold than outside. This one comes from below, from the earth itself. As if something beneath it were breathing.",
       fr="L'escalier grince sous mes pieds. Il fait froid ici en bas, mais un froid différent de celui de dehors. Celui-ci vient d'en dessous, de la terre elle-même. Comme si quelque chose respirait en dessous.",
       es="La escalera cruje bajo mis pies. Hace frio aqui abajo, pero un frio diferente al de afuera. Este viene de mas abajo, de la tierra misma. Como si algo debajo estuviera respirando.",
       it="Le scale scricchiolano sotto i miei piedi. Fa freddo quaggiu, ma un freddo diverso da quello fuori. Questo viene dal basso, dalla terra stessa. Come se qualcosa la sotto stesse respirando.")

    _t(tr, F, "elise_cellar_react",
       en="She hid it for me. Not in the obvious study, not in the bedroom. Down here, where the earth is cold and no one searches. As if she knew that others would also be looking for it.",
       fr="Elle l'a cache pour moi. Pas dans le bureau evident, pas dans la chambre. Ici en bas, ou la terre est froide et ou personne ne cherche. Comme si elle savait que d'autres le chercheraient aussi.",
       es="Lo escondio para mi. No en el obvio estudio, no en el dormitorio. Aqui abajo, donde la tierra esta fria y nadie busca. Como si supiera que otros tambien lo buscarian.",
       it="L'ha nascosto per me. Non nello studio, il posto ovvio, non nella camera da letto. Quaggiu, dove la terra e fredda e nessuno cerca. Come se sapesse che anche altri lo avrebbero cercato.")

    _t(tr, F, "elise_bedroom_1",
       en="Her dressing gown still hangs on the hook. I press my face into it. Lavender and herbs. Her scent. For a moment I am six years old again and she is holding me in her arms.",
       fr="Son peignoir est encore accroche au crochet. J'y enfouis mon visage. Lavande et herbes. Son odeur. Pendant un instant, j'ai de nouveau six ans et elle me tient dans ses bras.",
       es="Su bata todavia cuelga del gancho. Hundo mi rostro en ella. Lavanda y hierbas. Su olor. Por un momento vuelvo a tener seis años y ella me tiene en sus brazos.",
       it="La sua vestaglia e ancora appesa al gancio. Vi affondo il viso. Lavanda ed erbe. Il suo profumo. Per un momento ho di nuovo sei anni e lei mi tiene tra le braccia.")

    _t(tr, F, "elise_bedroom_react",
       en="She used the hiding place that only I knew. The place where she used to hide sweets for me. One last message from grandmother to her grandchild.",
       fr="Elle a utilise la cachette que moi seule connaissais. L'endroit ou elle cachait des bonbons pour moi. Un dernier message de grand-mère a sa petite-fille.",
       es="Uso el escondite que solo yo conocia. El lugar donde solia esconder dulces para mi. Un ultimo mensaje de la abuela a su nieta.",
       it="Ha usato il nascondiglio che solo io conoscevo. Il posto dove nascondeva le caramelle per me. Un ultimo messaggio dalla nonna alla sua nipotina.")

    _t(tr, F, "elise_journal_react_1",
       en="The spiral. On the gravestones, on Konrad's hand, in Anna's drawings. Everywhere the same symbol. It is not decoration - it is a signature.",
       fr="La spirale. Sur les pierres tombales, sur la main de Konrad, dans les dessins d'Anna. Partout le même symbole. Ce n'est pas une decoration - c'est une signature.",
       es="La espiral. En las lapidas, en la mano de Konrad, en los dibujos de Anna. En todas partes el mismo simbolo. No es decoracion - es una firma.",
       it="La spirale. Sulle lapidi, sulla mano di Konrad, nei disegni di Anna. Ovunque lo stesso simbolo. Non e decorazione - e una firma.")

    _t(tr, F, "elise_journal_react_2",
       en="A chant that silences the creature? That is one of the three components. Hilde still knows it - she must teach it to me.",
       fr="Un chant qui fait taire la creature ? C'est l'une des trois composantes. Hilde le connaît encore - elle doit me l'enseigner.",
       es="Un canto que silencia a la criatura? Es uno de los tres componentes. Hilde todavia lo conoce - debe ensenarmelo.",
       it="Un canto che fa tacere la creatura? E una delle tre componenti. Hilde lo conosce ancora - deve insegnarmelo.")

    _t(tr, F, "elise_journal_react_3",
       en="Konrad. She knew as early as 1921. For two years he stood at my door and smiled, and behind that smile lives something that is not him. And yesterday I spoke with him as if everything were normal.",
       fr="Konrad. Elle le savait déjà en 1921. Pendant deux ans, il s'est tenu devant ma porte et a souri, et derrière ce sourire vit quelque chose qui n'est pas lui. Et hier, je lui ai parle comme si tout était normal.",
       es="Konrad. Ella lo sabia ya en 1921. Durante dos años estuvo frente a mi puerta y sonrio, y detras de esa sonrisa vive algo que no es el. Y ayer hable con el como si todo fuera normal.",
       it="Konrad. Lo sapeva già nel 1921. Per due anni e stato davanti alla mia porta e ha sorriso, e dietro quel sorriso vive qualcosa che non e lui. E ieri gli ho parlato come se tutto fosse normale.")

    _t(tr, F, "read_journal_6",
       en="'1923: I found the name. In the book in the chamber. Elise Margarethe Brandt. Written in an ink that pulses. My granddaughter. Who is not even born yet.'",
       fr="'1923 : J'ai trouve le nom. Dans le livre de la chambre. Elise Margarethe Brandt. Ecrit dans une encre qui pulse. Ma petite-fille. Qui n'est même pas encore nee.'",
       es="'1923: Encontre el nombre. En el libro de la camara. Elise Margarethe Brandt. Escrito en una tinta que pulsa. Mi nieta. Que aun no ha nacido.'",
       it="'1923: Ho trovato il nome. Nel libro della camera. Elise Margarethe Brandt. Scritto in un inchiostro che pulsa. Mia nipote. Che non e ancora nata.'")

    _t(tr, F, "elise_journal_react_4",
       en="1923. My name was in that book before I was born. The creature knew me before I existed. It was waiting for ME.",
       fr="1923. Mon nom était dans ce livre avant ma naissance. La creature me connaissait avant que j'existe. Elle m'ATTENDAIT.",
       es="1923. Mi nombre estaba en ese libro antes de que yo naciera. La criatura me conocia antes de que existiera. Me estaba esperando a MI.",
       it="1923. Il mio nome era in quel libro prima che io nascessi. La creatura mi conosceva prima che esistessi. Stava aspettando ME.")

    _t(tr, F, "elise_journal_react_5",
       en="My hands tremble so badly that I can barely hold the journal. I set it down. Breathe. One. Two. Three. Then I pick it up again.",
       fr="Mes mains tremblent tellement que je peux a peine tenir le journal. Je le pose. Respire. Un. Deux. Trois. Puis je le reprends.",
       es="Mis manos tiemblan tanto que apenas puedo sostener el diario. Lo dejo. Respiro. Uno. Dos. Tres. Luego lo recojo de nuevo.",
       it="Le mie mani tremano così forte che riesco a malapena a tenere il diario. Lo appoggio. Respiro. Uno. Due. Tre. Poi lo riprendo.")

    _t(tr, F, "read_journal_7",
       en="'1923, Addendum: I will not allow my granddaughter to become a sacrifice. From today I work on another way. It will take thirty years. But I have thirty years.'",
       fr="'1923, Post-scriptum : Je ne permettrai pas que ma petite-fille devienne un sacrifice. A partir d'aujourd'hui, je travaille a une autre voie. Cela prendra trente ans. Mais j'ai trente ans.'",
       es="'1923, Posdata: No permitire que mi nieta se convierta en un sacrificio. A partir de hoy trabajo en otro camino. Llevara treinta años. Pero tengo treinta años.'",
       it="'1923, Nota aggiuntiva: Non permettero che mia nipote diventi un sacrificio. Da oggi lavoro a un'altra via. Ci vorranno trent'anni. Ma ho trent'anni.'")

    _t(tr, F, "elise_journal_react_6",
       en="She did it for me. Not out of duty or tradition. Because she loved me. A grandmother who fought against an ancient being for thirty years so that her grandchild could live.",
       fr="Elle l'a fait pour moi. Pas par devoir ni par tradition. Parce qu'elle m'aimait. Une grand-mère qui a lutte contre un être ancien pendant trente ans pour que sa petite-fille puisse vivre.",
       es="Lo hizo por mi. No por deber ni por tradicion. Porque me amaba. Una abuela que lucho contra un ser ancestral durante treinta años para que su nieta pudiera vivir.",
       it="L'ha fatto per me. Non per dovere o tradizione. Perché mi amava. Una nonna che ha lottato contro un essere ancestrale per trent'anni affinche la sua nipote potesse vivere.")

    _t(tr, F, "elise_plan_1",
       en="Three components. The sign of the earth - perhaps in the chamber beneath the church. The chant of the ancients - Hilde knows it. And an anchor.",
       fr="Trois composantes. Le signe de la terre - peut-être dans la chambre sous l'église. Le chant des anciens - Hilde le connaît. Et un ancre.",
       es="Tres componentes. El signo de la tierra - quiza en la camara bajo la iglesia. El canto de los antiguos - Hilde lo conoce. Y un ancla.",
       it="Tre componenti. Il segno della terra - forse nella camera sotto la chiesa. Il canto degli antichi - Hilde lo conosce. E un'ancora.")

    _t(tr, F, "elise_plan_2",
       en="I am the anchor. My name in the book is the connection. Grandmother did not want to destroy this connection - she wanted to USE it. Not as a sacrifice, but as a link.",
       fr="Je suis l'ancre. Mon nom dans le livre est le lien. Grand-mère ne voulait pas detruire cette connexion - elle voulait l'UTILISER. Non comme sacrifice, mais comme lien.",
       es="Yo soy el ancla. Mi nombre en el libro es la conexion. La abuela no queria destruir esta conexion - queria USARLA. No como sacrificio, sino como vinculo.",
       it="Io sono l'ancora. Il mio nome nel libro e il legame. La nonna non voleva distruggere questa connessione - voleva USARLA. Non come sacrificio, ma come tramite.")

    _t(tr, F, "elise_plan_3",
       en="Can this work? Or was grandmother just as desperate as I am, grasping at any straw?",
       fr="Est-ce que ça peut fonctionner ? Ou est-ce que grand-mère était aussi désespérée que moi, se raccrochant a n'importe quelle branche ?",
       es="Puede funcionar esto? O la abuela estaba tan desesperada como yo, aferrandose a cualquier esperanza?",
       it="Puo funzionare? O la nonna era disperata quanto me, aggrappandosi a qualsiasi appiglio?")


def _add_act2_church_secrets(tr):
    F = "res://data/dialogue/act2/church_secrets.json"

    _t(tr, F, "narration_1",
       en="Graubach's church is no less menacing in daylight. The bell tower juts into the grey sky like an admonishing finger.",
       fr="L'église de Graubach n'est pas moins menaçante en plein jour. Le clocher se dresse dans le ciel gris comme un doigt accusateur.",
       es="La iglesia de Graubach no resulta menos amenazante a la luz del día. El campanario se alza hacia el cielo gris como un dedo admonitorio.",
       it="La chiesa di Graubach non è meno minacciosa alla luce del giorno. Il campanile si staglia nel cielo grigio come un dito ammonitore.")

    _t(tr, F, "narration_2",
       en="I push open the heavy oak door. It yields with a groan that sounds like a sigh.",
       fr="Je pousse là lourde porte de chêne. Elle cède avec un grincement qui ressemble à un soupir.",
       es="Empujo la pesada puerta de roble. Cede con un quejido que suena como un suspiro.",
       it="Spingo la pesante porta di quercia. Cede con un gemito che sembra un sospiro.")

    _t(tr, F, "narration_3",
       en="Inside, it is cold. Colder than outside. The stained glass windows cast pale patterns on the stone floor, but the colors look wrong, shifted.",
       fr="À l'intérieur, il fait froid. Plus froid que dehors. Les vitraux projettent des motifs blafards sur le sol de pierre, mais les couleurs semblent fausses, décalées.",
       es="Dentro hace frío. Más frío que afuera. Las vidrieras arrojan pálidos dibujos sobre el suelo de piedra, pero los colores parecen erróneos, desplazados.",
       it="All'interno fa freddo. Più freddo che fuori. Le vetrate proiettano motivi pallidi sul pavimento di pietra, ma i colori appaiono sbagliati, alterati.")

    _t(tr, F, "narration_4",
       en="I search the chancel. Beneath a faded tapestry, I find a stone slab with carved symbols. Spirals, intertwined.",
       fr="Je fouille le chœur. Sous une tapisserie défraîchie, je trouve une dalle de pierre avec des symboles gravés. Des spirales, entrelacées.",
       es="Registro el presbiterio. Bajo un tapiz descolorido, encuentro una losa de piedra con símbolos tallados. Espirales, entrelazadas.",
       it="Perlusto il presbiterio. Sotto un arazzo sbiadito, trovo una lastra di pietra con simboli incisi. Spirali, intrecciate.")

    _t(tr, F, "narration_5",
       en="When I touch the spirals, I feel a vibration beneath my fingertips. Not mechanical — organic. Like a heartbeat, deep beneath the stone.",
       fr="Quand je touche les spirales, je sens une vibration sous mes doigts. Pas mécanique — organique. Comme un battement de cœur, profond sous là pierre.",
       es="Al tocar las espirales, siento una vibración bajo las yemas de mis dedos. No mecánica — orgánica. Como un latido, profundo bajo la piedra.",
       it="Quando tocco le spirali, sento una vibrazione sotto la punta delle dita. Non meccanica — organica. Come un battito cardiaco, in profondità sotto la pietra.")

    _t(tr, F, "voss_appears",
       en="A voice behind me. 'I wouldn't touch that if I were you.'",
       fr="Une voix derrière moi. « Je ne toucherais pas à ça, si j'étais vous. »",
       es="Una voz a mis espaldas. «Yo no tocaría eso, si fuera usted.»",
       it="Una voce alle mie spalle. 'Non lo toccherebbe, se fossi in lei.'")

    _t(tr, F, "voss_1",
       en="Fräulein Brandt. I saw you coming. This church... it is not what it seems.",
       fr="Fräulein Brandt. Je vous ai vue arriver. Cette église... elle n'est pas ce qu'elle paraît.",
       es="Fräulein Brandt. La vi llegar. Esta iglesia... no es lo que parece.",
       it="Fräulein Brandt. L'ho vista arrivare. Questa chiesa... non è ciò che sembra.")

    _t(tr, F, "voss_smells_herbs",
       en="You've been to see Hilde. I can smell her herbs. Good. Then you already know there is more here than prayers and incense.",
       fr="Vous êtes allée voir Hilde. Je sens ses herbes. Bien. Alors vous savez déjà qu'il y à ici plus que des prières et de l'encens.",
       es="Ha estado con Hilde. Puedo oler sus hierbas. Bien. Entonces ya sabe que aquí hay más que oraciones e incienso.",
       it="È stata da Hilde. Sento l'odore delle sue erbe. Bene. Allora sa già che qui c'è ben altro che preghiere è incenso.")

    _t(tr, F, "voss_3",
       en="Thirty years I have been pastor here. Thirty years I have stood on this ground, preaching of one God, while something else lurks beneath my feet.",
       fr="Voilà trente ans que je suis pasteur ici. Trente ans que je me tiens sur ce sol à prêcher un Dieu, tandis que quelque chose d'autre se tapit sous mes pieds.",
       es="Treinta años llevo siendo párroco aquí. Treinta años parado sobre este suelo, predicando sobre un Dios, mientras algo más acecha bajo mis pies.",
       it="Trent'anni che sono pastore qui. Trent'anni che sto su questo suolo a predicare di un Dio, mentre qualcos'altro si annida sotto i miei piedi.")

    _tc(tr, F, "choice_voss",
        en_choices=["Confront him directly: What do you know about the feeding?", "Ask cautiously: What can you tell me about this church's history?", "Lie: I'm just looking for a quiet place to pray."],
        fr_choices=["Le confronter directement : Que savez-vous sur le nourrissage ?", "Demander prudemment : Que pouvez-vous me dire sur l'histoire de cette église ?", "Mentir : Je cherche simplement un endroit tranquille pour prier."],
        es_choices=["Confrontarlo directamente: ¿Qué sabe usted sobre la alimentación?", "Preguntar con cautela: ¿Qué puede contarme sobre la historia de esta iglesia?", "Mentir: Solo busco un lugar tranquilo para rezar."],
        it_choices=["Affrontarlo direttamente: Cosa sa del nutrimento?", "Chiedere con cautela: Cosa può dirmi sulla storia di questa chiesa?", "Mentire: Cerco solo un posto tranquillo per pregare."])

    _t(tr, F, "voss_confronted_1",
       en="He flinches as though I've struck him. Then he sags, bracing himself against a pew.",
       fr="Il tressaille comme si je l'avais frappé. Puis il s'affaisse, s'appuyant contre un banc d'église.",
       es="Se estremece como si lo hubiera golpeado. Luego se desploma, apoyándose en un banco de la iglesia.",
       it="Sussulta come se lo avessi colpito. Poi si accascia, aggrappandosi a un banco della chiesa.")

    _t(tr, F, "voss_confronted_2",
       en="So you know. Georg has spoken. Good. Good that someone says it aloud.",
       fr="Alors vous savez. Georg à parlé. Bien. C'est bien que quelqu'un le dise à voix haute.",
       es="Así que lo sabe. Georg ha hablado. Bien. Bien que alguien lo diga en voz alta.",
       it="Quindi lo sa. Georg ha parlato. Bene. Bene che qualcuno lo dica ad alta voce.")

    _t(tr, F, "voss_confronted_3",
       en="I saw it in 1893. I was twenty-five. They took Friedrich Meier down there. I heard his screams — and then... then they stopped. And the singing began.",
       fr="Je l'ai vu en 1893. J'avais vingt-cinq ans. Ils ont emmené Friedrich Meier là-dessous. J'ai entendu ses cris — et puis... puis ils ont cessé. Et le chant à commencé.",
       es="Lo vi en 1893. Tenía veinticinco años. Llevaron a Friedrich Meier allá abajo. Oí sus gritos — y luego... luego cesaron. Y el canto comenzó.",
       it="L'ho visto nel 1893. Avevo venticinque anni. Hanno portato Friedrich Meier laggiù. Ho sentito le sue urla — è poi... poi si sono fermate. È il canto è iniziato.")

    _t(tr, F, "voss_confronted_4",
       en="I became a pastor to fight evil. But this thing... it is not the devil, Fräulein Brandt. I would prefer the devil. At least I understand him.",
       fr="Je suis devenu pasteur pour combattre le mal. Mais cette chose... ce n'est pas le diable, Fräulein Brandt. Je préférerais le diable. Au moins, je le comprends.",
       es="Me hice párroco para combatir el mal. Pero esta cosa... no es el diablo, Fräulein Brandt. Preferiría al diablo. Al menos a él lo entiendo.",
       it="Sono diventato pastore per combattere il male. Ma questa cosa... non è il diavolo, Fräulein Brandt. Preferirei il diavolo. Almeno lui lo capisco.")

    _t(tr, F, "voss_careful_1",
       en="The history? This church has stood since 1346. But the cellar... the cellar is older. Much older. The peasants built the church over something that was already there.",
       fr="L'histoire ? Cette église se dresse depuis 1346. Mais là cave... là cave est plus ancienne. Bien plus ancienne. Les paysans ont bâti l'église sur quelque chose qui était déjà là.",
       es="¿La historia? Esta iglesia se alza desde 1346. Pero el sótano... el sótano es más antiguo. Mucho más antiguo. Los campesinos construyeron la iglesia sobre algo que ya estaba allí.",
       it="La storia? Questa chiesa è in piedi dal 1346. Ma la cantina... la cantina è più antica. Molto più antica. I contadini costruirono la chiesa sopra qualcosa che c'era già.")

    _t(tr, F, "voss_careful_2",
       en="There are records. Old chronicles. The first pastor wrote: 'We have set the house of God upon the maw of the demon, that His light may banish the darkness.'",
       fr="Il existe des archives. De vieilles chroniques. Le premier pasteur écrivit : « Nous avons posé là maison de Dieu sur là gueule du démon, afin que Sà lumière bannisse les ténèbres. »",
       es="Hay registros. Viejas crónicas. El primer párroco escribió: «Hemos erigido la casa de Dios sobre las fauces del demonio, para que Su luz destierre las tinieblas.»",
       it="Ci sono documenti. Vecchie cronache. Il primo pastore scrisse: 'Abbiamo posto la casa di Dio sulle fauci del demonio, affinché la Sua luce bandisca le tenebre.'")

    _t(tr, F, "voss_careful_4",
       en="It didn't work. The light banishes nothing. It simply goes on sleeping, no matter what we build over it.",
       fr="Çà n'à pas fonctionné. Là lumière ne bannit rien du tout. Il continue simplement à dormir, quoi que nous bâtissions par-dessus.",
       es="No funcionó. La luz no destierra nada. Simplemente sigue durmiendo, sin importar lo que construyamos encima.",
       it="Non ha funzionato. La luce non bandisce nulla. Continua semplicemente a dormire, qualunque cosa ci costruiamo sopra.")

    _t(tr, F, "voss_lied_1",
       en="Pray. Yes. I pray every day too. But I'm no longer sure anyone is listening.",
       fr="Prier. Oui. Moi aussi, je prie chaque jour. Mais je ne suis plus sûr que quelqu'un écoute.",
       es="Rezar. Sí. Yo también rezo cada día. Pero ya no estoy seguro de que alguien escuche.",
       it="Pregare. Sì. Anch'io prego ogni giorno. Ma non sono più sicuro che qualcuno ascolti.")

    _t(tr, F, "voss_lied_2",
       en="He studies me. In his eyes lies a recognition, as though he knows I am lying.",
       fr="Il me dévisage. Dans ses yeux se lit une lucidité, comme s'il savait que je mens.",
       es="Me escudriña. En sus ojos hay un destello de reconocimiento, como si supiera que estoy mintiendo.",
       it="Mi scruta. Nei suoi occhi c'è un barlume di consapevolezza, come se sapesse che sto mentendo.")

    _t(tr, F, "voss_lied_3",
       en="Your grandmother was often here too. She didn't pray. She... searched. Just like you now, Fräulein Brandt. Just like you.",
       fr="Votre grand-mère venait souvent ici aussi. Elle ne priait pas. Elle... cherchait. Comme vous maintenant, Fräulein Brandt. Exactement comme vous.",
       es="Su abuela también venía aquí a menudo. No rezaba. Ella... buscaba. Como usted ahora, Fräulein Brandt. Exactamente como usted.",
       it="Anche sua nonna veniva spesso qui. Non pregava. Lei... cercava. Come lei adesso, Fräulein Brandt. Proprio come lei.")

    _t(tr, F, "voss_converge_2",
       en="If you truly want to know what lies beneath this church... come tonight. At midnight. I will show you the entrance to the chamber.",
       fr="Si vous voulez vraiment savoir ce qui se cache sous cette église... venez cette nuit. À minuit. Je vous montrerai l'accès à là chambre.",
       es="Si realmente quiere saber qué yace bajo esta iglesia... venga esta noche. A medianoche. Le mostraré el acceso a la cámara.",
       it="Se vuole davvero sapere cosa giace sotto questa chiesa... venga stanotte. A mezzanotte. Le mostrerò l'accesso alla camera.")

    _t(tr, F, "voss_converge_4",
       en="But bring the key. Your key. Without it, the inner door is sealed.",
       fr="Mais apportez là clé. Votre clé. Sans elle, là porte intérieure est scellée.",
       es="Pero traiga la llave. Su llave. Sin ella, la puerta interior está sellada.",
       it="Ma porti la chiave. La sua chiave. Senza di essa, la porta interna è sigillata.")

    _t(tr, F, "journal_church",
       en="The Church",
       fr="L'Église",
       es="La Iglesia",
       it="La Chiesa",
       field="title")

    _t(tr, F, "journal_church",
       en="Found spirals beneath the altar — they vibrate. Pastor Voss knows more than he lets on. He wants to show me the entrance to the chamber at midnight. The church was built over something older.",
       fr="Trouvé des spirales sous l'autel — elles vibrent. Le pasteur Voss en sait plus qu'il ne le dit. Il veut me montrer l'accès à là chambre à minuit. L'église à été bâtie sur quelque chose de plus ancien.",
       es="Encontradas espirales bajo el altar — vibran. El pastor Voss sabe más de lo que aparenta. Quiere mostrarme el acceso a la cámara a medianoche. La iglesia fue construida sobre algo más antiguo.",
       it="Trovate spirali sotto l'altare — vibrano. Il pastore Voss sa più di quanto lasci intendere. Vuole mostrarmi l'accesso alla camera a mezzanotte. La chiesa fu costruita sopra qualcosa di più antico.",
       field="content")

    _t(tr, F, "narration_leave_church",
       en="I leave the church. Outside, the sun is shining, but it feels thin, as though filtered through too much water.",
       fr="Je quitte l'église. Dehors, le soleil brille, mais il semble ténu, comme filtré à travers trop d'eau.",
       es="Salgo de la iglesia. Afuera brilla el sol, pero se siente tenue, como si estuviera filtrado por demasiada agua.",
       it="Esco dalla chiesa. Fuori splende il sole, ma sembra sottile, come se fosse filtrato attraverso troppa acqua.")

    # --- Additional translations (auto-generated) ---
    _t(tr, F, "elise_approach",
       en="Grandmother's journal mentions a chamber beneath the church. Built upon something older, deeper. The key in my pocket feels warm, as if it wanted to go home.",
       fr="Le journal de grand-mère mentionne une chambre sous l'église. Construite sur quelque chose de plus ancien, de plus profond. La clé dans ma poche est chaude, comme si elle voulait rentrer chez elle.",
       es="El diario de la abuela menciona una camara bajo la iglesia. Construida sobre algo mas antiguo, mas profundo. La llave en mi bolsillo se siente calida, como si quisiera volver a casa.",
       it="Il diario della nonna menziona una camera sotto la chiesa. Costruita su qualcosa di più antico, di più profondo. La chiave nella mia tasca e calda, come se volesse tornare a casa.")

    _t(tr, F, "elise_cold",
       en="The cold comes from below. Through the stone floor, through the soles of my shoes, into my bones. The same cold as in grandmother's cellar. The cold of something breathing beneath the earth.",
       fr="Le froid vient d'en bas. A travers le sol de pierre, a travers mes semelles, dans mes os. Le même froid que dans la cave de grand-mère. Le froid de quelque chose qui respire sous la terre.",
       es="El frio viene de abajo. A traves del suelo de piedra, a traves de las suelas de mis zapatos, hasta mis huesos. El mismo frio que en el sotano de la abuela. El frio de algo que respira bajo la tierra.",
       it="Il freddo viene dal basso. Attraverso il pavimento di pietra, attraverso le suole delle mie scarpe, nelle mie ossa. Lo stesso freddo della cantina della nonna. Il freddo di qualcosa che respira sotto terra.")

    _t(tr, F, "elise_spirals_recognize",
       en="These spirals. On the gravestones, on Konrad's hand, in grandmother's journal. Now here, beneath the altar. They all point in the same direction: downward.",
       fr="Ces spirales. Sur les pierres tombales, sur la main de Konrad, dans le journal de grand-mère. Maintenant ici, sous l'autel. Elles pointent toutes dans la même direction : vers le bas.",
       es="Estas espirales. En las lapidas, en la mano de Konrad, en el diario de la abuela. Ahora aqui, bajo el altar. Todas senalan en la misma direccion: hacia abajo.",
       it="Queste spirali. Sulle lapidi, sulla mano di Konrad, nel diario della nonna. Ora qui, sotto l'altare. Tutte indicano la stessa direzione: verso il basso.")

    _t(tr, F, "elise_heartbeat_react",
       en="It's alive. Right beneath me, under stone and earth. I feel it - not just with my fingers, but somewhere deeper, in a part of me that has no words. As if it recognizes me.",
       fr="C'est vivant. Juste en dessous de moi, sous la pierre et la terre. Je le sens - pas seulement avec mes doigts, mais quelque part de plus profond, dans une partie de moi qui n'a pas de mots. Comme s'il me reconnaissait.",
       es="Esta vivo. Justo debajo de mi, bajo piedra y tierra. Lo siento - no solo con los dedos, sino en algun lugar mas profundo, en una parte de mi que no tiene palabras. Como si me reconociera.",
       it="E vivo. Proprio sotto di me, sotto pietra e terra. Lo sento - non solo con le dita, ma da qualche parte più in profondo, in una parte di me che non ha parole. Come se mi riconoscesse.")

    _t(tr, F, "elise_voss_1",
       en="I know that, Pastor Voss. I found grandmother's journal. I know about the chamber. About what sleeps beneath it.",
       fr="Je le sais, pasteur Voss. J'ai trouve le journal de grand-mère. Je sais pour la chambre. Pour ce qui dort en dessous.",
       es="Lo se, pastor Voss. Encontre el diario de la abuela. Se lo de la camara. Lo de aquello que duerme debajo.",
       it="Lo so, pastore Voss. Ho trovato il diario della nonna. So della camera. Di cio che dorme la sotto.")

    _t(tr, F, "elise_voss_thirty",
       en="Thirty years. The same number as the ritual. As grandmother's struggle. Is that coincidence?",
       fr="Trente ans. Le même nombre que le rituel. Que le combat de grand-mère. Est-ce une coincidence ?",
       es="Treinta años. El mismo numero que el ritual. Que la lucha de la abuela. Es coincidencia?",
       it="Trent'anni. Lo stesso numero del rituale. Della lotta della nonna. E una coincidenza?")

    _t(tr, F, "voss_3b",
       en="Nothing in Graubach is coincidence. Thirty years is the cycle. And it is nearing its end.",
       fr="Rien a Graubach n'est une coincidence. Trente ans, c'est le cycle. Et il approche de sa fin.",
       es="Nada en Graubach es coincidencia. Treinta años es el ciclo. Y se acerca a su fin.",
       it="Niente a Graubach e una coincidenza. Trent'anni e il ciclo. E si avvicina alla fine.")

    _t(tr, F, "elise_confront_press",
       en="1893. Friedrich Meier. You were there, weren't you?",
       fr="1893. Friedrich Meier. Vous y etiez, n'est-ce pas ?",
       es="1893. Friedrich Meier. Usted estaba alli, verdad?",
       it="1893. Friedrich Meier. Lei c'era, vero?")

    _t(tr, F, "narration_voss_tears",
       en="His hands are trembling. In his eyes stand tears that are thirty years old.",
       fr="Ses mains tremblent. Dans ses yeux brillent des larmes vieilles de trente ans.",
       es="Sus manos tiemblan. En sus ojos hay lagrimas de treinta años.",
       it="Le sue mani tremano. Nei suoi occhi ci sono lacrime vecchie di trent'anni.")

    _t(tr, F, "elise_confront_comfort",
       en="My grandmother trusted you. She wrote that you were the only one who believed her.",
       fr="Ma grand-mère vous faisait confiance. Elle a écrit que vous etiez le seul a l'avoir crue.",
       es="Mi abuela confiaba en usted. Escribio que usted era el unico que le creyo.",
       it="Mia nonna si fidava di lei. Ha scritto che lei era l'unico che le aveva creduto.")

    _t(tr, F, "voss_confront_react",
       en="Margarethe... yes. She was the only one who understood. We met every month. For thirty years. And now she is dead, and I am alone.",
       fr="Margarethe... oui. Elle était la seule a comprendre. Nous nous retrouvions chaque mois. Pendant trente ans. Et maintenant elle est morte, et je suis seul.",
       es="Margarethe... si. Era la unica que lo entendia. Nos reuniamos cada mes. Durante treinta años. Y ahora esta muerta, y estoy solo.",
       it="Margarethe... si. Era l'unica che capiva. Ci incontravamo ogni mese. Per trent'anni. E adesso e morta, e sono solo.")

    _t(tr, F, "elise_confront_ally",
       en="You are not alone. I am here. And I intend to finish what she started.",
       fr="Vous n'êtes pas seul. Je suis la. Et j'ai l'intention de terminer ce qu'elle a commence.",
       es="No esta solo. Estoy aqui. Y tengo la intencion de terminar lo que ella empezo.",
       it="Non e solo. Sono qui. E intendo portare a termine cio che lei ha iniziato.")

    _t(tr, F, "elise_careful_ask",
       en="Something that was already there? The spirals on the stone slab - they're not Christian. They're pre-Christian. Celtic perhaps, or older.",
       fr="Quelque chose qui était déjà la ? Les spirales sur la dalle de pierre - elles ne sont pas chretiennes. Elles sont prechretiennes. Celtiques peut-être, ou plus anciennes.",
       es="Algo que ya estaba alli? Las espirales en la losa de piedra - no son cristianas. Son precristianas. Celtas quiza, o mas antiguas.",
       it="Qualcosa che c'era già? Le spirali sulla lastra di pietra - non sono cristiane. Sono precristiane. Celtiche forse, o più antiche.")

    _t(tr, F, "elise_careful_react",
       en="Because it is not a demon. It is older than your religion, Pastor Voss. Older than all religions. My grandmother understood that.",
       fr="Parce que ce n'est pas un demon. C'est plus ancien que votre religion, pasteur Voss. Plus ancien que toutes les religions. Ma grand-mère l'avait compris.",
       es="Porque no es un demonio. Es mas antiguo que su religion, pastor Voss. Mas antiguo que todas las religiones. Mi abuela lo entendia.",
       it="Perché non e un demone. E più antico della sua religione, pastore Voss. Piu antico di tutte le religioni. Mia nonna lo aveva capito.")

    _t(tr, F, "elise_lied_caught",
       en="He knows I'm lying. There's no point. In this village full of lies, I am the worst liar.",
       fr="Il sait que je mens. Ça ne sert a rien. Dans ce village plein de mensonges, je suis la pire des menteuses.",
       es="Sabe que miento. No tiene sentido. En este pueblo lleno de mentiras, soy la peor mentirosa.",
       it="Sa che sto mentendo. Non ha senso. In questo villaggio pieno di bugie, sono la peggior bugiarda.")

    _t(tr, F, "elise_midnight_why",
       en="Why at night? Why not now?",
       fr="Pourquoi la nuit ? Pourquoi pas maintenant ?",
       es="Por que de noche? Por que no ahora?",
       it="Perché di notte? Perché non adesso?")

    _t(tr, F, "voss_converge_2b",
       en="Because Otto has the church watched during the day. The mayor has eyes everywhere. At night, the eyes sleep.",
       fr="Parce qu'Otto fait surveiller l'église pendant la journee. Le maire a des yeux partout. La nuit, les yeux dorment.",
       es="Porque Otto hace vigilar la iglesia durante el dia. El alcalde tiene ojos en todas partes. De noche, los ojos duermen.",
       it="Perché Otto fa sorvegliare la chiesa di giorno. Il sindaco ha occhi ovunque. Di notte, gli occhi dormono.")

    _t(tr, F, "elise_key_confirm",
       en="I will be there. With the key.",
       fr="Je serai la. Avec la clé.",
       es="Estare alli. Con la llave.",
       it="Ci saro. Con la chiave.")

    _t(tr, F, "voss_converge_5",
       en="One more thing. When you are down there... the singing will grow louder. It will try to get inside your head. Think of something real. Of someone you love. That helps.",
       fr="Encore une chose. Quand vous serez la-bas... le chant deviendra plus fort. Il essaiera de penetrer dans votre tête. Pensez a quelque chose de reel. A quelqu'un que vous aimez. Ça aide.",
       es="Una cosa mas. Cuando este alli abajo... el canto se hara mas fuerte. Intentara meterse en su cabeza. Piense en algo real. En alguien a quien ame. Eso ayuda.",
       it="Un'altra cosa. Quando sara la sotto... il canto diventera più forte. Cerchera di entrare nella sua testa. Pensi a qualcosa di reale. A qualcuno che ama. Questo aiuta.")

    _t(tr, F, "elise_voss_thanks",
       en="Thank you, Pastor Voss. For the warning. And for standing by my grandmother.",
       fr="Merci, pasteur Voss. Pour l'avertissement. Et pour avoir soutenu ma grand-mère.",
       es="Gracias, pastor Voss. Por la advertencia. Y por haber apoyado a mi abuela.",
       it="Grazie, pastore Voss. Per l'avvertimento. E per essere stato accanto a mia nonna.")

    _t(tr, F, "elise_leave_thought",
       en="Tonight. In a few hours I will go down, to where the singing comes from. To where my name is written in a book older than I am. The thought frightens me. But the fear has grown smaller. Behind it, something else is growing: determination.",
       fr="Ce soir. Dans quelques heures, je descendrai la ou vient le chant. La ou mon nom est écrit dans un livre plus ancien que moi. Cette pensee m'effraie. Mais la peur a diminue. Derriere elle, autre chose grandit : la détermination.",
       es="Esta noche. En pocas horas bajare adonde viene el canto. Adonde mi nombre esta escrito en un libro mas antiguo que yo. El pensamiento me asusta. Pero el miedo se ha hecho mas pequeño. Detras de el crece otra cosa: determinacion.",
       it="Stanotte. Tra poche ore scendero la dove viene il canto. La dove il mio nome e scritto in un libro più antico di me. Il pensiero mi spaventa. Ma la paura si e fatta più piccola. Dietro di essa cresce qualcos'altro: determinazione.")


def _add_act2_konrad_encounter(tr):
    F = "res://data/dialogue/act2/konrad_encounter.json"

    _t(tr, F, "narration_1",
       en="Day four. In the village square, I run into Konrad by chance — or what disguises itself as chance. He sits on the edge of the fountain, reading.",
       fr="Quatrième jour. Sur là place du village, je croise Konrad par hasard — où ce qui se fait passer pour du hasard. Il est assis sur le rebord de là fontaine et lit.",
       es="Cuarto día. En la plaza del pueblo me encuentro con Konrad por casualidad — o lo que se disfraza de casualidad. Está sentado en el borde de la fuente, leyendo.",
       it="Quarto giorno. Nella piazza del paese incontro Konrad per caso — o ciò che si maschera da caso. È seduto sul bordo della fontana, intento a leggere.")

    _t(tr, F, "konrad_1",
       en="Fräulein Brandt! What a pleasant surprise. Please, sit down. I have fresh coffee — real coffee, not that substitute.",
       fr="Fräulein Brandt ! Quelle agréable surprise. Asseyez-vous donc. J'ai du café frais — du vrai, pas cet ersatz.",
       es="¡Fräulein Brandt! Qué agradable sorpresa. Siéntese, por favor. Tengo café recién hecho — de verdad, no ese sucedáneo.",
       it="Fräulein Brandt! Che piacevole sorpresa. Si sieda, prego. Ho del caffè fresco — vero, non quel surrogato.")

    _t(tr, F, "narration_2",
       en="His smile is warm, inviting. But grandmother's words echo: 'His eyes were not his own.'",
       fr="Son sourire est chaleureux, accueillant. Mais les mots de grand-mère résonnent : « Ses yeux n'étaient plus les siens. »",
       es="Su sonrisa es cálida, acogedora. Pero las palabras de la abuela resuenan: «Sus ojos no eran los suyos.»",
       it="Il suo sorriso è caldo, invitante. Ma le parole della nonna riecheggiano: 'I suoi occhi non erano i suoi.'")

    _t(tr, F, "konrad_remembers_door",
       en="Ah, it's nice to see you in daylight. Our nighttime encounter was somewhat... unfortunate. You must think me strange.",
       fr="Ah, c'est agréable de vous voir à là lumière du jour. Notre rencontre nocturne était quelque peu... malencontreuse. Vous devez me trouver étrange.",
       es="Ah, es agradable verla a la luz del día. Nuestro encuentro nocturno fue algo... desafortunado. Debe pensar que soy extraño.",
       it="Ah, è bello vederla alla luce del giorno. Il nostro incontro notturno è stato alquanto... sfortunato. Deve pensare che sono strano.")

    _t(tr, F, "konrad_door_narration",
       en="He mentions our encounter casually, as if it were the most normal thing in the world. But why was he at grandmother's house at night?",
       fr="Il mentionne notre rencontre avec désinvolture, comme si c'était là chose là plus normale du monde. Mais que faisait-il chez grand-mère en pleine nuit ?",
       es="Menciona nuestro encuentro con naturalidad, como si fuera lo más normal del mundo. Pero ¿por qué estaba en casa de la abuela de noche?",
       it="Menziona il nostro incontro con noncuranza, come se fosse la cosa più normale del mondo. Ma perché si trovava a casa della nonna di notte?")

    _t(tr, F, "narration_suspicious",
       en="I know what grandmother wrote about him. The vessel. I must be careful.",
       fr="Je sais ce que grand-mère à écrit sur lui. Le réceptacle. Je dois être prudente.",
       es="Sé lo que la abuela escribió sobre él. El recipiente. Debo tener cuidado.",
       it="So cosa ha scritto la nonna su di lui. Il ricettacolo. Devo stare attenta.")

    _t(tr, F, "narration_charmed",
       en="Something about him draws me in. He is different from the other villagers — educated, open, curious.",
       fr="Quelque chose en lui m'attire. Il est différent des autres villageois — cultivé, ouvert, curieux.",
       es="Algo en él me atrae. Es diferente de los demás aldeanos — culto, abierto, curioso.",
       it="Qualcosa in lui mi attrae. È diverso dagli altri paesani — colto, aperto, curioso.")

    _t(tr, F, "konrad_2",
       en="I've been thinking about your grandmother. Margarethe was a remarkable woman. Did you know she taught me to read?",
       fr="J'ai pensé à votre grand-mère. Margarethe était une femme remarquable. Saviez-vous que c'est elle qui m'à appris à lire ?",
       es="He estado pensando en su abuela. Margarethe era una mujer extraordinaria. ¿Sabía que ella me enseñó a leer?",
       it="Ho pensato a sua nonna. Margarethe era una donna straordinaria. Sapeva che è stata lei a insegnarmi a leggere?")

    _t(tr, F, "konrad_4",
       en="When I was a child, she came every Wednesday. She read to me, showed me a world beyond these mountains. Without her, I would never have become a teacher.",
       fr="Quand j'étais enfant, elle venait chaque mercredi. Elle me lisait des histoires, me montrait un monde au-delà de ces montagnes. Sans elle, je ne serais jamais devenu instituteur.",
       es="Cuando yo era niño, venía cada miércoles. Me leía, me mostraba un mundo más allá de estas montañas. Sin ella, nunca me habría convertido en maestro.",
       it="Quand'ero bambino, veniva ogni mercoledì. Mi leggeva, mi mostrava un mondo oltre queste montagne. Senza di lei, non sarei mai diventato insegnante.")

    _t(tr, F, "konrad_6",
       en="She always had a secret, your grandmother. Something she never shared. Have you discovered it?",
       fr="Elle avait toujours un secret, votre grand-mère. Quelque chose qu'elle ne partageait jamais. L'avez-vous découvert ?",
       es="Siempre tuvo un secreto, su abuela. Algo que nunca compartió. ¿Lo ha descubierto?",
       it="Aveva sempre un segreto, sua nonna. Qualcosa che non condivideva mai. L'ha scoperto?")

    _tc(tr, F, "choice_konrad_trust",
        en_choices=["Trust him and tell him about the tradition", "Distrust: Answer evasively", "Test him: Tell him about the spirals and observe his reaction"],
        fr_choices=["Lui faire confiance et lui parler de la tradition", "Se méfier : Répondre évasivement", "Le tester : Lui parler des spirales et observer sa réaction"],
        es_choices=["Confiar en él y contarle sobre la tradición", "Desconfiar: Responder con evasivas", "Ponerlo a prueba: Contarle de las espirales y observar su reacción"],
        it_choices=["Fidarsi di lui e raccontargli della tradizione", "Diffidare: Rispondere in modo evasivo", "Metterlo alla prova: Parlargli delle spirali e osservare la sua reazione"])

    _t(tr, F, "konrad_trusted",
       en="I tell him everything. About the tradition, the book, the feeding. He listens without interrupting.",
       fr="Je lui raconte tout. Là tradition, le livre, le nourrissage. Il écoute sans m'interrompre.",
       es="Se lo cuento todo. La tradición, el libro, la alimentación. Escucha sin interrumpir.",
       it="Gli racconto tutto. Della tradizione, del libro, del nutrimento. Ascolta senza interrompere.")

    _t(tr, F, "konrad_trusted_3",
       en="I know. I think I've always known. Not the details, but... the feeling. That something is wrong in this village. That something is wrong with me.",
       fr="Je le sais. Je crois que je l'ai toujours su. Pas les détails, mais... le sentiment. Que quelque chose ne và pas dans ce village. Que quelque chose ne và pas chez moi.",
       es="Lo sé. Creo que siempre lo he sabido. No los detalles, pero... la sensación. De que algo no está bien en este pueblo. De que algo no está bien conmigo.",
       it="Lo so. Credo di averlo sempre saputo. Non i dettagli, ma... la sensazione. Che qualcosa non va in questo villaggio. Che qualcosa non va in me.")

    _t(tr, F, "konrad_trusted_5",
       en="Sometimes I dream things that are not my dreams. I see... deeper. Older. As though I were merely a shell.",
       fr="Parfois je rêve de choses qui ne sont pas mes rêves. Je vois... plus profond. Plus ancien. Comme si je n'étais qu'une coquille.",
       es="A veces sueño cosas que no son mis sueños. Veo... más profundo. Más antiguo. Como si yo fuera solo una cáscara.",
       it="A volte sogno cose che non sono i miei sogni. Vedo... più in profondità. Più in là nel tempo. Come se fossi solo un involucro.")

    _t(tr, F, "konrad_trusted_6",
       en="He says it so calmly, so matter-of-factly. As though he were talking about the weather.",
       fr="Il le dit si calmement, si posément. Comme s'il parlait de là météo.",
       es="Lo dice con tanta calma, con tanta naturalidad. Como si hablara del tiempo.",
       it="Lo dice con tanta calma, con tanta naturalezza. Come se parlasse del tempo.")

    _t(tr, F, "konrad_distrusted",
       en="'Nothing special,' I say. 'Old letters, recipes, memories.' The lie tastes bitter.",
       fr="« Rien de particulier », dis-je. « De vieilles lettres, des recettes, des souvenirs. » Le mensonge à un goût amer.",
       es="«Nada especial», digo. «Viejas cartas, recetas, recuerdos.» La mentira sabe amarga.",
       it="'Niente di speciale,' dico. 'Vecchie lettere, ricette, ricordi.' La bugia ha un sapore amaro.")

    _t(tr, F, "konrad_distrusted_3",
       en="He smiles, but the smile doesn't reach his eyes. For a moment — just a moment — something seems to slide behind his pupils. Something ancient.",
       fr="Il sourit, mais le sourire n'atteint pas ses yeux. Pendant un instant — un seul instant — quelque chose semble glisser derrière ses pupilles. Quelque chose d'ancien.",
       es="Sonríe, pero la sonrisa no le llega a los ojos. Por un instante — solo un instante — algo parece deslizarse tras sus pupilas. Algo antiguo.",
       it="Sorride, ma il sorriso non raggiunge i suoi occhi. Per un istante — solo un istante — qualcosa sembra scivolare dietro le sue pupille. Qualcosa di antico.")

    _t(tr, F, "konrad_distrusted_4",
       en="Of course. Only memories. After all, Graubach is a perfectly normal village.",
       fr="Bien sûr. Que des souvenirs. Après tout, Graubach est un village tout à fait normal.",
       es="Por supuesto. Solo recuerdos. Al fin y al cabo, Graubach es un pueblo completamente normal.",
       it="Naturalmente. Solo ricordi. Dopotutto, Graubach è un villaggio del tutto normale.")

    _t(tr, F, "konrad_tested",
       en="I mention the spirals in the church in passing. 'Strange patterns,' I say. 'Do you know them?'",
       fr="Je mentionne les spirales de l'église en passant. « D'étranges motifs », dis-je. « Vous les connaissez ? »",
       es="Menciono las espirales de la iglesia de pasada. «Patrones extraños», digo. «¿Los conoce?»",
       it="Accenno di sfuggita alle spirali nella chiesa. 'Strani disegni,' dico. 'Li conosce?'")

    _t(tr, F, "konrad_tested_2",
       en="His hand twitches. Involuntarily, he grasps his wrist — right where I noticed the faint spiral patterns on his skin the other day.",
       fr="Sà main tressaille. Involontairement, il saisit son poignet — là même où j'avais remarqué les motifs en spirale sur sà peau l'autre jour.",
       es="Su mano se estremece. Involuntariamente, se agarra la muñeca — justo donde noté los tenues patrones en espiral en su piel el otro día.",
       it="La sua mano sussulta. Involontariamente, si afferra il polso — proprio dove l'altro giorno avevo notato i deboli disegni a spirale sulla sua pelle.")

    _t(tr, F, "konrad_tested_4",
       en="Spirals? No, I... I don't know any spirals.",
       fr="Des spirales ? Non, je... je ne connais aucune spirale.",
       es="¿Espirales? No, yo... no conozco ninguna espiral.",
       it="Spirali? No, io... non conosco nessuna spirale.")

    _t(tr, F, "konrad_tested_5",
       en="He's lying. And he knows that I know it. The air between us grows heavy.",
       fr="Il ment. Et il sait que je le sais. L'air entre nous s'alourdit.",
       es="Miente. Y sabe que yo lo sé. El aire entre nosotros se vuelve pesado.",
       it="Sta mentendo. È sa che io lo so. L'aria tra noi si fa pesante.")

    _t(tr, F, "konrad_walk",
       en="Come. Let me show you something. The forest behind the school — there is a place there that your grandmother loved.",
       fr="Venez. Laissez-moi vous montrer quelque chose. Là forêt derrière l'école — il y à là-bas un endroit que votre grand-mère aimait.",
       es="Venga. Déjeme enseñarle algo. El bosque detrás de la escuela — hay un lugar allí que su abuela adoraba.",
       it="Venga. Le voglio mostrare qualcosa. Il bosco dietro la scuola — c'è un posto che sua nonna amava.")

    _t(tr, F, "narration_forest_1",
       en="The forest path leads deeper than expected. The trees stand so close together here that barely any light gets through. Konrad walks ahead, sure-footed, as though he knows every root.",
       fr="Le sentier forestier s'enfonce plus loin que prévu. Les arbres sont si serrés ici que là lumière y pénètre à peine. Konrad marche devant, le pas assuré, comme s'il connaissait chaque racine.",
       es="El sendero del bosque se adentra más de lo esperado. Los árboles están tan apretados aquí que apenas pasa la luz. Konrad camina delante, con paso seguro, como si conociera cada raíz.",
       it="Il sentiero nel bosco si addentra più del previsto. Gli alberi qui sono così fitti che a malapena filtra la luce. Konrad cammina avanti, sicuro, come se conoscesse ogni radice.")

    _t(tr, F, "narration_forest_2",
       en="He stops at a clearing. In its center stands a single, ancient tree. Its trunk is twisted, grown in a spiral.",
       fr="Il s'arrête à une clairière. En son centre se dresse un arbre solitaire et très ancien. Son tronc est tordu, poussé en spirale.",
       es="Se detiene en un claro. En su centro se alza un único árbol antiquísimo. Su tronco está retorcido, crecido en espiral.",
       it="Si ferma in una radura. Al centro si erge un unico albero antichissimo. Il suo tronco è contorto, cresciuto a spirale.")

    _t(tr, F, "konrad_tree_1",
       en="The villagers call it the Guardian Tree. It has stood here for centuries. Your grandmother came here often.",
       fr="Les villageois l'appellent l'Arbre Gardien. Il se dresse ici depuis des siècles. Votre grand-mère venait souvent ici.",
       es="Los aldeanos lo llaman el Árbol Guardián. Lleva aquí siglos. Su abuela venía aquí a menudo.",
       it="I paesani lo chiamano l'Albero Guardiano. È qui da secoli. Sua nonna veniva qui spesso.")

    _t(tr, F, "konrad_tree_3",
       en="Do you feel it? The ground here... it breathes.",
       fr="Vous le sentez ? Le sol ici... il respire.",
       es="¿Lo siente? El suelo aquí... respira.",
       it="Lo sente? Il terreno qui... respira.")

    _t(tr, F, "narration_tree",
       en="He's right. Beneath my feet, there is a faint pulsing. Like a heartbeat, deep in the earth. The same rhythm as beneath the altar.",
       fr="Il à raison. Sous mes pieds, il y à une faible pulsation. Comme un battement de cœur, profond dans là terre. Le même rythme que sous l'autel.",
       es="Tiene razón. Bajo mis pies hay una leve pulsación. Como un latido, profundo en la tierra. El mismo ritmo que bajo el altar.",
       it="Ha ragione. Sotto i miei piedi c'è un debole pulsare. Come un battito cardiaco, in profondità nella terra. Lo stesso ritmo di sotto l'altare.")

    _t(tr, F, "journal_konrad",
       en="Konrad and the Guardian Tree",
       fr="Konrad et l'Arbre Gardien",
       es="Konrad y el Árbol Guardián",
       it="Konrad è l'Albero Guardiano",
       field="title")

    _t(tr, F, "journal_konrad",
       en="Konrad showed me the Guardian Tree in the forest — grown in a spiral. The ground there pulses like beneath the altar. Konrad behaved strangely — his hand twitches at the mention of spirals, his eyes change. Grandmother's journal confirmed it: He is the vessel.",
       fr="Konrad m'à montré l'Arbre Gardien dans là forêt — poussé en spirale. Le sol y pulse comme sous l'autel. Konrad s'est comporté étrangement — sà main tressaille à là mention des spirales, ses yeux changent. Le journal de grand-mère l'à confirmé : il est le réceptacle.",
       es="Konrad me mostró el Árbol Guardián en el bosque — crecido en espiral. El suelo allí pulsa como bajo el altar. Konrad se comportó de forma extraña — su mano se estremece ante la mención de las espirales, sus ojos cambian. El diario de la abuela lo confirmó: él es el recipiente.",
       it="Konrad mi ha mostrato l'Albero Guardiano nel bosco — cresciuto a spirale. Il terreno lì pulsa come sotto l'altare. Konrad si è comportato in modo strano — la sua mano sussulta alla menzione delle spirali, i suoi occhi cambiano. Il diario della nonna lo ha confermato: lui è il ricettacolo.",
       field="content")

    _t(tr, F, "narration_return",
       en="We walk back to the village in silence. Konrad whistles softly to himself. The melody sounds familiar — it is the singing from the depths.",
       fr="Nous retournons au village en silence. Konrad siffle doucement. Là mélodie me semble familière — c'est le chant des profondeurs.",
       es="Regresamos al pueblo en silencio. Konrad silba suavemente para sí. La melodía me resulta familiar — es el canto de las profundidades.",
       it="Torniamo al villaggio in silenzio. Konrad fischietta sommessamente tra sé. La melodia mi suona familiare — è il canto delle profondità.")
    # --- Missing Elise dialogue and narration nodes ---
    _t(tr, F, "narration_inner",
       en="Grandmother's words stand before my eyes: 'He is the vessel.' The man who sits there so peacefully reading carries something ancient within him. And he may not even know it.",
       fr="Les mots de grand-mère me hantent : « Il est le réceptacle. » L'homme qui est assis là si paisiblement à lire porte quelque chose d'ancien en lui. Et il ne le sait peut-être même pas.",
       es="Las palabras de la abuela me persiguen: «Él es el recipiente.» El hombre que está sentado ahí tan pacíficamente leyendo lleva algo antiguo dentro. Y quizás ni siquiera lo sabe.",
       it="Le parole della nonna mi stanno davanti agli occhi: 'Lui è il ricettacolo.' L'uomo che siede lì così pacificamente a leggere porta qualcosa di antico dentro di sé. È forse non lo sa nemmeno.")
    _t(tr, F, "elise_greet",
       en="Good day, Herr Müller. My grandmother often told me about you.",
       fr="Bonjour, Herr Müller. Mà grand-mère m'à souvent parlé de vous.",
       es="Buenos días, Herr Müller. Mi abuela me habló a menudo de usted.",
       it="Buongiorno, Herr Müller. Mia nonna mi parlava spesso di Lei.")
    _t(tr, F, "konrad_react_greet",
       en="Did she? That pleases me. Margarethe was a special woman.",
       fr="Vraiment ? Celà me fait plaisir. Margarethe était une femme spéciale.",
       es="¿De verdad? Me alegra. Margarethe era una mujer especial.",
       it="Davvero? Mi fa piacere. Margarethe era una donna speciale.")
    _t(tr, F, "elise_door_react",
       en="Yes, it surprised me. What brought you to Grandmother's house at night?",
       fr="Oui, çà m'à surprise. Qu'est-ce qui vous à amené chez grand-mère en pleine nuit ?",
       es="Sí, me sorprendió. ¿Qué le llevó a la casa de la abuela de noche?",
       it="Sì, mi ha sorpresa. Cosa L'ha portata a casa della nonna di notte?")
    _t(tr, F, "konrad_door_excuse",
       en="I wanted to offer my condolences. Old habit — Margarethe and I often chatted in the evenings.",
       fr="Je voulais présenter mes condoléances. Vieille habitude — Margarethe et moi bavardions souvent le soir.",
       es="Quería dar mis condolencias. Vieja costumbre — Margarethe y yo solíamos charlar por las tardes.",
       it="Volevo porgere le mie condoglianze. Vecchia abitudine — Margarethe è io chiacchieravamo spesso di sera.")
    _t(tr, F, "narration_door",
       en="He is lying. Or telling a half-truth. Grandmother did not write about evening chats in her diary.",
       fr="Il ment. Ou dit une demi-vérité. Grand-mère n'à pas écrit de bavardages du soir dans son journal.",
       es="Miente. O dice una verdad a medias. La abuela no escribió sobre charlas nocturnas en su diario.",
       it="Mente. O dice una mezza verità. La nonna non ha scritto di chiacchierate serali nel suo diario.")
    _t(tr, F, "elise_react_reading",
       en="I did not know that. She never talked much about Graubach. At least not... not in recent years.",
       fr="Je ne le savais pas. Elle n'à jamais beaucoup parlé de Graubach. Du moins pas... pas ces dernières années.",
       es="No lo sabía. Nunca habló mucho de Graubach. Al menos no... no en los últimos años.",
       it="Non lo sapevo. Non parlava mai molto di Graubach. Almeno non... non negli ultimi anni.")
    _t(tr, F, "elise_personal",
       en="That sounds wonderful. I wish I had visited her more often.",
       fr="Çà à l'air merveilleux. J'aurais aimé lui rendre visite plus souvent.",
       es="Suena maravilloso. Ojalá la hubiera visitado más a menudo.",
       it="Sembra meraviglioso. Vorrei averla visitata più spesso.")
    _t(tr, F, "narration_test_moment",
       en="He asks so directly. His eyes seek mine — calm, attentive. Too attentive? Or merely curious?",
       fr="Il pose là question si directement. Ses yeux cherchent les miens — calmes, attentifs. Trop attentifs ? Ou simplement curieux ?",
       es="Pregunta con tanta franqueza. Sus ojos buscan los míos — serenos, atentos. ¿Demasiado atentos? ¿O solo curiosos?",
       it="Chiede in modo così diretto. I suoi occhi cercano i miei — calmi, attenti. Troppo attenti? O solo curiosi?")
    # --- Trust path ---
    _t(tr, F, "elise_trust_1",
       en="Herr Müller... Konrad. I know about the tradition. About the book beneath the church. About the feeding every thirty years.",
       fr="Herr Müller... Konrad. Je suis au courant de là tradition. Du livre sous l'église. Du nourrissage tous les trente ans.",
       es="Herr Müller... Konrad. Sé lo de la tradición. Del libro bajo la iglesia. De la alimentación cada treinta años.",
       it="Herr Müller... Konrad. So della tradizione. Del libro sotto la chiesa. Del nutrimento ogni trent'anni.")
    _t(tr, F, "konrad_trust_silence",
       en="He says nothing. His face barely changes — but his hands around the coffee cup turn white with tension.",
       fr="Il ne dit rien. Son visage change à peine — mais ses mains autour de là tasse de café deviennent blanches de tension.",
       es="No dice nada. Su rostro apenas cambia — pero sus manos alrededor de la taza de café se ponen blancas de tensión.",
       it="Non dice nulla. Il suo volto cambia appena — ma le sue mani attorno alla tazza di caffè diventano bianche per la tensione.")
    _t(tr, F, "konrad_trust_2",
       en="I know. I think I have always known. Not the details, but... the feeling. That something is wrong in this village. That I am wrong.",
       fr="Je le sais. Je crois que je l'ai toujours su. Pas les détails, mais... le sentiment. Que quelque chose ne và pas dans ce village. Que MOI, je ne vais pas.",
       es="Lo sé. Creo que siempre lo he sabido. No los detalles, pero... la sensación. De que algo no está bien en este pueblo. De que YO no estoy bien.",
       it="Lo so. Credo di averlo sempre saputo. Non i dettagli, ma... la sensazione. Che qualcosa non va in questo villaggio. Che IO non vado bene.")
    _t(tr, F, "elise_trust_ask",
       en="What does it feel like? Can you... can you sense it?",
       fr="Qu'est-ce que çà fait ? Pouvez-vous... pouvez-vous le sentir ?",
       es="¿Cómo se siente? ¿Puede... puede percibirlo?",
       it="Com'è? Può... può percepirlo?")
    _t(tr, F, "konrad_trust_describe",
       en="Imagine you are standing in a dark room. You know you are not alone. Something breathes behind you. But when you turn around, there is only... yourself.",
       fr="Imaginez-vous dans une pièce sombre. Vous savez que vous n'êtes pas seule. Quelque chose respire derrière vous. Mais quand vous vous retournez, il n'y à que... vous-même.",
       es="Imagínese en una habitación oscura. Sabe que no está sola. Algo respira detrás de usted. Pero cuando se da la vuelta, solo está... usted misma.",
       it="Si immagini in una stanza buia. Sa di non essere sola. Qualcosa respira dietro di Lei. Ma quando si gira, c'è solo... Lei stessa.")
    _t(tr, F, "konrad_trust_dreams",
       en="Sometimes I dream things that are not my dreams. I see... deeper. Older. As though I were merely a shell.",
       fr="Parfois je rêve de choses qui ne sont pas mes rêves. Je vois... plus profond. Plus ancien. Comme si je n'étais qu'une coquille.",
       es="A veces sueño cosas que no son mis sueños. Veo... más profundo. Más antiguo. Como si solo fuera una cáscara.",
       it="A volte sogno cose che non sono i miei sogni. Vedo... più in profondità. Più anticamente. Come se fossi solo un involucro.")
    _t(tr, F, "elise_trust_vessel",
       en="Konrad... Grandmother called you 'the vessel' in her diary.",
       fr="Konrad... Grand-mère vous à appelé « le réceptacle » dans son journal.",
       es="Konrad... La abuela le llamaba 'el recipiente' en su diario.",
       it="Konrad... La nonna La chiamava 'il ricettacolo' nel suo diario.")
    _t(tr, F, "konrad_trust_vessel_react",
       en="He closes his eyes. A tremor runs through his body — brief, violent, as though an electric shock had hit him.",
       fr="Il ferme les yeux. Un tremblement parcourt son corps — bref, violent, comme si un choc électrique l'avait frappé.",
       es="Cierra los ojos. Un temblor recorre su cuerpo — breve, violento, como si le hubiera alcanzado una descarga eléctrica.",
       it="Chiude gli occhi. Un tremito gli attraversa il corpo — breve, violento, come se una scossa elettrica lo avesse colpito.")
    _t(tr, F, "konrad_trust_4",
       en="The vessel. Yes. That... that explains a few things. You know, Fräulein Brandt, sometimes I wake at night and my hands are drawing spirals. Without my wanting them to.",
       fr="Le réceptacle. Oui. Ça... çà explique certaines choses. Vous savez, Fräulein Brandt, parfois je me réveille là nuit et mes mains dessinent des spirales. Sans que je le veuille.",
       es="El recipiente. Sí. Eso... eso explica algunas cosas. Sabe, Fräulein Brandt, a veces me despierto de noche y mis manos dibujan espirales. Sin que yo quiera.",
       it="Il ricettacolo. Sì. Questo... spiega alcune cose. Sa, Fräulein Brandt, a volte mi sveglio di notte è le mie mani disegnano spirali. Senza che io lo voglia.")
    _t(tr, F, "narration_trust_horror",
       en="A shiver runs down my spine. He is describing possession from the inside — and it does not sound like a monster. It sounds like a prisoner.",
       fr="Un frisson me parcourt le dos. Il décrit là possession de l'intérieur — et çà ne ressemble pas à un monstre. Çà ressemble à un prisonnier.",
       es="Un escalofrío me recorre la espalda. Describe la posesión desde dentro — y no suena como un monstruo. Suena como un prisionero.",
       it="Un brivido mi percorre la schiena. Sta descrivendo la possessione dall'interno — è non sembra un mostro. Sembra un prigioniero.")
    # --- Distrust path ---
    _t(tr, F, "elise_distrust_1",
       en="Nothing special. Old letters, recipes. Memories of an old woman.",
       fr="Rien de particulier. De vieilles lettres, des recettes. Les souvenirs d'une vieille femme.",
       es="Nada especial. Viejas cartas, recetas. Recuerdos de una anciana.",
       it="Niente di speciale. Vecchie lettere, ricette. Ricordi di una donna anziana.")
    _t(tr, F, "narration_lie",
       en="The lie comes more easily than expected. But my voice sounds too high, too even.",
       fr="Le mensonge vient plus facilement que prévu. Mais mà voix sonne trop aiguë, trop régulière.",
       es="La mentira sale más fácil de lo esperado. Pero mi voz suena demasiado aguda, demasiado uniforme.",
       it="La bugia viene più facile del previsto. Ma la mia voce suona troppo alta, troppo uniforme.")
    _t(tr, F, "konrad_distrust_2",
       en="Only memories? No... records? No notes about the village?",
       fr="Que des souvenirs ? Pas de... registres ? Pas de notes sur le village ?",
       es="¿Solo recuerdos? ¿Ningún... registro? ¿Ninguna nota sobre el pueblo?",
       it="Solo ricordi? Nessun... documento? Nessun appunto sul villaggio?")
    _t(tr, F, "elise_distrust_push",
       en="Why would she have notes about the village?",
       fr="Pourquoi aurait-elle des notes sur le village ?",
       es="¿Por qué habría de tener notas sobre el pueblo?",
       it="Perché dovrebbe avere appunti sul villaggio?")
    _t(tr, F, "konrad_distrust_shift",
       en="His smile changes. The warmth fades. For a moment something seems to slide behind his pupils. Something old.",
       fr="Son sourire change. Là chaleur disparaît. Pendant un instant, quelque chose semble glisser derrière ses pupilles. Quelque chose d'ancien.",
       es="Su sonrisa cambia. La calidez se desvanece. Por un instante algo parece deslizarse tras sus pupilas. Algo antiguo.",
       it="Il suo sorriso cambia. Il calore svanisce. Per un istante qualcosa sembra scivolare dietro le sue pupille. Qualcosa di antico.")
    _t(tr, F, "konrad_distrust_3",
       en="Of course. Only memories. Graubach is a perfectly normal village, after all.",
       fr="Bien sûr. Que des souvenirs. Graubach est un village tout à fait normal, après tout.",
       es="Por supuesto. Solo recuerdos. Al fin y al cabo, Graubach es un pueblo completamente normal.",
       it="Naturalmente. Solo ricordi. Dopotutto, Graubach è un villaggio del tutto normale.")
    _t(tr, F, "elise_distrust_shiver",
       en="The way he emphasizes 'normal' makes me shiver. He knows I am lying. And I know that he knows.",
       fr="Là façon dont il accentue « normal » me fait frissonner. Il sait que je mens. Et je sais qu'il le sait.",
       es="La forma en que enfatiza 'normal' me hace estremecer. Sabe que miento. Y yo sé que él lo sabe.",
       it="Il modo in cui enfatizza 'normale' mi fa rabbrividire. Sa che sto mentendo. È io so che lui lo sa.")
    _t(tr, F, "konrad_distrust_4",
       en="You know, Fräulein Brandt...",
       fr="Vous savez, Fräulein Brandt...",
       es="Sabe, Fräulein Brandt...",
       it="Sa, Fräulein Brandt...")
    _t(tr, F, "konrad_distrust_voice",
       en="I never lie.",
       fr="JE ne mens jamais.",
       es="YO nunca miento.",
       it="IO non mento mai.")
    _t(tr, F, "narration_distrust_horror",
       en="His voice suddenly sounds different. Deeper. Older. As though not he were speaking, but something THROUGH him. Then he blinks, and the old Konrad is back.",
       fr="Sà voix sonne soudain différemment. Plus grave. Plus ancienne. Comme si ce n'était pas lui qui parlait, mais quelque chose À TRAVERS lui. Puis il cligne des yeux, et le vieux Konrad est de retour.",
       es="Su voz suena de repente diferente. Más profunda. Más antigua. Como si no hablara él, sino algo A TRAVÉS de él. Luego parpadea, y el viejo Konrad ha vuelto.",
       it="La sua voce suona improvvisamente diversa. Più profonda. Più antica. Come se non parlasse lui, ma qualcosa ATTRAVERSO di lui. Poi batte le palpebre, è il vecchio Konrad è tornato.")
    _t(tr, F, "konrad_distrust_5",
       en="Forgive me. I am somewhat... out of sorts today. Sleep was not good.",
       fr="Pardonnez-moi. Je suis un peu... dérangé aujourd'hui. Le sommeil n'était pas bon.",
       es="Discúlpeme. Hoy estoy algo... alterado. No dormí bien.",
       it="Mi perdoni. Oggi sono un po'... confuso. Non ho dormito bene.")
    # --- Test path ---
    _t(tr, F, "elise_test_1",
       en="The church is fascinating. Those spirals on the walls — have you noticed them? I know similar patterns from my folklore studies.",
       fr="L'église est fascinante. Ces spirales sur les murs — les avez-vous remarquées ? Je connais des motifs similaires grâce à mes études de folklore.",
       es="La iglesia es fascinante. Esas espirales en las paredes — ¿las ha notado? Conozco patrones similares de mis estudios de folclore.",
       it="La chiesa è affascinante. Quelle spirali sulle pareti — le ha notate? Conosco motivi simili dai miei studi di folklore.")
    _t(tr, F, "konrad_test_react",
       en="His hand twitches. Involuntarily he grabs his wrist — right where I saw the faint spiral patterns on his skin at our last meeting.",
       fr="Sà main tressaille. Involontairement, il saisit son poignet — là même où j'avais vu les motifs spiralés sur sà peau lors de notre dernière rencontre.",
       es="Su mano se estremece. Involuntariamente se agarra la muñeca — justo donde vi los tenues patrones en espiral en su piel en nuestro último encuentro.",
       it="La sua mano sussulta. Involontariamente si afferra il polso — proprio dove avevo visto i deboli motivi a spirale sulla sua pelle al nostro ultimo incontro.")
    _t(tr, F, "konrad_test_hide",
       en="Spirals? I... no, I do not pay attention to church decoration. Pastor Voss's domain, not mine.",
       fr="Des spirales ? Je... non, je ne prête pas attention à là décoration de l'église. C'est le domaine du pasteur Voss, pas le mien.",
       es="¿Espirales? Yo... no, no presto atención a la decoración de la iglesia. Eso es cosa del pastor Voss, no mía.",
       it="Spirali? Io... no, non faccio caso alla decorazione della chiesa. È il campo del pastore Voss, non il mio.")
    _t(tr, F, "elise_test_push",
       en="Strange. You just covered your wrist. Do you have such patterns too?",
       fr="Étrange. Vous venez de couvrir votre poignet. Vous avez aussi de tels motifs ?",
       es="Extraño. Acaba de cubrirse la muñeca. ¿Tiene usted también esos patrones?",
       it="Strano. Si è appena coperto il polso. Ha anche Lei questi motivi?")
    _t(tr, F, "konrad_test_3",
       en="Spirals? No, I... I do not know any spirals.",
       fr="Des spirales ? Non, je... je ne connais aucune spirale.",
       es="¿Espirales? No, yo... no conozco ninguna espiral.",
       it="Spirali? No, io... non conosco nessuna spirale.")
    _t(tr, F, "narration_test_lie",
       en="He is lying. And he knows that I know it. The air between us grows heavy. I say nothing more — sometimes silence is more revealing than questions.",
       fr="Il ment. Et il sait que je le sais. L'air entre nous s'alourdit. Je ne dis rien de plus — parfois le silence est plus révélateur que les questions.",
       es="Miente. Y sabe que yo lo sé. El aire entre nosotros se vuelve pesado. No digo nada más — a veces el silencio es más revelador que las preguntas.",
       it="Mente. È sa che io lo so. L'aria tra noi si fa pesante. Non dico più nulla — a volte il silenzio è più rivelatore delle domande.")
    # --- Forest walk ---
    _t(tr, F, "elise_forest_hesitate",
       en="Alone with him in the forest. With the man grandmother called 'the vessel'. Any sensible person would refuse.",
       fr="Seule avec lui dans là forêt. Avec l'homme que grand-mère appelait « le réceptacle ». Toute personne sensée refuserait.",
       es="Sola con él en el bosque. Con el hombre que la abuela llamaba 'el recipiente'. Cualquier persona sensata se negaría.",
       it="Sola con lui nel bosco. Con l'uomo che la nonna chiamava 'il ricettacolo'. Qualsiasi persona di buon senso rifiuterebbe.")
    _t(tr, F, "elise_forest_decide",
       en="Show me the place.",
       fr="Montrez-moi l'endroit.",
       es="Muéstreme el lugar.",
       it="Mi mostri il posto.")
    _t(tr, F, "narration_forest_why",
       en="But I am not here to be sensible. I am here to understand.",
       fr="Mais je ne suis pas ici pour être raisonnable. Je suis ici pour comprendre.",
       es="Pero no estoy aquí para ser sensata. Estoy aquí para entender.",
       it="Ma non sono qui per essere ragionevole. Sono qui per capire.")
    _t(tr, F, "elise_forest_1",
       en="Do you come here often?",
       fr="Vous venez souvent ici ?",
       es="¿Viene aquí a menudo?",
       it="Viene qui spesso?")
    _t(tr, F, "konrad_forest_reply",
       en="Sometimes. When school is over. The forest is a good place to think.",
       fr="Parfois. Quand l'école est finie. Là forêt est un bon endroit pour réfléchir.",
       es="A veces. Cuando termina la escuela. El bosque es un buen lugar para pensar.",
       it="A volte. Quando la scuola è finita. Il bosco è un buon posto per pensare.")
    _t(tr, F, "narration_forest_walk",
       en="His steps are sure, almost automatic. As though his body knows the way even when his mind is elsewhere.",
       fr="Ses pas sont assurés, presque automatiques. Comme si son corps connaissait le chemin même quand son esprit est ailleurs.",
       es="Sus pasos son seguros, casi automáticos. Como si su cuerpo conociera el camino incluso cuando su mente está en otra parte.",
       it="I suoi passi sono sicuri, quasi automatici. Come se il suo corpo conoscesse la strada anche quando la sua mente è altrove.")
    _t(tr, F, "elise_tree_1",
       en="Spirally grown... like the patterns in the church. Like the marks on your wrist.",
       fr="Poussé en spirale... comme les motifs dans l'église. Comme les marques sur votre poignet.",
       es="Crecido en espiral... como los patrones de la iglesia. Como las marcas en su muñeca.",
       it="Cresciuto a spirale... come i motivi nella chiesa. Come i segni sul suo polso.")
    _t(tr, F, "elise_tree_feel",
       en="Yes. Beneath my feet. A pulsing — like a heartbeat.",
       fr="Oui. Sous mes pieds. Un battement — comme un cœur.",
       es="Sí. Bajo mis pies. Un pulso — como un latido.",
       it="Sì. Sotto i miei piedi. Un pulsare — come un battito cardiaco.")
    _t(tr, F, "konrad_humming",
       en="Konrad stands motionless before the tree. His lips move, barely visible. He is humming — a melody I know. The melody from the depths.",
       fr="Konrad se tient immobile devant l'arbre. Ses lèvres bougent, à peine visibles. Il fredonne — une mélodie que je connais. Là mélodie des profondeurs.",
       es="Konrad está inmóvil frente al árbol. Sus labios se mueven, apenas visibles. Tararea — una melodía que conozco. La melodía de las profundidades.",
       it="Konrad sta immobile davanti all'albero. Le sue labbra si muovono, appena visibili. Canticchia — una melodia che conosco. La melodia delle profondità.")
    _t(tr, F, "elise_humming_react",
       en="The song. You are humming the song — the singing from the depths!",
       fr="Le chant. Vous fredonnez le chant — celui qui vient des profondeurs !",
       es="¡La canción! ¡Está tarareando la canción — el canto de las profundidades!",
       it="Il canto. Sta canticchiando il canto — quello che viene dalle profondità!")
    _t(tr, F, "konrad_humming_react",
       en="He flinches as though I had struck him. His eyes widen — confusion, fear. Real fear.",
       fr="Il sursaute comme si je l'avais frappé. Ses yeux s'écarquillent — confusion, peur. Une vraie peur.",
       es="Se sobresalta como si lo hubiera golpeado. Sus ojos se abren de par en par — confusión, miedo. Miedo real.",
       it="Sussulta come se lo avessi colpito. I suoi occhi si spalancano — confusione, paura. Paura vera.")
    _t(tr, F, "konrad_humming_2",
       en="I... what? I was not... I did not know I was...",
       fr="Je... quoi ? Je n'étais pas... je ne savais pas que je...",
       es="Yo... ¿qué? No estaba... no sabía que yo...",
       it="Io... cosa? Non stavo... non sapevo che io...")
    _t(tr, F, "narration_humming_pity",
       en="He does not know it. He hums the creature's song without realizing. Like a sleepwalker who does not know where his feet are taking him.",
       fr="Il ne le sait pas. Il fredonne le chant de là créature sans s'en rendre compte. Comme un somnambule qui ne sait pas où ses pieds le mènent.",
       es="No lo sabe. Tararea la canción de la criatura sin darse cuenta. Como un sonámbulo que no sabe adónde lo llevan sus pies.",
       it="Non lo sa. Canticchia il canto della creatura senza rendersene conto. Come un sonnambulo che non sa dove lo portano i suoi piedi.")
    _t(tr, F, "elise_humming_comfort",
       en="It is all right. It is not your fault, Konrad.",
       fr="Ce n'est rien. Ce n'est pas votre faute, Konrad.",
       es="No pasa nada. No es culpa suya, Konrad.",
       it="Va tutto bene. Non è colpa Sua, Konrad.")
    _t(tr, F, "konrad_humming_3",
       en="Nothing here is my fault. And at the same time everything is my fault. Or that which is inside me.",
       fr="Rien ici n'est mà faute. Et en même temps tout est mà faute. Ou ce qui est en moi.",
       es="Nada aquí es culpa mía. Y al mismo tiempo todo es culpa mía. O de lo que hay dentro de mí.",
       it="Niente qui è colpa mia. È allo stesso tempo tutto è colpa mia. O di ciò che è dentro di me.")
    _t(tr, F, "narration_pity_moment",
       en="For the first time I do not see him as a threat. But as a victim. A man, trapped between himself and something older than the mountains.",
       fr="Pour là première fois, je ne le vois pas comme une menace. Mais comme une victime. Un homme, prisonnier entre lui-même et quelque chose de plus ancien que les montagnes.",
       es="Por primera vez no lo veo como una amenaza. Sino como una víctima. Un hombre, atrapado entre sí mismo y algo más antiguo que las montañas.",
       it="Per la prima volta non lo vedo come una minaccia. Ma come una vittima. Un uomo, intrappolato tra sé stesso è qualcosa di più antico delle montagne.")
    _t(tr, F, "elise_return_thought",
       en="Can one free a vessel without breaking it? Or has Konrad Müller long since ceased to be Konrad Müller?",
       fr="Peut-on libérer un réceptacle sans le briser ? Ou Konrad Müller a-t-il depuis longtemps cessé d'être Konrad Müller ?",
       es="¿Se puede liberar un recipiente sin romperlo? ¿O hace mucho que Konrad Müller dejó de ser Konrad Müller?",
       it="Si può liberare un ricettacolo senza romperlo? O Konrad Müller ha cessato da tempo di essere Konrad Müller?")

def _add_act2_hilde_ritual(tr):
    F = "res://data/dialogue/act2/hilde_ritual.json"
    _t(tr,F,"narration_1", en="Hilde's cottage sits at the edge of the forest, half hidden among ancient oaks. It smells of sage, chamomile, and something I cannot name — earthier, older.", fr="Là chaumière de Hilde se trouve à l'orée de là forêt, à moitié cachée parmi de vieux chênes. Çà sent là sauge, là camomille et quelque chose que je ne saurais nommer — plus terreux, plus ancien.", es="La cabaña de Hilde se encuentra al borde del bosque, medio oculta entre robles centenarios. Huele a salvia, manzanilla y algo que no puedo nombrar — más terroso, más antiguo.", it="La capanna di Hilde sorge ai margini del bosco, seminascosta tra querce antiche. Sa di salvia, camomilla è qualcosa che non riesco a nominare — più terroso, più antico.")
    _t(tr,F,"narration_2", en="She opens the door before I knock. As if she had been expecting me.", fr="Elle ouvre là porte avant que je frappe. Comme si elle m'attendait.", es="Abre la puerta antes de que yo llame. Como si me hubiera estado esperando.", it="Apre la porta prima che io bussi. Come se mi stesse aspettando.")
    _t(tr,F,"hilde_1", en="There you are at last. Margarethe said you would come. Sit down. The tea is ready.", fr="Te voilà enfin. Margarethe m'à dit que tu viendrais. Assieds-toi. Le thé est prêt.", es="Por fin has llegado. Margarethe dijo que vendrías. Siéntate. El té está listo.", it="Eccoti finalmente. Margarethe mi ha detto che saresti venuta. Siediti. Il tè è pronto.")
    _t(tr,F,"narration_3", en="Inside the cottage, bundles of herbs, roots, and small pouches hang everywhere. On the walls are symbols I recognize from my folklore studies: protective runes, older than any church.", fr="Dans là chaumière, des bouquets d'herbes, des racines et de petits sachets pendent partout. Sur les murs, des symboles que je reconnais grâce à mes études folkloriques : des runes de protection, plus anciennes que n'importe quelle église.", es="Dentro de la cabaña cuelgan por todas partes manojos de hierbas, raíces y pequeñas bolsitas. En las paredes hay símbolos que reconozco de mis estudios de folclore: runas protectoras, más antiguas que cualquier iglesia.", it="Dentro la capanna, fasci di erbe, radici è piccoli sacchetti pendono ovunque. Sulle pareti ci sono simboli che riconosco dai miei studi di folclore: rune protettive, più antiche di qualsiasi chiesa.")
    _t(tr,F,"hilde_3", en="Your grandmother and I worked together for thirty years. She was the clever one, I the patient one. Together we figured out almost everything.", fr="Tà grand-mère et moi avons travaillé ensemble pendant trente ans. Elle était l'intelligente, moi là patiente. Ensemble, nous avons presque tout découvert.", es="Tu abuela y yo trabajamos juntas durante treinta años. Ella era la lista, yo la paciente. Juntas desciframos casi todo.", it="Tua nonna è io abbiamo lavorato insieme per trent'anni. Lei era quella intelligente, io quella paziente. Insieme abbiamo scoperto quasi tutto.")
    _t(tr,F,"hilde_4", en="Almost. One piece is still missing. That is why you are here, child.", fr="Presque. Il manque encore un morceau. C'est pour çà que tu es là, mon enfant.", es="Casi. Aún falta una pieza. Para eso estás aquí, niña.", it="Quasi. Manca ancora un pezzo. Per questo sei qui, bambina.")
    _t(tr,F,"hilde_teaches_intro_2", en="There are three things you must know, child. Three components of the seal. I will teach you all of them — just as I taught Margarethe.", fr="Il y à trois choses que tu dois savoir, mon enfant. Trois composantes du sceau. Je te les enseignerai toutes — comme je les ai enseignées à Margarethe.", es="Hay tres cosas que debes saber, niña. Tres componentes del sello. Te las enseñaré todas, tal como se las enseñé a Margarethe.", it="Ci sono tre cose che devi sapere, bambina. Tre componenti del sigillo. Te le insegnerò tutte — così come le ho insegnate a Margarethe.")
    _t(tr,F,"hilde_chant_1", en="The chant. Yes. The ancient peoples who lived here before the Celts knew sounds that could calm the entity. Not defeat it — calm it. Sing it back to sleep.", fr="Le chant. Oui. Les anciens peuples qui vivaient ici avant les Celtes connaissaient des sons capables d'apaiser l'entité. Pas là vaincre — l'apaiser. Là rendormir en chantant.", es="El canto. Sí. Los pueblos antiguos que vivían aquí antes que los celtas conocían sonidos capaces de calmar a la entidad. No vencerla — calmarla. Arrullarla de vuelta al sueño.", it="Il canto. Sì. I popoli antichi che vivevano qui prima dei Celti conoscevano suoni in grado di placare l'entità. Non sconfiggerla — placarla. Cantarla per farla riaddormentare.")
    _t(tr,F,"hilde_chant_2", en="Hilde begins to hum softly. The melody is simple, almost a lullaby. But it feels different — the air grows heavier, warmer.", fr="Hilde se met à fredonner doucement. Là mélodie est simple, presque une berceuse. Mais elle semble différente — l'air devient plus lourd, plus chaud.", es="Hilde comienza a tararear suavemente. La melodía es sencilla, casi una canción de cuna. Pero se siente diferente — el aire se vuelve más pesado, más cálido.", it="Hilde comincia a canticchiare piano. La melodia è semplice, quasi una ninna nanna. Ma la si percepisce diversa — l'aria si fa più pesante, più calda.")
    _t(tr,F,"hilde_chant_3", en="And then — for a brief moment — the distant singing from the depths falls silent. Complete stillness. As if the earth were holding its breath.", fr="Et puis — pendant un bref instant — le chant lointain venu des profondeurs se tait. Un silence total. Comme si là terre retenait son souffle.", es="Y entonces — por un breve instante — el canto lejano de las profundidades se calla. Quietud absoluta. Como si la tierra contuviera la respiración.", it="E poi — per un breve istante — il canto lontano dal profondo tace. Silenzio assoluto. Come se la terrà trattenesse il respiro.")
    _t(tr,F,"hilde_chant_4", en="Do you hear? Silence. The chant works. But I am old. My voice will no longer suffice for the full ritual. You must learn it.", fr="Tu entends ? Le silence. Le chant fonctionne. Mais je suis vieille. Mà voix ne suffirà plus pour le rituel complet. Tu dois l'apprendre.", es="¿Oyes? Silencio. El canto funciona. Pero soy vieja. Mi voz ya no bastará para el ritual completo. Tú debes aprenderlo.", it="Senti? Silenzio. Il canto funziona. Ma sono vecchia. La mia voce non basterà più per il rituale completo. Devi impararlo tu.")
    _t(tr,F,"transition_to_sign", en="Hilde waits until the silence has settled. The singing from the depths resumes, timidly at first. Then she speaks again, calmer now.", fr="Hilde attend que le silence se soit installé. Le chant des profondeurs reprend, timidement d'abord. Puis elle reprend là parole, plus calme à présent.", es="Hilde espera hasta que el silencio se haya asentado. El canto de las profundidades se reanuda tímidamente. Luego continúa hablando, más serena ahora.", it="Hilde aspetta che il silenzio si sia posato. Il canto dal profondo riprende, timidamente. Poi parla di nuovo, più calma ora.")
    _t(tr,F,"hilde_sign_1", en="The sign of the earth is not a mark that one draws. It is a place. Where the entity comes closest to the surface.", fr="Le signe de là terre n'est pas une marque que l'on trace. C'est un lieu. Là où l'entité se rapproche le plus de là surface.", es="El signo de la tierra no es una marca que se dibuja. Es un lugar. Donde la entidad se acerca más a la superficie.", it="Il segno della terrà non è un marchio che si disegna. È un luogo. Dove l'entità si avvicina di più alla superficie.")
    _t(tr,F,"hilde_sign_2", en="In the chamber beneath the church there is a point where the stone is thinner. There you feel the heartbeat most clearly. That is the sign — not made by human hands.", fr="Dans là chambre sous l'église, il y à un endroit où là pierre est plus mince. C'est là qu'on sent le battement de cœur le plus clairement. C'est le signe — il n'à pas été créé par là main de l'homme.", es="En la cámara bajo la iglesia hay un punto donde la piedra es más delgada. Allí se siente el latido con más claridad. Ese es el signo — no fue creado por manos humanas.", it="Nella camera sotto la chiesa c'è un punto dove la pietra è più sottile. Lì si sente il battito più chiaramente. Quello è il segno — non creato da mano umana.")
    _t(tr,F,"hilde_sign_3", en="Your grandmother found it. You must stand exactly there when you begin the chant. Otherwise the effect dissipates.", fr="Tà grand-mère l'à trouvé. Tu dois te tenir exactement là quand tu entonnes le chant. Sinon l'effet se dissipe.", es="Tu abuela lo encontró. Debes estar exactamente ahí cuando entones el canto. De lo contrario, el efecto se desvanece.", it="Tua nonna l'ha trovato. Devi stare esattamente lì quando intoni il canto. Altrimenti l'effetto svanisce.")
    _t(tr,F,"transition_to_anchor", en="Hilde stands and walks to the window. Outside, the trees sway in the wind, as if listening.", fr="Hilde se lève et s'approche de là fenêtre. Dehors, les arbres se balancent dans le vent, comme s'ils écoutaient.", es="Hilde se levanta y camina hacia la ventana. Afuera, los árboles se mecen con el viento, como si escucharan.", it="Hilde si alza è va alla finestra. Fuori, gli alberi si piegano nel vento, come se stessero ascoltando.")
    _t(tr,F,"hilde_anchor_1", en="The anchor. That is the hardest part. Someone must serve as a link between our world and the entity. Someone who knows it but does not fear it.", fr="L'ancre. C'est là partie là plus difficile. Quelqu'un doit servir de lien entre notre monde et l'entité. Quelqu'un qui là connaît mais ne là craint pas.", es="El ancla. Esa es la parte más difícil. Alguien debe servir de vínculo entre nuestro mundo y la entidad. Alguien que la conozca pero no la tema.", it="L'àncora. Questa è la parte più difficile. Qualcuno deve fungere da collegamento tra il nostro mondo è l'entità. Qualcuno che la conosca ma non la tema.")
    _t(tr,F,"hilde_anchor_3", en="Margarethe wanted to do it herself. But she grew too old, too frail. As the anchor, one must be strong — in spirit, not in body.", fr="Margarethe voulait le faire elle-même. Mais elle est devenue trop vieille, trop fragile. En tant qu'ancre, on doit être fort — en esprit, pas en corps.", es="Margarethe quería hacerlo ella misma. Pero se volvió demasiado vieja, demasiado débil. Como ancla, uno debe ser fuerte — de espíritu, no de cuerpo.", it="Margarethe voleva farlo lei stessa. Ma è diventata troppo vecchia, troppo fragile. Come àncora, bisogna essere forti — nello spirito, non nel corpo.")
    _t(tr,F,"hilde_anchor_5", en="Elise... Margarethe believed that you could be the anchor. Your name in the book — it is not a curse. It is a connection. You are already close to the entity.", fr="Elise... Margarethe croyait que tu pourrais être l'ancre. Ton nom dans le livre — ce n'est pas une malédiction. C'est un lien. Tu es déjà proche de l'entité.", es="Elise... Margarethe creía que tú podrías ser el ancla. Tu nombre en el libro — no es una maldición. Es una conexión. Ya estás cerca de la entidad.", it="Elise... Margarethe credeva che tu potessi essere l'àncora. Il tuo nome nel libro — non è una maledizione. È un legame. Sei già vicina all'entità.")
    _t(tr,F,"hilde_warning_1", en="But listen to me carefully, child. There is someone you must not trust.", fr="Mais écoute-moi bien, mon enfant. Il y à quelqu'un à qui tu ne dois pas faire confiance.", es="Pero escúchame bien, niña. Hay alguien en quien no debes confiar.", it="Ma ascoltami bene, bambina. C'è qualcuno di cui non devi fidarti.")
    _t(tr,F,"hilde_warning_3", en="Otto Reinhardt. The mayor. He is the keeper of the old tradition. He will do anything to ensure the feeding takes place. And he has helpers.", fr="Otto Reinhardt. Le maire. Il est le gardien de l'ancienne tradition. Il ferà tout pour que le nourrissage ait lieu. Et il à des complices.", es="Otto Reinhardt. El alcalde. Es el guardián de la vieja tradición. Hará lo que sea para que la alimentación se lleve a cabo. Y tiene cómplices.", it="Otto Reinhardt. Il sindaco. È il custode dell'antica tradizione. Farà qualsiasi cosa per assicurare che il nutrimento avvenga. È ha dei complici.")
    _t(tr,F,"hilde_warning_5", en="If he finds out what you intend — if he realizes you are continuing Margarethe's work — he will act. Swiftly and without conscience.", fr="S'il découvre ce que tu comptes faire — s'il réalise que tu poursuis le travail de Margarethe — il agira. Vite et sans scrupule.", es="Si descubre lo que pretendes — si se da cuenta de que continúas el trabajo de Margarethe — actuará. Rápido y sin escrúpulos.", it="Se scopre cosa intendi fare — se capisce che stai continuando il lavoro di Margarethe — agirà. Rapidamente è senza scrupoli.")
    _t(tr,F,"hilde_gift_1", en="Hilde reaches into her apron and presses a small pouch into my hand. Inside are dried herbs and a round stone amulet with a spiral carved into it.", fr="Hilde plonge là main dans son tablier et me glisse un petit sachet dans là main. À l'intérieur, des herbes séchées et une amulette de pierre ronde avec une spirale gravée.", es="Hilde mete la mano en su delantal y me pone una pequeña bolsita en la mano. Dentro hay hierbas secas y un amuleto de piedra redondo con una espiral tallada.", it="Hilde infila la mano nel grembiule è mi preme un sacchettino nel palmo. Dentro ci sono erbe essiccate è un amuleto di pietra rotondo con una spirale incisa.")
    _t(tr,F,"hilde_gift_2", en="Carry this with you. It does not protect against the entity — nothing does. But it protects against its dreams. You will be able to think more clearly.", fr="Garde ceci sur toi. Çà ne protège pas contre l'entité — rien ne le peut. Mais çà protège contre ses rêves. Tu pourras penser plus clairement.", es="Llévalo contigo. No protege contra la entidad — nada lo hace. Pero protege contra sus sueños. Podrás pensar con más claridad.", it="Portalo con te. Non protegge dall'entità — nulla può farlo. Ma protegge dai suoi sogni. Riuscirai a pensare più lucidamente.")
    _t(tr,F,"journal_hilde", en="Hilde's Teachings", fr="Les Enseignements de Hilde", es="Las enseñanzas de Hilde", it="Gli insegnamenti di Hilde", field="title")
    _t(tr,F,"journal_hilde", en="Hilde taught me all three components of the binding ritual: 1) The ancient chant — older than any known language, it calms the entity. 2) The sign of the earth — a place in the chamber beneath the church where the stone is thinnest. 3) The anchor — a person with a connection to the entity. Grandmother believed I could be the anchor. Hilde warned me about the mayor.", fr="Hilde m'à enseigné les trois composantes du rituel de scellement : 1) L'ancien chant — plus vieux que toute langue connue, il apaise l'entité. 2) Le signe de là terre — un endroit dans là chambre sous l'église où là pierre est là plus mince. 3) L'ancre — une personne liée à l'entité. Grand-mère croyait que je pourrais être l'ancre. Hilde m'à mise en garde contre le maire.", es="Hilde me enseñó los tres componentes del ritual de sellado: 1) El canto antiguo — más viejo que cualquier idioma conocido, calma a la entidad. 2) El signo de la tierra — un lugar en la cámara bajo la iglesia donde la piedra es más delgada. 3) El ancla — una persona con conexión a la entidad. La abuela creía que yo podría ser el ancla. Hilde me advirtió sobre el alcalde.", it="Hilde mi ha insegnato tutte è tre le componenti del rituale di sigillo: 1) L'antico canto — più antico di qualsiasi lingua conosciuta, placa l'entità. 2) Il segno della terrà — un luogo nella camera sotto la chiesa dove la pietra è più sottile. 3) L'àncora — una persona legata all'entità. La nonna credeva che io potessi essere l'àncora. Hilde mi ha messo in guardia dal sindaco.", field="content")
    _t(tr,F,"narration_evening", en="As I leave Hilde's cottage, dusk is falling. The forest is closer than this morning. I am certain of it.", fr="En quittant là chaumière de Hilde, le crépuscule tombe. Là forêt est plus proche que ce matin. J'en suis certaine.", es="Al salir de la cabaña de Hilde, cae el crepúsculo. El bosque está más cerca que esta mañana. Estoy segura de ello.", it="Mentre lascio la capanna di Hilde, cala il crepuscolo. Il bosco è più vicino di stamattina. Ne sono certa.")
    _t(tr,F,"narration_evening_2", en="On the way back I hear footsteps behind me. Heavy, deliberate. I turn around — no one there. But among the trees hangs a cloying scent, like wilted flowers.", fr="Sur le chemin du retour, j'entends des pas derrière moi. Lourds, mesurés. Je me retourne — personne. Mais entre les arbres flotte une odeur douceâtre, comme des fleurs fanées.", es="De regreso oigo pasos detrás de mí. Pesados, pausados. Me doy la vuelta — nadie. Pero entre los árboles flota un olor empalagoso, como flores marchitas.", it="Sulla via del ritorno sento passi dietro di me. Pesanti, lenti. Mi giro — nessuno. Ma tra gli alberi aleggia un odore dolciastro, come fiori appassiti.")

    # --- Additional translations (auto-generated) ---
    _t(tr, F, "elise_arrive",
       en="You were expecting me? How did you know I would come today?",
       fr="Vous m'attendiez ? Comment saviez-vous que je viendrais aujourd'hui ?",
       es="¿Me estaba esperando? ¿Cómo sabía que vendría hoy?",
       it="Mi aspettava? Come sapeva che sarei venuta oggi?")

    _t(tr, F, "hilde_expected",
       en="Thirty years teach you to read the signs. You met Konrad, visited the church, read the journal. The next step was always to come to me.",
       fr="Trente ans vous apprennent à lire les signes. Tu as rencontré Konrad, visité l'église, lu le journal. L'étape suivante menait toujours à moi.",
       es="Treinta años le enseñan a uno a leer las señales. Conociste a Konrad, visitaste la iglesia, leíste el diario. El siguiente paso siempre era venir a mí.",
       it="Trent'anni insegnano a leggere i segni. Hai incontrato Konrad, visitato la chiesa, letto il diario. Il passo successivo era sempre venire da me.")

    _t(tr, F, "elise_runes",
       en="Those runes on your walls - I recognise them. Germanic, but with Celtic elements. We studied them in the third semester.",
       fr="Ces runes sur vos murs - je les reconnais. Germaniques, mais avec des éléments celtiques. Nous les avons étudiées au troisième semestre.",
       es="Esas runas en sus paredes... las conozco. Germánicas, pero con elementos celtas. Las estudiamos en el tercer semestre.",
       it="Quelle rune sulle sue pareti... le conosco. Germaniche, ma con elementi celtici. Le abbiamo studiate al terzo semestre.")

    _t(tr, F, "hilde_impressed_2",
       en="You have sharp eyes. Most people only see scribbles. Your grandmother recognised them immediately too.",
       fr="Tu as de bons yeux. La plupart des gens n'y voient que des gribouillis. Ta grand-mère les a reconnues tout de suite aussi.",
       es="Tienes buen ojo. La mayoría solo ve garabatos. Tu abuela también las reconoció de inmediato.",
       it="Hai occhio fino. La maggior parte della gente vede solo scarabocchi. Anche tua nonna le riconobbe subito.")

    _t(tr, F, "elise_grandmother_question",
       en="Hilde... how was Grandmother in her last years? Was she happy here? Was she afraid?",
       fr="Hilde... comment allait Grand-mère ces dernières années ? Était-elle heureuse ici ? Avait-elle peur ?",
       es="Hilde... ¿cómo estaba la abuela en sus últimos años? ¿Era feliz aquí? ¿Tenía miedo?",
       it="Hilde... com'era la nonna negli ultimi anni? Era felice qui? Aveva paura?")

    _t(tr, F, "hilde_personal",
       en="Hilde pauses. Her hands close tighter around the teacup.",
       fr="Hilde s'arrête. Ses mains serrent plus fort la tasse de thé.",
       es="Hilde se detiene. Sus manos aprietan con más fuerza la taza de té.",
       it="Hilde si ferma. Le sue mani stringono più forte la tazza di tè.")

    _t(tr, F, "hilde_personal_2",
       en="She was... resolute. Not happy, no. But not unhappy either. She had a purpose, and that gave her strength. In the last months, however...",
       fr="Elle était... déterminée. Pas heureuse, non. Mais pas malheureuse non plus. Elle avait une mission, et cela lui donnait de la force. Ces derniers mois, cependant...",
       es="Ella estaba... decidida. No era feliz, no. Pero tampoco infeliz. Tenía una misión, y eso le daba fuerzas. En los últimos meses, sin embargo...",
       it="Era... risoluta. Non felice, no. Ma neppure infelice. Aveva un compito, e quello le dava forza. Negli ultimi mesi, però...")

    _t(tr, F, "hilde_personal_4",
       en="In the last months she grew quieter. She knew time was running short. And she was afraid - not for herself. For you.",
       fr="Ces derniers mois, elle est devenue plus silencieuse. Elle savait que le temps pressait. Et elle avait peur - pas pour elle. Pour toi.",
       es="En los últimos meses se volvió más callada. Sabía que el tiempo se agotaba. Y tenía miedo, no por ella. Por ti.",
       it="Negli ultimi mesi divenne più silenziosa. Sapeva che il tempo stringeva. E aveva paura - non per sé stessa. Per te.")

    _t(tr, F, "elise_react_personal",
       en="For me. For thirty years she thought of me. Of the girl whose name stands in the book, even before she was born.",
       fr="Pour moi. Pendant trente ans, elle a pensé à moi. À la fille dont le nom figure dans le livre, avant même sa naissance.",
       es="Por mí. Durante treinta años pensó en mí. En la chica cuyo nombre aparece en el libro, incluso antes de que naciera.",
       it="Per me. Per trent'anni ha pensato a me. Alla ragazza il cui nome è scritto nel libro, ancor prima che nascesse.")

    _t(tr, F, "hilde_tea",
       en="Hilde pours me tea. The liquid is dark green, nearly black, and smells of earth and honey.",
       fr="Hilde me sert du thé. Le liquide est vert foncé, presque noir, et sent la terre et le miel.",
       es="Hilde me sirve té. El líquido es verde oscuro, casi negro, y huele a tierra y miel.",
       it="Hilde mi versa del tè. Il liquido è verde scuro, quasi nero, e profuma di terra e miele.")

    _t(tr, F, "elise_tea_skeptic",
       en="What is in the tea? Forgive the question, but after everything I have experienced here...",
       fr="Qu'y a-t-il dans ce thé ? Pardonnez la question, mais après tout ce que j'ai vécu ici...",
       es="¿Qué contiene el té? Perdone la pregunta, pero después de todo lo que he vivido aquí...",
       it="Cosa c'è nel tè? Perdoni la domanda, ma dopo tutto quello che ho vissuto qui...")

    _t(tr, F, "hilde_tea_laugh",
       en="Ha! Suspicious. Good. Valerian, lemon balm, St. John's wort and a little thyme. No poison, no magic. Just herbs for the nerves.",
       fr="Ha ! Méfiante. Bien. Valériane, mélisse, millepertuis et un peu de thym. Pas de poison, pas de sortilège. Juste des herbes contre la peur.",
       es="¡Ja! Desconfiada. Bien. Valeriana, melisa, hipérico y un poco de tomillo. Ni veneno ni hechizo. Solo hierbas contra el miedo.",
       it="Ah! Diffidente. Bene. Valeriana, melissa, iperico e un po' di timo. Niente veleno, niente magia. Solo erbe contro la paura.")

    _t(tr, F, "elise_tea_drink",
       en="I drink. The tea is bitter but warming. Something truly loosens in my chest - a tension I have been carrying for days.",
       fr="Je bois. Le thé est amer, mais réchauffant. Quelque chose se dénoue vraiment dans ma poitrine - une tension que je porte depuis des jours.",
       es="Bebo. El té es amargo, pero reconfortante. Algo se afloja en mi pecho, una tensión que llevo arrastrando desde hace días.",
       it="Bevo. Il tè è amaro, ma riscaldante. Qualcosa si scioglie davvero nel mio petto - una tensione che porto con me da giorni.")

    _t(tr, F, "hilde_teaches_intro",
       en="Your grandmother and I worked together for thirty years. She was the clever one, I the patient one. Together we figured out nearly everything.",
       fr="Ta grand-mère et moi avons travaillé ensemble pendant trente ans. Elle était l'intelligente, moi la patiente. Ensemble, nous avons presque tout compris.",
       es="Tu abuela y yo trabajamos juntas durante treinta años. Ella era la inteligente, yo la paciente. Juntas lo descubrimos casi todo.",
       it="Tua nonna e io abbiamo lavorato insieme per trent'anni. Lei era la sagace, io la paziente. Insieme abbiamo scoperto quasi tutto.")

    _t(tr, F, "elise_ready",
       en="Then show me. Everything.",
       fr="Alors montrez-moi. Tout.",
       es="Entonces enséñemelo. Todo.",
       it="Allora me lo mostri. Tutto.")

    _t(tr, F, "elise_chant_question",
       en="From my studies I know of sonic rituals among the Germanic peoples. But those were ceremonial. Do you mean the tones themselves have an... effect?",
       fr="Mes études m'ont appris l'existence de rituels sonores chez les Germains. Mais c'était cérémoniel. Vous voulez dire que les sons eux-mêmes ont un... effet ?",
       es="Por mis estudios conozco los rituales sonoros de los pueblos germánicos. Pero eran ceremoniales. ¿Quiere decir que los sonidos en sí tienen un... efecto?",
       it="Dai miei studi conosco i rituali sonori dei popoli germanici. Ma erano cerimoniali. Intende dire che i suoni stessi hanno un... effetto?")

    _t(tr, F, "hilde_chant_confirm",
       en="Not the tones alone. The resonance. Listen.",
       fr="Pas les sons seuls. La résonance. Écoute.",
       es="No los sonidos solos. La resonancia. Escucha.",
       it="Non i suoni da soli. La risonanza. Ascolta.")

    _t(tr, F, "elise_chant_amazed",
       en="It stopped. The singing - it is silent!",
       fr="Ça s'est arrêté. Le chant... c'est le silence !",
       es="Ha parado. El canto... ¡hay silencio!",
       it="Si è fermato. Il canto... è silenzio!")

    _t(tr, F, "elise_chant_try",
       en="I can try. But I am no singer, Hilde.",
       fr="Je peux essayer. Mais je ne suis pas chanteuse, Hilde.",
       es="Puedo intentarlo. Pero no soy cantante, Hilde.",
       it="Posso provare. Ma non sono una cantante, Hilde.")

    _t(tr, F, "hilde_chant_teach",
       en="It is not about beauty. It is about intent. Sing with me.",
       fr="Ce n'est pas une question de beauté. C'est une question d'intention. Chante avec moi.",
       es="No se trata de belleza. Se trata de intención. Canta conmigo.",
       it="Non si tratta di bellezza. Si tratta di intenzione. Canta con me.")

    _t(tr, F, "narration_chant_try",
       en="I try to hum along with the melody. My voice is uncertain, trembling. But after a few bars I find the rhythm - and something responds.",
       fr="J'essaie de fredonner la mélodie. Ma voix est hésitante, tremblante. Mais après quelques mesures, je trouve le rythme - et quelque chose répond.",
       es="Intento tararear la melodía. Mi voz es insegura, temblorosa. Pero tras unos compases encuentro el ritmo, y algo responde.",
       it="Provo a canticchiare la melodia. La mia voce è incerta, tremante. Ma dopo qualche battuta trovo il ritmo - e qualcosa risponde.")

    _t(tr, F, "narration_chant_response",
       en="Deep beneath us, barely perceptible, something shifts. The singing from the depths falters - only for a moment, but it falters. It heard me.",
       fr="Profondément sous nous, à peine perceptible, quelque chose se déplace. Le chant des profondeurs vacille - un instant seulement, mais il vacille. Il m'a entendue.",
       es="En lo profundo, apenas perceptible, algo se desplaza. El canto de las profundidades titubea, solo un instante, pero titubea. Me ha oído.",
       it="In profondità sotto di noi, appena percettibile, qualcosa si muove. Il canto degli abissi vacilla - solo per un istante, ma vacilla. Mi ha sentita.")

    _t(tr, F, "elise_chant_fear",
       en="It reacted. It heard ME. Hilde, it knows I am here!",
       fr="Il a réagi. Il M'a entendue. Hilde, il sait que je suis là !",
       es="Ha reaccionado. ¡ME ha oído! ¡Hilde, sabe que estoy aquí!",
       it="Ha reagito. Ha sentito ME. Hilde, sa che sono qui!")

    _t(tr, F, "hilde_chant_calm",
       en="It knew that already, child. Your name stands in its book. But now it knows you can SING. That is important.",
       fr="Il le savait déjà, mon enfant. Ton nom figure dans son livre. Mais maintenant il sait que tu peux CHANTER. C'est important.",
       es="Ya lo sabía, niña. Tu nombre está en su libro. Pero ahora sabe que puedes CANTAR. Eso es importante.",
       it="Lo sapeva già, bambina. Il tuo nome è scritto nel suo libro. Ma ora sa che puoi CANTARE. Questo è importante.")

    _t(tr, F, "elise_sign_question",
       en="The chamber beneath the church. Where the ground pulses.",
       fr="La chambre sous l'église. Là où le sol palpite.",
       es="La cámara bajo la iglesia. Donde el suelo palpita.",
       it="La camera sotto la chiesa. Dove il pavimento pulsa.")

    _t(tr, F, "elise_sign_react",
       en="Standing directly above the creature and singing. That sounds like... knocking on a door and hoping that what lurks behind it does not open.",
       fr="Se tenir juste au-dessus de la créature et chanter. Ça ressemble à... frapper à une porte en espérant que ce qui se tapit derrière n'ouvrira pas.",
       es="Estar directamente sobre la criatura y cantar. Suena como... llamar a una puerta y esperar que lo que acecha detrás no la abra.",
       it="Stare direttamente sopra la creatura e cantare. Sembra come... bussare a una porta sperando che ciò che si annida dietro non apra.")

    _t(tr, F, "hilde_sign_honest",
       en="That is roughly what it is. The chant is the knocking. And yes - it could open.",
       fr="C'est à peu près ça. Le chant est le coup frappé. Et oui - elle pourrait s'ouvrir.",
       es="Es más o menos eso. El canto es la llamada. Y sí, podría abrir.",
       it="È più o meno così. Il canto è il bussare. E sì - potrebbe aprire.")

    _t(tr, F, "elise_anchor_question",
       en="What happens to the anchor? Does one survive it?",
       fr="Que devient l'ancre ? Est-ce qu'on y survit ?",
       es="¿Qué le pasa al ancla? ¿Se sobrevive a eso?",
       it="Cosa succede all'àncora? Si sopravvive?")

    _t(tr, F, "hilde_anchor_hesitate",
       en="Hilde hesitates. For the first time in this conversation, she avoids my gaze.",
       fr="Hilde hésite. Pour la première fois dans cette conversation, elle détourne le regard.",
       es="Hilde vacila. Por primera vez en esta conversación, evita mi mirada.",
       it="Hilde esita. Per la prima volta in questa conversazione, sfugge al mio sguardo.")

    _t(tr, F, "hilde_anchor_2",
       en="Margarethe wanted to do it herself. But she grew too old, too frail. As the anchor one must be strong - in spirit, not in body.",
       fr="Margarethe voulait le faire elle-même. Mais elle est devenue trop vieille, trop faible. L'ancre doit être forte - en esprit, pas en corps.",
       es="Margarethe quería hacerlo ella misma. Pero se volvió demasiado vieja, demasiado débil. Como ancla hay que ser fuerte, de espíritu, no de cuerpo.",
       it="Margarethe voleva farlo lei stessa. Ma divenne troppo vecchia, troppo debole. Come àncora bisogna essere forti - nello spirito, non nel corpo.")

    _t(tr, F, "elise_anchor_press",
       en="Hilde. You did not answer my question. Does one survive it?",
       fr="Hilde. Vous n'avez pas répondu à ma question. Est-ce qu'on y survit ?",
       es="Hilde. No ha respondido a mi pregunta. ¿Se sobrevive?",
       it="Hilde. Non ha risposto alla mia domanda. Si sopravvive?")

    _t(tr, F, "hilde_anchor_truth",
       en="Margarethe was not certain. No one has ever tried it. She died before she could find the answer.",
       fr="Margarethe n'en était pas sûre. Personne n'a jamais essayé. Elle est morte avant de trouver la réponse.",
       es="Margarethe no estaba segura. Nadie lo ha intentado nunca. Murió antes de poder encontrar la respuesta.",
       it="Margarethe non ne era certa. Nessuno l'ha mai tentato. È morta prima di poter trovare la risposta.")

    _t(tr, F, "narration_anchor_weight",
       en="Not certain. That means it could kill me. Or worse - it could change me. The way it changed Konrad.",
       fr="Pas sûre. Cela signifie que ça pourrait me tuer. Ou pire - me transformer. Comme ça a transformé Konrad.",
       es="No estaba segura. Eso significa que podría matarme. O peor: podría cambiarme. Como cambió a Konrad.",
       it="Non era certa. Significa che potrebbe uccidermi. O peggio - potrebbe cambiarmi. Come ha cambiato Konrad.")

    _t(tr, F, "elise_anchor_horror",
       en="That means the creature KNOWS me? It knows who I am?",
       fr="Cela veut dire que la créature me CONNAÎT ? Elle sait qui je suis ?",
       es="¿Eso significa que la criatura me CONOCE? ¿Sabe quién soy?",
       it="Vuol dire che la creatura mi CONOSCE? Sa chi sono?")

    _t(tr, F, "hilde_anchor_knows",
       en="It knows your name. It wrote it itself - in a script no human should read. Yes, child. It knows you.",
       fr="Il connaît ton nom. Il l'a écrit lui-même - dans une écriture qu'aucun humain ne devrait lire. Oui, mon enfant. Il te connaît.",
       es="Conoce tu nombre. Lo escribió él mismo, en una escritura que ningún humano debería leer. Sí, niña. Te conoce.",
       it="Conosce il tuo nome. L'ha scritto lei stessa - in una scrittura che nessun umano dovrebbe leggere. Sì, bambina. Ti conosce.")

    _t(tr, F, "narration_anchor_existential",
       en="A shiver runs down my spine. Something beneath the earth, older than humanity, knows my name. Wrote it before I was born. What AM I to this being?",
       fr="Un frisson me parcourt l'échine. Quelque chose sous la terre, plus ancien que l'humanité, connaît mon nom. L'a écrit avant ma naissance. Que SUIS-JE pour cet être ?",
       es="Un escalofrío me recorre la espalda. Algo bajo la tierra, más antiguo que la humanidad, conoce mi nombre. Lo escribió antes de que yo naciera. ¿Qué SOY para este ser?",
       it="Un brivido mi percorre la schiena. Qualcosa sotto terra, più antico dell'umanità, conosce il mio nome. L'ha scritto prima che io nascessi. Cosa SONO per questo essere?")

    _t(tr, F, "elise_warning_guess",
       en="Otto Reinhardt. The mayor.",
       fr="Otto Reinhardt. Le maire.",
       es="Otto Reinhardt. El alcalde.",
       it="Otto Reinhardt. Il sindaco.")

    _t(tr, F, "hilde_warning_surprised",
       en="You are quick. Yes - Otto. He is the keeper of the old tradition. He will do anything to enforce the feeding. And he has helpers.",
       fr="Tu es vive. Oui - Otto. Il est le gardien de l'ancienne tradition. Il fera tout pour imposer le nourrissage. Et il a des complices.",
       es="Eres rápida. Sí, Otto. Es el guardián de la vieja tradición. Hará cualquier cosa para imponer la alimentación. Y tiene cómplices.",
       it="Sei svelta. Sì - Otto. È il custode dell'antica tradizione. Farà di tutto per imporre il nutrimento. E ha dei complici.")

    _t(tr, F, "elise_warning_react",
       en="He could not stop my grandmother. He will not stop me either.",
       fr="Il n'a pas pu arrêter ma grand-mère. Il ne m'arrêtera pas non plus.",
       es="No pudo detener a mi abuela. A mí tampoco me detendrá.",
       it="Non è riuscito a fermare mia nonna. Non fermerà neppure me.")

    _t(tr, F, "hilde_warning_smile",
       en="You are more like her than you think.",
       fr="Tu lui ressembles plus que tu ne le crois.",
       es="Te pareces a ella más de lo que crees.",
       it="Le assomigli più di quanto pensi.")

    _t(tr, F, "elise_gift_react",
       en="Thank you, Hilde. For everything. For standing by Grandmother's side for thirty years.",
       fr="Merci, Hilde. Pour tout. D'être restée aux côtés de Grand-mère pendant trente ans.",
       es="Gracias, Hilde. Por todo. Por haber estado al lado de la abuela durante treinta años.",
       it="Grazie, Hilde. Per tutto. Per essere rimasta al fianco della nonna per trent'anni.")

    _t(tr, F, "hilde_gift_personal",
       en="Margarethe was my dearest friend. The only one who never thought me mad. And now you are here, and I am no longer alone with it.",
       fr="Margarethe était ma meilleure amie. La seule qui ne m'ait jamais prise pour une folle. Et maintenant tu es là, et je ne suis plus seule avec ce secret.",
       es="Margarethe era mi mejor amiga. La única que nunca me tomó por loca. Y ahora estás tú aquí, y ya no estoy sola con esto.",
       it="Margarethe era la mia migliore amica. L'unica che non mi abbia mai presa per pazza. E ora sei qui tu, e non sono più sola con tutto questo.")

    _t(tr, F, "narration_gift_moment",
       en="Her eyes glisten. For thirty years she carried this secret, together with Grandmother. And now the burden rests upon my shoulders.",
       fr="Ses yeux brillent. Pendant trente ans, elle a porté ce secret, avec Grand-mère. Et maintenant le fardeau repose sur mes épaules.",
       es="Sus ojos brillan. Durante treinta años cargó con este secreto, junto a la abuela. Y ahora el peso recae sobre mis hombros.",
       it="I suoi occhi brillano. Per trent'anni ha portato questo segreto, insieme alla nonna. E ora il peso grava sulle mie spalle.")

    _t(tr, F, "elise_stalked",
       en="My heart pounds. Among the trees hangs a sweet smell, like wilted flowers. The footsteps resume - closer this time.",
       fr="Mon cœur bat à tout rompre. Entre les arbres flotte une odeur douceâtre, comme des fleurs fanées. Les pas reprennent - plus proches cette fois.",
       es="Mi corazón martillea. Entre los árboles flota un olor dulzón, como flores marchitas. Los pasos se reanudan, más cerca esta vez.",
       it="Il mio cuore martella. Tra gli alberi aleggia un odore dolciastro, come fiori appassiti. I passi riprendono - più vicini questa volta.")

    _t(tr, F, "narration_stalked_run",
       en="I run. The last metres to the road I sprint. Only in the lamplight before Grandmother's house do I stop, gasping for breath.",
       fr="Je cours. Les derniers mètres jusqu'à la route, je les parcours en sprintant. Ce n'est que sous le réverbère devant la maison de Grand-mère que je m'arrête, haletante.",
       es="Echo a correr. Los últimos metros hasta la carretera los recorro a toda prisa. Solo bajo la farola frente a la casa de la abuela me detengo, jadeando.",
       it="Corro. Gli ultimi metri fino alla strada li percorro di corsa. Solo sotto il lampione davanti alla casa della nonna mi fermo, senza fiato.")

    _t(tr, F, "narration_stalked_who",
       en="Who was that? Otto? One of his helpers? Or something else entirely? The amulet in my pocket feels warm - as though it were working.",
       fr="Qui était-ce ? Otto ? Un de ses complices ? Ou quelque chose de tout autre ? L'amulette dans ma poche est chaude - comme si elle travaillait.",
       es="¿Quién era? ¿Otto? ¿Uno de sus cómplices? ¿O algo completamente distinto? El amuleto en mi bolsillo está caliente, como si estuviera trabajando.",
       it="Chi era? Otto? Uno dei suoi complici? O qualcosa di completamente diverso? L'amuleto nella mia tasca è caldo - come se stesse lavorando.")


def _add_act2_the_book(tr):
    F = "res://data/dialogue/act2/the_book.json"
    _t(tr,F,"narration_1", en="Day five. Midnight. The village sleeps — or pretends to. I creep through the empty lanes toward the church.", fr="Cinquième jour. Minuit. Le village dort — où fait semblant. Je me faufile dans les ruelles désertes vers l'église.", es="Día cinco. Medianoche. El pueblo duerme — o finge hacerlo. Me escabullo por las callejuelas vacías hacia la iglesia.", it="Quinto giorno. Mezzanotte. Il villaggio dorme — o finge di farlo. Sguscio per i vicoli vuoti verso la chiesa.")
    _t(tr,F,"narration_2", en="Georg's key sits heavy in my pocket. Hilde's amulet rests against my chest. Grandmother's journal is in my bag.", fr="Là clé de Georg pèse dans mà poche. L'amulette de Hilde repose contre mà poitrine. Le journal de grand-mère est dans mon sac.", es="La llave de Georg pesa en mi bolsillo. El amuleto de Hilde descansa sobre mi pecho. El diario de la abuela está en mi bolso.", it="La chiave di Georg pesa nella mia tasca. L'amuleto di Hilde riposa sul mio petto. Il diario della nonna è nella mia borsa.")
    _t(tr,F,"voss_night_1", en="You came. Good. We have little time. Otto's men are patrolling — he has noticed that something is changing in the village.", fr="Vous êtes venue. Bien. Nous avons peu de temps. Les hommes d'Otto patrouillent — il à remarqué que quelque chose changeait dans le village.", es="Ha venido. Bien. Tenemos poco tiempo. Los hombres de Otto patrullan — ha notado que algo está cambiando en el pueblo.", it="È venuta. Bene. Abbiamo poco tempo. Gli uomini di Otto pattugliano — ha notato che qualcosa sta cambiando nel villaggio.")
    _t(tr,F,"voss_night_2", en="Voss leads me through a side door into the sacristy. There, behind a heavy curtain, lies a stone staircase leading downward.", fr="Voss me conduit par une porte latérale dans là sacristie. Là, derrière un lourd rideau, se trouve un escalier de pierre qui descend.", es="Voss me guía por una puerta lateral hasta la sacristía. Allí, detrás de una pesada cortina, hay una escalera de piedra que desciende.", it="Voss mi conduce attraverso una porta laterale nella sacrestia. Lì, dietro una pesante tenda, c'è una scala di pietra che scende.")
    _t(tr,F,"narration_alone", en="The church door is locked. But Georg's key — it fits here too. The old iron turns heavily in the lock.", fr="Là porte de l'église est verrouillée. Mais là clé de Georg — elle fonctionne ici aussi. Le vieux fer tourne lourdement dans là serrure.", es="La puerta de la iglesia está cerrada. Pero la llave de Georg — también funciona aquí. El viejo hierro gira pesadamente en la cerradura.", it="La porta della chiesa è chiusa a chiave. Ma la chiave di Georg — funziona anche qui. Il vecchio ferro gira pesantemente nella serratura.")
    _t(tr,F,"narration_alone_2", en="Alone in the dark church. My candle casts trembling shadows. Behind the altar I find the staircase leading down.", fr="Seule dans l'église obscure. Mà bougie projette des ombres tremblantes. Derrière l'autel, je trouve l'escalier qui descend.", es="Sola en la iglesia oscura. Mi vela proyecta sombras temblorosas. Detrás del altar encuentro la escalera que baja.", it="Sola nella chiesa buia. La mia candela proietta ombre tremanti. Dietro l'altare trovo la scala che scende.")
    _t(tr,F,"narration_basement_1", en="The air changes at once. Warmer, damper, sweeter. The singing is no longer faint here — it fills the room, vibrates in my bones.", fr="L'air change immédiatement. Plus chaud, plus humide, plus doux. Le chant n'est plus discret ici — il emplit là salle, vibre dans mes os.", es="El aire cambia al instante. Más cálido, más húmedo, más dulce. El canto ya no es tenue aquí — llena la sala, vibra en mis huesos.", it="L'aria cambia all'istante. Più calda, più umida, più dolce. Il canto non è più sommesso qui — riempie la stanza, vibra nelle mie ossa.")
    _t(tr,F,"narration_basement_2", en="The walls are covered with spirals. Carved, painted, branded. Layer upon layer, centuries piled atop one another. Some look like writing I cannot read.", fr="Les murs sont couverts de spirales. Gravées, peintes, marquées au fer. Couche après couche, des siècles empilés les uns sur les autres. Certaines ressemblent à une écriture que je ne peux pas lire.", es="Las paredes están cubiertas de espirales. Grabadas, pintadas, marcadas a fuego. Capa sobre capa, siglos superpuestos. Algunas parecen escritura que no puedo leer.", it="Le pareti sono coperte di spirali. Incise, dipinte, marchiate a fuoco. Strato su strato, secoli sovrapposti. Alcune sembrano una scrittura che non riesco a leggere.")
    _t(tr,F,"narration_basement_3", en="On a stone pedestal in the center of the room lies a book. It is not old — it is beyond old. The leather is from no animal I know.", fr="Sur un piédestal de pierre au centre de là salle repose un livre. Il n'est pas vieux — il est au-delà de l'ancien. Le cuir ne provient d'aucun animal que je connaisse.", es="Sobre un pedestal de piedra en el centro de la sala yace un libro. No es viejo — está más allá de lo antiguo. El cuero no es de ningún animal que yo conozca.", it="Su un piedistallo di pietra al centro della stanza giace un libro. Non è vecchio — è al di là dell'antico. La pelle non è di nessun animale che io conosca.")
    _t(tr,F,"narration_basement_4", en="I open it. Page after page of names. Hundreds of names, in different handwritings, written across centuries. Some have a date behind them. Some have a cross.", fr="Je l'ouvre. Page après page de noms. Des centaines de noms, de différentes écritures, inscrits au fil des siècles. Certains sont suivis d'une date. Certains d'une croix.", es="Lo abro. Página tras página de nombres. Cientos de nombres, en diferentes caligrafías, escritos a lo largo de siglos. Algunos tienen una fecha detrás. Algunos una cruz.", it="Lo apro. Pagina dopo pagina di nomi. Centinaia di nomi, in calligrafie diverse, scritti nel corso dei secoli. Alcuni hanno una data accanto. Alcuni una croce.")
    _t(tr,F,"narration_basement_5", en="The crosses. I count them. One every thirty years, going back until... the oldest entries are no longer writing, just symbols.", fr="Les croix. Je les compte. Une tous les trente ans, en remontant jusqu'à... les entrées les plus anciennes ne sont plus de l'écriture, juste des symboles.", es="Las cruces. Las cuento. Una cada treinta años, retrocediendo hasta... las entradas más antiguas ya no son escritura, solo símbolos.", it="Le croci. Le conto. Una ogni trent'anni, risalendo fino a... le voci più antiche non sono più scrittura, solo simboli.")
    _t(tr,F,"narration_find_name", en="And there, on the last written page: 'Elise Brandt'. In a handwriting that does not look human. The letters are too even, too perfect.", fr="Et là, sur là dernière page écrite : « Elise Brandt ». D'une écriture qui ne semble pas humaine. Les lettres sont trop régulières, trop parfaites.", es="Y ahí, en la última página escrita: «Elise Brandt». En una caligrafía que no parece humana. Las letras son demasiado uniformes, demasiado perfectas.", it="E lì, sull'ultima pagina scritta: «Elise Brandt». In una grafia che non sembra umana. Le lettere sono troppo uniformi, troppo perfette.")
    _t(tr,F,"narration_name_1", en="I touch my name on the page. The ink is warm. It pulses beneath my fingers.", fr="Je touche mon nom sur là page. L'encre est tiède. Elle pulse sous mes doigts.", es="Toco mi nombre en la página. La tinta está tibia. Pulsa bajo mis dedos.", it="Tocco il mio nome sulla pagina. L'inchiostro è caldo. Pulsa sotto le mie dita.")
    _t(tr,F,"narration_name_2", en="And then the singing stops. Complete, absolute silence. Silence that weighs heavier than any sound.", fr="Et alors le chant s'arrête. Un silence complet, absolu. Un silence qui pèse plus lourd que n'importe quel son.", es="Y entonces el canto se detiene. Silencio completo, absoluto. Un silencio que pesa más que cualquier sonido.", it="E poi il canto si ferma. Silenzio completo, assoluto. Un silenzio che pesa più di qualsiasi suono.")
    _t(tr,F,"narration_silence", en="In the silence I feel it. Not hear, not see — feel. An attention, vast as an ocean, directed at me. It is awake. It knows I am here.", fr="Dans le silence, je le sens. Pas entendre, pas voir — sentir. Une attention, vaste comme un océan, dirigée vers moi. Il est éveillé. Il sait que je suis ici.", es="En el silencio lo siento. No oír, no ver — sentir. Una atención, vasta como un océano, dirigida hacia mí. Está despierto. Sabe que estoy aquí.", it="Nel silenzio lo percepisco. Non sentire, non vedere — percepire. Un'attenzione, vasta come un oceano, rivolta verso di me. È sveglio. Sa che sono qui.")
    _tc(tr,F,"choice_book", en_choices=["Try to scratch out the name","Take the book","Back away — leave the book alone"], fr_choices=["Essayer d'effacer le nom","Prendre le livre","Reculer — laisser le livre tranquille"], es_choices=["Intentar borrar el nombre","Llevarse el libro","Retroceder — dejar el libro en paz"], it_choices=["Provare a cancellare il nome","Prendere il libro","Indietreggiare — lasciare stare il libro"])
    _t(tr,F,"erase_attempt", en="I scrape my fingernail across my name. The ink does not yield. I spit on the page, rub — nothing. As grandmother wrote: the name always comes back.", fr="Je gratte mon nom avec l'ongle. L'encre ne cède pas. Je crache sur là page, je frotte — rien. Comme grand-mère l'à écrit : le nom revient toujours.", es="Raspo mi nombre con la uña. La tinta no cede. Escupo en la página, froto — nada. Como escribió la abuela: el nombre siempre vuelve.", it="Graffio il mio nome con l'unghia. L'inchiostro non cede. Sputo sulla pagina, strofino — niente. Come ha scritto la nonna: il nome ritorna sempre.")
    _t(tr,F,"erase_3", en="The ground trembles. Dust trickles from the ceiling. The singing resumes — louder, angrier, like a swarm of hornets rising from the deep.", fr="Le sol tremble. De là poussière tombe du plafond. Le chant reprend — plus fort, plus furieux, comme un essaim de frelons montant des profondeurs.", es="El suelo tiembla. El polvo cae del techo. El canto se reanuda — más fuerte, más furioso, como un enjambre de avispones surgiendo de las profundidades.", it="Il pavimento trema. Polvere cade dal soffitto. Il canto riprende — più forte, più furioso, come uno sciame di calabroni che sale dal profondo.")
    _t(tr,F,"take_book", en="I close the book and take it. It is heavier than it looks, and warm, almost hot. As I lift it from the pedestal, the room shudders.", fr="Je ferme le livre et le prends. Il est plus lourd qu'il n'y paraît, et chaud, presque brûlant. Quand je le soulève du piédestal, là salle frémit.", es="Cierro el libro y lo tomo. Es más pesado de lo que parece, y cálido, casi ardiente. Cuando lo levanto del pedestal, la sala se estremece.", it="Chiudo il libro è lo prendo. È più pesante di quanto sembri, è caldo, quasi rovente. Quando lo sollevo dal piedistallo, la stanza trema.")
    _t(tr,F,"take_3", en="A sound — not singing, not a scream. A sigh. So vast, so deep that the stone walls vibrate. It has noticed that something is missing.", fr="Un son — pas un chant, pas un cri. Un soupir. Si vaste, si profond que les murs de pierre vibrent. Il à remarqué que quelque chose manque.", es="Un sonido — no un canto, no un grito. Un suspiro. Tan vasto, tan profundo que las paredes de piedra vibran. Ha notado que algo falta.", it="Un suono — non un canto, non un grido. Un sospiro. Così vasto, così profondo che le pareti di pietra vibrano. Ha notato che qualcosa manca.")
    _t(tr,F,"leave_book", en="I step back. My instinct tells me: the book is not meant for human hands. It belongs below, in the dark, where it was placed.", fr="Je recule. Mon instinct me dit : le livre n'est pas fait pour les mains humaines. Il appartient aux profondeurs, à l'obscurité, là où il à été déposé.", es="Retrocedo. Mi instinto me dice: el libro no es para manos humanas. Pertenece abajo, en la oscuridad, donde fue colocado.", it="Mi ritraggo. Il mio istinto mi dice: il libro non è per mani umane. Appartiene laggiù, nel buio, dove è stato posto.")
    _t(tr,F,"leave_2", en="The singing resumes gently. Almost satisfied. As if I had made the right decision — or the one it wanted.", fr="Le chant reprend doucement. Presque satisfait. Comme si j'avais pris là bonne décision — où celle qu'il voulait.", es="El canto se reanuda suavemente. Casi satisfecho. Como si hubiera tomado la decisión correcta — o la que él quería.", it="Il canto riprende dolcemente. Quasi soddisfatto. Come se avessi preso la decisione giusta — o quella che voleva lui.")
    _t(tr,F,"book_converge", en="I must get out of here. Now. The walls seem to be closing in, the spirals spinning in my peripheral vision.", fr="Je dois sortir d'ici. Maintenant. Les murs semblent se refermer, les spirales tournoient dans mà vision périphérique.", es="Tengo que salir de aquí. Ahora. Las paredes parecen estrecharse, las espirales giran en mi visión periférica.", it="Devo uscire di qui. Adesso. Le pareti sembrano stringersi, le spirali ruotano nella mia visione periferica.")
    _t(tr,F,"narration_escape", en="I stumble up the stairs, through the church, into the open air. The night air hits me like a blow. Cold. Clear. Real.", fr="Je trébuche dans les escaliers, traverse l'église, sors à l'air libre. L'air nocturne me frappe comme un coup. Froid. Clair. Réel.", es="Subo las escaleras a trompicones, cruzo la iglesia, salgo al aire libre. El aire nocturno me golpea como un puñetazo. Frío. Claro. Real.", it="Inciampo su per le scale, attraverso la chiesa, fuori all'aria aperta. L'aria notturna mi colpisce come un pugno. Fredda. Limpida. Reale.")
    _t(tr,F,"otto_encounter", en="In front of the church stands a figure in the moonlight. Broad-shouldered, motionless. Mayor Reinhardt.", fr="Devant l'église se tient une silhouette au clair de lune. Large d'épaules, immobile. Le maire Reinhardt.", es="Frente a la iglesia hay una figura a la luz de la luna. De hombros anchos, inmóvil. El alcalde Reinhardt.", it="Davanti alla chiesa c'è una figura al chiaro di luna. Spalle larghe, immobile. Il sindaco Reinhardt.")
    _t(tr,F,"otto_1", en="Fräulein Brandt. Out late. And with something that does not belong to you.", fr="Fräulein Brandt. Dehors à une heure tardive. Et avec quelque chose qui ne vous appartient pas.", es="Fräulein Brandt. Fuera a estas horas. Y con algo que no le pertenece.", it="Fräulein Brandt. In giro a quest'ora. È con qualcosa che non le appartiene.")
    _t(tr,F,"otto_3", en="Give me the book. And go home. Forget what you have seen. That is not a request.", fr="Donnez-moi le livre. Et rentrez chez vous. Oubliez ce que vous avez vu. Ce n'est pas une requête.", es="Déme el libro. Y váyase a casa. Olvide lo que ha visto. Esto no es una petición.", it="Mi dia il libro. È torni a casa. Dimentichi quello che ha visto. Questa non è una richiesta.")
    _tc(tr,F,"choice_otto", en_choices=["Give back the book","Refuse and run"], fr_choices=["Rendre le livre","Refuser et fuir"], es_choices=["Devolver el libro","Negarse y huir"], it_choices=["Restituire il libro","Rifiutare e fuggire"])
    _t(tr,F,"give_book", en="My hands tremble as I hand him the book. Otto takes it with a care that contradicts his threat. He holds it like a baby.", fr="Mes mains tremblent quand je lui tends le livre. Otto le prend avec une délicatesse qui contredit sà menace. Il le tient comme un bébé.", es="Mis manos tiemblan cuando le entrego el libro. Otto lo toma con un cuidado que contradice su amenaza. Lo sostiene como a un bebé.", it="Le mie mani tremano mentre gli porgo il libro. Otto lo prende con una cura che contraddice la sua minaccia. Lo tiene come un bambino.")
    _t(tr,F,"give_book_3", en="Sensible. Just like your grandmother. She was sensible too — in the end. Go home, Fräulein Brandt. And stay there.", fr="Raisonnable. Tout comme votre grand-mère. Elle aussi était raisonnable — à là fin. Rentrez chez vous, Fräulein Brandt. Et restez-y.", es="Sensata. Igual que su abuela. Ella también fue sensata — al final. Váyase a casa, Fräulein Brandt. Y quédese allí.", it="Ragionevole. Proprio come sua nonna. Anche lei era ragionevole — alla fine. Vada a casa, Fräulein Brandt. È ci resti.")
    _t(tr,F,"defy_otto", en="I press the book against my chest and run. Through the lanes, across the square, toward grandmother's house. Otto calls after me, but he does not pursue.", fr="Je serre le livre contre mà poitrine et je cours. Par les ruelles, à travers là place, vers là maison de grand-mère. Otto crie derrière moi, mais il ne me poursuit pas.", es="Aprieto el libro contra mi pecho y corro. Por las callejuelas, cruzando la plaza, hacia la casa de la abuela. Otto grita detrás de mí, pero no me persigue.", it="Stringo il libro al petto è corro. Per i vicoli, attraverso la piazza, verso la casa della nonna. Otto grida dietro di me, ma non mi insegue.")
    _t(tr,F,"defy_3", en="His last words echo through the night: 'That was a mistake, Fräulein Brandt. A grave mistake.'", fr="Ses derniers mots résonnent dans là nuit : « C'était une erreur, Fräulein Brandt. Une grave erreur. »", es="Sus últimas palabras resuenan en la noche: «Eso fue un error, Fräulein Brandt. Un grave error.»", it="Le sue ultime parole riecheggiano nella notte: «Questo è stato un errore, Fräulein Brandt. Un grave errore.»")
    _t(tr,F,"narration_home_1", en="Back in grandmother's house. I bolt the door, shove a chair against it. My hands are still trembling.", fr="De retour dans là maison de grand-mère. Je verrouille là porte, pousse une chaise devant. Mes mains tremblent encore.", es="De vuelta en la casa de la abuela. Echo el cerrojo, empujo una silla contra la puerta. Mis manos aún tiemblan.", it="Di nuovo nella casa della nonna. Sprangherò la porta, spingo una sedia contro di essa. Le mie mani tremano ancora.")
    _t(tr,F,"narration_home_2", en="I have seen my name. In a script no human wrote. On a page that knows no error.", fr="J'ai vu mon nom. Dans une écriture qu'aucun humain n'à tracée. Sur une page qui ne connaît aucune erreur.", es="He visto mi nombre. En una escritura que ningún humano trazó. En una página que no conoce error.", it="Ho visto il mio nome. In una scrittura che nessun umano ha vergato. Su una pagina che non conosce errore.")
    _t(tr,F,"journal_book", en="The Book of Names", fr="Le Livre des Noms", es="El Libro de los Nombres", it="Il Libro dei Nomi", field="title")
    _t(tr,F,"journal_book", en="In the chamber beneath the church lies an ancient book containing hundreds of names. Some bear a cross — the sacrificed, every 30 years. My name is the last entry, in inhuman script. The ink pulses. The entity knew I would come.", fr="Dans là chambre sous l'église se trouve un livre antique contenant des centaines de noms. Certains portent une croix — les sacrifiés, tous les 30 ans. Mon nom est là dernière entrée, en écriture inhumaine. L'encre pulse. L'entité savait que je viendrais.", es="En la cámara bajo la iglesia yace un libro antiguo con cientos de nombres. Algunos llevan una cruz — los sacrificados, cada 30 años. Mi nombre es la última entrada, en escritura inhumana. La tinta pulsa. La entidad sabía que yo vendría.", it="Nella camera sotto la chiesa giace un libro antico contenente centinaia di nomi. Alcuni recano una croce — i sacrificati, ogni 30 anni. Il mio nome è l'ultima voce, in una scrittura inumana. L'inchiostro pulsa. L'entità sapeva che sarei venuta.", field="content")
    _t(tr,F,"narration_end_1", en="I cannot sleep. The singing is louder than ever. It seeps through the walls, through the floor, through my closed eyelids.", fr="Je ne peux pas dormir. Le chant est plus fort que jamais. Il s'infiltre à travers les murs, à travers le plancher, à travers mes paupières closes.", es="No puedo dormir. El canto es más fuerte que nunca. Se filtra por las paredes, por el suelo, por mis párpados cerrados.", it="Non riesco a dormire. Il canto è più forte che mai. Filtra attraverso le pareti, attraverso il pavimento, attraverso le mie palpebre chiuse.")
    _t(tr,F,"narration_end_2", en="And in the pauses between the tones I hear words. Not German, not Latin, no language that should exist. But I understand them all the same.", fr="Et dans les pauses entre les notes, j'entends des mots. Pas de l'allemand, pas du latin, aucune langue qui devrait exister. Mais je les comprends quand même.", es="Y en las pausas entre los tonos oigo palabras. No alemán, no latín, ningún idioma que debería existir. Pero las entiendo de todos modos.", it="E nelle pause tra i toni sento parole. Non tedesco, non latino, nessuna lingua che dovrebbe esistere. Eppure le capisco lo stesso.")
    _t(tr,F,"narration_end_3", en="It says my name. Over and over and over. Elise. Elise. Elise.", fr="Il dit mon nom. Encore et encore et encore. Elise. Elise. Elise.", es="Dice mi nombre. Una y otra y otra vez. Elise. Elise. Elise.", it="Dice il mio nome. Ancora è ancora è ancora. Elise. Elise. Elise.")
    _t(tr,F,"narration_end_4", en="End of Act 2", fr="Fin de l'Acte 2", es="Fin del Acto 2", it="Fine dell'Atto 2")

    # --- Additional translations (auto-generated) ---
    _t(tr, F, "elise_inner_ready",
       en="My hands tremble. But I keep walking. Grandmother worked towards this moment for thirty years. I will not let it pass.",
       fr="Mes mains tremblent. Mais je continue d'avancer. Grand-mère a œuvré pendant trente ans pour ce moment. Je ne le laisserai pas passer.",
       es="Me tiemblan las manos. Pero sigo adelante. La abuela trabajó treinta años para este momento. No dejaré que pase en vano.",
       it="Mi tremano le mani. Ma continuo a camminare. La nonna ha lavorato trent'anni per questo momento. Non lo lascerò sfuggire.")

    _t(tr, F, "elise_voss_greet",
       en="Thank you for being here, Father. I would not have wanted to do this alone.",
       fr="Merci d'être là, mon Père. Je n'aurais pas voulu faire cela seule.",
       es="Gracias por estar aquí, padre. No habría querido hacer esto sola.",
       it="Grazie di essere qui, padre. Non avrei voluto farlo da sola.")

    _t(tr, F, "narration_voss_leads",
       en="Voss leads me through a side door into the sacristy. There, behind a heavy curtain, lies a stone staircase leading downward.",
       fr="Voss me guide par une porte latérale jusqu'à la sacristie. Là, derrière un lourd rideau, s'ouvre un escalier de pierre qui descend.",
       es="Voss me conduce por una puerta lateral hasta la sacristía. Allí, detrás de una pesada cortina, hay una escalera de piedra que desciende.",
       it="Voss mi conduce attraverso una porta laterale nella sacrestia. Lì, dietro una pesante tenda, si apre una scala di pietra che scende.")

    _t(tr, F, "elise_alone_thought",
       en="Alone. No Voss, no Georg. Just me and whatever waits beneath the church. Grandmother did it alone for thirty years. I can manage one night.",
       fr="Seule. Pas de Voss, pas de Georg. Juste moi et ce qui attend sous l'église. Grand-mère l'a fait seule pendant trente ans. Je peux tenir une nuit.",
       es="Sola. Sin Voss, sin Georg. Solo yo y lo que aguarda bajo la iglesia. La abuela lo hizo sola durante treinta años. Puedo aguantar una noche.",
       it="Sola. Niente Voss, niente Georg. Solo io e ciò che attende sotto la chiesa. La nonna l'ha fatto da sola per trent'anni. Posso farcela per una notte.")

    _t(tr, F, "elise_descent_react",
       en="Nausea rises in me. Dizziness. The amulet on my chest grows warm - as though it were working against the pressure weighing on my thoughts.",
       fr="La nausée monte en moi. Le vertige. L'amulette sur ma poitrine devient chaude - comme si elle luttait contre la pression qui pèse sur mes pensées.",
       es="La náusea me invade. Mareo. El amuleto en mi pecho se calienta, como si trabajara contra la presión que oprime mis pensamientos.",
       it="La nausea sale. Vertigini. L'amuleto sul mio petto si scalda - come se lavorasse contro la pressione che grava sui miei pensieri.")

    _t(tr, F, "elise_voss_prayer",
       en="Does it help? The praying?",
       fr="Est-ce que ça aide ? La prière ?",
       es="¿Ayuda eso? ¿El rezar?",
       it="Aiuta? Il pregare?")

    _t(tr, F, "elise_voss_understand",
       en="I understand him. Down here, where the walls breathe and the ground pulses, one needs something to anchor oneself. For Voss it is his faith. For me... Grandmother's words.",
       fr="Je le comprends. Ici, où les murs respirent et le sol palpite, on a besoin de quelque chose pour s'ancrer. Pour Voss, c'est sa foi. Pour moi... les mots de Grand-mère.",
       es="Le entiendo. Aquí abajo, donde las paredes respiran y el suelo palpita, uno necesita algo que lo ancle. Para Voss es su fe. Para mí... las palabras de la abuela.",
       it="Lo capisco. Quaggiù, dove le pareti respirano e il pavimento pulsa, si ha bisogno di qualcosa a cui ancorarsi. Per Voss è la sua fede. Per me... le parole della nonna.")

    _t(tr, F, "elise_book_first",
       en="My hands tremble as I touch it. The leather feels like... skin. Warm skin. It responds to my touch - a gentle pulsing beneath my fingertips.",
       fr="Mes mains tremblent quand je le touche. Le cuir ressemble à... de la peau. De la peau chaude. Il réagit à mon contact - une légère pulsation sous mes doigts.",
       es="Me tiemblan las manos al tocarlo. El cuero se siente como... piel. Piel cálida. Reacciona a mi contacto: un leve palpitar bajo las yemas de mis dedos.",
       it="Mi tremano le mani quando lo tocco. La pelle sembra... pelle umana. Pelle calda. Reagisce al mio tocco - un lieve pulsare sotto le punte delle dita.")

    _t(tr, F, "elise_crosses",
       en="The crosses. One every thirty years. The sacrificed. I count them and my stomach turns. So many. So many people who descended into this hole and never came back up.",
       fr="Les croix. Une tous les trente ans. Les sacrifiés. Je les compte et mon estomac se retourne. Tant de gens. Tant de gens qui sont descendus dans ce trou et n'en sont jamais remontés.",
       es="Las cruces. Una cada treinta años. Los sacrificados. Los cuento y se me revuelve el estómago. Tantos. Tantas personas que descendieron a este agujero y nunca volvieron a subir.",
       it="Le croci. Una ogni trent'anni. I sacrificati. Li conto e lo stomaco mi si rivolta. Così tanti. Così tante persone che sono scese in questo buco e non sono mai risalite.")

    _t(tr, F, "elise_grandmother_notes",
       en="Her notes. Small, neat letters: 'Friedrich Meier, 1893. Last sacrifice.' And further on: 'Konrad M. - not entered as sacrifice. Marked differently. Vessel?' Grandmother studied this book. For years.",
       fr="Ses notes. De petites lettres soignées : \"Friedrich Meier, 1893. Dernier sacrifice.\" Et plus loin : \"Konrad M. - pas inscrit comme sacrifice. Marqué différemment. Réceptacle ?\" Grand-mère a étudié ce livre. Pendant des années.",
       es="Sus notas. Letras pequeñas y pulcras: \"Friedrich Meier, 1893. Último sacrificio.\" Y más adelante: \"Konrad M. - no inscrito como sacrificio. Marcado de forma distinta. ¿Recipiente?\" La abuela estudió este libro. Durante años.",
       it="Le sue annotazioni. Lettere piccole e ordinate: \"Friedrich Meier, 1893. Ultimo sacrificio.\" E più avanti: \"Konrad M. - non registrato come sacrificio. Contrassegnato diversamente. Ricettacolo?\" La nonna ha studiato questo libro. Per anni.")

    _t(tr, F, "elise_panic_1",
       en="My name. In a script no human can write. And the ink... the ink PULSES. It lives. It breathes beneath my fingers.",
       fr="Mon nom. Dans une écriture qu'aucun humain ne peut tracer. Et l'encre... l'encre PULSE. Elle vit. Elle respire sous mes doigts.",
       es="Mi nombre. En una escritura que ningún humano puede trazar. Y la tinta... la tinta PULSA. Vive. Respira bajo mis dedos.",
       it="Il mio nome. In una scrittura che nessun umano può tracciare. E l'inchiostro... l'inchiostro PULSA. Vive. Respira sotto le mie dita.")

    _t(tr, F, "elise_panic_2",
       en="No. No, that cannot be. It must be a mistake. Someone wrote it in - Otto, Konrad, someone. But the script is not human. No human hand writes like this.",
       fr="Non. Non, c'est impossible. Ce doit être une erreur. Quelqu'un l'a écrit - Otto, Konrad, quelqu'un. Mais l'écriture n'est pas humaine. Aucune main humaine n'écrit ainsi.",
       es="No. No, no puede ser. Tiene que ser un error. Alguien lo escribió: Otto, Konrad, alguien. Pero la escritura no es humana. Ninguna mano humana escribe así.",
       it="No. No, non può essere. Dev'essere un errore. Qualcuno l'ha scritto - Otto, Konrad, qualcuno. Ma la scrittura non è umana. Nessuna mano umana scrive così.")

    _t(tr, F, "elise_panic_3",
       en="Grandmother knew. She summoned me BECAUSE my name stands in the book. Did she sacrifice me or save me? Or both?",
       fr="Grand-mère le savait. Elle m'a fait venir PARCE QUE mon nom figure dans le livre. M'a-t-elle sacrifiée ou sauvée ? Ou les deux ?",
       es="La abuela lo sabía. Me llamó PORQUE mi nombre está en el libro. ¿Me sacrificó o me salvó? ¿O ambas cosas?",
       it="La nonna lo sapeva. Mi ha chiamata PERCHÉ il mio nome è nel libro. Mi ha sacrificata o salvata? O entrambe le cose?")

    _t(tr, F, "elise_awareness",
       en="It regards me. Not with eyes - with something older. I stand naked before a consciousness that saw mountains when they were not yet mountains.",
       fr="Il me contemple. Pas avec des yeux - avec quelque chose de plus ancien. Je me tiens nue devant une conscience qui a vu les montagnes quand elles n'étaient pas encore des montagnes.",
       es="Me observa. No con ojos, con algo más antiguo. Estoy desnuda ante una conciencia que vio las montañas cuando aún no eran montañas.",
       it="Mi osserva. Non con occhi - con qualcosa di più antico. Sono nuda davanti a una coscienza che ha visto le montagne quando non erano ancora montagne.")

    _t(tr, F, "narration_before_choice",
       en="The book lies open before me. My name stares back at me. What do I do now?",
       fr="Le livre est ouvert devant moi. Mon nom me fixe. Que fais-je maintenant ?",
       es="El libro yace abierto ante mí. Mi nombre me devuelve la mirada. ¿Qué hago ahora?",
       it="Il libro giace aperto davanti a me. Il mio nome mi fissa. Cosa faccio adesso?")

    _t(tr, F, "elise_deliberate_1",
       en="If I erase the name - will I be free? Or will it only anger the creature? Grandmother wrote that the name always comes back.",
       fr="Si j'efface le nom - serai-je libre ? Ou cela ne fera-t-il qu'irriter la créature ? Grand-mère a écrit que le nom revient toujours.",
       es="Si borro el nombre, ¿seré libre? ¿O solo enfurecerá a la criatura? La abuela escribió que el nombre siempre vuelve.",
       it="Se cancello il nome - sarò libera? O renderà solo furiosa la creatura? La nonna scrisse che il nome ritorna sempre.")

    _t(tr, F, "elise_deliberate_2",
       en="If I take the book, I have proof. Control. But Otto will notice. And the creature... it will know something is missing.",
       fr="Si je prends le livre, j'ai une preuve. Du contrôle. Mais Otto s'en apercevra. Et la créature... elle saura que quelque chose manque.",
       es="Si me llevo el libro, tendré pruebas. Control. Pero Otto lo notará. Y la criatura... sabrá que algo falta.",
       it="Se prendo il libro, ho una prova. Controllo. Ma Otto se ne accorgerà. E la creatura... saprà che manca qualcosa.")

    _t(tr, F, "elise_deliberate_3",
       en="Or I leave it here. Perhaps I do not need the book. Perhaps I need the CONNECTION that my name represents.",
       fr="Ou je le laisse ici. Peut-être n'ai-je pas besoin du livre. Peut-être ai-je besoin de la CONNEXION que mon nom représente.",
       es="O lo dejo aquí. Quizá no necesite el libro. Quizá necesite la CONEXIÓN que mi nombre representa.",
       it="Oppure lo lascio qui. Forse non ho bisogno del libro. Forse ho bisogno della CONNESSIONE che il mio nome rappresenta.")

    _t(tr, F, "elise_erase_frustrate",
       en="As Grandmother wrote: the name always comes back. As though it were not ON the page, but IN it. Part of the book itself.",
       fr="Comme Grand-mère l'a écrit : le nom revient toujours. Comme s'il n'était pas SUR la page, mais EN elle. Partie intégrante du livre.",
       es="Como escribió la abuela: el nombre siempre vuelve. Como si no estuviera EN la página, sino DENTRO de ella. Parte del libro mismo.",
       it="Come scrisse la nonna: il nome ritorna sempre. Come se non fosse SULLA pagina, ma IN essa. Parte del libro stesso.")

    _t(tr, F, "elise_take_react",
       en="The book presses against my chest like a heartbeat that is not my own. But I hold it tight. It belongs to me - or I belong to it.",
       fr="Le livre presse contre ma poitrine comme un battement de cœur qui n'est pas le mien. Mais je le serre fort. Il m'appartient - ou je lui appartiens.",
       es="El libro presiona contra mi pecho como un latido que no es el mío. Pero lo sujeto con fuerza. Me pertenece, o yo le pertenezco.",
       it="Il libro preme contro il mio petto come un battito che non è il mio. Ma lo stringo forte. Appartiene a me - o io appartengo a lui.")

    _t(tr, F, "elise_leave_reason",
       en="I do not need the book. I have something better: I now know that my name is a connection. And a connection can be used - without possessing it.",
       fr="Je n'ai pas besoin du livre. J'ai quelque chose de mieux : je sais maintenant que mon nom est un lien. Et un lien peut être utilisé - sans le posséder.",
       es="No necesito el libro. Tengo algo mejor: ahora sé que mi nombre es una conexión. Y una conexión se puede usar sin poseerla.",
       it="Non ho bisogno del libro. Ho qualcosa di meglio: ora so che il mio nome è una connessione. E una connessione si può usare - senza possederla.")

    _t(tr, F, "elise_otto_react",
       en="Herr Reinhardt. How long have you been standing here?",
       fr="Herr Reinhardt. Depuis combien de temps êtes-vous là ?",
       es="Señor Reinhardt. ¿Cuánto tiempo lleva aquí?",
       it="Herr Reinhardt. Da quanto tempo è qui?")

    _t(tr, F, "elise_otto_defiant",
       en="My name stands in this book, Herr Reinhardt. In a script no human wrote. I believe I have a right to it.",
       fr="Mon nom figure dans ce livre, Herr Reinhardt. Dans une écriture qu'aucun humain n'a tracée. Je crois que j'y ai droit.",
       es="Mi nombre está en este libro, señor Reinhardt. En una escritura que ningún humano trazó. Creo que tengo derecho a él.",
       it="Il mio nome è scritto in questo libro, Herr Reinhardt. In una scrittura che nessun umano ha tracciato. Credo di averne il diritto.")

    _t(tr, F, "otto_react_name",
       en="Rights? There are no rights here, Fräulein. There is only tradition. And tradition says: every thirty years it is fed. That has worked. For centuries.",
       fr="Des droits ? Il n'y a pas de droits ici, Fräulein. Il n'y a que la tradition. Et la tradition dit : tous les trente ans, on le nourrit. Cela a fonctionné. Pendant des siècles.",
       es="¿Derechos? Aquí no hay derechos, Fräulein. Solo está la tradición. Y la tradición dice: cada treinta años se le alimenta. Ha funcionado. Durante siglos.",
       it="Diritti? Qui non esistono diritti, Fräulein. C'è solo la tradizione. E la tradizione dice: ogni trent'anni si nutre. Ha funzionato. Per secoli.")

    _t(tr, F, "elise_give_whisper",
       en="In the end. What does that mean? Was Grandmother sensible - or did Otto silence her? The thought makes me shiver.",
       fr="À la fin. Qu'est-ce que cela signifie ? Grand-mère était-elle raisonnable - ou Otto l'a-t-il réduite au silence ? Cette pensée me glace.",
       es="Al final. ¿Qué significa eso? ¿Fue la abuela sensata, o fue Otto quien la silenció? El pensamiento me hace estremecer.",
       it="Alla fine. Cosa significa? La nonna era ragionevole - oppure Otto l'ha messa a tacere? Il pensiero mi fa rabbrividire.")

    _t(tr, F, "defy_narration",
       en="I press the book against my chest and run. Through the alleys, across the square, towards Grandmother's house. Otto calls after me, but he does not give chase.",
       fr="Je serre le livre contre ma poitrine et je cours. À travers les ruelles, en traversant la place, vers la maison de Grand-mère. Otto crie derrière moi, mais il ne me poursuit pas.",
       es="Aprieto el libro contra mi pecho y echo a correr. Por los callejones, cruzando la plaza, hacia la casa de la abuela. Otto grita a mis espaldas, pero no me persigue.",
       it="Stringo il libro al petto e corro. Per i vicoli, attraverso la piazza, verso la casa della nonna. Otto grida dietro di me, ma non mi insegue.")

    _t(tr, F, "defy_4",
       en="His call echoes through the night. But I am faster than an old man. And the darkness shields me - for the first time.",
       fr="Son cri résonne dans la nuit. Mais je suis plus rapide qu'un vieil homme. Et l'obscurité me protège - pour la première fois.",
       es="Su grito resuena en la noche. Pero soy más rápida que un viejo. Y la oscuridad me protege, por primera vez.",
       it="Il suo grido echeggia nella notte. Ma sono più veloce di un vecchio. E l'oscurità mi protegge - per la prima volta.")

    _t(tr, F, "elise_home_process",
       en="I saw my name. In a script no human wrote. On a page that knows no error. And now I know for certain: I am no bystander. I am part of the story.",
       fr="J'ai vu mon nom. Dans une écriture qu'aucun humain n'a tracée. Sur une page qui ne connaît pas l'erreur. Et maintenant j'en suis certaine : je ne suis pas spectatrice. Je fais partie de l'histoire.",
       es="He visto mi nombre. En una escritura que ningún humano trazó. En una página que no conoce el error. Y ahora lo sé con certeza: no soy una espectadora. Soy parte de la historia.",
       it="Ho visto il mio nome. In una scrittura che nessun umano ha tracciato. Su una pagina che non conosce errore. E ora lo so con certezza: non sono una spettatrice. Sono parte della storia.")

    _t(tr, F, "elise_end_cover",
       en="I press my hands over my ears. It does not help. The singing does not come from outside. It comes from WITHIN. Since I touched my name, it is part of me.",
       fr="Je plaque mes mains sur mes oreilles. Ça ne sert à rien. Le chant ne vient pas de l'extérieur. Il vient de l'INTÉRIEUR. Depuis que j'ai touché mon nom, il fait partie de moi.",
       es="Me tapo los oídos con las manos. No ayuda. El canto no viene de fuera. Viene de DENTRO. Desde que toqué mi nombre, es parte de mí.",
       it="Premo le mani sulle orecchie. Non serve. Il canto non viene da fuori. Viene da DENTRO. Da quando ho toccato il mio nome, è parte di me.")


def _add_act3_allies_choice(tr):
    F = "res://data/dialogue/act3/allies_choice.json"

    _t(tr, F, "narration_1", en="Day six, afternoon. Tomorrow is the anniversary. I need help - and I must decide whom I trust.", fr="Sixième jour, après-midi. Demain, c'est l'anniversaire. J'ai besoin d'aide - et je dois décider en qui j'ai confiance.", es="Día seis, por la tarde. Mañana es el aniversario. Necesito ayuda - y debo decidir en quién confío.", it="Sesto giorno, pomeriggio. Domani è l'anniversario. Ho bisogno di aiuto - è devo decidere di chi fidarmi.")
    _t(tr, F, "narration_2", en="Georg has the key and the strength. Hilde knows the chant and the old ways. Voss knows the chamber. And Konrad... Konrad is the key to everything - or the greatest danger.", fr="Georg à là clé et là force. Hilde connaît le chant et les anciennes traditions. Voss connaît là chambre. Et Konrad... Konrad est là clé de tout - où le plus grand danger.", es="Georg tiene la llave y la fuerza. Hilde conoce el canto y los antiguos caminos. Voss conoce la cámara. Y Konrad... Konrad es la clave de todo - o el mayor peligro.", it="Georg ha la chiave è la forza. Hilde conosce il canto è le antiche usanze. Voss conosce la camera. È Konrad... Konrad è la chiave di tutto - o il pericolo più grande.")
    _tc(tr, F, "choice_primary_ally",
        en_choices=["Choose Georg as main ally - strength and loyalty", "Choose Hilde as main ally - knowledge and experience", "Choose Voss as main ally - access and remorse"],
        fr_choices=["Choisir Georg comme allié principal - force et loyauté", "Choisir Hilde comme alliée principale - savoir et expérience", "Choisir Voss comme allié principal - accès et remords"],
        es_choices=["Elegir a Georg como aliado principal - fuerza y lealtad", "Elegir a Hilde como aliada principal - conocimiento y experiencia", "Elegir a Voss como aliado principal - acceso y remordimiento"],
        it_choices=["Scegliere Georg come alleato principale - forza e lealtà", "Scegliere Hilde come alleata principale - conoscenza ed esperienza", "Scegliere Voss come alleato principale - accesso e rimorso"])
    _t(tr, F, "georg_ally_1", en="You really want to go through with it. Margarethe's ritual. I hoped you'd leave, Elise. But I also knew you'd stay.", fr="Tu veux vraiment aller jusqu'au bout. Le rituel de Margarethe. J'espérais que tu partirais, Elise. Mais je savais aussi que tu resterais.", es="Realmente quieres llevarlo a cabo. El ritual de Margarethe. Esperaba que te fueras, Elise. Pero también sabía que te quedarías.", it="Vuoi davvero portarlo a termine. Il rituale di Margarethe. Speravo che te ne andassi, Elise. Ma sapevo anche che saresti rimasta.")
    _t(tr, F, "georg_flee_callback", en="You wanted to flee, back then. That was sensible. But you stayed. That was brave. Your grandmother would be proud.", fr="Tu voulais fuir, à l'époque. C'était raisonnable. Mais tu es restée. C'était courageux. Tà grand-mère serait fière.", es="Quisiste huir, en aquel entonces. Eso era sensato. Pero te quedaste. Eso fue valiente. Tu abuela estaría orgullosa.", it="Volevi fuggire, allora. Era ragionevole. Ma sei rimasta. Quello è stato coraggioso. Tua nonna sarebbe fiera.")
    _t(tr, F, "georg_ally_3", en="I'm in. I'll stop Otto when he comes. He will come - he has men, but I have hammers. And thirty years of pent-up rage.", fr="Je suis de là partie. J'arrêterai Otto quand il viendra. Il viendrà - il à des hommes, mais moi j'ai des marteaux. Et trente ans de rage contenue.", es="Estoy contigo. Detendré a Otto cuando venga. Vendrá - él tiene hombres, pero yo tengo martillos. Y treinta años de rabia contenida.", it="Ci sto. Fermerò Otto quando verrà. Verrà - lui ha uomini, ma io ho martelli. È trent'anni di rabbia repressa.")
    _t(tr, F, "georg_ally_4", en="Georg takes a heavy blacksmith's hammer from the wall. In his eyes burns a fire I've never seen before. Perhaps the fire that has only smoldered for thirty years.", fr="Georg décroche un lourd marteau de forgeron du mur. Dans ses yeux brûle un feu que je n'ai jamais vu. Peut-être le feu qui n'à fait que couver pendant trente ans.", es="Georg toma un pesado martillo de herrero de la pared. En sus ojos arde un fuego que nunca antes he visto. Quizás el fuego que solo ha estado latente durante treinta años.", it="Georg prende un pesante martello da fabbro dalla parete. Nei suoi occhi arde un fuoco che non ho mai visto prima. Forse il fuoco che per trent'anni ha solo covato.")
    _t(tr, F, "hilde_ally_1", en="Tomorrow, then. The chant must begin at sunset, when the entity lies between sleep and waking. That's when it's most vulnerable.", fr="Demain, alors. Le chant doit commencer au coucher du soleil, quand l'entité se trouve entre sommeil et veille. C'est là qu'elle est là plus vulnérable.", es="Mañana, entonces. El canto debe comenzar al atardecer, cuando la entidad yace entre el sueño y la vigilia. Entonces es más vulnerable.", it="Domani, dunque. Il canto deve iniziare al tramonto, quando l'entità giace tra sonno è veglia. È allora che è più vulnerabile.")
    _t(tr, F, "hilde_ally_2", en="I'll help you strengthen the chant. My voice may be old, but together - perhaps it will suffice. The ancient peoples always sang in chorus.", fr="Je t'aiderai à renforcer le chant. Mà voix est peut-être vieille, mais ensemble - peut-être que celà suffira. Les anciens peuples chantaient toujours en chœur.", es="Te ayudaré a fortalecer el canto. Mi voz puede ser vieja, pero juntas - quizás sea suficiente. Los pueblos antiguos siempre cantaban en coro.", it="Ti aiuterò a rafforzare il canto. La mia voce sarà anche vecchia, ma insieme - forse basterà. Gli antichi popoli cantavano sempre in coro.")
    _t(tr, F, "hilde_ally_3", en="Hilde begins tying bundles of herbs together and painting signs on strips of cloth. She murmurs the chant softly as she works. The air in the cottage thickens.", fr="Hilde commence à lier des bouquets d'herbes et à peindre des signes sur des bandes de tissu. Elle murmure doucement le chant en travaillant. L'air dans là cabane s'épaissit.", es="Hilde comienza a atar manojos de hierbas y a pintar signos en tiras de tela. Murmura suavemente el canto mientras trabaja. El aire en la cabaña se espesa.", it="Hilde comincia a legare fasci di erbe è a dipingere segni su strisce di stoffa. Mormora piano il canto mentre lavora. L'aria nella capanna si addensa.")
    _t(tr, F, "voss_ally_1", en="Thirty years I have kept silent. Thirty years I have stood by and watched. That ends tomorrow.", fr="Trente ans j'ai gardé le silence. Trente ans j'ai regardé sans rien faire. Celà prend fin demain.", es="Treinta años he callado. Treinta años he observado sin hacer nada. Eso termina mañana.", it="Trent'anni ho taciuto. Trent'anni ho osservato senza fare nulla. Questo finisce domani.")
    _t(tr, F, "voss_confronted_callback", en="You asked me in the church what I knew about the Feeding. I didn't say everything then. But now - I owe you the full truth. And I owe Friedrich Meier more than that.", fr="Vous m'avez demandé à l'église ce que je savais sur là Nourriture. Je n'ai pas tout dit à l'époque. Mais maintenant - je vous dois l'entière vérité. Et je dois plus que celà à Friedrich Meier.", es="Usted me preguntó en la iglesia qué sabía sobre la Alimentación. No dije todo entonces. Pero ahora - le debo toda la verdad. Y a Friedrich Meier le debo más que eso.", it="Lei mi ha chiesto in chiesa cosa sapessi sulla Nutrizione. Non ho detto tutto allora. Ma adesso - Le devo l'intera verità. È a Friedrich Meier devo più di questo.")
    _t(tr, F, "voss_ally_3", en="I know every stone in that chamber. I know where the traps are, where the ground is thin, where the singing grows loudest. I will guide you.", fr="Je connais chaque pierre de cette chambre. Je sais où sont les pièges, où le sol est mince, où le chant devient le plus fort. Je vous guiderai.", es="Conozco cada piedra de esa cámara. Sé dónde están las trampas, dónde el suelo es delgado, dónde el canto se vuelve más fuerte. La guiaré.", it="Conosco ogni pietra di quella camera. So dove sono le trappole, dove il suolo è sottile, dove il canto diventa più forte. La guiderò.")
    _t(tr, F, "voss_ally_4", en="And if it goes wrong... then I go first. I owe that to Friedrich Meier. I owe that to everyone.", fr="Et si celà tourne mal... alors j'irai en premier. Je le dois à Friedrich Meier. Je le dois à tous.", es="Y si sale mal... entonces yo iré primero. Se lo debo a Friedrich Meier. Se lo debo a todos.", it="E se va storto... allora vado per primo. Lo devo a Friedrich Meier. Lo devo a tutti.")
    _t(tr, F, "ally_converge", en="I have an ally. But is it enough? Evening falls, and with it the world grows stranger still.", fr="J'ai un allié. Mais est-ce suffisant ? Le soir tombe, et avec lui le monde devient plus étrange encore.", es="Tengo un aliado. Pero ¿es suficiente? Cae la noche, y con ella el mundo se vuelve aún más extraño.", it="Ho un alleato. Ma basta? Scende la sera, è con essa il mondo si fa ancora più strano.")
    _tc(tr, F, "choice_konrad_final",
        en_choices=["Seek out Konrad - perhaps he can resist the entity", "Avoid Konrad - he is too dangerous"],
        fr_choices=["Aller voir Konrad - peut-être peut-il résister à l'entité", "Éviter Konrad - il est trop dangereux"],
        es_choices=["Buscar a Konrad - quizás pueda resistir a la entidad", "Evitar a Konrad - es demasiado peligroso"],
        it_choices=["Cercare Konrad - forse può resistere all'entità", "Evitare Konrad - è troppo pericoloso"])
    _t(tr, F, "konrad_final_1", en="Konrad sits alone in the classroom. He has drawn spirals on the blackboard - dozens, intertwined. When I enter, he hastily wipes them away.", fr="Konrad est assis seul dans là salle de classe. Il à dessiné des spirales au tableau - des dizaines, entrelacées. Quand j'entre, il les efface précipitamment.", es="Konrad está sentado solo en el aula. Ha dibujado espirales en la pizarra - docenas, entrelazadas. Cuando entro, las borra apresuradamente.", it="Konrad siede da solo nell'aula. Ha disegnato spirali sulla lavagna - dozzine, intrecciate. Quando entro, le cancella in fretta.")
    _t(tr, F, "konrad_final_2", en="Elise. I... it's getting worse. I'm losing myself. At night I wake up in places I never went to. My hands do things I don't want.", fr="Elise. Je... çà empire. Je me perds. Là nuit, je me réveille dans des endroits où je ne suis jamais allé. Mes mains font des choses que je ne veux pas.", es="Elise. Yo... está empeorando. Me estoy perdiendo. Por las noches despierto en lugares a los que nunca fui. Mis manos hacen cosas que no quiero.", it="Elise. Io... sta peggiorando. Mi sto perdendo. Di notte mi sveglio in posti dove non sono mai andato. Le mie mani fanno cose che non voglio.")
    _t(tr, F, "konrad_final_4", en="His eyes flicker - brown, then something else, deeper, older. For a moment I see something immense behind his pupils, like an ocean behind a pane of glass.", fr="Ses yeux vacillent - bruns, puis autre chose, plus profond, plus ancien. Pendant un instant, je vois quelque chose d'immense derrière ses pupilles, comme un océan derrière une vitre.", es="Sus ojos parpadean - marrones, luego algo más, más profundo, más antiguo. Por un instante veo algo inmenso detrás de sus pupilas, como un océano detrás de un cristal.", it="I suoi occhi tremolano - marroni, poi qualcos'altro, più profondo, più antico. Per un momento vedo qualcosa di immenso dietro le sue pupille, come un oceano dietro un vetro.")
    _t(tr, F, "konrad_final_6", en="Help me, Elise. Please. Before it has me completely. I don't want to be its tool.", fr="Aide-moi, Elise. S'il te plaît. Avant qu'il ne me possède entièrement. Je ne veux pas être son instrument.", es="Ayúdame, Elise. Por favor. Antes de que me tenga por completo. No quiero ser su instrumento.", it="Aiutami, Elise. Ti prego. Prima che mi abbia completamente. Non voglio essere il suo strumento.")
    _t(tr, F, "avoided_konrad", en="Konrad is no longer Konrad. Not entirely. I can't risk the entity learning of my plan through him.", fr="Konrad n'est plus Konrad. Pas entièrement. Je ne peux pas risquer que l'entité apprenne mon plan à travers lui.", es="Konrad ya no es Konrad. No del todo. No puedo arriesgarme a que la entidad descubra mi plan a través de él.", it="Konrad non è più Konrad. Non del tutto. Non posso rischiare che l'entità scopra il mio piano attraverso di lui.")
    _t(tr, F, "ally_final_converge", en="Allies Chosen", fr="Alliés choisis", es="Aliados elegidos", it="Alleati scelti", field="title")
    _t(tr, F, "ally_final_converge", en="Tomorrow is the day of the Feeding. I have chosen my allies and discussed the plan. Grandmother's binding ritual instead of the blood ritual. Anna says the entity is afraid of me. That makes two of us.", fr="Demain est le jour de là Nourriture. J'ai choisi mes alliés et discuté du plan. Le rituel de liaison de grand-mère au lieu du rituel de sang. Annà dit que l'entité à peur de moi. Celà fait deux d'entre nous.", es="Mañana es el día de la Alimentación. He elegido a mis aliados y discutido el plan. El ritual de vinculación de la abuela en lugar del ritual de sangre. Anna dice que la entidad me tiene miedo. Eso nos hace dos.", it="Domani è il giorno della Nutrizione. Ho scelto i miei alleati è discusso il piano. Il rituale di legame della nonna al posto del rituale di sangue. Anna dice che l'entità ha paura di me. Questo fa due di noi.", field="content")

    # --- Additional translations (auto-generated) ---
    _t(tr, F, "elise_assess",
       en="Georg has the key and the strength. Hilde knows the chant and the old ways. Voss knows the chamber and carries thirty years of guilt. And Konrad... Konrad is the key to everything - or the greatest danger.",
       fr="Georg a la clef et la force. Hilde conna\u00eet le chant et les anciennes voies. Voss conna\u00eet la chambre et porte trente ans de culpabilit\u00e9. Et Konrad... Konrad est la clef de tout - ou le plus grand danger.",
       es="Georg tiene la llave y la fuerza. Hilde conoce el canto y los antiguos caminos. Voss conoce la c\u00e1mara y carga con treinta a\u00f1os de culpa. Y Konrad... Konrad es la clave de todo, o el mayor peligro.",
       it="Georg ha la chiave e la forza. Hilde conosce il canto e le antiche vie. Voss conosce la camera e porta trent'anni di colpa. E Konrad... Konrad \u00e8 la chiave di tutto, o il pericolo pi\u00f9 grande.")
    _t(tr, F, "elise_decide",
       en="I cannot confide in all of them at once. Otto has eyes everywhere. One must be my primary ally - the one I rely on tomorrow night.",
       fr="Je ne peux pas tous les mettre dans la confidence en m\u00eame temps. Otto a des yeux partout. L'un d'eux doit \u00eatre mon alli\u00e9 principal - celui sur qui je compterai demain soir.",
       es="No puedo confiar en todos a la vez. Otto tiene ojos en todas partes. Uno debe ser mi aliado principal, aquel en quien conf\u00ede ma\u00f1ana por la noche.",
       it="Non posso confidarmi con tutti contemporaneamente. Otto ha occhi ovunque. Uno deve essere il mio alleato principale - quello su cui conter\u00f2 domani notte.")
    _t(tr, F, "elise_georg_1",
       en="Leaving was never really an option. Not since I saw my name in that book.",
       fr="Partir n'a jamais vraiment \u00e9t\u00e9 une option. Pas depuis que j'ai vu mon nom dans ce livre.",
       es="Irme nunca fue realmente una opci\u00f3n. No desde que vi mi nombre en ese libro.",
       it="Andarsene non \u00e8 mai stata davvero un'opzione. Non da quando ho visto il mio nome in quel libro.")
    _t(tr, F, "elise_georg_flee",
       en="The forest would not let me. But even if it had... I believe I would have come back.",
       fr="La for\u00eat ne m'a pas laiss\u00e9e partir. Mais m\u00eame si elle l'avait fait... je crois que je serais revenue.",
       es="El bosque no me dej\u00f3. Pero incluso si lo hubiera hecho... creo que habr\u00eda vuelto.",
       it="La foresta non me lo ha permesso. Ma anche se lo avesse fatto... credo che sarei tornata.")
    _t(tr, F, "elise_georg_question",
       en="Georg, what happens if I fail? What happens to you, to Graubach?",
       fr="Georg, que se passe-t-il si j'\u00e9choue ? Qu'adviendra-t-il de vous, de Graubach ?",
       es="Georg, \u00bfqu\u00e9 pasa si fracaso? \u00bfQu\u00e9 ser\u00e1 de ti, de Graubach?",
       it="Georg, cosa succede se fallisco? Cosa succede a te, a Graubach?")
    _t(tr, F, "georg_ally_answer",
       en="Then it was all for nothing. Thirty years. Margarethe's sacrifice. My guilt.",
       fr="Alors tout aura \u00e9t\u00e9 pour rien. Trente ans. Le sacrifice de Margarethe. Ma culpabilit\u00e9.",
       es="Entonces todo habr\u00e1 sido en vano. Treinta a\u00f1os. El sacrificio de Margarethe. Mi culpa.",
       it="Allora sar\u00e0 stato tutto inutile. Trent'anni. Il sacrificio di Margarethe. La mia colpa.")
    _t(tr, F, "elise_georg_risk",
       en="And you? What are you risking? You could flee - you are not in the book.",
       fr="Et vous ? Que risquez-vous ? Vous pourriez fuir - vous n'\u00eates pas dans le livre.",
       es="Y t\u00fa, \u00bfqu\u00e9 arriesgas? Podr\u00edas huir, t\u00fa no est\u00e1s en el libro.",
       it="E tu? Cosa rischi? Potresti fuggire - tu non sei nel libro.")
    _t(tr, F, "elise_georg_otto",
       en="Otto has men. What if they are armed?",
       fr="Otto a des hommes. Et s'ils sont arm\u00e9s ?",
       es="Otto tiene hombres. \u00bfY si est\u00e1n armados?",
       it="Otto ha degli uomini. E se sono armati?")
    _t(tr, F, "georg_ally_hammer",
       en="Georg takes a heavy blacksmith's hammer from the wall. In his eyes burns a fire I have never seen before.",
       fr="Georg d\u00e9croche un lourd marteau de forge du mur. Dans ses yeux br\u00fble un feu que je n'ai encore jamais vu.",
       es="Georg toma un pesado martillo de herrero de la pared. En sus ojos arde un fuego que nunca antes hab\u00eda visto.",
       it="Georg prende un pesante martello da fabbro dalla parete. Nei suoi occhi brucia un fuoco che non ho mai visto prima.")
    _t(tr, F, "elise_georg_grateful",
       en="Thank you, Georg. Grandmother could not have wished for a better ally.",
       fr="Merci, Georg. Grand-m\u00e8re n'aurait pu souhaiter meilleur alli\u00e9.",
       es="Gracias, Georg. La abuela no podr\u00eda haber deseado un mejor aliado.",
       it="Grazie, Georg. La nonna non avrebbe potuto desiderare un alleato migliore.")
    _t(tr, F, "elise_hilde_1",
       en="Hilde, the chant... I cannot do it alone. When I tried it at your cottage, my voice was barely enough.",
       fr="Hilde, le chant... je n'y arriverai pas seule. Quand j'ai essay\u00e9 chez vous, ma voix suffisait \u00e0 peine.",
       es="Hilde, el canto... no puedo hacerlo sola. Cuando lo intent\u00e9 en su caba\u00f1a, mi voz apenas alcanzaba.",
       it="Hilde, il canto... non ce la faccio da sola. Quando l'ho provato nella sua capanna, la mia voce bastava a malapena.")
    _t(tr, F, "elise_hilde_chance",
       en="What if the creature does not accept the chant? What if it is not enough?",
       fr="Et si la cr\u00e9ature n'accepte pas le chant ? Et si cela ne suffit pas ?",
       es="\u00bfY si la criatura no acepta el canto? \u00bfY si no es suficiente?",
       it="E se la creatura non accetta il canto? E se non basta?")
    _t(tr, F, "hilde_ally_improvise",
       en="Then we improvise. As your grandmother would have done. Margarethe never gave up - and neither shall we.",
       fr="Alors nous improviserons. Comme votre grand-m\u00e8re l'aurait fait. Margarethe n'a jamais abandonn\u00e9 - et nous non plus.",
       es="Entonces improvisaremos. Como lo habr\u00eda hecho tu abuela. Margarethe nunca se rindi\u00f3, y nosotras tampoco lo haremos.",
       it="Allora improvviseremo. Come avrebbe fatto tua nonna. Margarethe non si \u00e8 mai arresa, e nemmeno noi lo faremo.")
    _t(tr, F, "hilde_ally_personal",
       en="Hilde takes my hands. Her fingers are rough and warm, full of life despite her age.",
       fr="Hilde prend mes mains. Ses doigts sont rugueux et chauds, pleins de vie malgr\u00e9 son \u00e2ge.",
       es="Hilde toma mis manos. Sus dedos son \u00e1speros y c\u00e1lidos, llenos de vida a pesar de su edad.",
       it="Hilde prende le mie mani. Le sue dita sono ruvide e calde, piene di vita nonostante la sua et\u00e0.")
    _t(tr, F, "hilde_ally_hands",
       en="You are more like her than you think, child. The same stubbornness. The same kindness. And the same fear she never admitted to.",
       fr="Tu lui ressembles plus que tu ne le crois, mon enfant. La m\u00eame obstination. La m\u00eame bont\u00e9. Et la m\u00eame peur qu'elle n'a jamais avou\u00e9e.",
       es="Te pareces a ella m\u00e1s de lo que crees, ni\u00f1a. La misma terquedad. La misma bondad. Y el mismo miedo que ella nunca admiti\u00f3.",
       it="Le assomigli pi\u00f9 di quanto credi, bambina. La stessa testardaggine. La stessa bont\u00e0. E la stessa paura che lei non ha mai ammesso.")
    _t(tr, F, "hilde_ally_truth",
       en="Of course she was afraid. Every night. But she used the fear - as fuel. You can do the same.",
       fr="Bien s\u00fbr qu'elle avait peur. Chaque nuit. Mais elle a utilis\u00e9 la peur - comme combustible. Tu peux faire de m\u00eame.",
       es="Por supuesto que ten\u00eda miedo. Cada noche. Pero us\u00f3 el miedo como combustible. T\u00fa tambi\u00e9n puedes hacerlo.",
       it="Certo che aveva paura. Ogni notte. Ma ha usato la paura come combustibile. Puoi farlo anche tu.")
    _t(tr, F, "elise_voss_1",
       en="Pastor Voss, you have suffered under guilt for thirty years. That is enough.",
       fr="Pasteur Voss, vous avez souffert sous le poids de la culpabilit\u00e9 pendant trente ans. Cela suffit.",
       es="Pastor Voss, ha sufrido bajo la culpa durante treinta a\u00f1os. Ya es suficiente.",
       it="Pastore Voss, ha sofferto sotto il peso della colpa per trent'anni. Basta cos\u00ec.")
    _t(tr, F, "voss_reacts",
       en="Nothing is ever enough. Not for Friedrich Meier. Not for all the others.",
       fr="Rien ne suffit jamais. Pas pour Friedrich Meier. Pas pour tous les autres.",
       es="Nada es nunca suficiente. No para Friedrich Meier. No para todos los dem\u00e1s.",
       it="Niente \u00e8 mai abbastanza. Non per Friedrich Meier. Non per tutti gli altri.")
    _t(tr, F, "elise_voss_lead",
       en="Then help me end it. Not for the guilt - for the future. So that no one is ever sacrificed again.",
       fr="Alors aidez-moi \u00e0 y mettre fin. Pas pour la culpabilit\u00e9 - pour l'avenir. Pour que plus jamais personne ne soit sacrifi\u00e9.",
       es="Entonces ay\u00fademe a terminarlo. No por la culpa, sino por el futuro. Para que nunca m\u00e1s nadie sea sacrificado.",
       it="Allora mi aiuti a porvi fine. Non per la colpa - per il futuro. Perch\u00e9 nessuno venga mai pi\u00f9 sacrificato.")
    _t(tr, F, "voss_confession",
       en="Friedrich screamed. All night. And I... I prayed instead of helping him. I spoke my prayers louder than his screams. I will never forgive myself for that.",
       fr="Friedrich a cri\u00e9. Toute la nuit. Et moi... j'ai pri\u00e9 au lieu de l'aider. J'ai r\u00e9cit\u00e9 mes pri\u00e8res plus fort que ses cris. Je ne me le pardonnerai jamais.",
       es="Friedrich grit\u00f3. Toda la noche. Y yo... rec\u00e9 en lugar de ayudarlo. Rec\u00e9 m\u00e1s fuerte que sus gritos. Nunca me lo perdonar\u00e9.",
       it="Friedrich ha urlato. Tutta la notte. E io... ho pregato invece di aiutarlo. Ho recitato le mie preghiere pi\u00f9 forte delle sue urla. Non me lo perdoner\u00f2 mai.")
    _t(tr, F, "elise_voss_forgive",
       en="You cannot undo it. But you can make sure it was the last time.",
       fr="Vous ne pouvez pas d\u00e9faire ce qui a \u00e9t\u00e9 fait. Mais vous pouvez faire en sorte que ce soit la derni\u00e8re fois.",
       es="No puede deshacerlo. Pero puede asegurarse de que fue la \u00faltima vez.",
       it="Non pu\u00f2 cancellare quello che \u00e8 stato. Ma pu\u00f2 fare in modo che sia stata l'ultima volta.")
    _t(tr, F, "elise_voss_risk",
       en="What if Otto stops us? He controls the village.",
       fr="Et si Otto nous arr\u00eate ? Il contr\u00f4le le village.",
       es="\u00bfY si Otto nos detiene? \u00c9l controla el pueblo.",
       it="E se Otto ci ferma? Lui controlla il villaggio.")
    _t(tr, F, "elise_voss_no",
       en="No one has to die, Pastor. Not you, not I. That is what we are doing this for.",
       fr="Personne ne doit mourir, Pasteur. Ni vous, ni moi. C'est pour cela que nous faisons tout ceci.",
       es="Nadie tiene que morir, Pastor. Ni usted, ni yo. Para eso hacemos esto.",
       it="Nessuno deve morire, Pastore. N\u00e9 lei, n\u00e9 io. \u00c8 per questo che lo facciamo.")
    _t(tr, F, "elise_konrad_consider",
       en="But then there is Konrad. The vessel. The man caught between himself and the creature. Can he help me - or will he betray me?",
       fr="Mais il y a aussi Konrad. Le r\u00e9ceptacle. L'homme prisonnier entre lui-m\u00eame et la cr\u00e9ature. Peut-il m'aider - ou me trahira-t-il ?",
       es="Pero luego est\u00e1 Konrad. El recipiente. El hombre atrapado entre s\u00ed mismo y la criatura. \u00bfPuede ayudarme, o me traicionar\u00e1?",
       it="Ma poi c'\u00e8 Konrad. Il ricettacolo. L'uomo intrappolato tra s\u00e9 stesso e la creatura. Pu\u00f2 aiutarmi, o mi tradir\u00e0?")
    _t(tr, F, "elise_konrad_enter",
       en="Konrad. How are you?",
       fr="Konrad. Comment allez-vous ?",
       es="Konrad. \u00bfC\u00f3mo est\u00e1s?",
       it="Konrad. Come stai?")
    _t(tr, F, "elise_konrad_concern",
       en="When did you last sleep? Truly sleep?",
       fr="Quand avez-vous dormi pour la derni\u00e8re fois ? Vraiment dormi ?",
       es="\u00bfCu\u00e1ndo dormiste por \u00faltima vez? \u00bfDormiste de verdad?",
       it="Quando hai dormito l'ultima volta? Dormito davvero?")
    _t(tr, F, "konrad_final_sleep",
       en="I do not know anymore. The nights blur together. Sometimes I do not know if I am awake or dreaming. Whether it is ME thinking or IT.",
       fr="Je ne sais plus. Les nuits se confondent. Parfois je ne sais plus si je suis \u00e9veill\u00e9 ou si je r\u00eave. Si c'est MOI qui pense ou si c'est LUI.",
       es="Ya no lo s\u00e9. Las noches se confunden. A veces no s\u00e9 si estoy despierto o so\u00f1ando. Si soy YO quien piensa o si es ELLO.",
       it="Non lo so pi\u00f9. Le notti si confondono. A volte non so se sono sveglio o se sto sognando. Se sono IO a pensare o se \u00e8 LUI.")
    _t(tr, F, "konrad_creature_voice",
       en="Elise... it is HERE... it speaks through me... I cannot...",
       fr="Elise... c'est ICI... \u00e7a parle \u00e0 travers moi... je ne peux pas...",
       es="Elise... est\u00e1 AQU\u00cd... habla a trav\u00e9s de m\u00ed... no puedo...",
       it="Elise... \u00e8 QUI... parla attraverso di me... non riesco...")
    _t(tr, F, "elise_konrad_reach",
       en="Konrad! Listen to my voice. YOU are Konrad M\u00fcller. You are a teacher. You learned to read from Grandmother.",
       fr="Konrad ! \u00c9coutez ma voix. VOUS \u00eates Konrad M\u00fcller. Vous \u00eates instituteur. Vous avez appris \u00e0 lire avec Grand-m\u00e8re.",
       es="\u00a1Konrad! Escucha mi voz. T\u00da eres Konrad M\u00fcller. Eres maestro. Aprendiste a leer con la abuela.",
       it="Konrad! Ascolta la mia voce. TU sei Konrad M\u00fcller. Sei un insegnante. Hai imparato a leggere dalla nonna.")
    _t(tr, F, "elise_konrad_promise",
       en="I will free you, Konrad. Or at least try. I promise.",
       fr="Je vous lib\u00e9rerai, Konrad. Ou du moins j'essaierai. Je vous le promets.",
       es="Te liberar\u00e9, Konrad. O al menos lo intentar\u00e9. Te lo prometo.",
       it="Ti liberer\u00f2, Konrad. O almeno ci prover\u00f2. Te lo prometto.")
    _t(tr, F, "konrad_final_hope",
       en="A faint smile. The first genuine smile I have seen from him - not charming, not seductive. Only grateful. Only human.",
       fr="Un faible sourire. Le premier sourire sinc\u00e8re que je lui vois - pas charmeur, pas s\u00e9ducteur. Simplement reconnaissant. Simplement humain.",
       es="Una d\u00e9bil sonrisa. La primera sonrisa genuina que le he visto, no encantadora, no seductora. Solo agradecida. Solo humana.",
       it="Un debole sorriso. Il primo sorriso genuino che gli ho visto - non affascinante, non seducente. Solo grato. Solo umano.")
    _t(tr, F, "elise_konrad_regret",
       en="I am sorry, Konrad. Perhaps I can help you when this is over. But now... now I must avoid you. For your own protection.",
       fr="Je suis d\u00e9sol\u00e9e, Konrad. Peut-\u00eatre pourrai-je vous aider quand tout sera fini. Mais maintenant... maintenant je dois vous \u00e9viter. Pour votre propre protection.",
       es="Lo siento, Konrad. Quiz\u00e1s pueda ayudarte cuando esto termine. Pero ahora... ahora debo evitarte. Por tu propia protecci\u00f3n.",
       it="Mi dispiace, Konrad. Forse potr\u00f2 aiutarti quando tutto sar\u00e0 finito. Ma ora... ora devo evitarti. Per la tua stessa protezione.")
    _t(tr, F, "elise_final_thought",
       en="Tomorrow is the day. Tomorrow I stand in the chamber, above the thinnest stone, and sing the chant Hilde taught me. And the creature will answer.",
       fr="Demain est le jour. Demain je me tiendrai dans la chambre, au-dessus de la pierre la plus fine, et je chanterai le chant que Hilde m'a enseign\u00e9. Et la cr\u00e9ature r\u00e9pondra.",
       es="Ma\u00f1ana es el d\u00eda. Ma\u00f1ana me situar\u00e9 en la c\u00e1mara, sobre la piedra m\u00e1s fina, y cantar\u00e9 el canto que Hilde me ense\u00f1\u00f3. Y la criatura responder\u00e1.",
       it="Domani \u00e8 il giorno. Domani star\u00f2 nella camera, sopra la pietra pi\u00f9 sottile, e canter\u00f2 il canto che Hilde mi ha insegnato. E la creatura risponder\u00e0.")
    _t(tr, F, "journal_allies",
       en="Allies Chosen",
       fr="Alli\u00e9s choisis",
       es="Aliados elegidos",
       it="Alleati scelti",
       field="title")
    _t(tr, F, "journal_allies",
       en="Tomorrow is the day of the feeding. I have chosen my allies and discussed the plan. Grandmother's binding ritual instead of the blood ritual. Anna says the creature is afraid of me. That makes two of us.",
       fr="Demain est le jour de la nourriture. J'ai choisi mes alli\u00e9s et discut\u00e9 du plan. Le rituel de liaison de Grand-m\u00e8re au lieu du rituel de sang. Anna dit que la cr\u00e9ature a peur de moi. Cela fait deux d'entre nous.",
       es="Ma\u00f1ana es el d\u00eda de la alimentaci\u00f3n. He elegido a mis aliados y discutido el plan. El ritual de atadura de la abuela en lugar del ritual de sangre. Anna dice que la criatura me tiene miedo. Eso nos hace dos.",
       it="Domani \u00e8 il giorno del nutrimento. Ho scelto i miei alleati e discusso il piano. Il rituale di legamento della nonna al posto del rituale di sangue. Anna dice che la creatura ha paura di me. Questo fa due di noi.",
       field="content")


def _add_act3_reality_breaks(tr):
    F = "res://data/dialogue/act3/reality_breaks.json"

    _t(tr, F, "narration_1", en="Day six. Something is different. When I look out the window, the colors are wrong. The sky is too violet for morning. The shadows fall in the wrong direction.", fr="Sixième jour. Quelque chose est différent. Quand je regarde par là fenêtre, les couleurs ne correspondent pas. Le ciel est trop violet pour le matin. Les ombres tombent dans là mauvaise direction.", es="Día seis. Algo es diferente. Cuando miro por la ventana, los colores no son correctos. El cielo es demasiado violeta para la mañana. Las sombras caen en la dirección equivocada.", it="Sesto giorno. Qualcosa è diverso. Quando guardo fuori dalla finestra, i colori sono sbagliati. Il cielo è troppo violetto per il mattino. Le ombre cadono nella direzione sbagliata.")
    _t(tr, F, "narration_2", en="In the mirror I see myself. But my reflection blinks half a second later than I do.", fr="Dans le miroir, je me vois. Mais mon reflet cligne des yeux une demi-seconde après moi.", es="En el espejo me veo a mí misma. Pero mi reflejo parpadea medio segundo después que yo.", it="Nello specchio vedo me stessa. Ma il mio riflesso sbatte le palpebre mezzo secondo dopo di me.")
    _t(tr, F, "narration_3", en="I turn away. This is what grandmother described: 'The dreams seep upward.' Reality is growing thin.", fr="Je me détourne. C'est ce que grand-mère décrivait : « Les rêves suintent vers le haut. » Là réalité s'amincit.", es="Me doy la vuelta. Esto es lo que la abuela describía: «Los sueños se filtran hacia arriba.» La realidad se vuelve delgada.", it="Mi volto. È quello che la nonna descriveva: 'I sogni filtrano verso l'alto.' La realtà si assottiglia.")
    _t(tr, F, "narration_4", en="The village outside is... wrong. The houses stand at slightly shifted angles, as if someone moved them overnight. The fountain in the square drips upward.", fr="Le village dehors est... faux. Les maisons se dressent à des angles légèrement décalés, comme si quelqu'un les avait déplacées pendant là nuit. Là fontaine sur là place goutte vers le haut.", es="El pueblo afuera está... mal. Las casas se alzan en ángulos ligeramente desplazados, como si alguien las hubiera movido durante la noche. La fuente de la plaza gotea hacia arriba.", it="Il villaggio fuori è... sbagliato. Le case si ergono ad angoli leggermente spostati, come se qualcuno le avesse spostate durante la notte. La fontana nella piazza gocciola verso l'alto.")
    _t(tr, F, "narration_5", en="The villagers go about their business as if nothing were amiss. Only their eyes - all gazing in the same direction. Toward the church.", fr="Les villageois vaquent à leurs occupations comme si de rien n'était. Seuls leurs yeux - tous regardent dans là même direction. Vers l'église.", es="Los aldeanos hacen sus cosas como si nada pasara. Solo sus ojos - todos miran en la misma dirección. Hacia la iglesia.", it="I paesani svolgono le loro faccende come se nulla fosse. Solo i loro occhi - tutti guardano nella stessa direzione. Verso la chiesa.")
    _t(tr, F, "narration_6", en="I must act. The day after tomorrow is the thirtieth anniversary of the last Feeding. If the ritual takes place, someone dies. If it doesn't...", fr="Je dois agir. Après-demain marque le trentième anniversaire de là dernière Nourriture. Si le rituel à lieu, quelqu'un meurt. S'il n'à pas lieu...", es="Debo actuar. Pasado mañana es el trigésimo aniversario de la última Alimentación. Si el ritual se lleva a cabo, alguien muere. Si no se lleva a cabo...", it="Devo agire. Dopodomani è il trentesimo anniversario dell'ultima Nutrizione. Se il rituale ha luogo, qualcuno muore. Se non ha luogo...")
    _t(tr, F, "narration_7", en="Then it wakes up. Completely. And no one knows what happens then.", fr="Alors il se réveille. Complètement. Et personne ne sait ce qui se passe ensuite.", es="Entonces despierta. Completamente. Y nadie sabe qué pasará después.", it="Allora si sveglia. Completamente. È nessuno sa cosa succederà dopo.")
    _t(tr, F, "nightmare_intro", en="Suddenly I feel dizzy. The world tilts. I reach for the doorframe, but it's no longer there.", fr="Soudain, j'ai le vertige. Le monde bascule. Je m'agrippe au chambranle de là porte, mais il n'est plus là.", es="De repente me mareo. El mundo se inclina. Me agarro al marco de la puerta, pero ya no está ahí.", it="Improvvisamente mi viene un capogiro. Il mondo si inclina. Mi aggrappo allo stipite della porta, ma non c'è più.")
    _t(tr, F, "nightmare_1", en="I stand in the chamber. No - I am DREAMING the chamber. The spirals on the walls are turning, and at their center I see a face. Immense, ancient, formed of stone and darkness.", fr="Je me tiens dans là chambre. Non - je RÊVE là chambre. Les spirales sur les murs tournent, et en leur centre je vois un visage. Immense, ancien, formé de pierre et de ténèbres.", es="Estoy en la cámara. No - estoy SOÑANDO la cámara. Las espirales en las paredes giran, y en su centro veo un rostro. Inmenso, antiguo, formado de piedra y oscuridad.", it="Sono nella camera. No - sto SOGNANDO la camera. Le spirali sulle pareti ruotano, è al loro centro vedo un volto. Immenso, antico, plasmato di pietra è oscurità.")
    _t(tr, F, "nightmare_3", en="It does not speak. It needs no words. I FEEL its question: Why are you here? What do you want?", fr="Il ne parle pas. Il n'à pas besoin de mots. Je RESSENS sà question : Pourquoi es-tu ici ? Que veux-tu ?", es="No habla. No necesita palabras. SIENTO su pregunta: ¿Por qué estás aquí? ¿Qué quieres?", it="Non parla. Non ha bisogno di parole. SENTO la sua domanda: Perché sei qui? Cosa vuoi?")
    _tc(tr, F, "choice_nightmare",
        en_choices=["I am here to bind you. As my grandmother wished.", "I am not afraid of you.", "Say nothing. Just endure."],
        fr_choices=["Je suis ici pour te lier. Comme ma grand-mère le voulait.", "Je n'ai pas peur de toi.", "Ne rien dire. Simplement tenir bon."],
        es_choices=["Estoy aquí para atarte. Como mi abuela quería.", "No te tengo miedo.", "No decir nada. Solo resistir."],
        it_choices=["Sono qui per legarti. Come voleva mia nonna.", "Non ho paura di te.", "Non dire nulla. Solo resistere."])
    _t(tr, F, "nightmare_defy", en="I feel the entity recoil. Not from fear - from surprise. No one has spoken to it like this since Margarethe.", fr="Je sens l'entité reculer. Pas de peur - de surprise. Personne ne lui à parlé ainsi depuis Margarethe.", es="Siento cómo la entidad retrocede. No de miedo - de sorpresa. Nadie le ha hablado así desde Margarethe.", it="Sento l'entità ritrarsi. Non per paura - per sorpresa. Nessuno le ha parlato così da Margarethe.")
    _t(tr, F, "nightmare_brave", en="The lie tastes like ash. But the entity... it laughs. Not maliciously. Approvingly. Like an old warrior sizing up a young opponent.", fr="Le mensonge à un goût de cendre. Mais l'entité... elle rit. Pas avec malveillance. Avec approbation. Comme un vieux guerrier jaugeant un jeune adversaire.", es="La mentira sabe a ceniza. Pero la entidad... se ríe. No con malicia. Con aprobación. Como un viejo guerrero evaluando a un joven oponente.", it="La bugia sa di cenere. Ma l'entità... ride. Non con malevolenza. Con approvazione. Come un vecchio guerriero che valuta un giovane avversario.")
    _t(tr, F, "nightmare_endure", en="I say nothing. I stand my ground. The darkness presses in on me, but I do not yield. At some point - seconds? Hours? - the pressure eases.", fr="Je ne dis rien. Je tiens bon. L'obscurité m'oppresse, mais je ne cède pas. À un moment - des secondes ? Des heures ? - là pression diminue.", es="No digo nada. Me mantengo firme. La oscuridad me presiona, pero no cedo. En algún momento - ¿segundos? ¿Horas? - la presión cede.", it="Non dico nulla. Tengo duro. L'oscurità preme su di me, ma non cedo. A un certo punto - secondi? Ore? - la pressione si allenta.")
    _t(tr, F, "nightmare_wake", en="I jolt awake. Cold sweat. I'm still standing in the doorframe. Only seconds have passed. But the entity has seen me. And I have seen it.", fr="Je me réveille en sursaut. Sueur froide. Je suis toujours debout dans le chambranle. Seules quelques secondes ont passé. Mais l'entité m'à vue. Et je l'ai vue.", es="Despierto sobresaltada. Sudor frío. Sigo de pie en el marco de la puerta. Solo han pasado segundos. Pero la entidad me ha visto. Y yo la he visto a ella.", it="Mi sveglio di soprassalto. Sudore freddo. Sono ancora in piedi nello stipite. Sono passati solo pochi secondi. Ma l'entità mi ha vista. È io ho visto lei.")
    _t(tr, F, "otto_threat", en="A dead chicken hangs on grandmother's garden fence. Next to it, carved into the wooden posts: a spiral. Otto's warning.", fr="Un poulet mort pend à là clôture du jardin de grand-mère. À côté, gravée dans les poteaux de bois : une spirale. L'avertissement d'Otto.", es="Una gallina muerta cuelga de la valla del jardín de la abuela. Al lado, tallada en los postes de madera: una espiral. La advertencia de Otto.", it="Un pollo morto pende dalla staccionata del giardino della nonna. Accanto, incisa nei pali di legno: una spirale. L'avvertimento di Otto.")
    _t(tr, F, "narration_plan", en="I need allies. I cannot perform the binding ritual alone - and Otto will not let it happen without a fight.", fr="J'ai besoin d'alliés. Je ne peux pas accomplir le rituel de liaison seule - et Otto ne laisserà pas celà se faire sans se battre.", es="Necesito aliados. No puedo realizar el ritual de vinculación sola - y Otto no permitirá que suceda sin luchar.", it="Ho bisogno di alleati. Non posso compiere il rituale di legame da sola - è Otto non lo lascerà accadere senza combattere.")
    _t(tr, F, "narration_forest_1", en="The forest has changed. The trees bend toward each other as if whispering. Glowing spirals pulse on the bark. The path splits in directions that didn't exist yesterday.", fr="Là forêt à changé. Les arbres se penchent les uns vers les autres comme s'ils chuchotaient. Des spirales lumineuses pulsent sur l'écorce. Le sentier se divise dans des directions qui n'existaient pas hier.", es="El bosque ha cambiado. Los árboles se inclinan unos hacia otros como susurrando. Espirales luminosas pulsan en la corteza. El camino se divide en direcciones que ayer no existían.", it="La foresta è cambiata. Gli alberi si piegano l'uno verso l'altro come sussurrando. Spirali luminose pulsano sulla corteccia. Il sentiero si divide in direzioni che ieri non esistevano.")
    _t(tr, F, "narration_forest_2", en="And the forest is closer. Much closer. The trees now stand directly behind the last houses. Graubach is shrinking. Or the forest is growing.", fr="Et là forêt est plus proche. Bien plus proche. Les arbres se dressent maintenant juste derrière les dernières maisons. Graubach rétrécit. Ou là forêt grandit.", es="Y el bosque está más cerca. Mucho más cerca. Los árboles ahora están justo detrás de las últimas casas. Graubach se encoge. O el bosque crece.", it="E la foresta è più vicina. Molto più vicina. Gli alberi ora si ergono proprio dietro le ultime case. Graubach si restringe. O la foresta cresce.")
    _t(tr, F, "anna_1", en="Anna Voss stands among the trees. Barefoot, in her nightgown. Her eyes are wide open, but they don't look at me. They look through me.", fr="Annà Voss se tient parmi les arbres. Pieds nus, en chemise de nuit. Ses yeux sont grands ouverts, mais ils ne me regardent pas. Ils regardent à travers moi.", es="Anna Voss está de pie entre los árboles. Descalza, en camisón. Sus ojos están muy abiertos, pero no me miran a mí. Miran a través de mí.", it="Anna Voss è in piedi tra gli alberi. Scalza, in camicia da notte. I suoi occhi sono spalancati, ma non guardano me. Guardano attraverso di me.")
    _t(tr, F, "anna_2", en="It dreams of you, Elise. Every night. It dreams that you come and set it free. Or that you come and put it to sleep forever.", fr="Il rêve de toi, Elise. Chaque nuit. Il rêve que tu viens et que tu le libères. Ou que tu viens et que tu l'endors pour toujours.", es="Sueña contigo, Elise. Cada noche. Sueña que vienes y lo liberas. O que vienes y lo duermes para siempre.", it="Sogna di te, Elise. Ogni notte. Sogna che vieni è lo liberi. O che vieni è lo addormenti per sempre.")
    _t(tr, F, "anna_4", en="It's afraid, Elise. It's afraid of you. That's why the dreams are growing stronger. It's trying to confuse you before you can act.", fr="Il à peur, Elise. Il à peur de toi. C'est pour celà que les rêves deviennent plus forts. Il essaie de te troubler avant que tu ne puisses agir.", es="Tiene miedo, Elise. Tiene miedo de ti. Por eso los sueños se vuelven más fuertes. Intenta confundirte antes de que puedas actuar.", it="Ha paura, Elise. Ha paura di te. Per questo i sogni diventano più forti. Cerca di confonderti prima che tu possa agire.")
    _t(tr, F, "anna_6", en="Please, Elise. Hurry. I can hear its voice growing louder. Soon I won't hear anything else.", fr="S'il te plaît, Elise. Dépêche-toi. J'entends sà voix de plus en plus fort. Bientôt, je n'entendrai plus rien d'autre.", es="Por favor, Elise. Date prisa. Puedo oír su voz cada vez más fuerte. Pronto no oiré nada más.", it="Ti prego, Elise. Sbrigati. Sento la sua voce sempre più forte. Presto non sentirò più nient'altro.")
    _t(tr, F, "journal_reality", en="Reality Is Breaking", fr="Là réalité se brise", es="La realidad se quiebra", it="La realtà si spezza", field="title")
    _t(tr, F, "journal_reality", en="Day 6: Reality is growing thin. The forest grows, the village distorts, colors are no longer right. Anna says the entity dreams of me - it's afraid. The Feeding is the day after tomorrow. I must act before then.", fr="Jour 6 : Là réalité s'amincit. Là forêt grandit, le village se déforme, les couleurs ne sont plus justes. Annà dit que l'entité rêve de moi - elle à peur. Là Nourriture est après-demain. Je dois agir avant.", es="Día 6: La realidad se vuelve delgada. El bosque crece, el pueblo se distorsiona, los colores ya no son correctos. Anna dice que la entidad sueña conmigo - tiene miedo. La Alimentación es pasado mañana. Debo actuar antes.", it="Giorno 6: La realtà si assottiglia. La foresta cresce, il villaggio si deforma, i colori non sono più giusti. Anna dice che l'entità sogna di me - ha paura. La Nutrizione è dopodomani. Devo agire prima.", field="content")

    # --- Additional translations (auto-generated) ---
    _t(tr, F, "elise_mirror",
       en="In the mirror I see myself. But my reflection blinks half a second later than I do.",
       fr="Dans le miroir, je me vois. Mais mon reflet cligne des yeux une demi-seconde apr\u00e8s moi.",
       es="En el espejo me veo. Pero mi reflejo parpadea medio segundo despu\u00e9s que yo.",
       it="Nello specchio vedo me stessa. Ma il mio riflesso sbatte le palpebre mezzo secondo dopo di me.")
    _t(tr, F, "elise_mirror_react",
       en="I step back. My heart pounds. The reflection smiles - half a second after I stopped smiling. I turn the mirror to the wall.",
       fr="Je recule. Mon c\u0153ur bat la chamade. Le reflet sourit - une demi-seconde apr\u00e8s que j'ai cess\u00e9 de sourire. Je retourne le miroir contre le mur.",
       es="Retrocedo. Mi coraz\u00f3n late con fuerza. El reflejo sonr\u00ede, medio segundo despu\u00e9s de que dej\u00e9 de sonre\u00edr. Giro el espejo hacia la pared.",
       it="Indietreggio. Il mio cuore martella. Il riflesso sorride - mezzo secondo dopo che ho smesso di sorridere. Giro lo specchio verso la parete.")
    _t(tr, F, "elise_street_react",
       en="The street was not this winding yesterday. I KNOW that. I have walked it for six days. But now it curves as though the ground were made of soft wax.",
       fr="La rue n'\u00e9tait pas aussi sinueuse hier. Je le SAIS. Je l'ai parcourue pendant six jours. Mais maintenant elle se courbe comme si le sol \u00e9tait fait de cire molle.",
       es="La calle no era tan sinuosa ayer. Lo S\u00c9. La he recorrido durante seis d\u00edas. Pero ahora se curva como si el suelo fuera de cera blanda.",
       it="La strada non era cos\u00ec tortuosa ieri. Lo SO. L'ho percorsa per sei giorni. Ma ora si curva come se il terreno fosse di cera morbida.")
    _t(tr, F, "villager_scene",
       en="An old woman stands before her house, staring into nothing. I know her - she sold me bread at the market yesterday. Today she does not recognize me.",
       fr="Une vieille femme se tient devant sa maison, le regard fix\u00e9 dans le vide. Je la connais - elle m'a vendu du pain au march\u00e9 hier. Aujourd'hui, elle ne me reconna\u00eet pas.",
       es="Una anciana est\u00e1 frente a su casa, mirando a la nada. La conozco: ayer me vendi\u00f3 pan en el mercado. Hoy no me reconoce.",
       it="Una vecchia donna sta davanti alla sua casa, fissando il nulla. La conosco - ieri mi ha venduto il pane al mercato. Oggi non mi riconosce.")
    _t(tr, F, "elise_villager",
       en="Frau Lehmann? Is everything all right?",
       fr="Frau Lehmann ? Tout va bien ?",
       es="\u00bfFrau Lehmann? \u00bfEst\u00e1 todo bien?",
       it="Frau Lehmann? Va tutto bene?")
    _t(tr, F, "villager_react",
       en="She turns slowly toward me. Her eyes are glassy, empty. Then she whispers something - in a language I do not know. But understand.",
       fr="Elle se tourne lentement vers moi. Ses yeux sont vitreux, vides. Puis elle murmure quelque chose - dans une langue que je ne connais pas. Mais que je comprends.",
       es="Se vuelve lentamente hacia m\u00ed. Sus ojos son vidriosos, vac\u00edos. Luego susurra algo, en un idioma que no conozco. Pero que entiendo.",
       it="Si gira lentamente verso di me. I suoi occhi sono vitrei, vuoti. Poi sussurra qualcosa - in una lingua che non conosco. Ma che comprendo.")
    _t(tr, F, "villager_whisper",
       en="'It is coming.' Two words. Then she turns back toward the church and stands motionless again. As if nothing had happened.",
       fr="\u00ab \u00c7a vient. \u00bb Deux mots. Puis elle se retourne vers l'\u00e9glise et se tient de nouveau immobile. Comme si rien ne s'\u00e9tait pass\u00e9.",
       es="'Viene.' Dos palabras. Luego se vuelve hacia la iglesia y se queda inm\u00f3vil de nuevo. Como si nada hubiera pasado.",
       it="'\u00c8 in arrivo.' Due parole. Poi si volta di nuovo verso la chiesa e resta immobile. Come se niente fosse accaduto.")
    _t(tr, F, "elise_villager_horror",
       en="It is not only the walls that are distorting. It is the people. The creature reaches into their heads, turns them in its direction like sunflowers toward the sun.",
       fr="Ce ne sont pas seulement les murs qui se d\u00e9forment. Ce sont les gens. La cr\u00e9ature s'insinue dans leurs t\u00eates, les tourne dans sa direction comme des tournesols vers le soleil.",
       es="No son solo los muros los que se deforman. Son las personas. La criatura se mete en sus cabezas, los gira en su direcci\u00f3n como girasoles hacia el sol.",
       it="Non sono solo i muri a distorcersi. Sono le persone. La creatura si insinua nelle loro teste, li volge nella sua direzione come girasoli verso il sole.")
    _t(tr, F, "elise_nightmare_inner",
       en="Panic rises. But Hilde's amulet burns against my chest - an anchor in this sea of darkness. I breathe. I am Elise Brandt. I am here because Grandmother called me.",
       fr="La panique monte. Mais l'amulette de Hilde br\u00fble contre ma poitrine - une ancre dans cette mer de t\u00e9n\u00e8bres. Je respire. Je suis Elise Brandt. Je suis ici parce que Grand-m\u00e8re m'a appel\u00e9e.",
       es="El p\u00e1nico crece. Pero el amuleto de Hilde arde contra mi pecho, un ancla en este mar de oscuridad. Respiro. Soy Elise Brandt. Estoy aqu\u00ed porque la abuela me llam\u00f3.",
       it="Il panico sale. Ma l'amuleto di Hilde brucia sul mio petto - un'\u00e0ncora in questo mare di tenebre. Respiro. Sono Elise Brandt. Sono qui perch\u00e9 la nonna mi ha chiamata.")
    _t(tr, F, "nightmare_defy_2",
       en="For a moment - shorter than a heartbeat - I sense something like... respect. Then the vision collapses.",
       fr="Pendant un instant - plus bref qu'un battement de c\u0153ur - je per\u00e7ois quelque chose comme... du respect. Puis la vision s'effondre.",
       es="Por un instante, m\u00e1s breve que un latido, percibo algo como... respeto. Luego la visi\u00f3n se desmorona.",
       it="Per un istante - pi\u00f9 breve di un battito cardiaco - percepisco qualcosa come... rispetto. Poi la visione crolla.")
    _t(tr, F, "nightmare_brave_2",
       en="It knows I am lying. Of course I am afraid. But it respects the courage it takes to conceal the fear.",
       fr="Il sait que je mens. Bien s\u00fbr que j'ai peur. Mais il respecte le courage qu'il faut pour dissimuler la peur.",
       es="Sabe que miento. Por supuesto que tengo miedo. Pero respeta el valor que se necesita para ocultar el miedo.",
       it="Sa che sto mentendo. Certo che ho paura. Ma rispetta il coraggio necessario per nascondere la paura.")
    _t(tr, F, "nightmare_endure_2",
       en="Silence as an answer. The creature seems to... ponder. As if it had not expected that. Then the vision dissolves.",
       fr="Le silence pour r\u00e9ponse. La cr\u00e9ature semble... r\u00e9fl\u00e9chir. Comme si elle ne s'y attendait pas. Puis la vision se dissout.",
       es="Silencio como respuesta. La criatura parece... reflexionar. Como si no lo hubiera esperado. Luego la visi\u00f3n se disuelve.",
       it="Il silenzio come risposta. La creatura sembra... riflettere. Come se non se lo fosse aspettata. Poi la visione si dissolve.")
    _t(tr, F, "elise_wake_react",
       en="It is real. No superstition, no fairy tale, no delusion of an old woman. It is down there, and it is more awake than ever. And it knows my name.",
       fr="C'est r\u00e9el. Pas de superstition, pas de conte de f\u00e9es, pas le d\u00e9lire d'une vieille femme. C'est l\u00e0-dessous, et c'est plus \u00e9veill\u00e9 que jamais. Et \u00e7a conna\u00eet mon nom.",
       es="Es real. No es superstici\u00f3n, ni cuento de hadas, ni delirio de una anciana. Est\u00e1 ah\u00ed abajo, y est\u00e1 m\u00e1s despierta que nunca. Y conoce mi nombre.",
       it="\u00c8 reale. Nessuna superstizione, nessuna favola, nessun delirio di una vecchia. \u00c8 l\u00e0 sotto, ed \u00e8 pi\u00f9 sveglia che mai. E conosce il mio nome.")
    _t(tr, F, "elise_otto_react",
       en="My stomach turns. Not from fear - from rage. He threatens me with a dead animal while beneath our feet something awakens that could devour the world.",
       fr="Mon estomac se retourne. Pas de peur - de col\u00e8re. Il me menace avec un animal mort tandis que sous nos pieds quelque chose s'\u00e9veille qui pourrait d\u00e9vorer le monde.",
       es="Se me revuelve el est\u00f3mago. No de miedo, sino de rabia. Me amenaza con un animal muerto mientras bajo nuestros pies algo despierta que podr\u00eda devorar el mundo.",
       it="Lo stomaco mi si rivolta. Non per la paura - per la rabbia. Mi minaccia con un animale morto mentre sotto i nostri piedi qualcosa si risveglia che potrebbe divorare il mondo.")
    _t(tr, F, "elise_plan_assess",
       en="Georg has strength and loyalty. Hilde knows the old ways. Voss knows the chamber. And Konrad... Konrad is either the key or the greatest danger.",
       fr="Georg a la force et la loyaut\u00e9. Hilde conna\u00eet les anciennes voies. Voss conna\u00eet la chambre. Et Konrad... Konrad est soit la clef, soit le plus grand danger.",
       es="Georg tiene fuerza y lealtad. Hilde conoce los antiguos caminos. Voss conoce la c\u00e1mara. Y Konrad... Konrad es o la clave o el mayor peligro.",
       it="Georg ha forza e lealt\u00e0. Hilde conosce le antiche vie. Voss conosce la camera. E Konrad... Konrad \u00e8 o la chiave o il pericolo pi\u00f9 grande.")
    _t(tr, F, "elise_forest_react",
       en="Yesterday these spirals were barely visible. Today they glow. The ground vibrates beneath my steps, as if I were walking upon a thin skin.",
       fr="Hier, ces spirales \u00e9taient \u00e0 peine visibles. Aujourd'hui, elles brillent. Le sol vibre sous mes pas, comme si je marchais sur une peau fine.",
       es="Ayer estas espirales apenas eran visibles. Hoy brillan. El suelo vibra bajo mis pasos, como si caminara sobre una piel fina.",
       it="Ieri queste spirali erano appena visibili. Oggi brillano. Il terreno vibra sotto i miei passi, come se camminassi su una pelle sottile.")
    _t(tr, F, "elise_anna_approach",
       en="Anna? Can you hear me? What are you doing out here in the forest alone?",
       fr="Anna ? Tu m'entends ? Que fais-tu ici, seule dans la for\u00eat ?",
       es="\u00bfAnna? \u00bfMe oyes? \u00bfQu\u00e9 haces aqu\u00ed sola en el bosque?",
       it="Anna? Mi senti? Cosa fai qui da sola nel bosco?")
    _t(tr, F, "elise_anna_question",
       en="How do you know that? Can you see its dreams?",
       fr="Comment le sais-tu ? Peux-tu voir ses r\u00eaves ?",
       es="\u00bfC\u00f3mo lo sabes? \u00bfPuedes ver sus sue\u00f1os?",
       it="Come lo sai? Riesci a vedere i suoi sogni?")
    _t(tr, F, "elise_anna_light",
       en="A light? It is afraid of ME?",
       fr="Une lumi\u00e8re ? Il a peur de MOI ?",
       es="\u00bfUna luz? \u00bfTiene miedo de M\u00cd?",
       it="Una luce? Ha paura di ME?")
    _t(tr, F, "anna_confirms",
       en="It is afraid of you, Elise. That is why the dreams grow stronger. It is trying to confuse you before you can act.",
       fr="Il a peur de toi, Elise. C'est pour cela que les r\u00eaves deviennent plus forts. Il essaie de te d\u00e9sorienter avant que tu ne puisses agir.",
       es="Tiene miedo de ti, Elise. Por eso los sue\u00f1os se vuelven m\u00e1s fuertes. Intenta confundirte antes de que puedas actuar.",
       it="Ha paura di te, Elise. Per questo i sogni si fanno pi\u00f9 forti. Sta cercando di confonderti prima che tu possa agire.")
    _t(tr, F, "narration_anna_realization",
       en="I am not the victim. I am the threat. Since I touched my name in the book, since I learned the chant - the creature knows what I intend. And it is desperately trying to stop me.",
       fr="Je ne suis pas la victime. Je suis la menace. Depuis que j'ai touch\u00e9 mon nom dans le livre, depuis que j'ai appris le chant - la cr\u00e9ature sait ce que j'ai l'intention de faire. Et elle essaie d\u00e9sesp\u00e9r\u00e9ment de m'arr\u00eater.",
       es="No soy la v\u00edctima. Soy la amenaza. Desde que toqu\u00e9 mi nombre en el libro, desde que aprend\u00ed el canto, la criatura sabe lo que pretendo. Y est\u00e1 intentando desesperadamente detenerme.",
       it="Non sono la vittima. Sono la minaccia. Da quando ho toccato il mio nome nel libro, da quando ho imparato il canto - la creatura sa cosa intendo fare. E sta cercando disperatamente di fermarmi.")
    _t(tr, F, "elise_anna_promise",
       en="I will end it, Anna. For you, for Konrad, for everyone. I promise.",
       fr="J'y mettrai fin, Anna. Pour toi, pour Konrad, pour tous. Je te le promets.",
       es="Lo terminar\u00e9, Anna. Por ti, por Konrad, por todos. Te lo prometo.",
       it="Lo finir\u00f2, Anna. Per te, per Konrad, per tutti. Te lo prometto.")
    _t(tr, F, "narration_determination",
       en="As Anna vanishes among the trees, I feel something new. Not fear - determination. The creature is afraid of me. Then I have a chance.",
       fr="Tandis qu'Anna dispara\u00eet entre les arbres, je ressens quelque chose de nouveau. Pas de la peur - de la d\u00e9termination. La cr\u00e9ature a peur de moi. Alors j'ai une chance.",
       es="Mientras Anna desaparece entre los \u00e1rboles, siento algo nuevo. No miedo, sino determinaci\u00f3n. La criatura me tiene miedo. Entonces tengo una oportunidad.",
       it="Mentre Anna scompare tra gli alberi, sento qualcosa di nuovo. Non paura - determinazione. La creatura ha paura di me. Allora ho una possibilit\u00e0.")


def _add_act3_descent(tr):
    F = "res://data/dialogue/act3/descent.json"

    _t(tr, F, "narration_1", en="Day seven. Evening. The church no longer looks like a church. The pews are shifted, some hovering centimeters above the floor. The stained-glass windows show images that do not belong in glass.", fr="Septième jour. Soir. L'église ne ressemble plus à une église. Les bancs sont déplacés, certains flottent à quelques centimètres du sol. Les vitraux montrent des images qui n'ont rien à faire dans du verre.", es="Día siete. Noche. La iglesia ya no parece una iglesia. Los bancos están desplazados, algunos flotan centímetros por encima del suelo. Las vidrieras muestran imágenes que no pertenecen al cristal.", it="Giorno sette. Sera. La chiesa non sembra più una chiesa. Le panche sono spostate, alcune fluttuano a centimetri dal pavimento. Le vetrate mostrano immagini che non appartengono al vetro.")
    _t(tr, F, "narration_2", en="The singing is everywhere. No longer just from the depths — it comes from the walls, from the air, from inside my own head. Hilde's amulet pulses warm against my chest.", fr="Le chant est partout. Plus seulement depuis les profondeurs — il vient des murs, de l'air, de l'intérieur de mà propre tête. L'amulette de Hilde pulse, chaude contre mà poitrine.", es="El canto está en todas partes. Ya no solo desde las profundidades — viene de las paredes, del aire, del interior de mi propia cabeza. El amuleto de Hilde pulsa cálido contra mi pecho.", it="Il canto è ovunque. Non più solo dal profondo — viene dalle pareti, dall'aria, dall'interno della mia stessa testa. L'amuleto di Hilde pulsa caldo contro il mio petto.")
    _t(tr, F, "narration_3", en="I stand before the stairs to the chamber. The key in my hand is warm — not from my body heat. A warmth of its own.", fr="Je me tiens devant l'escalier menant à là chambre. Là clé dans mà main est chaude — pas de mà chaleur corporelle. Une chaleur propre.", es="Estoy frente a la escalera que lleva a la cámara. La llave en mi mano está caliente — no por mi calor corporal. Un calor propio.", it="Sono davanti alla scala che porta alla camera. La chiave nella mia mano è calda — non per il calore del mio corpo. Un calore proprio.")
    _t(tr, F, "otto_confrontation", en="The church door flies open. Otto Reinhardt stands in the entrance, flanked by two men with torches. His expression is cold.", fr="Là porte de l'église s'ouvre brusquement. Otto Reinhardt se tient dans l'entrée, flanqué de deux hommes portant des torches. Son expression est glaciale.", es="La puerta de la iglesia se abre de golpe. Otto Reinhardt está en la entrada, flanqueado por dos hombres con antorchas. Su expresión es fría.", it="La porta della chiesa si spalanca. Otto Reinhardt è sulla soglia, fiancheggiato da due uomini con le torce. La sua espressione è gelida.")
    _t(tr, F, "otto_conf_1", en="I warned you, Fräulein Brandt. The tradition is older than you, older than I, older than this village. And you will not break it.", fr="Je vous ai prévenue, Fräulein Brandt. Là tradition est plus ancienne que vous, plus ancienne que moi, plus ancienne que ce village. Et vous ne là briserez pas.", es="Se lo advertí, Fräulein Brandt. La tradición es más antigua que usted, más antigua que yo, más antigua que este pueblo. Y usted no la romperá.", it="L'avevo avvertita, Fräulein Brandt. La tradizione è più antica di Lei, più antica di me, più antica di questo villaggio. È Lei non la spezzerà.")
    _t(tr, F, "georg_defends_1", en="Enough, Otto. For thirty years I watched. For thirty years I stayed silent. That is over.", fr="Assez, Otto. Pendant trente ans j'ai regardé. Pendant trente ans je me suis tu. C'est terminé.", es="Basta, Otto. Treinta años he mirado. Treinta años he callado. Se acabó.", it="Basta, Otto. Per trent'anni ho guardato. Per trent'anni ho taciuto. È finita.")
    _t(tr, F, "georg_defends_2", en="Georg steps between me and Otto. In his hand the blacksmith's hammer. Otto backs away — he knows Georg, knows his strength.", fr="Georg se place entre moi et Otto. Dans sà main, le marteau de forgeron. Otto recule — il connaît Georg, connaît sà force.", es="Georg se interpone entre Otto y yo. En su mano, el martillo de herrero. Otto retrocede — conoce a Georg, conoce su fuerza.", it="Georg si mette tra me è Otto. Nella mano il martello da fabbro. Otto indietreggia — conosce Georg, conosce la sua forza.")
    _t(tr, F, "georg_defends_3", en="Go, Elise. I will hold them off. Do what Margarethe planned.", fr="Va, Elise. Je les retiens. Fais ce que Margarethe avait prévu.", es="Ve, Elise. Yo los detengo. Haz lo que Margarethe planeó.", it="Vai, Elise. Li trattengo io. Fai quello che Margarethe aveva progettato.")
    _t(tr, F, "otto_blocks", en="Step back. Immediately. Or you will share the fate of all who have stood against the tradition.", fr="Reculez. Immédiatement. Ou il vous arriverà là même chose qu'à tous ceux qui se sont dressés contre là tradition.", es="Retroceda. Inmediatamente. O le ocurrirá lo mismo que a todos los que se han opuesto a la tradición.", it="Si faccia indietro. Immediatamente. O Le accadrà ciò che è accaduto a tutti coloro che si sono opposti alla tradizione.")
    _t(tr, F, "narration_dodge", en="But the church is on my side — or the entity beneath it. The flagstones under Otto's feet tremble, and he stumbles. I seize the moment and run for the stairs.", fr="Mais l'église est de mon côté — où l'entité sous elle. Les dalles sous les pieds d'Otto tremblent, et il trébuche. Je saisis l'instant et cours vers l'escalier.", es="Pero la iglesia está de mi lado — o la entidad debajo de ella. Las losas bajo los pies de Otto tiemblan, y él tropieza. Aprovecho el momento y corro hacia la escalera.", it="Ma la chiesa è dalla mia parte — o l'entità sotto di essa. Le lastre di pietra sotto i piedi di Otto tremano, è lui inciampa. Colgo l'attimo è corro verso la scala.")
    _t(tr, F, "otto_surprise", en="No one stopped me. Perhaps Otto knows nothing. Perhaps he is busy elsewhere. Or perhaps something is letting me through on purpose.", fr="Personne ne m'à arrêtée. Peut-être qu'Otto ne sait rien. Peut-être est-il occupé ailleurs. Ou peut-être que quelque chose me laisse passer volontairement.", es="Nadie me ha detenido. Quizá Otto no sabe nada. Quizá está ocupado en otra parte. O quizá algo me deja pasar a propósito.", it="Nessuno mi ha fermata. Forse Otto non sa nulla. Forse è impegnato altrove. O forse qualcosa mi sta lasciando passare di proposito.")
    _t(tr, F, "narration_descent_1", en="The staircase spirals downward. Of course. Everything here is spiral. Each step brings me closer to the singing. It does not grow louder — it grows truer.", fr="L'escalier descend en spirale. Bien sûr. Tout ici est spirale. Chaque marche me rapproche du chant. Il ne devient pas plus fort — il devient plus vrai.", es="La escalera desciende en espiral. Por supuesto. Todo aquí es espiral. Cada paso me acerca al canto. No se hace más fuerte — se hace más verdadero.", it="La scala scende a spirale. Naturalmente. Tutto qui è spirale. Ogni passo mi avvicina al canto. Non diventa più forte — diventa più vero.")
    _t(tr, F, "narration_descent_2", en="The air is thick and sweet. My candlelight flickers, though no draft blows. The spirals on the walls seem to move when I am not looking directly at them.", fr="L'air est épais et doux. Là flamme de mà bougie vacille, bien qu'aucun courant d'air ne souffle. Les spirales sur les murs semblent bouger quand je ne les regarde pas directement.", es="El aire es denso y dulce. La llama de mi vela parpadea, aunque no sopla corriente alguna. Las espirales en las paredes parecen moverse cuando no las miro directamente.", it="L'aria è densa è dolce. La luce della mia candela tremola, sebbene non ci sia corrente. Le spirali sulle pareti sembrano muoversi quando non le guardo direttamente.")
    _t(tr, F, "narration_descent_3", en="Then: the chamber. Larger than expected. The stone here is not masoned — it has grown. Organic, like the inside of a vast creature.", fr="Puis : là chambre. Plus grande que prévu. Là pierre ici n'est pas maçonnée — elle à poussé. Organique, comme l'intérieur d'une créature immense.", es="Entonces: la cámara. Más grande de lo esperado. La piedra aquí no es obra de albañil — ha crecido. Orgánica, como el interior de una criatura inmensa.", it="Poi: la camera. Più grande del previsto. La pietra qui non è murata — è cresciuta. Organica, come l'interno di un'immensa creatura.")
    _t(tr, F, "narration_chamber_1", en="In the center of the chamber lies the book. Beside it: a circle of ancient symbols, carved into the stone. And in the middle of the circle: a spot where the floor pulses.", fr="Au centre de là chambre repose le livre. À côté : un cercle d'anciens symboles, gravés dans là pierre. Et au milieu du cercle : un endroit où le sol pulse.", es="En el centro de la cámara yace el libro. A su lado: un círculo de antiguos símbolos, grabados en la piedra. Y en el centro del círculo: un punto donde el suelo pulsa.", it="Al centro della camera giace il libro. Accanto: un cerchio di antichi simboli, incisi nella pietra. È al centro del cerchio: un punto dove il pavimento pulsa.")
    _t(tr, F, "narration_chamber_2", en="The sign of the earth. Here it is. I feel the heartbeat through the soles of my shoes, stronger than ever before. It lives. It waits.", fr="Le signe de là terre. Le voici. Je sens le battement de cœur à travers mes semelles, plus fort que jamais. Il vit. Il attend.", es="El signo de la tierra. Aquí está. Siento el latido a través de las suelas de mis zapatos, más fuerte que nunca. Vive. Espera.", it="Il segno della terra. Eccolo. Sento il battito attraverso le suole delle mie scarpe, più forte che mai. Vive. Aspetta.")
    _t(tr, F, "journal_descent", en="The Descent", fr="Là Descente", es="El Descenso", it="La Discesa", field="title")
    _t(tr, F, "journal_descent", en="I am in the chamber beneath the church. The floor pulses, the walls live, the singing fills everything. The Book of Names lies here. The sign of the earth — the pulsing point — is in the center. Tomorrow I perform the ritual. Or die trying.", fr="Je suis dans là chambre sous l'église. Le sol pulse, les murs vivent, le chant emplit tout. Le Livre des Noms repose ici. Le signe de là terre — le point pulsant — est au centre. Demain j'accomplis le rituel. Ou je meurs en essayant.", es="Estoy en la cámara bajo la iglesia. El suelo pulsa, las paredes viven, el canto lo llena todo. El Libro de los Nombres yace aquí. El signo de la tierra — el punto pulsante — está en el centro. Mañana realizaré el ritual. O moriré en el intento.", it="Sono nella camera sotto la chiesa. Il pavimento pulsa, le pareti vivono, il canto riempie tutto. Il Libro dei Nomi giace qui. Il segno della terrà — il punto pulsante — è al centro. Domani eseguirò il rituale. O morirò provandoci.", field="content")
    _t(tr, F, "narration_end_1", en="I stand in the chamber, and the entity knows I am here. Between us lies only thin stone and centuries of waiting.", fr="Je me tiens dans là chambre, et l'entité sait que je suis là. Entre nous, seulement de là pierre mince et des siècles d'attente.", es="Estoy en la cámara, y la entidad sabe que estoy aquí. Entre nosotros solo hay piedra delgada y siglos de espera.", it="Sono nella camera, è l'entità sa che sono qui. Tra noi solo pietra sottile è secoli di attesa.")
    _t(tr, F, "narration_end_2", en="Tomorrow it ends. One way or another.", fr="Demain, tout se termine. D'une manière où d'une autre.", es="Mañana termina. De un modo u otro.", it="Domani finisce. In un modo o nell'altro.")
    # --- Opening: resolve + ally arrival ---
    _t(tr, F, "narration_resolve",
       en="My heart pounds. But my hands are steady. Grandmother's hands, Georg said. Hands that do not tremble when it matters.",
       fr="Mon cœur bat fort. Mais mes mains sont fermes. Les mains de grand-mère, à dit Georg. Des mains qui ne tremblent pas quand çà compte.",
       es="Mi corazón martillea. Pero mis manos están firmes. Las manos de la abuela, dijo Georg. Manos que no tiemblan cuando importa.",
       it="Il mio cuore martella. Ma le mie mani sono ferme. Le mani della nonna, ha detto Georg. Mani che non tremano quando conta.")
    # Georg ally
    _t(tr, F, "georg_ally_1",
       en="Are you ready?",
       fr="Tu es prête ?",
       es="¿Estás lista?",
       it="Sei pronta?")
    _t(tr, F, "elise_ally_georg_1",
       en="No. But when would one be ready for something like this?",
       fr="Non. Mais quand serait-on prêt pour une chose pareille ?",
       es="No. Pero ¿cuándo se estaría lista para algo así?",
       it="No. Ma quando si sarebbe pronti per una cosa del genere?")
    _t(tr, F, "georg_ally_2",
       en="Margarethe said the same thing, back then. Word for word.",
       fr="Margarethe à dit là même chose, à l'époque. Mot pour mot.",
       es="Margarethe dijo lo mismo, en aquel entonces. Palabra por palabra.",
       it="Margarethe disse la stessa cosa, allora. Parola per parola.")
    _t(tr, F, "elise_ally_georg_2",
       en="Then at least she left me that.",
       fr="Alors au moins elle m'à laissé ça.",
       es="Entonces al menos me dejó eso.",
       it="Allora almeno questo me l'ha lasciato.")
    _t(tr, F, "narration_ally_together",
       en="He nods. No more words needed. We go together.",
       fr="Il hoche là tête. Plus besoin de mots. Nous y allons ensemble.",
       es="Asiente. No hacen falta más palabras. Vamos juntos.",
       it="Annuisce. Non servono altre parole. Andiamo insieme.")
    # Hilde ally
    _t(tr, F, "hilde_ally_1",
       en="The church is resisting. Can you feel it? The stones are bristling.",
       fr="L'église résiste. Tu le sens ? Les pierres se hérissent.",
       es="La iglesia se resiste. ¿Lo sientes? Las piedras se erizan.",
       it="La chiesa resiste. Lo senti? Le pietre si drizzano.")
    _t(tr, F, "elise_ally_hilde_1",
       en="Mostly I feel the singing. It is... louder than last night. Closer.",
       fr="Je sens surtout le chant. Il est... plus fort que là nuit dernière. Plus proche.",
       es="Sobre todo siento el canto. Es... más fuerte que anoche. Más cercano.",
       it="Sento soprattutto il canto. È... più forte di ieri notte. Più vicino.")
    _t(tr, F, "hilde_ally_2",
       en="That is good. It knows you are coming. It expects you.",
       fr="C'est bien. Il sait que tu arrives. Il t'attend.",
       es="Eso es bueno. Sabe que vienes. Te espera.",
       it="Questo è un bene. Sa che stai arrivando. Ti aspetta.")
    _t(tr, F, "elise_ally_hilde_2",
       en="That is supposed to reassure me?",
       fr="C'est censé me rassurer ?",
       es="¿Eso debería tranquilizarme?",
       it="Questo dovrebbe rassicurarmi?")
    _t(tr, F, "hilde_ally_3",
       en="It is supposed to prepare you. I leave the reassurance to the valerian.",
       fr="C'est censé te préparer. Là réassurance, je là laisse à là valériane.",
       es="Debería prepararte. La tranquilidad se la dejo a la valeriana.",
       it="Dovrebbe prepararti. La rassicurazione la lascio alla valeriana.")
    _t(tr, F, "narration_hilde_smile",
       en="Despite everything, I have to smile. Hilde has that way of taking the edge off the terror.",
       fr="Malgré tout, je ne peux m'empêcher de sourire. Hilde à cette façon d'émousser là terreur.",
       es="A pesar de todo, tengo que sonreír. Hilde tiene esa forma de quitarle el filo al terror.",
       it="Nonostante tutto, devo sorridere. Hilde ha quel modo di smussare il terrore.")
    # Voss ally
    _t(tr, F, "voss_ally_1",
       en="God help us. The church... my church... what has it done to her?",
       fr="Dieu nous aide. L'église... mon église... qu'est-ce qu'il lui à fait ?",
       es="Dios nos ayude. La iglesia... mi iglesia... ¿qué le ha hecho?",
       it="Dio ci aiuti. La chiesa... la mia chiesa... che cosa le ha fatto?")
    _t(tr, F, "elise_ally_voss_1",
       en="It is showing us what has always been beneath the surface, Pastor. Are you ready?",
       fr="Il nous montre ce qui à toujours été sous là surface, Pasteur. Êtes-vous prêt ?",
       es="Nos muestra lo que siempre estuvo bajo la superficie, Pastor. ¿Está listo?",
       it="Ci mostra ciò che è sempre stato sotto la superficie, Pastore. È pronto?")
    _t(tr, F, "voss_ally_2",
       en="For thirty years I have dreaded this night. But now... now I am almost relieved that it is finally here.",
       fr="Pendant trente ans j'ai redouté cette nuit. Mais maintenant... maintenant je suis presque soulagé que ce soit enfin arrivé.",
       es="Durante treinta años he temido esta noche. Pero ahora... ahora casi me alivia que por fin haya llegado.",
       it="Per trent'anni ho temuto questa notte. Ma ora... ora sono quasi sollevato che sia finalmente arrivata.")
    _t(tr, F, "elise_ally_voss_2",
       en="Relief before the abyss. I understand what you mean.",
       fr="Le soulagement face à l'abîme. Je comprends ce que vous voulez dire.",
       es="Alivio ante el abismo. Entiendo lo que quiere decir.",
       it="Sollievo davanti all'abisso. Capisco cosa intende.")
    _t(tr, F, "narration_voss_together",
       en="Voss crosses himself. His hands tremble, but his steps are firm. Thirty years of guilt are a heavy anchor.",
       fr="Voss se signe. Ses mains tremblent, mais ses pas sont fermes. Trente ans de culpabilité sont un lourd ancrage.",
       es="Voss se persigna. Sus manos tiemblan, pero sus pasos son firmes. Treinta años de culpa son un ancla pesada.",
       it="Voss si fa il segno della croce. Le sue mani tremano, ma i suoi passi sono fermi. Trent'anni di colpa sono un'ancora pesante.")
    # Alone
    _t(tr, F, "narration_alone",
       en="I am alone. No ally, no protector. Only me, the key, and the singing.",
       fr="Je suis seule. Pas d'allié, pas de protecteur. Seulement moi, là clé et le chant.",
       es="Estoy sola. Sin aliado, sin protector. Solo yo, la llave y el canto.",
       it="Sono sola. Nessun alleato, nessun protettore. Solo io, la chiave è il canto.")
    _t(tr, F, "narration_alone_2",
       en="Grandmother did it alone for thirty years. Perhaps that runs in the family.",
       fr="Grand-mère l'à fait seule pendant trente ans. Peut-être que çà court dans là famille.",
       es="La abuela lo hizo sola durante treinta años. Quizás eso viene de familia.",
       it="La nonna lo ha fatto da sola per trent'anni. Forse è una cosa di famiglia.")
    # --- Otto confrontation details ---
    _t(tr, F, "elise_otto_1",
       en="Tradition? You mean: murder. Every thirty years a murder, so you get to play mayor.",
       fr="Là tradition ? Vous voulez dire : le meurtre. Tous les trente ans un meurtre, pour que vous puissiez jouer au maire.",
       es="¿Tradición? Quiere decir: asesinato. Cada treinta años un asesinato, para que usted pueda jugar a ser alcalde.",
       it="Tradizione? Intende: omicidio. Ogni trent'anni un omicidio, perché Lei possa fare il sindaco.")
    _t(tr, F, "otto_conf_2",
       en="So that this village EXISTS! Do you think anyone LIKES living next to such an entity? We do what is necessary!",
       fr="Pour que ce village EXISTE ! Croyez-vous que quelqu'un AIME vivre à côté d'une telle entité ? Nous faisons ce qui est nécessaire !",
       es="¡Para que este pueblo EXISTA! ¿Cree que a alguien le GUSTA vivir junto a semejante entidad? ¡Hacemos lo que es necesario!",
       it="Perché questo villaggio ESISTA! Crede che a qualcuno PIACCIA vivere accanto a una simile entità? Facciamo ciò che è necessario!")
    _t(tr, F, "elise_otto_2",
       en="My grandmother searched for another way for thirty years. I will find it.",
       fr="Mà grand-mère à cherché un autre chemin pendant trente ans. Je le trouverai.",
       es="Mi abuela buscó otro camino durante treinta años. Yo lo encontraré.",
       it="Mia nonna ha cercato un'altra via per trent'anni. Io la troverò.")
    _t(tr, F, "otto_conf_3",
       en="Your grandmother DIED before she found one!",
       fr="Votre grand-mère est MORTE avant d'en trouver un !",
       es="¡Su abuela MURIÓ antes de encontrarlo!",
       it="Sua nonna è MORTA prima di trovarne una!")
    _t(tr, F, "narration_otto_silence",
       en="The words hit. For a moment I cannot breathe. He is right. Grandmother searched for thirty years and died without finding a solution.",
       fr="Les mots frappent. Pendant un instant, je ne peux plus respirer. Il à raison. Grand-mère à cherché pendant trente ans et est morte sans trouver de solution.",
       es="Las palabras golpean. Por un momento no puedo respirar. Tiene razón. La abuela buscó durante treinta años y murió sin encontrar una solución.",
       it="Le parole colpiscono. Per un istante non riesco a respirare. Ha ragione. La nonna ha cercato per trent'anni ed è morta senza trovare una soluzione.")
    _t(tr, F, "elise_otto_3",
       en="Then at least she showed me the way. Step aside, Otto.",
       fr="Alors au moins elle m'à montré le chemin. Écartez-vous, Otto.",
       es="Entonces al menos me mostró el camino. Hágase a un lado, Otto.",
       it="Allora almeno mi ha mostrato la strada. Si faccia da parte, Otto.")
    _t(tr, F, "elise_georg_go",
       en="Georg... take care of yourself.",
       fr="Georg... fais attention à toi.",
       es="Georg... cuídate.",
       it="Georg... stai attento.")
    _t(tr, F, "georg_defends_4",
       en="I am a blacksmith. We are tough.",
       fr="Je suis forgeron. Nous sommes coriaces.",
       es="Soy herrero. Somos duros.",
       it="Sono un fabbro. Siamo duri.")
    _t(tr, F, "ally_confronts_otto",
       en="Otto Reinhardt. I knew your father and your grandfather. They all had more courage than you. Let us through.",
       fr="Otto Reinhardt. J'ai connu ton père et ton grand-père. Ils avaient tous plus de courage que toi. Laisse-nous passer.",
       es="Otto Reinhardt. Conocí a tu padre y a tu abuelo. Todos tenían más valor que tú. Déjanos pasar.",
       it="Otto Reinhardt. Ho conosciuto tuo padre è tuo nonno. Avevano tutti più coraggio di te. Facci passare.")
    _t(tr, F, "narration_hilde_otto",
       en="Hilde steps forward, small and old and utterly unyielding. Otto hesitates. In Graubach, no one contradicts Hilde.",
       fr="Hilde s'avance, petite et vieille et absolument inflexible. Otto hésite. À Graubach, personne ne contredit Hilde.",
       es="Hilde da un paso adelante, pequeña y vieja y absolutamente inflexible. Otto duda. En Graubach, nadie contradice a Hilde.",
       it="Hilde fa un passo avanti, piccola è vecchia è assolutamente irremovibile. Otto esita. A Graubach, nessuno contraddice Hilde.")
    _t(tr, F, "voss_confronts_otto",
       en="Otto, I have been silent for thirty years about what happened in 1893. Do you really want me to start talking now?",
       fr="Otto, j'ai gardé le silence pendant trente ans sur ce qui s'est passé en 1893. Voulez-vous vraiment que je commence à parler maintenant ?",
       es="Otto, he callado durante treinta años sobre lo que ocurrió en 1893. ¿De verdad quiere que empiece a hablar ahora?",
       it="Otto, ho taciuto per trent'anni su ciò che accadde nel 1893. Vuole davvero che cominci a parlare adesso?")
    _t(tr, F, "narration_voss_threat",
       en="Otto's face loses all color. Whatever Voss knows — it is enough to bring down a mayor.",
       fr="Le visage d'Otto perd toute couleur. Quoi que Voss sache — c'est assez pour faire tomber un maire.",
       es="El rostro de Otto pierde todo color. Sea lo que sea que Voss sabe — es suficiente para derribar a un alcalde.",
       it="Il volto di Otto perde ogni colore. Qualunque cosa Voss sappia — è sufficiente per far cadere un sindaco.")
    _t(tr, F, "otto_retreats",
       en="You are bringing death upon this village. Upon all of us.",
       fr="Vous apportez là mort sur ce village. Sur nous tous.",
       es="Traen la muerte a este pueblo. A todos nosotros.",
       it="Portate la morte su questo villaggio. Su tutti noi.")
    _t(tr, F, "elise_otto_retreat",
       en="No. I am bringing the end of the killing.",
       fr="Non. J'apporte là fin des meurtres.",
       es="No. Traigo el fin de las muertes.",
       it="No. Porto la fine delle uccisioni.")
    _t(tr, F, "elise_otto_alone",
       en="If the entity wants me, Otto — do you really believe you can prevent it?",
       fr="Si l'entité me veut, Otto — croyez-vous vraiment pouvoir l'en empêcher ?",
       es="Si la entidad me quiere, Otto — ¿de verdad cree que puede impedirlo?",
       it="Se l'entità vuole me, Otto — crede davvero di poterlo impedire?")
    _t(tr, F, "narration_dodge_2",
       en="I run for the stairs, past the stumbling men. Otto's shouts fade behind me, swallowed by the singing.",
       fr="Je cours vers l'escalier, dépassant les hommes qui trébuchent. Les cris d'Otto s'estompent derrière moi, engloutis par le chant.",
       es="Corro hacia la escalera, pasando junto a los hombres que tropiezan. Los gritos de Otto se desvanecen detrás de mí, engullidos por el canto.",
       it="Corro verso la scala, superando gli uomini barcollanti. Le urla di Otto svaniscono dietro di me, inghiottite dal canto.")
    _t(tr, F, "narration_otto_surprise_2",
       en="Or perhaps something is letting me through on purpose. The thought is worse than any confrontation.",
       fr="Ou peut-être que quelque chose me laisse passer volontairement. Cette pensée est pire que n'importe quelle confrontation.",
       es="O quizás algo me deja pasar a propósito. El pensamiento es peor que cualquier confrontación.",
       it="O forse qualcosa mi sta lasciando passare di proposito. Il pensiero è peggiore di qualsiasi confronto.")
    # --- Descent dialogue: Georg path ---
    _t(tr, F, "descent_georg_dialogue",
       en="Georg... the walls. The spirals are moving.",
       fr="Georg... les murs. Les spirales bougent.",
       es="Georg... las paredes. Las espirales se mueven.",
       it="Georg... le pareti. Le spirali si muovono.")
    _t(tr, F, "georg_descent_1",
       en="Don't look. Just keep walking. Margarethe said that too.",
       fr="Ne regarde pas. Continue d'avancer. Margarethe disait çà aussi.",
       es="No mires. Sigue caminando. Margarethe también decía eso.",
       it="Non guardare. Continua a camminare. Anche Margarethe lo diceva.")
    _t(tr, F, "elise_descent_georg",
       en="How often was she down here?",
       fr="Combien de fois est-elle descendue ici ?",
       es="¿Cuántas veces estuvo aquí abajo?",
       it="Quante volte è stata quaggiù?")
    _t(tr, F, "georg_descent_2",
       en="Too often. Each time she came back... changed. Quieter. As if each descent took a piece of her.",
       fr="Trop souvent. Chaque fois elle revenait... changée. Plus silencieuse. Comme si chaque descente lui prenait un morceau.",
       es="Demasiadas. Cada vez volvía... cambiada. Más callada. Como si cada descenso le quitara un pedazo.",
       it="Troppe. Ogni volta tornava... cambiata. Più silenziosa. Come se ogni discesa le portasse via un pezzo.")
    _t(tr, F, "narration_descent_cost",
       en="What did it take from her? What will it take from me? The questions hammer in my head, in time with the singing.",
       fr="Que lui a-t-il pris ? Que me prendra-t-il ? Les questions martèlent dans mà tête, au rythme du chant.",
       es="¿Qué le quitó? ¿Qué me quitará a mí? Las preguntas martillean en mi cabeza, al ritmo del canto.",
       it="Che cosa le ha preso? Che cosa prenderà a me? Le domande martellano nella mia testa, al ritmo del canto.")
    # --- Descent dialogue: Hilde path ---
    _t(tr, F, "descent_hilde_dialogue",
       en="Breathe evenly. The air down here wants to confuse you. It lies.",
       fr="Respire régulièrement. L'air ici-bas veut te dérouter. Il ment.",
       es="Respira uniformemente. El aire aquí abajo quiere confundirte. Miente.",
       it="Respira in modo regolare. L'aria quaggiù vuole confonderti. Mente.")
    _t(tr, F, "elise_descent_hilde",
       en="The sweetness... is that the breath of the entity?",
       fr="Là douceur... c'est le souffle de l'entité ?",
       es="La dulzura... ¿es el aliento de la entidad?",
       it="La dolcezza... è il respiro dell'entità?")
    _t(tr, F, "hilde_descent_1",
       en="In a way. It dreams, and its breath is the scent of its dreams. Not pleasant dreams.",
       fr="En quelque sorte. Il rêve, et son souffle est le parfum de ses rêves. Pas des rêves agréables.",
       es="En cierto modo. Sueña, y su aliento es el aroma de sus sueños. No sueños agradables.",
       it="In un certo senso. Sogna, è il suo respiro è il profumo dei suoi sogni. Non sogni piacevoli.")
    _t(tr, F, "elise_descent_hilde_2",
       en="What does something older than the trees dream of?",
       fr="De quoi rêve quelque chose de plus ancien que les arbres ?",
       es="¿Con qué sueña algo más viejo que los árboles?",
       it="Di cosa sogna qualcosa che è più antico degli alberi?")
    _t(tr, F, "hilde_descent_2",
       en="Of company. That is the sad part.",
       fr="De compagnie. C'est ce qu'il y à de triste.",
       es="De compañía. Eso es lo triste.",
       it="Di compagnia. Questa è la parte triste.")
    # --- Descent dialogue: Voss path ---
    _t(tr, F, "descent_voss_dialogue",
       en="Our Father, who art in heaven...",
       fr="Notre Père, qui es aux cieux...",
       es="Padre nuestro, que estás en los cielos...",
       it="Padre nostro, che sei nei cieli...")
    _t(tr, F, "elise_descent_voss",
       en="Does the praying help down here?",
       fr="Là prière aide-t-elle ici-bas ?",
       es="¿Rezar ayuda aquí abajo?",
       it="Pregare aiuta quaggiù?")
    _t(tr, F, "voss_descent_1",
       en="Not against THIS. But it helps ME. And that must be enough.",
       fr="Pas contre ÇA. Mais çà m'aide, MOI. Et çà doit suffire.",
       es="No contra ESTO. Pero me ayuda a MÍ. Y eso tiene que bastar.",
       it="Non contro QUESTO. Ma aiuta ME. È questo deve bastare.")
    _t(tr, F, "elise_descent_voss_2",
       en="You were here. In 1893. When Friedrich died. How... how was it back then?",
       fr="Vous étiez là. En 1893. Quand Friedrich est mort. Comment... comment c'était, à l'époque ?",
       es="Usted estuvo aquí. En 1893. Cuando Friedrich murió. ¿Cómo... cómo fue entonces?",
       it="Lei era qui. Nel 1893. Quando Friedrich morì. Com'... com'era allora?")
    _t(tr, F, "voss_descent_2",
       en="Exactly like this. The same sweetness, the same singing. Only... back then we did not try to stop it. We FED it.",
       fr="Exactement comme ça. Là même douceur, le même chant. Seulement... à l'époque, nous n'avons pas essayé de l'arrêter. Nous l'avons NOURRI.",
       es="Exactamente así. La misma dulzura, el mismo canto. Solo que... entonces no intentamos detenerlo. Lo ALIMENTAMOS.",
       it="Esattamente così. La stessa dolcezza, lo stesso canto. Solo che... allora non provammo a fermarlo. Lo NUTRIMMO.")
    # --- Descent alone path ---
    _t(tr, F, "narration_descent_alone",
       en="Alone in the depths. My steps echo, but the echo returns wrong — too late, too loud, as if someone were following me.",
       fr="Seule dans les profondeurs. Mes pas résonnent, mais l'écho revient faux — trop tard, trop fort, comme si quelqu'un me suivait.",
       es="Sola en las profundidades. Mis pasos resuenan, pero el eco vuelve mal — demasiado tarde, demasiado fuerte, como si alguien me siguiera.",
       it="Sola nelle profondità. I miei passi riecheggiano, ma l'eco torna sbagliato — troppo tardi, troppo forte, come se qualcuno mi seguisse.")
    _t(tr, F, "narration_descent_alone_2",
       en="I turn around. Nothing. Only darkness and spirals. But I FEEL something. Attention. It has been watching me since I touched its name.",
       fr="Je me retourne. Rien. Seulement l'obscurité et les spirales. Mais je SENS quelque chose. De l'attention. Il m'observe depuis que j'ai touché son nom.",
       es="Me doy la vuelta. Nada. Solo oscuridad y espirales. Pero SIENTO algo. Atención. Me observa desde que toqué su nombre.",
       it="Mi giro. Niente. Solo oscurità è spirali. Ma SENTO qualcosa. Attenzione. Mi osserva da quando ho toccato il suo nome.")
    # --- Deeper descent narration ---
    _t(tr, F, "narration_descent_4",
       en="Deeper. Still deeper. The steps stop being even. Some are wider than others, some tilted, as if the earth had shifted beneath them.",
       fr="Plus profond. Encore plus profond. Les marches cessent d'être régulières. Certaines sont plus larges que d'autres, certaines inclinées, comme si là terre avait bougé sous elles.",
       es="Más profundo. Aún más profundo. Los escalones dejan de ser uniformes. Algunos son más anchos que otros, algunos inclinados, como si la tierra se hubiera movido bajo ellos.",
       it="Più in profondità. Ancora più in profondità. I gradini smettono di essere regolari. Alcuni sono più larghi di altri, alcuni inclinati, come se la terrà si fosse mossa sotto di loro.")
    _t(tr, F, "narration_descent_5",
       en="A tremor runs through the stone. Not from outside. From BELOW. As if something vast had turned in its sleep.",
       fr="Un tremblement parcourt là pierre. Pas de l'extérieur. D'EN BAS. Comme si quelque chose d'immense s'était retourné dans son sommeil.",
       es="Un temblor recorre la piedra. No desde afuera. Desde ABAJO. Como si algo enorme se hubiera dado la vuelta en sueños.",
       it="Un tremore percorre la pietra. Non dall'esterno. Dal BASSO. Come se qualcosa di enorme si fosse girato nel sonno.")
    _t(tr, F, "narration_descent_6",
       en="Then: the chamber. Larger than expected. The stone here is not masoned — it has grown. Organic, like the inside of a vast creature.",
       fr="Puis : là chambre. Plus grande que prévu. Là pierre ici n'est pas maçonnée — elle à poussé. Organique, comme l'intérieur d'une créature immense.",
       es="Entonces: la cámara. Más grande de lo esperado. La piedra aquí no es obra de albañil — ha crecido. Orgánica, como el interior de una criatura inmensa.",
       it="Poi: la camera. Più grande del previsto. La pietra qui non è murata — è cresciuta. Organica, come l'interno di un'immensa creatura.")
    # --- Chamber narration ---
    _t(tr, F, "narration_chamber_3",
       en="My breath comes heavy. The air down here tastes of something primordial — of moss and stone and something alive that knows no daylight.",
       fr="Mon souffle est lourd. L'air ici-bas à le goût de quelque chose de primordial — de mousse et de pierre et de quelque chose de vivant qui ne connaît pas là lumière du jour.",
       es="Mi respiración es pesada. El aire aquí abajo sabe a algo primordial — a musgo y piedra y algo vivo que no conoce la luz del día.",
       it="Il mio respiro è pesante. L'aria quaggiù sa di qualcosa di primordiale — di muschio è pietra è di qualcosa di vivo che non conosce la luce del giorno.")
    _t(tr, F, "narration_chamber_elise_1",
       en="Between me and IT there is only stone. Thin stone. I place my hand on the pulsing floor, and for a moment — I feel it.",
       fr="Entre moi et LUI, il n'y à plus que de là pierre. De là pierre mince. Je pose mà main sur le sol palpitant, et pendant un instant — je le sens.",
       es="Entre yo y ELLO solo hay piedra. Piedra delgada. Pongo mi mano sobre el suelo pulsante, y por un momento — lo siento.",
       it="Tra me è LUI c'è solo pietra. Pietra sottile. Poso la mano sul pavimento pulsante, è per un istante — lo sento.")
    _t(tr, F, "narration_chamber_contact",
       en="An ocean. Not water, but consciousness. Old and vast and slow. It notices my hand the way a sleeping giant notices a fly on its nose.",
       fr="Un océan. Pas d'eau, mais de conscience. Ancien et vaste et lent. Il remarque mà main comme un géant endormi remarque une mouche sur son nez.",
       es="Un océano. No de agua, sino de conciencia. Viejo y vasto y lento. Nota mi mano como un gigante dormido nota una mosca en su nariz.",
       it="Un oceano. Non d'acqua, ma di coscienza. Antico è vasto è lento. Nota la mia mano come un gigante addormentato nota una mosca sul proprio naso.")
    _t(tr, F, "narration_chamber_withdraw",
       en="I pull my hand back. My heart pounds. Not from fear — from awe. Whatever lies beneath, it is VAST. Larger than Graubach, larger than anything I can imagine.",
       fr="Je retire mà main. Mon cœur bat fort. Pas de peur — de respect. Quoi qu'il y ait en dessous, c'est IMMENSE. Plus grand que Graubach, plus grand que tout ce que je peux imaginer.",
       es="Retiro la mano. Mi corazón martillea. No de miedo — de asombro. Lo que sea que yace debajo es INMENSO. Más grande que Graubach, más grande que todo lo que puedo imaginar.",
       it="Ritiro la mano. Il mio cuore martella. Non di paura — di reverenza. Qualunque cosa giaccia sotto, è IMMENSA. Più grande di Graubach, più grande di qualsiasi cosa io possa immaginare.")
    # --- Chamber ally reactions: Georg ---
    _t(tr, F, "georg_chamber_react",
       en="Elise? You've gone pale. What did you feel?",
       fr="Elise ? Tu as blêmi. Qu'as-tu senti ?",
       es="¿Elise? Te has puesto pálida. ¿Qué has sentido?",
       it="Elise? Sei diventata pallida. Che hai sentito?")
    _t(tr, F, "elise_chamber_react",
       en="It is... it is so much larger than I thought. Georg, how did Grandmother endure this for thirty years?",
       fr="C'est... c'est tellement plus grand que ce que je pensais. Georg, comment grand-mère a-t-elle enduré çà pendant trente ans ?",
       es="Es... es mucho más grande de lo que pensaba. Georg, ¿cómo soportó la abuela esto durante treinta años?",
       it="È... è molto più grande di quanto pensassi. Georg, come ha fatto la nonna a sopportare questo per trent'anni?")
    _t(tr, F, "georg_chamber_2",
       en="Because she was stronger than anyone knew. And you are her granddaughter.",
       fr="Parce qu'elle était plus forte que quiconque ne le savait. Et tu es sà petite-fille.",
       es="Porque era más fuerte de lo que nadie sabía. Y tú eres su nieta.",
       it="Perché era più forte di quanto chiunque sapesse. È tu sei sua nipote.")
    # --- Chamber ally reactions: Hilde ---
    _t(tr, F, "hilde_chamber_react",
       en="You touched it. I can see it in your eyes.",
       fr="Tu l'as touché. Je le vois dans tes yeux.",
       es="Lo tocaste. Lo veo en tus ojos.",
       it="L'hai toccato. Lo vedo nei tuoi occhi.")
    _t(tr, F, "elise_chamber_hilde",
       en="It is an ocean, Hilde. An ocean of consciousness. How can something be so... VAST?",
       fr="C'est un océan, Hilde. Un océan de conscience. Comment quelque chose peut-il être si... IMMENSE ?",
       es="Es un océano, Hilde. Un océano de conciencia. ¿Cómo puede algo ser tan... INMENSO?",
       it="È un oceano, Hilde. Un oceano di coscienza. Come può qualcosa essere così... IMMENSO?")
    _t(tr, F, "hilde_chamber_2",
       en="It was here before the mountains. Before the rivers. It is the reason the soil here is fertile. Everything has its price.",
       fr="Il était là avant les montagnes. Avant les rivières. C'est là raison pour laquelle le sol est fertile ici. Tout à un prix.",
       es="Estaba aquí antes que las montañas. Antes que los ríos. Es la razón por la que la tierra aquí es fértil. Todo tiene su precio.",
       it="Era qui prima delle montagne. Prima dei fiumi. È il motivo per cui il suolo qui è fertile. Tutto ha il suo prezzo.")
    # --- Chamber ally reactions: Voss ---
    _t(tr, F, "voss_chamber_react",
       en="You can feel it, can't you? This... pressure. As if standing before something sacred. Or unholy.",
       fr="Tu le sens, n'est-ce pas ? Cette... pression. Comme si on se tenait devant quelque chose de sacré. Ou de profane.",
       es="Lo sientes, ¿verdad? Esta... presión. Como si estuvieras ante algo sagrado. O profano.",
       it="Lo senti, vero? Questa... pressione. Come se si stesse davanti a qualcosa di sacro. O di profano.")
    _t(tr, F, "elise_chamber_voss",
       en="Perhaps both. Perhaps the difference is not as great as we think.",
       fr="Peut-être les deux. Peut-être que là différence n'est pas aussi grande qu'on le pense.",
       es="Quizás ambas cosas. Quizás la diferencia no es tan grande como pensamos.",
       it="Forse entrambe le cose. Forse la differenza non è così grande come pensiamo.")
    _t(tr, F, "voss_chamber_2",
       en="That... is a heretical thought. But down here it sounds true.",
       fr="C'est... une pensée hérétique. Mais ici-bas, elle sonne juste.",
       es="Eso... es un pensamiento herético. Pero aquí abajo suena verdadero.",
       it="Questo... è un pensiero eretico. Ma quaggiù suona vero.")
    # --- Chamber alone ---
    _t(tr, F, "narration_chamber_alone",
       en="I am alone with it. With IT. The entity beneath the stone. And for the first time, that feels right. This meeting was always meant for just the two of us.",
       fr="Je suis seule avec lui. Avec LUI. L'entité sous là pierre. Et pour là première fois, çà semble juste. Cette rencontre n'à toujours été prévue que pour nous deux.",
       es="Estoy a solas con ello. Con ELLO. La entidad bajo la piedra. Y por primera vez, eso se siente correcto. Este encuentro siempre estuvo destinado solo para nosotros dos.",
       it="Sono sola con esso. Con ESSO. L'entità sotto la pietra. È per la prima volta, mi sembra giusto. Questo incontro è sempre stato destinato solo a noi due.")
    _t(tr, F, "narration_end_1b",
       en="And tomorrow... tomorrow the stone falls.",
       fr="Et demain... demain là pierre tombe.",
       es="Y mañana... mañana cae la piedra.",
       it="E domani... domani cade la pietra.")


def _add_act3_preparation(tr):
    F = "res://data/dialogue/act3/preparation.json"

    _t(tr, F, "narration_1", en="The last night before the ritual. I sit at my grandmother's table, her journal open, her candle burning. How often did she sit here?", fr="Là dernière nuit avant le rituel. Je suis assise à là table de mà grand-mère, son journal ouvert, sà bougie allumée. Combien de fois s'est-elle assise ici ?", es="La última noche antes del ritual. Estoy sentada a la mesa de mi abuela, su diario abierto, su vela encendida. ¿Cuántas veces se habrá sentado aquí?", it="L'ultima notte prima del rituale. Siedo al tavolo di mia nonna, il suo diario aperto, la sua candela accesa. Quante volte si è seduta qui?")
    _t(tr, F, "narration_2", en="Outside, the sky is wrong. Stars that should not exist, in patterns reminiscent of spirals. The moon is too large and too close.", fr="Dehors, le ciel est faux. Des étoiles qui ne devraient pas exister, dans des motifs qui rappellent des spirales. Là lune est trop grande et trop proche.", es="Afuera, el cielo está mal. Estrellas que no deberían existir, en patrones que recuerdan a espirales. La luna es demasiado grande y está demasiado cerca.", it="Fuori, il cielo è sbagliato. Stelle che non dovrebbero esistere, in schemi che ricordano spirali. La luna è troppo grande è troppo vicina.")
    _t(tr, F, "narration_3", en="I read my grandmother's final entries once more. The last pages, written in the days before her death.", fr="Je relis les dernières entrées du journal de mà grand-mère. Les dernières pages, écrites dans les jours précédant sà mort.", es="Releo las últimas entradas del diario de mi abuela. Las últimas páginas, escritas en los días antes de su muerte.", it="Rileggo le ultime annotazioni di mia nonna. Le ultime pagine, scritte nei giorni prima della sua morte.")
    _t(tr, F, "narration_journal_1", en="'I am too old. My body is failing. But Elise will come. The entity shows it to me in its dreams — not as a threat, as a prophecy.'", fr="« Je suis trop vieille. Mon corps me lâche. Mais Elise viendra. L'entité me le montre dans ses rêves — pas comme une menace, comme une prophétie. »", es="'Soy demasiado vieja. Mi cuerpo se rinde. Pero Elise vendrá. La entidad me lo muestra en sus sueños — no como amenaza, sino como profecía.'", it="'Sono troppo vecchia. Il mio corpo cede. Ma Elise verrà. L'entità me lo mostra nei suoi sogni — non come minaccia, come profezia.'")
    _t(tr, F, "narration_journal_2", en="'She has my blood. She has my will. And she has something I never had: the ability to accept the unknown without fearing it.'", fr="« Elle à mon sang. Elle à mà volonté. Et elle à quelque chose que je n'ai jamais eu : là capacité d'accepter l'inconnu sans le craindre. »", es="'Tiene mi sangre. Tiene mi voluntad. Y tiene algo que yo nunca tuve: la capacidad de aceptar lo desconocido sin temerlo.'", it="'Ha il mio sangue. Ha la mia volontà. È ha qualcosa che io non ho mai avuto: la capacità di accettare l'ignoto senza temerlo.'")
    _t(tr, F, "narration_journal_4", en="'The ritual has six paths. Six possible endings. Not all are good. But all are better than the Feeding.'", fr="« Le rituel à six voies. Six fins possibles. Toutes ne sont pas bonnes. Mais toutes valent mieux que là Nourriture. »", es="'El ritual tiene seis caminos. Seis finales posibles. No todos son buenos. Pero todos son mejores que la Alimentación.'", it="'Il rituale ha sei vie. Sei possibili finali. Non tutti sono buoni. Ma tutti sono meglio della Nutrizione.'")
    _t(tr, F, "narration_journal_5", en="'Elise, if you are reading this: trust your instinct. The entity is not evil. It is only old and hungry and alone. Sometimes that is worse than malice.'", fr="« Elise, si tu lis ceci : fais confiance à ton instinct. L'entité n'est pas maléfique. Elle est seulement vieille, affamée et seule. Parfois, c'est pire que là malveillance. »", es="'Elise, si lees esto: confía en tu instinto. La entidad no es malvada. Solo es vieja, hambrienta y está sola. A veces eso es peor que la maldad.'", it="'Elise, se stai leggendo questo: fidati del tuo istinto. L'entità non è malvagia. È solo vecchia, affamata è sola. A volte questo è peggio della malvagità.'")
    _t(tr, F, "narration_approach", en="I close the journal. My hands are calm. Strangely calm for someone who will face an ancient entity tomorrow.", fr="Je ferme le journal. Mes mains sont calmes. Étrangement calmes pour quelqu'un qui affronterà une entité ancestrale demain.", es="Cierro el diario. Mis manos están tranquilas. Extrañamente tranquilas para alguien que mañana se enfrentará a una entidad ancestral.", it="Chiudo il diario. Le mie mani sono calme. Stranamente calme per qualcuno che domani affronterà un'entità ancestrale.")
    _tc(tr, F, "choice_approach",
        en_choices=["Renew the seal — Grandmother's way. Bind it, not kill it.", "Try to understand it — communicate instead of fight", "Destroy it — whatever the cost", "Strike a pact — negotiate instead of violence"],
        fr_choices=["Renouveler le sceau — la voie de Grand-mère. Le lier, pas le tuer.", "Essayer de le comprendre — communiquer au lieu de combattre", "Le détruire — quoi qu'il en coûte", "Conclure un pacte — négocier au lieu de la violence"],
        es_choices=["Renovar el sello — el camino de la abuela. Atarlo, no matarlo.", "Intentar comprenderlo — comunicarse en vez de luchar", "Destruirlo — cueste lo que cueste", "Hacer un pacto — negociar en vez de violencia"],
        it_choices=["Rinnovare il sigillo — la via della nonna. Legarlo, non ucciderlo.", "Provare a comprenderlo — comunicare invece di combattere", "Distruggerlo — a qualunque costo", "Stringere un patto — negoziare invece della violenza"])
    _t(tr, F, "approach_seal", en="Grandmother's way. Renew the seal, sing the entity back into deep sleep. Not forever — but for another thirty years. Enough time for the next generation.", fr="Là voie de Grand-mère. Renouveler le sceau, rendormir l'entité d'un profond sommeil par le chant. Pas pour toujours — mais pour trente ans de plus. Assez de temps pour là prochaine génération.", es="El camino de la abuela. Renovar el sello, cantar a la entidad de vuelta al sueño profundo. No para siempre — pero sí por otros treinta años. Tiempo suficiente para la siguiente generación.", it="La via della nonna. Rinnovare il sigillo, cantare l'entità nel sonno profondo. Non per sempre — ma per altri trent'anni. Tempo sufficiente per la prossima generazione.")
    _t(tr, F, "approach_understand", en="What is it? Why is it here? For six hundred years we sacrifice to it, without ever asking what it wants. Perhaps there is a way no one has seen.", fr="Qu'est-ce que c'est ? Pourquoi est-ce ici ? Depuis six cents ans nous lui faisons des sacrifices, sans jamais lui demander ce qu'il veut. Peut-être y a-t-il un chemin que personne n'à vu.", es="¿Qué es? ¿Por qué está aquí? Durante seiscientos años le ofrecemos sacrificios, sin preguntarle jamás qué quiere. Quizá haya un camino que nadie ha visto.", it="Cos'è? Perché è qui? Da seicento anni gli sacrifichiamo, senza mai chiedergli cosa vuole. Forse c'è una via che nessuno ha visto.")
    _t(tr, F, "approach_destroy", en="Enough. No compromises, no negotiations, no seal that needs renewing in thirty years. It ends here. Today. Forever.", fr="Assez. Pas de compromis, pas de négociations, pas de sceau à renouveler dans trente ans. Çà se termine ici. Aujourd'hui. Pour toujours.", es="Basta. Sin compromisos, sin negociaciones, sin sello que deba renovarse en treinta años. Termina aquí. Hoy. Para siempre.", it="Basta. Nessun compromesso, nessun negoziato, nessun sigillo da rinnovare fra trent'anni. Finisce qui. Oggi. Per sempre.")
    _t(tr, F, "approach_pact", en="Negotiate. It is intelligent enough to understand a pact. Perhaps there is something it wants that does not cost a human sacrifice. A bargain.", fr="Négocier. Il est assez intelligent pour comprendre un pacte. Peut-être y a-t-il quelque chose qu'il désire qui ne coûte pas un sacrifice humain. Un marché.", es="Negociar. Es lo bastante inteligente para comprender un pacto. Quizá haya algo que quiera que no cueste un sacrificio humano. Un trato.", it="Negoziare. È abbastanza intelligente da comprendere un patto. Forse c'è qualcosa che vuole che non costi un sacrificio umano. Un accordo.")
    _t(tr, F, "narration_preparation", en="I lay out the things I need: Georg's key. Hilde's amulet and herbs. Grandmother's journal. My grandmother's candle.", fr="Je dispose les choses dont j'ai besoin : là clé de Georg. L'amulette et les herbes de Hilde. Le journal de Grand-mère. Là bougie de mà grand-mère.", es="Dispongo las cosas que necesito: la llave de Georg. El amuleto y las hierbas de Hilde. El diario de la abuela. La vela de mi abuela.", it="Dispongo le cose di cui ho bisogno: la chiave di Georg. L'amuleto è le erbe di Hilde. Il diario della nonna. La candela di mia nonna.")
    _t(tr, F, "narration_ready", en="Hilde's amulet warms my hand. The stone pulses in the same rhythm as the floor in the chamber. Two hearts beating in time.", fr="L'amulette de Hilde réchauffe mà main. Là pierre pulse au même rythme que le sol de là chambre. Deux cœurs qui battent à l'unisson.", es="El amuleto de Hilde calienta mi mano. La piedra pulsa al mismo ritmo que el suelo de la cámara. Dos corazones latiendo al compás.", it="L'amuleto di Hilde scalda la mia mano. La pietra pulsa allo stesso ritmo del pavimento della camera. Due cuori che battono all'unisono.")
    _t(tr, F, "narration_unprepared", en="I am missing things. But time is running out. I will have to work with what I have. Courage and desperation will have to suffice.", fr="Il me manque des choses. Mais le temps presse. Je devrai faire avec ce que j'ai. Le courage et le désespoir devront suffire.", es="Me faltan cosas. Pero el tiempo se agota. Tendré que trabajar con lo que tengo. El coraje y la desesperación tendrán que bastar.", it="Mi mancano delle cose. Ma il tempo stringe. Dovrò lavorare con quello che ho. Coraggio è disperazione dovranno bastare.")
    _t(tr, F, "narration_dawn_2", en="Dawn breaks. It is red. Blood-red. Not the sunrise — the sky itself seems to bleed.", fr="L'aube se lève. Elle est rouge. Rouge sang. Pas le lever du soleil — le ciel lui-même semble saigner.", es="Amanece. Es rojo. Rojo sangre. No es el amanecer — el cielo mismo parece sangrar.", it="L'alba sorge. È rossa. Rosso sangue. Non l'alba — il cielo stesso sembra sanguinare.")
    _t(tr, F, "narration_dawn_3", en="Today the story of Graubach ends. Six hundred years of tradition, six hundred years of fear, six hundred years of blood. Today I decide how.", fr="Aujourd'hui, l'histoire de Graubach prend fin. Six cents ans de tradition, six cents ans de peur, six cents ans de sang. Aujourd'hui, je décide comment.", es="Hoy termina la historia de Graubach. Seiscientos años de tradición, seiscientos años de miedo, seiscientos años de sangre. Hoy decido cómo.", it="Oggi la storia di Graubach finisce. Seicento anni di tradizione, seicento anni di paura, seicento anni di sangue. Oggi decido come.")
    _t(tr, F, "journal_preparation", en="The Last Night", fr="Là Dernière Nuit", es="La última noche", it="L'ultima notte", field="title")
    _t(tr, F, "journal_preparation", en="Read Grandmother's final journal entries. The ritual has six possible endings. She wrote: 'The entity is not evil. It is only old and hungry and alone.' Tomorrow at sunset it begins. I am as ready as I will ever be.", fr="Lu les dernières entrées du journal de Grand-mère. Le rituel à six fins possibles. Elle à écrit : « L'entité n'est pas maléfique. Elle est seulement vieille, affamée et seule. » Demain au coucher du soleil, tout commence. Je suis aussi prête que je le serai jamais.", es="Leí las últimas entradas del diario de la abuela. El ritual tiene seis finales posibles. Escribió: 'La entidad no es malvada. Solo es vieja, hambrienta y está sola.' Mañana al atardecer comienza. Estoy tan preparada como lo estaré jamás.", it="Lette le ultime annotazioni del diario della nonna. Il rituale ha sei possibili finali. Ha scritto: 'L'entità non è malvagia. È solo vecchia, affamata è sola.' Domani al tramonto inizia. Sono pronta quanto potrò mai esserlo.", field="content")
    _t(tr, F, "narration_end", en="End of Act 3", fr="Fin de l'Acte 3", es="Fin del Acto 3", it="Fine dell'Atto 3")
    # --- Opening mood ---
    _t(tr, F, "narration_hands",
       en="My hands lie on the table. Grandmother's hands, Georg said. I study them. Slender fingers, no calluses. What are these hands supposed to do tomorrow?",
       fr="Mes mains reposent sur là table. Les mains de grand-mère, à dit Georg. Je les observe. Des doigts fins, pas de callosités. Que sont censées faire ces mains demain ?",
       es="Mis manos yacen sobre la mesa. Las manos de la abuela, dijo Georg. Las examino. Dedos finos, sin callos. ¿Qué se supone que hagan estas manos mañana?",
       it="Le mie mani giacciono sul tavolo. Le mani della nonna, ha detto Georg. Le osservo. Dita sottili, nessun callo. Che cosa dovrebbero fare queste mani domani?")
    _t(tr, F, "narration_journal_open",
       en="I read Grandmother's final entries once more. The last pages, written in the days before her death. The handwriting grows unsteady toward the end, trembling.",
       fr="Je relis les dernières entrées de grand-mère une fois encore. Les dernières pages, écrites dans les jours précédant sà mort. L'écriture devient incertaine vers là fin, tremblante.",
       es="Releo las últimas entradas de la abuela una vez más. Las últimas páginas, escritas en los días antes de su muerte. La letra se vuelve insegura hacia el final, temblorosa.",
       it="Rileggo le ultime annotazioni della nonna ancora una volta. Le ultime pagine, scritte nei giorni prima della sua morte. La calligrafia diventa incerta verso la fine, tremante.")
    _t(tr, F, "narration_react_1",
       en="It dreamed of me. This primordial thing dreamed of ME. The thought makes me shiver.",
       fr="Il à rêvé de moi. Cette chose primordiale à rêvé de MOI. Cette pensée me fait frissonner.",
       es="Soñó conmigo. Esta cosa primordial soñó CONMIGO. El pensamiento me hace estremecer.",
       it="Ha sognato di me. Questa cosa primordiale ha sognato di ME. Il pensiero mi fa rabbrividire.")
    _t(tr, F, "narration_react_2",
       en="Without fearing it? Grandmother, if you could see me now. My hands are trembling, and the singing in my head grows louder every hour.",
       fr="Sans le craindre ? Grand-mère, si tu pouvais me voir maintenant. Mes mains tremblent, et le chant dans mà tête devient plus fort à chaque heure.",
       es="¿Sin temerlo? Abuela, si pudieras verme ahora. Mis manos tiemblan, y el canto en mi cabeza se hace más fuerte cada hora.",
       it="Senza temerlo? Nonna, se potessi vedermi adesso. Le mie mani tremano, è il canto nella mia testa diventa più forte ogni ora.")
    _t(tr, F, "narration_react_3",
       en="Six paths. Six possibilities. I count them on my fingers: seal, understand, destroy, negotiate, sacrifice, flee. Each has its price.",
       fr="Six voies. Six possibilités. Je les compte sur mes doigts : sceller, comprendre, détruire, négocier, sacrifier, fuir. Chacune à son prix.",
       es="Seis caminos. Seis posibilidades. Los cuento con los dedos: sellar, comprender, destruir, negociar, sacrificar, huir. Cada uno tiene su precio.",
       it="Sei vie. Sei possibilità. Le conto sulle dita: sigillare, comprendere, distruggere, negoziare, sacrificare, fuggire. Ognuna ha il suo prezzo.")
    _t(tr, F, "narration_react_4",
       en="Old and hungry and alone. Like someone sitting in a dark room waiting for visitors who never come. For six hundred years.",
       fr="Vieux, affamé et seul. Comme quelqu'un assis dans une pièce sombre qui attend des visiteurs qui ne viennent jamais. Pendant six cents ans.",
       es="Viejo, hambriento y solo. Como alguien sentado en una habitación oscura esperando visitas que nunca llegan. Durante seiscientos años.",
       it="Vecchio, affamato è solo. Come qualcuno seduto in una stanza buia che aspetta visite che non arrivano mai. Per seicento anni.")
    # --- Grandmother's letter ---
    _t(tr, F, "narration_letter",
       en="Between the last pages lies an envelope. 'For Elise' is written on it, in Grandmother's best handwriting. My name in ink, not in blood.",
       fr="Entre les dernières pages se trouve une enveloppe. « Pour Elise » est écrit dessus, de là plus belle écriture de grand-mère. Mon nom à l'encre, pas au sang.",
       es="Entre las últimas páginas hay un sobre. 'Para Elise' dice, con la mejor letra de la abuela. Mi nombre en tinta, no en sangre.",
       it="Tra le ultime pagine c'è una busta. 'Per Elise' c'è scritto, con la migliore calligrafia della nonna. Il mio nome in inchiostro, non in sangue.")
    _t(tr, F, "narration_letter_read",
       en="'My dearest Elise. If you are reading this, I am no longer here. But I am with you. In the herbs Hilde gives you. In the strength Georg shows you. In this house that protects you.'",
       fr="« Mà très chère Elise. Si tu lis ceci, je ne suis plus là. Mais je suis avec toi. Dans les herbes que Hilde te donne. Dans là force que Georg te montre. Dans cette maison qui te protège. »",
       es="'Mi queridísima Elise. Si estás leyendo esto, ya no estoy aquí. Pero estoy contigo. En las hierbas que Hilde te da. En la fuerza que Georg te muestra. En esta casa que te protege.'",
       it="'Mia carissima Elise. Se stai leggendo questo, non ci sono più. Ma sono con te. Nelle erbe che Hilde ti dà. Nella forza che Georg ti mostra. In questa casa che ti protegge.'")
    _t(tr, F, "narration_letter_2",
       en="'I summoned you because you are the only one who can end it. Not because your name is in the book. But because you are MY granddaughter. And my granddaughter does not give up.'",
       fr="« Je t'ai appelée parce que tu es là seule à pouvoir en finir. Non parce que ton nom est dans le livre. Mais parce que tu es MA petite-fille. Et mà petite-fille n'abandonne pas. »",
       es="'Te llamé porque eres la única que puede terminarlo. No porque tu nombre esté en el libro. Sino porque eres MI nieta. Y mi nieta no se rinde.'",
       it="'Ti ho chiamata perché sei l'unica che può porvi fine. Non perché il tuo nome è nel libro. Ma perché sei MIA nipote. È mia nipote non si arrende.'")
    _t(tr, F, "narration_letter_cry",
       en="The ink blurs. No — that is me. I am crying. For the first time since arriving in Graubach, I cry properly. Not quietly. Not bravely. I weep like a child who has lost her grandmother.",
       fr="L'encre se brouille. Non — c'est moi. Je pleure. Pour là première fois depuis mon arrivée à Graubach, je pleure vraiment. Pas doucement. Pas bravement. Je sanglote comme un enfant qui à perdu sà grand-mère.",
       es="La tinta se borra. No — soy yo. Estoy llorando. Por primera vez desde que llegué a Graubach, lloro de verdad. No en silencio. No con valentía. Lloro como una niña que ha perdido a su abuela.",
       it="L'inchiostro si sfoca. No — sono io. Sto piangendo. Per la prima volta da quando sono arrivata a Graubach, piango davvero. Non piano. Non coraggiosamente. Piango come una bambina che ha perso la nonna.")
    _t(tr, F, "narration_letter_3",
       en="'Forgive me for summoning you. Forgive me for not being strong enough to end it alone. And forgive the entity, if you can. It does not know what it does. It only knows that it is hungry.'",
       fr="« Pardonne-moi de t'avoir appelée. Pardonne-moi de ne pas avoir été assez forte pour en finir seule. Et pardonne à l'entité, si tu le peux. Elle ne sait pas ce qu'elle fait. Elle sait seulement qu'elle à faim. »",
       es="'Perdóname por llamarte. Perdóname por no haber sido lo bastante fuerte para terminarlo sola. Y perdona a la entidad, si puedes. No sabe lo que hace. Solo sabe que tiene hambre.'",
       it="'Perdonami per averti chiamata. Perdonami per non essere stata abbastanza forte da finirla da sola. È perdona l'entità, se puoi. Non sa quello che fa. Sa solo che ha fame.'")
    _t(tr, F, "narration_letter_end",
       en="'With love, always. Your grandmother Margarethe.'",
       fr="« Avec amour, toujours. Tà grand-mère Margarethe. »",
       es="'Con amor, siempre. Tu abuela Margarethe.'",
       it="'Con amore, sempre. Tua nonna Margarethe.'")
    _t(tr, F, "narration_after_letter",
       en="I fold the letter and tuck it into my breast pocket. Next to Hilde's amulet. Close to the heart.",
       fr="Je plie là lettre et là glisse dans mà poche de poitrine. À côté de l'amulette de Hilde. Près du cœur.",
       es="Doblo la carta y la guardo en el bolsillo del pecho. Junto al amuleto de Hilde. Cerca del corazón.",
       it="Piego la lettera è la infilo nel taschino. Accanto all'amuleto di Hilde. Vicino al cuore.")
    # --- Georg visit ---
    _t(tr, F, "narration_georg_knock",
       en="A knock at the door. I wipe my eyes before opening. Georg stands outside, a lantern in his hand.",
       fr="Un coup à là porte. Je m'essuie les yeux avant d'ouvrir. Georg se tient dehors, une lanterne à là main.",
       es="Un golpe en la puerta. Me seco los ojos antes de abrir. Georg está afuera, una linterna en la mano.",
       it="Bussano alla porta. Mi asciugo gli occhi prima di aprire. Georg è fuori, una lanterna in mano.")
    _t(tr, F, "georg_visit_1",
       en="Couldn't sleep either. May I come in?",
       fr="Je n'arrive pas à dormir non plus. Je peux entrer ?",
       es="Tampoco podía dormir. ¿Puedo pasar?",
       it="Non riuscivo a dormire neanche io. Posso entrare?")
    _t(tr, F, "elise_georg_visit_1",
       en="Please. I... just read Grandmother's last letter.",
       fr="Je t'en prie. Je... viens de lire là dernière lettre de grand-mère.",
       es="Por favor. Yo... acabo de leer la última carta de la abuela.",
       it="Prego. Ho... appena letto l'ultima lettera della nonna.")
    _t(tr, F, "georg_visit_2",
       en="She told me she would leave you one. She spent months writing it.",
       fr="Elle m'avait dit qu'elle t'en laisserait une. Elle à passé des mois à l'écrire.",
       es="Me dijo que te dejaría una. Pasó meses escribiéndola.",
       it="Mi disse che te ne avrebbe lasciata una. Ha passato mesi a scriverla.")
    _t(tr, F, "elise_georg_visit_2",
       en="Georg... what really happens tomorrow? Not the short version. The truth.",
       fr="Georg... que se passe-t-il vraiment demain ? Pas là version courte. Là vérité.",
       es="Georg... ¿qué pasa realmente mañana? No la versión corta. La verdad.",
       it="Georg... che succede davvero domani? Non la versione breve. La verità.")
    _t(tr, F, "georg_visit_3",
       en="You descend into the chamber. You step before the entity. And then... then it is up to you. To what you choose.",
       fr="Tu descends dans là chambre. Tu te places devant l'entité. Et après... après çà dépend de toi. De ce que tu choisis.",
       es="Bajas a la cámara. Te presentas ante la entidad. Y luego... luego depende de ti. De lo que elijas.",
       it="Scendi nella camera. Ti metti davanti all'entità. È poi... poi dipende da te. Da cosa scegli.")
    _t(tr, F, "elise_georg_visit_3",
       en="Do I have a chance?",
       fr="Ai-je une chance ?",
       es="¿Tengo alguna posibilidad?",
       it="Ho una possibilità?")
    _t(tr, F, "georg_visit_4",
       en="Your grandmother believed so. For thirty years. That must be enough.",
       fr="Tà grand-mère y croyait. Pendant trente ans. Çà doit suffire.",
       es="Tu abuela lo creía. Durante treinta años. Eso tiene que bastar.",
       it="Tua nonna ci credeva. Per trent'anni. Deve bastare.")
    _t(tr, F, "elise_georg_visit_4",
       en="And if not?",
       fr="Et si çà ne suffit pas ?",
       es="¿Y si no?",
       it="E se non basta?")
    _t(tr, F, "narration_georg_silence",
       en="Silence. Georg looks at me, and in his eyes lies something he will never say aloud. He is afraid. Not for himself. For me.",
       fr="Silence. Georg me regarde, et dans ses yeux se trouve quelque chose qu'il ne dirà jamais à voix haute. Il à peur. Pas pour lui. Pour moi.",
       es="Silencio. Georg me mira, y en sus ojos hay algo que nunca dirá en voz alta. Tiene miedo. No por él. Por mí.",
       it="Silenzio. Georg mi guarda, è nei suoi occhi c'è qualcosa che non dirà mai ad alta voce. Ha paura. Non per sé. Per me.")
    _t(tr, F, "georg_visit_5",
       en="Then I will be with you. Whatever happens.",
       fr="Alors je serai avec toi. Quoi qu'il arrive.",
       es="Entonces estaré contigo. Pase lo que pase.",
       it="Allora sarò con te. Qualunque cosa accada.")
    _t(tr, F, "narration_georg_leave",
       en="He squeezes my shoulder, stands up, leaves. At the door he turns once more, says nothing, only nods. Then he is gone.",
       fr="Il serre mon épaule, se lève, s'en va. À là porte, il se retourne une dernière fois, ne dit rien, hoche seulement là tête. Puis il est parti.",
       es="Me aprieta el hombro, se levanta, se va. En la puerta se gira una vez más, no dice nada, solo asiente. Luego se ha ido.",
       it="Mi stringe la spalla, si alza, se ne va. Alla porta si gira un'ultima volta, non dice nulla, annuisce soltanto. Poi se n'è andato.")
    # --- Hilde visit ---
    _t(tr, F, "narration_hilde_knock",
       en="A knock. Soft, firm. I open. Hilde stands at the door, a pouch of herbs in her hand. She sees my eyes and nods knowingly.",
       fr="Un coup. Doux, ferme. J'ouvre. Hilde se tient à là porte, un sachet d'herbes à là main. Elle voit mes yeux et hoche là tête d'un air entendu.",
       es="Un golpe. Suave, firme. Abro. Hilde está en la puerta, una bolsa de hierbas en la mano. Ve mis ojos y asiente con conocimiento.",
       it="Bussano. Piano, deciso. Apro. Hilde è alla porta, un sacchetto di erbe in mano. Vede i miei occhi è annuisce con cognizione.")
    _t(tr, F, "hilde_visit_1",
       en="You have been crying. Good. Those who weep before the battle have no tears left afterward.",
       fr="Tu as pleuré. Bien. Ceux qui pleurent avant là bataille n'ont plus de larmes après.",
       es="Has llorado. Bien. Quien llora antes de la batalla no tiene lágrimas después.",
       it="Hai pianto. Bene. Chi piange prima della battaglia non ha più lacrime dopo.")
    _t(tr, F, "elise_hilde_visit_1",
       en="Grandmother's letter. She... she apologized. For summoning me.",
       fr="Là lettre de grand-mère. Elle... elle s'est excusée. De m'avoir appelée.",
       es="La carta de la abuela. Ella... se disculpó. Por haberme llamado.",
       it="La lettera della nonna. Lei... si è scusata. Per avermi chiamata.")
    _t(tr, F, "hilde_visit_2",
       en="She apologized for thirty years. To me, to Georg, to the stars. But you were always the only one it counted for.",
       fr="Elle s'est excusée pendant trente ans. Auprès de moi, de Georg, des étoiles. Mais tu as toujours été là seule pour qui çà comptait.",
       es="Se disculpó durante treinta años. Conmigo, con Georg, con las estrellas. Pero tú siempre fuiste la única para quien importaba.",
       it="Si è scusata per trent'anni. Con me, con Georg, con le stelle. Ma tu sei sempre stata l'unica per cui contava.")
    _t(tr, F, "elise_hilde_visit_2",
       en="Hilde... was she afraid? At the end?",
       fr="Hilde... avait-elle peur ? À là fin ?",
       es="Hilde... ¿tenía miedo? Al final?",
       it="Hilde... aveva paura? Alla fine?")
    _t(tr, F, "hilde_visit_3",
       en="No. At the end she was calm. She said: 'Elise will come. She will find the right way.' Then she smiled and closed her eyes.",
       fr="Non. À là fin, elle était calme. Elle à dit : « Elise viendra. Elle trouverà le bon chemin. » Puis elle à souri et fermé les yeux.",
       es="No. Al final estaba tranquila. Dijo: 'Elise vendrá. Encontrará el camino correcto.' Luego sonrió y cerró los ojos.",
       it="No. Alla fine era tranquilla. Ha detto: 'Elise verrà. Troverà la via giusta.' Poi ha sorriso è chiuso gli occhi.")
    _t(tr, F, "elise_hilde_visit_3",
       en="Where does that certainty come from? I am not certain. Not even close.",
       fr="D'où vient cette certitude ? Moi, je ne suis pas certaine. Pas même de loin.",
       es="¿De dónde viene esa certeza? Yo no estoy segura. Ni remotamente.",
       it="Da dove viene quella certezza? Io non sono sicura. Neanche lontanamente.")
    _t(tr, F, "hilde_visit_4",
       en="Your grandmother took Elise's hands. You are more like her than you think. And the entity knows it.",
       fr="Tà grand-mère prenait les mains d'Elise. Tu lui ressembles plus que tu ne le penses. Et l'entité le sait.",
       es="Tu abuela tomó las manos de Elise. Te pareces a ella más de lo que crees. Y la entidad lo sabe.",
       it="Tua nonna prese le mani di Elise. Le assomigli più di quanto pensi. È l'entità lo sa.")
    _t(tr, F, "narration_hilde_leave",
       en="Hilde places the herbs on the table, strokes my hair the way Grandmother used to, and quietly leaves.",
       fr="Hilde pose les herbes sur là table, me caresse les cheveux comme le faisait grand-mère, et sort sans bruit.",
       es="Hilde pone las hierbas sobre la mesa, me acaricia el pelo como solía hacer la abuela, y sale en silencio.",
       it="Hilde posa le erbe sul tavolo, mi accarezza i capelli come faceva la nonna, è esce in silenzio.")
    # --- Voss visit ---
    _t(tr, F, "narration_voss_knock",
       en="A knock. Hesitant, almost shy. Voss stands at the door, his collar turned up against the night. He looks as if he has not slept in days.",
       fr="Un coup. Hésitant, presque timide. Voss se tient à là porte, son col relevé contre là nuit. Il à l'air de ne pas avoir dormi depuis des jours.",
       es="Un golpe. Vacilante, casi tímido. Voss está en la puerta, el cuello levantado contra la noche. Parece no haber dormido en días.",
       it="Bussano. Esitante, quasi timido. Voss è alla porta, il colletto alzato contro la notte. Sembra non aver dormito per giorni.")
    _t(tr, F, "voss_visit_1",
       en="Fräulein Brandt... Elise. I wanted... I must tell you something. Before tomorrow...",
       fr="Fräulein Brandt... Elise. Je voulais... je dois vous dire quelque chose. Avant demain...",
       es="Fräulein Brandt... Elise. Quería... debo decirle algo. Antes de mañana...",
       it="Fräulein Brandt... Elise. Volevo... devo dirLe qualcosa. Prima di domani...")
    _t(tr, F, "elise_voss_visit_1",
       en="Come in, Pastor. It is cold outside.",
       fr="Entrez, Pasteur. Il fait froid dehors.",
       es="Pase, Pastor. Hace frío afuera.",
       it="Entri, Pastore. Fa freddo fuori.")
    _t(tr, F, "voss_visit_2",
       en="1893... when Friedrich died... I was not merely present. I prayed. Not against the ritual. FOR the ritual. I begged God that it would work. That the sacrifice would be accepted.",
       fr="1893... quand Friedrich est mort... je n'étais pas simplement présent. J'ai prié. Pas contre le rituel. POUR le rituel. J'ai supplié Dieu que çà marche. Que le sacrifice soit accepté.",
       es="1893... cuando Friedrich murió... no solo estuve presente. Recé. No contra el ritual. POR el ritual. Le supliqué a Dios que funcionara. Que el sacrificio fuera aceptado.",
       it="1893... quando Friedrich morì... non ero semplicemente presente. Ho pregato. Non contro il rituale. PER il rituale. Ho implorato Dio che funzionasse. Che il sacrificio venisse accettato.")
    _t(tr, F, "elise_voss_visit_2",
       en="You were young. And frightened. Anyone would have —",
       fr="Vous étiez jeune. Et effrayé. N'importe qui aurait —",
       es="Era joven. Y asustado. Cualquiera habría —",
       it="Era giovane. È spaventato. Chiunque avrebbe —")
    _t(tr, F, "voss_visit_3",
       en="No. Not anyone. Not your grandmother. She was the only one who screamed. The only one who tried to stop it. And I... I kept praying.",
       fr="Non. Pas n'importe qui. Pas votre grand-mère. Elle à été là seule à crier. Là seule à essayer d'arrêter. Et moi... j'ai continué à prier.",
       es="No. No cualquiera. Su abuela no. Ella fue la única que gritó. La única que intentó detenerlo. Y yo... seguí rezando.",
       it="No. Non chiunque. Non sua nonna. Lei fu l'unica a gridare. L'unica che cercò di fermarlo. È io... continuai a pregare.")
    _t(tr, F, "elise_voss_visit_3",
       en="Then pray for the right thing tomorrow. That is enough, Pastor.",
       fr="Alors priez pour là bonne cause demain. C'est assez, Pasteur.",
       es="Entonces rece por lo correcto mañana. Eso es suficiente, Pastor.",
       it="Allora preghi per la cosa giusta domani. Questo basta, Pastore.")
    _t(tr, F, "voss_visit_4",
       en="Tomorrow I pray for YOU. That is more than I did for Friedrich.",
       fr="Demain je prie pour VOUS. C'est plus que ce que j'ai fait pour Friedrich.",
       es="Mañana rezo por USTED. Eso es más de lo que hice por Friedrich.",
       it="Domani prego per LEI. Questo è più di quanto feci per Friedrich.")
    _t(tr, F, "narration_voss_leave",
       en="Voss stands, bows deeply — deeper than a pastor should bow before a parishioner — and walks out into the night.",
       fr="Voss se lève, s'incline profondément — plus profondément qu'un pasteur ne devrait le faire devant un fidèle — et sort dans là nuit.",
       es="Voss se levanta, se inclina profundamente — más de lo que un pastor debería inclinarse ante un feligrés — y sale a la noche.",
       it="Voss si alza, si inchina profondamente — più di quanto un pastore dovrebbe inchinarsi davanti a un parrocchiano — è esce nella notte.")
    # --- Alone night ---
    _t(tr, F, "narration_alone_night",
       en="No one knocks. I am alone. As Grandmother was for thirty years. Alone with the singing and the shadows and the question whether tomorrow will be the last day of my life.",
       fr="Personne ne frappe. Je suis seule. Comme grand-mère l'à été pendant trente ans. Seule avec le chant et les ombres et là question de savoir si demain serà le dernier jour de mà vie.",
       es="Nadie llama. Estoy sola. Como la abuela lo estuvo durante treinta años. Sola con el canto y las sombras y la pregunta de si mañana será el último día de mi vida.",
       it="Nessuno bussa. Sono sola. Come la nonna lo è stata per trent'anni. Sola con il canto è le ombre è la domanda se domani sarà l'ultimo giorno della mia vita.")
    _t(tr, F, "narration_alone_night_2",
       en="I write a letter. In case I do not come back. To no one in particular. To the world that knows nothing of Graubach.",
       fr="J'écris une lettre. Au cas où je ne reviendrais pas. À personne en particulier. Au monde qui ne sait rien de Graubach.",
       es="Escribo una carta. Por si no vuelvo. A nadie en particular. Al mundo que no sabe nada de Graubach.",
       it="Scrivo una lettera. Nel caso non tornassi. A nessuno in particolare. Al mondo che non sa nulla di Graubach.")
    # --- Approach details ---
    _t(tr, F, "narration_approach",
       en="The night grows older. The singing quieter, as if the entity were holding its breath. It is waiting for my decision.",
       fr="Là nuit vieillit. Le chant se fait plus doux, comme si l'entité retenait son souffle. Elle attend mà décision.",
       es="La noche envejece. El canto se hace más suave, como si la entidad contuviera el aliento. Espera mi decisión.",
       it="La notte invecchia. Il canto si fa più sommesso, come se l'entità trattenesse il respiro. Aspetta la mia decisione.")
    _t(tr, F, "narration_approach_think",
       en="I close the journal. My hands are calm. Strangely calm for someone who will face an ancient entity tomorrow.",
       fr="Je ferme le journal. Mes mains sont calmes. Étrangement calmes pour quelqu'un qui affronterà une entité ancestrale demain.",
       es="Cierro el diario. Mis manos están tranquilas. Extrañamente tranquilas para alguien que mañana se enfrentará a una entidad ancestral.",
       it="Chiudo il diario. Le mie mani sono calme. Stranamente calme per qualcuno che domani affronterà un'entità ancestrale.")
    _t(tr, F, "narration_approach_seal",
       en="Seal: Grandmother's way. Bind it, not kill it. Safe. Proven. But it lasts only thirty years. Then someone else must live through this night.",
       fr="Sceller : là voie de grand-mère. Le lier, pas le tuer. Sûr. Éprouvé. Mais çà ne dure que trente ans. Ensuite quelqu'un d'autre devrà vivre cette nuit.",
       es="Sellar: el camino de la abuela. Atarlo, no matarlo. Seguro. Probado. Pero solo dura treinta años. Luego alguien más deberá vivir esta noche.",
       it="Sigillare: la via della nonna. Legarlo, non ucciderlo. Sicuro. Collaudato. Ma dura solo trent'anni. Poi qualcun altro dovrà vivere questa notte.")
    _t(tr, F, "narration_approach_understand",
       en="Understand: What does it want? Why is it here? For six hundred years we sacrifice to it without ever asking. Perhaps the answer is the solution.",
       fr="Comprendre : que veut-il ? Pourquoi est-il ici ? Depuis six cents ans nous lui faisons des sacrifices sans jamais le questionner. Peut-être que là réponse est là solution.",
       es="Comprender: ¿Qué quiere? ¿Por qué está aquí? Seiscientos años sacrificándole sin preguntar jamás. Quizás la respuesta sea la solución.",
       it="Comprendere: cosa vuole? Perché è qui? Seicento anni a sacrificargli senza mai chiedere. Forse la risposta è la soluzione.")
    _t(tr, F, "narration_approach_destroy",
       en="Destroy: Final. Forever. No seal that needs renewing. No more sacrifice. But the price... Grandmother wrote that destruction costs the destroyer.",
       fr="Détruire : définitif. Pour toujours. Pas de sceau à renouveler. Plus de sacrifice. Mais le prix... Grand-mère à écrit que là destruction coûte au destructeur.",
       es="Destruir: definitivo. Para siempre. Sin sello que renovar. No más sacrificios. Pero el precio... La abuela escribió que la destrucción cuesta al destructor.",
       it="Distruggere: definitivo. Per sempre. Nessun sigillo da rinnovare. Nessun altro sacrificio. Ma il prezzo... La nonna ha scritto che la distruzione costa al distruttore.")
    _t(tr, F, "narration_approach_pact",
       en="Negotiate: A pact. Give and take. Less than sacrifice, more than ignorance. But: can you trust an entity that has accepted six hundred years of human sacrifice?",
       fr="Négocier : un pacte. Donner et prendre. Moins qu'un sacrifice, plus que l'ignorance. Mais : peut-on faire confiance à une entité qui à accepté six cents ans de sacrifices humains ?",
       es="Negociar: un pacto. Dar y recibir. Menos que un sacrificio, más que la ignorancia. Pero: ¿se puede confiar en una entidad que ha aceptado seiscientos años de sacrificios humanos?",
       it="Negoziare: un patto. Dare è ricevere. Meno di un sacrificio, più dell'ignoranza. Ma: ci si può fidare di un'entità che ha accettato seicento anni di sacrifici umani?")
    _t(tr, F, "approach_seal_2",
       en="Grandmother showed the way. I just need to follow her footsteps. The chant, the earth sign, the anchor. Three components, one ritual. I can do this.",
       fr="Grand-mère à montré le chemin. Je n'ai qu'à suivre ses traces. Le chant, le signe de terre, l'ancre. Trois composantes, un rituel. J'en suis capable.",
       es="La abuela mostró el camino. Solo debo seguir sus pasos. El canto, el signo de la tierra, el ancla. Tres componentes, un ritual. Puedo hacerlo.",
       it="La nonna ha mostrato la via. Devo solo seguire le sue orme. Il canto, il segno della terra, l'ancora. Tre componenti, un rituale. Ce la posso fare.")
    _t(tr, F, "approach_understand_2",
       en="I am a folklorist. I study the unknown. If anyone is capable of communicating with something no human understands, it should be me.",
       fr="Je suis folkloriste. J'étudie l'inconnu. Si quelqu'un est capable de communiquer avec quelque chose qu'aucun humain ne comprend, çà devrait être moi.",
       es="Soy folclorista. Estudio lo desconocido. Si alguien es capaz de comunicarse con algo que ningún humano entiende, debería ser yo.",
       it="Sono una folclorista. Studio l'ignoto. Se qualcuno è capace di comunicare con qualcosa che nessun umano comprende, dovrei essere io.")
    _t(tr, F, "approach_destroy_2",
       en="Grandmother wrote that destruction costs the destroyer. I am willing to pay that price. Six hundred years of blood are enough.",
       fr="Grand-mère à écrit que là destruction coûte au destructeur. Je suis prête à payer ce prix. Six cents ans de sang, c'est assez.",
       es="La abuela escribió que la destrucción cuesta al destructor. Estoy dispuesta a pagar ese precio. Seiscientos años de sangre son suficientes.",
       it="La nonna ha scritto che la distruzione costa al distruttore. Sono pronta a pagare quel prezzo. Seicento anni di sangue sono abbastanza.")
    _t(tr, F, "approach_pact_2",
       en="My name is in the book. That gives me a connection, a voice. For the first time in six hundred years, someone will TALK to the entity, not sacrifice to it.",
       fr="Mon nom est dans le livre. Celà me donne un lien, une voix. Pour là première fois en six cents ans, quelqu'un và PARLER à l'entité, pas lui faire un sacrifice.",
       es="Mi nombre está en el libro. Eso me da una conexión, una voz. Por primera vez en seiscientos años, alguien va a HABLAR con la entidad, no sacrificarle.",
       it="Il mio nome è nel libro. Questo mi dà un legame, una voce. Per la prima volta in seicento anni, qualcuno PARLERÀ con l'entità, non le sacrificherà.")
    # --- Final preparation ---
    _t(tr, F, "narration_preparation_2",
       en="And the letter. Grandmother's letter. Not because it is a tool. But because I want to have it with me when the time comes.",
       fr="Et là lettre. Là lettre de grand-mère. Non parce que c'est un outil. Mais parce que je veux l'avoir sur moi quand le moment viendra.",
       es="Y la carta. La carta de la abuela. No porque sea una herramienta. Sino porque quiero tenerla conmigo cuando llegue el momento.",
       it="E la lettera. La lettera della nonna. Non perché sia uno strumento. Ma perché voglio averla con me quando sarà il momento.")
    _t(tr, F, "narration_write_letter",
       en="I pick up a pen. In case I do not return, someone should know what happened here. What I tried.",
       fr="Je prends un stylo. Au cas où je ne reviendrais pas, quelqu'un devrait savoir ce qui s'est passé ici. Ce que j'ai tenté.",
       es="Tomo un bolígrafo. Si no vuelvo, alguien debería saber lo que ocurrió aquí. Lo que intenté.",
       it="Prendo una penna. Nel caso non tornassi, qualcuno dovrebbe sapere cosa è successo qui. Cosa ho tentato.")
    _t(tr, F, "narration_write_letter_2",
       en="'Whoever reads this: beneath the church of Graubach sleeps something old. It is not evil. It is hungry. And the people living above it have chosen the wrong way to feed it for six hundred years.'",
       fr="« Qui que vous soyez qui lisez ceci : sous l'église de Graubach dort quelque chose d'ancien. Ce n'est pas maléfique. C'est affamé. Et les gens qui vivent au-dessus ont choisi là mauvaise façon de le nourrir pendant six cents ans. »",
       es="'Quien lea esto: bajo la iglesia de Graubach duerme algo antiguo. No es malvado. Tiene hambre. Y la gente que vive sobre él ha elegido la forma equivocada de alimentarlo durante seiscientos años.'",
       it="'Chiunque legga questo: sotto la chiesa di Graubach dorme qualcosa di antico. Non è malvagio. Ha fame. È le persone che vivono sopra di esso hanno scelto il modo sbagliato di nutrirlo per seicento anni.'")
    _t(tr, F, "narration_write_letter_3",
       en="'My name is Elise Brandt, and tonight I am trying to find a better way. If I fail, please — do not come to Graubach. Not in thirty years. Not in a hundred. Leave it in peace.'",
       fr="« Je m'appelle Elise Brandt, et cette nuit j'essaie de trouver un meilleur chemin. Si j'échoue, je vous en prie — ne venez pas à Graubach. Ni dans trente ans. Ni dans cent. Laissez-le en paix. »",
       es="'Me llamo Elise Brandt, y esta noche intento encontrar un camino mejor. Si fracaso, por favor — no vengan a Graubach. Ni en treinta años. Ni en cien. Déjenlo en paz.'",
       it="'Mi chiamo Elise Brandt, è stanotte provo a trovare una via migliore. Se fallisco, per favore — non venite a Graubach. Non fra trent'anni. Non fra cento. Lasciatelo in pace.'")
    _t(tr, F, "narration_write_letter_end",
       en="I put the pen down. There is nothing more to write. Nothing more to do. Only wait.",
       fr="Je pose le stylo. Il n'y à plus rien à écrire. Plus rien à faire. Seulement attendre.",
       es="Dejo el bolígrafo. No hay nada más que escribir. Nada más que hacer. Solo esperar.",
       it="Poso la penna. Non c'è più nulla da scrivere. Nulla da fare. Solo aspettare.")
    # --- Dawn ---
    _t(tr, F, "narration_dawn_3",
       en="I stand up. Stretch my back. Breathe in, breathe out. The last ordinary act of my old life.",
       fr="Je me lève. J'étire mon dos. Inspire, expire. Le dernier geste ordinaire de mon ancienne vie.",
       es="Me levanto. Estiro la espalda. Inhalo, exhalo. El último acto ordinario de mi vieja vida.",
       it="Mi alzo. Stiro la schiena. Inspiro, espiro. L'ultimo gesto ordinario della mia vecchia vita.")
    _t(tr, F, "narration_dawn_4",
       en="Today the story of Graubach ends. Six hundred years of tradition, six hundred years of fear, six hundred years of blood. Today I decide how.",
       fr="Aujourd'hui, l'histoire de Graubach prend fin. Six cents ans de tradition, six cents ans de peur, six cents ans de sang. Aujourd'hui, je décide comment.",
       es="Hoy termina la historia de Graubach. Seiscientos años de tradición, seiscientos años de miedo, seiscientos años de sangre. Hoy decido cómo.",
       it="Oggi la storia di Graubach finisce. Seicento anni di tradizione, seicento anni di paura, seicento anni di sangue. Oggi decido come.")
    _t(tr, F, "narration_dawn_5",
       en="I take Grandmother's key, pocket the letter, extinguish the candle. It does not go out. Of course not.",
       fr="Je prends là clé de grand-mère, glisse là lettre dans mà poche, éteins là bougie. Elle ne s'éteint pas. Bien sûr que non.",
       es="Tomo la llave de la abuela, guardo la carta, apago la vela. No se apaga. Por supuesto que no.",
       it="Prendo la chiave della nonna, infilo la lettera in tasca, spengo la candela. Non si spegne. Certo che no.")
    _t(tr, F, "narration_dawn_final",
       en="I leave it burning. Perhaps it will light my way back. If there is a way back.",
       fr="Je là laisse brûler. Peut-être qu'elle m'éclairerà le chemin du retour. S'il y à un chemin du retour.",
       es="La dejo arder. Quizás me ilumine el camino de vuelta. Si hay un camino de vuelta.",
       it="La lascio ardere. Forse mi illuminerà la via del ritorno. Se c'è una via del ritorno.")


def _add_act4_ritual_night(tr):
    F = "res://data/dialogue/act4/ritual_night.json"

    # --- Opening narration ---
    _t(tr, F, "narration_1",
       en="Day eight. Sunset. The chamber beneath the church pulses like a heart. The spirals on the walls are turning. The singing fills everything.",
       fr="Huitième jour. Coucher de soleil. Là chambre sous l'église pulse comme un cœur. Les spirales sur les murs tournent. Le chant emplit tout.",
       es="Día ocho. Atardecer. La cámara bajo la iglesia pulsa como un corazón. Las espirales en las paredes giran. El canto lo llena todo.",
       it="Giorno otto. Tramonto. La camera sotto la chiesa pulsa come un cuore. Le spirali sulle pareti girano. Il canto riempie tutto.")

    _t(tr, F, "narration_2",
       en="I stand on the earth sign, the point where the stone is thinnest. Beneath my feet I feel it: vast, ancient, awakening.",
       fr="Je me tiens sur le signe de terre, le point où là pierre est là plus mince. Sous mes pieds, je le sens : immense, ancien, en train de s'éveiller.",
       es="Estoy de pie sobre el signo de la tierra, el punto donde la piedra es más delgada. Bajo mis pies lo siento: inmenso, antiguo, despertando.",
       it="Sono in piedi sul segno della terra, il punto dove la pietra è più sottile. Sotto i miei piedi lo sento: immenso, antico, in risveglio.")

    _t(tr, F, "narration_3",
       en="Georg's key opened the last door. Hilde's herbs burn in a bowl beside me, their smoke rising in spirals. Grandmother's journal lies open.",
       fr="Là clé de Georg à ouvert là dernière porte. Les herbes de Hilde brûlent dans un bol à côté de moi, leur fumée s'élève en spirales. Le journal de grand-mère est ouvert.",
       es="La llave de Georg abrió la última puerta. Las hierbas de Hilde arden en un cuenco junto a mí, su humo asciende en espirales. El diario de la abuela está abierto.",
       it="La chiave di Georg ha aperto l'ultima porta. Le erbe di Hilde bruciano in una ciotola accanto a me, il loro fumo sale a spirale. Il diario della nonna è aperto.")

    _t(tr, F, "narration_4",
       en="Grandmother's letter in my breast pocket. Hilde's amulet around my neck. Everything that connects me to the living.",
       fr="Là lettre de grand-mère dans mà poche de poitrine. L'amulette de Hilde autour de mon cou. Tout ce qui me relie aux vivants.",
       es="La carta de la abuela en mi bolsillo del pecho. El amuleto de Hilde alrededor de mi cuello. Todo lo que me conecta con los vivos.",
       it="La lettera della nonna nella tasca del petto. L'amuleto di Hilde al collo. Tutto ciò che mi lega ai vivi.")

    _t(tr, F, "narration_5",
       en="Now there is no turning back. The entity knows I am here. It is waiting.",
       fr="Maintenant, il n'y à plus de retour possible. L'entité sait que je suis là. Elle attend.",
       es="Ahora no hay vuelta atrás. La entidad sabe que estoy aquí. Está esperando.",
       it="Ora non si torna indietro. L'entità sa che sono qui. Sta aspettando.")

    # --- Georg ally branch ---
    _t(tr, F, "georg_ritual_1",
       en="I am here, Elise. As promised.",
       fr="Je suis là, Elise. Comme promis.",
       es="Estoy aquí, Elise. Como prometí.",
       it="Sono qui, Elise. Come promesso.")

    _t(tr, F, "elise_georg_ritual",
       en="Whatever happens, Georg — thank you. For everything. For Grandmother. For me.",
       fr="Quoi qu'il arrive, Georg — merci. Pour tout. Pour grand-mère. Pour moi.",
       es="Pase lo que pase, Georg — gracias. Por todo. Por la abuela. Por mí.",
       it="Qualunque cosa accada, Georg — grazie. Per tutto. Per la nonna. Per me.")

    _t(tr, F, "georg_ritual_2",
       en="Thank me afterwards. When we walk out of here. Together.",
       fr="Remercie-moi après. Quand on sortirà d'ici. Ensemble.",
       es="Agradécemelo después. Cuando salgamos de aquí. Juntos.",
       it="Ringraziami dopo. Quando usciremo di qui. Insieme.")

    # --- Hilde ally branch ---
    _t(tr, F, "hilde_ritual_entry_1",
       en="The herbs are burning properly. Good. The smoke will open the way.",
       fr="Les herbes brûlent correctement. Bien. Là fumée ouvrirà le chemin.",
       es="Las hierbas arden correctamente. Bien. El humo abrirá el camino.",
       it="Le erbe bruciano come si deve. Bene. Il fumo aprirà la via.")

    _t(tr, F, "elise_hilde_ritual",
       en="Hilde... if I don't come back...",
       fr="Hilde... si je ne reviens pas...",
       es="Hilde... si no vuelvo...",
       it="Hilde... se non torno...")

    _t(tr, F, "hilde_ritual_entry_2",
       en="You will come back. Your grandmother promised me that, and Margarethe never lied.",
       fr="Tu reviendras. Tà grand-mère me l'à promis, et Margarethe n'à jamais menti.",
       es="Volverás. Tu abuela me lo prometió, y Margarethe nunca mintió.",
       it="Tornerai. Tua nonna me lo ha promesso, è Margarethe non ha mai mentito.")

    # --- Voss ally branch ---
    _t(tr, F, "voss_ritual_1",
       en="Heavenly Father, stand by this child in her darkest hour...",
       fr="Père céleste, soutiens cette enfant en son heure là plus sombre...",
       es="Padre celestial, asiste a esta criatura en su hora más oscura...",
       it="Padre celeste, assisti questa creatura nella sua ora più buia...")

    _t(tr, F, "elise_voss_ritual",
       en="Pastor. If your God has power down here — then now.",
       fr="Pasteur. Si votre Dieu à du pouvoir ici-bas — c'est maintenant.",
       es="Pastor. Si su Dios tiene poder aquí abajo — que sea ahora.",
       it="Pastore. Se il vostro Dio ha potere quaggiù — che sia adesso.")

    _t(tr, F, "voss_ritual_2",
       en="He has power everywhere. Even over things that are older than His name.",
       fr="Il à du pouvoir partout. Même sur les choses plus anciennes que Son nom.",
       es="Tiene poder en todas partes. Incluso sobre cosas más antiguas que Su nombre.",
       it="Ha potere ovunque. Anche sulle cose più antiche del Suo nome.")

    # --- Alone branch ---
    _t(tr, F, "narration_alone_ritual",
       en="I am alone. Just as Grandmother was for thirty years. Perhaps that is the right way. This meeting was always meant for just the two of us.",
       fr="Je suis seule. Comme grand-mère l'à été pendant trente ans. C'est peut-être le bon chemin. Cette rencontre n'à toujours été destinée qu'à nous deux.",
       es="Estoy sola. Igual que la abuela lo estuvo durante treinta años. Quizás ese sea el camino correcto. Este encuentro siempre estuvo destinado solo a nosotros dos.",
       it="Sono sola. Come lo è stata la nonna per trent'anni. Forse è la via giusta. Questo incontro è sempre stato destinato solo a noi due.")

    # --- Ally ready ---
    _t(tr, F, "narration_ally_ready",
       en="I breathe deeply. The smoke of the herbs fills my lungs. The amulet pulses warm against my chest. It is time.",
       fr="J'inspire profondément. Là fumée des herbes emplit mes poumons. L'amulette pulse chaudement contre mà poitrine. Le moment est venu.",
       es="Respiro hondo. El humo de las hierbas llena mis pulmones. El amuleto pulsa cálido contra mi pecho. Es el momento.",
       it="Respiro a fondo. Il fumo delle erbe riempie i miei polmoni. L'amuleto pulsa caldo contro il mio petto. È il momento.")

    # --- Begin ritual ---
    _t(tr, F, "narration_begin_ritual",
       en="I place my hands on the earth sign. The pulsing point at the center of the circle. And this time I do not pull them back.",
       fr="Je pose mes mains sur le signe de terre. Le point pulsant au centre du cercle. Et cette fois, je ne les retire pas.",
       es="Pongo mis manos sobre el signo de la tierra. El punto pulsante en el centro del círculo. Y esta vez no las retiro.",
       it="Poso le mani sul segno della terra. Il punto pulsante al centro del cerchio. È questa volta non le ritiro.")

    # --- Contact with the entity ---
    _t(tr, F, "narration_contact_1",
       en="The ocean. Again. But this time I am not just a fly on its surface. This time I dive in.",
       fr="L'océan. Encore. Mais cette fois, je ne suis pas qu'une mouche à sà surface. Cette fois, je plonge.",
       es="El océano. De nuevo. Pero esta vez no soy solo una mosca en su superficie. Esta vez me sumerjo.",
       it="L'oceano. Di nuovo. Ma questa volta non sono solo una mosca sulla sua superficie. Questa volta mi immergo.")

    _t(tr, F, "narration_contact_2",
       en="Cold. Then warmth. Then something beyond temperature. A consciousness that slowly turns around and LOOKS AT ME.",
       fr="Froid. Puis chaleur. Puis quelque chose au-delà de là température. Une conscience qui se retourne lentement et ME REGARDE.",
       es="Frío. Luego calor. Luego algo más allá de la temperatura. Una consciencia que se vuelve lentamente y ME MIRA.",
       it="Freddo. Poi calore. Poi qualcosa oltre la temperatura. Una coscienza che lentamente si volta è MI GUARDA.")

    # --- Creature speaks ---
    _t(tr, F, "narration_creature_1",
       en="Then it speaks. Not with words. Not with sounds. It speaks directly into my mind, and the words are older than any language I know.",
       fr="Puis il parle. Pas avec des mots. Pas avec des sons. Il parle directement dans mà tête, et les mots sont plus anciens que toute langue que je connais.",
       es="Entonces habla. No con palabras. No con sonidos. Habla directamente en mi mente, y las palabras son más antiguas que cualquier idioma que conozco.",
       it="Poi parla. Non con parole. Non con suoni. Parla direttamente nella mia mente, è le parole sono più antiche di qualsiasi lingua io conosca.")

    _t(tr, F, "narration_creature_speak_1",
       en="I KNOW YOU. YOUR NAME IS WRITTEN IN MY BOOK.",
       fr="JE TE CONNAIS. TON NOM EST INSCRIT DANS MON LIVRE.",
       es="TE CONOZCO. TU NOMBRE ESTÁ ESCRITO EN MI LIBRO.",
       it="TI CONOSCO. IL TUO NOME È SCRITTO NEL MIO LIBRO.")

    _t(tr, F, "narration_creature_speak_2",
       en="The voice is like thunder in a closed room. My teeth vibrate. My bones hum.",
       fr="Là voix est comme le tonnerre dans une pièce close. Mes dents vibrent. Mes os bourdonnent.",
       es="La voz es como un trueno en una habitación cerrada. Mis dientes vibran. Mis huesos zumban.",
       it="La voce è come un tuono in una stanza chiusa. I miei denti vibrano. Le mie ossa ronzano.")

    _t(tr, F, "elise_creature_1",
       en="I... I know. I know that you know me. I have come to—",
       fr="Je... je sais. Je sais que tu me connais. Je suis venue pour—",
       es="Yo... lo sé. Sé que me conoces. He venido para—",
       it="Io... lo so. So che mi conosci. Sono venuta per—")

    _t(tr, F, "narration_creature_speak_3",
       en="YOU ARE LIKE HER. THE OLD ONE. SHE SMELLED OF HERBS AND STUBBORNNESS. YOU SMELL THE SAME.",
       fr="TU ES COMME ELLE. LA VIEILLE. ELLE SENTAIT LES HERBES ET L'OBSTINATION. TU SENS PAREIL.",
       es="ERES COMO ELLA. LA VIEJA. OLÍA A HIERBAS Y A TERQUEDAD. TÚ HUELES IGUAL.",
       it="SEI COME LEI. LA VECCHIA. ODORAVA DI ERBE È DI OSTINAZIONE. TU HAI LO STESSO ODORE.")

    _t(tr, F, "narration_creature_react",
       en="It knows Grandmother. It remembers her. For thirty years she visited it, sang to it, bound it. And it remembers.",
       fr="Il connaît grand-mère. Il se souvient d'elle. Pendant trente ans, elle l'à visité, lui à chanté, l'à lié. Et il s'en souvient.",
       es="Conoce a la abuela. La recuerda. Durante treinta años ella lo visitó, le cantó, lo ató. Y lo recuerda.",
       it="Conosce la nonna. La ricorda. Per trent'anni lei lo ha visitato, gli ha cantato, lo ha legato. È se ne ricorda.")

    _t(tr, F, "elise_creature_2",
       en="Margarethe. My grandmother. She sent me.",
       fr="Margarethe. Mà grand-mère. C'est elle qui m'à envoyée.",
       es="Margarethe. Mi abuela. Ella me envió.",
       it="Margarethe. Mia nonna. Mi ha mandato lei.")

    _t(tr, F, "narration_creature_speak_4",
       en="SHE IS NO MORE. I FELT HER LIGHT GO OUT. IT WAS... QUIET AFTERWARDS.",
       fr="ELLE N'EST PLUS. J'AI SENTI SA LUMIÈRE S'ÉTEINDRE. C'ÉTAIT... SILENCIEUX APRÈS.",
       es="YA NO ESTÁ. SENTÍ SU LUZ APAGARSE. DESPUÉS FUE... SILENCIO.",
       it="NON C'È PIÙ. HO SENTITO LA SUA LUCE SPEGNERSI. DOPO È STATO... SILENZIO.")

    _t(tr, F, "narration_creature_lonely",
       en="In the voice there is something I did not expect. Not hunger. Not rage. Grief. This ancient, inhuman entity GRIEVES for my grandmother.",
       fr="Dans là voix, il y à quelque chose que je n'attendais pas. Pas là faim. Pas là rage. Le chagrin. Cette entité ancienne et inhumaine PLEURE mà grand-mère.",
       es="En la voz hay algo que no esperaba. No hambre. No ira. Duelo. Esta entidad antigua e inhumana LLORA a mi abuela.",
       it="Nella voce c'è qualcosa che non mi aspettavo. Non fame. Non rabbia. Lutto. Questa entità antica è disumana è IN LUTTO per mia nonna.")

    _t(tr, F, "elise_creature_3",
       en="You... grieve for her?",
       fr="Tu... tu là pleures ?",
       es="Tú... ¿la lloras?",
       it="Tu... sei in lutto per lei?")

    _t(tr, F, "narration_creature_speak_5",
       en="SHE WAS THE ONLY ONE WHO SANG. NOT OUT OF FEAR. OUT OF... I HAVE NO WORD FOR IT. YOU MIGHT SAY: COMPASSION.",
       fr="ELLE ÉTAIT LA SEULE À CHANTER. PAS PAR PEUR. PAR... JE N'AI PAS DE MOT POUR CELA. VOUS DIRIEZ PEUT-ÊTRE : COMPASSION.",
       es="ELLA ERA LA ÚNICA QUE CANTABA. NO POR MIEDO. POR... NO TENGO PALABRA PARA ESO. USTEDES QUIZÁS DIRÍAN: COMPASIÓN.",
       it="ERA L'UNICA CHE CANTAVA. NON PER PAURA. PER... NON HO UNA PAROLA PER QUESTO. VOI FORSE DIRESTE: COMPASSIONE.")

    _t(tr, F, "narration_creature_speak_6",
       en="I AM OLDER THAN YOUR GOD. I WAS HERE BEFORE THE TREES, BEFORE THE MOUNTAINS, BEFORE THE RIVER. AND I AM SO TIRED.",
       fr="JE SUIS PLUS ANCIEN QUE VOTRE DIEU. J'ÉTAIS LÀ AVANT LES ARBRES, AVANT LES MONTAGNES, AVANT LA RIVIÈRE. ET JE SUIS SI FATIGUÉ.",
       es="SOY MÁS ANTIGUO QUE VUESTRO DIOS. ESTUVE AQUÍ ANTES QUE LOS ÁRBOLES, ANTES QUE LAS MONTAÑAS, ANTES QUE EL RÍO. Y ESTOY TAN CANSADO.",
       it="SONO PIÙ ANTICO DEL VOSTRO DIO. ERO QUI PRIMA DEGLI ALBERI, PRIMA DELLE MONTAGNE, PRIMA DEL FIUME. È SONO COSÌ STANCO.")

    _t(tr, F, "narration_creature_hunger",
       en="HUNGER IS NOT A WORD. IT IS A VOID. FOR SIX HUNDRED YEARS YOU GAVE ME YOUR DEAD. THEY TASTE OF FEAR. I WANT NO MORE FEAR.",
       fr="LA FAIM N'EST PAS UN MOT. C'EST UN VIDE. PENDANT SIX CENTS ANS, VOUS M'AVEZ DONNÉ VOS MORTS. ILS ONT LE GOÛT DE LA PEUR. JE NE VEUX PLUS DE PEUR.",
       es="EL HAMBRE NO ES UNA PALABRA. ES UN VACÍO. DURANTE SEISCIENTOS AÑOS ME DISTEIS A VUESTROS MUERTOS. SABEN A MIEDO. NO QUIERO MÁS MIEDO.",
       it="LA FAME NON È UNA PAROLA. È UN VUOTO. PER SEICENTO ANNI MI AVETE DATO I VOSTRI MORTI. SANNO DI PAURA. NON VOGLIO PIÙ PAURA.")

    _t(tr, F, "narration_elise_realization",
       en="My hands tremble on the stone. But not from fear. From realization. It is not a monster. It is something old and lonely that never had any other choice than to take what was given to it.",
       fr="Mes mains tremblent sur là pierre. Mais pas de peur. De compréhension. Ce n'est pas un monstre. C'est quelque chose de vieux et de solitaire qui n'à jamais eu d'autre choix que de prendre ce qu'on lui donnait.",
       es="Mis manos tiemblan sobre la piedra. Pero no de miedo. De comprensión. No es un monstruo. Es algo viejo y solitario que nunca tuvo otra opción que tomar lo que le daban.",
       it="Le mie mani tremano sulla pietra. Ma non per la paura. Per la comprensione. Non è un mostro. È qualcosa di vecchio è di solo che non ha mai avuto altra scelta se non prendere ciò che gli veniva dato.")

    _t(tr, F, "elise_creature_4",
       en="What do you really want? Not sacrifices. Not blood. What do you WANT?",
       fr="Que veux-tu vraiment ? Pas des sacrifices. Pas du sang. Que VEUX-tu ?",
       es="¿Qué quieres realmente? No sacrificios. No sangre. ¿Qué QUIERES?",
       it="Cosa vuoi davvero? Non sacrifici. Non sangue. Cosa VUOI?")

    _t(tr, F, "narration_creature_speak_7",
       en="FOR SOMEONE TO STAY. NOT DIE. STAY. SIX HUNDRED YEARS AND NOBODY EVER ASKED.",
       fr="QUE QUELQU'UN RESTE. QU'IL NE MEURE PAS. QU'IL RESTE. SIX CENTS ANS ET PERSONNE N'A JAMAIS DEMANDÉ.",
       es="QUE ALGUIEN SE QUEDE. QUE NO MUERA. QUE SE QUEDE. SEISCIENTOS AÑOS Y NADIE PREGUNTÓ JAMÁS.",
       it="CHE QUALCUNO RESTI. CHE NON MUOIA. CHE RESTI. SEICENTO ANNI È NESSUNO HA MAI CHIESTO.")

    # --- Revelation ---
    _t(tr, F, "narration_revelation",
       en="Silence. In my mind, in the chamber, everywhere. The singing has stopped. For the first time since I arrived in Graubach, it is quiet.",
       fr="Le silence. Dans mà tête, dans là chambre, partout. Le chant s'est arrêté. Pour là première fois depuis mon arrivée à Graubach, c'est le silence.",
       es="Silencio. En mi mente, en la cámara, en todas partes. El canto se ha detenido. Por primera vez desde que llegué a Graubach, hay silencio.",
       it="Silenzio. Nella mia mente, nella camera, ovunque. Il canto si è fermato. Per la prima volta da quando sono arrivata a Graubach, c'è silenzio.")

    _t(tr, F, "narration_revelation_2",
       en="It is waiting for my answer. The oldest being in the world is waiting for the words of a folklorist from Berlin.",
       fr="Il attend mà réponse. L'être le plus ancien du monde attend les mots d'une folkloriste de Berlin.",
       es="Espera mi respuesta. El ser más antiguo del mundo espera las palabras de una folclorista de Berlín.",
       it="Aspetta la mia risposta. L'essere più antico del mondo aspetta le parole di una folklorista di Berlino.")

    # --- Konrad appears ---
    _t(tr, F, "konrad_appears",
       en="Footsteps on the stairs. Konrad. He stands in the entrance of the chamber, half in shadow. His eyes flicker between brown and something bottomless.",
       fr="Des pas dans l'escalier. Konrad. Il se tient à l'entrée de là chambre, à moitié dans l'ombre. Ses yeux oscillent entre le brun et quelque chose de sans fond.",
       es="Pasos en la escalera. Konrad. Está de pie en la entrada de la cámara, medio en sombras. Sus ojos oscilan entre el marrón y algo sin fondo.",
       it="Passi sulle scale. Konrad. È in piedi all'ingresso della camera, mezzo nell'ombra. I suoi occhi oscillano tra il marrone è qualcosa di senza fondo.")

    _t(tr, F, "konrad_1",
       en="Elise... it brought me here. It... IT SPEAKS THROUGH ME. But a part of me is still here. Still.",
       fr="Elise... çà m'à amené ici. Ça... ÇA PARLE À TRAVERS MOI. Mais une partie de moi est encore là. Encore.",
       es="Elise... me trajo aquí. Eso... ESO HABLA A TRAVÉS DE MÍ. Pero una parte de mí sigue aquí. Todavía.",
       it="Elise... mi ha portato qui. Quella cosa... PARLA ATTRAVERSO DI ME. Ma una parte di me è ancora qui. Ancora.")

    _t(tr, F, "elise_konrad_ritual_1",
       en="Konrad! Listen to my voice. YOU are Konrad Mueller. You are a teacher. Hold on!",
       fr="Konrad ! Écoute mà voix. TU es Konrad Müller. Tu es enseignant. Tiens bon !",
       es="¡Konrad! Escucha mi voz. TÚ eres Konrad Müller. Eres maestro. ¡Resiste!",
       it="Konrad! Ascolta la mia voce. TU sei Konrad Müller. Sei un insegnante. Resisti!")

    _t(tr, F, "konrad_3",
       en="It is so tired, Elise. I feel it. Six hundred years of loneliness... no human could endure that. And it is not human.",
       fr="Il est si fatigué, Elise. Je le sens. Six cents ans de solitude... aucun humain ne pourrait endurer cela. Et ce n'est pas un humain.",
       es="Está tan cansado, Elise. Lo siento. Seiscientos años de soledad... ningún humano podría soportar eso. Y no es humano.",
       it="È così stanco, Elise. Lo sento. Seicento anni di solitudine... nessun essere umano potrebbe sopportarlo. È non è umano.")

    _t(tr, F, "elise_konrad_ritual_2",
       en="I know. I heard it. It does not want to feed. It does not want to kill. It just wants someone to stay.",
       fr="Je sais. Je l'ai entendu. Il ne veut pas se nourrir. Il ne veut pas tuer. Il veut juste que quelqu'un reste.",
       es="Lo sé. Lo escuché. No quiere alimentarse. No quiere matar. Solo quiere que alguien se quede.",
       it="Lo so. L'ho sentito. Non vuole nutrirsi. Non vuole uccidere. Vuole solo che qualcuno resti.")

    _t(tr, F, "konrad_4",
       en="For thirty years I HAVE stayed. Not willingly. But I understand it now. The loneliness. The endless, bottomless loneliness.",
       fr="Pendant trente ans, je SUIS resté. Pas de mon plein gré. Mais je comprends maintenant. Là solitude. L'infinie, l'insondable solitude.",
       es="Durante treinta años HE permanecido. No voluntariamente. Pero ahora lo entiendo. La soledad. La interminable e insondable soledad.",
       it="Per trent'anni SONO rimasto. Non per scelta. Ma ora capisco. La solitudine. L'infinita, insondabile solitudine.")

    _t(tr, F, "narration_konrad_choice",
       en="Konrad's eyes flicker. Brown. Bottomless. Brown. He is fighting against himself. Against the entity. Against thirty years of captivity.",
       fr="Les yeux de Konrad oscillent. Bruns. Sans fond. Bruns. Il se bat contre lui-même. Contre l'entité. Contre trente ans de captivité.",
       es="Los ojos de Konrad oscilan. Marrones. Sin fondo. Marrones. Lucha contra sí mismo. Contra la entidad. Contra treinta años de cautiverio.",
       it="Gli occhi di Konrad oscillano. Marroni. Senza fondo. Marroni. Sta lottando contro se stesso. Contro l'entità. Contro trent'anni di prigionia.")

    # --- Sacrifice choice ---
    _tc(tr, F, "choice_sacrifice_override",
        en_choices=["Take Konrad's place — free him, whatever the cost", "Stick to the original plan"],
        fr_choices=["Prendre la place de Konrad — le libérer, quoi qu'il en coûte", "S'en tenir au plan initial"],
        es_choices=["Ocupar el lugar de Konrad — liberarlo, cueste lo que cueste", "Seguir con el plan original"],
        it_choices=["Prendere il posto di Konrad — liberarlo, costi quel che costi", "Attenersi al piano originale"])

    # --- Sacrifice branch ---
    _t(tr, F, "sacrifice_decision",
       en="Konrad. I am taking your place.",
       fr="Konrad. Je prends tà place.",
       es="Konrad. Ocupo tu lugar.",
       it="Konrad. Prendo il tuo posto.")

    _t(tr, F, "konrad_sacrifice_react",
       en="No... no, Elise, you can't—",
       fr="Non... non, Elise, tu ne peux pas—",
       es="No... no, Elise, no puedes—",
       it="No... no, Elise, non puoi—")

    _t(tr, F, "elise_sacrifice_2",
       en="Nobody should be alone. Not even something older than the mountains. And you have suffered for thirty years. That is enough.",
       fr="Personne ne devrait être seul. Pas même quelque chose de plus ancien que les montagnes. Et tu as souffert pendant trente ans. Çà suffit.",
       es="Nadie debería estar solo. Ni siquiera algo más antiguo que las montañas. Y has sufrido durante treinta años. Es suficiente.",
       it="Nessuno dovrebbe essere solo. Nemmeno qualcosa di più antico delle montagne. È tu hai sofferto per trent'anni. Basta così.")

    _t(tr, F, "narration_sacrifice_creature",
       en="YOU ARE LIKE HER. THE OLD ONE. SHE WOULD HAVE DONE THE SAME.",
       fr="TU ES COMME ELLE. LA VIEILLE. ELLE AURAIT FAIT PAREIL.",
       es="ERES COMO ELLA. LA VIEJA. ELLA HABRÍA HECHO LO MISMO.",
       it="SEI COME LEI. LA VECCHIA. AVREBBE FATTO LO STESSO.")

    # --- Plan branch ---
    _t(tr, F, "plan_decision",
       en="Konrad... I'm sorry. But I have a plan. Trust me.",
       fr="Konrad... je suis désolée. Mais j'ai un plan. Fais-moi confiance.",
       es="Konrad... lo siento. Pero tengo un plan. Confía en mí.",
       it="Konrad... mi dispiace. Ma ho un piano. Fidati di me.")

    _t(tr, F, "konrad_plan_react",
       en="Then do it. Quickly. Before HE takes over again.",
       fr="Alors fais-le. Vite. Avant qu'IL ne reprenne le dessus.",
       es="Entonces hazlo. Rápido. Antes de que ÉL recupere el control.",
       it="Allora fallo. In fretta. Prima che LUI riprenda il sopravvento.")

    # --- Seal ritual branch ---
    _t(tr, F, "seal_ritual_begin",
       en="The seal. Grandmother's way. I open the journal, find the page with the chant. The words are old, in no language I know, but somehow I understand them.",
       fr="Le sceau. Là voie de grand-mère. J'ouvre le journal, trouve là page avec le chant. Les mots sont anciens, dans aucune langue que je connais, mais d'une certaine manière je les comprends.",
       es="El sello. El camino de la abuela. Abro el diario, encuentro la página con el canto. Las palabras son antiguas, en ningún idioma que conozca, pero de algún modo las entiendo.",
       it="Il sigillo. La via della nonna. Apro il diario, trovo la pagina con il canto. Le parole sono antiche, in nessuna lingua che conosca, ma in qualche modo le capisco.")

    _t(tr, F, "elise_seal_begin",
       en="Grandmother, if you can hear me — help me. Show me the way.",
       fr="Grand-mère, si tu m'entends — aide-moi. Montre-moi le chemin.",
       es="Abuela, si puedes oírme — ayúdame. Muéstrame el camino.",
       it="Nonna, se puoi sentirmi — aiutami. Mostrami la via.")

    _t(tr, F, "narration_seal_creature",
       en="YOU WANT TO BIND ME? LIKE HER? ANOTHER THIRTY YEARS OF DARKNESS?",
       fr="TU VEUX ME LIER ? COMME ELLE ? ENCORE TRENTE ANS D'OBSCURITÉ ?",
       es="¿QUIERES ATARME? ¿COMO ELLA? ¿OTROS TREINTA AÑOS DE OSCURIDAD?",
       it="VUOI LEGARMI? COME LEI? ALTRI TRENT'ANNI DI OSCURITÀ?")

    _t(tr, F, "narration_seal_resist",
       en="Rage. Real rage. The chamber shakes, the spirals spin faster. The entity does not want to go back to sleep.",
       fr="Là rage. Une vraie rage. Là chambre tremble, les spirales tournent plus vite. L'entité ne veut pas se rendormir.",
       es="Ira. Ira real. La cámara tiembla, las espirales giran más rápido. La entidad no quiere volver a dormirse.",
       it="Rabbia. Rabbia vera. La camera trema, le spirali girano più veloci. L'entità non vuole tornare a dormire.")

    _t(tr, F, "elise_seal_2",
       en="Not forever! Only until... until we find a better way. Please!",
       fr="Pas pour toujours ! Seulement jusqu'à... jusqu'à ce qu'on trouve un meilleur moyen. S'il te plaît !",
       es="¡No para siempre! Solo hasta... hasta que encontremos un camino mejor. ¡Por favor!",
       it="Non per sempre! Solo finché... finché non troviamo una via migliore. Per favore!")

    _t(tr, F, "seal_chant_begin",
       en="I begin to sing. The words Hilde taught me flow from my mouth like water from a spring. Old. Clear. Powerful.",
       fr="Je commence à chanter. Les mots que Hilde m'à enseignés coulent de mà bouche comme l'eau d'une source. Anciens. Clairs. Puissants.",
       es="Comienzo a cantar. Las palabras que Hilde me enseñó fluyen de mi boca como agua de un manantial. Antiguas. Claras. Poderosas.",
       it="Comincio a cantare. Le parole che Hilde mi ha insegnato fluiscono dalla mia bocca come acqua da una sorgente. Antiche. Chiare. Potenti.")

    # --- Hilde saves seal branch ---
    _t(tr, F, "hilde_saves_seal",
       en="I begin the ritual, but the words are missing. The chant — I don't know it completely. Panic rises.",
       fr="Je commence le rituel, mais les mots manquent. Le chant — je ne le connais pas en entier. Là panique monte.",
       es="Comienzo el ritual, pero faltan las palabras. El canto... no lo conozco por completo. El pánico se apodera de mí.",
       it="Comincio il rituale, ma le parole mancano. Il canto — non lo conosco per intero. Il panico sale.")

    _t(tr, F, "hilde_ritual_1",
       en="Child, I am here. I will sing with you. My voice is old, but together — together it will be enough.",
       fr="Mon enfant, je suis là. Je chanterai avec toi. Mà voix est vieille, mais ensemble — ensemble, celà suffira.",
       es="Niña, estoy aquí. Cantaré contigo. Mi voz es vieja, pero juntas... juntas será suficiente.",
       it="Bambina, sono qui. Canterò con te. La mia voce è vecchia, ma insieme — insieme basterà.")

    _t(tr, F, "elise_hilde_sing",
       en="Together. As Grandmother would have wanted.",
       fr="Ensemble. Comme grand-mère l'aurait voulu.",
       es="Juntas. Como la abuela habría querido.",
       it="Insieme. Come la nonna avrebbe voluto.")

    _t(tr, F, "hilde_ritual_2",
       en="Hilde's voice rises beside mine, brittle but sure. She knows every word, every turn. The melody grows stronger, fills the chamber.",
       fr="Là voix de Hilde s'élève à côté de là mienne, fragile mais assurée. Elle connaît chaque mot, chaque tournure. Là mélodie se renforce, emplit là chambre.",
       es="La voz de Hilde se eleva junto a la mía, quebradiza pero segura. Conoce cada palabra, cada giro. La melodía se fortalece, llena la cámara.",
       it="La voce di Hilde si leva accanto alla mia, fragile ma sicura. Conosce ogni parola, ogni svolta. La melodia si fa più forte, riempie la camera.")

    # --- Seal fails branch ---
    _t(tr, F, "seal_fails",
       en="I begin the ritual, but the words are missing. The chant — I don't know it completely. The air vibrates, the entity reacts, but the seal will not close.",
       fr="Je commence le rituel, mais les mots manquent. Le chant — je ne le connais pas en entier. L'air vibre, l'entité réagit, mais le sceau ne se ferme pas.",
       es="Comienzo el ritual, pero faltan las palabras. El canto... no lo conozco por completo. El aire vibra, la entidad reacciona, pero el sello no se cierra.",
       it="Comincio il rituale, ma le parole mancano. Il canto — non lo conosco per intero. L'aria vibra, l'entità reagisce, ma il sigillo non si chiude.")

    _t(tr, F, "elise_seal_fail",
       en="No... no, I need more time, I—",
       fr="Non... non, j'ai besoin de plus de temps, je—",
       es="No... no, necesito más tiempo, yo—",
       it="No... no, ho bisogno di più tempo, io—")

    _t(tr, F, "narration_seal_fail_creature",
       en="YOUR WORDS ARE EMPTY. YOU DO NOT KNOW THE CHANT. HOW CAN YOU BIND WHAT YOU DO NOT UNDERSTAND?",
       fr="TES MOTS SONT VIDES. TU NE CONNAIS PAS LE CHANT. COMMENT PEUX-TU LIER CE QUE TU NE COMPRENDS PAS ?",
       es="TUS PALABRAS ESTÁN VACÍAS. NO CONOCES EL CANTO. ¿CÓMO PUEDES ATAR LO QUE NO COMPRENDES?",
       it="LE TUE PAROLE SONO VUOTE. NON CONOSCI IL CANTO. COME PUOI LEGARE CIÒ CHE NON COMPRENDI?")

    # --- Voss escape branch ---
    _t(tr, F, "voss_escape_narration",
       en="The ritual fails. The chamber shakes. But Voss is there — he knows every stone, every tunnel.",
       fr="Le rituel échoue. Là chambre tremble. Mais Voss est là — il connaît chaque pierre, chaque tunnel.",
       es="El ritual fracasa. La cámara tiembla. Pero Voss está ahí — conoce cada piedra, cada túnel.",
       it="Il rituale fallisce. La camera trema. Ma Voss è lì — conosce ogni pietra, ogni tunnel.")

    _t(tr, F, "voss_escape_2",
       en="This way! There is a second exit that only the pastors know!",
       fr="Par ici ! Il y à une seconde sortie que seuls les pasteurs connaissent !",
       es="¡Por aquí! ¡Hay una segunda salida que solo los pastores conocen!",
       it="Da questa parte! C'è una seconda uscita che solo i pastori conoscono!")

    _t(tr, F, "elise_escape_voss",
       en="Run! Quickly!",
       fr="Courez ! Vite !",
       es="¡Correr! ¡Rápido!",
       it="Corriamo! Presto!")

    # --- Courage escape branch ---
    _t(tr, F, "courage_escape",
       en="The ritual fails. The chamber breaks apart. But something in me refuses to give up. The same stubbornness that brought me here.",
       fr="Le rituel échoue. Là chambre se disloque. Mais quelque chose en moi refuse d'abandonner. Là même obstination qui m'à amenée ici.",
       es="El ritual fracasa. La cámara se desmorona. Pero algo en mí se niega a rendirse. La misma terquedad que me trajo aquí.",
       it="Il rituale fallisce. La camera si sgretola. Ma qualcosa in me rifiuta di arrendersi. La stessa ostinazione che mi ha portata qui.")

    _t(tr, F, "narration_courage_escape_2",
       en="I run. Through rubble, through darkness, through the roaring of the entity. My legs carry me even though they should have given out long ago.",
       fr="Je cours. À travers les décombres, à travers l'obscurité, à travers le rugissement de l'entité. Mes jambes me portent alors qu'elles auraient dû lâcher depuis longtemps.",
       es="Corro. Entre escombros, entre oscuridad, entre el rugido de la entidad. Mis piernas me llevan aunque hace tiempo que deberían haber fallado.",
       it="Corro. Tra le macerie, attraverso l'oscurità, attraverso il ruggito dell'entità. Le mie gambe mi portano anche se avrebbero dovuto cedere da tempo.")

    # --- Understand branch ---
    _t(tr, F, "understand_begin",
       en="Understanding. Not fighting, not binding. Understanding. I am a folklorist. I study the unknown. It is time to put that into practice.",
       fr="Comprendre. Pas combattre, pas lier. Comprendre. Je suis folkloriste. J'étudie l'inconnu. Il est temps de mettre celà en pratique.",
       es="Comprender. No luchar, no atar. Comprender. Soy folclorista. Estudio lo desconocido. Es hora de ponerlo en práctica.",
       it="Comprendere. Non combattere, non legare. Comprendere. Sono una folklorista. Studio l'ignoto. È ora di metterlo in pratica.")

    _t(tr, F, "elise_understand_1",
       en="I want to understand you. Not bind you, not destroy you. Show me what you are. Show me everything.",
       fr="Je veux te comprendre. Pas te lier, pas te détruire. Montre-moi ce que tu es. Montre-moi tout.",
       es="Quiero comprenderte. No atarte, no destruirte. Muéstrame lo que eres. Muéstrame todo.",
       it="Voglio capirti. Non legarti, non distruggerti. Mostrami cosa sei. Mostrami tutto.")

    _t(tr, F, "narration_understand_creature",
       en="UNDERSTAND? SIX HUNDRED YEARS AND NOBODY WANTED THAT. ARE YOU READY FOR WHAT YOU WILL SEE?",
       fr="COMPRENDRE ? SIX CENTS ANS ET PERSONNE NE L'A VOULU. ES-TU PRÊTE POUR CE QUE TU VERRAS ?",
       es="¿COMPRENDER? SEISCIENTOS AÑOS Y NADIE QUISO ESO. ¿ESTÁS PREPARADA PARA LO QUE VERÁS?",
       it="COMPRENDERE? SEICENTO ANNI È NESSUNO LO HA VOLUTO. SEI PRONTA PER QUELLO CHE VEDRAI?")

    _t(tr, F, "elise_understand_2",
       en="No. But I am asking anyway.",
       fr="Non. Mais je pose là question quand même.",
       es="No. Pero pregunto de todos modos.",
       it="No. Ma chiedo lo stesso.")

    _t(tr, F, "understand_ready",
       en="Grandmother's journal has prepared me. The symbols, the history, the connection. I understand enough to ask the right questions.",
       fr="Le journal de grand-mère m'à préparée. Les symboles, l'histoire, là connexion. J'en comprends assez pour poser les bonnes questions.",
       es="El diario de la abuela me ha preparado. Los símbolos, la historia, la conexión. Entiendo lo suficiente para hacer las preguntas correctas.",
       it="Il diario della nonna mi ha preparata. I simboli, la storia, la connessione. Capisco abbastanza per fare le domande giuste.")

    _t(tr, F, "understand_unprepared",
       en="But I lack the knowledge. Grandmother's journal — I should have read it more thoroughly. Without preparation, the gaze into this abyss...",
       fr="Mais le savoir me manque. Le journal de grand-mère — j'aurais dû le lire plus attentivement. Sans préparation, le regard dans cet abîme...",
       es="Pero me falta el conocimiento. El diario de la abuela — debería haberlo leído con más detalle. Sin preparación, la mirada a este abismo...",
       it="Ma mi manca la conoscenza. Il diario della nonna — avrei dovuto leggerlo con più attenzione. Senza preparazione, lo sguardo in questo abisso...")

    _t(tr, F, "narration_understand_fail",
       en="YOU WANT TO SEE, BUT YOUR EYES ARE STILL CLOSED. PERHAPS I WILL OPEN THEM FOR YOU.",
       fr="TU VEUX VOIR, MAIS TES YEUX SONT ENCORE FERMÉS. PEUT-ÊTRE QUE JE LES OUVRIRAI POUR TOI.",
       es="QUIERES VER, PERO TUS OJOS SIGUEN CERRADOS. QUIZÁS LOS ABRA POR TI.",
       it="VUOI VEDERE, MA I TUOI OCCHI SONO ANCORA CHIUSI. FORSE LI APRIRÒ PER TE.")

    # --- Pact branch ---
    _t(tr, F, "pact_begin",
       en="A pact. Negotiate. My name in the book gives me a voice. For the first time in six hundred years, someone will speak with the entity.",
       fr="Un pacte. Négocier. Mon nom dans le livre me donne une voix. Pour là première fois en six cents ans, quelqu'un và parler avec l'entité.",
       es="Un pacto. Negociar. Mi nombre en el libro me da voz. Por primera vez en seiscientos años, alguien hablará con la entidad.",
       it="Un patto. Negoziare. Il mio nome nel libro mi dà voce. Per la prima volta in seicento anni, qualcuno parlerà con l'entità.")

    _t(tr, F, "elise_pact_1",
       en="I propose a deal. No more sacrifices. Never again. In return... in return I offer you something you never had in six hundred years.",
       fr="Je propose un marché. Plus de sacrifices. Plus jamais. En échange... en échange, je t'offre quelque chose que tu n'as jamais eu en six cents ans.",
       es="Propongo un trato. No más sacrificios. Nunca más. A cambio... a cambio te ofrezco algo que nunca tuviste en seiscientos años.",
       it="Propongo un accordo. Niente più sacrifici. Mai più. In cambio... in cambio ti offro qualcosa che non hai mai avuto in seicento anni.")

    _t(tr, F, "narration_pact_creature",
       en="HUMANS BREAK PROMISES. WHY SHOULD I BELIEVE YOU?",
       fr="LES HUMAINS BRISENT LEURS PROMESSES. POURQUOI DEVRAIS-JE TE CROIRE ?",
       es="LOS HUMANOS ROMPEN SUS PROMESAS. ¿POR QUÉ DEBERÍA CREERTE?",
       it="GLI UMANI INFRANGONO LE PROMESSE. PERCHÉ DOVREI CREDERTI?")

    _t(tr, F, "elise_pact_2",
       en="My grandmother kept her promise for thirty years. Every month, every chant. Did she ever lie?",
       fr="Mà grand-mère à tenu sà promesse pendant trente ans. Chaque mois, chaque chant. A-t-elle jamais menti ?",
       es="Mi abuela cumplió su promesa durante treinta años. Cada mes, cada canto. ¿Mintió alguna vez?",
       it="Mia nonna ha mantenuto la sua promessa per trent'anni. Ogni mese, ogni canto. Ha mai mentito?")

    _t(tr, F, "narration_pact_creature_2",
       en="Silence. Long, infinite contemplation. Then: NO. SHE WAS... DIFFERENT. LIKE YOU.",
       fr="Silence. Une longue, infinie réflexion. Puis : NON. ELLE ÉTAIT... DIFFÉRENTE. COMME TOI.",
       es="Silencio. Una larga, infinita reflexión. Luego: NO. ELLA ERA... DIFERENTE. COMO TÚ.",
       it="Silenzio. Una lunga, infinita riflessione. Poi: NO. LEI ERA... DIVERSA. COME TE.")

    # --- Destroy branch ---
    _t(tr, F, "destroy_begin",
       en="Enough talk. Enough pity. This thing has accepted six hundred years of human sacrifices. Regardless of what it feels — it must end.",
       fr="Assez parlé. Assez de pitié. Cette chose à accepté six cents ans de sacrifices humains. Peu importe ce qu'elle ressent — çà doit cesser.",
       es="Basta de hablar. Basta de piedad. Esta cosa aceptó seiscientos años de sacrificios humanos. Sin importar lo que sienta — tiene que acabar.",
       it="Basta parlare. Basta pietà. Questa cosa ha accettato seicento anni di sacrifici umani. A prescindere da ciò che prova — deve finire.")

    _t(tr, F, "elise_destroy_1",
       en="Enough. Six hundred years of blood. Six hundred years of fear. Today you die!",
       fr="Çà suffit. Six cents ans de sang. Six cents ans de peur. Aujourd'hui tu meurs !",
       es="¡Basta! Seiscientos años de sangre. Seiscientos años de miedo. ¡Hoy mueres!",
       it="Basta. Seicento anni di sangue. Seicento anni di paura. Oggi muori!")

    _t(tr, F, "narration_destroy_creature",
       en="YOU WANT TO KILL ME? ME? I AM OLDER THAN YOUR DUST. YOU CANNOT TEAR DOWN A MOUNTAIN WITH BARE HANDS.",
       fr="TU VEUX ME TUER ? MOI ? JE SUIS PLUS ANCIEN QUE TA POUSSIÈRE. ON NE PEUT PAS DÉMOLIR UNE MONTAGNE À MAINS NUES.",
       es="¿QUIERES MATARME? ¿A MÍ? SOY MÁS ANTIGUO QUE TU POLVO. NO SE PUEDE DERRIBAR UNA MONTAÑA CON LAS MANOS DESNUDAS.",
       it="VUOI UCCIDERMI? ME? SONO PIÙ ANTICO DELLA TUA POLVERE. NON SI PUÒ ABBATTERE UNA MONTAGNA A MANI NUDE.")

    _t(tr, F, "destroy_attempt",
       en="I attack. With everything I have — will, rage, desperation. Grandmother's amulet glows, the herbs flare up, and I hurl everything against the consciousness beneath the stone.",
       fr="J'attaque. Avec tout ce que j'ai — volonté, rage, désespoir. L'amulette de grand-mère brille, les herbes s'embrasent, et je projette tout contre là conscience sous là pierre.",
       es="Ataco. Con todo lo que tengo — voluntad, rabia, desesperación. El amuleto de la abuela brilla, las hierbas se inflaman, y lanzo todo contra la consciencia bajo la piedra.",
       it="Attacco. Con tutto ciò che ho — volontà, rabbia, disperazione. L'amuleto della nonna brilla, le erbe si infiammano, è scaglio tutto contro la coscienza sotto la pietra.")

    _t(tr, F, "destroy_attempt_3",
       en="My attack bounces off like a wave against a continent. The entity is not evil — it is VAST. And the impact... the impact wakes it.",
       fr="Mon attaque rebondit comme une vague contre un continent. L'entité n'est pas maléfique — elle est IMMENSE. Et l'impact... l'impact là réveille.",
       es="Mi ataque rebota como una ola contra un continente. La entidad no es malvada — es INMENSA. Y el impacto... el impacto la despierta.",
       it="Il mio attacco rimbalza come un'onda contro un continente. L'entità non è malvagia — è IMMENSA. È l'impatto... l'impatto la sveglia.")

    _t(tr, F, "narration_destroy_recoil",
       en="PAIN. YOU GIVE ME PAIN. I HAVE HAD ENOUGH PAIN.",
       fr="DOULEUR. TU ME DONNES DE LA DOULEUR. J'AI EU ASSEZ DE DOULEUR.",
       es="DOLOR. ME DAS DOLOR. YA HE TENIDO BASTANTE DOLOR.",
       it="DOLORE. MI DAI DOLORE. HO AVUTO ABBASTANZA DOLORE.")

    _t(tr, F, "elise_destroy_2",
       en="It... it is moving. Oh God, it is MOVING—",
       fr="Il... il bouge. Mon Dieu, il BOUGE—",
       es="Se... se mueve. Dios mío, se MUEVE—",
       it="Si... si muove. Dio mio, si STA MUOVENDO—")

    # --- Fallback branch ---
    _t(tr, F, "route_fallback",
       en="I stand before the entity without a plan, without preparation. Just me and the abyss. And the abyss stares back.",
       fr="Je me tiens face à l'entité sans plan, sans préparation. Juste moi et l'abîme. Et l'abîme me regarde en retour.",
       es="Estoy frente a la entidad sin plan, sin preparación. Solo yo y el abismo. Y el abismo devuelve la mirada.",
       it="Sono di fronte all'entità senza un piano, senza preparazione. Solo io è l'abisso. È l'abisso ricambia lo sguardo.")

    _t(tr, F, "narration_fallback_creature",
       en="YOU HAVE CHOSEN NO PATH. THEN I CHOOSE FOR YOU.",
       fr="TU N'AS CHOISI AUCUN CHEMIN. ALORS JE CHOISIS POUR TOI.",
       es="NO HAS ELEGIDO NINGÚN CAMINO. ENTONCES YO ELIJO POR TI.",
       it="NON HAI SCELTO NESSUN CAMMINO. ALLORA SCELGO IO PER TE.")


def _add_act4_ending_seal(tr):
    F = "res://data/dialogue/act4/ending_seal.json"

    _t(tr, F, "narration_1",
       en="I begin the chant. The words Hilde taught me — older than any language I know. They flow from me as if I had always known them.",
       fr="Je commence le chant. Les mots que Hilde m'à enseignés — plus anciens que toute langue que je connais. Ils coulent de moi comme si je les avais toujours connus.",
       es="Comienzo el canto. Las palabras que Hilde me enseñó — más antiguas que cualquier idioma que conozco. Fluyen de mí como si siempre las hubiera sabido.",
       it="Comincio il canto. Le parole che Hilde mi ha insegnato — più antiche di qualsiasi lingua che conosca. Fluiscono da me come se le avessi sempre conosciute.")

    _t(tr, F, "narration_2",
       en="The chamber reacts. The spirals on the walls begin to glow, faintly at first, then brighter. A bluish light, cold as moonlight.",
       fr="Là chambre réagit. Les spirales sur les murs commencent à luire, faiblement d'abord, puis plus fort. Une lumière bleutée, froide comme le clair de lune.",
       es="La cámara reacciona. Las espirales en las paredes comienzan a brillar, débilmente al principio, luego con más fuerza. Una luz azulada, fría como la luz de la luna.",
       it="La camera reagisce. Le spirali sulle pareti cominciano a brillare, debolmente all'inizio, poi più forte. Una luce bluastra, fredda come il chiaro di luna.")

    _t(tr, F, "narration_3",
       en="The singing from the depths changes. It does not fight my chant — it answers. Two melodies intertwining like the spirals on the walls.",
       fr="Le chant des profondeurs change. Il ne lutte pas contre mon chant — il répond. Deux mélodies qui s'entrelacent comme les spirales sur les murs.",
       es="El canto de las profundidades cambia. No lucha contra mi canto — responde. Dos melodías entrelazándose como las espirales en las paredes.",
       it="Il canto dalle profondità cambia. Non combatte il mio canto — risponde. Due melodie che si intrecciano come le spirali sulle pareti.")

    _t(tr, F, "narration_4",
       en="The floor beneath me pulses faster. I feel the entity — its attention, its age, its infinite weariness. It WANTS to sleep. It has simply forgotten how.",
       fr="Le sol sous mes pieds pulse plus vite. Je sens l'entité — son attention, son âge, sà lassitude infinie. Elle VEUT dormir. Elle à simplement oublié comment.",
       es="El suelo bajo mis pies pulsa más rápido. Siento a la entidad — su atención, su edad, su cansancio infinito. QUIERE dormir. Simplemente ha olvidado cómo.",
       it="Il pavimento sotto di me pulsa più veloce. Sento l'entità — la sua attenzione, la sua età, la sua stanchezza infinita. VUOLE dormire. Ha semplicemente dimenticato come.")

    _t(tr, F, "narration_5",
       en="Grandmother's words: 'It is not evil. It is only old and hungry and alone.' I understand now. The feeding was never necessary. It only needed someone to sing it back to sleep.",
       fr="Les mots de grand-mère : « Ce n'est pas maléfique. C'est seulement vieux, affamé et seul. » Je comprends maintenant. Les offrandes n'ont jamais été nécessaires. Il avait seulement besoin de quelqu'un pour le rendormir en chantant.",
       es="Las palabras de la abuela: «No es malvado. Solo es viejo, hambriento y está solo.» Ahora lo entiendo. La alimentación nunca fue necesaria. Solo necesitaba a alguien que lo arrullara de vuelta al sueño.",
       it="Le parole della nonna: «Non è malvagio. È solo vecchio, affamato è solo.» Ora capisco. Le offerte non erano mai state necessarie. Aveva solo bisogno di qualcuno che lo cantasse di nuovo nel sonno.")

    _t(tr, F, "narration_6",
       en="The spirals condense into a pattern on the floor. A seal. Not made of stone or ink — of sound, of will, of the connection between my voice and the entity.",
       fr="Les spirales se condensent en un motif sur le sol. Un sceau. Non fait de pierre où d'encre — de son, de volonté, de là connexion entre mà voix et l'entité.",
       es="Las espirales se condensan en un patrón en el suelo. Un sello. No hecho de piedra ni tinta — de sonido, de voluntad, de la conexión entre mi voz y la entidad.",
       it="Le spirali si condensano in un disegno sul pavimento. Un sigillo. Non fatto di pietra o inchiostro — di suono, di volontà, della connessione tra la mia voce è l'entità.")

    _t(tr, F, "narration_7",
       en="The pulsing grows slower. Calmer. Like a child finally falling asleep. The bluish light fades to a gentle shimmer.",
       fr="Le battement ralentit. Se calme. Comme un enfant qui s'endort enfin. Là lumière bleutée s'estompe en un léger scintillement.",
       es="El pulso se vuelve más lento. Más tranquilo. Como un niño que por fin se queda dormido. La luz azulada se desvanece en un suave resplandor.",
       it="Il pulsare rallenta. Si calma. Come un bambino che finalmente si addormenta. La luce bluastra sfuma in un tenue bagliore.")

    _t(tr, F, "narration_8",
       en="Silence. True silence. For the first time since I entered Graubach, it is truly quiet. No singing, no pulsing, no whispering in my head.",
       fr="Le silence. Un vrai silence. Pour là première fois depuis que je suis entrée à Graubach, c'est véritablement calme. Plus de chant, plus de pulsation, plus de murmures dans mà tête.",
       es="Silencio. Verdadero silencio. Por primera vez desde que entré en Graubach, hay verdadera quietud. Ningún canto, ningún pulso, ningún susurro en mi cabeza.",
       it="Silenzio. Vero silenzio. Per la prima volta da quando sono entrata a Graubach, è davvero quiete. Nessun canto, nessun pulsare, nessun sussurro nella mia testa.")

    _t(tr, F, "narration_9",
       en="The seal is set. Not forever — nothing is forever. But for thirty years. Enough time.",
       fr="Le sceau est posé. Pas pour toujours — rien n'est éternel. Mais pour trente ans. Assez de temps.",
       es="El sello está puesto. No para siempre — nada es para siempre. Pero por treinta años. Tiempo suficiente.",
       it="Il sigillo è posto. Non per sempre — niente è per sempre. Ma per trent'anni. Abbastanza tempo.")

    _t(tr, F, "narration_10",
       en="I climb the stairs, through the church, into the morning light. It is a new day. The sky is blue. Truly blue.",
       fr="Je monte l'escalier, traverse l'église, sors dans là lumière du matin. C'est un nouveau jour. Le ciel est bleu. Vraiment bleu.",
       es="Subo las escaleras, cruzo la iglesia, salgo a la luz de la mañana. Es un nuevo día. El cielo es azul. Realmente azul.",
       it="Salgo le scale, attraverso la chiesa, esco nella luce del mattino. È un nuovo giorno. Il cielo è azzurro. Davvero azzurro.")

    _t(tr, F, "narration_11",
       en="Georg waits outside, Hilde beside him. They see my face and they know. Hilde nods. Georg weeps.",
       fr="Georg attend dehors, Hilde à ses côtés. Ils voient mon visage et comprennent. Hilde hoche là tête. Georg pleure.",
       es="Georg espera afuera, Hilde a su lado. Ven mi rostro y lo saben. Hilde asiente. Georg llora.",
       it="Georg aspetta fuori, Hilde accanto a lui. Vedono il mio volto è capiscono. Hilde annuisce. Georg piange.")

    _t(tr, F, "packed_books_seal",
       en="In my bag I find the books I brought from Berlin. Folklore texts. Back then I didn't know why I packed them. Now I know: Grandmother showed me the way before I knew there was one.",
       fr="Dans mon sac, je trouve les livres que j'ai apportés de Berlin. Des textes de folklore. À l'époque, je ne savais pas pourquoi je les avais emballés. Maintenant je sais : grand-mère m'à montré le chemin avant que je sache qu'il en existait un.",
       es="En mi bolso encuentro los libros que traje de Berlín. Textos de folclore. En aquel entonces no sabía por qué los empaqué. Ahora lo sé: la abuela me mostró el camino antes de que yo supiera que existía.",
       it="Nella mia borsa trovo i libri che ho portato da Berlino. Testi di folklore. Allora non sapevo perché li avessi messi in valigia. Ora lo so: la nonna mi ha indicato la strada prima che io sapessi che ce n'era una.")

    _t(tr, F, "packed_cross_seal",
       en="I hold Grandmother's crucifix in my hand. It was her only concession to the pastor's faith. But the true protection came from her, not from God.",
       fr="Je tiens le crucifix de grand-mère dans mà main. C'était sà seule concession à là foi du pasteur. Mais là vraie protection venait d'elle, pas de Dieu.",
       es="Sostengo el crucifijo de la abuela en mi mano. Era su única concesión a la fe del pastor. Pero la verdadera protección venía de ella, no de Dios.",
       it="Stringo il crocifisso della nonna nella mano. Era la sua unica concessione alla fede del pastore. Ma la vera protezione veniva da lei, non da Dio.")

    _t(tr, F, "packed_camera_seal",
       en="I brought the camera to capture Graubach. But what I experienced here fits no photograph. Some truths must be carried within.",
       fr="J'ai apporté l'appareil photo pour immortaliser Graubach. Mais ce que j'ai vécu ici ne tient sur aucune image. Certaines vérités doivent être portées en soi.",
       es="Traje la cámara para capturar Graubach. Pero lo que he vivido aquí no cabe en ninguna fotografía. Algunas verdades hay que llevarlas dentro.",
       it="Ho portato la macchina fotografica per immortalare Graubach. Ma ciò che ho vissuto qui non entra in nessuna fotografia. Alcune verità bisogna portarle dentro di sé.")

    _t(tr, F, "letter_resolution_seal",
       en="In Grandmother's journal I find a last page I had overlooked. Pinned with a needle, hidden behind the cover: 'Elise, if you are reading this, you did it. The letter I sent you — the truth I could not speak aloud: You were never in danger. You were the solution. Always.'",
       fr="Dans le journal de grand-mère, je trouve une dernière page que j'avais manquée. Épinglée avec une aiguille, cachée derrière là couverture : « Elise, si tu lis ceci, tu as réussi. Là lettre que je t'ai envoyée — là vérité que je ne pouvais dire à voix haute : tu n'as jamais été en danger. Tu étais là solution. Depuis toujours. »",
       es="En el diario de la abuela encuentro una última página que había pasado por alto. Sujeta con una aguja, oculta detrás de la cubierta: «Elise, si estás leyendo esto, lo lograste. La carta que te envié — la verdad que no pude decir en voz alta: nunca estuviste en peligro. Tú eras la solución. Siempre.»",
       it="Nel diario della nonna trovo un'ultima pagina che avevo trascurato. Appuntata con un ago, nascosta dietro la copertina: «Elise, se stai leggendo questo, ce l'hai fatta. La lettera che ti ho mandato — la verità che non potevo pronunciare ad alta voce: non sei mai stata in pericolo. Tu eri la soluzione. Da sempre.»")

    _t(tr, F, "narration_12",
       en="I will return to Berlin. Finish my studies. But I will come back. In thirty years, when the seal needs to be renewed. Or sooner, to find someone who will sing after me.",
       fr="Je retournerai à Berlin. Je finirai mes études. Mais je reviendrai. Dans trente ans, quand le sceau devrà être renouvelé. Ou plus tôt, pour trouver quelqu'un qui chanterà après moi.",
       es="Volveré a Berlín. Terminaré mis estudios. Pero regresaré. En treinta años, cuando el sello deba renovarse. O antes, para encontrar a alguien que cante después de mí.",
       it="Tornerò a Berlino. Finirò i miei studi. Ma tornerò qui. Fra trent'anni, quando il sigillo dovrà essere rinnovato. O prima, per trovare qualcuno che canti dopo di me.")

    _t(tr, F, "narration_13",
       en="Grandmother, I did it. Your life's work is complete.",
       fr="Grand-mère, j'ai réussi. L'œuvre de tà vie est accomplie.",
       es="Abuela, lo logré. La obra de tu vida está completa.",
       it="Nonna, ce l'ho fatta. L'opera della tua vita è compiuta.")

    # --- Creature dialogue during seal ---
    _t(tr, F, "narration_creature_seal",
       en="YOUR SONG IS LIKE HERS. BUT YOUNGER. WARMER. SHE SANG WITH DUTY. YOU SING WITH... SOMETHING ELSE.",
       fr="TON CHANT EST COMME LE SIEN. MAIS PLUS JEUNE. PLUS CHAUD. ELLE CHANTAIT PAR DEVOIR. TU CHANTES AVEC... AUTRE CHOSE.",
       es="TU CANTO ES COMO EL SUYO. PERO MÁS JOVEN. MÁS CÁLIDO. ELLA CANTABA POR DEBER. TÚ CANTAS CON... ALGO DIFERENTE.",
       it="IL TUO CANTO È COME IL SUO. MA PIÙ GIOVANE. PIÙ CALDO. LEI CANTAVA PER DOVERE. TU CANTI CON... QUALCOS'ALTRO.")
    _t(tr, F, "elise_seal_1",
       en="Then let me help you. Sleep. Not by force. Because you are tired.",
       fr="Alors laisse-moi t'aider. Dors. Pas par contrainte. Parce que tu es fatigué.",
       es="Entonces déjame ayudarte. Duerme. No por la fuerza. Porque estás cansado.",
       it="Allora lasciami aiutarti. Dormi. Non per costrizione. Perché sei stanco.")
    _t(tr, F, "narration_creature_seal_2",
       en="I AM... SO TIRED. SO LONG AWAKE. SO LONG HUNGRY. YOUR SONG MAKES THE HUNGER QUIETER.",
       fr="JE SUIS... SI FATIGUÉ. SI LONGTEMPS ÉVEILLÉ. SI LONGTEMPS AFFAMÉ. TON CHANT REND LA FAIM PLUS SILENCIEUSE.",
       es="ESTOY... TAN CANSADO. TANTO TIEMPO DESPIERTO. TANTO TIEMPO HAMBRIENTO. TU CANTO HACE QUE EL HAMBRE SEA MÁS SILENCIOSA.",
       it="SONO... COSÌ STANCO. COSÌ A LUNGO SVEGLIO. COSÌ A LUNGO AFFAMATO. IL TUO CANTO RENDE LA FAME PIÙ SILENZIOSA.")
    _t(tr, F, "elise_seal_2",
       en="Sleep well. I will come back. In thirty years. Or sooner.",
       fr="Dors bien. Je reviendrai. Dans trente ans. Ou plus tôt.",
       es="Duerme bien. Volveré. En treinta años. O antes.",
       it="Dormi bene. Tornerò. Fra trent'anni. O prima.")
    _t(tr, F, "narration_creature_seal_3",
       en="PROMISED?",
       fr="PROMIS ?",
       es="¿PROMETIDO?",
       it="PROMESSO?")
    _t(tr, F, "elise_seal_3",
       en="Promised.",
       fr="Promis.",
       es="Prometido.",
       it="Promesso.")
    _t(tr, F, "narration_8b",
       en="I pull my hands from the stone. They are trembling. My cheeks are wet — I have been crying without realizing it. Tears of joy? Grief? I do not know.",
       fr="Je retire mes mains de là pierre. Elles tremblent. Mes joues sont mouillées — j'ai pleuré sans m'en rendre compte. Des larmes de joie ? De chagrin ? Je ne sais pas.",
       es="Retiro mis manos de la piedra. Tiemblan. Mis mejillas están mojadas — he llorado sin darme cuenta. ¿Lágrimas de alegría? ¿De tristeza? No lo sé.",
       it="Ritiro le mani dalla pietra. Tremano. Le mie guance sono bagnate — ho pianto senza rendermene conto. Lacrime di gioia? Di dolore? Non lo so.")
    # --- Georg ally branch (seal) ---
    _t(tr, F, "narration_georg_waits",
       en="Georg waits outside. He sees my face and knows. His eyes fill with tears.",
       fr="Georg attend dehors. Il voit mon visage et comprend. Ses yeux se remplissent de larmes.",
       es="Georg espera afuera. Ve mi rostro y lo sabe. Sus ojos se llenan de lágrimas.",
       it="Georg aspetta fuori. Vede il mio volto è capisce. I suoi occhi si riempiono di lacrime.")
    _t(tr, F, "georg_seal_1",
       en="You did it. Margarethe... she would have...",
       fr="Tu as réussi. Margarethe... elle aurait...",
       es="Lo lograste. Margarethe... ella habría...",
       it="Ce l'hai fatta. Margarethe... lei avrebbe...")
    _t(tr, F, "elise_georg_seal",
       en="I know. She would have cried and laughed at the same time.",
       fr="Je sais. Elle aurait pleuré et ri en même temps.",
       es="Lo sé. Habría llorado y reído al mismo tiempo.",
       it="Lo so. Avrebbe pianto è riso allo stesso tempo.")
    _t(tr, F, "georg_seal_2",
       en="Exactly. Exactly so.",
       fr="Exactement. Exactement comme ça.",
       es="Exacto. Exactamente así.",
       it="Esatto. Proprio così.")
    _t(tr, F, "narration_georg_embrace",
       en="Georg embraces me. For the first time. He smells of iron and smoke and relief. Thirty years of burden fall from his shoulders.",
       fr="Georg me prend dans ses bras. Pour là première fois. Il sent le fer, là fumée et le soulagement. Trente ans de fardeau tombent de ses épaules.",
       es="Georg me abraza. Por primera vez. Huele a hierro, humo y alivio. Treinta años de carga caen de sus hombros.",
       it="Georg mi abbraccia. Per la prima volta. Odora di ferro, fumo è sollievo. Trent'anni di peso gli cadono dalle spalle.")
    # --- Hilde ally branch (seal) ---
    _t(tr, F, "hilde_seal_1",
       en="I heard the chant. All the way here. It was... beautiful.",
       fr="J'ai entendu le chant. Jusqu'ici. Il était... beau.",
       es="Escuché el canto. Hasta aquí. Era... hermoso.",
       it="Ho sentito il canto. Fin quassù. Era... bello.")
    _t(tr, F, "elise_hilde_seal",
       en="It answered, Hilde. It sang with me. In the end it was almost... peaceful.",
       fr="Il à répondu, Hilde. Il à chanté avec moi. À là fin, c'était presque... paisible.",
       es="Respondió, Hilde. Cantó conmigo. Al final fue casi... pacífico.",
       it="Ha risposto, Hilde. Ha cantato con me. Alla fine era quasi... sereno.")
    _t(tr, F, "hilde_seal_2",
       en="Your grandmother always said that the right chant does not bind the entity. It rocks it to sleep. Like a lullaby.",
       fr="Tà grand-mère à toujours dit que le bon chant ne lie pas l'entité. Il là berce pour l'endormir. Comme une berceuse.",
       es="Tu abuela siempre decía que el canto correcto no ata a la entidad. La mece hasta dormirla. Como una nana.",
       it="Tua nonna diceva sempre che il canto giusto non lega l'entità. La culla fino a farla addormentare. Come una ninna nanna.")
    # --- Voss ally branch (seal) ---
    _t(tr, F, "voss_seal_1",
       en="Thank God. Thank God.",
       fr="Dieu merci. Dieu merci.",
       es="Gracias a Dios. Gracias a Dios.",
       it="Grazie a Dio. Grazie a Dio.")
    _t(tr, F, "elise_voss_seal",
       en="Not God, Pastor. Grandmother. And a very tired, very lonely entity that is finally allowed to sleep.",
       fr="Pas Dieu, Pasteur. Grand-mère. Et une entité très fatiguée, très seule, qui à enfin le droit de dormir.",
       es="No Dios, Pastor. La abuela. Y una entidad muy cansada, muy solitaria, que por fin puede dormir.",
       it="Non Dio, Pastore. La nonna. È un'entità molto stanca, molto sola, che finalmente può dormire.")
    _t(tr, F, "voss_seal_2",
       en="Is it... is it over? No more sacrifice?",
       fr="Est-ce... est-ce fini ? Plus de sacrifice ?",
       es="¿Se... se acabó? ¿No más sacrificios?",
       it="È... è finita? Nessun altro sacrificio?")
    _t(tr, F, "elise_voss_seal_2",
       en="No more sacrifice. Never again. We have thirty years to find a permanent solution.",
       fr="Plus de sacrifice. Plus jamais. Nous avons trente ans pour trouver une solution permanente.",
       es="No más sacrificios. Nunca más. Tenemos treinta años para encontrar una solución permanente.",
       it="Nessun altro sacrificio. Mai più. Abbiamo trent'anni per trovare una soluzione permanente.")
    # --- Village morning and letter ---
    _t(tr, F, "narration_village_morning",
       en="The village awakens. Windows open. Children run into the street. The silence of Graubach is, for the first time in centuries, an ordinary, peaceful silence.",
       fr="Le village s'éveille. Les fenêtres s'ouvrent. Les enfants courent dans là rue. Le silence de Graubach est, pour là première fois en des siècles, un silence ordinaire et paisible.",
       es="El pueblo despierta. Las ventanas se abren. Los niños corren por la calle. El silencio de Graubach es, por primera vez en siglos, un silencio ordinario y pacífico.",
       it="Il villaggio si sveglia. Le finestre si aprono. I bambini corrono per la strada. Il silenzio di Graubach è, per la prima volta in secoli, un silenzio ordinario è pacifico.")
    _t(tr, F, "narration_letter_seal",
       en="'Elise, if you are reading this, you did it. You were never in danger. You were the solution. Always.'",
       fr="« Elise, si tu lis ces lignes, tu as réussi. Tu n'as jamais été en danger. Tu étais là solution. Depuis toujours. »",
       es="«Elise, si estás leyendo esto, lo lograste. Nunca estuviste en peligro. Tú eras la solución. Siempre.»",
       it="«Elise, se stai leggendo questo, ce l'hai fatta. Non sei mai stata in pericolo. Tu eri la soluzione. Da sempre.»")
    _t(tr, F, "elise_letter_react",
       en="I lay the journal on the table and laugh. For the first time in a week, I laugh. Through the tears, but it is a real laugh.",
       fr="Je pose le journal sur là table et je ris. Pour là première fois depuis une semaine, je ris. À travers les larmes, mais c'est un vrai rire.",
       es="Dejo el diario sobre la mesa y me río. Por primera vez en una semana, me río. Entre las lágrimas, pero es una risa de verdad.",
       it="Poso il diario sul tavolo è rido. Per la prima volta in una settimana, rido. Attraverso le lacrime, ma è una risata vera.")
    _t(tr, F, "narration_12b",
       en="For beneath the stone sleeps something to which I have made a promise. And Brandts keep their promises.",
       fr="Car sous là pierre dort quelque chose à qui j'ai fait une promesse. Et les Brandt tiennent leurs promesses.",
       es="Porque bajo la piedra duerme algo a lo que he hecho una promesa. Y los Brandt cumplen sus promesas.",
       it="Perché sotto la pietra dorme qualcosa a cui ho fatto una promessa. È i Brandt mantengono le loro promesse.")

    _t(tr, F, "journal_seal",
       en="The Seal",
       fr="Le Sceau",
       es="El Sello",
       it="Il Sigillo",
       field="title")
    _t(tr, F, "journal_seal",
       en="The binding ritual succeeded. The entity sleeps again, held by song instead of blood. No more sacrifices. Grandmother's thirty years of research have proven their worth.",
       fr="Le rituel de liaison à réussi. L'entité dort à nouveau, retenue par le chant au lieu du sang. Plus de sacrifices. Les trente années de recherches de grand-mère ont porté leurs fruits.",
       es="El ritual de vinculación tuvo éxito. La entidad duerme de nuevo, sostenida por el canto en lugar de la sangre. No más sacrificios. Los treinta años de investigación de la abuela han dado sus frutos.",
       it="Il rituale di legame è riuscito. L'entità dorme di nuovo, trattenuta dal canto invece che dal sangue. Niente più sacrifici. I trent'anni di ricerche della nonna hanno dato i loro frutti.",
       field="content")


def _add_act4_ending_escape(tr):
    F = "res://data/dialogue/act4/ending_escape.json"

    _t(tr, F, "narration_1",
       en="It goes wrong. Everything goes wrong. The floor tears open, the spirals explode in blinding light, and the singing becomes a scream.",
       fr="Tout và mal. Tout và de travers. Le sol se déchire, les spirales explosent en une lumière aveuglante, et le chant devient un cri.",
       es="Sale mal. Todo sale mal. El suelo se abre, las espirales explotan en una luz cegadora y el canto se convierte en un grito.",
       it="Va storto. Tutto va storto. Il pavimento si squarcia, le spirali esplodono in una luce accecante, è il canto diventa un urlo.")

    _t(tr, F, "narration_2",
       en="Georg is suddenly there. He fought his way through Otto's men, down the stairs, into the shaking chamber.",
       fr="Georg est soudain là. Il s'est frayé un chemin à travers les hommes d'Otto, à descendu l'escalier, est entré dans là chambre qui tremble.",
       es="Georg aparece de repente. Se abrió paso entre los hombres de Otto, bajó las escaleras, entró en la cámara temblorosa.",
       it="Georg è improvvisamente lì. Si è fatto strada tra gli uomini di Otto, giù per le scale, nella camera che trema.")

    _t(tr, F, "georg_1",
       en="ELISE! GET OUT! NOW!",
       fr="ELISE ! SORS D'ICI ! TOUT DE SUITE !",
       es="¡ELISE! ¡SAL DE AQUÍ! ¡AHORA!",
       it="ELISE! FUORI DI QUI! SUBITO!")

    _t(tr, F, "narration_3",
       en="I try to speak, to tell him I can still make it. But he grabs my arm and drags me toward the stairs.",
       fr="J'essaie de parler, de lui dire que je peux encore y arriver. Mais il m'attrape le bras et me traîne vers l'escalier.",
       es="Intento hablar, decirle que aún puedo lograrlo. Pero me agarra del brazo y me arrastra hacia las escaleras.",
       it="Cerco di parlare, di dirgli che posso ancora farcela. Ma mi afferra il braccio è mi trascina verso le scale.")

    _t(tr, F, "georg_3",
       en="It's too late for the seal. But not for you. Go. Run. I'll hold it off.",
       fr="Il est trop tard pour le sceau. Mais pas pour toi. Va. Cours. Je vais le retenir.",
       es="Es demasiado tarde para el sello. Pero no para ti. Ve. Corre. Yo lo contendré.",
       it="È troppo tardi per il sigillo. Ma non per te. Vai. Corri. Lo terrò a bada.")

    _t(tr, F, "narration_4",
       en="'Georg, no —' But he has already turned around. He stands with legs braced on the pulsing floor, the forge hammer in both hands.",
       fr="« Georg, non — » Mais il s'est déjà retourné. Il se tient les jambes écartées sur le sol pulsant, le marteau de forge dans les deux mains.",
       es="«Georg, no...» Pero ya se ha dado la vuelta. Está de pie con las piernas firmes sobre el suelo pulsante, el martillo de forja en ambas manos.",
       it="«Georg, no —» Ma si è già voltato. Sta in piedi a gambe larghe sul pavimento pulsante, il martello da fucina in entrambe le mani.")

    _t(tr, F, "georg_4",
       en="I was silent for thirty years, Elise. Thirty years of cowardice. Let me do the right thing at least once.",
       fr="J'ai gardé le silence pendant trente ans, Elise. Trente ans de lâcheté. Laisse-moi faire ce qui est juste au moins une fois.",
       es="Callé durante treinta años, Elise. Treinta años de cobardía. Déjame hacer lo correcto al menos una vez.",
       it="Ho taciuto per trent'anni, Elise. Trent'anni di vigliaccheria. Lasciami fare la cosa giusta almeno una volta.")

    _t(tr, F, "narration_5",
       en="He strikes the hammer on the floor. Once. The stone breaks. The singing becomes silence — not peaceful, but startled. Confused.",
       fr="Il frappe le marteau sur le sol. Une fois. Là pierre se brise. Le chant devient silence — pas paisible, mais stupéfait. Confus.",
       es="Golpea el martillo contra el suelo. Una vez. La piedra se quiebra. El canto se convierte en silencio — no pacífico, sino sobresaltado. Confuso.",
       it="Colpisce il martello sul pavimento. Una volta. La pietra si spezza. Il canto diventa silenzio — non pacifico, ma attonito. Confuso.")

    _t(tr, F, "narration_6",
       en="I run. Up the stairs, through the church, into the open. Behind me the floor collapses. Dust and light and a sound that should not be a sound.",
       fr="Je cours. L'escalier, à travers l'église, dehors. Derrière moi, le sol s'effondre. Poussière et lumière et un son qui ne devrait pas être un son.",
       es="Corro. Escaleras arriba, a través de la iglesia, al exterior. Detrás de mí el suelo se derrumba. Polvo y luz y un sonido que no debería ser un sonido.",
       it="Corro. Su per le scale, attraverso la chiesa, all'aperto. Dietro di me il pavimento crolla. Polvere è luce è un suono che non dovrebbe essere un suono.")

    _t(tr, F, "narration_7",
       en="I keep running. Through the village, past the well, past the dark houses. The forest opens — for the first time, the forest opens.",
       fr="Je continue de courir. À travers le village, devant le puits, devant les maisons sombres. Là forêt s'ouvre — pour là première fois, là forêt s'ouvre.",
       es="Sigo corriendo. A través del pueblo, junto al pozo, junto a las casas oscuras. El bosque se abre — por primera vez, el bosque se abre.",
       it="Continuo a correre. Attraverso il villaggio, oltre il pozzo, oltre le case buie. Il bosco si apre — per la prima volta, il bosco si apre.")

    _t(tr, F, "narration_8",
       en="I turn around one last time. Graubach is sinking. The houses cave in, the church tilts, the forest swallows everything. In seconds, nothing remains.",
       fr="Je me retourne une dernière fois. Graubach s'enfonce. Les maisons s'affaissent, l'église penche, là forêt engloutit tout. En quelques secondes, il ne reste plus rien.",
       es="Me giro una última vez. Graubach se hunde. Las casas se desploman, la iglesia se inclina, el bosque lo devora todo. En segundos, no queda nada.",
       it="Mi volto un'ultima volta. Graubach sprofonda. Le case cedono, la chiesa si inclina, il bosco inghiotte tutto. In pochi secondi, non resta più nulla.")

    _t(tr, F, "narration_9",
       en="Only forest. As if Graubach had never existed.",
       fr="Rien que là forêt. Comme si Graubach n'avait jamais existé.",
       es="Solo bosque. Como si Graubach nunca hubiera existido.",
       it="Solo bosco. Come se Graubach non fosse mai esistita.")

    _t(tr, F, "narration_10",
       en="Georg. My uncle. The man who walked bent with guilt for thirty years and stood upright at the end.",
       fr="Georg. Mon oncle. L'homme qui à marché courbé sous là culpabilité pendant trente ans et qui s'est tenu droit à là fin.",
       es="Georg. Mi tío. El hombre que caminó encorvado por la culpa durante treinta años y al final se irguió.",
       it="Georg. Mio zio. L'uomo che ha camminato piegato dal senso di colpa per trent'anni è alla fine si è alzato in piedi.")

    _t(tr, F, "narration_11",
       en="I walk. Through the forest, into the night, back to a world that knows nothing of Graubach. That will never know of Graubach.",
       fr="Je marche. À travers là forêt, dans là nuit, vers un monde qui ne sait rien de Graubach. Qui ne saurà jamais rien de Graubach.",
       es="Camino. A través del bosque, en la noche, de vuelta a un mundo que no sabe nada de Graubach. Que nunca sabrá de Graubach.",
       it="Cammino. Attraverso il bosco, nella notte, verso un mondo che non sa nulla di Graubach. Che non saprà mai di Graubach.")

    _t(tr, F, "narration_12",
       en="In my pocket lies Grandmother's journal. The proof that it was real. That Georg was real. That his sacrifice meant something.",
       fr="Dans mà poche se trouve le journal de grand-mère. Là preuve que c'était réel. Que Georg était réel. Que son sacrifice à eu un sens.",
       es="En mi bolsillo está el diario de la abuela. La prueba de que fue real. De que Georg fue real. De que su sacrificio significó algo.",
       it="Nella mia tasca c'è il diario della nonna. La prova che era reale. Che Georg era reale. Che il suo sacrificio ha avuto un senso.")

    # --- Elise dialogue during escape ---
    _t(tr, F, "elise_escape_1",
       en="No — NO! The chant is breaking — I cannot hold it —",
       fr="Non — NON ! Le chant se brise — je ne peux pas le maintenir —",
       es="No — ¡NO! El canto se rompe — no puedo mantenerlo —",
       it="No — NO! Il canto si spezza — non riesco a tenerlo —")
    _t(tr, F, "elise_escape_2",
       en="Georg, no! I can still make it — give me one more minute —",
       fr="Georg, non ! Je peux encore y arriver — donne-moi encore une minute —",
       es="¡Georg, no! Aún puedo lograrlo — dame un minuto más —",
       it="Georg, no! Posso ancora farcela — dammi ancora un minuto —")
    _t(tr, F, "georg_2",
       en="It is too late for the seal. But not for you. Go. Run. I will hold it off.",
       fr="Il est trop tard pour le sceau. Mais pas pour toi. Va. Cours. Je le retiendrai.",
       es="Es demasiado tarde para el sello. Pero no para ti. Ve. Corre. Yo lo detendré.",
       it="È troppo tardi per il sigillo. Ma non per te. Vai. Corri. Lo terrò a bada.")
    _t(tr, F, "elise_escape_3",
       en="Georg, NO! You cannot — it will —",
       fr="Georg, NON ! Tu ne peux pas — çà và te —",
       es="¡Georg, NO! No puedes — te va a —",
       it="Georg, NO! Non puoi — ti —")
    _t(tr, F, "elise_escape_4",
       en="You are not a coward. You were never a coward. Grandmother knew that.",
       fr="Tu n'es pas un lâche. Tu n'as jamais été un lâche. Grand-mère le savait.",
       es="No eres un cobarde. Nunca fuiste un cobarde. La abuela lo sabía.",
       it="Non sei un codardo. Non sei mai stato un codardo. La nonna lo sapeva.")
    _t(tr, F, "creature_escape_1",
       en="WHAT IS HE DOING? THE STONE — HE IS BREAKING THE STONE — NO —",
       fr="QUE FAIT-IL ? LA PIERRE — IL BRISE LA PIERRE — NON —",
       es="¿QUÉ HACE? LA PIEDRA — ESTÁ ROMPIENDO LA PIEDRA — NO —",
       it="CHE COSA FA? LA PIETRA — STA SPEZZANDO LA PIETRA — NO —")
    _t(tr, F, "narration_hammer",
       en="Georg strikes a second time. A third. Each blow a thunderclap. The chamber trembles. Georg roars — not in rage. In grief. Thirty years of grief in every blow.",
       fr="Georg frappe une deuxième fois. Une troisième. Chaque coup est un coup de tonnerre. Là chambre tremble. Georg rugit — pas de rage. De chagrin. Trente ans de chagrin dans chaque coup.",
       es="Georg golpea una segunda vez. Una tercera. Cada golpe un trueno. La cámara tiembla. Georg ruge — no de ira. De dolor. Treinta años de dolor en cada golpe.",
       it="Georg colpisce una seconda volta. Una terza. Ogni colpo un tuono. La camera trema. Georg ruggisce — non di rabbia. Di dolore. Trent'anni di dolore in ogni colpo.")
    _t(tr, F, "elise_escape_5",
       en="GEORG!",
       fr="GEORG !",
       es="¡GEORG!",
       it="GEORG!")
    _t(tr, F, "narration_no_answer",
       en="No answer. Only the breaking of stone and the silencing of the singing.",
       fr="Pas de réponse. Seulement le bris de là pierre et le silence du chant.",
       es="Sin respuesta. Solo el quebrarse de la piedra y el silencio del canto.",
       it="Nessuna risposta. Solo il frantumarsi della pietra è il tacere del canto.")
    # --- Hilde escape branch ---
    _t(tr, F, "hilde_escape_1",
       en="Elise! Keep running! Do not stop!",
       fr="Elise ! Continue de courir ! Ne t'arrête pas !",
       es="¡Elise! ¡Sigue corriendo! ¡No te detengas!",
       it="Elise! Continua a correre! Non fermarti!")
    _t(tr, F, "elise_hilde_escape",
       en="Georg is still down there — he —",
       fr="Georg est encore là-bas — il à —",
       es="Georg sigue allá abajo — él —",
       it="Georg è ancora laggiù — lui —")
    _t(tr, F, "hilde_escape_2",
       en="I know. I know, child. But we must LIVE. That was his last wish.",
       fr="Je sais. Je sais, mon enfant. Mais nous devons VIVRE. C'était son dernier souhait.",
       es="Lo sé. Lo sé, niña. Pero debemos VIVIR. Ese fue su último deseo.",
       it="Lo so. Lo so, bambina. Ma dobbiamo VIVERE. Era il suo ultimo desiderio.")
    # --- Voss escape branch ---
    _t(tr, F, "voss_escape_1",
       en="The church is collapsing! We must get to the forest —",
       fr="L'église s'effondre ! Nous devons gagner là forêt —",
       es="¡La iglesia se derrumba! Debemos llegar al bosque —",
       it="La chiesa sta crollando! Dobbiamo raggiungere il bosco —")
    _t(tr, F, "elise_voss_escape",
       en="Georg is down there. He sacrificed himself. For me. For all of us.",
       fr="Georg est là-bas. Il s'est sacrifié. Pour moi. Pour nous tous.",
       es="Georg está allá abajo. Se sacrificó. Por mí. Por todos nosotros.",
       it="Georg è laggiù. Si è sacrificato. Per me. Per tutti noi.")
    _t(tr, F, "voss_escape_2",
       en="God take him in. Come, Fräulein Brandt. His sacrifice must not be in vain.",
       fr="Que Dieu l'accueille. Venez, Fräulein Brandt. Son sacrifice ne doit pas être vain.",
       es="Dios lo acoja. Venga, Fräulein Brandt. Su sacrificio no debe ser en vano.",
       it="Dio lo accolga. Venga, Fräulein Brandt. Il suo sacrificio non deve essere vano.")
    _t(tr, F, "elise_escape_6",
       en="Georg...",
       fr="Georg...",
       es="Georg...",
       it="Georg...")
    # --- Epilogue ---
    _t(tr, F, "narration_10b",
       en="I pick it up. It is heavy. As heavy as thirty years of guilt. But also as heavy as thirty years of loyalty.",
       fr="Je le ramasse. Il est lourd. Aussi lourd que trente ans de culpabilité. Mais aussi lourd que trente ans de fidélité.",
       es="Lo levanto. Es pesado. Tan pesado como treinta años de culpa. Pero también tan pesado como treinta años de lealtad.",
       it="Lo raccolgo. È pesante. Pesante come trent'anni di colpa. Ma anche pesante come trent'anni di fedeltà.")
    _t(tr, F, "narration_epilog",
       en="Weeks later, in Berlin. I sit in my room. Georg's hammer stands by the door. Grandmother's journal lies on the desk.",
       fr="Des semaines plus tard, à Berlin. Je suis assise dans mà chambre. Le marteau de Georg est posé près de là porte. Le journal de grand-mère repose sur le bureau.",
       es="Semanas después, en Berlín. Estoy sentada en mi habitación. El martillo de Georg está junto a la puerta. El diario de la abuela yace sobre el escritorio.",
       it="Settimane dopo, a Berlino. Sono seduta nella mia stanza. Il martello di Georg è accanto alla porta. Il diario della nonna giace sulla scrivania.")
    _t(tr, F, "narration_epilog_2",
       en="Sometimes, in the silence between midnight and dawn, I think I hear the singing. Soft. Distant. Almost like a lullaby.",
       fr="Parfois, dans le silence entre minuit et l'aube, je crois entendre le chant. Doux. Lointain. Presque comme une berceuse.",
       es="A veces, en el silencio entre la medianoche y el amanecer, creo escuchar el canto. Suave. Lejano. Casi como una nana.",
       it="A volte, nel silenzio tra la mezzanotte è l'alba, mi sembra di sentire il canto. Sommesso. Lontano. Quasi come una ninna nanna.")
    _t(tr, F, "narration_epilog_3",
       en="Did Georg survive? I do not know. Graubach exists on no map anymore. The forest has closed. But sometimes I dream that he stands at the well, waiting.",
       fr="Georg a-t-il survécu ? Je ne sais pas. Graubach n'existe plus sur aucune carte. Là forêt s'est refermée. Mais parfois je rêve qu'il se tient près du puits et qu'il attend.",
       es="¿Sobrevivió Georg? No lo sé. Graubach ya no existe en ningún mapa. El bosque se ha cerrado. Pero a veces sueño que está junto al pozo, esperando.",
       it="Georg è sopravvissuto? Non lo so. Graubach non esiste più su nessuna mappa. Il bosco si è chiuso. Ma a volte sogno che sia in piedi accanto al pozzo, in attesa.")
    _t(tr, F, "narration_epilog_4",
       en="Grandmother, you sent me to end it. I failed. But Georg... Georg did the right thing. In the end, he was the bravest of us all.",
       fr="Grand-mère, tu m'as envoyée pour en finir. J'ai échoué. Mais Georg... Georg à fait ce qu'il fallait. À là fin, il était le plus courageux de nous tous.",
       es="Abuela, me enviaste para terminarlo. Fracasé. Pero Georg... Georg hizo lo correcto. Al final, fue el más valiente de todos nosotros.",
       it="Nonna, mi hai mandata per finirla. Ho fallito. Ma Georg... Georg ha fatto la cosa giusta. Alla fine, è stato il più coraggioso di tutti noi.")
    _t(tr, F, "journal_escape",
       en="The Escape",
       fr="Là Fuite",
       es="La huida",
       it="La fuga",
       field="title")
    _t(tr, F, "journal_escape",
       en="Graubach has vanished. Georg sacrificed himself so I could escape. His hammer is all I have left. And the question that never lets me go: Did he survive?",
       fr="Graubach à disparu. Georg s'est sacrifié pour que je puisse fuir. Son marteau est tout ce qu'il me reste. Et là question qui ne me quitte jamais : a-t-il survécu ?",
       es="Graubach ha desaparecido. Georg se sacrificó para que yo pudiera escapar. Su martillo es todo lo que me queda. Y la pregunta que nunca me deja: ¿sobrevivió?",
       it="Graubach è scomparsa. Georg si è sacrificato perché io potessi fuggire. Il suo martello è tutto ciò che mi resta. È la domanda che non mi lascia mai: è sopravvissuto?",
       field="content")


def _add_act4_ending_pact(tr):
    F = "res://data/dialogue/act4/ending_pact.json"

    _t(tr, F, "narration_1",
       en="I speak to the entity. Not with words — with thoughts, with will. I step onto the earth sign and open my mind.",
       fr="Je parle à l'entité. Pas avec des mots — avec des pensées, avec de là volonté. Je me place sur le signe de terre et j'ouvre mon esprit.",
       es="Le hablo a la entidad. No con palabras — con pensamientos, con voluntad. Me coloco sobre el signo de la tierra y abro mi mente.",
       it="Parlo all'entità. Non con parole — con pensieri, con volontà. Mi posiziono sul segno della terrà è apro la mia mente.")

    _t(tr, F, "narration_2",
       en="It answers. Not in words. In images, feelings, memories that are not mine. I see millennia in seconds. Civilizations that came and went like tides.",
       fr="Elle répond. Pas en mots. En images, en sentiments, en souvenirs qui ne sont pas les miens. Je vois des millénaires en quelques secondes. Des civilisations qui sont venues et reparties comme des marées.",
       es="Responde. No con palabras. Con imágenes, sentimientos, recuerdos que no son míos. Veo milenios en segundos. Civilizaciones que vinieron y se fueron como mareas.",
       it="Risponde. Non con parole. Con immagini, sentimenti, ricordi che non sono miei. Vedo millenni in secondi. Civiltà che sono venute è andate come maree.")

    _t(tr, F, "narration_3",
       en="And hunger. A hunger so old and deep that it blurs the boundaries between emotion and natural law. It needs nourishment. Not flesh, not blood — attention. Consciousness. Contact.",
       fr="Et là faim. Une faim si ancienne et si profonde qu'elle brouille les frontières entre émotion et loi naturelle. Elle à besoin de nourriture. Pas de chair, pas de sang — de l'attention. De là conscience. Du contact.",
       es="Y hambre. Un hambre tan antiguo y profundo que difumina los límites entre emoción y ley natural. Necesita alimento. No carne, no sangre — atención. Conciencia. Contacto.",
       it="E fame. Una fame così antica è profonda da confondere i confini tra emozione è legge naturale. Ha bisogno di nutrimento. Non carne, non sangue — attenzione. Coscienza. Contatto.")

    _t(tr, F, "narration_4",
       en="I offer a bargain: I will become the guardian. No more sacrifices, no blood. Instead, I will come every year, sit on the sign, and let it touch my thoughts.",
       fr="Je propose un marché : je deviendrai là gardienne. Plus de sacrifices, plus de sang. À là place, je viendrai chaque année, m'assiérai sur le signe et le laisserai toucher mes pensées.",
       es="Ofrezco un trato: me convertiré en la guardiana. No más sacrificios, no más sangre. En cambio, vendré cada año, me sentaré sobre el signo y dejaré que toque mis pensamientos.",
       it="Offro un patto: diventerò la guardiana. Niente più sacrifici, niente sangue. Invece, verrò ogni anno, mi siederò sul segno è gli lascerò toccare i miei pensieri.")

    _t(tr, F, "narration_5",
       en="It considers. I feel its skepticism, its experience with broken promises. But also its weariness. It doesn't want to fight anymore. It just doesn't want to be forgotten.",
       fr="Elle réfléchit. Je sens son scepticisme, son expérience des promesses brisées. Mais aussi sà lassitude. Elle ne veut plus se battre. Elle veut simplement ne pas être oubliée.",
       es="Lo considera. Siento su escepticismo, su experiencia con promesas rotas. Pero también su cansancio. Ya no quiere luchar. Solo no quiere ser olvidada.",
       it="Ci pensa. Sento il suo scetticismo, la sua esperienza con le promesse infrante. Ma anche la sua stanchezza. Non vuole più combattere. Vuole solo non essere dimenticata.")

    _t(tr, F, "narration_7",
       en="It accepts. I feel the pact forming — not as a contract, but as a connection. A thin thread between its consciousness and mine. It will never break.",
       fr="Elle accepte. Je sens le pacte se former — non comme un contrat, mais comme une connexion. Un fil ténu entre sà conscience et là mienne. Il ne se romprà jamais.",
       es="Acepta. Siento el pacto formarse — no como un contrato, sino como una conexión. Un hilo delgado entre su conciencia y la mía. Nunca se romperá.",
       it="Accetta. Sento il patto formarsi — non come un contratto, ma come una connessione. Un filo sottile tra la sua coscienza è la mia. Non si spezzerà mai.")

    _t(tr, F, "narration_8",
       en="The singing grows softer. Gentler. Satisfied. The pulsing beneath my feet slows to a calm rhythm.",
       fr="Le chant devient plus doux. Plus tendre. Satisfait. Le battement sous mes pieds ralentit en un rythme calme.",
       es="El canto se vuelve más suave. Más dulce. Satisfecho. El pulso bajo mis pies se ralentiza hasta un ritmo tranquilo.",
       it="Il canto si fa più sommesso. Più dolce. Soddisfatto. Il pulsare sotto i miei piedi rallenta in un ritmo calmo.")

    _t(tr, F, "narration_9",
       en="I leave the chamber. The village outside looks normal again. The houses stand straight, the sky is grey and ordinary. Graubach breathes a sigh of relief.",
       fr="Je quitte là chambre. Le village dehors paraît de nouveau normal. Les maisons se tiennent droites, le ciel est gris et ordinaire. Graubach pousse un soupir de soulagement.",
       es="Salgo de la cámara. El pueblo afuera se ve normal de nuevo. Las casas están derechas, el cielo es gris y corriente. Graubach respira aliviado.",
       it="Lascio la camera. Il villaggio fuori sembra di nuovo normale. Le case sono diritte, il cielo è grigio è ordinario. Graubach tira un sospiro di sollievo.")

    _t(tr, F, "narration_10",
       en="I will come back. Every year. For the rest of my life. And after that, someone else must take over the pact.",
       fr="Je reviendrai. Chaque année. Pour le reste de mà vie. Et après, quelqu'un d'autre devrà reprendre le pacte.",
       es="Volveré. Cada año. Por el resto de mi vida. Y después, alguien más deberá asumir el pacto.",
       it="Tornerò. Ogni anno. Per il resto della mia vita. È dopo, qualcun altro dovrà ereditare il patto.")

    _t(tr, F, "narration_11",
       en="The tradition lives on. But it has become a different one. No blood, no sacrifice. Only a woman who descends into a cellar once a year and keeps an ancient entity company.",
       fr="Là tradition perdure. Mais elle est devenue autre. Plus de sang, plus de sacrifice. Seulement une femme qui descend dans une cave une fois par an pour tenir compagnie à une entité ancestrale.",
       es="La tradición continúa. Pero se ha convertido en otra cosa. Sin sangre, sin sacrificio. Solo una mujer que baja a un sótano una vez al año y le hace compañía a una entidad ancestral.",
       it="La tradizione sopravvive. Ma è diventata diversa. Niente sangue, niente sacrificio. Solo una donna che scende in una cantina una volta all'anno è fa compagnia a un'entità ancestrale.")

    _t(tr, F, "narration_12",
       en="Sometimes, on quiet nights in Berlin, I hear the singing. Soft, distant, almost like a lullaby. It is no longer threatening. It is... lonely.",
       fr="Parfois, lors de nuits calmes à Berlin, j'entends le chant. Doux, lointain, presque comme une berceuse. Il n'est plus menaçant. Il est... solitaire.",
       es="A veces, en noches tranquilas en Berlín, oigo el canto. Suave, lejano, casi como una nana. Ya no es amenazante. Es... solitario.",
       it="A volte, nelle notti silenziose a Berlino, sento il canto. Sommesso, lontano, quasi come una ninna nanna. Non è più minaccioso. È... solitario.")

    # --- Elise/Creature dialogue during pact ---
    _t(tr, F, "elise_pact_1",
       en="I am not here to bind you. Not to kill you. I propose a bargain.",
       fr="Je ne suis pas là pour te lier. Ni pour te tuer. Je propose un marché.",
       es="No estoy aquí para atarte. Ni para matarte. Propongo un trato.",
       it="Non sono qui per legarti. Non per ucciderti. Propongo un patto.")
    _t(tr, F, "creature_pact_1",
       en="A BARGAIN? HUMANS TRADE IN GOLD AND CATTLE. WHAT DO YOU HAVE THAT I WANT?",
       fr="UN MARCHÉ ? LES HUMAINS TROQUENT L'OR ET LE BÉTAIL. QU'AS-TU QUE JE VEUILLE ?",
       es="¿UN TRATO? LOS HUMANOS COMERCIAN CON ORO Y GANADO. ¿QUÉ TIENES QUE YO QUIERA?",
       it="UN PATTO? GLI UMANI COMMERCIANO IN ORO È BESTIAME. CHE COSA HAI CHE IO VOGLIA?")
    _t(tr, F, "elise_pact_2",
       en="Consciousness. Contact. You do not hunger for blood. You hunger for attention. For someone who is there.",
       fr="Là conscience. Le contact. Tu n'as pas faim de sang. Tu as faim d'attention. De quelqu'un qui soit là.",
       es="Consciencia. Contacto. No tienes hambre de sangre. Tienes hambre de atención. De alguien que esté ahí.",
       it="Coscienza. Contatto. Non hai fame di sangue. Hai fame di attenzione. Di qualcuno che sia presente.")
    _t(tr, F, "creature_pact_2",
       en="Silence. Long silence. Then: HOW DO YOU KNOW THAT?",
       fr="Silence. Un long silence. Puis : COMMENT SAIS-TU CELA ?",
       es="Silencio. Largo silencio. Luego: ¿CÓMO SABES ESO?",
       it="Silenzio. Lungo silenzio. Poi: COME FAI A SAPERLO?")
    _t(tr, F, "elise_pact_3",
       en="My grandmother understood. At the end of her life. She wrote it in her journal. And she summoned me to finish it.",
       fr="Mà grand-mère l'à compris. À là fin de sà vie. Elle l'à écrit dans son journal. Et elle m'à appelée pour achever ce qu'elle avait commencé.",
       es="Mi abuela lo entendió. Al final de su vida. Lo escribió en su diario. Y me llamó para terminarlo.",
       it="Mia nonna lo ha capito. Alla fine della sua vita. Lo ha scritto nel suo diario. È mi ha chiamata per portare a termine il suo lavoro.")
    _t(tr, F, "creature_pact_3",
       en="THE OLD ONE. SHE SPOKE TO ME. AT THE END. WHEN HER LIGHT WAS ALREADY FADING. SHE SAID: MY GRANDDAUGHTER WILL COME.",
       fr="LA VIEILLE. ELLE M'A PARLÉ. À LA FIN. QUAND SA LUMIÈRE FAIBLISSAIT DÉJÀ. ELLE A DIT : MA PETITE-FILLE VIENDRA.",
       es="LA VIEJA. ME HABLÓ. AL FINAL. CUANDO SU LUZ YA SE APAGABA. DIJO: MI NIETA VENDRÁ.",
       it="LA VECCHIA. MI HA PARLATO. ALLA FINE. QUANDO LA SUA LUCE ERA GIÀ DEBOLE. HA DETTO: MIA NIPOTE VERRÀ.")
    _t(tr, F, "elise_pact_4",
       en="And here I am. As she promised.",
       fr="Et me voilà. Comme elle l'à promis.",
       es="Y aquí estoy. Como ella prometió.",
       it="E sono qui. Come lei aveva promesso.")
    _t(tr, F, "creature_pact_4",
       en="HUMANS BREAK PROMISES. YOUR LIVES ARE SHORT. YOU FORGET.",
       fr="LES HUMAINS BRISENT LEURS PROMESSES. VOS VIES SONT COURTES. VOUS OUBLIEZ.",
       es="LOS HUMANOS ROMPEN PROMESAS. SUS VIDAS SON CORTAS. OLVIDAN.",
       it="GLI UMANI ROMPONO LE PROMESSE. LE VOSTRE VITE SONO BREVI. DIMENTICATE.")
    _t(tr, F, "elise_pact_5",
       en="My grandmother kept her promise for thirty years. Every day. Until her death.",
       fr="Mà grand-mère à tenu sà promesse pendant trente ans. Chaque jour. Jusqu'à sà mort.",
       es="Mi abuela mantuvo su promesa durante treinta años. Cada día. Hasta su muerte.",
       it="Mia nonna ha mantenuto la sua promessa per trent'anni. Ogni giorno. Fino alla morte.")
    _t(tr, F, "creature_pact_5",
       en="YES. SHE WAS... DIFFERENT. SHE DID NOT FEED. SHE SPOKE. IN THE LAST YEARS. QUIETLY. I LISTENED.",
       fr="OUI. ELLE ÉTAIT... DIFFÉRENTE. ELLE N'A PAS NOURRI. ELLE A PARLÉ. LES DERNIÈRES ANNÉES. DOUCEMENT. J'AI ÉCOUTÉ.",
       es="SÍ. ELLA ERA... DIFERENTE. NO ALIMENTÓ. HABLÓ. EN LOS ÚLTIMOS AÑOS. EN VOZ BAJA. YO ESCUCHÉ.",
       it="SÌ. LEI ERA... DIVERSA. NON HA NUTRITO. HA PARLATO. NEGLI ULTIMI ANNI. PIANO. IO HO ASCOLTATO.")
    _t(tr, F, "narration_revelation",
       en="My eyes burn. Grandmother spoke with the entity. In the last years, when she fell ill, when no one was looking. She kept it company.",
       fr="Mes yeux brûlent. Grand-mère à parlé avec l'entité. Les dernières années, quand elle est tombée malade, quand personne ne regardait. Elle lui à tenu compagnie.",
       es="Me arden los ojos. La abuela habló con la entidad. En los últimos años, cuando enfermó, cuando nadie miraba. Le hizo compañía.",
       it="Mi bruciano gli occhi. La nonna ha parlato con l'entità. Negli ultimi anni, quando si è ammalata, quando nessuno guardava. Le ha tenuto compagnia.")
    _t(tr, F, "elise_pact_6",
       en="I am her granddaughter. And I keep my promises.",
       fr="Je suis sà petite-fille. Et je tiens mes promesses.",
       es="Soy su nieta. Y cumplo mis promesas.",
       it="Sono sua nipote. È mantengo le mie promesse.")
    _t(tr, F, "creature_pact_6",
       en="I KNOW THAT. THAT IS WHY I AM LISTENING. WHAT DO YOU OFFER?",
       fr="JE LE SAIS. C'EST POUR CELA QUE J'ÉCOUTE. QUE PROPOSES-TU ?",
       es="LO SÉ. POR ESO ESCUCHO. ¿QUÉ OFRECES?",
       it="LO SO. PER QUESTO ASCOLTO. COSA OFFRI?")
    _t(tr, F, "elise_pact_7",
       en="No more sacrifices. No blood. No vessel. Instead, I come. Every year. I sit here and let you touch my thoughts.",
       fr="Plus de sacrifices. Plus de sang. Plus de réceptacle. À là place, je viens. Chaque année. Je m'assieds ici et je te laisse toucher mes pensées.",
       es="No más sacrificios. Sin sangre. Sin receptáculo. En su lugar, yo vengo. Cada año. Me siento aquí y dejo que toques mis pensamientos.",
       it="Niente più sacrifici. Niente sangue. Nessun ricettacolo. Invece, vengo io. Ogni anno. Mi siedo qui è ti lascio toccare i miei pensieri.")
    _t(tr, F, "creature_pact_7",
       en="ONCE A YEAR. THAT IS... LITTLE. FOR SIX HUNDRED YEARS OF HUNGER.",
       fr="UNE FOIS PAR AN. C'EST... PEU. POUR SIX CENTS ANS DE FAIM.",
       es="UNA VEZ AL AÑO. ESO ES... POCO. PARA SEISCIENTOS AÑOS DE HAMBRE.",
       it="UNA VOLTA ALL'ANNO. È... POCO. PER SEICENTO ANNI DI FAME.")
    _t(tr, F, "elise_pact_8",
       en="Once a year is more than thirty years of silence. And I will teach others. After me, others will come. You will never be forgotten again.",
       fr="Une fois par an, c'est plus que trente ans de silence. Et j'enseignerai à d'autres. Après moi, d'autres viendront. Tu ne seras plus jamais oublié.",
       es="Una vez al año es más que treinta años de silencio. Y enseñaré a otros. Después de mí, otros vendrán. Nunca más serás olvidado.",
       it="Una volta all'anno è più di trent'anni di silenzio. È insegnerò ad altri. Dopo di me, altri verranno. Non sarai mai più dimenticato.")
    _t(tr, F, "creature_pact_8",
       en="Silence. I feel it thinking. Weighing. Six hundred years of experience against a promise from a single human lifetime.",
       fr="Silence. Je le sens réfléchir. Peser le pour et le contre. Six cents ans d'expérience contre là promesse d'une seule vie humaine.",
       es="Silencio. Lo siento pensar. Sopesar. Seiscientos años de experiencia contra la promesa de una sola vida humana.",
       it="Silenzio. Lo sento pensare. Soppesare. Seicento anni di esperienza contro la promessa di una singola vita umana.")
    _t(tr, F, "creature_pact_9",
       en="AND WHEN YOU DIE? LIKE YOUR OLD ONE?",
       fr="ET QUAND TU MOURRAS ? COMME TA VIEILLE ?",
       es="¿Y CUANDO MUERAS? ¿COMO TU VIEJA?",
       it="E QUANDO MORIRAI? COME LA TUA VECCHIA?")
    _t(tr, F, "elise_pact_9",
       en="Then someone will come. As I have come. Brandts do not break their promises.",
       fr="Alors quelqu'un viendra. Comme je suis venue. Les Brandt ne brisent pas leurs promesses.",
       es="Entonces alguien vendrá. Como yo vine. Los Brandt no rompen sus promesas.",
       it="Allora qualcuno verrà. Come sono venuta io. I Brandt non rompono le loro promesse.")
    _t(tr, F, "creature_pact_10",
       en="I... ACCEPT. NOT BECAUSE I TRUST YOU. BECAUSE I AM TIRED. AND BECAUSE YOUR OLD ONE TAUGHT ME TRUST.",
       fr="J'... ACCEPTE. PAS PARCE QUE JE TE FAIS CONFIANCE. PARCE QUE JE SUIS FATIGUÉ. ET PARCE QUE TA VIEILLE M'A APPRIS LA CONFIANCE.",
       es="YO... ACEPTO. NO PORQUE CONFÍE EN TI. PORQUE ESTOY CANSADO. Y PORQUE TU VIEJA ME ENSEÑÓ A CONFIAR.",
       it="IO... ACCETTO. NON PERCHÉ MI FIDO DI TE. PERCHÉ SONO STANCO. È PERCHÉ LA TUA VECCHIA MI HA INSEGNATO LA FIDUCIA.")
    _t(tr, F, "narration_5b",
       en="The singing grows quieter. Gentler. Satisfied. The pulsing beneath my feet slows to a calm rhythm. Like a heartbeat coming to rest.",
       fr="Le chant devient plus doux. Plus tendre. Satisfait. Le battement sous mes pieds ralentit en un rythme calme. Comme un cœur qui se repose.",
       es="El canto se vuelve más suave. Más dulce. Satisfecho. El pulso bajo mis pies se ralentiza hasta un ritmo tranquilo. Como un latido que se calma.",
       it="Il canto si fa più sommesso. Più dolce. Soddisfatto. Il pulsare sotto i miei piedi rallenta in un ritmo calmo. Come un battito che si placa.")
    # --- Georg ally branch (pact) ---
    _t(tr, F, "georg_pact_1",
       en="Elise! What happened? The singing stopped, and then...",
       fr="Elise ! Que s'est-il passé ? Le chant s'est arrêté, et puis...",
       es="¡Elise! ¿Qué pasó? El canto se detuvo, y luego...",
       it="Elise! Che è successo? Il canto si è fermato, è poi...")
    _t(tr, F, "elise_georg_pact",
       en="It is over, Georg. No more sacrifices. I have made a pact. A fair one.",
       fr="C'est fini, Georg. Plus de sacrifices. J'ai conclu un pacte. Un pacte juste.",
       es="Se acabó, Georg. No más sacrificios. Hice un pacto. Uno justo.",
       it="È finita, Georg. Niente più sacrifici. Ho stretto un patto. Uno giusto.")
    _t(tr, F, "georg_pact_2",
       en="A pact... Margarethe would have wanted that. Peace instead of war.",
       fr="Un pacte... Margarethe aurait voulu ça. Là paix au lieu de là guerre.",
       es="Un pacto... Margarethe habría querido eso. Paz en lugar de guerra.",
       it="Un patto... Margarethe lo avrebbe voluto. Pace invece di guerra.")
    # --- Hilde ally branch (pact) ---
    _t(tr, F, "hilde_pact_1",
       en="I feel the connection. A thread. Thin, but strong. What have you done, child?",
       fr="Je sens là connexion. Un fil. Fin, mais solide. Qu'as-tu fait, mon enfant ?",
       es="Siento la conexión. Un hilo. Delgado, pero fuerte. ¿Qué has hecho, niña?",
       it="Sento la connessione. Un filo. Sottile, ma forte. Che hai fatto, bambina?")
    _t(tr, F, "elise_hilde_pact",
       en="Negotiated. As Grandmother would have wanted in the end. No more blood. Only company.",
       fr="Négocié. Comme grand-mère l'aurait voulu à là fin. Plus de sang. Seulement de là compagnie.",
       es="Negocié. Como la abuela habría querido al final. No más sangre. Solo compañía.",
       it="Negoziato. Come la nonna avrebbe voluto alla fine. Niente più sangue. Solo compagnia.")
    _t(tr, F, "hilde_pact_2",
       en="Company. So simple. And so difficult.",
       fr="De là compagnie. Si simple. Et si difficile.",
       es="Compañía. Tan simple. Y tan difícil.",
       it="Compagnia. Così semplice. È così difficile.")
    # --- Voss ally branch (pact) ---
    _t(tr, F, "voss_pact_1",
       en="What did I miss? What happened down there?",
       fr="Qu'ai-je manqué ? Que s'est-il passé là-bas ?",
       es="¿Qué me perdí? ¿Qué pasó allá abajo?",
       it="Che cosa mi sono perso? Che è successo laggiù?")
    _t(tr, F, "elise_voss_pact",
       en="Peace, Pastor. For the first time in six hundred years. No more sacrifice. No blood. Only a promise.",
       fr="Là paix, Pasteur. Pour là première fois en six cents ans. Plus de sacrifice. Plus de sang. Seulement une promesse.",
       es="Paz, Pastor. Por primera vez en seiscientos años. No más sacrificios. Sin sangre. Solo una promesa.",
       it="Pace, Pastore. Per la prima volta in seicento anni. Nessun altro sacrificio. Niente sangue. Solo una promessa.")
    _t(tr, F, "voss_pact_2",
       en="A promise... Thank God. Or whoever we should thank.",
       fr="Une promesse... Dieu merci. Ou qui que ce soit que nous devions remercier.",
       es="Una promesa... Gracias a Dios. O a quien sea que debamos agradecer.",
       it="Una promessa... Grazie a Dio. O a chiunque dovremmo ringraziare.")
    _t(tr, F, "narration_13",
       en="Grandmother, you left it to me. Not as a burden. As an inheritance. And I accept it.",
       fr="Grand-mère, tu me l'as laissé. Non comme un fardeau. Comme un héritage. Et je l'accepte.",
       es="Abuela, me lo dejaste. No como una carga. Como una herencia. Y la acepto.",
       it="Nonna, me lo hai lasciato. Non come un fardello. Come un'eredità. È la accetto.")
    _t(tr, F, "journal_pact",
       en="The Pact",
       fr="Le Pacte",
       es="El pacto",
       it="Il patto",
       field="title")
    _t(tr, F, "journal_pact",
       en="No blood. No sacrifice. No vessel. Only a promise: every year I will return and keep the entity company. It accepted. Grandmother paved the way. I will see it through.",
       fr="Pas de sang. Pas de sacrifice. Pas de réceptacle. Seulement une promesse : chaque année, je reviendrai tenir compagnie à l'entité. Elle à accepté. Grand-mère à ouvert là voie. Je là suivrai jusqu'au bout.",
       es="Sin sangre. Sin sacrificio. Sin receptáculo. Solo una promesa: cada año volveré y le haré compañía a la entidad. Aceptó. La abuela allanó el camino. Yo lo recorreré hasta el final.",
       it="Niente sangue. Niente sacrificio. Nessun ricettacolo. Solo una promessa: ogni anno tornerò è farò compagnia all'entità. Ha accettato. La nonna ha aperto la strada. Io la percorrerò fino in fondo.",
       field="content")


def _add_act4_ending_truth(tr):
    F = "res://data/dialogue/act4/ending_truth.json"

    _t(tr, F, "narration_1",
       en="I open my mind. Not to bind, not to destroy. To understand. Grandmother's journal taught me that knowledge is the strongest weapon.",
       fr="J'ouvre mon esprit. Non pour lier, non pour détruire. Pour comprendre. Le journal de grand-mère m'à appris que le savoir est l'arme là plus puissante.",
       es="Abro mi mente. No para atar, no para destruir. Para comprender. El diario de la abuela me enseñó que el conocimiento es el arma más poderosa.",
       it="Apro la mia mente. Non per legare, non per distruggere. Per comprendere. Il diario della nonna mi ha insegnato che la conoscenza è l'arma più potente.")

    _t(tr, F, "narration_2",
       en="The entity senses my intention. It hesitates. Then, like a door opening after centuries, it shows me everything.",
       fr="L'entité perçoit mon intention. Elle hésite. Puis, comme une porte qui s'ouvre après des siècles, elle me montre tout.",
       es="La entidad percibe mi intención. Duda. Luego, como una puerta que se abre después de siglos, me lo muestra todo.",
       it="L'entità percepisce la mia intenzione. Esita. Poi, come una porta che si apre dopo secoli, mi mostra tutto.")

    _t(tr, F, "narration_3",
       en="Images. Thousands of images. The earth as it was before humans set foot on it. Things that live beneath the surface, older than stone, older than water.",
       fr="Des images. Des milliers d'images. Là terre telle qu'elle était avant que les humains n'y posent le pied. Des choses qui vivent sous là surface, plus anciennes que là pierre, plus anciennes que l'eau.",
       es="Imágenes. Miles de imágenes. La tierra como era antes de que los humanos la pisaran. Cosas que viven bajo la superficie, más antiguas que la piedra, más antiguas que el agua.",
       it="Immagini. Migliaia di immagini. La terrà com'era prima che gli esseri umani vi mettessero piede. Cose che vivono sotto la superficie, più antiche della pietra, più antiche dell'acqua.")

    _t(tr, F, "narration_4",
       en="Graubach is not unique. There are hundreds of such places. Thin places, where the boundary between above and below, between our world and what lies beneath, barely exists.",
       fr="Graubach n'est pas unique. Il existe des centaines d'endroits semblables. Des lieux ténus, où là frontière entre le dessus et le dessous, entre notre monde et ce qui gît en dessous, existe à peine.",
       es="Graubach no es único. Hay cientos de lugares así. Lugares delgados, donde el límite entre arriba y abajo, entre nuestro mundo y lo que yace debajo, apenas existe.",
       it="Graubach non è unica. Ci sono centinaia di luoghi simili. Luoghi sottili, dove il confine tra sopra è sotto, tra il nostro mondo è ciò che giace al di sotto, quasi non esiste.")

    _t(tr, F, "narration_5",
       en="Beneath the Black Forest. Beneath the Alps. Beneath the seas. Everywhere. A world beneath the world, full of entities like this one — and older, larger, other ones.",
       fr="Sous là Forêt-Noire. Sous les Alpes. Sous les mers. Partout. Un monde sous le monde, rempli d'entités comme celle-ci — et de plus anciennes, de plus grandes, d'autres.",
       es="Bajo la Selva Negra. Bajo los Alpes. Bajo los mares. En todas partes. Un mundo bajo el mundo, lleno de entidades como esta — y de otras más antiguas, más grandes, diferentes.",
       it="Sotto la Foresta Nera. Sotto le Alpi. Sotto i mari. Ovunque. Un mondo sotto il mondo, pieno di entità come questa — è di altre più antiche, più grandi, diverse.")

    _t(tr, F, "narration_7",
       en="The entity beneath Graubach is small. A child, compared to what sleeps in the depths of the ocean. It is not our enemy. It is a neighbor who lives too close.",
       fr="L'entité sous Graubach est petite. Un enfant, comparé à ce qui dort dans les profondeurs de l'océan. Ce n'est pas notre ennemi. C'est un voisin qui vit trop près.",
       es="La entidad bajo Graubach es pequeña. Un niño, comparada con lo que duerme en las profundidades del océano. No es nuestro enemigo. Es un vecino que vive demasiado cerca.",
       it="L'entità sotto Graubach è piccola. Una bambina, rispetto a ciò che dorme nelle profondità dell'oceano. Non è il nostro nemico. È un vicino che vive troppo vicino.")

    _t(tr, F, "narration_8",
       en="And the heaviest realization: we never had the choice to fight them. We can only learn to exist alongside them.",
       fr="Et là révélation là plus lourde : nous n'avons jamais eu le choix de les combattre. Nous ne pouvons qu'apprendre à exister à côté d'eux.",
       es="Y la revelación más pesada: nunca tuvimos la opción de combatirlos. Solo podemos aprender a existir junto a ellos.",
       it="E la consapevolezza più pesante: non abbiamo mai avuto la possibilità di combatterli. Possiamo solo imparare a esistere accanto a loro.")

    _t(tr, F, "narration_9",
       en="The entity withdraws. Satisfied. For the first time in centuries, someone has looked at it without running away. It falls asleep — not by force, but in peace.",
       fr="L'entité se retire. Satisfaite. Pour là première fois en des siècles, quelqu'un l'à regardée sans fuir. Elle s'endort — non par contrainte, mais en paix.",
       es="La entidad se retira. Satisfecha. Por primera vez en siglos, alguien la ha mirado sin huir. Se duerme — no por la fuerza, sino en paz.",
       it="L'entità si ritira. Soddisfatta. Per la prima volta in secoli, qualcuno l'ha guardata senza fuggire. Si addormenta — non per costrizione, ma in pace.")

    _t(tr, F, "anna_truth_1",
       en="Anna Voss stands at the entrance of the chamber. Her eyes are clear — clearer than I have ever seen them.",
       fr="Annà Voss se tient à l'entrée de là chambre. Ses yeux sont clairs — plus clairs que je ne les ai jamais vus.",
       es="Anna Voss está de pie en la entrada de la cámara. Sus ojos están claros — más claros de lo que los he visto jamás.",
       it="Anna Voss è in piedi all'ingresso della camera. I suoi occhi sono limpidi — più limpidi di quanto li abbia mai visti.")

    _t(tr, F, "anna_truth_2",
       en="You understood, Elise. I always sensed it — the images, the spirals. But you put it into words. The silence is... different now. Lighter.",
       fr="Tu as compris, Elise. Je l'ai toujours senti — les images, les spirales. Mais toi, tu l'as mis en mots. Le silence est... différent maintenant. Plus léger.",
       es="Lo entendiste, Elise. Yo siempre lo sentí — las imágenes, las espirales. Pero tú lo pusiste en palabras. El silencio es... diferente ahora. Más ligero.",
       it="Hai capito, Elise. Io l'ho sempre sentito — le immagini, le spirali. Ma tu l'hai messo in parole. Il silenzio è... diverso adesso. Più leggero.")

    _t(tr, F, "anna_truth_3",
       en="For the first time, I see Anna smile. Truly smile. The entity has let her go — or she has let it go.",
       fr="Pour là première fois, je vois Annà sourire. Vraiment sourire. L'entité l'à libérée — où elle l'à libérée.",
       es="Por primera vez veo a Anna sonreír. Sonreír de verdad. La entidad la ha dejado ir — o ella la ha dejado ir.",
       it="Per la prima volta vedo Anna sorridere. Davvero sorridere. L'entità l'ha lasciata andare — o lei ha lasciato andare l'entità.")

    _t(tr, F, "letter_resolution_truth",
       en="In the light of understanding, I finally grasp Grandmother's letter. She did not write a warning — she wrote an invitation. 'Come and see.' She knew I would be the first to look without running away.",
       fr="À là lumière de là compréhension, je saisis enfin là lettre de grand-mère. Elle n'à pas écrit un avertissement — elle à écrit une invitation. « Viens et regarde. » Elle savait que je serais là première à regarder sans fuir.",
       es="A la luz de la comprensión, por fin entiendo la carta de la abuela. No escribió una advertencia — escribió una invitación. «Ven y mira.» Sabía que yo sería la primera en mirar sin huir.",
       it="Alla luce della comprensione, finalmente afferro la lettera della nonna. Non scrisse un avvertimento — scrisse un invito. «Vieni è guarda.» Sapeva che sarei stata la prima a guardare senza fuggire.")

    _t(tr, F, "narration_10",
       en="I stand up and climb into the light. But the world looks different. I feel the thin places — everywhere. Beneath my feet, in the distance, on the horizon.",
       fr="Je me lève et monte vers là lumière. Mais le monde à changé d'aspect. Je sens les lieux ténus — partout. Sous mes pieds, au loin, à l'horizon.",
       es="Me pongo de pie y subo hacia la luz. Pero el mundo se ve diferente. Siento los lugares delgados — en todas partes. Bajo mis pies, a lo lejos, en el horizonte.",
       it="Mi alzo è salgo verso la luce. Ma il mondo appare diverso. Sento i luoghi sottili — ovunque. Sotto i miei piedi, in lontananza, all'orizzonte.")

    _t(tr, F, "narration_11",
       en="I will never be ignorant again. That is the price of truth.",
       fr="Je ne serai plus jamais dans l'ignorance. C'est le prix de là vérité.",
       es="Nunca volveré a ser ignorante. Ese es el precio de la verdad.",
       it="Non sarò mai più nell'ignoranza. Questo è il prezzo della verità.")

    _t(tr, F, "narration_12",
       en="The world is larger than we thought. Deeper. Older. And beneath every city, beneath every forest, beneath every ocean, something sleeps that we do not understand. Not yet.",
       fr="Le monde est plus vaste que nous le pensions. Plus profond. Plus ancien. Et sous chaque ville, sous chaque forêt, sous chaque océan, dort quelque chose que nous ne comprenons pas. Pas encore.",
       es="El mundo es más grande de lo que pensábamos. Más profundo. Más antiguo. Y bajo cada ciudad, bajo cada bosque, bajo cada océano, duerme algo que no comprendemos. Aún no.",
       it="Il mondo è più grande di quanto pensassimo. Più profondo. Più antico. È sotto ogni città, sotto ogni foresta, sotto ogni oceano, dorme qualcosa che non comprendiamo. Non ancora.")

    _t(tr, F, "narration_13",
       en="But I am the first to try.",
       fr="Mais je suis là première à essayer.",
       es="Pero soy la primera en intentarlo.",
       it="Ma sono la prima a provarci.")

    # --- Elise/Creature dialogue during truth ---
    _t(tr, F, "elise_truth_1",
       en="I am not here to fight. I am here to listen. Show me what you are.",
       fr="Je ne suis pas là pour combattre. Je suis là pour écouter. Montre-moi ce que tu es.",
       es="No estoy aquí para pelear. Estoy aquí para escuchar. Muéstrame lo que eres.",
       it="Non sono qui per combattere. Sono qui per ascoltare. Mostrami cosa sei.")
    _t(tr, F, "narration_creature_hears",
       en="Silence. Then, like a breath held for six hundred years:",
       fr="Silence. Puis, comme un souffle retenu pendant six cents ans :",
       es="Silencio. Luego, como un aliento contenido durante seiscientos años:",
       it="Silenzio. Poi, come un respiro trattenuto per seicento anni:")
    _t(tr, F, "creature_truth_1",
       en="YOU WANT TO SEE? TRULY SEE? THE LAST ONE WHO WANTED THAT WAS THREE HUNDRED YEARS AGO. SHE WENT MAD.",
       fr="TU VEUX VOIR ? VRAIMENT VOIR ? LA DERNIÈRE QUI L'A VOULU, C'ÉTAIT IL Y A TROIS CENTS ANS. ELLE EST DEVENUE FOLLE.",
       es="¿QUIERES VER? ¿VER DE VERDAD? LA ÚLTIMA QUE QUISO ESO FUE HACE TRESCIENTOS AÑOS. ENLOQUECIÓ.",
       it="VUOI VEDERE? DAVVERO VEDERE? L'ULTIMA CHE LO HA VOLUTO È STATA TRECENTO ANNI FA. È IMPAZZITA.")
    _t(tr, F, "elise_truth_2",
       en="I am a folklorist. I study the unknown. Show me.",
       fr="Je suis folkloriste. J'étudie l'inconnu. Montre-moi.",
       es="Soy folclorista. Estudio lo desconocido. Muéstramelo.",
       it="Sono una folclorista. Studio l'ignoto. Mostrami.")
    _t(tr, F, "creature_truth_2",
       en="SIX HUNDRED YEARS AND NO ONE HAS WANTED THIS. YOUR OLD ONE... SHE ASKED. BUT SHE WAS TOO TIRED IN THE END. TOO SICK. I HAVE... WAITED.",
       fr="SIX CENTS ANS ET PERSONNE N'A VOULU CELA. TA VIEILLE... ELLE A DEMANDÉ. MAIS ELLE ÉTAIT TROP FATIGUÉE À LA FIN. TROP MALADE. J'AI... ATTENDU.",
       es="SEISCIENTOS AÑOS Y NADIE HA QUERIDO ESTO. TU VIEJA... ELLA PREGUNTÓ. PERO ESTABA DEMASIADO CANSADA AL FINAL. DEMASIADO ENFERMA. YO HE... ESPERADO.",
       it="SEICENTO ANNI È NESSUNO LO HA VOLUTO. LA TUA VECCHIA... LEI HA CHIESTO. MA ERA TROPPO STANCA ALLA FINE. TROPPO MALATA. IO HO... ASPETTATO.")
    _t(tr, F, "elise_truth_3",
       en="That... that is the Earth? Before humans? It is... beautiful. And terrifying.",
       fr="Ça... c'est là Terre ? Avant les humains ? C'est... magnifique. Et terrifiant.",
       es="Eso... ¿eso es la Tierra? ¿Antes de los humanos? Es... hermoso. Y aterrador.",
       it="Quella... quella è la Terra? Prima degli umani? È... meravigliosa. È terrificante.")
    _t(tr, F, "creature_truth_3",
       en="WE WERE HERE BEFORE YOU. BEFORE YOUR TREES. BEFORE YOUR SKY. YOUR WORLD IS A THIN FILM UPON OURS.",
       fr="NOUS ÉTIONS LÀ AVANT VOUS. AVANT VOS ARBRES. AVANT VOTRE CIEL. VOTRE MONDE EST UN MINCE FILM SUR LE NÔTRE.",
       es="ESTUVIMOS AQUÍ ANTES QUE USTEDES. ANTES QUE SUS ÁRBOLES. ANTES QUE SU CIELO. SU MUNDO ES UNA DELGADA PELÍCULA SOBRE EL NUESTRO.",
       it="ERAVAMO QUI PRIMA DI VOI. PRIMA DEI VOSTRI ALBERI. PRIMA DEL VOSTRO CIELO. IL VOSTRO MONDO È UN SOTTILE FILM SUL NOSTRO.")
    _t(tr, F, "elise_truth_4",
       en="How many... how many are you?",
       fr="Combien... combien êtes-vous ?",
       es="Cuántos... ¿cuántos son?",
       it="Quanti... quanti siete?")
    _t(tr, F, "creature_truth_4",
       en="MORE THAN YOUR STARS. FEWER THAN YOUR THOUGHTS. WE DO NOT COUNT. WE ARE.",
       fr="PLUS QUE VOS ÉTOILES. MOINS QUE VOS PENSÉES. NOUS NE COMPTONS PAS. NOUS SOMMES.",
       es="MÁS QUE SUS ESTRELLAS. MENOS QUE SUS PENSAMIENTOS. NO CONTAMOS. SOMOS.",
       it="PIÙ DELLE VOSTRE STELLE. MENO DEI VOSTRI PENSIERI. NON CONTIAMO. SIAMO.")
    _t(tr, F, "narration_tears",
       en="I weep. Not from fear. From awe. From the incomprehensible vastness of what I see. My mind is a teaspoon trying to hold an ocean.",
       fr="Je pleure. Pas de peur. De respect. De l'immensité incompréhensible de ce que je vois. Mon esprit est une cuillère à café essayant de contenir un océan.",
       es="Lloro. No de miedo. De asombro. De la inmensidad incomprensible de lo que veo. Mi mente es una cucharadita intentando contener un océano.",
       it="Piango. Non di paura. Di meraviglia. Dell'incomprensibile vastità di ciò che vedo. La mia mente è un cucchiaino che tenta di contenere un oceano.")
    _t(tr, F, "elise_truth_5",
       en="You are... alone here. For six hundred years alone. Cut off from the others.",
       fr="Tu es... seul ici. Depuis six cents ans, seul. Coupé des autres.",
       es="Estás... solo aquí. Desde hace seiscientos años solo. Separado de los demás.",
       it="Sei... solo qui. Da seicento anni solo. Tagliato fuori dagli altri.")
    _t(tr, F, "creature_truth_5",
       en="THE THIN PLACE HAS TRAPPED ME. I AM TOO CLOSE TO YOUR WORLD. TOO FAR FROM MINE. I CANNOT GO BACK. I CANNOT GO FORWARD. I AM... IN BETWEEN.",
       fr="LE LIEU MINCE M'A PIÉGÉ. JE SUIS TROP PRÈS DE VOTRE MONDE. TROP LOIN DU MIEN. JE NE PEUX PAS REVENIR. JE NE PEUX PAS AVANCER. JE SUIS... ENTRE LES DEUX.",
       es="EL LUGAR DELGADO ME HA ATRAPADO. ESTOY DEMASIADO CERCA DE SU MUNDO. DEMASIADO LEJOS DEL MÍO. NO PUEDO VOLVER. NO PUEDO AVANZAR. ESTOY... EN MEDIO.",
       it="IL LUOGO SOTTILE MI HA INTRAPPOLATO. SONO TROPPO VICINO AL VOSTRO MONDO. TROPPO LONTANO DAL MIO. NON POSSO TORNARE INDIETRO. NON POSSO ANDARE AVANTI. SONO... IN MEZZO.")
    _t(tr, F, "elise_truth_6",
       en="That is why the hunger. That is why the sacrifices. You need contact with conscious life because you are cut off from your own kind.",
       fr="C'est pour çà là faim. C'est pour çà les sacrifices. Tu as besoin de contact avec là vie consciente parce que tu es coupé des tiens.",
       es="Por eso el hambre. Por eso los sacrificios. Necesitas contacto con vida consciente porque estás aislado de los tuyos.",
       it="Per questo la fame. Per questo i sacrifici. Hai bisogno di contatto con vita cosciente perché sei tagliato fuori dai tuoi simili.")
    _t(tr, F, "creature_truth_6",
       en="YES. HUNGER IS NOT THE WORD FOR IT. IT IS LIKE... WHEN YOUR EYES CAN NO LONGER SEE LIGHT. WHEN YOUR EARS CAN NO LONGER HEAR VOICES. ONLY SILENCE. SIX HUNDRED YEARS OF SILENCE.",
       fr="OUI. FAIM N'EST PAS LE MOT. C'EST COMME... QUAND VOS YEUX NE VOIENT PLUS LA LUMIÈRE. QUAND VOS OREILLES N'ENTENDENT PLUS DE VOIX. RIEN QUE LE SILENCE. SIX CENTS ANS DE SILENCE.",
       es="SÍ. HAMBRE NO ES LA PALABRA. ES COMO... CUANDO SUS OJOS YA NO VEN LA LUZ. CUANDO SUS OÍDOS YA NO OYEN VOCES. SOLO SILENCIO. SEISCIENTOS AÑOS DE SILENCIO.",
       it="SÌ. FAME NON È LA PAROLA GIUSTA. È COME... QUANDO I VOSTRI OCCHI NON VEDONO PIÙ LA LUCE. QUANDO LE VOSTRE ORECCHIE NON SENTONO PIÙ VOCI. SOLO SILENZIO. SEICENTO ANNI DI SILENZIO.")
    _t(tr, F, "elise_truth_7",
       en="I understand now. The sacrifices were never necessary. The tradition was an answer to a question that no one asked properly.",
       fr="Je comprends maintenant. Les sacrifices n'ont jamais été nécessaires. Là tradition était une réponse à une question que personne n'à posée correctement.",
       es="Ahora lo entiendo. Los sacrificios nunca fueron necesarios. La tradición era una respuesta a una pregunta que nadie formuló correctamente.",
       it="Ora capisco. I sacrifici non sono mai stati necessari. La tradizione era una risposta a una domanda che nessuno ha posto correttamente.")
    _t(tr, F, "creature_truth_7",
       en="YOUR OLD ONE ASKED THE QUESTION. AT THE END. WHEN IT WAS TOO LATE. SHE WEPT. I DID... NOT UNDERSTAND WHY.",
       fr="TA VIEILLE A POSÉ LA QUESTION. À LA FIN. QUAND IL ÉTAIT TROP TARD. ELLE A PLEURÉ. JE N'AI... PAS COMPRIS POURQUOI.",
       es="TU VIEJA HIZO LA PREGUNTA. AL FINAL. CUANDO ERA DEMASIADO TARDE. LLORÓ. YO NO... ENTENDÍ POR QUÉ.",
       it="LA TUA VECCHIA HA POSTO LA DOMANDA. ALLA FINE. QUANDO ERA TROPPO TARDI. HA PIANTO. IO NON... HO CAPITO PERCHÉ.")
    _t(tr, F, "narration_grandma",
       en="Grandmother. She knew. At the end of her life, she understood what I now understand. And she summoned me to finish it.",
       fr="Grand-mère. Elle savait. À là fin de sà vie, elle à compris ce que je comprends maintenant. Et elle m'à appelée pour achever ce qu'elle avait commencé.",
       es="La abuela. Ella lo sabía. Al final de su vida, entendió lo que yo ahora entiendo. Y me llamó para terminarlo.",
       it="La nonna. Lo sapeva. Alla fine della sua vita, ha capito quello che ora capisco io. È mi ha chiamata per portare a termine il suo lavoro.")
    _t(tr, F, "elise_truth_8",
       en="She wept because she understood you. Because thirty years of sacrifice were unnecessary. Because she could have seen it sooner.",
       fr="Elle à pleuré parce qu'elle t'à compris. Parce que trente ans de sacrifices étaient inutiles. Parce qu'elle aurait pu le voir plus tôt.",
       es="Lloró porque te entendió. Porque treinta años de sacrificios fueron innecesarios. Porque podría haberlo visto antes.",
       it="Ha pianto perché ti ha capito. Perché trent'anni di sacrifici erano inutili. Perché avrebbe potuto vederlo prima.")
    _t(tr, F, "creature_truth_8",
       en="YOU WEEP TOO. WHY?",
       fr="TU PLEURES AUSSI. POURQUOI ?",
       es="TÚ TAMBIÉN LLORAS. ¿POR QUÉ?",
       it="ANCHE TU PIANGI. PERCHÉ?")
    _t(tr, F, "elise_truth_9",
       en="Because you have been alone for six hundred years. And no one asked how you were.",
       fr="Parce que tu es seul depuis six cents ans. Et personne ne t'à demandé comment tu allais.",
       es="Porque has estado solo durante seiscientos años. Y nadie te preguntó cómo estabas.",
       it="Perché sei stato solo per seicento anni. È nessuno ti ha chiesto come stavi.")
    _t(tr, F, "creature_truth_final",
       en="Silence. Long silence. Then, quieter than ever before: THANK YOU.",
       fr="Silence. Un long silence. Puis, plus doucement que jamais : MERCI.",
       es="Silencio. Largo silencio. Luego, más bajo que nunca: GRACIAS.",
       it="Silenzio. Lungo silenzio. Poi, più sommesso che mai: GRAZIE.")
    _t(tr, F, "narration_9b",
       en="But before it goes, I feel something. Like a hand touching mine. A gesture that no human word describes. Farewell? Gratitude? Hope of reunion?",
       fr="Mais avant de partir, je sens quelque chose. Comme une main qui touche là mienne. Un geste qu'aucun mot humain ne décrit. Adieu ? Gratitude ? Espoir de retrouvailles ?",
       es="Pero antes de irse, siento algo. Como una mano que toca la mía. Un gesto que ninguna palabra humana describe. ¿Despedida? ¿Gratitud? ¿Esperanza de reencuentro?",
       it="Ma prima che se ne vada, sento qualcosa. Come una mano che tocca la mia. Un gesto che nessuna parola umana descrive. Addio? Gratitudine? Speranza di rivedersi?")
    # --- Georg ally branch (truth) ---
    _t(tr, F, "georg_truth_1",
       en="Elise? Your face... you are crying. What happened down there?",
       fr="Elise ? Ton visage... tu pleures. Que s'est-il passé là-bas ?",
       es="¿Elise? Tu rostro... estás llorando. ¿Qué pasó allá abajo?",
       it="Elise? Il tuo volto... stai piangendo. Che è successo laggiù?")
    _t(tr, F, "elise_georg_truth",
       en="I understood it, Georg. It is not evil. It was never evil. It is just... alone.",
       fr="Je l'ai compris, Georg. Ce n'est pas maléfique. Çà ne l'à jamais été. C'est juste... seul.",
       es="Lo entendí, Georg. No es malvado. Nunca fue malvado. Solo está... solo.",
       it="L'ho capito, Georg. Non è malvagio. Non lo è mai stato. È solo... solo.")
    _t(tr, F, "georg_truth_2",
       en="Thirty years. For thirty years we fed it as if it needed blood. And all it wanted...",
       fr="Trente ans. Pendant trente ans, nous l'avons nourri comme s'il avait besoin de sang. Et tout ce qu'il voulait...",
       es="Treinta años. Durante treinta años lo alimentamos como si necesitara sangre. Y todo lo que quería...",
       it="Trent'anni. Per trent'anni lo abbiamo nutrito come se avesse bisogno di sangue. È tutto ciò che voleva...")
    _t(tr, F, "elise_georg_truth_2",
       en="Was company. Yes. Grandmother understood in the end. Now we understand too.",
       fr="C'était de là compagnie. Oui. Grand-mère l'à compris à là fin. Maintenant nous le comprenons aussi.",
       es="Era compañía. Sí. La abuela lo entendió al final. Ahora lo entendemos nosotros también.",
       it="Era compagnia. Sì. La nonna lo ha capito alla fine. Ora lo capiamo anche noi.")
    # --- Hilde ally branch (truth) ---
    _t(tr, F, "hilde_truth_1",
       en="I feel it. The air is different. What have you done?",
       fr="Je le sens. L'air est différent. Qu'as-tu fait ?",
       es="Lo siento. El aire es diferente. ¿Qué has hecho?",
       it="Lo sento. L'aria è diversa. Che hai fatto?")
    _t(tr, F, "elise_hilde_truth",
       en="Listened. Nothing more. It showed me its story. Hilde... the entire tradition was a misunderstanding.",
       fr="Écouté. Rien de plus. Il m'à montré son histoire. Hilde... toute là tradition était un malentendu.",
       es="Escuché. Nada más. Me mostró su historia. Hilde... toda la tradición era un malentendido.",
       it="Ascoltato. Niente di più. Mi ha mostrato la sua storia. Hilde... l'intera tradizione era un malinteso.")
    _t(tr, F, "hilde_truth_2",
       en="Margarethe suspected that in the end. She said: 'It does not need nourishment. It needs a voice.'",
       fr="Margarethe l'à soupçonné à là fin. Elle disait : « Il n'à pas besoin de nourriture. Il à besoin d'une voix. »",
       es="Margarethe sospechó eso al final. Decía: «No necesita alimento. Necesita una voz.»",
       it="Margarethe lo sospettava alla fine. Diceva: «Non ha bisogno di nutrimento. Ha bisogno di una voce.»")
    # --- Voss ally branch (truth) ---
    _t(tr, F, "voss_truth_1",
       en="The singing has stopped. Is it... is it dead?",
       fr="Le chant s'est arrêté. Est-il... est-il mort ?",
       es="El canto se ha detenido. ¿Está... está muerto?",
       it="Il canto si è fermato. È... è morto?")
    _t(tr, F, "elise_voss_truth",
       en="It sleeps. Content. Pastor Voss... it was never a demon. It was a being that was alone. Six hundred years alone.",
       fr="Il dort. Satisfait. Pasteur Voss... ce n'à jamais été un démon. C'était un être qui était seul. Six cents ans de solitude.",
       es="Duerme. Satisfecho. Pastor Voss... nunca fue un demonio. Era un ser que estaba solo. Seiscientos años solo.",
       it="Dorme. Soddisfatto. Pastore Voss... non è mai stato un demone. Era un essere che era solo. Seicento anni da solo.")
    _t(tr, F, "voss_truth_2",
       en="No demon? Then everything... the sacrifices... Friedrich...",
       fr="Pas un démon ? Alors tout... les sacrifices... Friedrich...",
       es="¿No es un demonio? Entonces todo... los sacrificios... Friedrich...",
       it="Nessun demone? Allora tutto... i sacrifici... Friedrich...")
    _t(tr, F, "elise_voss_truth_2",
       en="Yes. It was all unnecessary. But we did not know. No one knew.",
       fr="Oui. Tout était inutile. Mais nous ne le savions pas. Personne ne le savait.",
       es="Sí. Todo fue innecesario. Pero no lo sabíamos. Nadie lo sabía.",
       it="Sì. Era tutto inutile. Ma non lo sapevamo. Nessuno lo sapeva.")
    # --- Anna scene (truth) ---
    _t(tr, F, "elise_anna_truth",
       en="You always felt it, did you not? The spirals, the images. You tried to show us.",
       fr="Tu l'as toujours senti, n'est-ce pas ? Les spirales, les images. Tu as essayé de nous montrer.",
       es="Siempre lo sentiste, ¿verdad? Las espirales, las imágenes. Intentaste mostrárnoslo.",
       it="L'hai sempre sentito, vero? Le spirali, le immagini. Hai cercato di mostrarcelo.")
    _t(tr, F, "journal_truth",
       en="The Truth",
       fr="Là Vérité",
       es="La verdad",
       it="La verità",
       field="title")
    _t(tr, F, "journal_truth",
       en="The entity is not our enemy. It is a neighbor, trapped between worlds, six hundred years alone. The sacrifices were never necessary. It only needed someone to listen. I am the first who listened.",
       fr="L'entité n'est pas notre ennemi. C'est un voisin, piégé entre les mondes, six cents ans de solitude. Les sacrifices n'ont jamais été nécessaires. Il avait juste besoin de quelqu'un pour l'écouter. Je suis là première à avoir écouté.",
       es="La entidad no es nuestro enemigo. Es un vecino, atrapado entre mundos, seiscientos años solo. Los sacrificios nunca fueron necesarios. Solo necesitaba a alguien que escuchara. Soy la primera que escuchó.",
       it="L'entità non è il nostro nemico. È un vicino, intrappolato tra i mondi, seicento anni da solo. I sacrifici non sono mai stati necessari. Aveva solo bisogno di qualcuno che ascoltasse. Sono la prima che ha ascoltato.",
       field="content")


def _add_act4_ending_sacrifice(tr):
    F = "res://data/dialogue/act4/ending_sacrifice.json"

    _t(tr, F, "narration_1",
       en="I look at Konrad. He is trembling. Beads of sweat on his forehead. Behind his eyes, a man fights against an ocean.",
       fr="Je regarde Konrad. Il tremble. Des gouttes de sueur sur son front. Derrière ses yeux, un homme lutte contre un océan.",
       es="Miro a Konrad. Está temblando. Gotas de sudor en su frente. Detrás de sus ojos, un hombre lucha contra un océano.",
       it="Guardo Konrad. Trema. Gocce di sudore sulla sua fronte. Dietro i suoi occhi, un uomo lotta contro un oceano.")

    _t(tr, F, "narration_2",
       en="He taught me to read — no, that was Grandmother. He showed me the guardian tree. He asked for help when no one else did.",
       fr="C'est lui qui m'à appris à lire — non, c'était grand-mère. Il m'à montré l'arbre du gardien. Il à demandé de l'aide quand personne d'autre ne l'à fait.",
       es="Él me enseñó a leer — no, eso fue la abuela. Me mostró el árbol del guardián. Pidió ayuda cuando nadie más lo hizo.",
       it="Mi ha insegnato a leggere — no, quella era la nonna. Mi ha mostrato l'albero del guardiano. Ha chiesto aiuto quando nessun altro lo ha fatto.")

    _t(tr, F, "narration_3",
       en="And I read in Grandmother's journal what the vessel is: a bridge. The entity needs a human mind as an anchor in our world. Without a vessel, it cannot stay here.",
       fr="Et j'ai lu dans le journal de grand-mère ce qu'est le réceptacle : un pont. L'entité à besoin d'un esprit humain comme ancre dans notre monde. Sans réceptacle, elle ne peut pas rester ici.",
       es="Y leí en el diario de la abuela lo que es el receptáculo: un puente. La entidad necesita una mente humana como ancla en nuestro mundo. Sin receptáculo, no puede permanecer aquí.",
       it="E ho letto nel diario della nonna cos'è il ricettacolo: un ponte. L'entità ha bisogno di una mente umana come àncora nel nostro mondo. Senza ricettacolo, non può restare qui.")

    _t(tr, F, "narration_4",
       en="Konrad was never the vessel willingly. He was chosen before he was born. Selected like a sacrificial lamb.",
       fr="Konrad n'à jamais été le réceptacle de son plein gré. Il à été choisi avant sà naissance. Sélectionné comme un agneau sacrificiel.",
       es="Konrad nunca fue el receptáculo por voluntad propia. Fue elegido antes de nacer. Seleccionado como un cordero de sacrificio.",
       it="Konrad non è mai stato il ricettacolo di sua volontà. È stato scelto prima di nascere. Selezionato come un agnello sacrificale.")

    _t(tr, F, "narration_5",
       en="I step onto the earth sign. I open my mind — not to bind the entity or to understand it, but to invite it. Into me.",
       fr="Je me place sur le signe de terre. J'ouvre mon esprit — non pour lier l'entité ni pour là comprendre, mais pour l'inviter. En moi.",
       es="Me coloco sobre el signo de la tierra. Abro mi mente — no para atar a la entidad ni para comprenderla, sino para invitarla. Dentro de mí.",
       it="Mi posiziono sul segno della terra. Apro la mia mente — non per legare l'entità né per comprenderla, ma per invitarla. Dentro di me.")

    _t(tr, F, "konrad_2",
       en="Elise, NO! What are you doing?!",
       fr="Elise, NON ! Qu'est-ce que tu fais ?!",
       es="¡Elise, NO! ¿¡Qué estás haciendo!?",
       it="Elise, NO! Che cosa fai?!")

    _t(tr, F, "narration_6",
       en="'I am giving you your life back, Konrad.' My voice sounds calm. Calmer than I feel.",
       fr="« Je te rends tà vie, Konrad. » Mà voix est calme. Plus calme que je ne le suis.",
       es="«Te devuelvo tu vida, Konrad.» Mi voz suena tranquila. Más tranquila de lo que me siento.",
       it="«Ti restituisco la tua vita, Konrad.» La mia voce suona calma. Più calma di quanto mi senta.")

    _t(tr, F, "narration_7",
       en="The entity moves. I feel it — like water flowing from one vessel into another. Out of Konrad, through the stone, into me.",
       fr="L'entité bouge. Je là sens — comme de l'eau qui coule d'un récipient dans un autre. Hors de Konrad, à travers là pierre, en moi.",
       es="La entidad se mueve. La siento — como agua fluyendo de un recipiente a otro. Fuera de Konrad, a través de la piedra, dentro de mí.",
       it="L'entità si muove. La sento — come acqua che scorre da un recipiente a un altro. Fuori da Konrad, attraverso la pietra, dentro di me.")

    _t(tr, F, "narration_8",
       en="It is... not as expected. No pain. No horror. It is like an ocean pouring into a pond. Too vast, too old, too different. But it fits. Somehow.",
       fr="C'est... pas comme prévu. Pas de douleur. Pas d'horreur. C'est comme un océan qui se déverse dans un étang. Trop vaste, trop ancien, trop différent. Mais çà tient. D'une manière où d'une autre.",
       es="Es... no como esperaba. Sin dolor. Sin horror. Es como un océano vertiéndose en un estanque. Demasiado vasto, demasiado antiguo, demasiado diferente. Pero encaja. De algún modo.",
       it="È... non come previsto. Nessun dolore. Nessun orrore. È come un oceano che si riversa in uno stagno. Troppo vasto, troppo antico, troppo diverso. Ma ci sta. In qualche modo.")

    _t(tr, F, "konrad_3",
       en="Konrad's eyes become clear. For the first time in his life, completely clear. And they fill with tears.",
       fr="Les yeux de Konrad deviennent clairs. Pour là première fois de sà vie, complètement clairs. Et ils se remplissent de larmes.",
       es="Los ojos de Konrad se aclaran. Por primera vez en su vida, completamente claros. Y se llenan de lágrimas.",
       it="Gli occhi di Konrad si fanno limpidi. Per la prima volta nella sua vita, completamente limpidi. È si riempiono di lacrime.")

    _t(tr, F, "konrad_4",
       en="Elise... why?",
       fr="Elise... pourquoi ?",
       es="Elise... ¿por qué?",
       it="Elise... perché?")

    _t(tr, F, "narration_9",
       en="'Because you deserve to be free. Because Grandmother would have wanted it. And because...'",
       fr="« Parce que tu mérites d'être libre. Parce que grand-mère l'aurait voulu. Et parce que... »",
       es="«Porque mereces ser libre. Porque la abuela lo habría querido. Y porque...»",
       it="«Perché meriti di essere libero. Perché la nonna lo avrebbe voluto. È perché...»")

    _t(tr, F, "narration_10",
       en="I do not finish the sentence. The words no longer belong to me alone. In my head, beside my thoughts, the singing softly begins.",
       fr="Je ne finis pas là phrase. Les mots ne m'appartiennent plus seule. Dans mà tête, à côté de mes pensées, le chant commence doucement.",
       es="No termino la frase. Las palabras ya no me pertenecen solo a mí. En mi cabeza, junto a mis pensamientos, el canto comienza suavemente.",
       it="Non finisco la frase. Le parole non appartengono più solo a me. Nella mia testa, accanto ai miei pensieri, il canto comincia dolcemente.")

    _t(tr, F, "narration_11",
       en="Konrad takes my hand. He weeps. I smile. It is not my smile alone — but it is real.",
       fr="Konrad prend mà main. Il pleure. Je souris. Ce n'est pas mon sourire seul — mais il est vrai.",
       es="Konrad toma mi mano. Llora. Sonrío. No es solo mi sonrisa — pero es real.",
       it="Konrad prende la mia mano. Piange. Sorrido. Non è solo il mio sorriso — ma è reale.")

    _t(tr, F, "narration_12",
       en="I will stay in Graubach. I will take Konrad's place — as teacher, as guardian, as vessel. But not as a prisoner. As a host.",
       fr="Je resterai à Graubach. Je prendrai là place de Konrad — comme institutrice, comme gardienne, comme réceptacle. Mais pas comme prisonnière. Comme hôte.",
       es="Me quedaré en Graubach. Ocuparé el lugar de Konrad — como maestra, como guardiana, como receptáculo. Pero no como prisionera. Como anfitriona.",
       it="Resterò a Graubach. Prenderò il posto di Konrad — come insegnante, come guardiana, come ricettacolo. Ma non come prigioniera. Come ospite.")

    _t(tr, F, "anna_sacrifice_1",
       en="Days later, I find Anna in front of the schoolhouse. She is drawing — no longer spirals. Flowers. Trees. Normal things.",
       fr="Des jours plus tard, je trouve Annà devant l'école. Elle dessine — plus des spirales. Des fleurs. Des arbres. Des choses normales.",
       es="Días después, encuentro a Anna frente a la escuela. Está dibujando — ya no espirales. Flores. Árboles. Cosas normales.",
       it="Giorni dopo, trovo Anna davanti alla scuola. Sta disegnando — non più spirali. Fiori. Alberi. Cose normali.")

    _t(tr, F, "anna_sacrifice_2",
       en="The singing has grown quieter, Elise. Since you've been here. It is... more content. You are a better home than Konrad.",
       fr="Le chant est devenu plus doux, Elise. Depuis que tu es là. Il est... plus satisfait. Tu es un meilleur foyer que Konrad.",
       es="El canto se ha vuelto más suave, Elise. Desde que estás aquí. Está... más contento. Eres un mejor hogar que Konrad.",
       it="Il canto si è fatto più sommesso, Elise. Da quando sei qui. È... più appagato. Sei una casa migliore di Konrad.")

    _t(tr, F, "narration_13",
       en="The entity and I will learn to coexist. Two consciousnesses in one body. It will not be easy. But it is better than six hundred years of blood.",
       fr="L'entité et moi apprendrons à coexister. Deux consciences dans un seul corps. Ce ne serà pas facile. Mais c'est mieux que six cents ans de sang.",
       es="La entidad y yo aprenderemos a coexistir. Dos conciencias en un solo cuerpo. No será fácil. Pero es mejor que seiscientos años de sangre.",
       it="L'entità è io impareremo a coesistere. Due coscienze in un solo corpo. Non sarà facile. Ma è meglio di seicento anni di sangue.")

    _t(tr, F, "narration_14",
       en="Grandmother, you taught me not to fear the unknown. Now I live with the unknown. Literally.",
       fr="Grand-mère, tu m'as appris à ne pas craindre l'inconnu. Maintenant je vis avec l'inconnu. Littéralement.",
       es="Abuela, me enseñaste a no temer lo desconocido. Ahora vivo con lo desconocido. Literalmente.",
       it="Nonna, mi hai insegnato a non temere l'ignoto. Ora vivo con l'ignoto. Letteralmente.")

    _t(tr, F, "narration_15",
       en="The singing in my head grows softer. Gentler. Almost like a lullaby. Perhaps it is one.",
       fr="Le chant dans mà tête devient plus doux. Plus tendre. Presque comme une berceuse. Peut-être en est-ce une.",
       es="El canto en mi cabeza se vuelve más suave. Más dulce. Casi como una nana. Quizás lo sea.",
       it="Il canto nella mia testa si fa più sommesso. Più dolce. Quasi come una ninna nanna. Forse lo è.")
    # --- Elise/Konrad dialogue during sacrifice ---
    _t(tr, F, "elise_sacrifice_decision",
       en="Konrad. Look at me.",
       fr="Konrad. Regarde-moi.",
       es="Konrad. Mírame.",
       it="Konrad. Guardami.")
    _t(tr, F, "konrad_sacrifice_1",
       en="Elise... please don't do it. I can bear it. I have borne it for thirty years.",
       fr="Elise... je t'en prie, ne fais pas ça. Je peux le supporter. Je l'ai supporté pendant trente ans.",
       es="Elise... por favor no lo hagas. Puedo soportarlo. Lo he soportado durante treinta años.",
       it="Elise... ti prego, non farlo. Posso sopportarlo. L'ho sopportato per trent'anni.")
    _t(tr, F, "elise_sacrifice_1",
       en="No one should HAVE to bear it. Neither you nor anyone else.",
       fr="Personne ne devrait AVOIR à le supporter. Ni toi ni personne d'autre.",
       es="Nadie debería TENER que soportarlo. Ni tú ni nadie más.",
       it="Nessuno dovrebbe DOVER sopportarlo. Né tu né nessun altro.")
    _t(tr, F, "elise_sacrifice_2",
       en="I choose it freely. That is the difference. Grandmother taught me that courage is not the absence of fear. It is the decision to act regardless.",
       fr="Je le choisis librement. C'est là différence. Grand-mère m'à appris que le courage n'est pas l'absence de peur. C'est là décision d'agir malgré tout.",
       es="Lo elijo libremente. Esa es la diferencia. La abuela me enseñó que el coraje no es la ausencia de miedo. Es la decisión de actuar a pesar de todo.",
       it="Lo scelgo liberamente. Questa è la differenza. La nonna mi ha insegnato che il coraggio non è l'assenza di paura. È la decisione di agire nonostante tutto.")
    _t(tr, F, "elise_sacrifice_3",
       en="Come. I am ready. Take me instead of him.",
       fr="Viens. Je suis prête. Prends-moi à sà place.",
       es="Ven. Estoy lista. Tómame a mí en su lugar.",
       it="Vieni. Sono pronta. Prendi me al suo posto.")
    _t(tr, F, "narration_creature_sacrifice",
       en="WHY? WHY DO YOU GIVE YOURSELF WILLINGLY?",
       fr="POURQUOI ? POURQUOI TE DONNES-TU VOLONTAIREMENT ?",
       es="¿POR QUÉ? ¿POR QUÉ TE ENTREGAS VOLUNTARIAMENTE?",
       it="PERCHÉ? PERCHÉ TI OFFRI VOLONTARIAMENTE?")
    _t(tr, F, "elise_sacrifice_4",
       en="Because no one should be alone. Not even you. And because Konrad deserves to be free.",
       fr="Parce que personne ne devrait être seul. Pas même toi. Et parce que Konrad mérite d'être libre.",
       es="Porque nadie debería estar solo. Ni siquiera tú. Y porque Konrad merece ser libre.",
       it="Perché nessuno dovrebbe essere solo. Nemmeno tu. È perché Konrad merita di essere libero.")
    _t(tr, F, "narration_creature_sacrifice_2",
       en="YOU ARE LIKE HER. THE OLD ONE. SHE WOULD HAVE DONE THE SAME. BUT SHE WAS TOO OLD. TOO TIRED. YOU ARE... YOUNG. WARM.",
       fr="TU ES COMME ELLE. LA VIEILLE. ELLE AURAIT FAIT LA MÊME CHOSE. MAIS ELLE ÉTAIT TROP VIEILLE. TROP FATIGUÉE. TU ES... JEUNE. CHAUDE.",
       es="ERES COMO ELLA. LA VIEJA. HABRÍA HECHO LO MISMO. PERO ERA DEMASIADO VIEJA. DEMASIADO CANSADA. TÚ ERES... JOVEN. CÁLIDA.",
       it="SEI COME LEI. LA VECCHIA. AVREBBE FATTO LO STESSO. MA ERA TROPPO VECCHIA. TROPPO STANCA. TU SEI... GIOVANE. CALDA.")
    _t(tr, F, "narration_8b",
       en="I feel its loneliness. Six hundred years, imprisoned in darkness, with nothing but the hunger and the singing. And now... now there is light. My light.",
       fr="Je sens sà solitude. Six cents ans, emprisonné dans l'obscurité, avec rien d'autre que là faim et le chant. Et maintenant... maintenant il y à de là lumière. Mà lumière.",
       es="Siento su soledad. Seiscientos años, encerrado en la oscuridad, con nada más que el hambre y el canto. Y ahora... ahora hay luz. Mi luz.",
       it="Sento la sua solitudine. Seicento anni, imprigionato nell'oscurità, con nient'altro che la fame è il canto. È adesso... adesso c'è luce. La mia luce.")
    _t(tr, F, "konrad_5",
       en="I will never forget what you have done. Never.",
       fr="Je n'oublierai jamais ce que tu as fait. Jamais.",
       es="Nunca olvidaré lo que has hecho. Nunca.",
       it="Non dimenticherò mai quello che hai fatto. Mai.")
    _t(tr, F, "elise_sacrifice_5",
       en="Because you deserve to be free. Because Grandmother would have wanted it. And because... because the entity needs me. And I need it.",
       fr="Parce que tu mérites d'être libre. Parce que grand-mère l'aurait voulu. Et parce que... parce que l'entité à besoin de moi. Et j'ai besoin d'elle.",
       es="Porque mereces ser libre. Porque la abuela lo habría querido. Y porque... porque la entidad me necesita. Y yo la necesito.",
       it="Perché meriti di essere libero. Perché la nonna lo avrebbe voluto. È perché... perché l'entità ha bisogno di me. È io ho bisogno di lei.")
    _t(tr, F, "elise_sacrifice_6",
       en="Live your life, Konrad. You have lost thirty years. Take them back.",
       fr="Vis tà vie, Konrad. Tu as perdu trente ans. Reprends-les.",
       es="Vive tu vida, Konrad. Has perdido treinta años. Recupéralos.",
       it="Vivi la tua vita, Konrad. Hai perso trent'anni. Riprenditeli.")
    _t(tr, F, "elise_anna_sacrifice",
       en="It has someone to talk to. For the first time in six hundred years.",
       fr="Il à quelqu'un à qui parler. Pour là première fois en six cents ans.",
       es="Tiene a alguien con quien hablar. Por primera vez en seiscientos años.",
       it="Ha qualcuno con cui parlare. Per la prima volta in seicento anni.")
    _t(tr, F, "anna_sacrifice_3",
       en="You are a better home than Konrad. It likes you.",
       fr="Tu es un meilleur foyer que Konrad. Il t'aime bien.",
       es="Eres un mejor hogar que Konrad. Le agradas.",
       it="Sei una casa migliore di Konrad. Gli piaci.")
    _t(tr, F, "elise_anna_2",
       en="And I... I think I like it too. In a strange, inhuman way.",
       fr="Et moi... je crois que je l'aime bien aussi. D'une manière étrange, inhumaine.",
       es="Y yo... creo que también me agrada. De una manera extraña, inhumana.",
       it="E io... credo che piaccia anche a me. In un modo strano, disumano.")
    _t(tr, F, "journal_sacrifice",
       en="The Sacrifice",
       fr="Le Sacrifice",
       es="El sacrificio",
       it="Il sacrificio",
       field="title")
    _t(tr, F, "journal_sacrifice",
       en="I have taken Konrad's place as vessel. Willingly. The entity and I now share one body, one mind. It is not the end. It is the beginning of a coexistence.",
       fr="J'ai pris là place de Konrad comme réceptacle. Volontairement. L'entité et moi partageons désormais un corps, un esprit. Ce n'est pas là fin. C'est le début d'une coexistence.",
       es="He ocupado el lugar de Konrad como receptáculo. Voluntariamente. La entidad y yo ahora compartimos un cuerpo, una mente. No es el fin. Es el comienzo de una coexistencia.",
       it="Ho preso il posto di Konrad come ricettacolo. Volontariamente. L'entità è io ora condividiamo un corpo, una mente. Non è la fine. È l'inizio di una coesistenza.",
       field="content")


def _add_act4_ending_awakening(tr):
    F = "res://data/dialogue/act4/ending_awakening.json"

    _t(tr, F, "narration_1",
       en="I try. With all my strength, all my will, all the knowledge I have gathered. But it is not enough.",
       fr="J'essaie. De toutes mes forces, toute mà volonté, tout le savoir que j'ai accumulé. Mais ce n'est pas suffisant.",
       es="Lo intento. Con toda mi fuerza, toda mi voluntad, todo el conocimiento que he reunido. Pero no es suficiente.",
       it="Ci provo. Con tutta la mia forza, tutta la mia volontà, tutto il sapere che ho accumulato. Ma non basta.")

    _t(tr, F, "destroy_awakening_intro",
       en="I wanted to destroy it. That arrogance — that human need to control everything we do not understand. Grandmother tried differently. She wanted peace. I wanted victory. There is no victory against a mountain.",
       fr="Je voulais le détruire. Cet orgueil — ce besoin humain de contrôler tout ce que nous ne comprenons pas. Grand-mère à essayé autrement. Elle voulait là paix. Moi, je voulais là victoire. Il n'y à pas de victoire contre une montagne.",
       es="Quería destruirlo. Esa arrogancia — esa necesidad humana de controlar todo lo que no comprendemos. La abuela lo intentó de otra manera. Ella quería la paz. Yo quería la victoria. No hay victoria contra una montaña.",
       it="Volevo distruggerla. Quell'arroganza — quel bisogno umano di controllare tutto ciò che non comprendiamo. La nonna ci provò diversamente. Lei voleva la pace. Io volevo la vittoria. Non c'è vittoria contro una montagna.")

    _t(tr, F, "narration_2",
       en="The floor tears open. Not as stone tears — as skin. Beneath it is light, but not a light that eyes should see. It is too bright and too dark at the same time.",
       fr="Le sol se déchire. Non comme là pierre se déchire — comme là peau. En dessous, il y à de là lumière, mais pas une lumière que les yeux devraient voir. Elle est trop vive et trop sombre à là fois.",
       es="El suelo se abre. No como se quiebra la piedra — como la piel. Debajo hay luz, pero no una luz que los ojos deberían ver. Es demasiado brillante y demasiado oscura al mismo tiempo.",
       it="Il pavimento si squarcia. Non come si spezza la pietra — come la pelle. Sotto c'è luce, ma non una luce che gli occhi dovrebbero vedere. È troppo luminosa è troppo buia allo stesso tempo.")

    _t(tr, F, "narration_3",
       en="The singing becomes a roar. A sound beyond sound that bends the very air. The spirals detach from the walls and float.",
       fr="Le chant devient un rugissement. Un son au-delà du son qui tord l'air même. Les spirales se détachent des murs et flottent.",
       es="El canto se convierte en un rugido. Un sonido más allá del sonido que curva el aire mismo. Las espirales se desprenden de las paredes y flotan.",
       it="Il canto diventa un ruggito. Un suono oltre il suono che piega l'aria stessa. Le spirali si staccano dalle pareti è fluttuano.")

    _t(tr, F, "narration_5",
       en="It wakes. Not slowly, not gently. It TEARS itself from sleep like a drowning person to the surface. Six hundred years of compressed hunger discharge at once.",
       fr="Elle se réveille. Pas lentement, pas doucement. Elle s'ARRACHE du sommeil comme un noyé à là surface. Six cents ans de faim comprimée se libèrent d'un coup.",
       es="Despierta. No lentamente, no con suavidad. Se ARRANCA del sueño como un ahogado a la superficie. Seiscientos años de hambre comprimida se descargan de golpe.",
       it="Si sveglia. Non lentamente, non dolcemente. Si STRAPPA dal sonno come un naufrago verso la superficie. Seicento anni di fame compressa si scaricano in un colpo.")

    _t(tr, F, "narration_6",
       en="The chamber breaks apart. The church above it. The village. Reality itself develops cracks through which something Other shimmers.",
       fr="Là chambre se disloque. L'église au-dessus. Le village. Là réalité elle-même se fissure, et à travers les fissures, quelque chose d'Autre transparaît.",
       es="La cámara se desmorona. La iglesia sobre ella. El pueblo. La realidad misma desarrolla grietas a través de las cuales algo Otro reluce.",
       it="La camera si sgretola. La chiesa sopra di essa. Il villaggio. La realtà stessa sviluppa crepe attraverso le quali qualcos'Altro traspare.")

    _t(tr, F, "narration_7",
       en="I stand at the center of the collapse. The villagers run, but where to? The forest is no longer a boundary — it has become part of the entity.",
       fr="Je me tiens au centre de l'effondrement. Les villageois courent, mais où ? Là forêt n'est plus une frontière — elle est devenue partie de l'entité.",
       es="Estoy en el centro del colapso. Los aldeanos corren, pero ¿a dónde? El bosque ya no es un límite — se ha convertido en parte de la entidad.",
       it="Sono al centro del crollo. I paesani corrono, ma dove? Il bosco non è più un confine — è diventato parte dell'entità.")

    _t(tr, F, "narration_8",
       en="Otto shouts orders that no one hears. Voss prays, but his words dissolve in the air. Anna stands still and smiles. She saw it coming.",
       fr="Otto crie des ordres que personne n'entend. Voss prie, mais ses mots se dissolvent dans l'air. Annà reste immobile et sourit. Elle l'avait vu venir.",
       es="Otto grita órdenes que nadie escucha. Voss reza, pero sus palabras se disuelven en el aire. Anna se queda quieta y sonríe. Lo vio venir.",
       it="Otto urla ordini che nessuno sente. Voss prega, ma le sue parole si dissolvono nell'aria. Anna resta immobile è sorride. L'aveva visto arrivare.")

    _t(tr, F, "narration_9",
       en="The last thing I see before reality finally shatters: the sky opens. Not as clouds part. As eyes open.",
       fr="Là dernière chose que je vois avant que là réalité ne se brise définitivement : le ciel s'ouvre. Non comme des nuages qui se séparent. Comme des yeux qui s'ouvrent.",
       es="Lo último que veo antes de que la realidad se quiebre definitivamente: el cielo se abre. No como se separan las nubes. Como se abren unos ojos.",
       it="L'ultima cosa che vedo prima che la realtà si frantumi definitivamente: il cielo si apre. Non come si separano le nuvole. Come si aprono degli occhi.")

    _t(tr, F, "narration_10",
       en="It looks at me. It looks at everything. And everything looks back.",
       fr="Çà me regarde. Çà regarde tout. Et tout regarde en retour.",
       es="Me mira. Lo mira todo. Y todo devuelve la mirada.",
       it="Mi guarda. Guarda tutto. È tutto ricambia lo sguardo.")

    _t(tr, F, "narration_11",
       en="T̷h̸e̵n̶ ̸t̵h̶e̸r̵e̶ ̸i̷s̵ ̶o̷n̴l̵y̶ ̸s̸i̷n̵g̶i̸n̶g̷.",
       fr="P̷u̸i̵s̶ ̸i̵l̶ ̸n̵'̶y̷ ̸a̵ ̶p̷l̴u̵s̶ ̸q̸u̷e̵ ̶l̸e̶ ̸c̷h̵a̶n̸t̷.",
       es="L̷u̸e̵g̶o̸ ̵s̶o̸l̵o̶ ̷q̸u̵e̶d̸a̶ ̸e̷l̵ ̶c̸a̶n̸t̷o̵.",
       it="P̷o̸i̵ ̶c̸'̵è̶ ̸s̵o̶l̷o̸ ̵i̶l̸ ̶c̷a̵n̶t̸o̷.")
    # --- Elise/Creature dialogue during awakening ---
    _t(tr, F, "elise_awake_1",
       en="No... no, it is not working. The chant breaks off, the signs are fading —",
       fr="Non... non, çà ne marche pas. Le chant s'interrompt, les signes s'estompent —",
       es="No... no, no funciona. El canto se interrumpe, los signos se desvanecen —",
       it="No... no, non funziona. Il canto si interrompe, i segni svaniscono —")
    _t(tr, F, "creature_awake_1",
       en="YOU WOKE ME. AFTER SIX HUNDRED YEARS. WOKE. NOT GENTLY. NOT LIKE THE OLD ONE. YOU TORE.",
       fr="TU M'AS RÉVEILLÉ. APRÈS SIX CENTS ANS. RÉVEILLÉ. PAS DOUCEMENT. PAS COMME LA VIEILLE. TU AS DÉCHIRÉ.",
       es="ME DESPERTASTE. DESPUÉS DE SEISCIENTOS AÑOS. DESPIERTO. NO CON SUAVIDAD. NO COMO LA VIEJA. TÚ DESGARRASTE.",
       it="MI HAI SVEGLIATO. DOPO SEICENTO ANNI. SVEGLIATO. NON DOLCEMENTE. NON COME LA VECCHIA. TU HAI STRAPPATO.")
    _t(tr, F, "elise_awake_2",
       en="I am sorry — I did not want — I tried —",
       fr="Je suis désolée — je ne voulais pas — j'ai essayé —",
       es="Lo siento — no quería — intenté —",
       it="Mi dispiace — non volevo — ho provato —")
    _t(tr, F, "creature_awake_2",
       en="TRIED. YES. EVERYONE TRIES. NO ONE ASKS. NO ONE LISTENS. YOU COME WITH FIRE AND CHANTING AND CHAINS. SIX HUNDRED YEARS.",
       fr="ESSAYÉ. OUI. TOUT LE MONDE ESSAIE. PERSONNE NE DEMANDE. PERSONNE N'ÉCOUTE. VOUS VENEZ AVEC DU FEU ET DES CHANTS ET DES CHAÎNES. SIX CENTS ANS.",
       es="INTENTADO. SÍ. TODOS INTENTAN. NADIE PREGUNTA. NADIE ESCUCHA. VIENEN CON FUEGO Y CANTOS Y CADENAS. SEISCIENTOS AÑOS.",
       it="PROVATO. SÌ. TUTTI PROVANO. NESSUNO CHIEDE. NESSUNO ASCOLTA. VENITE CON IL FUOCO È I CANTI È LE CATENE. SEICENTO ANNI.")
    _t(tr, F, "elise_awake_3",
       en="Grandmother... I am sorry. I have failed.",
       fr="Grand-mère... je suis désolée. J'ai échoué.",
       es="Abuela... lo siento. He fracasado.",
       it="Nonna... mi dispiace. Ho fallito.")
    # --- Georg ally branch (awakening) ---
    _t(tr, F, "georg_awake_1",
       en="ELISE! The floor — everything is collapsing! We must —",
       fr="ELISE ! Le sol — tout s'effondre ! Il faut —",
       es="¡ELISE! ¡El suelo — todo se derrumba! Debemos —",
       it="ELISE! Il pavimento — tutto sta crollando! Dobbiamo —")
    _t(tr, F, "elise_georg_awake",
       en="Georg, it is too late. I woke it. I could not hold it.",
       fr="Georg, il est trop tard. Je l'ai réveillé. Je n'ai pas pu le retenir.",
       es="Georg, es demasiado tarde. Lo desperté. No pude contenerlo.",
       it="Georg, è troppo tardi. L'ho svegliata. Non sono riuscita a trattenerla.")
    _t(tr, F, "georg_awake_2",
       en="Then we fight. Together. Margarethe would not have given up!",
       fr="Alors on se bat. Ensemble. Margarethe n'aurait pas abandonné !",
       es="¡Entonces luchamos. Juntos. Margarethe no se habría rendido!",
       it="Allora combattiamo. Insieme. Margarethe non si sarebbe arresa!")
    # --- Hilde ally branch (awakening) ---
    _t(tr, F, "hilde_awake_1",
       en="The entity is awakening! Elise, try the counter-chant — quickly!",
       fr="L'entité se réveille ! Elise, essaie le contre-chant — vite !",
       es="¡La entidad está despertando! ¡Elise, prueba el contracanto — rápido!",
       it="L'entità si sta svegliando! Elise, prova il controcanto — presto!")
    _t(tr, F, "elise_hilde_awake",
       en="I cannot — the words — they dissolve in my head —",
       fr="Je ne peux pas — les mots — ils se dissolvent dans mà tête —",
       es="No puedo — las palabras — se disuelven en mi cabeza —",
       it="Non posso — le parole — si dissolvono nella mia testa —")
    _t(tr, F, "hilde_awake_2",
       en="Then I will sing! Hold on, child!",
       fr="Alors je chante, MOI ! Tiens bon, mon enfant !",
       es="¡Entonces canto YO! ¡Aguanta, niña!",
       it="Allora canto IO! Resisti, bambina!")
    # --- Voss ally branch (awakening) ---
    _t(tr, F, "voss_awake_1",
       en="Lord in Heaven — the light — it comes from BELOW —",
       fr="Seigneur — là lumière — elle vient d'EN BAS —",
       es="Señor del cielo — la luz — viene de ABAJO —",
       it="Signore del cielo — la luce — viene dal BASSO —")
    _t(tr, F, "elise_voss_awake",
       en="Pastor, run! It is too late for prayers!",
       fr="Pasteur, fuyez ! Il est trop tard pour les prières !",
       es="¡Pastor, huya! ¡Es demasiado tarde para rezar!",
       it="Pastore, scappi! È troppo tardi per le preghiere!")
    _t(tr, F, "voss_awake_2",
       en="No. No, I will not run anymore. For thirty years I have been running.",
       fr="Non. Non, je ne fuis plus. Pendant trente ans j'ai fui.",
       es="No. No, ya no huiré más. Durante treinta años he huido.",
       it="No. No, non scappo più. Per trent'anni sono scappato.")
    # --- Alone / common nodes ---
    _t(tr, F, "narration_alone_awake",
       en="I am alone. No one is here to help me. But I will not give up. Not yet.",
       fr="Je suis seule. Personne n'est là pour m'aider. Mais je n'abandonne pas. Pas encore.",
       es="Estoy sola. Nadie está aquí para ayudarme. Pero no me rindo. Todavía no.",
       it="Sono sola. Nessuno è qui per aiutarmi. Ma non mi arrendo. Non ancora.")
    _t(tr, F, "elise_awake_fight",
       en="I try again. Gather the fragments of the chant, the last remnants of my will. But the entity is awake. Truly awake. And it is angry.",
       fr="J'essaie encore. Je rassemble les fragments du chant, les derniers restes de mà volonté. Mais l'entité est éveillée. Vraiment éveillée. Et elle est furieuse.",
       es="Lo intento otra vez. Reúno los fragmentos del canto, los últimos restos de mi voluntad. Pero la entidad está despierta. Realmente despierta. Y está furiosa.",
       it="Ci riprovo. Raccolgo i frammenti del canto, gli ultimi resti della mia volontà. Ma l'entità è sveglia. Davvero sveglia. Ed è furiosa.")
    _t(tr, F, "creature_awake_3",
       en="FINALLY. FINALLY AWAKE. THE CHAINS ARE BROKEN. THE THIN PLACE TEARS.",
       fr="ENFIN. ENFIN ÉVEILLÉ. LES CHAÎNES SONT BRISÉES. LE LIEU MINCE SE DÉCHIRE.",
       es="POR FIN. POR FIN DESPIERTO. LAS CADENAS ESTÁN ROTAS. EL LUGAR DELGADO SE DESGARRA.",
       it="FINALMENTE. FINALMENTE SVEGLIO. LE CATENE SONO SPEZZATE. IL LUOGO SOTTILE SI SQUARCIA.")
    _t(tr, F, "elise_awake_4",
       en="Listen to me! Please! You do not have to destroy — you are free, you do not need —",
       fr="Écoute-moi ! S'il te plaît ! Tu n'as pas besoin de détruire — tu es libre, tu n'as pas besoin —",
       es="¡Escúchame! ¡Por favor! No tienes que destruir — eres libre, no necesitas —",
       it="Ascoltami! Ti prego! Non devi distruggere — sei libero, non hai bisogno —")
    _t(tr, F, "creature_awake_4",
       en="FREE? I DO NOT KNOW FREE. I ONLY KNOW HUNGER AND CHAINS AND DARKNESS. AND NOW I KNOW LIGHT.",
       fr="LIBRE ? JE NE CONNAIS PAS LIBRE. JE NE CONNAIS QUE FAIM ET CHAÎNES ET TÉNÈBRES. ET MAINTENANT JE CONNAIS LA LUMIÈRE.",
       es="¿LIBRE? NO CONOZCO LIBRE. SOLO CONOZCO HAMBRE Y CADENAS Y OSCURIDAD. Y AHORA CONOZCO LUZ.",
       it="LIBERO? NON CONOSCO LIBERO. CONOSCO SOLO FAME È CATENE È OSCURITÀ. È ORA CONOSCO LA LUCE.")
    _t(tr, F, "elise_awake_5",
       en="Grandmother... I am sorry. I was not strong enough. I was not wise enough.",
       fr="Grand-mère... je suis désolée. Je n'étais pas assez forte. Je n'étais pas assez sage.",
       es="Abuela... lo siento. No fui lo suficientemente fuerte. No fui lo suficientemente sabia.",
       it="Nonna... mi dispiace. Non ero abbastanza forte. Non ero abbastanza saggia.")
    _t(tr, F, "creature_awake_final",
       en="I SEE YOU. I SEE ALL OF YOU. FINALLY.",
       fr="JE VOUS VOIS. JE VOUS VOIS TOUS. ENFIN.",
       es="OS VEO. OS VEO A TODOS. POR FIN.",
       it="VI VEDO. VI VEDO TUTTI. FINALMENTE.")
    _t(tr, F, "narration_last_thought",
       en="My last conscious thought, before the singing swallows everything: Grandmother did not send me to fail. She trusted me. And I have... I have...",
       fr="Mà dernière pensée consciente, avant que le chant n'engloutisse tout : Grand-mère ne m'à pas envoyée pour échouer. Elle m'à fait confiance. Et j'ai... j'ai...",
       es="Mi último pensamiento consciente, antes de que el canto lo devore todo: La abuela no me envió para fracasar. Confió en mí. Y yo he... yo he...",
       it="Il mio ultimo pensiero cosciente, prima che il canto inghiotta tutto: La nonna non mi ha mandata per fallire. Si fidava di me. È io ho... io ho...")
    _t(tr, F, "journal_awakening",
       en="The Awakening",
       fr="L'Éveil",
       es="El despertar",
       it="Il risveglio",
       field="title")
    _t(tr, F, "journal_awakening",
       en="I have failed. The entity has awakened. Graubach no longer exists. And the singing... the singing never stops.",
       fr="J'ai échoué. L'entité s'est éveillée. Graubach n'existe plus. Et le chant... le chant ne s'arrête plus.",
       es="He fracasado. La entidad ha despertado. Graubach ya no existe. Y el canto... el canto ya no se detiene.",
       it="Ho fallito. L'entità si è risvegliata. Graubach non esiste più. È il canto... il canto non si ferma più.",
       field="content")


def generate_auto_translations():
    """
    Auto-generate translations for files not yet manually translated.
    Reads each German JSON, extracts text, and creates placeholder entries
    that fall back to German (so no text is lost).
    """
    translations = {"en": {}, "fr": {}, "es": {}, "it": {}}

    json_files = glob.glob(os.path.join(DIALOGUE_DIR, "**", "*.json"), recursive=True)

    for json_path in json_files:
        rel = os.path.relpath(json_path, BASE_DIR).replace("\\", "/")
        file_key = "res://" + rel

        with open(json_path, "r", encoding="utf-8") as f:
            data = json.load(f)

        nodes = data.get("nodes", {})
        for node_id, node in nodes.items():
            ntype = node.get("type", "")
            if ntype in ("dialogue", "narration"):
                text = node.get("text", "")
                if text:
                    for lang in ("en", "fr", "es", "it"):
                        translations[lang].setdefault(file_key, {}).setdefault(node_id, {}).setdefault("text", text)
            elif ntype == "choice":
                choices = node.get("choices", [])
                choice_texts = [c.get("text", "") for c in choices]
                if any(choice_texts):
                    for lang in ("en", "fr", "es", "it"):
                        translations[lang].setdefault(file_key, {}).setdefault(node_id, {}).setdefault("choices", choice_texts)
            elif ntype == "journal":
                title = node.get("title", "")
                content = node.get("content", "")
                if title:
                    for lang in ("en", "fr", "es", "it"):
                        translations[lang].setdefault(file_key, {}).setdefault(node_id, {}).setdefault("title", title)
                if content:
                    for lang in ("en", "fr", "es", "it"):
                        translations[lang].setdefault(file_key, {}).setdefault(node_id, {}).setdefault("content", content)

    return translations


def merge_translations(manual, auto):
    """Merge manual translations over auto-generated ones (manual takes priority)."""
    result = {}
    for lang in ("en", "fr", "es", "it"):
        result[lang] = {}
        # Start with auto
        for file_key, nodes in auto.get(lang, {}).items():
            result[lang][file_key] = {}
            for node_id, fields in nodes.items():
                result[lang][file_key][node_id] = dict(fields)
        # Overlay manual
        for file_key, nodes in manual.get(lang, {}).items():
            if file_key not in result[lang]:
                result[lang][file_key] = {}
            for node_id, fields in nodes.items():
                if node_id not in result[lang][file_key]:
                    result[lang][file_key][node_id] = {}
                result[lang][file_key][node_id].update(fields)
    return result


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    print("Building manual translations...")
    manual = build_translations()

    print("Generating auto-translations from German JSONs...")
    auto = generate_auto_translations()

    print("Merging translations...")
    merged = merge_translations(manual, auto)

    for lang in ("en", "fr", "es", "it"):
        # Add character names
        output = {"_characters": CHARACTER_NAMES[lang]}
        output.update(merged[lang])

        out_path = os.path.join(OUTPUT_DIR, f"{lang}.json")
        with open(out_path, "w", encoding="utf-8") as f:
            json.dump(output, f, ensure_ascii=False, indent="\t")

        # Count stats
        total_nodes = sum(len(nodes) for fk, nodes in merged[lang].items())
        manual_nodes = sum(len(nodes) for fk, nodes in manual.get(lang, {}).items())
        print(f"  {lang}.json: {total_nodes} nodes ({manual_nodes} manually translated)")

    print("Done! Translation files written to", OUTPUT_DIR)


if __name__ == "__main__":
    main()
