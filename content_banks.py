"""Extra, authored content for random short sessions. All texts are original."""
EXTRA={}
def E(id,questions,pairs,story):EXTRA[id]={'questions':questions,'pairs':pairs,'story':story}
E('be',[
'''My tablet ___ in my bag.|is|are~am
The players ___ excited.|are|is~am
I ___ good at drawing.|am|is~are
Our classroom ___ quiet.|is|are~am
Your shoes ___ blue.|are|is~am
You ___ a good listener.|are|is~am''',
'''___ the books on the shelf?|Are|Is~Am
She ___ not in our group.|is|are~am
___ I too early?|Am|Is~Are
Yes, we ___.|are|is~am
___ your phone fully charged?|Is|Are~Am
My parents ___ not at home.|are|is~am''',
'''Each of these rooms ___ different.|is|are~am
The number of players ___ six.|is|are~am
A pair of socks ___ on the floor.|is|are~am
Both of my cousins ___ here.|are|is~am
Someone ___ waiting outside.|is|are~am
My favourite thing about these games ___ the stories.|is|are~am'''
],'''Alex ___|Alex is|0
my cousins ___|my cousins are|0
I am not → kortform|I’m not|0
you are → kortform|you’re|0
we are not → kortform|we aren’t|1
he is → kortform|he’s|1
Is the game fun? → positivt kort svar|Yes, it is.|1
Are they here? → negativt kort svar|No, they aren’t.|1
everyone ___|everyone is|2
each student ___|each student is|2
both teams ___|both teams are|2
one of my friends ___|one of my friends is|2''',('I {0} in a school band. Our singer {1} fifteen. The other players {2} my friends. You {3} welcome at our concert. Our teacher {4} proud of us. We {5} excited about Friday.',['am','is','are','are','is','are']))
E('pastbe',[
'''The café ___ closed yesterday.|was|were~are
My shoes ___ wet after the walk.|were|was~is
I ___ busy last night.|was|were~are
You ___ right about the film.|were|was~is
Our teacher ___ away last Tuesday.|was|were~are
We ___ excited before the trip.|were|was~is''',
'''___ the shops open yesterday?|Were|Was~Is
It ___ not cold last Sunday.|was|were~are
___ she in your class last year?|Was|Were~Are
Yes, we ___. We went together.|were|was~is
They ___ not angry after the match.|were|was~is
___ I late yesterday?|Was|Were~Am''',
'''Everyone ___ tired after the hike.|was|were~are
Both answers ___ wrong in yesterday’s quiz.|were|was~is
The information ___ useful yesterday.|was|were~are
One of the doors ___ locked last night.|was|were~are
There ___ no seats left yesterday.|were|was~is
Each visitor ___ given a map last Saturday.|was|were~are'''
],'''I am tired → i går|I was tired|0
Alex → i går|Alex was|0
my friends → i går|my friends were|0
You are ready → i går|You were ready|0
he was not → kortform|he wasn’t|1
we were not → kortform|we weren’t|1
Was she there? → positivt svar|Yes, she was.|1
Were they ready? → negativt svar|No, they weren’t.|1
everyone → i går|everyone was|2
both teams → i går|both teams were|2
one student → i går|one student was|2
the information → i går|the information was|2''',('Last weekend {0} exciting. I {1} at a concert. My friends {2} there too. The singer {3} amazing. The songs {4} familiar. We {5} happy when we went home.',['was','was','were','was','were','were']))
E('have',[
'''The dog ___ a new toy.|has|have~are
My friends ___ a plan.|have|has~is
I ___ two sisters.|have|has~is
The library ___ many books.|has|have~are
You ___ a nice jacket.|have|has~is
We ___ a free afternoon.|have|has~is''',
'''Does the school ___ a library?|have|has~having
She doesn’t ___ much free time.|have|has~having
Do you ___ any questions?|have|has~having
My cousin ___ a small garden.|has|have~having
They don’t ___ tickets yet.|have|has~having
The café ___ good sandwiches.|has|have~having''',
'''We ___ got enough chairs.|have|has~does
___ your cousins got a dog?|Have|Has~Do
She hasn’t ___ her notebook today.|got|have~has
Do your friends ___ their own bikes?|have|has~got
___ he got a map of the city?|Has|Have~Does
I ___ got a great idea.|have|has~does'''
],'''you ___|you have|0
we ___|we have|0
my friend ___|my friend has|0
the dog ___|the dog has|0
do you …?|have a ticket|1
she doesn’t …|have a helmet|1
does he …?|have time|1
they don’t …|have any questions|1
have you …?|got a pen|2
she has not got → kortform|she hasn’t got|2
we have got → kortform|we’ve got|2
he has got → kortform|he’s got|2''',('We {0} a photography club. Maya {1} a camera. Leo and Sam {2} their phones. Our teacher {3} some useful books. I {4} a notebook. The school {5} a printer for our photos.',['have','has','have','has','have','has']))
E('pronouns',[
'''Leo is outside. ___ is waiting.|He|Him~His
Please give the ball to ___.|me|I~my
My sisters are here. ___ are smiling.|They|Them~Their
Maya called Alex. She called ___.|him|he~his
This is ___ seat; it belongs to us.|our|us~we
We are looking for Sara. Have you seen ___?|her|she~hers''',
'''These keys are ___. They belong to us.|ours|our~us
That is ___ jacket. It belongs to you.|your|yours~you
The bikes are ___. They belong to the neighbours.|theirs|their~them
This is my brother. I like ___ new haircut.|his|he~him
The robot uses ___ camera to find the door.|its|it’s~it
This hat is Leo’s. It is ___.|his|him~he''',
'''She made the cake ___.|herself|her~hers
You should be proud of ___.|yourself|you~yours
The machine switches ___ off at night.|itself|its~it’s
My friends introduced ___ to the new teacher.|themselves|themself~theirselves
___ been a difficult week.|It’s|Its~It
The decision is ___; we must make it together.|ours|our~us'''
],'''she → objekt|her|0
they → ägande före ett namn på en sak|their|0
we → ägande före ett namn på en sak|our|0
you → ägande före ett namn på en sak|your|0
your book → utan book|yours|1
our house → utan house|ours|1
their bikes → utan bikes|theirs|1
his coat → utan coat|his|1
I → sig själv|myself|2
she → sig själv|herself|2
we → oss själva|ourselves|2
they → sig själva|themselves|2''',('Leo is my cousin. {0} is in a band. I often listen to {1}. The other musicians bring {2} instruments. They invite {3} to concerts; we love music. Leo has {4} own guitar. The red notebook is {5}; it belongs to me.',['He','him','their','us','his','mine']))
E('articles',[
'''She has ___ camera.|a|an
I need ___ orange.|an|a
He is ___ student.|a|an
We saw ___ owl.|an|a
This is ___ useful book.|a|an
That is ___ old map.|an|a''',
'''I found a key. ___ key was silver.|The|An
We adopted a cat. ___ cat is very shy.|The|An
I watched a match. ___ match ended late.|The|An
There is a café nearby. ___ café opens at eight.|The|An
She gave me a photo. ___ photo was beautiful.|The|An
I heard a noise. ___ noise came from the garden.|The|An''',
'''We waited for ___ hour.|an|a
She is ___ European student.|a|an
That is ___ unusual name.|an|a
I have ___ one-way ticket.|a|an
He wants to be ___ actor.|an|a
We visited ___ historic building.|a|an'''
],'''___ student|a student|0
___ egg|an egg|0
___ camera|a camera|0
___ owl|an owl|0
___ umbrella|an umbrella|1
___ useful idea|a useful idea|1
___ old jacket|an old jacket|1
___ new phone|a new phone|1
___ honest answer|an honest answer|2
___ hour|an hour|2
___ European city|a European city|2
___ one-way ticket|a one-way ticket|2''',('We went to {0} café after school. {1} café was quiet. I ordered {2} sandwich. Maya had {3} orange. We sat near {4} open window. {5} window faced the park.',['a','The','a','an','an','The']))
E('plurals',[
'''One chair, four ___.|chairs|chaires~chair
One fox, two ___.|foxes|foxs~fox
One class, three ___.|classes|classs~class
One desk, ten ___.|desks|deskes~desk
One match, two ___.|matches|matchs~match
One pen, six ___.|pens|penes~pen''',
'''One story, three ___.|stories|storys~storyes
One key, two ___.|keys|keies~keyes
One man, four ___.|men|mans~manes
One baby, two ___.|babies|babys~babyes
One family, three ___.|families|familys~familyes
One child, several ___.|children|childs~childes''',
'''One wolf, three ___.|wolves|wolfs~wolfes
One half, two ___.|halves|halfs~halfes
One deer, five ___.|deer|deers~deeres
One goose, two ___.|geese|gooses~goose
One scarf, several ___.|scarves|scarfses~scarveses
One shelf, four ___.|shelves|shelfs~shelfes'''
],'''book|books|0
chair|chairs|0
bus|buses|0
box|boxes|0
woman|women|1
man|men|1
foot|feet|1
baby|babies|1
mouse|mice|2
leaf|leaves|2
wolf|wolves|2
shelf|shelves|2''',('Our art room has four {0} (table). There are twelve {1} (chair). Two {2} (woman) teach here. We keep paints in {3} (box). Some students draw {4} (fox). Others paint pictures of {5} (city).',['tables','chairs','women','boxes','foxes','cities']))
E('present',[
'''He ___ his room every Sunday.|cleans|clean~cleaning
I ___ comics after school.|read|reads~reading
The café ___ at eight every day.|opens|open~opening
They ___ chess on Fridays.|play|plays~playing
She ___ near the library.|lives|live~living
We ___ our friends every weekend.|visit|visits~visiting''',
'''My cousin ___ the bus every morning.|catches|catchs~catch
She ___ her hands before lunch.|washes|washs~wash
He ___ his sister with homework.|helps|help~helping
I don’t ___ TV in the morning.|watch|watches~watching
Our teacher ___ us new words.|teaches|teachs~teach
Leo doesn’t ___ spicy food.|like|likes~liking''',
'''Each player ___ a different role.|has|have~having
The girl in the blue trainers ___ very fast.|runs|run~running
Both of my cousins ___ in the same town.|live|lives~living
Someone always ___ the door open.|leaves|leave~leaving
The train usually ___ at platform two.|stops|stop~stopping
My favourite band ___ a concert here every year.|plays|play~playing'''
],'''read → she|reads|0
walk → he|walks|0
like → she|likes|0
work → he|works|0
wash → she|washes|1
catch → he|catches|1
carry → she|carries|1
try → he|tries|1
fly → it|flies|2
fix → she|fixes|2
miss → he|misses|2
teach → she|teaches|2''',('Sam {0} (live) near school. He {1} (cycle) there every day. His friends {2} (walk). Sam {3} (like) science. He {4} (watch) science videos after dinner. We often {5} (talk) about them in class.',['lives','cycles','walk','likes','watches','talk']))
E('do',[
'''___ we need our books today?|Do|Does~Is
___ your sister like films?|Does|Do~Are
___ I have the right address?|Do|Does~Am
She ___ not live nearby.|does|do~are
They ___ not know the answer.|do|does~is
___ the café open on Sundays?|Does|Do~Are''',
'''Did she ___ her lunch yesterday?|bring|brought~brings
He didn’t ___ the question.|understand|understood~understands
Does your friend ___ here?|work|works~working
___ you see the rainbow yesterday?|Did|Does~Are
We don’t ___ much TV.|watch|watches~watched
What did they ___ after school?|do|did~does''',
'''No, he ___. He doesn’t live here.|doesn’t|don’t~isn’t
Yes, I ___. I saw it yesterday.|did|does~am
___ the students tired now?|Are|Do~Does
___ she at the library yesterday?|Was|Did~Does
Why does he always ___ late?|arrive|arrives~arrived
When did your cousins ___ back?|come|came~comes'''
],'''you play → fråga|Do you play?|0
she plays → fråga|Does she play?|0
we like it → fråga|Do we like it?|0
he knows → neka|He doesn’t know.|0
I went → fråga|Did I go?|1
she came → neka|She didn’t come.|1
Did you win? → positivt svar|Yes, I did.|1
Do they work here? → negativt svar|No, they don’t.|1
you are ready → fråga|Are you ready?|2
he was late → fråga|Was he late?|2
she can swim → fråga|Can she swim?|2
Does he live here? → positivt svar|Yes, he does.|2''',('Maya likes chess. {0} she play at school? Yes, she does. Her friends {1} not know all the rules. Yesterday they {2} not finish their game. {3} Maya win yesterday? Nobody won. Does she {4} (want) to try again? Yes. Her friends do not {5} (mind) playing another game.',['Does','do','did','Did','want','mind']))
E('continuous',[
'''We ___ learning a new song now.|are|is~am
I am ___ for my friend.|waiting|wait~waits
She is ___ to her sister now.|talking|talk~talks
He ___ drawing a map right now.|is|are~am
They are ___ their bags now.|packing|pack~packs
You ___ listening very carefully now.|are|is~am''',
'''He is ___ a cake right now.|baking|bakeing~bakes
She is ___ in the pool now.|swimming|swiming~swims
___ you coming with us now?|Are|Is~Do
They aren’t ___ the film right now.|watching|watch~watches
I am ___ my friend at the moment.|helping|help~helps
The dog is ___ under the tree now.|lying|lieing~lies''',
'''Look! The children ___ a snowman.|are building|builds~is building
I ___ what you mean.|understand|am understanding~understands
We usually cycle, but today we ___ home.|are walking|is walking~walks
She ___ that it is a good idea.|believes|is believing~believe
He ___ at his cousin’s house this weekend.|is staying|are staying~staying
Listen! The birds ___.|are singing|is singing~singing'''
],'''play → -ing|playing|0
walk → -ing|walking|0
listen → -ing|listening|0
talk → -ing|talking|0
bake → -ing|baking|1
stop → -ing|stopping|1
dance → -ing|dancing|1
shop → -ing|shopping|1
lie → -ing|lying|2
tie → -ing|tying|2
begin → -ing|beginning|2
travel → -ing (brittisk stavning)|travelling|2''',('It is Saturday afternoon. We are {0} (prepare) a meal. Sam is {1} (cut) tomatoes. Maya is {2} (make) a salad. I am {3} (bake) bread. Leo is {4} (set) the table. Everyone is {5} (help).',['preparing','cutting','making','baking','setting','helping']))
E('past',[
'''She ___ the door a minute ago.|opened|open~opens
We ___ to music last night.|listened|listen~listens
I ___ the bus yesterday.|missed|miss~misses
They ___ their friend last Sunday.|visited|visit~visits
He ___ for the train yesterday.|waited|wait~waits
We ___ in the park last Saturday.|walked|walk~walks''',
'''She ___ a bus to town yesterday.|took|taked~take
I ___ a coin on the floor last night.|found|finded~find
We ___ a new friend last summer.|met|meeted~meet
He ___ football with us yesterday.|played|play~plays
Did they ___ the train?|catch|caught~catches
I didn’t ___ your message yesterday.|read|reading~reads''',
'''The dog ___ across the garden a moment ago.|ran|runned~run
He ___ me his bike yesterday.|lent|lended~lend
I ___ the glass by accident last night.|broke|breaked~broken
They ___ the wrong bus yesterday.|chose|choosed~chosen
She ___ her umbrella home last night.|took|taken~taked
We ___ the problem during yesterday’s lesson.|solved|solve~solves'''
],'''walk → dåtid|walked|0
help → dåtid|helped|0
visit → dåtid|visited|0
listen → dåtid|listened|0
have → dåtid|had|1
meet → dåtid|met|1
find → dåtid|found|1
bring → dåtid|brought|1
run → dåtid|ran|2
break → dåtid|broke|2
choose → dåtid|chose|2
lend → dåtid|lent|2''',('Yesterday we {0} (plan) a class party. We {1} (choose) a date. Maya {2} (write) a list. Leo {3} (bring) some ideas. We {4} (discuss) the food. Our teacher {5} (say) yes to our plan.',['planned','chose','wrote','brought','discussed','said']))
E('perfect',[
'''We ___ started a new project.|have|has~are
He ___ opened the window.|has|have~is
I have ___ my friend.|called|call~calling
They have ___ the tickets.|booked|book~booking
She ___ painted her room.|has|have~is
You have ___ a lot today.|worked|work~working''',
'''I have ___ my keys.|lost|lose~losed
She has never ___ a horse.|ridden|rode~ride
They have ___ a new game.|bought|buyed~buy
Have you ___ this song before?|heard|hear~heared
He hasn’t ___ his bag yet.|found|find~finded
We have already ___ our lunch.|eaten|ate~eat''',
'''They have lived here ___ six months.|for|since~from
I have played chess ___ I was seven.|since|for~during
She ___ that song last night.|sang|has sung~have sung
We ___ just arrived, so our bags are still packed.|have|has~are
He has worked here ___ September.|since|for~during
Have you read the new book ___?|yet|since~for'''
],'''play → particip|played|0
visit → particip|visited|0
finish → particip|finished|0
help → particip|helped|0
lose → particip|lost|1
buy → particip|bought|1
find → particip|found|1
hear → particip|heard|1
ride → particip|ridden|2
break → particip|broken|2
choose → particip|chosen|2
speak → particip|spoken|2''',('We have {0} (choose) a book for our reading club. I have {1} (read) the first chapter. Maya has {2} (write) some notes. Leo has {3} (find) an interesting question. We have {4} (talk) about the characters. Our teacher has {5} (suggest) another book for next month.',['chosen','read','written','found','talked','suggested']))
E('future',[
'''He ___ going to paint his room tomorrow.|is|are~am
They ___ going to walk home later.|are|is~am
I am going to ___ a cake tomorrow.|bake|bakes~baked
We will ___ at seven tomorrow.|start|starts~started
She will ___ us later.|join|joins~joined
You are going to ___ a great time.|have|has~had''',
'''I’ve made a plan. I’m ___ read every evening.|going to|will~going
I can see you’re lost. I ___ show you the way.|will|am going~going to
He is going to ___ his cousin tomorrow.|visit|visits~visited
I promise I ___ help you tomorrow.|will|am going~going
We ___ be late; we promise.|won’t|willn’t~not will
Is she ___ to bring her guitar?|going|will~goes''',
'''They ___ arriving at ten tomorrow; their tickets are booked.|are|is~will
We’ll leave when the rain ___.|stops|will stop~stopped
I’ll tell you as soon as I ___ the answer.|know|will know~knew
She ___ meeting her coach tomorrow at three.|is|are~will
If you need help tomorrow, I ___ be here.|will|am~going
We’ll eat before we ___ home tonight.|go|will go~went'''
],'''you will → kortform|you’ll|0
we will → kortform|we’ll|0
they will → kortform|they’ll|0
he will → kortform|he’ll|0
it will → kortform|it’ll|1
I am going to → kortform|I’m going to|1
you are going to → kortform|you’re going to|1
she is going to → kortform|she’s going to|1
when I … (framtid)|arrive|2
as soon as she … (framtid)|finishes|2
before we … (framtid)|leave|2
until he … (framtid)|comes|2''',('Next weekend I am going to {0} (visit) my cousin. She {1} going to meet me at the station. We {2} going to watch a match. My brother {3} going to join us. We will {4} (bring) our own lunch. I will {5} (take) photos for our family.',['visit','is','are','is','bring','take']))
E('adjectives',[
'''The water is ___.|cold|coldly~colds
They live in a ___ house.|small|smallly~smalls
He has ___ shoes.|red|reds~redly
That is a ___ question.|difficult|difficulty~difficultly
My neighbours are ___.|kind|kindlyly~kinds
The film was ___.|funny|funnily~funnies''',
'''My street is ___ than yours.|quieter|quietest~more quieter
This is the ___ route to school.|shortest|shorter~more shortest
Her room is ___ than mine.|larger|largest~more larger
That game is ___ than this one.|more exciting|most exciting~excitinger
The soup tastes ___ today than yesterday.|better|best~gooder
This is the ___ answer of all.|best|better~goodest''',
'''His bag is ___ than mine.|heavier|heavyer~more heavier
This chair is as ___ as that one.|comfortable|more comfortable~most comfortable
The train is ___ expensive than flying.|less|least~few
That was the ___ question in the quiz.|easiest|easyest~most easiest
Today is much ___ than yesterday.|colder|more colder~coldest than
The first route is ___ than the second.|safer|safest~more safer'''
],'''cold → jämförelse|colder|0
short → jämförelse|shorter|0
long → jämförelse|longer|0
fast → jämförelse|faster|0
heavy → jämförelse|heavier|1
easy → jämförelse|easier|1
large → jämförelse|larger|1
hot → jämförelse|hotter|1
comfortable → jämförelse|more comfortable|2
expensive → mest|most expensive|2
good → mest|best|2
bad → mest|worst|2''',('Our class is planning a trip. The bus is {0} (cheap) than the train. The train is {1} (fast) than the bus. The new museum is {2} (big) than the old one. Its café is the {3} (quiet) place in the building. Maya thinks the museum is {4} (interesting) than the cinema. Leo thinks the cinema is the {5} (good) choice.',['cheaper','faster','bigger','quietest','more interesting','best']))
E('adverbs',[
'''He closed the door ___.|quietly|quiet~quiets
She explained the rule ___.|clearly|clear~clears
Please carry the glass ___.|carefully|careful~cares
He waved ___.|happily|happy~happiness
The classroom is ___.|quiet|quietly~quiets
They finished the task ___.|quickly|quick~quicks''',
'''She sings very ___.|well|good~goodly
He is a ___ musician.|good|well~goodly
The train travels ___.|fast|fastly~fasts
Our team works ___.|hard|hardly~hardlyly
Please speak ___.|slowly|slow~slows
That is a ___ explanation.|clear|clearly~clearness''',
'''I can ___ see the screen from here.|hardly|hard~hardlyly
She is ___ early for lessons.|usually|usual~usuals
He ___ forgets his keys.|never|neverly~nevers
This bread tastes ___.|good|well~goodly
The students answered ___.|politely|polite~polites
The room looks ___.|clean|cleanly~cleans'''
],'''quiet → hur?|quietly|0
quick → hur?|quickly|0
clear → hur?|clearly|0
loud → hur?|loudly|0
polite → hur?|politely|1
easy → hur?|easily|1
angry → hur?|angrily|1
bad → hur?|badly|1
knappt (adverb)|hardly|2
vanligtvis (adverb)|usually|2
alltid (frekvensord)|always|2
aldrig (frekvensord)|never|2''',('Sam is a {0} (quiet/quietly) person. He speaks {1} (quiet/quietly). Maya is a {2} (good/well) singer. She sings {3} (good/well). Leo reads {4} (quick/quickly). They all listen {5} (careful/carefully) when someone needs help.',['quiet','quietly','good','well','quickly','carefully']))
E('prepositions',[
'''The pencils are ___ the box, inside it.|in|on~under
The bag is ___ the chair, below it.|under|in~on
Your phone is ___ top of the shelf.|on|in~under
The table is ___ the two windows.|between|in~under
The library is next ___ the school.|to|in~on
A photo hangs ___ the classroom wall.|on|in~under''',
'''We meet ___ Friday.|on|at~in
The film starts ___ half past six.|at|on~in
We go swimming ___ the morning.|in|at~on
The school closes ___ July.|in|on~at
My birthday is ___ 12 May.|on|at~in
I often read ___ night.|at|on~in''',
'''She jumped ___ the pool from the side.|into|on~at
We walked ___ the forest to reach the lake.|through|on~between
He ran ___ the road to the other side.|across|in~between
They are interested ___ science.|in|on~at
She is very good ___ drawing.|at|on~to
Who are you waiting ___?|for|on~at'''
],'''___ the box (inuti)|in the box|0
___ the chair (under)|under the chair|0
___ the shelf (på)|on the shelf|0
___ two windows (mellan)|between two windows|0
___ Friday|on Friday|1
___ June|in June|1
___ nine o’clock|at nine o’clock|1
___ the evening|in the evening|1
rörelse in i ett rum|into the room|2
från ena sidan av en bro till den andra|across the bridge|2
genom en tunnel|through the tunnel|2
listen ___ the music|listen to the music|2''',('Our book club meets {0} Wednesdays. We start {1} half past three. We sit {2} the library, inside the building. A notice is {3} the wall. Our bags are {4} the table, below it. Everyone listens {5} the person who is speaking.',['on','at','in','on','under','to']))
E('there',[
'''There ___ a lamp in my room.|is|are~am
There ___ four chairs around the table.|are|is~am
There ___ milk in the fridge.|is|are~am
There ___ two windows in the kitchen.|are|is~am
There ___ a bus stop outside.|is|are~am
There ___ six books in my bag.|are|is~am''',
'''___ there any milk left?|Is|Are~Am
___ there any clean cups?|Are|Is~Am
There ___ not a café in this street.|is|are~am
There ___ not any students in the classroom.|are|is~am
Yes, there ___. There is one spare seat.|is|are~am
No, there ___. There aren’t any tickets left.|aren’t|isn’t~am not''',
'''There ___ two concerts here last summer.|were|was~is
There ___ a message for you yesterday.|was|were~are
There will ___ new rules next month.|be|are~is
There ___ some information on the poster.|is|are~am
There are two shops. ___ are both open.|They|It~There
There ___ no water in the bottle now.|is|are~am'''
],'''en bok finns|There is a book.|0
flera böcker finns|There are books.|0
vatten finns|There is water.|0
två fönster finns|There are two windows.|0
finns det en buss?|Is there a bus?|1
finns det några platser?|Are there any seats?|1
det finns inte en pool|There isn’t a pool.|1
det finns inte några biljetter|There aren’t any tickets.|1
en kö fanns i går|There was a queue.|2
flera butiker fanns förut|There were shops.|2
ett möte kommer att finnas|There will be a meeting.|2
information finns|There is information.|2''',('There {0} a new café in our town. There {1} six tables inside. There {2} a small garden behind it. There {3} flowers near the door. There {4} some water on each table. There {5} two people working in the kitchen.',['is','are','is','are','is','are']))
E('quantifiers',[
'''There is ___ juice in the fridge.|some|many~a few
We don’t have ___ clean cups.|any|much~a little
Are there ___ apples left?|any|much~a little
I have ___ questions to ask.|some|much~a little
They haven’t got ___ bread.|any|many~a few
We brought ___ food for the journey.|some|many~a few''',
'''How ___ chairs do we need?|many|much~little
How ___ milk is left?|much|many~few
There are a ___ people waiting.|few|little~much
I need a ___ advice.|little|few~many
How ___ homework do you have?|much|many~few
How ___ messages did she send?|many|much~little''',
'''Could I have ___ bread, please?|some|many~a few
This week we used ___ paper than last week.|less|fewer~many
We made ___ mistakes this time.|fewer|less~much
There is very ___ space in this bag.|little|few~many
Only a ___ students missed the bus.|few|little~much
There are ___ bottles to recycle than yesterday.|fewer|less~much'''
],'''böcker: hur många?|How many books?|0
vatten: hur mycket?|How much water?|0
positiv mening med äpplen|some apples|0
nekande mening med biljetter|not any tickets|0
några stolar|a few chairs|1
lite mjölk|a little milk|1
mycket information|a lot of information|1
många vänner|many friends|1
mindre papper|less paper|2
färre flaskor|fewer bottles|2
mycket lite tid|very little time|2
mycket få biljetter|very few tickets|2''',('We are organising a games evening. We have {0} (some/any) games ready. How {1} (much/many) chairs do we need? There aren’t {2} (some/any) spare tables. We have a {3} (little/few) snacks. There is a {4} (little/few) juice left. How {5} (much/many) time do we have to prepare?',['some','many','any','few','little','much']))
E('modals',[
'''My cousin can ___ very fast.|run|runs~running
Can they ___ the window?|open|opens~opening
She can ___ a bicycle.|ride|rides~riding
We cannot ___ the screen.|see|sees~seeing
He can ___ dinner for us.|cook|cooks~cooking
You can ___ a book here.|borrow|borrows~borrowing''',
'''You should ___ your teacher for help.|ask|asks~to ask
We must ___ on time.|arrive|arrives~to arrive
He shouldn’t ___ that heavy bag alone.|carry|carries~to carry
She must ___ her seatbelt.|wear|wears~to wear
Can we ___ here for a moment?|sit|sits~to sit
You should ___ the question again.|read|reads~to read''',
'''The library is free. You ___ pay.|don’t have to|mustn’t~must
It is forbidden to use phones here. You ___ use yours.|mustn’t|don’t have to~must
I ___ read when I was six.|could|can~must
___ you open the door for me, please?|Could|Mustn’t~Shouldn’t
Bringing a pen is required. You ___ bring one.|must|can~don’t have to
The bus is optional. You ___ take it.|don’t have to|mustn’t~cannot'''
],'''kan simma|can swim|0
kan inte köra|can’t drive|0
kan spela|can play|0
kan du hjälpa?|Can you help?|0
borde vila|should rest|1
måste komma|must arrive|1
borde inte vänta|shouldn’t wait|1
måste bära hjälm|must wear a helmet|1
behöver inte betala|don’t have to pay|2
får inte gå in|mustn’t enter|2
kunde läsa|could read|2
artig fråga om hjälp|Could you help me?|2''',('In our school kitchen, you must {0} (wash) your hands. You should {1} (tie) back long hair. You can {2} (borrow) an apron. You must not {3} (run) near the cookers. You should {4} (ask) if you are unsure. You don’t have to {5} (bring) your own equipment.',['wash','tie','borrow','run','ask','bring']))
E('questions',[
'''___ is your favourite subject?|What|Where~When
___ do you keep your shoes?|Where|Who~When
___ do you usually eat lunch: at noon or at one?|When|Who~What
___ is your best friend?|Who|When~Why
___ are you laughing?|Why|Who~Where
___ do you spell your name?|How|Who~Where''',
'''Why ___ she need a new bag?|does|do~is
When ___ your parents get home yesterday?|did|does~is
How old ___ your cousin?|is|does~do
What did you ___ for lunch yesterday?|eat|ate~eats
Where ___ your friends now?|are|do~does
How much ___ that ticket cost?|does|do~is''',
'''Who ___ the answer?|knows|does knows~know
Do you know where they ___?|live|do live~lives
Can you tell me why the shop ___ closed?|is|does~are
Who ___ she invite yesterday?|did|does~are
Do you know when the next bus ___?|leaves|does leaves~leave
Who ___ this bag yesterday?|found|did found~finded'''
],'''vilken (av flera)|which|0
vems|whose|0
hur många|how many|0
hur mycket|how much|0
hur gammal|how old|1
hur ofta|how often|1
hur länge|how long|1
vilken tid|what time|1
Where is she? → indirekt fråga|Do you know where she is?|2
Where does he live? → indirekt fråga|Do you know where he lives?|2
who som subjekt: ___ here?|Who works here?|2
who som objekt: ___ know?|Who do you know?|2''',('Leo interviews a new club member. “{0} is your name?” “Sara.” “{1} do you live?” “In the town centre.” “{2} do you travel here?” “On foot.” “{3} do you usually arrive?” “At four.” “{4} helps you practise?” “My cousin.” “{5} do you enjoy chess?” “Every game is different.”',['What','Where','How','When','Who','Why']))
E('connectors',[
'''We bought bread ___ milk.|and|because~although
He called me ___ he needed help.|because|although~but
The game was hard, ___ it was fun.|but|because~so because
I enjoy both swimming ___ cycling.|and|but~because
She took an umbrella ___ it was raining.|because|although~but
The bus was slow, ___ we arrived on time.|but|because~so because''',
'''The café was closed, ___ we went home.|so|because~although
We went home ___ the café was closed.|because|so~although
We packed our bags. ___ we caught the bus.|Then|Because~Although
He was nervous, ___ he gave the presentation.|but|because~so because
She missed lunch, ___ she was hungry later.|so|because~although
They brought a map ___ they didn’t know the area.|because|although~but''',
'''___ the rain, we had a good time.|Despite|Although~Because
It was difficult. ___, we did not give up.|However|Because~Although
We missed the train; ___, we had to wait.|therefore|although~because
___ she was nervous, she tried again.|Although|So~Because of
I enjoy reading, ___ my cousin enjoys drawing.|whereas|because~so
The meal was tasty ___ it was simple.|although|so~because of'''
],'''and → funktion|lägger till information|0
but → funktion|visar kontrast|0
because → funktion|ger en orsak|0
first|först|0
then|sedan|1
finally|till sist|1
so → funktion|visar en följd|1
whereas|medan (jämförelse)|1
despite|trots|2
therefore|därför / följaktligen|2
however → funktion|inleder en kontrast mellan meningar|2
although → funktion|visar en kontrast inom en mening|2''',('We wanted to go cycling, {0} (but/because) it was raining. We stayed indoors {1} (because/although) the roads were wet. Maya brought a game {2} (and/because) some snacks. We read the rules. {3} (Then/Although) we started playing. Leo was new to the game, {4} (but/because) he learned quickly. Everyone enjoyed it, {5} (so/because) we decided to play again next week.',['but','because','and','Then','but','so']))

def enrich(topics):
    import re
    def norm(x):return x.casefold().replace('’',"'").strip()
    assert len(EXTRA)==20
    for t in topics:
        extra=EXTRA[t['id']]
        for level,block in enumerate(extra['questions']):
            for index,line in enumerate(block.strip().splitlines()):
                parts=line.split('|');prompt,answer,wrong=parts[:3]
                q={'id':f'{t["id"]}-extra-{level}-{index}','level':level,'prompt':prompt,'answer':answer,'options':[answer]+wrong.split('~'),'why':parts[3] if len(parts)>3 else t['rules'][level],'sentence':prompt.replace('___',answer)}
                if t['id']=='articles' and answer in ('a','an'):q['instruction']='Välj a eller an. Utgå från det första ljudet.'
                t['questions'].append(q)
        bank=[]
        # Expand ambiguous short article answers into full phrases, so every match is unambiguous.
        for i,(left,right) in enumerate(t['pairs']):
            if sum(norm(p[1])==norm(right) for p in t['pairs'])>1:
                right=left.replace('___',right).strip()
            bank.append({'id':f'{t["id"]}-basepair-{i}','left':left,'right':right,'minLevel':0})
        for i,line in enumerate(extra['pairs'].strip().splitlines()):
            left,right,level=line.split('|')
            if any(norm(x['left'])==norm(left) or norm(x['right'])==norm(right) for x in bank):continue
            bank.append({'id':f'{t["id"]}-pair-{i}','left':left,'right':right,'minLevel':int(level)})
        assert len(bank)>=16,(t['id'],len(bank))
        assert len([x for x in bank if x['minLevel']==0])>=10,t['id']
        t['matchBank']=bank
        text,answers=extra['story'];t['stories']=[dict(t['story'],id=t['id']+'-text-0'),{'id':t['id']+'-text-1','text':text,'answers':answers}]
    # This optional standard alternative is also accepted in freely written plural answers.
    for t in topics:
        for q in t['questions']:
            if q['answer']=='scarves':q['alternatives']=['scarves','scarfs']
