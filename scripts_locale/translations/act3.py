"""Act 3 translations: allies_choice, reality_breaks, descent, preparation."""

from .common import _t, _tc


def _add_act3_allies_choice(tr):
    F = "res://data/dialogue/act3/allies_choice.json"

    _t(tr, F, "narration_1", en="Day six, afternoon. Tomorrow is the anniversary. I need help - and I must decide whom I trust.", fr="Sixième jour, après-midi. Demain, c'est l'anniversaire. J'ai besoin d'aide - et je dois décider en qui j'ai confiance.", es="Día seis, por la tarde. Mañana es el aniversario. Necesito ayuda - y debo decidir en quién confío.", it="Sesto giorno, pomeriggio. Domani è l'anniversario. Ho bisogno di aiuto - è devo decidere di chi fidarmi.")
    _t(tr, F, "narration_2", en="Georg has the key and the strength. Hilde knows the chant and the old ways. Voss knows the chamber. And Konrad... Konrad is the key to everything - or the greatest danger.", fr="Georg à là clé et là force. Hilde connaît le chant et les anciennes traditions. Voss connaît là chambre. Et Konrad... Konrad est là clé de tout - où le plus grand danger.", es="Georg tiene la llave y la fuerza. Hilde conoce el canto y los antiguos caminos. Voss conoce la cámara. Y Konrad... Konrad es la clave de todo - o el mayor peligro.", it="Georg ha la chiave è la forza. Hilde conosce il canto è le antiche usanze. Voss conosce la camera. È Konrad... Konrad è la chiave di tutto - o il pericolo più grande.")
    _tc(tr, F, "choice_primary_ally",
        en_choices=["Choose Georg as main ally - strength and loyalty", "Choose Hilde as main ally - knowledge and experience", "Choose Voss as main ally - access and remorse", "Confide in no one - I won't put anyone in danger"],
        fr_choices=["Choisir Georg comme allié principal - force et loyauté", "Choisir Hilde comme alliée principale - savoir et expérience", "Choisir Voss comme allié principal - accès et remords", "Ne confier à personne - je ne veux mettre personne en danger"],
        es_choices=["Elegir a Georg como aliado principal - fuerza y lealtad", "Elegir a Hilde como aliada principal - conocimiento y experiencia", "Elegir a Voss como aliado principal - acceso y remordimiento", "No confiar en nadie - no quiero poner a nadie en peligro"],
        it_choices=["Scegliere Georg come alleato principale - forza e lealtà", "Scegliere Hilde come alleata principale - conoscenza ed esperienza", "Scegliere Voss come alleato principale - accesso e rimorso", "Non confidarsi con nessuno - non voglio mettere nessuno in pericolo"])
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
    _t(tr, F, "ally_converge_solo", en="I am alone. Like grandmother. But I have her knowledge, her preparation. That has to be enough.", fr="Je suis seule. Comme grand-mère. Mais j'ai son savoir, sa préparation. Cela doit suffire.", es="Estoy sola. Como la abuela. Pero tengo su conocimiento, su preparación. Eso tiene que ser suficiente.", it="Sono sola. Come la nonna. Ma ho il suo sapere, la sua preparazione. Deve bastare.")
    _t(tr, F, "ally_converge_allied", en="I have an ally. Not a miracle, not a guarantee—just one human witness who can pull me back if the thing below tries to pull me under.", fr="J'ai un allié. Quelqu'un qui se tiendra à mes côtés demain soir, quand je devrai affronter ce qui attend en bas.", es="Tengo un aliado. Alguien que estará a mi lado mañana por la noche, cuando tenga que enfrentarme a lo que espera abajo.", it="Ho un alleato. Qualcuno che domani sera sarà al mio fianco, quando dovrò affrontare ciò che aspetta laggiù.")
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
       en="Tomorrow is the day. I will stand above the thinnest stone, sing the chant Hilde taught me, and find out whether the thing below answers in violence... or in words.",
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

    # --- Phase 10 Story-Konsistenz-Fixes ---
    _t(tr, F, "ally_solo",
       en="No one. I will put no one in danger. Not Georg, not Hilde, not Voss. Whatever waits in the chamber - it is between me and the entity. Just the two of us.",
       fr="Personne. Je ne mettrai personne en danger. Ni Georg, ni Hilde, ni Voss. Quoi qu'il attende dans la chambre - c'est entre moi et l'entité. Rien que nous deux.",
       es="Nadie. No pondré a nadie en peligro. Ni a Georg, ni a Hilde, ni a Voss. Lo que sea que espere en la cámara - es entre la entidad y yo. Solo nosotros dos.",
       it="Nessuno. Non metterò nessuno in pericolo. Né Georg, né Hilde, né Voss. Qualunque cosa attenda nella camera - è tra me e l'entità. Solo noi due.")

    _t(tr, F, "ally_solo_2",
       en="Grandmother fought alone for thirty years. She dragged no one down, sacrificed no one, risked no one. If I am her granddaughter, I can do the same.",
       fr="Grand-mère s'est battue seule pendant trente ans. Elle n'a entraîné personne, n'a sacrifié personne, n'a risqué personne. Si je suis sa petite-fille, je peux faire de même.",
       es="La abuela luchó sola durante treinta años. No arrastró a nadie, no sacrificó a nadie, no arriesgó a nadie. Si soy su nieta, puedo hacer lo mismo.",
       it="La nonna ha combattuto da sola per trent'anni. Non ha trascinato nessuno, non ha sacrificato nessuno, non ha rischiato nessuno. Se sono sua nipote, posso fare altrettanto.")

    _t(tr, F, "ally_solo_3",
       en="It is lonely. But loneliness is not a death sentence. I should know that - I am a folklorist, not a soldier. My tool is understanding, not violence. For that, I need no army.",
       fr="C'est solitaire. Mais la solitude n'est pas une condamnation à mort. Je devrais le savoir - je suis folkloriste, pas soldat. Mon outil est la compréhension, pas la violence. Pour cela, je n'ai besoin d'aucune armée.",
       es="Es solitario. Pero la soledad no es una sentencia de muerte. Debería saberlo - soy folklorista, no soldado. Mi herramienta es la comprensión, no la violencia. Para eso, no necesito un ejército.",
       it="È solitario. Ma la solitudine non è una condanna a morte. Dovrei saperlo - sono una folklorista, non una soldatessa. Il mio strumento è la comprensione, non la violenza. Per questo, non ho bisogno di un esercito.")


def _add_act3_reality_breaks(tr):
    F = "res://data/dialogue/act3/reality_breaks.json"

    _t(tr, F, "narration_1", en="Day six. Something is different. When I look out the window, the colors are wrong. The sky is too violet for morning. The shadows fall in the wrong direction.", fr="Sixième jour. Quelque chose est différent. Quand je regarde par là fenêtre, les couleurs ne correspondent pas. Le ciel est trop violet pour le matin. Les ombres tombent dans là mauvaise direction.", es="Día seis. Algo es diferente. Cuando miro por la ventana, los colores no son correctos. El cielo es demasiado violeta para la mañana. Las sombras caen en la dirección equivocada.", it="Sesto giorno. Qualcosa è diverso. Quando guardo fuori dalla finestra, i colori sono sbagliati. Il cielo è troppo violetto per il mattino. Le ombre cadono nella direzione sbagliata.")
    _t(tr, F, "narration_2", en="In the mirror I see myself. But my reflection blinks half a second later than I do.", fr="Dans le miroir, je me vois. Mais mon reflet cligne des yeux une demi-seconde après moi.", es="En el espejo me veo a mí misma. Pero mi reflejo parpadea medio segundo después que yo.", it="Nello specchio vedo me stessa. Ma il mio riflesso sbatte le palpebre mezzo secondo dopo di me.")
    _t(tr, F, "narration_3", en="I turn away. This is what grandmother described: 'The dreams seep upward.' Reality is growing thin.", fr="Je me détourne. C'est ce que grand-mère décrivait : « Les rêves suintent vers le haut. » Là réalité s'amincit.", es="Me doy la vuelta. Esto es lo que la abuela describía: «Los sueños se filtran hacia arriba.» La realidad se vuelve delgada.", it="Mi volto. È quello che la nonna descriveva: 'I sogni filtrano verso l'alto.' La realtà si assottiglia.")
    _t(tr, F, "narration_4", en="The village outside is... wrong. The houses stand at slightly shifted angles, as if someone moved them overnight. The fountain in the square drips upward.", fr="Le village dehors est... faux. Les maisons se dressent à des angles légèrement décalés, comme si quelqu'un les avait déplacées pendant là nuit. Là fontaine sur là place goutte vers le haut.", es="El pueblo afuera está... mal. Las casas se alzan en ángulos ligeramente desplazados, como si alguien las hubiera movido durante la noche. La fuente de la plaza gotea hacia arriba.", it="Il villaggio fuori è... sbagliato. Le case si ergono ad angoli leggermente spostati, come se qualcuno le avesse spostate durante la notte. La fontana nella piazza gocciola verso l'alto.")
    _t(tr, F, "narration_5", en="The villagers go about their business as if nothing were amiss. Only their eyes - all gazing in the same direction. Toward the church.", fr="Les villageois vaquent à leurs occupations comme si de rien n'était. Seuls leurs yeux - tous regardent dans là même direction. Vers l'église.", es="Los aldeanos hacen sus cosas como si nada pasara. Solo sus ojos - todos miran en la misma dirección. Hacia la iglesia.", it="I paesani svolgono le loro faccende come se nulla fosse. Solo i loro occhi - tutti guardano nella stessa direzione. Verso la chiesa.")
    _t(tr, F, "narration_6", en="I must act. Tomorrow night is the thirtieth anniversary of the last Feeding. If the ritual takes place, someone dies. If it doesn't...", fr="Je dois agir. Demain soir marque le trentième anniversaire de la dernière Nourriture. Si le rituel a lieu, quelqu'un meurt. S'il n'a pas lieu...", es="Debo actuar. Mañana por la noche es el trigésimo aniversario de la última Alimentación. Si el ritual se lleva a cabo, alguien muere. Si no se lleva a cabo...", it="Devo agire. Domani sera è il trentesimo anniversario dell'ultima Nutrizione. Se il rituale ha luogo, qualcuno muore. Se non ha luogo...")
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
    _t(tr, F, "journal_reality", en="Day 6: Reality is growing thin. The forest grows, the village distorts, colors are no longer right. Anna says the entity dreams of me - it's afraid. The Feeding is tomorrow night. I must act before then.", fr="Jour 6 : La réalité s'amincit. La forêt grandit, le village se déforme, les couleurs ne sont plus justes. Anna dit que l'entité rêve de moi - elle a peur. La Nourriture est demain soir. Je dois agir avant.", es="Día 6: La realidad se vuelve delgada. El bosque crece, el pueblo se distorsiona, los colores ya no son correctos. Anna dice que la entidad sueña conmigo - tiene miedo. La Alimentación es mañana por la noche. Debo actuar antes.", it="Giorno 6: La realtà si assottiglia. La foresta cresce, il villaggio si deforma, i colori non sono più giusti. Anna dice che l'entità sogna di me - ha paura. La Nutrizione è domani sera. Devo agire prima.", field="content")

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

    # --- Phase 9 Story-Fixes: Anna fear detail ---
    _t(tr, F, "anna_fear_detail_1",
       en="Fear? Of what exactly? That I will destroy it?",
       fr="Peur ? De quoi exactement ? Que je le détruise ?",
       es="¿Miedo? ¿De qué exactamente? ¿De que lo destruya?",
       it="Paura? Di cosa esattamente? Che lo distrugga?")
    _t(tr, F, "anna_fear_detail_2",
       en="No. It is not afraid you will destroy it. It is afraid you will SEE it and... leave.",
       fr="Non. Il n'a pas peur que tu le détruises. Il a peur que tu le VOIES et... que tu partes.",
       es="No. No tiene miedo de que lo destruyas. Tiene miedo de que lo VEAS y... te vayas.",
       it="No. Non ha paura che tu lo distrugga. Ha paura che tu lo VEDA e... te ne vada.")
    _t(tr, F, "anna_fear_detail_3",
       en="Six hundred years alone. And now you are here. What if you leave too?",
       fr="Six cents ans de solitude. Et maintenant tu es là. Et si tu partais aussi ?",
       es="Seiscientos años solo. Y ahora estás aquí. ¿Y si tú también te vas?",
       it="Seicento anni da solo. E ora sei qui. E se anche tu te ne andassi?")
    _t(tr, F, "anna_fear_narration",
       en="I understand it suddenly. The creature did not call me out of hunger. Out of hope. Six hundred years of loneliness, and now someone is here who might listen — and it is terrified that I will run away.",
       fr="Je comprends soudain. La créature ne m'a pas appelée par faim. Par espoir. Six cents ans de solitude, et maintenant quelqu'un est là qui pourrait écouter — et elle est terrifiée à l'idée que je m'enfuie.",
       es="Lo comprendo de repente. La criatura no me llamó por hambre. Por esperanza. Seiscientos años de soledad, y ahora hay alguien que podría escuchar — y está aterrorizada de que yo huya.",
       it="Lo capisco all'improvviso. La creatura non mi ha chiamata per fame. Per speranza. Seicento anni di solitudine, e ora c'è qualcuno che potrebbe ascoltare — ed è terrorizzata che io scappi.")

    # --- Phase 10 Story-Konsistenz-Fixes ---
    _t(tr, F, "anna_coexistence_hint",
       en="It doesn't want to possess. It just doesn't want to be alone. Konrad could have been its friend. But Konrad resisted.",
       fr="Il ne veut pas posséder. Il veut simplement ne pas être seul. Konrad aurait pu être son ami. Mais Konrad a résisté.",
       es="No quiere poseer. Solo no quiere estar solo. Konrad podría haber sido su amigo. Pero Konrad se resistió.",
       it="Non vuole possedere. Vuole solo non essere solo. Konrad avrebbe potuto essere suo amico. Ma Konrad ha resistito.")


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

    # --- Phase 9b: Georg catch-up when otto_hostile ---
    _t(tr, F, "georg_catchup_narration",
       en="Footsteps on the stairs. Heavy, hurried, but familiar. Georg. He made it.",
       fr="Des pas dans l'escalier. Lourds, pressés, mais familiers. Georg. Il a réussi.",
       es="Pasos en la escalera. Pesados, apresurados, pero familiares. Georg. Lo logró.",
       it="Passi sulle scale. Pesanti, frettolosi, ma familiari. Georg. Ce l'ha fatta.")
    _t(tr, F, "georg_catchup_1",
       en="Otto's men are not so brave when it gets dark. They ran when the church started shaking.",
       fr="Les hommes d'Otto ne sont pas si courageux quand il fait noir. Ils se sont enfuis quand l'église a commencé à trembler.",
       es="Los hombres de Otto no son tan valientes cuando oscurece. Huyeron cuando la iglesia comenzó a temblar.",
       it="Gli uomini di Otto non sono così coraggiosi quando si fa buio. Sono scappati quando la chiesa ha iniziato a tremare.")
    _t(tr, F, "elise_catchup_1",
       en="Georg! I thought you —",
       fr="Georg ! Je croyais que tu —",
       es="¡Georg! Pensé que tú —",
       it="Georg! Pensavo che tu —")
    _t(tr, F, "georg_catchup_2",
       en="I promised Margarethe to watch over you. A blacksmith keeps his word.",
       fr="J'ai promis à Margarethe de veiller sur toi. Un forgeron tient parole.",
       es="Le prometí a Margarethe cuidarte. Un herrero cumple su palabra.",
       it="Ho promesso a Margarethe di vegliare su di te. Un fabbro mantiene la parola.")




def _add_act3_preparation(tr):
    F = "res://data/dialogue/act3/preparation.json"

    # --- Phase 11: Return from descent ---
    _t(tr, F, "narration_return",
       en="I climb the stairs, back through the church, out into the night. The fresh air burns in my lungs. The sky above Graubach is clear, but the stars look wrong. Too close. Too bright.",
       fr="Je monte l'escalier, retour à travers l'église, dehors dans la nuit. L'air frais brûle dans mes poumons. Le ciel au-dessus de Graubach est clair, mais les étoiles semblent fausses. Trop proches. Trop vives.",
       es="Subo las escaleras, de vuelta a través de la iglesia, hacia la noche. El aire fresco quema en mis pulmones. El cielo sobre Graubach está despejado, pero las estrellas se ven mal. Demasiado cerca. Demasiado brillantes.",
       it="Salgo per le scale, di nuovo attraverso la chiesa, fuori nella notte. L'aria fresca brucia nei miei polmoni. Il cielo sopra Graubach è sereno, ma le stelle sembrano sbagliate. Troppo vicine. Troppo luminose.")
    _t(tr, F, "narration_1", en="The last night before the ritual. I sit at my grandmother's table, her journal open, her candle burning. How often did she sit here?", fr="Là dernière nuit avant le rituel. Je suis assise à là table de mà grand-mère, son journal ouvert, sà bougie allumée. Combien de fois s'est-elle assise ici ?", es="La última noche antes del ritual. Estoy sentada a la mesa de mi abuela, su diario abierto, su vela encendida. ¿Cuántas veces se habrá sentado aquí?", it="L'ultima notte prima del rituale. Siedo al tavolo di mia nonna, il suo diario aperto, la sua candela accesa. Quante volte si è seduta qui?")
    _t(tr, F, "narration_2", en="Outside, the sky is wrong. Stars that should not exist, in patterns reminiscent of spirals. The moon is too large and too close.", fr="Dehors, le ciel est faux. Des étoiles qui ne devraient pas exister, dans des motifs qui rappellent des spirales. Là lune est trop grande et trop proche.", es="Afuera, el cielo está mal. Estrellas que no deberían existir, en patrones que recuerdan a espirales. La luna es demasiado grande y está demasiado cerca.", it="Fuori, il cielo è sbagliato. Stelle che non dovrebbero esistere, in schemi che ricordano spirali. La luna è troppo grande è troppo vicina.")
    # --- Phase 9b: No-journal alternative path ---
    _t(tr, F, "narration_no_journal",
       en="I have no journal, no records. Only what the others have told me. Hilde, Georg, Voss — each gave me a piece of the truth. Now I must piece them together.",
       fr="Je n'ai ni journal, ni notes. Seulement ce que les autres m'ont dit. Hilde, Georg, Voss — chacun m'a donné un morceau de la vérité. Maintenant je dois les assembler.",
       es="No tengo diario, ni registros. Solo lo que los demás me han contado. Hilde, Georg, Voss — cada uno me dio un pedazo de la verdad. Ahora debo unir las piezas.",
       it="Non ho un diario, nessun appunto. Solo ciò che gli altri mi hanno detto. Hilde, Georg, Voss — ognuno mi ha dato un pezzo della verità. Ora devo metterli insieme.")
    _t(tr, F, "narration_no_journal_2",
       en="Grandmother, what did you know? What would you have told me if you were still here? I must do it without your words. But perhaps she left me enough — in the people she knew.",
       fr="Grand-mère, que savais-tu ? Que m'aurais-tu dit si tu étais encore là ? Je dois y arriver sans tes mots. Mais peut-être m'a-t-elle laissé assez — dans les gens qu'elle connaissait.",
       es="Abuela, ¿qué sabías? ¿Qué me habrías dicho si aún estuvieras aquí? Debo hacerlo sin tus palabras. Pero quizás me dejó suficiente — en la gente que conocía.",
       it="Nonna, cosa sapevi? Cosa mi avresti detto se fossi ancora qui? Devo farcela senza le tue parole. Ma forse mi ha lasciato abbastanza — nelle persone che conosceva.")
    _t(tr, F, "narration_3", en="I read my grandmother's final entries once more. The last pages, written in the days before her death.", fr="Je relis les dernières entrées du journal de mà grand-mère. Les dernières pages, écrites dans les jours précédant sà mort.", es="Releo las últimas entradas del diario de mi abuela. Las últimas páginas, escritas en los días antes de su muerte.", it="Rileggo le ultime annotazioni di mia nonna. Le ultime pagine, scritte nei giorni prima della sua morte.")
    _t(tr, F, "narration_journal_1", en="'I am too old. My body is failing. But Elise will come. The entity shows it to me in its dreams — not as a threat, as a prophecy.'", fr="« Je suis trop vieille. Mon corps me lâche. Mais Elise viendra. L'entité me le montre dans ses rêves — pas comme une menace, comme une prophétie. »", es="'Soy demasiado vieja. Mi cuerpo se rinde. Pero Elise vendrá. La entidad me lo muestra en sus sueños — no como amenaza, sino como profecía.'", it="'Sono troppo vecchia. Il mio corpo cede. Ma Elise verrà. L'entità me lo mostra nei suoi sogni — non come minaccia, come profezia.'")
    _t(tr, F, "narration_journal_2", en="'She has my blood. She has my will. And she has something I never had: the ability to accept the unknown without fearing it.'", fr="« Elle à mon sang. Elle à mà volonté. Et elle à quelque chose que je n'ai jamais eu : là capacité d'accepter l'inconnu sans le craindre. »", es="'Tiene mi sangre. Tiene mi voluntad. Y tiene algo que yo nunca tuve: la capacidad de aceptar lo desconocido sin temerlo.'", it="'Ha il mio sangue. Ha la mia volontà. È ha qualcosa che io non ho mai avuto: la capacità di accettare l'ignoto senza temerlo.'")
    _t(tr, F, "narration_journal_4", en="'The ritual has many possible outcomes. The chant can bind, liberate, open, or destroy. And some paths only emerge in the moment itself.'", fr="« Le rituel a de nombreuses issues possibles. Le chant peut lier, libérer, ouvrir ou détruire. Et certains chemins n'apparaissent qu'au moment même. »", es="'El ritual tiene muchos desenlaces posibles. El canto puede atar, liberar, abrir o destruir. Y algunos caminos solo surgen en el momento mismo.'", it="'Il rituale ha molti esiti possibili. Il canto può legare, liberare, aprire o distruggere. E alcuni percorsi nascono solo nel momento stesso.'")
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
    # --- Phase 11: Journal flag_check split ---
    _t(tr, F, "narration_preparation_journal",
       en="I lay out the things I need: Georg's key. Hilde's amulet and herbs. Grandmother's journal. The candle that never goes out.",
       fr="Je dispose les choses dont j'ai besoin : la clé de Georg. L'amulette et les herbes de Hilde. Le journal de grand-mère. La bougie qui ne s'éteint jamais.",
       es="Dispongo las cosas que necesito: la llave de Georg. El amuleto y las hierbas de Hilde. El diario de la abuela. La vela que nunca se apaga.",
       it="Dispongo le cose di cui ho bisogno: la chiave di Georg. L'amuleto e le erbe di Hilde. Il diario della nonna. La candela che non si spegne mai.")
    _t(tr, F, "narration_preparation_nojournal",
       en="I lay out the things I need: Georg's key. Hilde's amulet and herbs. The candle that never goes out.",
       fr="Je dispose les choses dont j'ai besoin : la clé de Georg. L'amulette et les herbes de Hilde. La bougie qui ne s'éteint jamais.",
       es="Dispongo las cosas que necesito: la llave de Georg. El amuleto y las hierbas de Hilde. La vela que nunca se apaga.",
       it="Dispongo le cose di cui ho bisogno: la chiave di Georg. L'amuleto e le erbe di Hilde. La candela che non si spegne mai.")
    _t(tr, F, "narration_ready", en="Hilde's amulet warms my hand. The stone pulses in the same rhythm as the floor in the chamber. Two hearts beating in time.", fr="L'amulette de Hilde réchauffe mà main. Là pierre pulse au même rythme que le sol de là chambre. Deux cœurs qui battent à l'unisson.", es="El amuleto de Hilde calienta mi mano. La piedra pulsa al mismo ritmo que el suelo de la cámara. Dos corazones latiendo al compás.", it="L'amuleto di Hilde scalda la mia mano. La pietra pulsa allo stesso ritmo del pavimento della camera. Due cuori che battono all'unisono.")
    _t(tr, F, "narration_unprepared", en="I am missing things. But time is running out. I will have to work with what I have. Courage and desperation will have to suffice.", fr="Il me manque des choses. Mais le temps presse. Je devrai faire avec ce que j'ai. Le courage et le désespoir devront suffire.", es="Me faltan cosas. Pero el tiempo se agota. Tendré que trabajar con lo que tengo. El coraje y la desesperación tendrán que bastar.", it="Mi mancano delle cose. Ma il tempo stringe. Dovrò lavorare con quello che ho. Coraggio è disperazione dovranno bastare.")
    _t(tr, F, "narration_dawn_2", en="Dawn breaks. It is red. Blood-red. Not the sunrise — the sky itself seems to bleed.", fr="L'aube se lève. Elle est rouge. Rouge sang. Pas le lever du soleil — le ciel lui-même semble saigner.", es="Amanece. Es rojo. Rojo sangre. No es el amanecer — el cielo mismo parece sangrar.", it="L'alba sorge. È rossa. Rosso sangue. Non l'alba — il cielo stesso sembra sanguinare.")
    _t(tr, F, "narration_dawn_3", en="Today the story of Graubach ends. Six hundred years of tradition, six hundred years of fear, six hundred years of blood. Today I decide how.", fr="Aujourd'hui, l'histoire de Graubach prend fin. Six cents ans de tradition, six cents ans de peur, six cents ans de sang. Aujourd'hui, je décide comment.", es="Hoy termina la historia de Graubach. Seiscientos años de tradición, seiscientos años de miedo, seiscientos años de sangre. Hoy decido cómo.", it="Oggi la storia di Graubach finisce. Seicento anni di tradizione, seicento anni di paura, seicento anni di sangue. Oggi decido come.")
    _t(tr, F, "journal_preparation", en="The Last Night", fr="Là Dernière Nuit", es="La última noche", it="L'ultima notte", field="title")
    _t(tr, F, "journal_preparation", en="Read Grandmother's last letter. She apologized - and gave me courage. The ritual has many possible outcomes. I have chosen my path. Written my own letter, just in case. The morning is blood-red. It is time.", fr="Lu la dernière lettre de grand-mère. Elle s'est excusée - et m'a donné du courage. Le rituel a de nombreuses issues possibles. J'ai choisi mon chemin. Écrit ma propre lettre, au cas où. Le matin est rouge sang. C'est le moment.", es="Leí la última carta de la abuela. Se disculpó - y me dio valor. El ritual tiene muchos desenlaces posibles. He elegido mi camino. Escribí mi propia carta, por si acaso. La mañana es roja como la sangre. Es el momento.", it="Letta l'ultima lettera della nonna. Si è scusata - e mi ha dato coraggio. Il rituale ha molti esiti possibili. Ho scelto la mia strada. Scritto una mia lettera, per ogni evenienza. Il mattino è rosso sangue. È giunto il momento.", field="content")
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
       en="Bind, understand, destroy, negotiate - and whatever happens in the moment itself. Each path has its price.",
       fr="Lier, comprendre, détruire, négocier - et ce qui advient dans le moment même. Chaque chemin a son prix.",
       es="Atar, comprender, destruir, negociar - y lo que suceda en el momento mismo. Cada camino tiene su precio.",
       it="Legare, comprendere, distruggere, negoziare - e qualunque cosa accada nel momento stesso. Ogni percorso ha il suo prezzo.")
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
       en="Your grandmother took my hands, just before she went. And said: 'Elise will be stronger than me.' You are more like her than you think. And the entity knows it.",
       fr="Ta grand-mère a pris mes mains, juste avant de partir. Et a dit : « Elise sera plus forte que moi. » Tu lui ressembles plus que tu ne le penses. Et l'entité le sait.",
       es="Tu abuela tomó mis manos, justo antes de irse. Y dijo: 'Elise será más fuerte que yo.' Te pareces a ella más de lo que crees. Y la entidad lo sabe.",
       it="Tua nonna mi prese le mani, poco prima di andarsene. E disse: 'Elise sarà più forte di me.' Le assomigli più di quanto pensi. E l'entità lo sa.")
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
    # narration_approach_think is now a flag_check (Phase 12)
    _t(tr, F, "narration_approach_think_journal",
       en="I close the journal. My hands are calm. Strangely calm for someone who will face an ancient entity tomorrow.",
       fr="Je ferme le journal. Mes mains sont calmes. Étrangement calmes pour quelqu'un qui affrontera une entité ancestrale demain.",
       es="Cierro el diario. Mis manos están tranquilas. Extrañamente tranquilas para alguien que mañana se enfrentará a una entidad ancestral.",
       it="Chiudo il diario. Le mie mani sono calme. Stranamente calme per qualcuno che domani affronterà un'entità ancestrale.")
    _t(tr, F, "narration_approach_think_nojournal",
       en="I lay my hands flat on the table. They are calm. Strangely calm for someone who will face an ancient entity tomorrow.",
       fr="Je pose les mains à plat sur la table. Elles sont calmes. Étrangement calmes pour quelqu'un qui affrontera une entité ancestrale demain.",
       es="Pongo las manos planas sobre la mesa. Están tranquilas. Extrañamente tranquilas para alguien que mañana se enfrentará a una entidad ancestral.",
       it="Appoggio le mani sul tavolo. Sono calme. Stranamente calme per qualcuno che domani affronterà un'entità ancestrale.")
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
    # --- Phase 12: No-letter dialogue alternatives ---
    _t(tr, F, "elise_georg_visit_1_noletter",
       en="Please. I... I'm sitting here staring at the walls. What will happen tomorrow, Georg?",
       fr="Je t'en prie. Je... je suis assise ici à fixer les murs. Que va-t-il se passer demain, Georg ?",
       es="Por favor. Yo... estoy sentada aquí mirando las paredes. ¿Qué pasará mañana, Georg?",
       it="Prego. Io... sto qui seduta a fissare le pareti. Cosa succederà domani, Georg?")
    _t(tr, F, "georg_visit_2_noletter",
       en="Your grandmother would have known what to say to you. I'm just an old man with a lantern. But I'm here.",
       fr="Ta grand-mère aurait su quoi te dire. Je ne suis qu'un vieil homme avec une lanterne. Mais je suis là.",
       es="Tu abuela habría sabido qué decirte. Solo soy un viejo con una linterna. Pero estoy aquí.",
       it="Tua nonna avrebbe saputo cosa dirti. Sono solo un vecchio con una lanterna. Ma sono qui.")
    _t(tr, F, "elise_hilde_visit_1_noletter",
       en="I wish Grandmother had left me something. Instructions. Anything.",
       fr="J'aurais aimé que grand-mère me laisse quelque chose. Des instructions. N'importe quoi.",
       es="Ojalá la abuela me hubiera dejado algo. Instrucciones. Lo que sea.",
       it="Vorrei che la nonna mi avesse lasciato qualcosa. Istruzioni. Qualsiasi cosa.")
    _t(tr, F, "hilde_visit_2_noletter",
       en="Margarethe left you more than you think. Not in ink and paper. In the people here. In me.",
       fr="Margarethe t'a laissé plus que tu ne le penses. Pas dans l'encre et le papier. Dans les gens ici. En moi.",
       es="Margarethe te dejó más de lo que crees. No en tinta y papel. En la gente de aquí. En mí.",
       it="Margarethe ti ha lasciato più di quanto pensi. Non in inchiostro e carta. Nelle persone qui. In me.")


