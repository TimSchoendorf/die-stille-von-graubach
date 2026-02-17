"""Act 2 translations: investigation, church, konrad, hilde_ritual, the_book."""

from .common import _t, _tc


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
       en="'1923: I found the name. In the book in the chamber. Elise Margarethe Brandt. Written in an ink that pulses. My granddaughter. Who is studying in Berlin and suspects nothing of all this.'",
       fr="'1923 : J'ai trouvé le nom. Dans le livre de la chambre. Elise Margarethe Brandt. Écrit dans une encre qui pulse. Ma petite-fille. Qui étudie à Berlin et ne se doute de rien.'",
       es="'1923: Encontré el nombre. En el libro de la cámara. Elise Margarethe Brandt. Escrito en una tinta que pulsa. Mi nieta. Que estudia en Berlín y no sospecha nada de todo esto.'",
       it="'1923: Ho trovato il nome. Nel libro della camera. Elise Margarethe Brandt. Scritto in un inchiostro che pulsa. Mia nipote. Che studia a Berlino e non sospetta nulla di tutto questo.'")

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
       en="I am the anchor. My name in the book is the connection. Grandmother didn't try to cut that thread - she taught me to hold it on my own terms. Not as a sacrifice, but as a bridge.",
       fr="Je suis l'ancre. Mon nom dans le livre est le lien. Grand-mère ne voulait pas detruire cette connexion - elle voulait l'UTILISER. Non comme sacrifice, mais comme lien.",
       es="Yo soy el ancla. Mi nombre en el libro es la conexion. La abuela no queria destruir esta conexion - queria USARLA. No como sacrificio, sino como vinculo.",
       it="Io sono l'ancora. Il mio nome nel libro e il legame. La nonna non voleva distruggere questa connessione - voleva USARLA. Non come sacrificio, ma come tramite.")

    _t(tr, F, "elise_plan_3",
       en="Can this work? Or am I reading hope into notes written by a woman who was running out of time and refused to admit it?",
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
       en="If you truly want to know what lies beneath this church, come at midnight. Come alone. If Otto's men see us, neither of us will leave that chamber.",
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
       en="It's alive. Right beneath me, under stone and earth. I feel it not only in my fingertips, but in the place where my name is tied to it. As if the thing below has been waiting for this exact touch.",
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

    # --- Phase 10 Story-Konsistenz-Fixes ---
    _t(tr, F, "elise_hilde_knowledge",
       en="Hilde told me about the chant. And the sign of the earth. If you know where the thinnest point in the chamber is, you can save me time, Father.",
       fr="Hilde m'a parlé du chant. Et du signe de la terre. Si vous savez où se trouve le point le plus mince dans la chambre, vous pouvez me faire gagner du temps, mon Père.",
       es="Hilde me habló del canto. Y del signo de la tierra. Si sabe dónde está el punto más delgado en la cámara, puede ahorrarme tiempo, Padre.",
       it="Hilde mi ha parlato del canto. E del segno della terra. Se sa dove si trova il punto più sottile nella camera, può farmi risparmiare tempo, Padre.")

    _t(tr, F, "voss_hilde_react",
       en="The old pagan knows more than the Church would ever admit. Yes. I know the thinnest point. I will show you where you must stand.",
       fr="La vieille païenne en sait plus que l'Église ne l'admettrait jamais. Oui. Je connais le point le plus mince. Je vous montrerai où vous devez vous tenir.",
       es="La vieja pagana sabe más de lo que la Iglesia jamás admitiría. Sí. Conozco el punto más delgado. Le mostraré dónde debe colocarse.",
       it="La vecchia pagana sa più di quanto la Chiesa ammetterebbe mai. Sì. Conosco il punto più sottile. Le mostrerò dove deve stare.")

    # --- Phase 12: Foreshadowing ---
    _t(tr, F, "elise_heartbeat_hint",
       en="And in that recognition there is no hostility. Only... expectation. Like a dog that hears someone at the door and lifts its head.",
       fr="Et dans cette reconnaissance, il n'y a pas d'hostilité. Seulement... de l'attente. Comme un chien qui entend quelqu'un à la porte et lève la tête.",
       es="Y en ese reconocimiento no hay hostilidad. Solo... expectación. Como un perro que oye a alguien en la puerta y levanta la cabeza.",
       it="E in quel riconoscimento non c'è ostilità. Solo... attesa. Come un cane che sente qualcuno alla porta e alza la testa.")


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

    # --- Phase 9 Story-Fixes: Konrad possession clarity ---
    _t(tr, F, "konrad_possession_1",
       en="I observe him more closely. There — his gaze turns glassy. For three, four seconds there is no one behind his eyes. Then he returns, confused, as though he had been dreaming.",
       fr="Je l'observe plus attentivement. Là — son regard devient vitreux. Pendant trois, quatre secondes, il n'y a personne derrière ses yeux. Puis il revient, confus, comme s'il avait rêvé.",
       es="Lo observo más de cerca. Ahí — su mirada se vuelve vidriosa. Durante tres, cuatro segundos no hay nadie detrás de sus ojos. Luego vuelve, confuso, como si hubiera estado soñando.",
       it="Lo osservo più attentamente. Ecco — il suo sguardo diventa vitreo. Per tre, quattro secondi non c'è nessuno dietro i suoi occhi. Poi ritorna, confuso, come se avesse sognato.")
    _t(tr, F, "konrad_possession_2",
       en="How... how long was I just...? What did I say?",
       fr="Com... combien de temps est-ce que je viens de...? Qu'est-ce que j'ai dit ?",
       es="¿Cuánto... cuánto tiempo acabo de...? ¿Qué he dicho?",
       it="Quanto... per quanto tempo ho appena...? Cosa ho detto?")
    _t(tr, F, "konrad_possession_3",
       en="The creature sleeps and dreams through him. In those moments Konrad is not Konrad — he is a window through which something ancient peers. And the gaps are growing longer. Whole hours, he said, that he cannot account for.",
       fr="La créature dort et rêve à travers lui. Dans ces moments, Konrad n'est pas Konrad — il est une fenêtre à travers laquelle quelque chose d'ancien regarde. Et les absences s'allongent. Des heures entières, dit-il, dont il ne peut rendre compte.",
       es="La criatura duerme y sueña a través de él. En esos momentos Konrad no es Konrad — es una ventana a través de la cual algo antiguo mira. Y los vacíos se hacen más largos. Horas enteras, dice, que no puede explicar.",
       it="La creatura dorme e sogna attraverso di lui. In quei momenti Konrad non è Konrad — è una finestra attraverso la quale qualcosa di antico scruta. E i vuoti si allungano. Ore intere, dice, di cui non riesce a rendere conto.")

    # --- Phase 10 Story-Konsistenz-Fixes ---
    _t(tr, F, "georg_warned_about_konrad",
       en="Georg warned me. 'Be careful with the teacher,' he said. His eyes were more serious than I've seen in anyone. Konrad's smile conceals something.",
       fr="Georg m'a prévenue. « Soyez prudente avec l'instituteur », a-t-il dit. Ses yeux étaient plus graves que je n'en ai jamais vu. Le sourire de Konrad dissimule quelque chose.",
       es="Georg me advirtió. «Ten cuidado con el maestro», dijo. Sus ojos eran más serios de lo que he visto en nadie. La sonrisa de Konrad oculta algo.",
       it="Georg mi ha avvertita. 'Stia attenta con il maestro', ha detto. I suoi occhi erano più seri di quelli di chiunque altro. Il sorriso di Konrad nasconde qualcosa.")

    _t(tr, F, "georg_warned_2",
       en="I will be friendly. But on my guard. Every question I ask, every answer he gives — I will listen closely. Not just to the words. To what lies between the words.",
       fr="Je serai aimable. Mais sur mes gardes. Chaque question que je poserai, chaque réponse qu'il donnera — j'écouterai attentivement. Pas seulement les mots. Ce qui se cache entre les mots.",
       es="Seré amable. Pero estaré alerta. Cada pregunta que haga, cada respuesta que él dé — escucharé con atención. No solo las palabras. Lo que yace entre las palabras.",
       it="Sarò gentile. Ma in guardia. Ogni domanda che porrò, ogni risposta che darà — ascolterò attentamente. Non solo le parole. Ciò che giace tra le parole.")

    _t(tr, F, "konrad_coexistence_hint",
       en="But there are moments... when I stop fighting... then it's almost peaceful. As if one were sitting beside someone, not trapped inside someone.",
       fr="Mais il y a des moments... quand j'arrête de lutter... alors c'est presque paisible. Comme si l'on était assis à côté de quelqu'un, pas prisonnier à l'intérieur de quelqu'un.",
       es="Pero hay momentos... cuando dejo de luchar... entonces es casi apacible. Como si uno estuviera sentado junto a alguien, no atrapado dentro de alguien.",
       it="Ma ci sono momenti... quando smetto di combattere... allora è quasi sereno. Come se si sedesse accanto a qualcuno, non imprigionati dentro qualcuno.")

    _t(tr, F, "elise_coexistence_react",
       en="Not fighting, but coexisting? The thought is more disturbing than anything else. And yet — something about it rings true.",
       fr="Ne pas lutter, mais coexister ? L'idée est plus troublante que tout le reste. Et pourtant — quelque chose en elle sonne juste.",
       es="¿No luchar, sino coexistir? El pensamiento es más perturbador que cualquier otra cosa. Y sin embargo — algo en ello suena verdadero.",
       it="Non combattere, ma coesistere? Il pensiero è più inquietante di qualsiasi altra cosa. Eppure — qualcosa in esso suona vero.")


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

    # --- Phase 9 Story-Fixes: Letter riddle, creature duality, Margarethe ---
    _t(tr, F, "hilde_letter_1",
       en="Hilde... the letter. Grandmother's letter. How could it reach me in Berlin if she had already been dead for days when I arrived?",
       fr="Hilde... la lettre. La lettre de grand-mère. Comment a-t-elle pu me parvenir à Berlin si elle était déjà morte depuis des jours quand je suis arrivée ?",
       es="Hilde... la carta. La carta de la abuela. ¿Cómo pudo llegar a mí en Berlín si ella ya llevaba días muerta cuando llegué?",
       it="Hilde... la lettera. La lettera della nonna. Come ha potuto raggiungermi a Berlino se era già morta da giorni quando sono arrivata?")
    _t(tr, F, "hilde_letter_2",
       en="Ah. That was Margarethe's last spell. She wrote it months ago and bound it with a time-binder — an old ritual that only delivers the letter when the recipient is ready.",
       fr="Ah. C'était le dernier sortilège de Margarethe. Elle l'a écrite il y a des mois et l'a liée avec un lien temporel — un ancien rituel qui ne délivre la lettre que lorsque le destinataire est prêt.",
       es="Ah. Ese fue el último hechizo de Margarethe. La escribió hace meses y la ató con un vinculador temporal — un antiguo ritual que solo entrega la carta cuando el destinatario está listo.",
       it="Ah. Quello era l'ultimo incantesimo di Margarethe. L'ha scritta mesi fa e l'ha legata con un vincolo temporale — un antico rituale che consegna la lettera solo quando il destinatario è pronto.")
    _t(tr, F, "hilde_letter_3",
       en="Not when she dies, but when I am ready? That means the letter... waited for me?",
       fr="Pas quand elle meurt, mais quand JE suis prête ? Cela veut dire que la lettre... m'a attendue ?",
       es="¿No cuando ella muere, sino cuando YO estoy lista? Eso significa que la carta... ¿me esperó?",
       it="Non quando lei muore, ma quando IO sono pronta? Vuol dire che la lettera... mi ha aspettata?")
    _t(tr, F, "hilde_letter_4",
       en="Exactly. It waited for the right moment. The moment you were strong enough to come to Graubach.",
       fr="Exactement. Elle a attendu le bon moment. Le moment où tu étais assez forte pour venir à Graubach.",
       es="Exacto. Esperó el momento adecuado. El momento en que fuiste lo suficientemente fuerte para venir a Graubach.",
       it="Esattamente. Ha aspettato il momento giusto. Il momento in cui eri abbastanza forte per venire a Graubach.")
    _t(tr, F, "hilde_creature_dual_1",
       en="And one more thing, child. About the creature. The elders invented the feeding — not the creature. They interpreted its loneliness as hunger and answered with blood.",
       fr="Et encore une chose, mon enfant. À propos de la créature. Les anciens ont inventé la nourriture — pas la créature. Ils ont interprété sa solitude comme de la faim et ont répondu avec du sang.",
       es="Y una cosa más, niña. Sobre la criatura. Los ancianos inventaron la alimentación — no la criatura. Interpretaron su soledad como hambre y respondieron con sangre.",
       it="E un'altra cosa, bambina. Sulla creatura. Gli anziani hanno inventato la nutrizione — non la creatura. Hanno interpretato la sua solitudine come fame e hanno risposto col sangue.")
    _t(tr, F, "hilde_creature_dual_2",
       en="Perhaps that was wrong. Perhaps a conversation would have sufficed.",
       fr="Peut-être que c'était faux. Peut-être qu'une conversation aurait suffi.",
       es="Quizás eso estuvo mal. Quizás una conversación habría bastado.",
       it="Forse era sbagliato. Forse sarebbe bastata una conversazione.")
    _t(tr, F, "hilde_creature_dual_3",
       en="Hilde pauses. In the silence I hear the distant singing — quieter than usual, almost questioning.",
       fr="Hilde fait une pause. Dans le silence, j'entends le chant lointain — plus bas que d'habitude, presque interrogateur.",
       es="Hilde hace una pausa. En el silencio oigo el canto lejano — más bajo de lo habitual, casi interrogante.",
       it="Hilde si ferma. Nel silenzio sento il canto lontano — più basso del solito, quasi interrogativo.")
    _t(tr, F, "hilde_creature_dual_4",
       en="But who talks to what sleeps beneath the earth?",
       fr="Mais qui parle à ce qui dort sous la terre ?",
       es="Pero ¿quién habla con lo que duerme bajo la tierra?",
       it="Ma chi parla con ciò che dorme sotto terra?")
    _t(tr, F, "hilde_margarethe_1",
       en="Georg says Grandmother failed. That her ritual did not work. But you sound as if you know something different.",
       fr="Georg dit que grand-mère a échoué. Que son rituel n'a pas fonctionné. Mais vous parlez comme si vous saviez autre chose.",
       es="Georg dice que la abuela fracasó. Que su ritual no funcionó. Pero usted habla como si supiera algo diferente.",
       it="Georg dice che la nonna ha fallito. Che il suo rituale non ha funzionato. Ma lei parla come se sapesse qualcosa di diverso.")
    _t(tr, F, "hilde_margarethe_2",
       en="Georg believes she failed. Margarethe wanted it that way. She only told him half — to protect him.",
       fr="Georg croit qu'elle a échoué. Margarethe le voulait ainsi. Elle ne lui a dit que la moitié — pour le protéger.",
       es="Georg cree que fracasó. Margarethe lo quiso así. Solo le contó la mitad — para protegerlo.",
       it="Georg crede che abbia fallito. Margarethe lo voleva così. Gli ha detto solo la metà — per proteggerlo.")
    _t(tr, F, "hilde_margarethe_3",
       en="If Otto knew the ritual was complete, he would have long since... eliminated Georg.",
       fr="Si Otto savait que le rituel est complet, il aurait depuis longtemps... éliminé Georg.",
       es="Si Otto supiera que el ritual está completo, hace tiempo que habría... eliminado a Georg.",
       it="Se Otto sapesse che il rituale è completo, avrebbe da tempo... eliminato Georg.")
    _t(tr, F, "hilde_margarethe_4",
       en="Hilde lowers her voice. The shadows in the cottage seem to grow thicker.",
       fr="Hilde baisse la voix. Les ombres dans la chaumière semblent s'épaissir.",
       es="Hilde baja la voz. Las sombras en la cabaña parecen espesarse.",
       it="Hilde abbassa la voce. Le ombre nella capanna sembrano farsi più fitte.")
    _t(tr, F, "hilde_margarethe_5",
       en="The complete knowledge lies here. With me. And now with you.",
       fr="Le savoir complet est ici. Chez moi. Et maintenant chez toi.",
       es="El conocimiento completo está aquí. Conmigo. Y ahora contigo.",
       it="La conoscenza completa è qui. Con me. E ora con te.")

    # --- Phase 10 Story-Konsistenz-Fixes ---
    _tc(tr, F, "choice_practice_chant",
        en_choices=["Practice the chant — I must master it", "Later — I need more information first"],
        fr_choices=["Pratiquer le chant — je dois le maîtriser", "Plus tard — j'ai d'abord besoin de plus d'informations"],
        es_choices=["Practicar el canto — debo dominarlo", "Más tarde — primero necesito más información"],
        it_choices=["Esercitare il canto — devo padroneggiarlo", "Più tardi — prima ho bisogno di più informazioni"])

    _t(tr, F, "practice_chant_success",
       en="I practice the melody over and over until it imprints itself into my bones. Hilde corrects me patiently — a tone lower here, a breath longer there. After an hour, it sounds... right.",
       fr="Je répète la mélodie encore et encore jusqu'à ce qu'elle s'imprime dans mes os. Hilde me corrige patiemment — un ton plus bas ici, un souffle plus long là. Au bout d'une heure, cela sonne... juste.",
       es="Practico la melodía una y otra vez hasta que se graba en mis huesos. Hilde me corrige pacientemente — un tono más bajo aquí, una respiración más larga allá. Al cabo de una hora, suena... correcto.",
       it="Ripeto la melodia ancora e ancora finché non si imprime nelle mie ossa. Hilde mi corregge pazientemente — un tono più basso qui, un respiro più lungo là. Dopo un'ora, suona... giusto.")

    _t(tr, F, "skip_chant_practice",
       en="My head is spinning. The chant, the sign, the anchor — too much at once. I need to understand what all this means before I memorize it.",
       fr="Ma tête tourne. Le chant, le signe, l'ancre — trop de choses à la fois. Je dois d'abord comprendre ce que tout cela signifie avant de l'apprendre par cœur.",
       es="Me da vueltas la cabeza. El canto, el signo, el ancla — demasiado de golpe. Necesito entender qué significa todo esto antes de memorizarlo.",
       it="Mi gira la testa. Il canto, il segno, l'ancora — troppo tutto in una volta. Devo prima capire cosa significa tutto questo prima di impararlo a memoria.")

    _t(tr, F, "skip_chant_2",
       en="Don't wait too long, child. The chant needs practice. Without it, the seal is just an empty promise.",
       fr="N'attends pas trop longtemps, mon enfant. Le chant demande de la pratique. Sans lui, le sceau n'est qu'une promesse vide.",
       es="No esperes demasiado, niña. El canto necesita práctica. Sin él, el sello no es más que una promesa vacía.",
       it="Non aspettare troppo, bambina. Il canto richiede pratica. Senza di esso, il sigillo è solo una promessa vuota.")

    _t(tr, F, "hilde_margarethe_death_1",
       en="In the end, Margarethe did it. She went down one last time, the night before her death. Not to fight. To talk.",
       fr="À la fin, Margarethe l'a fait. Elle est descendue une dernière fois, la nuit précédant sa mort. Pas pour se battre. Pour parler.",
       es="Al final, Margarethe lo hizo. Bajó una última vez, la noche antes de su muerte. No para luchar. Para hablar.",
       it="Alla fine, Margarethe lo fece. Scese un'ultima volta, la notte prima della sua morte. Non per combattere. Per parlare.")

    _t(tr, F, "hilde_margarethe_death_2",
       en="She came back. Lay down in her bed, smiled, and closed her eyes. She died in her sleep, child. Peacefully. It was a farewell, not a sacrifice.",
       fr="Elle est revenue. Elle s'est couchée, a souri et a fermé les yeux. Elle est morte dans son sommeil, mon enfant. Paisiblement. C'était un adieu, pas un sacrifice.",
       es="Volvió. Se acostó, sonrió y cerró los ojos. Murió mientras dormía, niña. En paz. Fue una despedida, no un sacrificio.",
       it="È tornata. Si è coricata, ha sorriso e ha chiuso gli occhi. È morta nel sonno, bambina. Serenamente. Era un addio, non un sacrificio.")

    _t(tr, F, "hilde_margarethe_death_3",
       en="But Otto implied that her death wasn't natural...",
       fr="Mais Otto a laissé entendre que sa mort n'était pas naturelle...",
       es="Pero Otto insinuó que su muerte no fue natural...",
       it="Ma Otto ha lasciato intendere che la sua morte non fosse naturale...")

    _t(tr, F, "hilde_margarethe_death_4",
       en="Otto lies. That's what Otto does. He wants to frighten you into accepting his feeding. Don't believe a word that man says about Margarethe.",
       fr="Otto ment. C'est ce qu'Otto fait. Il veut te faire assez peur pour que tu acceptes sa Nourriture. Ne crois pas un mot de ce que cet homme dit sur Margarethe.",
       es="Otto miente. Eso es lo que Otto hace. Quiere asustarte para que aceptes su Alimentación. No creas ni una palabra de lo que ese hombre diga sobre Margarethe.",
       it="Otto mente. È quello che fa Otto. Vuole spaventarti perché tu accetti la sua Nutrizione. Non credere a una parola di ciò che quell'uomo dice su Margarethe.")

    _tc(tr, F, "choice_anchor_reaction",
        en_choices=["And if I die? What happens to the entity then?", "Grandmother wanted to be the anchor. Why didn't she do it?"],
        fr_choices=["Et si je meurs ? Qu'advient-il de l'entité ?", "Grand-mère voulait être l'ancre. Pourquoi ne l'a-t-elle pas fait ?"],
        es_choices=["¿Y si muero? ¿Qué ocurre entonces con la entidad?", "La abuela quería ser el ancla. ¿Por qué no lo hizo?"],
        it_choices=["E se muoio? Cosa succede all'entità?", "La nonna voleva essere l'ancora. Perché non l'ha fatto?"])

    _t(tr, F, "hilde_death_answer",
       en="If the anchor dies, the connection tears. The seal breaks. The entity awakens — confused, angry, hungry. That's why the anchor must be strong. And that's why it must be someone young enough.",
       fr="Si l'ancre meurt, la connexion se rompt. Le sceau se brise. L'entité s'éveille — confuse, furieuse, affamée. C'est pourquoi l'ancre doit être forte. Et c'est pourquoi ce doit être quelqu'un d'assez jeune.",
       es="Si el ancla muere, la conexión se desgarra. El sello se rompe. La entidad despierta — confusa, furiosa, hambrienta. Por eso el ancla debe ser fuerte. Y por eso debe ser alguien lo bastante joven.",
       it="Se l'ancora muore, la connessione si spezza. Il sigillo si rompe. L'entità si risveglia — confusa, furiosa, affamata. Ecco perché l'ancora deve essere forte. Ed ecco perché deve essere qualcuno abbastanza giovane.")

    _t(tr, F, "hilde_death_answer_2",
       en="So I don't just have to survive — I have to survive a LONG time. Thirty years. Like grandmother.",
       fr="Alors je ne dois pas seulement survivre — je dois survivre LONGTEMPS. Trente ans. Comme grand-mère.",
       es="Entonces no solo tengo que sobrevivir — tengo que sobrevivir MUCHO tiempo. Treinta años. Como la abuela.",
       it="Quindi non devo solo sopravvivere — devo sopravvivere a LUNGO. Trent'anni. Come la nonna.")

    _t(tr, F, "hilde_margarethe_answer",
       en="She wanted to. Until the very end. But her body gave out. The anchor needs strength — not physical, mental. And Margarethe's mind was weary. Thirty years awake, thirty years vigilant.",
       fr="Elle le voulait. Jusqu'au bout. Mais son corps a lâché. L'ancre a besoin de force — pas physique, mentale. Et l'esprit de Margarethe était las. Trente ans éveillée, trente ans vigilante.",
       es="Quería hacerlo. Hasta el final. Pero su cuerpo no aguantó más. El ancla necesita fuerza — no física, mental. Y la mente de Margarethe estaba agotada. Treinta años despierta, treinta años vigilante.",
       it="Lo voleva. Fino alla fine. Ma il suo corpo ha ceduto. L'ancora ha bisogno di forza — non fisica, mentale. E la mente di Margarethe era stanca. Trent'anni sveglia, trent'anni vigile.")

    _t(tr, F, "hilde_margarethe_answer_2",
       en="She waited for you. Not because you are stronger. Because you are fresh. Because you still have the strength she had lost.",
       fr="Elle t'a attendue. Non parce que tu es plus forte. Parce que tu es fraîche. Parce que tu as encore la force qu'elle avait perdue.",
       es="Te esperó a ti. No porque seas más fuerte. Porque estás fresca. Porque aún tienes la fuerza que ella había perdido.",
       it="Ha aspettato te. Non perché sei più forte. Perché sei fresca. Perché hai ancora la forza che lei aveva perduto.")

    # --- Phase 12: Foreshadowing ---
    _t(tr, F, "narration_chant_hint",
       en="The faltering doesn't sound like defense. It sounds like surprise. As if someone had received an answer for the first time after a very, very long time.",
       fr="Ce n'est pas un son de défense. C'est de la surprise. Comme si quelqu'un avait reçu une réponse pour la première fois après très, très longtemps.",
       es="El titubeo no suena como defensa. Suena como sorpresa. Como si alguien hubiera recibido una respuesta por primera vez después de mucho, mucho tiempo.",
       it="L'esitazione non suona come difesa. Suona come sorpresa. Come se qualcuno avesse ricevuto una risposta per la prima volta dopo molto, molto tempo.")


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

    # --- Phase 9 Story-Fixes: Train woman reference ---
    _t(tr, F, "zugfrau_1",
       en="I page back. Dozens of pages, hundreds of names. And then — an old entry: 'Mathilde, 1863'. Beside it a drawing. My breath catches.",
       fr="Je feuillette en arrière. Des dizaines de pages, des centaines de noms. Et puis — une ancienne entrée : « Mathilde, 1863 ». À côté, un dessin. Mon souffle se coupe.",
       es="Paso las páginas hacia atrás. Docenas de páginas, cientos de nombres. Y entonces — una entrada antigua: 'Mathilde, 1863'. Junto a ella un dibujo. Se me corta la respiración.",
       it="Sfoglio all'indietro. Decine di pagine, centinaia di nomi. E poi — una vecchia voce: 'Mathilde, 1863'. Accanto un disegno. Mi si mozza il respiro.")
    _t(tr, F, "zugfrau_2",
       en="The drawing shows a woman with empty eye sockets. The blind woman from the train. She was no stranger — she was the last to survive the ritual. She waited sixty years.",
       fr="Le dessin montre une femme aux orbites vides. La femme aveugle du train. Ce n'était pas une inconnue — c'était la dernière à avoir survécu au rituel. Elle a attendu soixante ans.",
       es="El dibujo muestra a una mujer con las cuencas de los ojos vacías. La mujer ciega del tren. No era una desconocida — era la última en sobrevivir al ritual. Esperó sesenta años.",
       it="Il disegno mostra una donna con le orbite vuote. La donna cieca del treno. Non era un'estranea — era l'ultima a sopravvivere al rituale. Ha aspettato sessant'anni.")

    # --- Phase 10 Story-Konsistenz-Fixes ---
    _t(tr, F, "voss_distrusts",
       en="But first... you lied to me in the church. About what you know. What you're looking for. I saw it in your eyes.",
       fr="Mais d'abord... vous m'avez menti dans l'église. Sur ce que vous savez. Ce que vous cherchez. Je l'ai vu dans vos yeux.",
       es="Pero primero... me mintió en la iglesia. Sobre lo que sabe. Lo que busca. Lo vi en sus ojos.",
       it="Ma prima... mi ha mentito in chiesa. Su ciò che sa. Su ciò che cerca. L'ho visto nei suoi occhi.")

    _t(tr, F, "elise_voss_lied",
       en="I didn't know if I could trust you, Father. Can you forgive me?",
       fr="Je ne savais pas si je pouvais vous faire confiance, mon Père. Pouvez-vous me pardonner ?",
       es="No sabía si podía confiar en usted, Padre. ¿Puede perdonarme?",
       it="Non sapevo se potevo fidarmi di lei, Padre. Può perdonarmi?")

    _t(tr, F, "voss_forgives_lie",
       en="Forgive? I am the last person who should condemn lies. I stayed silent for thirty years. That is worse than any lie.",
       fr="Pardonner ? Je suis le dernier à pouvoir condamner les mensonges. J'ai gardé le silence pendant trente ans. C'est pire que n'importe quel mensonge.",
       es="¿Perdonar? Soy el último que debería condenar las mentiras. Guardé silencio durante treinta años. Eso es peor que cualquier mentira.",
       it="Perdonare? Sono l'ultimo che dovrebbe condannare le bugie. Ho taciuto per trent'anni. È peggio di qualsiasi menzogna.")

