"""Act 1 translations: arrival, first_night, village_exploration, smithy_evening."""

from .common import _t, _tc


def _add_act1_arrival(tr):
    """Act 1 - Grandmother's House"""
    F = "res://data/dialogue/act1/arrival.json"
    _t(tr,F,"narration_1", en="The inside of grandmother's house has barely changed. The same dark wooden furniture, the same crocheted blankets.", fr="L'intérieur de là maison de grand-mère n'à guère changé. Les mêmes meubles en bois sombre, les mêmes couvertures au crochet.", es="El interior de la casa de la abuela apenas ha cambiado. Los mismos muebles de madera oscura, las mismas mantas de ganchillo.", it="L'interno della casa della nonna è a malapena cambiato. Gli stessi mobili di legno scuro, le stesse coperte all'uncinetto.")
    _t(tr,F,"narration_2", en="But the smell is different. Beneath the familiar scent of chamomile tea and beeswax lies something sweet. Something I can't place.", fr="Mais l'odeur est différente. Sous le parfum familier de camomille et de cire d'abeille se cache quelque chose de douceâtre. Quelque chose que je n'arrive pas à identifier.", es="Pero el olor es diferente. Bajo el aroma familiar de té de manzanilla y cera de abeja hay algo dulzón. Algo que no puedo identificar.", it="Ma l'odore è diverso. Sotto il familiare profumo di camomilla è cera d'api c'è qualcosa di dolciastro. Qualcosa che non riesco a identificare.")
    _t(tr,F,"narration_3", en="In the bedroom she lies. Grandmother Margarethe. The blanket is pulled up to her chin, as if someone carefully tucked her in.", fr="Dans là chambre, elle repose. Grand-mère Margarethe. Là couverture est tirée jusqu'au menton, comme si quelqu'un l'avait soigneusement bordée.", es="En el dormitorio yace ella. La abuela Margarethe. La manta está subida hasta la barbilla, como si alguien la hubiera arropado con cuidado.", it="Nella camera da letto giace lei. Nonna Margarethe. La coperta è tirata fino al mento, come se qualcuno l'avesse rimboccata con cura.")
    _t(tr,F,"narration_4", en="Her eyes are closed. Her mouth smiles faintly. But her skin has the color of old parchment, and when I touch her hand, it's cold as stone.", fr="Ses yeux sont fermés. Sà bouche esquisse un léger sourire. Mais sà peau à là couleur du vieux parchemin, et quand je touche sà main, elle est froide comme là pierre.", es="Sus ojos están cerrados. Su boca esboza una leve sonrisa. Pero su piel tiene el color del pergamino viejo, y cuando toco su mano, está fría como la piedra.", it="I suoi occhi sono chiusi. La sua bocca sorride lievemente. Ma la sua pelle ha il colore della vecchia pergamena, è quando tocco la sua mano, è fredda come la pietra.")
    _t(tr,F,"narration_4b", en="That smile. It doesn't look like the peaceful death of an old woman. It looks like the smile of someone who finished something. Something important.", fr="Ce sourire. Il ne ressemble pas à la mort paisible d'une vieille femme. Il ressemble au sourire de quelqu'un qui a terminé quelque chose. Quelque chose d'important.", es="Esa sonrisa. No parece la muerte pacífica de una anciana. Parece la sonrisa de alguien que terminó algo. Algo importante.", it="Quel sorriso. Non sembra la morte pacifica di una vecchia. Sembra il sorriso di chi ha finito qualcosa. Qualcosa di importante.")
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
       en="Your grandmother knew both ways. She waited and prepared for thirty years. She wanted to do it differently this time — without bloodshed.",
       fr="Ta grand-mère connaissait les deux voies. Elle a attendu et s'est préparée pendant trente ans. Elle voulait faire autrement cette fois — sans effusion de sang.",
       es="Tu abuela conocía ambos caminos. Esperó y se preparó durante treinta años. Quería hacerlo diferente esta vez — sin derramamiento de sangre.",
       it="Tua nonna conosceva entrambe le vie. Ha aspettato e si è preparata per trent'anni. Voleva farlo diversamente questa volta — senza spargimento di sangue.")
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
       en="At the blackboard stands a man, explaining something. The children call him 'Herr Müller'. Konrad Müller — the man from last night. In daylight he looks... normal. Friendly. Even charismatic.",
       fr="Au tableau se tient un homme qui explique quelque chose. Les enfants l'appellent « Herr Müller ». Konrad Müller — l'homme de la nuit dernière. À la lumière du jour, il a l'air... normal. Amical. Même charismatique.",
       es="Ante la pizarra hay un hombre explicando algo. Los niños lo llaman 'Herr Müller'. Konrad Müller — el hombre de anoche. A la luz del día parece... normal. Amable. Incluso carismático.",
       it="Alla lavagna c'è un uomo che spiega qualcosa. I bambini lo chiamano 'Herr Müller'. Konrad Müller — l'uomo di ieri notte. Alla luce del giorno sembra... normale. Cordiale. Persino carismatico.")
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
       en="In the early afternoon I go to the fountain. A blind old woman sits on the stone bench beside it, humming softly to herself. The melody seems familiar - the singing I heard last night. She turns her head in my direction, as if she can sense me.",
       fr="En début d'après-midi, je vais au puits. Une vieille femme aveugle est assise sur le banc de pierre à côté, fredonnant doucement. La mélodie me semble familière - le chant que j'ai entendu la nuit dernière. Elle tourne la tête dans ma direction, comme si elle pouvait me sentir.",
       es="A primera hora de la tarde voy a la fuente. Una anciana ciega está sentada en el banco de piedra, tarareando suavemente. La melodía me resulta familiar - el canto que escuché anoche. Gira la cabeza en mi dirección, como si pudiera sentirme.",
       it="Nel primo pomeriggio vado alla fontana. Una vecchia cieca è seduta sulla panchina di pietra accanto, canticchiando piano. La melodia mi sembra familiare - il canto che ho sentito la notte scorsa. Gira la testa nella mia direzione, come se potesse percepirmi.")
    _t(tr, F, "converge_1b",
       en="Before I can speak to her, she stands and walks away. Slowly, surely, as if she knows every stone. Georg is already waiting at the fountain. He looks as though he, too, did not sleep.",
       fr="Avant que je puisse lui parler, elle se lève et s'en va. Lentement, sûrement, comme si elle connaissait chaque pierre. Georg attend déjà au puits. Il a l'air de ne pas avoir dormi non plus.",
       es="Antes de que pueda hablarle, se levanta y se va. Lentamente, con seguridad, como si conociera cada piedra. Georg ya espera en la fuente. Parece como si él tampoco hubiera dormido.",
       it="Prima che possa parlarle, si alza e se ne va. Lentamente, sicura, come se conoscesse ogni pietra. Georg aspetta già alla fontana. Sembra che nemmeno lui abbia dormito.")
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

    # --- Phase 9 Story-Fixes: Otto motivation ---
    _t(tr, F, "otto_motivation_1",
       en="On the way back I think about the mayor. About his self-assurance. About the weight of his words — not like a man who threatens, but like one who is absolutely convinced.",
       fr="Sur le chemin du retour, je pense au maire. À son assurance. Au poids de ses mots — pas comme un homme qui menace, mais comme quelqu'un qui est absolument convaincu.",
       es="De vuelta pienso en el alcalde. En su seguridad. En el peso de sus palabras — no como un hombre que amenaza, sino como alguien que está absolutamente convencido.",
       it="Sulla via del ritorno penso al sindaco. Alla sua sicurezza. Al peso delle sue parole — non come un uomo che minaccia, ma come uno che è assolutamente convinto.")
    _t(tr, F, "otto_motivation_2",
       en="Georg once told me that Otto's father was mayor in 1893. And his father before him. The Reinhardts have ruled Graubach for generations — and profited from it.",
       fr="Georg m'a dit un jour que le père d'Otto était maire en 1893. Et son père avant lui. Les Reinhardt gouvernent Graubach depuis des générations — et en profitent.",
       es="Georg me contó una vez que el padre de Otto fue alcalde en 1893. Y su padre antes que él. Los Reinhardt gobiernan Graubach desde hace generaciones — y se benefician de ello.",
       it="Georg una volta mi ha detto che il padre di Otto era sindaco nel 1893. E suo padre prima di lui. I Reinhardt governano Graubach da generazioni — e ne traggono profitto.")
    _t(tr, F, "otto_motivation_3",
       en="The forest protects their land. The harvests on the Reinhardt fields are unnaturally good, even in bad years. The family stays healthy while other children die of fever.",
       fr="La forêt protège leurs terres. Les récoltes sur les champs des Reinhardt sont anormalement bonnes, même les mauvaises années. La famille reste en bonne santé tandis que d'autres enfants meurent de fièvre.",
       es="El bosque protege sus tierras. Las cosechas en los campos de los Reinhardt son antinaturalmente buenas, incluso en años malos. La familia se mantiene sana mientras otros niños mueren de fiebre.",
       it="Il bosco protegge le loro terre. I raccolti sui campi dei Reinhardt sono innaturalmente buoni, anche nelle annate cattive. La famiglia resta in salute mentre altri bambini muoiono di febbre.")
    _t(tr, F, "otto_motivation_4",
       en="Otto does not act only from tradition. He acts from self-interest. And the worst part: he truly believes in it. He is convinced that the sacrifices are necessary. That he is doing the right thing.",
       fr="Otto n'agit pas seulement par tradition. Il agit par intérêt personnel. Et le pire : il y croit vraiment. Il est convaincu que les sacrifices sont nécessaires. Qu'il fait ce qui est juste.",
       es="Otto no actúa solo por tradición. Actúa por interés propio. Y lo peor: realmente cree en ello. Está convencido de que los sacrificios son necesarios. De que hace lo correcto.",
       it="Otto non agisce solo per tradizione. Agisce per interesse personale. E la cosa peggiore: ci crede davvero. È convinto che i sacrifici siano necessari. Che stia facendo la cosa giusta.")
    _t(tr, F, "otto_motivation_5",
       en="A madman would be easier. A madman can be exposed. But a true believer? A true believer must be broken.",
       fr="Un fou serait plus facile. On peut démasquer un fou. Mais un croyant ? Un croyant, il faut le briser.",
       es="Un loco sería más fácil. A un loco se le puede desenmascarar. Pero a un creyente? A un creyente hay que quebrantarlo.",
       it="Un pazzo sarebbe più facile. Un pazzo lo si può smascherare. Ma un credente? Un credente bisogna spezzarlo.")




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

    _t(tr, F, "elise_tradition_1_hilde",
       en="Tradition? What kind of tradition? Hilde spoke of it too.",
       fr="Tradition ? Quelle tradition ? Hilde en a parlé aussi.",
       es="¿Tradición? ¿Qué clase de tradición? Hilde también habló de ello.",
       it="Tradizione? Che tipo di tradizione? Anche Hilde ne ha parlato.")
    _t(tr, F, "elise_tradition_1_nohilde",
       en="Tradition? What kind of tradition? Grandmother hinted at something like that in her letter.",
       fr="Tradition ? Quelle tradition ? Grand-mère a fait allusion à quelque chose comme ça dans sa lettre.",
       es="¿Tradición? ¿Qué clase de tradición? La abuela insinuó algo así en su carta.",
       it="Tradizione? Che tipo di tradizione? La nonna ha accennato a qualcosa del genere nella sua lettera.")

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

    # --- Phase 9 Story-Fixes: Forest logic ---
    _t(tr, F, "georg_wald_1",
       en="But how? The postman comes through. Merchants travel through. Why does the forest hold me but not others?",
       fr="Mais comment ? Le facteur passe bien. Les marchands voyagent. Pourquoi la forêt me retient-elle, mais pas les autres ?",
       es="Pero ¿cómo? El cartero viene. Los comerciantes viajan. ¿Por qué el bosque me retiene a mí pero no a los demás?",
       it="Ma come? Il postino passa. I mercanti viaggiano. Perché il bosco trattiene me ma non gli altri?")
    _t(tr, F, "georg_wald_2",
       en="The forest lets most people pass. Merchants, travelers, even the postman. But those whose names are in the book... it does not let them go.",
       fr="La forêt laisse passer la plupart des gens. Marchands, voyageurs, même le facteur. Mais ceux dont le nom est dans le livre... elle ne les laisse pas partir.",
       es="El bosque deja pasar a la mayoría. Comerciantes, viajeros, incluso al cartero. Pero a quienes tienen su nombre en el libro... no los deja ir.",
       it="Il bosco lascia passare la maggior parte della gente. Mercanti, viaggiatori, persino il postino. Ma quelli il cui nome è nel libro... non li lascia andare.")
    _t(tr, F, "georg_wald_3",
       en="That is why I cannot flee.",
       fr="C'est pour ça que je ne peux pas fuir.",
       es="Por eso no puedo huir.",
       it="Per questo non posso fuggire.")
    _t(tr, F, "georg_wald_4",
       en="Your grandmother tried to leave the village for thirty years. Once. Just a single time. The forest led her in circles for three days until she gave up.",
       fr="Ta grand-mère a essayé de quitter le village pendant trente ans. Une fois. Une seule fois. La forêt l'a fait tourner en rond pendant trois jours, jusqu'à ce qu'elle abandonne.",
       es="Tu abuela intentó salir del pueblo durante treinta años. Una vez. Una sola vez. El bosque la hizo caminar en círculos durante tres días hasta que se rindió.",
       it="Tua nonna ha cercato di lasciare il villaggio per trent'anni. Una volta. Una sola volta. Il bosco l'ha fatta camminare in cerchio per tre giorni, finché non ha rinunciato.")


