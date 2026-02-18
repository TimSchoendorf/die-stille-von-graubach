"""Act 4 translations: ritual_night and all 6 endings."""

from .common import _t, _tc


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

    _t(tr, F, "narration_3_journal",
       en="Georg's key opened the last door. Hilde's herbs burn in a bowl beside me, their smoke rising in spirals. Grandmother's journal lies open.",
       fr="La clé de Georg a ouvert la dernière porte. Les herbes de Hilde brûlent dans un bol à côté de moi, leur fumée s'élève en spirales. Le journal de grand-mère est ouvert.",
       es="La llave de Georg abrió la última puerta. Las hierbas de Hilde arden en un cuenco junto a mí, su humo asciende en espirales. El diario de la abuela está abierto.",
       it="La chiave di Georg ha aperto l'ultima porta. Le erbe di Hilde bruciano in una ciotola accanto a me, il loro fumo sale a spirale. Il diario della nonna è aperto.")

    _t(tr, F, "narration_4_journal",
       en="Grandmother's letter in my breast pocket. Hilde's amulet around my neck. Everything that connects me to the living.",
       fr="La lettre de grand-mère dans ma poche de poitrine. L'amulette de Hilde autour de mon cou. Tout ce qui me relie aux vivants.",
       es="La carta de la abuela en mi bolsillo del pecho. El amuleto de Hilde alrededor de mi cuello. Todo lo que me conecta con los vivos.",
       it="La lettera della nonna nella tasca del petto. L'amuleto di Hilde al collo. Tutto ciò che mi lega ai vivi.")

    _t(tr, F, "narration_3_nojournal",
       en="Georg's key opened the last door. Hilde's herbs burn in a bowl beside me, their smoke rising in spirals.",
       fr="La clé de Georg a ouvert la dernière porte. Les herbes de Hilde brûlent dans un bol à côté de moi, leur fumée s'élève en spirales.",
       es="La llave de Georg abrió la última puerta. Las hierbas de Hilde arden en un cuenco junto a mí, su humo asciende en espirales.",
       it="La chiave di Georg ha aperto l'ultima porta. Le erbe di Hilde bruciano in una ciotola accanto a me, il loro fumo sale a spirale.")

    _t(tr, F, "narration_4_nojournal",
       en="Hilde's amulet around my neck. My own letter in my pocket. Everything that connects me to the living.",
       fr="L'amulette de Hilde autour de mon cou. Ma propre lettre dans ma poche. Tout ce qui me relie aux vivants.",
       es="El amuleto de Hilde alrededor de mi cuello. Mi propia carta en el bolsillo. Todo lo que me conecta con los vivos.",
       it="L'amuleto di Hilde al collo. La mia lettera in tasca. Tutto ciò che mi lega ai vivi.")

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
       en="What do you really want? Not sacrifice. Not blood. Say it plainly—what do you need from us?",
       fr="Que veux-tu vraiment ? Pas des sacrifices. Pas du sang. Que VEUX-tu ?",
       es="¿Qué quieres realmente? No sacrificios. No sangre. ¿Qué QUIERES?",
       it="Cosa vuoi davvero? Non sacrifici. Non sangue. Cosa VUOI?")

    _t(tr, F, "narration_creature_speak_7",
       en="FOR SOMEONE TO STAY WITHOUT DYING. TO RETURN BY CHOICE, AND LEAVE BY CHOICE. SIX HUNDRED YEARS AND NOBODY EVER ASKED.",
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
       en="It is waiting for my answer. The oldest being beneath these mountains is holding its breath for the terms of a conversation no one ever offered.",
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
       fr="Le journal de grand-mère m'a préparée. Les symboles, l'histoire, la connexion. J'en comprends assez pour poser les bonnes questions.",
       es="El diario de la abuela me ha preparado. Los símbolos, la historia, la conexión. Entiendo lo suficiente para hacer las preguntas correctas.",
       it="Il diario della nonna mi ha preparata. I simboli, la storia, la connessione. Capisco abbastanza per fare le domande giuste.")

    _t(tr, F, "understand_ready_books",
       en="My books have prepared me - differently from the journal, but the academic texts on pre-Christian rituals give me enough foundation to ask the right questions.",
       fr="Mes livres m'ont préparée - différemment du journal, mais les textes académiques sur les rituels préchrétiens me donnent assez de bases pour poser les bonnes questions.",
       es="Mis libros me han preparado - de forma diferente al diario, pero los textos académicos sobre rituales precristianos me dan suficiente base para hacer las preguntas correctas.",
       it="I miei libri mi hanno preparata - diversamente dal diario, ma i testi accademici sui rituali precristiani mi danno abbastanza basi per fare le domande giuste.")

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
       en="I propose a deal. No more sacrifices. Never again. In return, we offer what was never offered in six hundred years: chosen presence, explicit consent, and no death.",
       fr="Je propose un marché. Plus de sacrifices. Plus jamais. En échange... en échange, je t'offre quelque chose que tu n'as jamais eu en six cents ans.",
       es="Propongo un trato. No más sacrificios. Nunca más. A cambio... a cambio te ofrezco algo que nunca tuviste en seiscientos años.",
       it="Propongo un accordo. Niente più sacrifici. Mai più. In cambio... in cambio ti offro qualcosa che non hai mai avuto in seicento anni.")

    _t(tr, F, "narration_pact_creature",
       en="HUMANS BREAK PROMISES. WHY SHOULD I BELIEVE YOU?",
       fr="LES HUMAINS BRISENT LEURS PROMESSES. POURQUOI DEVRAIS-JE TE CROIRE ?",
       es="LOS HUMANOS ROMPEN SUS PROMESAS. ¿POR QUÉ DEBERÍA CREERTE?",
       it="GLI UMANI INFRANGONO LE PROMESSE. PERCHÉ DOVREI CREDERTI?")

    _t(tr, F, "elise_pact_2",
       en="My grandmother kept her promise for thirty years—month after month, chant after chant. Tell me one time she lied to you.",
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

    # --- Destroy partial success (high courage) ---
    _t(tr, F, "destroy_partial_success",
       en="But something is there. A crack. Tiny, barely perceptible, but REAL. My attack did not kill the entity - but it HURT it. For the first time in six hundred years.",
       fr="Mais il y a quelque chose. Une fissure. Minuscule, à peine perceptible, mais RÉELLE. Mon attaque n'a pas tué l'entité - mais elle l'a BLESSÉE. Pour la première fois en six cents ans.",
       es="Pero hay algo. Una grieta. Diminuta, apenas perceptible, pero REAL. Mi ataque no mató a la entidad - pero la HIRIÓ. Por primera vez en seiscientos años.",
       it="Ma c'è qualcosa. Una crepa. Minuscola, appena percettibile, ma REALE. Il mio attacco non ha ucciso l'entità - ma l'ha FERITA. Per la prima volta in seicento anni.")

    _t(tr, F, "destroy_partial_2",
       en="STOP. STOP. YOU... YOU CAN HURT ME. NO ONE HAS EVER BEEN ABLE TO DO THAT.",
       fr="ARRÊTE. ARRÊTE. TU... TU PEUX ME BLESSER. PERSONNE N'A JAMAIS PU FAIRE ÇA.",
       es="DETENTE. DETENTE. TÚ... PUEDES HACERME DAÑO. NADIE HABÍA PODIDO HACER ESO.",
       it="FERMATI. FERMATI. TU... PUOI FARMI DEL MALE. NESSUNO È MAI RIUSCITO A FARLO.")

    _t(tr, F, "destroy_partial_3",
       en="It is afraid. The ancient entity beneath the stone is AFRAID. Of me. The realization hits me like a blow.",
       fr="Elle a peur. L'ancienne entité sous la pierre a PEUR. De moi. La réalisation me frappe comme un coup.",
       es="Tiene miedo. La antigua entidad bajo la piedra tiene MIEDO. De mí. La revelación me golpea como un puñetazo.",
       it="Ha paura. L'antica entità sotto la pietra ha PAURA. Di me. La consapevolezza mi colpisce come un pugno.")

    _t(tr, F, "destroy_partial_4",
       en="Yes. I can hurt you. And I will do it again. Unless...",
       fr="Oui. Je peux te blesser. Et je le referai. À moins que...",
       es="Sí. Puedo hacerte daño. Y lo haré de nuevo. A menos que...",
       it="Sì. Posso ferirti. E lo farò di nuovo. A meno che...")

    _t(tr, F, "destroy_partial_5",
       en="UNLESS?",
       fr="À MOINS QUE ?",
       es="¿A MENOS QUE?",
       it="A MENO CHE?")

    _tc(tr, F, "choice_destroy_pivot",
        en_choices=["Attack again - destroy it for good", "Use my strength - dictate terms"],
        fr_choices=["Attaquer de nouveau - le détruire définitivement", "Utiliser ma force - dicter mes conditions"],
        es_choices=["Atacar de nuevo - destruirlo definitivamente", "Usar mi fuerza - dictar condiciones"],
        it_choices=["Attaccare di nuovo - distruggerlo definitivamente", "Usare la mia forza - dettare le condizioni"])

    _t(tr, F, "destroy_to_pact",
       en="No more sacrifices. Never again. No blood, no forced vessel, no tradition. Chosen presence only, with consent and the right to stop. You accept my terms. Or I attack again.",
       fr="Plus de sacrifices. Plus jamais. Pas de sang, pas de réceptacle, pas de tradition. Tu acceptes mes conditions. Ou j'attaque de nouveau.",
       es="No más sacrificios. Nunca más. Sin sangre, sin recipiente, sin tradición. Aceptas mis condiciones. O ataco de nuevo.",
       it="Niente più sacrifici. Mai più. Niente sangue, niente recipiente, niente tradizione. Accetti le mie condizioni. O attacco di nuovo.")

    _t(tr, F, "destroy_to_pact_creature",
       en="THREATS. BUT YOUR THREATS HAVE TEETH. THAT IS... NEW.",
       fr="DES MENACES. MAIS TES MENACES ONT DES DENTS. C'EST... NOUVEAU.",
       es="AMENAZAS. PERO TUS AMENAZAS TIENEN DIENTES. ESO ES... NUEVO.",
       it="MINACCE. MA LE TUE MINACCE HANNO DENTI. QUESTO È... NUOVO.")

    _t(tr, F, "destroy_to_pact_2",
       en="For the first time, a human bargains with the entity from strength instead of terror. Grandmother would have called that progress.",
       fr="Pour la première fois, un humain négocie avec l'entité en position de force. Grand-mère aurait ri.",
       es="Por primera vez, un humano negocia con la entidad desde una posición de fuerza. La abuela se habría reído.",
       it="Per la prima volta, un umano negozia con l'entità da una posizione di forza. La nonna avrebbe riso.")

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

    # --- Phase 9 Story-Fixes: Book check, packed items, 30-year logic, Margarethe death ---
    _t(tr, F, "book_taken_narration",
       en="The book in my hands pulses. It is warm, alive, as though it had its own heartbeat. The creature recognizes it immediately.",
       fr="Le livre dans mes mains pulse. Il est chaud, vivant, comme s'il avait son propre battement de cœur. La créature le reconnaît immédiatement.",
       es="El libro en mis manos pulsa. Está caliente, vivo, como si tuviera su propio latido. La criatura lo reconoce de inmediato.",
       it="Il libro nelle mie mani pulsa. È caldo, vivo, come se avesse un proprio battito cardiaco. La creatura lo riconosce subito.")
    _t(tr, F, "book_taken_creature",
       en="YOU BROUGHT IT. MY BREATH. MY MEMORY.",
       fr="TU L'AS APPORTÉ. MON SOUFFLE. MA MÉMOIRE.",
       es="LO HAS TRAÍDO. MI ALIENTO. MI MEMORIA.",
       it="L'HAI PORTATO. IL MIO RESPIRO. LA MIA MEMORIA.")
    _t(tr, F, "book_taken_reaction",
       en="The book vibrates in my hands. The pages turn by themselves — names, hundreds of names, in an ink that glows in the dark.",
       fr="Le livre vibre dans mes mains. Les pages se tournent d'elles-mêmes — des noms, des centaines de noms, dans une encre qui brille dans le noir.",
       es="El libro vibra en mis manos. Las páginas se pasan solas — nombres, cientos de nombres, en una tinta que brilla en la oscuridad.",
       it="Il libro vibra nelle mie mani. Le pagine si girano da sole — nomi, centinaia di nomi, in un inchiostro che brilla nel buio.")
    _t(tr, F, "book_left_narration",
       en="On the pedestal in the corner lies the book. I did not take it back then. The creature senses my gaze upon it.",
       fr="Sur le piédestal dans le coin repose le livre. Je ne l'avais pas pris à l'époque. La créature sent mon regard posé dessus.",
       es="En el pedestal del rincón está el libro. No lo tomé entonces. La criatura percibe mi mirada sobre él.",
       it="Sul piedistallo nell'angolo giace il libro. Non l'avevo preso allora. La creatura percepisce il mio sguardo su di esso.")
    _t(tr, F, "book_left_creature",
       en="YOU LEFT IT. THAT WAS... WISE. OR FEAR.",
       fr="TU L'AS LAISSÉ. C'ÉTAIT... SAGE. OU DE LA PEUR.",
       es="LO DEJASTE. ESO FUE... SABIO. O MIEDO.",
       it="L'HAI LASCIATO. È STATO... SAGGIO. O PAURA.")
    _t(tr, F, "book_left_reaction",
       en="The book remains closed. But the spiral on the cover turns slowly, as though watching me.",
       fr="Le livre reste fermé. Mais la spirale sur la couverture tourne lentement, comme si elle m'observait.",
       es="El libro permanece cerrado. Pero la espiral en la portada gira lentamente, como si me observara.",
       it="Il libro resta chiuso. Ma la spirale sulla copertina gira lentamente, come se mi stesse osservando.")
    _t(tr, F, "packed_books_narration",
       en="My books lie open beside me. A passage about binding rituals in pre-Christian communities comes to mind — the resonance of the spoken word, the connection between sound and earth.",
       fr="Mes livres sont ouverts à côté de moi. Un passage sur les rituels de liaison dans les communautés précrétiennes me revient — la résonance du mot prononcé, le lien entre le son et la terre.",
       es="Mis libros están abiertos junto a mí. Me viene a la mente un pasaje sobre rituales de vinculación en comunidades precristianas — la resonancia de la palabra hablada, la conexión entre sonido y tierra.",
       it="I miei libri giacciono aperti accanto a me. Mi viene in mente un passaggio sui rituali di legame nelle comunità precristiane — la risonanza della parola pronunciata, il legame tra suono e terra.")
    _t(tr, F, "packed_books_creature",
       en="YOU CARRY WORDS. WORDS HAVE POWER.",
       fr="TU PORTES DES MOTS. LES MOTS ONT DU POUVOIR.",
       es="LLEVAS PALABRAS. LAS PALABRAS TIENEN PODER.",
       it="PORTI PAROLE. LE PAROLE HANNO POTERE.")
    _t(tr, F, "packed_cross_narration",
       en="My mother's cross pulses in my hand — not divine, but... human. Warm. It protects me for a moment from the overwhelm as the entity's consciousness rolls over me.",
       fr="La croix de ma mère pulse dans ma main — pas divine, mais... humaine. Chaude. Elle me protège un instant de la submersion quand la conscience de l'entité déferle sur moi.",
       es="La cruz de mi madre pulsa en mi mano — no divina, pero... humana. Cálida. Me protege un momento de la abrumación cuando la consciencia de la entidad me arrolla.",
       it="La croce di mia madre pulsa nella mia mano — non divina, ma... umana. Calda. Mi protegge per un istante dal sovraccarico quando la coscienza dell'entità mi travolge.")
    _t(tr, F, "packed_camera_narration",
       en="Through the camera's lens I see it. The connection. Spirals in the air, threads of light between the stones. Visible, tangible. The camera shows what the naked eye cannot grasp.",
       fr="À travers l'objectif de l'appareil photo, je le vois. La connexion. Des spirales dans l'air, des fils de lumière entre les pierres. Visible, tangible. L'appareil montre ce que l'œil nu ne peut saisir.",
       es="A través del objetivo de la cámara lo veo. La conexión. Espirales en el aire, hilos de luz entre las piedras. Visible, tangible. La cámara muestra lo que el ojo desnudo no puede captar.",
       it="Attraverso l'obiettivo della macchina fotografica lo vedo. La connessione. Spirali nell'aria, fili di luce tra le pietre. Visibile, tangibile. La macchina mostra ciò che l'occhio nudo non riesce ad afferrare.")
    _t(tr, F, "creature_names_1",
       en="HUNDREDS OF NAMES. NOT ALL VICTIMS. SOME I TOUCHED. SOME TOUCHED ME. VESSELS. SEERS. ONLY EVERY THIRTY YEARS ONE WITH THE CROSS.",
       fr="DES CENTAINES DE NOMS. PAS TOUS DES VICTIMES. CERTAINS, JE LES AI TOUCHÉS. CERTAINS M'ONT TOUCHÉ. DES RÉCEPTACLES. DES VOYANTS. SEULEMENT TOUS LES TRENTE ANS UN AVEC LA CROIX.",
       es="CIENTOS DE NOMBRES. NO TODOS VÍCTIMAS. A ALGUNOS LOS TOQUÉ YO. ALGUNOS ME TOCARON A MÍ. RECIPIENTES. VIDENTES. SOLO CADA TREINTA AÑOS UNO CON LA CRUZ.",
       it="CENTINAIA DI NOMI. NON TUTTI VITTIME. ALCUNI LI HO TOCCATI IO. ALCUNI HANNO TOCCATO ME. RICETTACOLI. VEGGENTI. SOLO OGNI TRENT'ANNI UNO CON LA CROCE.")
    _t(tr, F, "creature_margarethe_1",
       en="THE OLD ONE. SHE CAME TO ME. AT THE END. OF HER OWN WILL. I DID NOT TAKE HER. SHE... SAID FAREWELL.",
       fr="LA VIEILLE. ELLE EST VENUE À MOI. À LA FIN. DE SA PROPRE VOLONTÉ. JE NE L'AI PAS PRISE. ELLE S'EST... DIT AU REVOIR.",
       es="LA VIEJA. VINO A MÍ. AL FINAL. POR SU PROPIA VOLUNTAD. NO LA TOMÉ. ELLA SE... DESPIDIÓ.",
       it="LA VECCHIA. È VENUTA DA ME. ALLA FINE. DI SUA VOLONTÀ. NON L'HO PRESA. LEI HA... DETTO ADDIO.")
    _t(tr, F, "creature_margarethe_2",
       en="Grandmother. She died peacefully. She went to the creature of her own will, had her last conversation with it. No murder, no accident. A farewell.",
       fr="Grand-mère. Elle est morte paisiblement. Elle est allée vers la créature de son plein gré, a eu sa dernière conversation avec elle. Pas de meurtre, pas d'accident. Un adieu.",
       es="La abuela. Murió en paz. Fue a la criatura por voluntad propia, tuvo su última conversación con ella. Ni asesinato, ni accidente. Una despedida.",
       it="La nonna. È morta serenamente. È andata dalla creatura per sua volontà, ha avuto la sua ultima conversazione con lei. Nessun omicidio, nessun incidente. Un addio.")
    _t(tr, F, "creature_margarethe_3",
       en="My eyes burn. Grandmother did not have to die alone. She had someone with her — even if that someone was older than humankind.",
       fr="Mes yeux brûlent. Grand-mère n'a pas dû mourir seule. Elle avait quelqu'un auprès d'elle — même si ce quelqu'un était plus ancien que l'humanité.",
       es="Me arden los ojos. La abuela no tuvo que morir sola. Tenía a alguien a su lado — aunque ese alguien fuera más antiguo que la humanidad.",
       it="Mi bruciano gli occhi. La nonna non ha dovuto morire sola. Aveva qualcuno accanto — anche se quel qualcuno era più antico dell'umanità.")

    # --- Phase 10 Story-Konsistenz-Fixes ---
    _t(tr, F, "courage_high_dialogue",
       en="My hands rest steady on the stone. No trembling. No panic. Only clarity, razor-sharp and cold.",
       fr="Mes mains reposent, fermes, sur la pierre. Pas de tremblement. Pas de panique. Seulement de la clarté, tranchante et froide.",
       es="Mis manos descansan firmes sobre la piedra. Sin temblores. Sin pánico. Solo claridad, afilada y fría.",
       it="Le mie mani poggiano salde sulla pietra. Nessun tremore. Nessun panico. Solo chiarezza, tagliente e fredda.")

    _t(tr, F, "courage_high_2",
       en="YOU ARE NOT AFRAID. THAT IS... NEW. SIX HUNDRED YEARS AND NO ONE STOOD SO CALM BEFORE ME.",
       fr="TU N'AS PAS PEUR. C'EST... NOUVEAU. SIX CENTS ANS ET PERSONNE NE S'EST TENU SI CALME DEVANT MOI.",
       es="NO TIENES MIEDO. ESO ES... NUEVO. SEISCIENTOS AÑOS Y NADIE SE MANTUVO TAN SERENO ANTE MÍ.",
       it="NON HAI PAURA. QUESTO È... NUOVO. SEICENTO ANNI E NESSUNO È RIMASTO COSÌ CALMO DAVANTI A ME.")

    _t(tr, F, "courage_high_3",
       en="I am afraid. But I have learned that fear need not be the last thing one feels.",
       fr="J'ai peur. Mais j'ai appris que la peur ne doit pas être la dernière chose que l'on ressent.",
       es="Tengo miedo. Pero he aprendido que el miedo no tiene por qué ser lo último que uno siente.",
       it="Ho paura. Ma ho imparato che la paura non deve essere l'ultima cosa che si prova.")

    _t(tr, F, "courage_low_dialogue",
       en="My whole body trembles. My teeth chatter. The cold creeps from inside out, as if the entity had pushed a finger of ice into my chest.",
       fr="Tout mon corps tremble. Mes dents claquent. Le froid rampe de l'intérieur vers l'extérieur, comme si l'entité avait enfoncé un doigt de glace dans ma poitrine.",
       es="Todo mi cuerpo tiembla. Me castañetean los dientes. El frío se arrastra de dentro hacia fuera, como si la entidad hubiera hundido un dedo de hielo en mi pecho.",
       it="Tutto il mio corpo trema. I denti mi battono. Il freddo striscia dall'interno verso l'esterno, come se l'entità avesse spinto un dito di ghiaccio nel mio petto.")

    _t(tr, F, "courage_low_2",
       en="YOUR FEAR TASTES LIKE THE OTHERS'. BUT YOU ARE HERE NONETHELESS. THAT MAKES YOU... STRANGE.",
       fr="TA PEUR A LE GOÛT DE CELLE DES AUTRES. MAIS TU ES LÀ QUAND MÊME. CELA TE REND... ÉTRANGE.",
       es="TU MIEDO SABE COMO EL DE LOS DEMÁS. PERO ESTÁS AQUÍ DE TODOS MODOS. ESO TE HACE... EXTRAÑA.",
       it="LA TUA PAURA HA IL SAPORE DI QUELLA DEGLI ALTRI. MA SEI QUI COMUNQUE. QUESTO TI RENDE... STRANA.")

    _t(tr, F, "courage_low_3",
       en="I am so afraid. But I cannot leave. Not now. Not after everything.",
       fr="J'ai tellement peur. Mais je ne peux pas partir. Pas maintenant. Pas après tout cela.",
       es="Tengo tanto miedo. Pero no puedo irme. No ahora. No después de todo.",
       it="Ho così tanta paura. Ma non posso andarmene. Non ora. Non dopo tutto questo.")

    _t(tr, F, "knowledge_high",
       en="Everything I have learned - the spirals, the singing, the old stories - it all makes sense now. The creature is no monster. It is a prisoner. Like Konrad, only older. Much older.",
       fr="Tout ce que j'ai appris - les spirales, le chant, les vieilles histoires - tout prend sens maintenant. La créature n'est pas un monstre. C'est un prisonnier. Comme Konrad, mais plus ancien. Bien plus ancien.",
       es="Todo lo que he aprendido - las espirales, el canto, las viejas historias - todo tiene sentido ahora. La criatura no es un monstruo. Es un prisionero. Como Konrad, solo que más antiguo. Mucho más antiguo.",
       it="Tutto ciò che ho imparato - le spirali, il canto, le vecchie storie - ora ha senso. La creatura non è un mostro. È un prigioniero. Come Konrad, solo più antico. Molto più antico.")

    _t(tr, F, "knowledge_high_2",
       en="I know you. Not your name, but your loneliness. The spirals, the dreams, the singing - I listened.",
       fr="Je te connais. Pas ton nom, mais ta solitude. Les spirales, les rêves, le chant - j'ai écouté.",
       es="Te conozco. No tu nombre, pero sí tu soledad. Las espirales, los sueños, el canto - escuché.",
       it="Ti conosco. Non il tuo nome, ma la tua solitudine. Le spirali, i sogni, il canto - ho ascoltato.")

    _t(tr, F, "knowledge_partial",
       en="I know it is old. I know it sleeps beneath the earth and sings in its sleep. But that is not enough. I do not understand its language, only fragments, like words of a foreign language one catches in passing.",
       fr="Je sais qu'elle est ancienne. Je sais qu'elle dort sous la terre et chante dans son sommeil. Mais cela ne suffit pas. Je ne comprends pas son langage, seulement des fragments, comme des mots d'une langue étrangère qu'on attrape en passant.",
       es="Sé que es antiguo. Sé que duerme bajo la tierra y canta en sueños. Pero no es suficiente. No entiendo su idioma, solo fragmentos, como palabras de una lengua extranjera que uno capta al pasar.",
       it="So che è antico. So che dorme sotto la terra e canta nel sonno. Ma non è abbastanza. Non capisco il suo linguaggio, solo frammenti, come parole di una lingua straniera che si colgono di passaggio.")

    _t(tr, F, "konrad_door_memory",
       en="You opened the door for me when everyone else kept it locked. On the first night. That... that was me, Elise. Not IT. That was me.",
       fr="Tu m'as ouvert la porte quand tous les autres la gardaient verrouillée. La première nuit. Ça... c'était moi, Elise. Pas LUI. C'était moi.",
       es="Me abriste la puerta cuando todos los demás la mantenían cerrada. La primera noche. Eso... eso fui yo, Elise. No ÉL. Fui yo.",
       it="Mi hai aperto la porta quando tutti gli altri la tenevano chiusa. La prima notte. Quello... quello ero io, Elise. Non LUI. Ero io.")

    _t(tr, F, "otto_has_book",
       en="A sound at the entrance. Otto Reinhardt steps from the shadows, the book in his hands. He must have followed me.",
       fr="Un bruit à l'entrée. Otto Reinhardt sort de l'ombre, le livre dans les mains. Il a dû me suivre.",
       es="Un ruido en la entrada. Otto Reinhardt sale de las sombras, el libro en las manos. Debe haberme seguido.",
       it="Un rumore all'ingresso. Otto Reinhardt esce dall'ombra, il libro tra le mani. Deve avermi seguita.")

    _t(tr, F, "otto_book_taunt",
       en="Otto's lips form a triumphant smile. He raises the book like a weapon - but before he can speak, the air vibrates.",
       fr="Les lèvres d'Otto dessinent un sourire triomphant. Il brandit le livre comme une arme - mais avant qu'il puisse parler, l'air vibre.",
       es="Los labios de Otto forman una sonrisa triunfante. Levanta el libro como un arma - pero antes de que pueda hablar, el aire vibra.",
       it="Le labbra di Otto formano un sorriso trionfante. Alza il libro come un'arma - ma prima che possa parlare, l'aria vibra.")

    _t(tr, F, "otto_book_creature",
       en="THE BOOK BELONGS TO ME. NOT TO HIM.",
       fr="LE LIVRE M'APPARTIENT. PAS À LUI.",
       es="EL LIBRO ME PERTENECE. NO A ÉL.",
       it="IL LIBRO APPARTIENE A ME. NON A LUI.")

    _t(tr, F, "otto_book_taken",
       en="The book tears itself from Otto's hands, flies through the air, and lands open before me. Otto stumbles back, chalk-white, and flees up the stairs. The entity has no patience for thieves.",
       fr="Le livre s'arrache des mains d'Otto, vole dans les airs et atterrit ouvert devant moi. Otto recule, blanc comme un linge, et fuit dans l'escalier. L'entité n'a aucune patience pour les voleurs.",
       es="El libro se arranca de las manos de Otto, vuela por el aire y aterriza abierto ante mí. Otto retrocede, blanco como la tiza, y huye escaleras arriba. La entidad no tiene paciencia con los ladrones.",
       it="Il libro si strappa dalle mani di Otto, vola nell'aria e atterra aperto davanti a me. Otto indietreggia, bianco come un cencio, e fugge su per le scale. L'entità non ha pazienza per i ladri.")


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

    # --- Phase 9 Story-Fixes: Epilog nodes + trusted_konrad ---
    _t(tr, F, "seal_anna_epilog",
       en="Anna's eyes grow clearer by the day. The singing fades, and with it her visions. For the first time she is a normal child.",
       fr="Les yeux d'Anna deviennent plus clairs de jour en jour. Le chant s'estompe, et avec lui ses visions. Pour la première fois, elle est une enfant normale.",
       es="Los ojos de Anna se aclaran día a día. El canto se desvanece, y con él sus visiones. Por primera vez es una niña normal.",
       it="Gli occhi di Anna diventano più chiari giorno dopo giorno. Il canto si affievolisce, e con esso le sue visioni. Per la prima volta è una bambina normale.")
    _t(tr, F, "seal_otto_epilog",
       en="Otto Reinhardt leaves Graubach a week after the ritual. No one stops him. No one misses him.",
       fr="Otto Reinhardt quitte Graubach une semaine après le rituel. Personne ne l'arrête. Personne ne le regrette.",
       es="Otto Reinhardt deja Graubach una semana después del ritual. Nadie lo detiene. Nadie lo echa de menos.",
       it="Otto Reinhardt lascia Graubach una settimana dopo il rituale. Nessuno lo ferma. Nessuno lo rimpiange.")
    _t(tr, F, "seal_candle_epilog",
       en="The candle on Grandmother's nightstand goes out at the moment the entity falls asleep. Quietly. Peacefully.",
       fr="La bougie sur la table de nuit de grand-mère s'éteint au moment où l'entité s'endort. Doucement. Paisiblement.",
       es="La vela en la mesita de noche de la abuela se apaga en el momento en que la entidad se duerme. En silencio. En paz.",
       it="La candela sul comodino della nonna si spegne nel momento in cui l'entità si addormenta. Piano. Serenamente.")
    _t(tr, F, "konrad_trusted_seal",
       en="Konrad appears the next morning. The spirals on his hand are fading. He weeps. 'I am free,' he whispers. And for the first time I believe him.",
       fr="Konrad apparaît le lendemain matin. Les spirales sur sa main s'estompent. Il pleure. « Je suis libre », murmure-t-il. Et pour la première fois, je le crois.",
       es="Konrad aparece a la mañana siguiente. Las espirales en su mano se desvanecen. Llora. 'Soy libre', susurra. Y por primera vez le creo.",
       it="Konrad appare la mattina dopo. Le spirali sulla sua mano si stanno sbiadendo. Piange. 'Sono libero', sussurra. E per la prima volta gli credo.")
    _t(tr, F, "konrad_untrusted_seal",
       en="Konrad vanished on the night of the ritual. No one saw him leave. Some say he lives in the forest now. Some say the forest took him.",
       fr="Konrad a disparu la nuit du rituel. Personne ne l'a vu partir. Certains disent qu'il vit dans la forêt maintenant. Certains disent que la forêt l'a pris.",
       es="Konrad desapareció la noche del ritual. Nadie lo vio irse. Algunos dicen que ahora vive en el bosque. Algunos dicen que el bosque se lo llevó.",
       it="Konrad è scomparso la notte del rituale. Nessuno l'ha visto andarsene. Alcuni dicono che ora vive nel bosco. Alcuni dicono che il bosco l'ha preso.")

    # --- Phase 10 Story-Konsistenz-Fixes ---
    _t(tr, F, "narration_anchor_seal",
       en="Three parts lock into place - the chant, the sign beneath my feet, and me. The anchor. Not a martyr's chain, but a chosen bond I can still survive.",
       fr="Trois parties se rejoignent - le chant, le signe sous mes pieds, et moi-même. L'ancre. Le plan de grand-mère, accompli.",
       es="Tres partes se unen - el canto, el signo bajo mis pies, y yo misma. El ancla. El plan de la abuela, cumplido.",
       it="Tre parti si uniscono - il canto, il segno sotto i miei piedi, e io stessa. L'ancora. Il piano della nonna, compiuto.")


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

    # --- Phase 9 Story-Fixes: Epilog nodes ---
    _t(tr, F, "escape_konrad_epilog",
       en="Konrad. On some nights I think of the man with glassy eyes who was imprisoned for thirty years. Did the awakening free him? Or did it take him with it?",
       fr="Konrad. Certaines nuits, je pense à l'homme aux yeux vitreux qui a été prisonnier pendant trente ans. L'éveil l'a-t-il libéré ? Ou l'a-t-il emporté ?",
       es="Konrad. Algunas noches pienso en el hombre de ojos vidriosos que estuvo preso durante treinta años. ¿El despertar lo liberó? ¿O se lo llevó?",
       it="Konrad. Certe notti penso all'uomo dagli occhi vitrei che è stato prigioniero per trent'anni. Il risveglio lo ha liberato? O lo ha portato con sé?")
    _t(tr, F, "escape_anna_epilog",
       en="In my darkest nights I wonder whether Anna survived. A child with eyes that saw too much.",
       fr="Dans mes nuits les plus sombres, je me demande si Anna a survécu. Une enfant aux yeux qui voyaient trop.",
       es="En mis noches más oscuras, me pregunto si Anna sobrevivió. Una niña con ojos que veían demasiado.",
       it="Nelle mie notti più buie, mi chiedo se Anna sia sopravvissuta. Una bambina con occhi che vedevano troppo.")
    _t(tr, F, "escape_otto_epilog",
       en="Otto? Vanished with the village. Buried beneath his own silence.",
       fr="Otto ? Disparu avec le village. Enseveli sous son propre silence.",
       es="¿Otto? Desaparecido con el pueblo. Enterrado bajo su propio silencio.",
       it="Otto? Scomparso con il villaggio. Sepolto sotto il suo stesso silenzio.")

    # --- Phase 10 Story-Konsistenz-Fixes ---
    _t(tr, F, "narration_forest_opens",
       en="The trees recede. The forest that held me captive for days suddenly opens - as if the creature's awakening had torn the old bindings apart.",
       fr="Les arbres reculent. La forêt qui m'a retenue captive pendant des jours s'ouvre soudain - comme si l'éveil de la créature avait déchiré les anciens liens.",
       es="Los árboles retroceden. El bosque que me mantuvo cautiva durante días se abre de repente - como si el despertar de la criatura hubiera desgarrado las antiguas ataduras.",
       it="Gli alberi arretrano. La foresta che mi ha tenuta prigioniera per giorni si apre improvvisamente - come se il risveglio della creatura avesse strappato gli antichi vincoli.")

    _t(tr, F, "narration_forest_opens_2",
       en="Of course. The entity HAD controlled the forest. Whoever guards the book also guards the borders. But now it is awake, and its attention no longer falls on the trees.",
       fr="Bien sûr. L'entité contrôlait la forêt. Celui qui garde le livre garde aussi les frontières. Mais maintenant elle est éveillée, et son attention ne se porte plus sur les arbres.",
       es="Por supuesto. La entidad controlaba el bosque. Quien custodia el libro también custodia las fronteras. Pero ahora está despierta, y su atención ya no recae sobre los árboles.",
       it="Certo. L'entità controllava la foresta. Chi custodisce il libro custodisce anche i confini. Ma ora è sveglia, e la sua attenzione non ricade più sugli alberi.")

    _t(tr, F, "escape_candle_epilog",
       en="Somewhere in the ruins of Graubach, a candle that burned for three weeks goes out. Its last flicker is seen by no one.",
       fr="Quelque part dans les ruines de Graubach, une bougie qui a brûlé pendant trois semaines s'éteint. Son dernier scintillement n'est vu par personne.",
       es="En algún lugar entre las ruinas de Graubach, una vela que ardió durante tres semanas se apaga. Su último parpadeo no lo ve nadie.",
       it="Da qualche parte tra le rovine di Graubach, una candela che ha bruciato per tre settimane si spegne. Il suo ultimo guizzo non è visto da nessuno.")

    _t(tr, F, "packed_books_escape",
       en="My books lie somewhere under the rubble. The folklore, the myths - all useless against something older than stories. But I will write new ones. Warnings.",
       fr="Mes livres gisent quelque part sous les décombres. Le folklore, les mythes - tout inutile contre quelque chose de plus ancien que les histoires. Mais j'en écrirai de nouveaux. Des avertissements.",
       es="Mis libros yacen en algún lugar bajo los escombros. El folklore, los mitos - todo inútil contra algo más antiguo que las historias. Pero escribiré nuevos. Advertencias.",
       it="I miei libri giacciono da qualche parte sotto le macerie. Il folklore, i miti - tutto inutile contro qualcosa di più antico delle storie. Ma ne scriverò di nuovi. Avvertimenti.")

    _t(tr, F, "packed_cross_escape",
       en="My mother's crucifix still dangles from my neck. Did it help? No. But it reminded me of something: there is a world beyond Graubach. And I am on my way back to it.",
       fr="Le crucifix de ma mère pend encore à mon cou. A-t-il aidé ? Non. Mais il m'a rappelé quelque chose : il existe un monde au-delà de Graubach. Et je suis en chemin pour y retourner.",
       es="El crucifijo de mi madre aún cuelga de mi cuello. ¿Ayudó? No. Pero me recordó algo: hay un mundo más allá de Graubach. Y estoy en camino de regreso.",
       it="Il crocifisso di mia madre pende ancora dal mio collo. Ha aiutato? No. Ma mi ha ricordato qualcosa: esiste un mondo oltre Graubach. E sono in cammino per tornarci.")

    _t(tr, F, "packed_camera_escape",
       en="The camera has one last image: Graubach, sinking, dissolving. The only proof besides Grandmother's journal. Sometimes I study it on sleepless nights and wonder if it was real.",
       fr="L'appareil photo a une dernière image : Graubach, qui sombre, qui se dissout. La seule preuve en dehors du journal de grand-mère. Parfois je l'examine lors de nuits blanches et me demande si c'était réel.",
       es="La cámara tiene una última imagen: Graubach, hundiéndose, disolviéndose. La única prueba además del diario de la abuela. A veces la contemplo en noches de insomnio y me pregunto si fue real.",
       it="La macchina fotografica ha un'ultima immagine: Graubach, che affonda, che si dissolve. L'unica prova oltre al diario della nonna. A volte la osservo nelle notti insonni e mi chiedo se fosse reale.")


def _add_act4_ending_pact(tr):
    F = "res://data/dialogue/act4/ending_pact.json"

    _t(tr, F, "narration_1_wounded",
       en="The creature contracts, wounded, frightened. For the first time in six hundred years, a human stands above it, not beneath it.",
       fr="La créature se contracte, blessée, effrayée. Pour la première fois en six cents ans, un humain se tient au-dessus d'elle, pas en dessous.",
       es="La criatura se contrae, herida, asustada. Por primera vez en seiscientos años, un humano está por encima de ella, no por debajo.",
       it="La creatura si contrae, ferita, spaventata. Per la prima volta in seicento anni, un umano le sta sopra, non sotto.")

    _t(tr, F, "narration_1_normal",
       en="I speak to the entity. Not with words — with thoughts, with will. I step onto the earth sign and open my mind.",
       fr="Je parle à l'entité. Pas avec des mots — avec des pensées, avec de la volonté. Je me place sur le signe de terre et j'ouvre mon esprit.",
       es="Le hablo a la entidad. No con palabras — con pensamientos, con voluntad. Me coloco sobre el signo de la tierra y abro mi mente.",
       it="Parlo all'entità. Non con parole — con pensieri, con volontà. Mi posiziono sul segno della terra e apro la mia mente.")

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

    # --- Wounded pact path (from destroy) ---
    _t(tr, F, "wounded_pact_creature",
       en="I HEAR. STATE YOUR TERMS. MY... PAIN... IS GREAT.",
       fr="J'ÉCOUTE. POSE TES CONDITIONS. MA... DOULEUR... EST GRANDE.",
       es="ESCUCHO. PLANTEA TUS CONDICIONES. MI... DOLOR... ES GRANDE.",
       it="ASCOLTO. PONI LE TUE CONDIZIONI. IL MIO... DOLORE... È GRANDE.")

    _t(tr, F, "wounded_pact_elise",
       en="Six hundred years of sacrifice. It ends. Today. Forever. In return, I leave you in peace.",
       fr="Six cents ans de sacrifices. Ça s'arrête. Aujourd'hui. Pour toujours. En échange, je te laisse en paix.",
       es="Seiscientos años de sacrificios. Se acaba. Hoy. Para siempre. A cambio, te dejo en paz.",
       it="Seicento anni di sacrifici. Finisce. Oggi. Per sempre. In cambio, ti lascio in pace.")

    _t(tr, F, "wounded_creature_react",
       en="PEACE. A WORD I HAVE ALMOST FORGOTTEN. WHAT DOES IT MEAN TO YOU?",
       fr="PAIX. UN MOT QUE J'AI PRESQUE OUBLIÉ. QUE SIGNIFIE-T-IL POUR TOI ?",
       es="PAZ. UNA PALABRA QUE CASI HE OLVIDADO. ¿QUÉ SIGNIFICA PARA TI?",
       it="PACE. UNA PAROLA CHE HO QUASI DIMENTICATO. CHE COSA SIGNIFICA PER TE?")

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
       en="Negotiated. As Grandmother would have wanted in the end. No more blood — only chosen company, with consent and the right to leave.",
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
       en="Peace, Pastor. For the first time in six hundred years. No more sacrifice. No blood. A pact with terms: consent, chosen presence, and the right to stop.",
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
       en="No blood. No sacrifice. No vessel. We set clear terms: chosen presence only, explicit consent, and the right to stop. I will return by choice, and if one day I cannot, another willing voice can take my place. It accepted. Grandmother paved the way.",
       fr="Pas de sang. Pas de sacrifice. Pas de réceptacle. Seulement une promesse : chaque année, je reviendrai tenir compagnie à l'entité. Elle à accepté. Grand-mère à ouvert là voie. Je là suivrai jusqu'au bout.",
       es="Sin sangre. Sin sacrificio. Sin receptáculo. Solo una promesa: cada año volveré y le haré compañía a la entidad. Aceptó. La abuela allanó el camino. Yo lo recorreré hasta el final.",
       it="Niente sangue. Niente sacrificio. Nessun ricettacolo. Solo una promessa: ogni anno tornerò è farò compagnia all'entità. Ha accettato. La nonna ha aperto la strada. Io la percorrerò fino in fondo.",
       field="content")

    # --- Phase 11: Epilog transition ---
    _t(tr, F, "pact_epilog_transition",
       en="Weeks pass. Months. The memory of that night fades like a dream — but the pact remains.",
       fr="Les semaines passent. Les mois. Le souvenir de cette nuit s'estompe comme un rêve — mais le pacte demeure.",
       es="Pasan semanas. Meses. El recuerdo de aquella noche se desvanece como un sueño — pero el pacto permanece.",
       it="Passano settimane. Mesi. Il ricordo di quella notte svanisce come un sogno — ma il patto resta.")
    # --- Phase 9b: Konrad epilog ---
    _t(tr, F, "pact_konrad_epilog",
       en="Konrad stands at the fountain as Elise leaves the chamber. The spirals on his hands are already fading. For the first time in thirty years, his gaze belongs to himself.",
       fr="Konrad se tient près de la fontaine quand Elise quitte la chambre. Les spirales sur ses mains s'estompent déjà. Pour la première fois en trente ans, son regard lui appartient.",
       es="Konrad está junto a la fuente cuando Elise sale de la cámara. Las espirales en sus manos ya se desvanecen. Por primera vez en treinta años, su mirada le pertenece.",
       it="Konrad è alla fontana quando Elise esce dalla camera. Le spirali sulle sue mani stanno già svanendo. Per la prima volta in trent'anni, il suo sguardo appartiene a lui stesso.")
    _t(tr, F, "pact_konrad_epilog_2",
       en="'It's letting me go,' he says quietly. 'I can feel it. It doesn't need me anymore.' He weeps — not from grief. From relief.",
       fr="« Il me laisse partir », dit-il doucement. « Je le sens. Il n'a plus besoin de moi. » Il pleure — pas de chagrin. De soulagement.",
       es="'Me está soltando', dice en voz baja. 'Puedo sentirlo. Ya no me necesita.' Llora — no de pena. De alivio.",
       it="'Mi sta lasciando andare', dice piano. 'Lo sento. Non ha più bisogno di me.' Piange — non di dolore. Di sollievo.")
    # --- Phase 9 Story-Fixes: Epilog nodes ---
    _t(tr, F, "pact_anna_epilog",
       en="Anna visits Elise every autumn. 'It sings differently,' she says. 'More content.' Anna smiles — for the first time without fear.",
       fr="Anna rend visite à Elise chaque automne. « Il chante différemment », dit-elle. « Plus content. » Anna sourit — pour la première fois sans peur.",
       es="Anna visita a Elise cada otoño. 'Canta diferente', dice. 'Más contento.' Anna sonríe — por primera vez sin miedo.",
       it="Anna fa visita a Elise ogni autunno. 'Canta diversamente', dice. 'Più soddisfatto.' Anna sorride — per la prima volta senza paura.")
    _t(tr, F, "pact_otto_epilog",
       en="Otto leaves the village when he realizes the tradition is over. His life's work — meaningless.",
       fr="Otto quitte le village quand il comprend que la tradition est terminée. L'œuvre de sa vie — sans signification.",
       es="Otto deja el pueblo cuando comprende que la tradición ha terminado. La obra de su vida — sin sentido.",
       it="Otto lascia il villaggio quando capisce che la tradizione è finita. L'opera della sua vita — senza significato.")

    # --- Phase 10 Story-Konsistenz-Fixes ---
    _t(tr, F, "narration_anchor_pact",
       en="I stand on the sign, the chant thins, and the anchor holds - by consent, not coercion. The pact forms not from power, but from trust.",
       fr="Je me tiens sur le signe, le chant s'estompe, et l'ancre tient - non comme une chaîne, mais comme un pont. Le pacte se forme non par la puissance, mais par la confiance.",
       es="Me alzo sobre el signo, el canto se desvanece, y el ancla sostiene - no como una cadena, sino como un puente. El pacto se forma no por el poder, sino por la confianza.",
       it="Mi ergo sul segno, il canto sfuma, e l'ancora tiene - non come una catena, ma come un ponte. Il patto si forma non dal potere, ma dalla fiducia.")

    _t(tr, F, "pact_candle_epilog",
       en="The candle on Grandmother's nightstand burns more steadily. No longer desperate, no longer waiting. A calm, contented flame.",
       fr="La bougie sur la table de nuit de grand-mère brûle plus régulièrement. Plus désespérée, plus en attente. Une flamme calme et satisfaite.",
       es="La vela en la mesita de noche de la abuela arde con más calma. Ya no desesperada, ya no esperando. Una llama tranquila y satisfecha.",
       it="La candela sul comodino della nonna arde più regolarmente. Non più disperata, non più in attesa. Una fiamma calma e appagata.")

    _t(tr, F, "packed_books_pact",
       en="My books lie open beside me. The old texts on rituals and bindings - they led me here. But the true knowledge was never in books. It lay in listening.",
       fr="Mes livres sont ouverts à côté de moi. Les anciens textes sur les rituels et les liens - ils m'ont menée ici. Mais le vrai savoir n'a jamais été dans les livres. Il résidait dans l'écoute.",
       es="Mis libros yacen abiertos a mi lado. Los viejos textos sobre rituales y vínculos - me trajeron hasta aquí. Pero el verdadero conocimiento nunca estuvo en los libros. Estaba en escuchar.",
       it="I miei libri giacciono aperti accanto a me. I vecchi testi su rituali e legami - mi hanno condotta fin qui. Ma la vera conoscenza non è mai stata nei libri. Risiedeva nell'ascolto.")

    _t(tr, F, "packed_cross_pact",
       en="My mother's crucifix lies warm in my hand. Faith against the unknown - but the unknown was never the enemy. It was only lonely.",
       fr="Le crucifix de ma mère repose, chaud, dans ma main. La foi contre l'inconnu - mais l'inconnu n'a jamais été l'ennemi. Il était seulement seul.",
       es="El crucifijo de mi madre reposa cálido en mi mano. Fe contra lo desconocido - pero lo desconocido nunca fue el enemigo. Solo estaba solo.",
       it="Il crocifisso di mia madre giace caldo nella mia mano. Fede contro l'ignoto - ma l'ignoto non è mai stato il nemico. Era solo solo.")

    _t(tr, F, "packed_camera_pact",
       en="My camera hangs unused around my neck. Some truths cannot be photographed. But I will write them down - every word, every encounter.",
       fr="Mon appareil photo pend inutilisé autour de mon cou. Certaines vérités ne se photographient pas. Mais je les écrirai - chaque mot, chaque rencontre.",
       es="Mi cámara cuelga sin usar de mi cuello. Algunas verdades no pueden fotografiarse. Pero las escribiré - cada palabra, cada encuentro.",
       it="La mia macchina fotografica pende inutilizzata al mio collo. Certe verità non si possono fotografare. Ma le scriverò - ogni parola, ogni incontro.")


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

    # --- Phase 11: Epilog transition ---
    _t(tr, F, "truth_epilog_transition",
       en="Dawn. The longest night of my life is over. And with it thirty years of lies.",
       fr="L'aube. La plus longue nuit de ma vie est terminée. Et avec elle trente ans de mensonges.",
       es="Amanecer. La noche más larga de mi vida ha terminado. Y con ella treinta años de mentiras.",
       it="L'alba. La notte più lunga della mia vita è finita. E con essa trent'anni di bugie.")
    # --- Phase 9b: Konrad epilog ---
    _t(tr, F, "truth_konrad_epilog",
       en="Konrad stands at the church entrance as the morning light falls through the windows. The glassy moments are over. His eyes are clear. 'It sleeps peacefully,' he whispers. 'For the first time it is not dreaming through me.'",
       fr="Konrad se tient à l'entrée de l'église tandis que la lumière du matin traverse les vitraux. Les moments vitreux sont terminés. Ses yeux sont clairs. « Il dort paisiblement », murmure-t-il. « Pour la première fois, il ne rêve pas à travers moi. »",
       es="Konrad está en la entrada de la iglesia mientras la luz de la mañana atraviesa las ventanas. Los momentos vidriosos han terminado. Sus ojos están claros. 'Duerme en paz', susurra. 'Por primera vez no sueña a través de mí.'",
       it="Konrad è all'ingresso della chiesa mentre la luce del mattino filtra dalle finestre. I momenti vitrei sono finiti. I suoi occhi sono limpidi. 'Dorme in pace', sussurra. 'Per la prima volta non sogna attraverso di me.'")
    # --- Phase 9 Story-Fixes: Epilog nodes ---
    _t(tr, F, "truth_otto_epilog",
       en="Otto stands at the edge of the village and watches the sunrise. He weeps. For thirty years he believed the sacrifices were necessary. They never were.",
       fr="Otto se tient au bord du village et regarde le lever du soleil. Il pleure. Pendant trente ans, il a cru que les sacrifices étaient nécessaires. Ils ne l'ont jamais été.",
       es="Otto está al borde del pueblo y observa el amanecer. Llora. Durante treinta años creyó que los sacrificios eran necesarios. Nunca lo fueron.",
       it="Otto sta ai margini del villaggio e guarda l'alba. Piange. Per trent'anni ha creduto che i sacrifici fossero necessari. Non lo sono mai stati.")
    _t(tr, F, "truth_candle_epilog",
       en="In Grandmother's house the candle goes out. But the scent of honey and herbs remains.",
       fr="Dans la maison de grand-mère, la bougie s'éteint. Mais l'odeur de miel et d'herbes reste.",
       es="En la casa de la abuela la vela se apaga. Pero el olor a miel y hierbas permanece.",
       it="Nella casa della nonna la candela si spegne. Ma il profumo di miele ed erbe resta.")

    # --- Phase 10 Story-Konsistenz-Fixes ---
    _t(tr, F, "narration_anchor_truth",
       en="The sign pulses beneath me, the chant echoes, and the anchor - I - keeps the connection open. Not as a prison, but as a threshold we both can step back from.",
       fr="Le signe pulse sous moi, le chant résonne, et l'ancre - moi - maintient la connexion. Mais au lieu de lier, elle ouvre. La compréhension coule dans les deux sens.",
       es="El signo pulsa debajo de mí, el canto resuena, y el ancla - yo - mantiene la conexión. Pero en vez de atar, abre. La comprensión fluye en ambas direcciones.",
       it="Il segno pulsa sotto di me, il canto riecheggia, e l'ancora - io - mantiene la connessione. Ma invece di legare, apre. La comprensione fluisce in entrambe le direzioni.")

    _t(tr, F, "truth_mathilde_epilog",
       en="Elise thinks of the blind woman on the train. Mathilde. She had known it for sixty years. She hummed the melody not from madness - but from understanding.",
       fr="Elise pense à la femme aveugle dans le train. Mathilde. Elle le savait depuis soixante ans. Elle fredonnait la mélodie non par folie - mais par compréhension.",
       es="Elise piensa en la mujer ciega del tren. Mathilde. Lo había sabido durante sesenta años. Tarareaba la melodía no por locura - sino por comprensión.",
       it="Elise pensa alla donna cieca sul treno. Mathilde. Lo sapeva da sessant'anni. Canticchiava la melodia non per follia - ma per comprensione.")

    _t(tr, F, "packed_books_truth",
       en="My books - folklore, myths, binding rituals - they prepared me for asking. But the answers did not come from paper. They came from the abyss itself.",
       fr="Mes livres - folklore, mythes, rituels de liaison - ils m'ont préparée à poser des questions. Mais les réponses ne sont pas venues du papier. Elles sont venues de l'abîme lui-même.",
       es="Mis libros - folklore, mitos, rituales de vinculación - me prepararon para preguntar. Pero las respuestas no vinieron del papel. Vinieron del abismo mismo.",
       it="I miei libri - folklore, miti, rituali di legame - mi hanno preparata a fare domande. Ma le risposte non sono venute dalla carta. Sono venute dall'abisso stesso.")

    _t(tr, F, "packed_cross_truth",
       en="My mother's crucifix lay useless in my pocket. No god saved me. The truth saved me - and the willingness to endure it.",
       fr="Le crucifix de ma mère gisait inutile dans ma poche. Aucun dieu ne m'a sauvée. La vérité m'a sauvée - et la volonté de la supporter.",
       es="El crucifijo de mi madre yacía inútil en mi bolsillo. Ningún dios me salvó. La verdad me salvó - y la disposición a soportarla.",
       it="Il crocifisso di mia madre giaceva inutile in tasca. Nessun dio mi ha salvata. La verità mi ha salvata - e la volontà di sopportarla.")

    _t(tr, F, "packed_camera_truth",
       en="The camera could not have captured what I saw. Six hundred years of loneliness do not fit on a strip of film. But I will write about it. The world shall know what was here.",
       fr="L'appareil photo n'aurait rien pu capturer de ce que j'ai vu. Six cents ans de solitude ne tiennent pas sur une pellicule. Mais j'en écrirai. Le monde doit savoir ce qui était ici.",
       es="La cámara no habría podido capturar lo que vi. Seiscientos años de soledad no caben en una película fotográfica. Pero escribiré sobre ello. El mundo debe saber lo que hubo aquí.",
       it="La macchina fotografica non avrebbe potuto catturare ciò che ho visto. Seicento anni di solitudine non entrano in una pellicola. Ma ne scriverò. Il mondo deve sapere cosa c'era qui.")


def _add_act4_ending_sacrifice(tr):
    F = "res://data/dialogue/act4/ending_sacrifice.json"

    _t(tr, F, "narration_1",
       en="I look at Konrad. He is trembling. Beads of sweat on his forehead. Behind his eyes, a man fights against an ocean.",
       fr="Je regarde Konrad. Il tremble. Des gouttes de sueur sur son front. Derrière ses yeux, un homme lutte contre un océan.",
       es="Miro a Konrad. Está temblando. Gotas de sudor en su frente. Detrás de sus ojos, un hombre lucha contra un océano.",
       it="Guardo Konrad. Trema. Gocce di sudore sulla sua fronte. Dietro i suoi occhi, un uomo lotta contro un oceano.")
    _t(tr, F, "narration_1_helped_konrad",
       en="In the schoolhouse he asked for help when he could barely speak. That promise stands between us now like a burning line.",
       fr="Il m'a demandé de l'aide alors qu'il arrivait à peine à parler. Cette promesse se tient maintenant entre nous comme une ligne brûlante.",
       es="Me pidió ayuda cuando apenas podía hablar. Esa promesa ahora se alza entre nosotros como una línea ardiente.",
       it="Mi ha chiesto aiuto quando riusciva a malapena a parlare. Ora quella promessa sta tra noi come una linea ardente.")
    _t(tr, F, "narration_1_distanced_konrad",
       en="I kept my distance to protect the plan, ever since the square, when something older spoke through him. But now I am here to free him anyway.",
       fr="J'ai gardé mes distances pour protéger le plan, depuis la place, quand quelque chose de plus ancien a parlé à travers lui. Et pourtant je suis ici pour le libérer.",
       es="Mantuve mi distancia para proteger el plan, desde la plaza, cuando algo más antiguo habló por su boca. Y aun así estoy aquí para liberarlo.",
       it="Ho mantenuto le distanze per proteggere il piano, da quella piazza in cui qualcosa di più antico parlò attraverso di lui. Eppure ora sono qui per liberarlo.")
    _t(tr, F, "narration_chose_sacrifice_callback",
       en="This time the decision was not made by a book, not by Otto, and not by tradition. I made it myself.",
       fr="Cette fois, la décision n'a pas été prise par un livre, ni par Otto, ni par la tradition. C'est moi qui l'ai prise.",
       es="Esta vez la decisión no la tomó un libro, ni Otto, ni la tradición. La tomé yo.",
       it="Questa volta la decisione non l'ha presa un libro, né Otto, né la tradizione. L'ho presa io.")

    _t(tr, F, "narration_2",
       en="He taught me to read — no, that was Grandmother. He showed me the guardian tree. He asked for help when no one else did.",
       fr="C'est lui qui m'à appris à lire — non, c'était grand-mère. Il m'à montré l'arbre du gardien. Il à demandé de l'aide quand personne d'autre ne l'à fait.",
       es="Él me enseñó a leer — no, eso fue la abuela. Me mostró el árbol del guardián. Pidió ayuda cuando nadie más lo hizo.",
       it="Mi ha insegnato a leggere — no, quella era la nonna. Mi ha mostrato l'albero del guardiano. Ha chiesto aiuto quando nessun altro lo ha fatto.")

    _t(tr, F, "narration_3",
       en="And I read in Grandmother's journal what the vessel is: a bridge. The entity has relied on a human mind as an anchor in our world. Without that bridge, it thrashes, reaches, and drags others down.",
       fr="Et j'ai lu dans le journal de grand-mère ce qu'est le réceptacle : un pont. L'entité à besoin d'un esprit humain comme ancre dans notre monde. Sans réceptacle, elle ne peut pas rester ici.",
       es="Y leí en el diario de la abuela lo que es el receptáculo: un puente. La entidad necesita una mente humana como ancla en nuestro mundo. Sin receptáculo, no puede permanecer aquí.",
       it="E ho letto nel diario della nonna cos'è il ricettacolo: un ponte. L'entità ha bisogno di una mente umana come àncora nel nostro mondo. Senza ricettacolo, non può restare qui.")

    _t(tr, F, "narration_4",
       en="Konrad was never the vessel willingly. He was chosen before he was born. Selected like a sacrificial lamb.",
       fr="Konrad n'à jamais été le réceptacle de son plein gré. Il à été choisi avant sà naissance. Sélectionné comme un agneau sacrificiel.",
       es="Konrad nunca fue el receptáculo por voluntad propia. Fue elegido antes de nacer. Seleccionado como un cordero de sacrificio.",
       it="Konrad non è mai stato il ricettacolo di sua volontà. È stato scelto prima di nascere. Selezionato come un agnello sacrificale.")

    _t(tr, F, "narration_5",
       en="I step onto the earth sign. I open my mind — not to bind the entity or to worship it, but to make a chosen offer. Into me, on terms I can still speak.",
       fr="Je me place sur le signe de terre. J'ouvre mon esprit — non pour lier l'entité ni pour là comprendre, mais pour l'inviter. En moi.",
       es="Me coloco sobre el signo de la tierra. Abro mi mente — no para atar a la entidad ni para comprenderla, sino para invitarla. Dentro de mí.",
       it="Mi posiziono sul segno della terra. Apro la mia mente — non per legare l'entità né per comprenderla, ma per invitarla. Dentro di me.")

    _t(tr, F, "konrad_2",
       en="Elise, NO! What are you doing?!",
       fr="Elise, NON ! Qu'est-ce que tu fais ?!",
       es="¡Elise, NO! ¿¡Qué estás haciendo!?",
       it="Elise, NO! Che cosa fai?!")

    _t(tr, F, "narration_6",
       en="'I promised to give you your life back, Konrad. This is me keeping it.' My voice sounds calm. Calmer than I feel.",
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
       en="I will stay in Graubach. I take Konrad's place — as teacher and guardian of the boundary. Not as a mindless vessel, but as a negotiating partner with clear rules: no access without consent, no coercion, stop at any time.",
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
       en="Because you deserve to be free. Because Grandmother would have wanted us to choose, not obey. And because I can set boundaries with it — no access without consent, no coercion, stop at any time — without making you pay for it any longer.",
       fr="Parce que tu mérites d'être libre. Parce que grand-mère l'aurait voulu. Et parce que... parce que l'entité à besoin de moi. Et j'ai besoin d'elle.",
       es="Porque mereces ser libre. Porque la abuela lo habría querido. Y porque... porque la entidad me necesita. Y yo la necesito.",
       it="Perché meriti di essere libero. Perché la nonna lo avrebbe voluto. È perché... perché l'entità ha bisogno di me. È io ho bisogno di lei.")
    _t(tr, F, "elise_sacrifice_6",
       en="Live your life, Konrad. You have lost thirty years. Take them back.",
       fr="Vis tà vie, Konrad. Tu as perdu trente ans. Reprends-les.",
       es="Vive tu vida, Konrad. Has perdido treinta años. Recupéralos.",
       it="Vivi la tua vita, Konrad. Hai perso trent'anni. Riprenditeli.")
    # --- Phase 11: Ally reactions after sacrifice ---
    _t(tr, F, "georg_sacrifice_1",
       en="Elise, no! You can't — this is madness! There must be another way!",
       fr="Elise, non ! Tu ne peux pas — c'est de la folie ! Il doit y avoir un autre moyen !",
       es="¡Elise, no! No puedes — ¡esto es una locura! ¡Tiene que haber otro camino!",
       it="Elise, no! Non puoi — è follia! Ci dev'essere un'altra via!")
    _t(tr, F, "elise_georg_sacrifice",
       en="It is not madness, Georg. It is a decision. My decision. Take care of the village.",
       fr="Ce n'est pas de la folie, Georg. C'est une décision. Ma décision. Prends soin du village.",
       es="No es una locura, Georg. Es una decisión. Mi decisión. Cuida del pueblo.",
       it="Non è follia, Georg. È una decisione. La mia decisione. Prenditi cura del villaggio.")
    _t(tr, F, "hilde_sacrifice_1",
       en="You are braver than your grandmother. She would have done it if she could have. I bless you, child.",
       fr="Tu es plus courageuse que ta grand-mère. Elle l'aurait fait si elle avait pu. Je te bénis, mon enfant.",
       es="Eres más valiente que tu abuela. Ella lo habría hecho si hubiera podido. Te bendigo, niña.",
       it="Sei più coraggiosa di tua nonna. L'avrebbe fatto se avesse potuto. Ti benedico, bambina.")
    _t(tr, F, "elise_hilde_sacrifice",
       en="Thank you, Hilde. For everything.",
       fr="Merci, Hilde. Pour tout.",
       es="Gracias, Hilde. Por todo.",
       it="Grazie, Hilde. Per tutto.")
    _t(tr, F, "voss_sacrifice_1",
       en="God be with you, child. What you are doing is... holy. In a way that no prayer can reach.",
       fr="Dieu soit avec toi, mon enfant. Ce que tu fais est... saint. D'une manière qu'aucune prière ne peut atteindre.",
       es="Dios esté contigo, niña. Lo que haces es... sagrado. De una manera que ninguna oración puede alcanzar.",
       it="Dio sia con te, bambina. Quello che fai è... sacro. In un modo che nessuna preghiera può raggiungere.")
    _t(tr, F, "elise_voss_sacrifice",
       en="Pray for me, Pastor. Not for my soul. For my strength.",
       fr="Priez pour moi, Pasteur. Pas pour mon âme. Pour ma force.",
       es="Rece por mí, Pastor. No por mi alma. Por mi fuerza.",
       it="Preghi per me, Pastore. Non per la mia anima. Per la mia forza.")
    _t(tr, F, "narration_sacrifice_solo",
       en="Silence. Only the singing — softer now, more content. No one is here to stop me. No one to comfort me. Only me and the entity that slowly finds its new place.",
       fr="Le silence. Seulement le chant — plus doux maintenant, plus satisfait. Personne n'est là pour m'arrêter. Personne pour me consoler. Seulement moi et l'entité qui trouve lentement sa nouvelle place.",
       es="Silencio. Solo el canto — más suave ahora, más satisfecho. Nadie está aquí para detenerme. Nadie para consolarme. Solo yo y la entidad que lentamente encuentra su nuevo lugar.",
       it="Silenzio. Solo il canto — più sommesso ora, più soddisfatto. Nessuno è qui per fermarmi. Nessuno per consolarmi. Solo io e l'entità che lentamente trova il suo nuovo posto.")
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
    _t(tr, F, "sacrifice_anna_warning_payoff",
       en="You listened when I warned you about him — and later you listened when I said there was still a person inside him. You held both truths. That is why this worked.",
       fr="Tu as écouté quand je t'ai mise en garde contre lui — puis tu as écouté quand j'ai dit qu'il y avait encore une personne en lui. Tu as tenu les deux vérités. C'est pour ça que ça a marché.",
       es="Escuchaste cuando te advertí sobre él, y después escuchaste cuando dije que aún había una persona dentro. Sostuviste ambas verdades. Por eso funcionó.",
       it="Hai ascoltato quando ti ho avvertita su di lui — e poi hai ascoltato quando ho detto che dentro c'era ancora una persona. Hai tenuto insieme entrambe le verità. Per questo ha funzionato.")
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

    # --- Phase 11: Epilog transition ---
    _t(tr, F, "sacrifice_epilog_transition",
       en="Days become weeks. Weeks become months. I learn to live with my guest. And my guest learns not to devour me.",
       fr="Les jours deviennent des semaines. Les semaines des mois. J'apprends à vivre avec mon hôte. Et mon hôte apprend à ne pas me dévorer.",
       es="Los días se convierten en semanas. Las semanas en meses. Aprendo a vivir con mi huésped. Y mi huésped aprende a no devorarme.",
       it="I giorni diventano settimane. Le settimane mesi. Imparo a vivere con il mio ospite. E il mio ospite impara a non divorarmi.")
    # --- Phase 9 Story-Fixes: Epilog nodes + trusted_konrad ---
    _t(tr, F, "sacrifice_anna_epilog",
       en="Anna understands it first. 'The singing sounds different,' she whispers. 'Warmer. Like a conversation.' She places her hand on Elise's shoulder.",
       fr="Anna comprend la première. « Le chant sonne différemment », murmure-t-elle. « Plus chaud. Comme une conversation. » Elle pose sa main sur l'épaule d'Elise.",
       es="Anna lo entiende primero. 'El canto suena diferente', susurra. 'Más cálido. Como una conversación.' Pone su mano en el hombro de Elise.",
       it="Anna lo capisce per prima. 'Il canto suona diverso', sussurra. 'Più caldo. Come una conversazione.' Posa la mano sulla spalla di Elise.")
    _t(tr, F, "sacrifice_otto_epilog",
       en="Otto never understands. He leaves because the tradition no longer makes sense. His last glance back is empty.",
       fr="Otto ne comprend jamais. Il part parce que la tradition n'a plus de sens. Son dernier regard en arrière est vide.",
       es="Otto nunca lo entiende. Se va porque la tradición ya no tiene sentido. Su última mirada atrás está vacía.",
       it="Otto non capisce mai. Se ne va perché la tradizione non ha più senso. Il suo ultimo sguardo indietro è vuoto.")
    _t(tr, F, "sacrifice_sought_konrad_memory",
       en="I hear his words from the schoolhouse again — help me before it has me completely. Seeking him out was risky, but that look carried me all the way to this altar.",
       fr="Je réentends ses mots de l'école — aide-moi avant qu'il ne m'ait complètement. Le chercher était risqué, mais ce regard m'a portée jusqu'à cet autel.",
       es="Vuelvo a oír sus palabras en la escuela: ayúdame antes de que me tenga por completo. Buscarlo fue arriesgado, pero esa mirada me trajo hasta este altar.",
       it="Risento le sue parole nell'aula: aiutami prima che mi abbia del tutto. Cercarlo è stato rischioso, ma quello sguardo mi ha portata fino a questo altare.")
    _t(tr, F, "sacrifice_avoided_konrad_memory",
       en="I avoided him to protect the plan. That distance hurt us both — and that is exactly why I know what this freedom costs, and why I owe it to him.",
       fr="Je l'ai évité pour protéger le plan. Cette distance nous a blessés tous les deux — et c'est justement pour cela que je sais ce que coûte cette liberté, et pourquoi je la lui dois.",
       es="Lo evité para proteger el plan. Esa distancia nos hirió a los dos — y justo por eso sé lo que cuesta esta libertad y por qué se la debo.",
       it="L'ho evitato per proteggere il piano. Quella distanza ha ferito entrambi — ed è proprio per questo che so quanto costa questa libertà e perché gliela devo.")
    _t(tr, F, "konrad_trusted_sacrifice",
       en="You believed me. At the village square, when all the others feared me. You looked at me and saw a person, not a monster.",
       fr="Tu m'as cru. Sur la place du village, quand tous les autres me craignaient. Tu m'as regardé et tu as vu un être humain, pas un monstre.",
       es="Me creíste. En la plaza del pueblo, cuando todos los demás me temían. Me miraste y viste a una persona, no a un monstruo.",
       it="Mi hai creduto. Nella piazza del villaggio, quando tutti gli altri mi temevano. Mi hai guardato e hai visto una persona, non un mostro.")
    _t(tr, F, "konrad_tested_sacrifice",
       en="You did not trust me blindly. Since that evening with the spirals, you weighed every reaction so caution would not turn into coldness. And still you do this for me.",
       fr="Tu ne m'as pas fait confiance aveuglément. Depuis ce soir avec les spirales, tu as évalué chaque réaction pour que la prudence ne devienne pas froideur. Et malgré ça, tu fais ça pour moi.",
       es="No confiaste en mí a ciegas. Desde aquella noche de las espirales, evaluaste cada reacción para que la cautela no se volviera frialdad. Y aun así haces esto por mí.",
       it="Non ti sei fidata ciecamente di me. Da quella sera delle spirali hai valutato ogni reazione perché la prudenza non diventasse freddezza. E nonostante questo, lo fai per me.")
    _t(tr, F, "konrad_distrusted_sacrifice",
       en="You kept me at arm's length to protect your plan. After what spoke through my mouth at the fountain, that was not betrayal — it was self-protection. And now you still give everything to set me free.",
       fr="Tu m'as tenu à distance pour protéger ton plan. Après ce qui a parlé par ma bouche à la fontaine, ce n'était pas une trahison — c'était de la protection. Et maintenant tu donnes quand même tout pour me libérer.",
       es="Me mantuviste a distancia para proteger tu plan. Después de lo que habló por mi boca en la fuente, eso no fue traición — fue protección. Y aun así ahora lo das todo para liberarme.",
       it="Mi hai tenuto a distanza per proteggere il tuo piano. Dopo ciò che ha parlato dalla mia bocca alla fontana, non era tradimento — era autodifesa. E ora dai comunque tutto per liberarmi.")
    _t(tr, F, "konrad_untrusted_sacrifice",
       en="You barely knew me. And yet... why? Why for me?",
       fr="Tu me connaissais à peine. Et pourtant... pourquoi ? Pourquoi pour moi ?",
       es="Apenas me conocías. Y sin embargo... ¿por qué? ¿Por qué por mí?",
       it="Mi conoscevi appena. Eppure... perché? Perché per me?")

    # --- Phase 10 Story-Konsistenz-Fixes ---
    _t(tr, F, "sacrifice_candle_epilog",
       en="In Grandmother's house, the candle burns on. But its light is warmer now, more golden. As though it knows that Elise has stayed.",
       fr="Dans la maison de grand-mère, la bougie continue de brûler. Mais sa lumière est plus chaude maintenant, plus dorée. Comme si elle savait qu'Elise est restée.",
       es="En la casa de la abuela, la vela sigue ardiendo. Pero su luz es más cálida ahora, más dorada. Como si supiera que Elise se ha quedado.",
       it="Nella casa della nonna, la candela continua a bruciare. Ma la sua luce è più calda ora, più dorata. Come se sapesse che Elise è rimasta.")

    _t(tr, F, "sacrifice_mathilde_epilog",
       en="Mathilde, the blind woman from the train, survived the ritual sixty years ago. Alone, forgotten. I will not be forgotten.",
       fr="Mathilde, la femme aveugle du train, a survécu au rituel il y a soixante ans. Seule, oubliée. Je ne serai pas oubliée.",
       es="Mathilde, la mujer ciega del tren, sobrevivió al ritual hace sesenta años. Sola, olvidada. Yo no seré olvidada.",
       it="Mathilde, la donna cieca del treno, sopravvisse al rituale sessant'anni fa. Sola, dimenticata. Io non sarò dimenticata.")

    _t(tr, F, "packed_books_sacrifice",
       en="My books now stand on Grandmother's shelf. Elise reads them sometimes, when the entity sleeps. Folklore has taken on a new meaning - no longer study. Living experience.",
       fr="Mes livres sont maintenant sur l'étagère de grand-mère. Elise les lit parfois, quand l'entité dort. Le folklore a pris un nouveau sens - non plus une étude. Une expérience vécue.",
       es="Mis libros ahora están en la estantería de la abuela. Elise los lee a veces, cuando la entidad duerme. El folklore ha adquirido un nuevo significado - ya no es estudio. Experiencia vivida.",
       it="I miei libri ora stanno sullo scaffale della nonna. Elise li legge a volte, quando l'entità dorme. Il folklore ha assunto un nuovo significato - non più studio. Esperienza vissuta.")

    _t(tr, F, "packed_cross_sacrifice",
       en="The crucifix hangs above the bed. Sometimes, when the entity gazes at the cross through Elise's eyes, she feels its curiosity. It knows no gods. But it understands the comfort.",
       fr="Le crucifix est accroché au-dessus du lit. Parfois, quand l'entité regarde la croix à travers les yeux d'Elise, elle sent sa curiosité. Il ne connaît pas de dieux. Mais il comprend le réconfort.",
       es="El crucifijo cuelga sobre la cama. A veces, cuando la entidad mira la cruz a través de los ojos de Elise, ella siente su curiosidad. No conoce dioses. Pero comprende el consuelo.",
       it="Il crocifisso è appeso sopra il letto. A volte, quando l'entità guarda la croce attraverso gli occhi di Elise, lei ne sente la curiosità. Non conosce dèi. Ma comprende il conforto.")

    _t(tr, F, "packed_camera_sacrifice",
       en="The camera sits dusty on the shelf. Elise no longer photographs. Why would she? What she sees, no lens can capture. But sometimes, in clear moments, she captures the world in words.",
       fr="L'appareil photo repose, poussiéreux, sur l'étagère. Elise ne photographie plus. À quoi bon ? Ce qu'elle voit, aucun objectif ne peut le saisir. Mais parfois, dans les moments de clarté, elle capture le monde en mots.",
       es="La cámara reposa polvorienta en la estantería. Elise ya no fotografía. ¿Para qué? Lo que ve, ningún lente puede captarlo. Pero a veces, en momentos de lucidez, captura el mundo en palabras.",
       it="La macchina fotografica giace impolverata sullo scaffale. Elise non fotografa più. Perché dovrebbe? Ciò che vede, nessun obiettivo può catturarlo. Ma a volte, nei momenti di lucidità, cattura il mondo in parole.")


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
    # --- Phase 11: Renamed node for ally dialogue ---
    _t(tr, F, "elise_awake_fight_ally",
       en="You are right. I will try again. I MUST try.",
       fr="Tu as raison. Je vais réessayer. Je DOIS essayer.",
       es="Tienes razón. Lo intentaré otra vez. DEBO intentarlo.",
       it="Hai ragione. Riproverò. DEVO provarci.")
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

    # --- Phase 9b: Konrad epilog ---
    _t(tr, F, "awakening_konrad_epilog",
       en="Konrad stands in the middle of the village square. He smiles. The spirals on his hands glow. For the first time he is no longer a vessel — he is a bridge. The entity flows through him into the world, and Konrad lets it happen. Thirty years of struggle, and in the end he surrenders — not from weakness, but from exhaustion.",
       fr="Konrad se tient au milieu de la place du village. Il sourit. Les spirales sur ses mains brillent. Pour la première fois, il n'est plus un réceptacle — il est un pont. L'entité coule à travers lui dans le monde, et Konrad la laisse faire. Trente ans de lutte, et à la fin il se rend — non par faiblesse, mais par épuisement.",
       es="Konrad está en medio de la plaza del pueblo. Sonríe. Las espirales en sus manos brillan. Por primera vez ya no es un receptáculo — es un puente. La entidad fluye a través de él hacia el mundo, y Konrad lo permite. Treinta años de lucha, y al final se rinde — no por debilidad, sino por agotamiento.",
       it="Konrad è in mezzo alla piazza del villaggio. Sorride. Le spirali sulle sue mani brillano. Per la prima volta non è più un ricettacolo — è un ponte. L'entità fluisce attraverso di lui nel mondo, e Konrad lo lascia accadere. Trent'anni di lotta, e alla fine si arrende — non per debolezza, ma per stanchezza.")
    # --- Phase 9 Story-Fixes: Epilog nodes ---
    _t(tr, F, "awakening_anna_epilog",
       en="Anna smiles. She always knew. 'It only wanted to be seen,' she whispers as the walls open.",
       fr="Anna sourit. Elle a toujours su. « Il voulait seulement être vu », murmure-t-elle tandis que les murs s'ouvrent.",
       es="Anna sonríe. Siempre lo supo. 'Solo quería ser visto', susurra mientras las paredes se abren.",
       it="Anna sorride. L'ha sempre saputo. 'Voleva solo essere visto', sussurra mentre le pareti si aprono.")
    _t(tr, F, "awakening_otto_epilog",
       en="Otto's commands fade away. His system of power — meaningless before something older than power.",
       fr="Les ordres d'Otto se perdent. Son système de pouvoir — sans signification face à quelque chose de plus ancien que le pouvoir.",
       es="Las órdenes de Otto se desvanecen. Su sistema de poder — insignificante ante algo más antiguo que el poder.",
       it="Gli ordini di Otto svaniscono. Il suo sistema di potere — insignificante davanti a qualcosa di più antico del potere.")

    # --- Phase 10 Story-Konsistenz-Fixes ---
    _t(tr, F, "awakening_candle_epilog",
       en="The candle on the nightstand flares - a wild, hungry flame - and then goes out with a hiss, as though someone had blown it out.",
       fr="La bougie sur la table de nuit s'embrase - une flamme sauvage, affamée - puis s'éteint avec un sifflement, comme si quelqu'un l'avait soufflée.",
       es="La vela en la mesita de noche llamea - una llama salvaje, hambrienta - y luego se apaga con un siseo, como si alguien la hubiera soplado.",
       it="La candela sul comodino divampa - una fiamma selvaggia, affamata - e poi si spegne con un sibilo, come se qualcuno l'avesse soffiata.")

