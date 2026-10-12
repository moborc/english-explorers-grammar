import json
from pathlib import Path
TOPICS=[]
def T(id,title,sv,group,desc,rules,rows,story,pairs,use):
    qs=[]
    for level,block in enumerate(rows):
        for line in block.strip().split('\n'):
            parts=line.split('|'); prompt,answer,wrong,why=parts
            qs.append(dict(prompt=prompt,answer=answer,options=[answer]+wrong.split('~'),why=why,level=level,id=f'{id}-{level}-{len(qs)%6}'))
    assert len(qs)==18,(id,len(qs))
    st,answers=story
    TOPICS.append(dict(id=id,title=title,sv=sv,group=group,desc=desc,rules=rules,questions=qs,story=dict(text=st,answers=answers),pairs=[x.split('|') for x in pairs.split(';')],use=use))
T('be','Am, is & are','Att vara','Grunder','Presentera dig och beskriv hur någon är.',[
'To be betyder att vara. I presens använder du I am, he/she/it is och you/we/they are. På svenska säger vi ibland ”jag är 14”, på engelska I am 14.',
'Lägg not efter am, is eller are för att neka. I am not tired. I frågor kommer verbet först: Are you ready? Is she here? Korta svar: Yes, I am. No, she isn’t.',
'Subjektet bestämmer formen, även om det är långt: My best friend is … men My friends are … . Sammandragningar: I’m, you’re, isn’t och aren’t. There och it har olika funktioner; här tränar du personers och sakers egenskaper.'
],[
'''I ___ thirteen.|am|is~are|I hör ihop med am.
She ___ my friend.|is|are~am|She hör ihop med is.
We ___ ready.|are|am~is|We hör ihop med are.
My phone ___ new.|is|am~are|En telefon är it: använd is.
You ___ welcome.|are|is~am|You använder are, både för en och flera personer.
They ___ in the library.|are|is~am|They hör ihop med are.''',
'''___ your brother at home?|Is|Are~Am|Frågan börjar med Is när subjektet är your brother.
I ___ not angry.|am|is~are|I am not är den nekande formen.
___ you interested in music?|Are|Is~Am|Fråga med you: Are you …?
The lessons ___ not boring.|are|is~am|Lessons är plural, så använd are.
Yes, she ___.|is|are~am|Kort svar: Yes, she is.
No, we ___ not.|are|is~am|We använder are även i korta svar.''',
'''One of my friends ___ from Wales.|is|are~am|Subjektet är one, en person, så använd is.
My sister and I ___ on the same team.|are|am~is|My sister and I motsvarar we.
Everyone ___ welcome here.|is|are~am|Everyone räknas som singular i engelskan.
The news ___ surprising.|is|are~am|News behandlas som singular trots s på slutet.
Neither of these answers ___ correct.|is|am~be|Här använder vi standardformen is med neither.
The people in this photo ___ my cousins.|are|is~am|People är plural: are.'''
],('Hi! I {0} Sam. My sister {1} fifteen. We {2} at a new school. Our teachers {3} friendly. My favourite subject {4} English. You {5} welcome to join our study group.',['am','is','are','are','is','are']),
'I|am;she|is;we|are;I am|I’m;she is not|she isn’t;they are not|they aren’t',
['Presentera dig med tre meningar. Börja med I am … och My friend is … .','Beskriv två personer med fyra meningar. Använd både is och are och en nekande mening.','Skriv ett meddelande till en ny klasskamrat. Beskriv din grupp, fråga två frågor med to be och använd ett kort svar.'])
T('pastbe','Was & were','Att vara i dåtid','Verb & tid','Berätta hur det var igår.',[
'Was och were är dåtid av am, is och are. I/he/she/it was. You/we/they were. Exempel: I was tired yesterday. We were at school.',
'Neka med was not (wasn’t) och were not (weren’t). Börja frågor med Was eller Were: Were you at home? Yes, I was.',
'Välj formen efter subjektet, inte efter det närmaste ordet. The group was … men The students were … . Använd tydliga tidsuttryck när du beskriver dåtid.'
],[
'''I ___ tired yesterday.|was|were~are|I använder was i dåtid.
They ___ at the park.|were|was~is|They använder were i dåtid.
She ___ happy last Friday.|was|were~are|She använder was.
We ___ late yesterday.|were|was~is|We använder were.
The film ___ exciting.|was|were~are|The film är singular: was.
You ___ very kind yesterday.|were|was~is|You använder were.''',
'''___ you at school yesterday?|Were|Was~Are|Yesterday visar dåtid, och you använder were.
He ___ not at home last night.|was|were~are|He was not kan förkortas till he wasn’t.
___ the match exciting?|Was|Were~Am|The match är singular: Was the match …?
We ___ not ready yesterday.|were|was~is|We were not är nekande dåtid.
Yes, they ___.|were|was~is|Kort svar med they i dåtid: were.
No, I ___ not.|was|were~are|Kort nekande svar med I i dåtid: was not.''',
'''The first two lessons ___ cancelled yesterday.|were|was~is|Two lessons är plural: were.
Each student ___ nervous before the test.|was|were~are|Each student är singular: was.
My headphones ___ in my bag yesterday.|were|was~is|Headphones är plural.
There ___ a long queue outside.|was|were~are|A long queue är singular: there was.
The weather ___ better last weekend.|was|were~are|Weather är singular.
My brother and his friends ___ at the concert.|were|was~is|Flera personer: were.'''
],('Yesterday {0} a busy day. My friends {1} at the sports centre. I {2} at the library. The books {3} interesting. My teacher {4} there too. We {5} all tired in the evening.',['was','were','was','were','was','were']),
'I am → yesterday|I was;she is → yesterday|she was;we are → yesterday|we were;you are → yesterday|you were;was not|wasn’t;were not|weren’t',
['Skriv tre meningar om gårdagen med I was … .','Berätta om en skoldag med fyra meningar. Använd was, were och wasn’t.','Beskriv en dag som blev annorlunda än du trodde. Lägg till två frågor med was eller were.'])
T('have','Have & has','Att ha','Grunder','Berätta vad du och andra har.',[
'Have betyder ha. I/you/we/they have. He/she/it has. My sister has a bike. Vi säger I am hungry, inte I have hungry.',
'Fråga med do/does + have: Does she have a bike? Neka med don’t/doesn’t have. Efter does och doesn’t ska have stå i grundform.',
'Have got kan också uttrycka att någon har något: She has got a bike. Fråga: Has she got a bike? Neka: She hasn’t got a bike. Blanda inte Does she have …? och Has she got …?'
],[
'''I ___ a new bag.|have|has~is|I använder have.
He ___ a bike.|has|have~are|He använder has.
They ___ two cats.|have|has~is|They använder have.
My sister ___ a guitar.|has|have~am|My sister motsvarar she.
We ___ English today.|have|has~is|We använder have.
You ___ a good idea.|have|has~are|You använder have.''',
'''Does she ___ a ticket?|have|has~having|Efter does används have.
I don’t ___ my phone.|have|has~having|Efter don’t används grundformen have.
He doesn’t ___ a helmet.|have|has~having|Doesn’t följs av have, inte has.
Do they ___ time to help?|have|has~having|Do följs av have.
My friend ___ lunch at school every day.|has|have~having|My friend är singular: has.
We ___ a lot of homework today.|have|has~having|We använder have.''',
'''She ___ got a younger brother.|has|have~does|She has got beskriver vad hon har.
___ you got your keys?|Have|Has~Do|Have you got är rätt frågeform med got.
He hasn’t ___ any money.|got|have~has|Hasn’t got är den nekande formen.
Does your cousin ___ a skateboard?|have|has~got|Efter does används have, utan got.
My friends ___ got tickets for tonight.|have|has~does|My friends är plural: have got.
___ your teacher got a red car?|Has|Have~Does|Has your teacher got är en fråga med have got.'''
],('Our class {0} a new project. I {1} a notebook. My friend {2} a camera. We {3} lots of ideas. Our teacher {4} some advice. The other groups {5} interesting plans too.',['has','have','has','have','has','have']),
'I|have;he|has;they|have got;she|has got;does she …?|have a bike;has she …?|got a bike',
['Skriv tre meningar om vad du och en kompis har.','Beskriv vad ni behöver till en aktivitet. Använd have, has och doesn’t have.','Skriv en kort dialog om en resa. Använd både have och have got i korrekta frågor.'])
T('pronouns','Pronouns','Pronomen & ägande','Grunder','I, me, my eller mine? Välj rätt person och form.',[
'Pronomen ersätter namn: I, you, he, she, it, we, they. Som objekt använder vi me, you, him, her, it, us, them. She likes him. He helps me.',
'Ägande före ett substantiv: my, your, his, her, its, our, their. This is my bag. Utan substantiv: mine, yours, his, hers, ours, theirs. This bag is mine.',
'Its visar ägande: The dog wagged its tail. It’s betyder it is eller it has. Reflexiva pronomen används när personen gör något med sig själv: I taught myself. They enjoyed themselves.'
],[
'''Sam is my friend. ___ is kind.|He|Him~His|He är subjekt, den som är snäll.
Mia is here. I can see ___.|her|she~hers|Efter see behövs objektformen her.
My friends are outside. ___ are waiting.|They|Them~Their|They är subjekt.
Please help ___.|me|I~my|Help följs här av objektformen me.
This is ___ bag. It belongs to me.|my|I~me|My står framför substantivet bag.
We like our teacher. She helps ___.|us|we~our|Us är objektformen av we.''',
'''This book is ___. It belongs to me.|mine|my~me|Mine används utan ett efterföljande substantiv.
The players are wearing ___ new shirts.|their|they~them|Their visar ägande före shirts.
Is this phone ___? Does it belong to you?|yours|your~you|Yours står utan substantiv efteråt.
I know Leo. ___ sister is in my class.|His|Him~He|His visar att det är Leos syster.
Our dog loves ___ new bed.|its|it’s~it|Its visar ägande.
That is Sara’s coat. The coat is ___.|hers|her~she|Hers används utan substantiv efteråt.''',
'''I taught ___ to play the guitar.|myself|me~mine|Myself visar att jag lärde mig själv.
The students enjoyed ___ at the festival.|themselves|theirselves~themself|Den reflexiva pluralformen är themselves.
___ raining outside.|It’s|Its~It|It’s betyder it is.
The cat has hurt ___ paw.|its|it’s~it|Its visar att tassen tillhör katten.
We made the posters ___.|ourselves|ourself~usself|Ourselves betyder själva när subjektet är we.
Please give the tickets to Leo and ___.|me|I~my|Efter to används objektformen me.'''
],('This is Maya. {0} is in my class. I often study with {1}. We bring {2} notebooks. Her brother joins {3} sometimes. He has {4} own notebook. The blue pen is {5}; it belongs to me.',['She','her','our','us','his','mine']),
'I → objekt|me;he → objekt|him;we → objekt|us;they → objekt|them;my bag → utan bag|mine;her coat → utan coat|hers',
['Beskriv två personer med he, she eller they. Skriv också en mening med me.','Skriv fyra meningar om föremål som tillhör olika personer. Använd my och mine.','Skriv ett kort meddelande om en borttappad sak. Använd minst ett objektpronomen och skilj på its och it’s.'])
T('articles','A, an & the','Artiklar','Grunder','En sak, en bestämd sak eller ingen artikel?',[
'A och an betyder ungefär en eller ett. Använd a före konsonantljud och an före vokalljud: a bike, an apple. Det är ljudet, inte bokstaven, som avgör.',
'The används när läsaren vet vilken sak du menar: I saw a dog. The dog was black. Vi använder ofta ingen artikel när vi talar allmänt om plural eller oräkneliga saker: I like books. I like music.',
'Lyssna på första ljudet: an hour (tyst h), a university (börjar med ett j-ljud). Uttryck som play football och go to school har normalt ingen artikel. I play the guitar har normalt the.'
],[
'''I have ___ bike.|a|an~the an|Bike börjar med konsonantljud.
She is eating ___ apple.|an|a~the a|Apple börjar med vokalljud.
He needs ___ umbrella.|an|a~a the|Umbrella börjar med vokalljud.
This is ___ new game.|a|an~an the|New börjar med konsonantljud.
We saw ___ elephant at the zoo.|an|a~a an|Elephant börjar med vokalljud.
My sister is ___ teacher.|a|an~an a|Teacher börjar med konsonantljud.''',
'''I bought a book. ___ book is about space.|The|An~A the|Vi vet vilken bok det är: the book.
Could you close ___ door next to you?|the|an~a the|Den bestämda dörren bredvid dig: the.
She is ___ engineer.|an|a~the an|Engineer börjar med vokalljud.
We watched a film. ___ film was funny.|The|A~An|Filmen har redan presenterats: the.
He has ___ orange backpack.|an|a~an the|Orange börjar med vokalljud.
That is ___ interesting idea.|an|a~the an|Interesting börjar med vokalljud.''',
'''It takes ___ hour to get there.|an|a~an the|H i hour är tyst: ordet börjar med vokalljud.
My cousin studies at ___ university.|a|an~a the|University börjar med j-ljud: a university.
I play ___ guitar after school.|the|an~a the|Det vanliga uttrycket är play the guitar.
She is ___ honest person.|an|a~a an|Honest börjar med vokalljud eftersom h är tyst.
He wears ___ uniform at work.|a|an~an the|Uniform börjar med j-ljud: a uniform.
The sun is ___ star.|a|an~a an|Star börjar med konsonantljud; här klassificerar vi solen som en stjärna.'''
],('I saw {0} dog near our school. {1} dog had a ball. It ran towards {2} old tree. Under {3} tree was a girl. She had {4} book and {5} umbrella.',['a','The','an','the','a','an']),
'___ apple|an;___ bike|a;___ hour|an;___ university|a;___ honest person|an;___ guitar (play)|the',
['Skriv tre meningar om saker i ditt rum. Använd a och an.','Presentera en sak med a/an. Skriv sedan två meningar om samma sak med the.','Beskriv din dag. Ta med a university eller an hour och en mening om ett instrument eller en sport.'])
T('plurals','Nouns & plurals','Substantiv & plural','Grunder','One friend, two friends. Träna vanliga och ovanliga former.',[
'Substantiv är ord för personer, platser och saker. Plural betyder fler än en. Oftast lägger du till -s: friend → friends. Efter till exempel -ch och -s behövs ofta -es: watch → watches.',
'Konsonant + y blir ofta -ies: city → cities. Vokal + y får -s: boy → boys. Några pluralformer är oregelbundna: child → children, person → people, tooth → teeth.',
'Vissa ord är likadana i singular och plural: sheep → sheep. Information och advice är oräkneliga och får normalt inte -s. Säg some advice eller a piece of advice. Några ord på -f/-fe får -ves: knife → knives.'
],[
'''One book, two ___.|books|bookes~book|Oftast bildas plural med -s.
One friend, three ___.|friends|friendes~friend|Friend får -s i plural.
One bus, two ___.|buses|buss~bus|Bus får -es i plural.
One watch, four ___.|watches|watchs~watch|Watch slutar på -ch och får -es.
One box, five ___.|boxes|boxs~box|Box får -es i plural.
One game, two ___.|games|gamees~game|Game får -s i plural.''',
'''One city, two ___.|cities|citys~cityes|Konsonant + y blir -ies.
One boy, three ___.|boys|boies~boyes|Vokal + y behåller y och får -s.
One child, two ___.|children|childs~childes|Children är oregelbunden plural.
One tooth, several ___.|teeth|tooths~toothes|Tooth har pluralformen teeth.
One woman, two ___.|women|womans~womanes|Woman har pluralformen women.
One person, many ___.|people|persones~peoples|Den vanliga pluralformen av person är people.''',
'''One sheep, ten ___.|sheep|sheeps~sheepes|Sheep är samma i singular och plural.
One knife, two ___.|knives|knifes~knifees|Knife får pluralformen knives.
One foot, two ___.|feet|foots~feets|Foot har pluralformen feet.
One mouse, three ___.|mice|mouses~mices|Mouse har pluralformen mice.
One leaf, many ___.|leaves|leafs~leafes|Leaf får normalt pluralformen leaves.
One life, many ___.|lives|lifes~lifees|Life får pluralformen lives.'''
],('Our school has two {0} (library). There are many {1} (book). Three {2} (child) are reading. Two {3} (woman) are helping them. There are new {4} (box) on a table. We find photos of several {5} (city).',['libraries','books','children','women','boxes','cities']),
'child|children;person|people;tooth|teeth;city|cities;knife|knives;sheep (en)|sheep (flera)',
['Beskriv saker du har mer än en av. Skriv tre meningar.','Beskriv en plats med fyra meningar och minst två oregelbundna pluralformer.','Skriv en kort annons om en aktivitet. Använd pluralformer och some information eller some advice.'])
T('present','Present simple','Vanor & fakta','Verb & tid','Berätta vad som händer ofta.',[
'Present simple används för vanor och fakta. I/you/we/they play. He/she/it plays. Lägg till -s med he, she och it: My friend walks to school.',
'Verb på -ch, -sh, -s, -x och ofta -o får -es: watches, goes. Konsonant + y blir -ies: study → studies. Negation: don’t/doesn’t + grundform. She doesn’t play.',
'Frekvensord som usually, often och never står normalt före huvudverbet men efter to be: I often walk. I am often tired. Ett långt subjekt kan fortfarande vara singular: The boy with the red shoes plays.'
],[
'''I ___ football every Saturday.|play|plays~playing|I använder grundformen play.
She ___ to school every day.|walks|walk~walking|She använder verb med -s.
They ___ music in the evening.|listen to|listens to~listening to|They använder grundformen.
He ___ pizza.|likes|like~liking|He använder likes.
We ___ English on Tuesdays.|study|studies~studying|We använder study.
My brother ___ games after school.|plays|play~playing|My brother motsvarar he.''',
'''She ___ TV after dinner.|watches|watchs~watch|Watch får -es med she.
He ___ to school by bus.|goes|go~gos|Go får -es med he.
My sister ___ English every day.|studies|studys~study|Konsonant + y blir -ies.
They don’t ___ meat.|eat|eats~eating|Efter don’t används grundformen.
She doesn’t ___ tennis.|play|plays~playing|Efter doesn’t används grundformen.
My dad ___ lunch at noon.|has|have~having|Have blir has med he.''',
'''The student next to the windows ___ very hard.|works|work~working|Subjektet är the student, singular.
Everyone in our team ___ a water bottle.|brings|bring~bringing|Everyone är singular och kräver -s.
Neither of the phones ___ properly.|works|working~workes|Standardformen med neither är works.
My friends and I ___ online every weekend.|chat|chats~chatting|My friends and I motsvarar we.
The shop ___ at nine every morning.|opens|open~opening|The shop är singular; en regelbunden vana.
My teacher always ___ our questions.|answers|answer~answering|My teacher är singular. Always står före huvudverbet.'''
],('Every morning, Maya {0} (get) up at seven. She {1} (eat) breakfast. Her brother {2} (watch) the news. They {3} (walk) to school together. Maya {4} (study) English. After school, they {5} (play) basketball.',['gets','eats','watches','walk','studies','play']),
'I play → she|plays;I go → he|goes;I watch → she|watches;I study → he|studies;I have → she|has;I do → he|does',
['Skriv tre meningar om vad du gör varje vecka.','Beskriv din och en annan persons rutiner. Använd don’t och doesn’t också.','Skriv en kort profil av en elev. Använd usually, often och never på rätt plats och variera subjekten.'])
T('do','Do, does & did','Frågor & nekande','Verb & tid','Ställ frågor och säg vad som inte händer.',[
'I present simple använder du do med I/you/we/they och does med he/she/it. Do you play? Does she play? Huvudverbet står i grundform.',
'Negation: don’t och doesn’t + grundform. I don’t know. She doesn’t know. I dåtid använder alla subjekt did och didn’t: Did she go? She didn’t go.',
'To be och hjälpverb som can behöver inte do: Are you ready? Can she swim? Kort svar följer hjälpverbet: Yes, she does. No, they didn’t. Använd inte dubbel dåtid efter did.'
],[
'''___ you like music?|Do|Does~Is|You använder do med like.
___ she play tennis?|Does|Do~Are|She använder does.
___ they live near school?|Do|Does~Am|They använder do.
He ___ not like coffee.|does|do~is|He does not like är nekande present simple.
We ___ not eat lunch at home.|do|does~are|We do not eat är nekande present simple.
___ your brother speak English?|Does|Do~Are|Your brother är singular: does.''',
'''Did you ___ the match yesterday?|watch|watched~watches|Efter did står verbet i grundform.
She didn’t ___ to school yesterday.|go|went~goes|Didn’t följs av go, inte went.
Does he ___ a bike?|have|has~had|Does följs av have.
They don’t ___ here.|live|lives~lived|Don’t följs av grundformen live.
___ they arrive last night?|Did|Does~Are|Last night visar dåtid: did.
___ your friend call you every day?|Does|Do~Did|Every day visar en vana, your friend är singular.''',
'''Yes, she ___. She plays every week.|does|do~is|Kort svar på en does-fråga: does.
No, they ___. They stayed at home yesterday.|didn’t|doesn’t~isn’t|Svaret är i dåtid och använder didn’t.
___ you ready to leave now?|Are|Do~Does|Ready är ett adjektiv: fråga med to be.
___ he swim well?|Can|Does~Is|Can kan direkt följas av swim; does behöver annan innebörd och is kräver swimming.
Why ___ she leave early yesterday?|did|does~do|Yesterday kräver did, sedan grundformen leave.
What time ___ the bus usually arrive?|does|do~is|The bus är singular och usually visar vana.'''
],('Leo likes skating. {0} he practise every week? Yes, he does. His friends {1} not skate, but they watch. Yesterday they {2} not stay long. {3} Leo win the race yesterday? No, he didn’t. Today he does not {4} (feel) tired. His friends do not {5} (want) to miss the next race.',['Does','do','did','Did','feel','want']),
'I/you/we/they → fråga nu|do;he/she/it → fråga nu|does;alla → fråga då|did;do not|don’t;does not|doesn’t;did not|didn’t',
['Skriv tre frågor till en klasskamrat med Do you …?','Skriv två frågor med does och två med did. Lägg till korta svar.','Skriv en dialog som blandar frågor med do, did, be och can. Kontrollera huvudverbens former.'])
T('continuous','Present continuous','Det som händer nu','Verb & tid','Am/is/are + verb med -ing.',[
'Present continuous beskriver ofta vad som händer just nu. Bygg med am/is/are + verb-ing: I am reading. She is playing. They are talking.',
'Ta oftast bort slut-e före -ing: make → making. I korta verb kan slutkonsonanten dubbleras: run → running. Fråga: Are you listening? Neka: I am not listening.',
'Skilj vana från pågående handling: I walk every day. I am walking now. Vissa verb används vanligen i enkel form: I know, I want, I believe. Pågående form kan också visa en tillfällig situation.'
],[
'''I ___ reading right now.|am|is~are|I am + reading.
She ___ playing a game now.|is|am~are|She is + playing.
They ___ listening to music now.|are|is~am|They are + listening.
We are ___ TV right now.|watching|watch~watches|Efter are i pågående form används verb-ing.
He is ___ a message now.|writing|write~writes|Write tappar sitt e före -ing.
You ___ talking very loudly now.|are|am~is|You are + talking.''',
'''She is ___ dinner right now.|making|makeing~makes|Make tappar e: making.
He is ___ in the park now.|running|runing~runs|Run dubblerar n: running.
___ they waiting for us now?|Are|Is~Do|Frågan börjar med Are när subjektet är they.
I am not ___ to anyone right now.|talking|talk~talks|Am not + verb-ing.
We are ___ for the next bus.|waiting|wait~waits|Are + waiting.
My friend is ___ on the sofa right now.|sitting|siting~sits|Sit dubblerar t: sitting.''',
'''I usually walk, but today I ___ the bus.|am taking|take~takes|Today visar här en tillfällig avvikelse från vanan.
She ___ the answer already.|knows|is knowing~know|Know används normalt inte i pågående form.
Listen! Someone ___ at the door.|is knocking|knocks~are knocking|Listen visar att det händer nu; someone är singular.
He ___ a new phone, but he has no money.|wants|is wanting~want|Want används normalt i enkel form.
We ___ with my aunt this week.|are staying|is staying~stays|En tillfällig situation, och we använder are.
Look! The dog ___ towards us.|is running|run~are running|Look visar pågående handling; the dog är singular.'''
],('It is lunchtime. I am {0} (sit) with my friends. Maya is {1} (eat) a sandwich. Leo is {2} (drink) water. Two students are {3} (play) chess. Our teacher is {4} (read). We are {5} (enjoy) our break.',['sitting','eating','drinking','playing','reading','enjoying']),
'read → -ing|reading;make → -ing|making;run → -ing|running;sit → -ing|sitting;write → -ing|writing;swim → -ing|swimming',
['Beskriv tre saker som händer just nu.','Beskriv en rast med fyra meningar, en fråga och en nekande mening i pågående form.','Beskriv vad en person brukar göra och vad personen gör annorlunda idag. Använd båda presensformerna.'])
T('past','Past simple','Det som hände','Verb & tid','Träna regelbundna och oregelbundna verb i dåtid.',[
'Past simple berättar om något avslutat. Regelbundna verb får ofta -ed: play → played. Verb på -e får -d: live → lived. I went home yesterday är ett exempel med oregelbundet verb.',
'Konsonant + y blir -ied: study → studied. Vanliga oregelbundna former: go → went, see → saw, eat → ate, have → had. Efter did och didn’t använder du grundformen.',
'Välj past simple med avslutade tider: yesterday, last week, in 2024. Sätt tidsorden i en berättelse och håll ordningen tydlig. Oregelbundna verb behöver tränas i meningsfulla sammanhang.'
],[
'''We ___ football yesterday.|played|play~plays|Play är regelbundet och får -ed.
She ___ in London last year.|lived|live~lives|Live slutar på e och får -d.
I ___ my friend yesterday.|called|call~calls|Call får -ed i dåtid.
They ___ a film last night.|watched|watch~watches|Last night visar avslutad dåtid.
He ___ to school yesterday.|walked|walk~walks|Walk får -ed.
We ___ the classroom yesterday.|cleaned|clean~cleans|Clean får -ed.''',
'''I ___ to the cinema yesterday.|went|go~goed|Go har den oregelbundna formen went.
She ___ pizza last night.|ate|eat~eated|Eat blir ate i dåtid.
We ___ our teacher at the park yesterday.|saw|see~seed|See blir saw i dåtid.
He ___ hard for the test last week.|studied|studyed~studies|Konsonant + y blir -ied.
They didn’t ___ the game.|win|won~winned|Efter didn’t står grundformen win.
Did you ___ a good weekend?|have|had~has|Efter did står have.''',
'''Maya ___ a new jacket last Saturday.|bought|buyed~buy|Buy blir bought.
I ___ my phone at home yesterday.|left|leaved~leave|Leave blir left.
The lesson ___ at nine yesterday.|began|beginned~begin|Begin blir began i past simple.
She ___ a letter to her cousin last week.|wrote|written~write|Write blir wrote i past simple; written är particip.
We ___ the answer after a long discussion yesterday.|understood|understanded~understand|Understand blir understood.
He ___ the ball to his teammate a minute ago.|threw|throwed~thrown|Throw blir threw; thrown är particip.'''
],('Last Saturday, we {0} (visit) a friend. We {1} (go) by bus. Maya {2} (bring) a game. We {3} (play) for an hour. Then we {4} (eat) pizza. I {5} (have) a great evening.',['visited','went','brought','played','ate','had']),
'go → dåtid|went;see → dåtid|saw;eat → dåtid|ate;buy → dåtid|bought;write → dåtid|wrote;take → dåtid|took',
['Skriv tre meningar om vad du gjorde igår.','Berätta om en helg. Använd regelbundna och oregelbundna verb samt didn’t.','Skriv en kort berättelse med first, then och finally. Lägg till en fråga i dåtid till läsaren.'])
T('perfect','Present perfect','Erfarenheter & resultat','Verb & tid','Have/has + tredje verbformen.',[
'Present perfect bildas med have/has + perfekt particip. I have visited London. She has finished. Formen kan berätta om en erfarenhet eller ett resultat som är viktigt nu.',
'Fråga: Have you ever seen snow? Neka: I haven’t seen it. Vanliga particip: go → gone, see → seen, eat → eaten, do → done. Already, just och yet används ofta med perfekt.',
'Perfekt kopplar till nu: I have lost my keys (de är borta nu). Past simple har en avslutad tidsangivelse: I lost them yesterday. Since anger startpunkt, for en tidsperiod: since Monday, for two days.'
],[
'''I ___ finished my homework.|have|has~am|I använder have + particip.
She ___ visited London.|has|have~is|She använder has + particip.
We have ___ the film.|watched|watch~watching|Have följs av particip; watch är regelbundet.
They ___ cleaned their room.|have|has~are|They använder have.
He has ___ the game.|played|play~playing|Play har participformen played.
You ___ helped me a lot.|have|has~are|You använder have.''',
'''Have you ever ___ sushi?|eaten|ate~eat|Eat har participformen eaten.
She has already ___ the book.|read|reading~reads|Read stavas likadant i grundform och particip.
We haven’t ___ that film yet.|seen|saw~see|Efter haven’t används participformen seen.
He has just ___ his homework.|done|did~do|Do har participformen done.
Have they ___ home already?|gone|went~go|Go har participformen gone.
I have never ___ to Scotland.|been|was~be|Been används för erfarenhet av att ha varit någonstans.''',
'''I have lived here ___ 2020.|since|for~during|Since används med startpunkt.
She has studied English ___ three years.|for|since~from|For används med tidsperiod.
We ___ the museum yesterday.|visited|have visited~has visited|Yesterday är avslutad tid: past simple.
He ___ his keys, so he can’t open the door now.|has lost|have lost~is lose|Has lost visar ett resultat som gäller nu.
Have you finished your project ___?|yet|already not~since|Yet används ofta sist i en fråga om något är klart.
I have known her ___ we were children.|since|for~during|Since kopplar till när perioden började.'''
],('We have just {0} (finish) our project. Maya has {1} (write) the introduction. Leo has {2} (take) the photos. I have {3} (make) the slides. We have {4} (learn) a lot. Our teacher has {5} (give) us useful advice.',['finished','written','taken','made','learned','given']),
'see → particip|seen;eat → particip|eaten;go → particip|gone;do → particip|done;write → particip|written;take → particip|taken',
['Skriv tre saker du har gjort med I have … .','Skriv om fyra erfarenheter. Använd ever, never eller yet och fråga en kompis.','Skriv om något du har lärt dig över tid. Använd since och for och skilj en avslutad händelse från ett resultat nu.'])
T('future','Future forms','Framtid','Verb & tid','Planer, beslut och förutsägelser.',[
'Going to används ofta för en plan: I am going to study tonight. Bygg med am/is/are + going to + grundform. Will + grundform kan beskriva framtid: It will rain.',
'Will används ofta för ett beslut just nu, ett erbjudande eller en förutsägelse. I’ll help you. Going to passar för planer som redan finns och för förutsägelser med synliga tecken: Look at the clouds! It’s going to rain.',
'Present continuous kan beskriva en ordnad framtida aktivitet: We are meeting at six tomorrow. Använd tidsuttryck som visar framtid. I tidsbisatser efter when används normalt presens: I’ll call when I arrive.'
],[
'''I ___ going to study tonight.|am|is~are|I am going to + grundform.
She ___ going to visit a friend tomorrow.|is|am~are|She is going to + grundform.
We ___ going to play after school.|are|is~am|We are going to + grundform.
He will ___ you tomorrow.|call|calls~called|Efter will används grundformen.
They are going to ___ a film tonight.|watch|watching~watched|Going to följs av grundformen.
I will ___ my best.|try|tries~trying|Will följs av grundformen try.''',
'''I’ve already decided: I’m ___ study medicine.|going to|will~going|Going to används för en redan bestämd plan.
Your bag looks heavy. I ___ carry it for you.|will|am going~going to|Will passar för ett erbjudande i stunden.
Look at those dark clouds! It’s ___ rain.|going to|will~going|Going to passar för en förutsägelse med synliga tecken.
She is going to ___ a ticket tomorrow.|buy|buys~bought|Going to följs av grundformen.
Don’t worry. I ___ forget your birthday.|won’t|not will~willn’t|Won’t är sammandragningen av will not.
Are you ___ to join us tomorrow?|going|will~goes|Are you going to är rätt frågeform.''',
'''We ___ our cousins at six tomorrow; the table is booked.|are meeting|is meeting~meeting|Present continuous kan uttrycka en ordnad framtidsplan.
I’ll text you when I ___.|arrive|will arrive~arrived|Efter when i en framtida tidsbisats används presens.
She ___ leaving for London tomorrow; she has her ticket.|is|are~will|Is leaving är pågående form för en ordnad resa.
If it rains tomorrow, we ___ stay indoors.|will|are~going|Huvudsatsen kan ha will + grundform.
I promise I ___ tell anyone your secret.|won’t|don’t will~willn’t|Won’t används i ett löfte om att inte göra något.
We’ll start as soon as everyone ___.|arrives|will arrive~arrived|Efter as soon as används presens för framtida tid.'''
],('Tomorrow we are going to {0} (visit) a museum. Maya {1} going to bring lunch. Leo {2} going to take photos. I {3} going to write notes. We will {4} (meet) at the station. Our teacher will {5} (help) us find the train.',['visit','is','is','am','meet','help']),
'will not|won’t;I will|I’ll;she will|she’ll;I → going to|am going to;she → going to|is going to;we → going to|are going to',
['Skriv tre planer med I am going to … .','Skriv om dina helgplaner och erbjud en kompis hjälp med will.','Skriv ett meddelande om en ordnad utflykt. Använd going to, pågående form och en mening med when.'])
T('adjectives','Adjectives','Adjektiv & jämförelser','Beskriv & bygg','Beskriv saker och jämför dem.',[
'Adjektiv beskriver personer och saker. De står före substantivet eller efter to be: a tall student, The student is tall. Engelska adjektiv ändras inte i plural: two tall students.',
'Korta adjektiv får ofta -er och -est: small, smaller, the smallest. Längre får more och most: interesting, more interesting, the most interesting. Good → better → best. Bad → worse → worst.',
'Efter en jämförelse används ofta than: My bag is heavier than yours. As … as visar likhet: as tall as. Konsonant + y blir i: happy → happier. Big dubblerar g: bigger. Använd inte more tillsammans med -er.'
],[
'''She has a ___ bike.|new|newly~news|New beskriver substantivet bike.
My friends are ___.|friendly|friendlies~friend|Adjektivet friendly ändras inte i plural.
This is an ___ book.|interesting|interest~interestingly|Interesting beskriver book.
The room is ___.|quiet|quietly~quiets|Efter is beskriver quiet rummet.
He is a ___ player.|good|well~goods|Good är adjektivet som beskriver player.
They have two ___ bags.|heavy|heavies~heavily|Adjektiv får inte plural-s.''',
'''My bag is ___ than yours.|smaller|smallest~more small|Small får -er i jämförelse.
This is the ___ room in the house.|biggest|bigger~most big|The och in the house visar superlativ: biggest.
This book is ___ than that one.|more interesting|interestinger~most interesting|Ett längre adjektiv använder more vid jämförelse.
Today is ___ than yesterday.|better|gooder~best|Good har den oregelbundna formen better.
That was the ___ film I have ever seen.|worst|worse~baddest|Bad har superlativformen worst.
She is the ___ runner in our class.|fastest|faster~more fast|The fastest jämför med hela gruppen.''',
'''This exercise is ___ than the last one.|easier|easyer~more easier|Konsonant + y blir i före -er.
My brother is as ___ as me.|tall|taller~tallest|As … as använder grundformen tall.
That was the ___ day of the holiday.|happiest|happyest~most happiest|Happy blir happiest.
This phone is ___ expensive than mine.|less|least~few|Less expensive betyder mindre dyr.
The blue jacket is ___ than the black one.|more comfortable|comfortabler~most comfortable|Comfortable jämförs med more.
The second question was much ___.|harder|more harder~hardest than|Much kan förstärka jämförelsen harder.'''
],('Our new classroom is {0} (big) than the old one. It is also {1} (bright) than before. The chairs are {2} (comfortable) than the old chairs. My desk is the {3} (small) in the room. The library is the {4} (quiet) place in school. I think this year is {5} (good) than last year.',['bigger','brighter','more comfortable','smallest','quietest','better']),
'good → jämförelse|better;bad → jämförelse|worse;big → jämförelse|bigger;happy → jämförelse|happier;small → mest|smallest;interesting → jämförelse|more interesting',
['Beskriv tre saker eller personer med adjektiv.','Jämför två spel, filmer eller platser med fyra meningar.','Skriv en kort recension. Använd than, as … as och en superlativ och motivera vad du tycker.'])
T('adverbs','Adverbs','Hur & hur ofta','Beskriv & bygg','Quick eller quickly? Beskriv handlingen.',[
'Adverb beskriver ofta hur något görs. Många bildas med adjektiv + -ly: slow → slowly. She walks slowly. Adjektivet beskriver en sak eller person: She is slow.',
'Good blir well när det beskriver en handling: He is a good singer. He sings well. Fast och hard kan vara både adjektiv och adverb: She runs fast. I work hard. Friendly är normalt ett adjektiv.',
'Frekvensord står vanligtvis före huvudverbet men efter to be: I often read. I am often tired. Hardly betyder knappt, inte hårt. Var uppmärksam på om ordet beskriver personen eller handlingen.'
],[
'''She walks ___.|slowly|slow~slows|Slowly beskriver hur hon går.
He speaks ___.|quietly|quiet~quiets|Quietly beskriver hur han talar.
Please listen ___.|carefully|careful~care|Carefully beskriver hur du ska lyssna.
They answered ___.|quickly|quick~quicks|Quickly beskriver handlingen answered.
The music is ___.|loud|loudly~louds|Loud beskriver music efter is.
She smiled ___.|happily|happy~happiness|Happily beskriver hur hon log.''',
'''He plays the guitar ___.|well|good~goodly|Well är adverbet till good.
She runs very ___.|fast|fastly~fasterly|Fast är också adverb, utan -ly.
We work ___ at school.|hard|hardly~hardlyly|Hard betyder hårt. Hardly betyder knappt.
That is a ___ answer.|good|well~goodly|Good beskriver substantivet answer.
My teacher explains things ___.|clearly|clear~clears|Clearly beskriver verbet explains.
Leo is a ___ person.|friendly|friendlily~friend|Friendly är ett adjektiv som beskriver person.''',
'''I can ___ hear you. Please speak louder.|hardly|hard~hardlyly|Hardly betyder knappt.
She ___ arrives on time.|usually|usual~usuale|Usually beskriver hur ofta hon kommer i tid.
He is ___ tired after practice.|often|oftens~oftenly|Often står här efter to be.
They answered the difficult question ___.|correctly|correct~correction|Correctly beskriver hur de svarade.
The soup smells ___.|good|well~goodly|Efter smells beskriver good soppans egenskap.
Please drive ___. The roads are icy.|carefully|careful~carefulness|Carefully beskriver hur någon ska köra.'''
],('Maya is a {0} (careful/carefully) student. She reads questions {1} (careful/carefully). Leo writes very {2} (quick/quickly). Our teacher speaks {3} (clear/clearly). Maya plays chess {4} (good/well). They both work {5} (hard/hardly) because they want to improve.',['careful','carefully','quickly','clearly','well','hard']),
'slow → hur?|slowly;careful → hur?|carefully;happy → hur?|happily;good → hur?|well;fast → hur?|fast;hard → hur?|hard',
['Skriv tre meningar om hur någon gör saker. Använd slowly, quickly och carefully.','Beskriv en person och hur personen arbetar. Skilj mellan good och well.','Skriv ett råd till en ny elev. Använd frekvensord och förklara skillnaden mellan work hard och hardly work.'])
T('prepositions','Prepositions','Plats & tid','Beskriv & bygg','In, on, at, under, between och fler.',[
'Prepositioner visar till exempel plats: in = i, on = på, under = under, next to = bredvid, between = mellan. The keys are on the table. Läs hela situationen.',
'För tid: at med klockslag, on med dagar och datum, in med månader, år och delar av dagen. At five, on Monday, in October. Vanligt undantag: at night.',
'In kan visa var något är, into en rörelse in i något. Across = över från sida till sida, through = genom. Många kombinationer behöver tränas som fraser: interested in, good at, listen to.'
],[
'''The keys are ___ the bag, inside it.|in|on~under|Inside visar att nycklarna är i väskan.
The book is lying ___ top of the desk.|on|in~under|On top of betyder ovanpå.
The shoes are ___ the bed, below it.|under|on~in|Below visar att skorna är under sängen.
Maya sits ___ Leo and Sam.|between|under~in|Between används för platsen mellan två personer.
The bus stop is ___ to our school.|next|between~in|Uttrycket next to betyder bredvid.
The poster is ___ the wall.|on|in~under|En affisch sitter on the wall.''',
'''The lesson starts ___ nine o’clock.|at|on~in|Klockslag använder at.
We play football ___ Mondays.|on|at~in|Veckodagar använder on.
My birthday is ___ June.|in|on~at|Månader använder in.
I was born ___ 2012.|in|at~on|Årtal använder in.
The stars are bright ___ night.|at|on~in|At night är ett fast uttryck.
We often study ___ the evening.|in|on~at|Delar av dagen använder vanligen in.''',
'''She walked ___ the room from the corridor.|into|on~at|Into visar rörelse in i rummet.
We walked ___ the bridge to the other side.|across|between~in|Across visar rörelse från en sida till den andra.
The train went ___ a tunnel.|through|between~on|Through betyder genom.
I am interested ___ music.|in|on~at|Det fasta uttrycket är interested in.
He is good ___ maths.|at|in~on|Det fasta uttrycket är good at.
Please listen ___ the instructions.|to|on~at|Listen följs av to när något ska lyssnas på.'''
],('Our club meets {0} Mondays. We start {1} four o’clock. We sit {2} the library, inside the building. Our bags are {3} the table, below it. We often meet {4} the afternoon. Everyone is interested {5} games.',['on','at','in','under','in','in']),
'___ Monday|on;___ five o’clock|at;___ October|in;___ night|at;interested ___|in;good ___|at',
['Beskriv var tre saker finns med in, on och under.','Skriv ett schema med dagar och tider. Använd in, on och at.','Ge en kompis vägbeskrivning och berätta när ni ska ses. Använd rörelseprepositioner och tidsuttryck.'])
T('there','There is & there are','Det finns','Grunder','Beskriv vad som finns på en plats.',[
'There is betyder det finns när det gäller en sak. There are används för flera. There is a café. There are two shops. There is används också för oräkneliga saker: There is water.',
'Fråga genom att byta plats: Is there a café? Are there any shops? Neka med there isn’t och there aren’t. Short answer: Yes, there is. No, there aren’t.',
'I dåtid: there was (singular) och there were (plural). I framtid: there will be, samma för en och flera. It is beskriver en sak som redan är känd: There is a library. It is quiet.'
],[
'''There ___ a café near our school.|is|are~am|A café är en sak: there is.
There ___ two shops in my street.|are|is~am|Two shops är plural: there are.
There ___ a book on the desk.|is|are~am|A book är singular.
There ___ three students outside.|are|is~am|Three students är plural.
There ___ water in my bottle.|is|are~am|Water är oräkneligt och använder is.
There ___ a park behind the library.|is|are~am|A park är singular.''',
'''___ there a bus stop here?|Is|Are~Am|A bus stop är singular: Is there …?
___ there any free seats?|Are|Is~Am|Seats är plural: Are there …?
There ___ not any tickets left.|are|is~am|Tickets är plural: there are not.
There ___ not much time.|is|are~am|Time är oräkneligt: there is not.
Yes, there ___. There are two shops.|are|is~am|Kort svar med plural: there are.
No, there ___. There isn’t a pool.|isn’t|aren’t~am not|A pool är singular: there isn’t.''',
'''There ___ a long queue yesterday.|was|were~are|A queue är singular och yesterday visar dåtid.
There ___ many visitors last Saturday.|were|was~is|Many visitors är plural i dåtid.
There will ___ a meeting tomorrow.|be|is~are|Efter will används be.
There is a library. ___ is very quiet.|It|There~They|It beskriver den redan presenterade platsen.
There ___ some advice on the website.|is|are~am|Advice är oräkneligt, så there is.
There ___ three different ways to solve this problem.|are|is~am|Three ways är plural.'''
],('There {0} a new youth club in town. There {1} two games rooms. There {2} a small kitchen. There {3} some water on the table. There {4} several books to borrow. There {5} a noticeboard near the door.',['is','are','is','is','are','is']),
'en sak nu|there is;flera saker nu|there are;en sak då|there was;flera saker då|there were;finns inte (en)|there isn’t;finns inte (flera)|there aren’t',
['Beskriv vad som finns i ett rum med tre meningar.','Beskriv din skola. Ta med något som finns, något som inte finns och en fråga.','Beskriv hur en plats har förändrats. Använd there was/were och there is/are och en plan med there will be.'])
T('quantifiers','Some, any & more','Mängdord','Beskriv & bygg','Countable, uncountable, much och many.',[
'Some används ofta i positiva meningar: I have some apples. Any används ofta i frågor och negationer: Do you have any apples? I don’t have any apples.',
'Many används med räkneliga substantiv i plural: many books. Much används med oräkneliga: much water. A lot of fungerar med båda. A few = några räkneliga; a little = lite oräkneligt.',
'Some är vanligt i erbjudanden och önskemål: Would you like some water? Few/little kan betyda för få/för lite, medan a few/a little visar att något finns. Less används vanligen med oräkneligt och fewer med räknelig plural.'
],[
'''I have ___ apples in my bag.|some|any~much|En positiv mening med flera äpplen använder här some.
I don’t have ___ homework today.|any|many~a few|Any används i negation; homework är oräkneligt.
Are there ___ books on the shelf?|any|much~a little|Any passar i en neutral fråga, books är plural.
We need ___ water.|some|many~a few|Water är oräkneligt: some water.
She hasn’t got ___ money.|any|many~a few|Any används i negation; money är oräkneligt.
There are ___ students outside.|some|much~a little|Students är räknelig plural.''',
'''How ___ books do you have?|many|much~little|Books kan räknas, använd many.
How ___ water do we need?|much|many~few|Water är oräkneligt, använd much.
There are a ___ seats left.|few|little~much|Seats är räknelig plural: a few.
We have a ___ time before the bus comes.|little|few~many|Time är oräkneligt: a little.
How ___ people are in your class?|many|much~little|People är plural och räkneliga.
I don’t have ___ information yet.|much|many~a few|Information är oräkneligt.''',
'''Would you like ___ water?|some|many~a few|Some är vanligt i erbjudanden; water är oräkneligt.
We should use ___ plastic.|less|fewer~many|Plastic är oräkneligt: less.
There are ___ cars on this road than before.|fewer|less~much|Cars är räknelig plural: fewer.
We have very ___ time, so we must hurry.|little|few~many|Little passar med det oräkneliga time.
There are very ___ tickets left, so book now.|few|little~much|Tickets är räkneliga: few.
Could I have a ___ more milk, please?|little|few~many|Milk är oräkneligt: a little more.'''
],('We are planning a picnic. We need {0} (some/any) sandwiches. How {1} (much/many) people are coming? We don’t have {2} (some/any) juice. There is a {3} (little/few) water. We have a {4} (little/few) apples. How {5} (much/many) money do we need?',['some','many','any','little','few','much']),
'many|räkneliga i plural;much|oräkneliga;a few|några räkneliga;a little|lite oräkneligt;fewer|färre räkneliga;less|mindre oräkneligt',
['Beskriv vad du har och inte har i väskan med some och any.','Planera en måltid. Använd much, many, a few och a little.','Skriv råd för att minska avfall. Använd less, fewer och ett erbjudande med some.'])
T('modals','Can, should & must','Förmåga, råd & regler','Beskriv & bygg','Vad kan du göra? Vad borde eller måste du göra?',[
'Can visar ofta förmåga: I can swim. Can följs av grundform och får aldrig -s. Neka med cannot eller can’t. Fråga: Can you swim?',
'Should används för råd: You should rest. Must uttrycker ofta ett starkt krav: You must wear a helmet. Båda följs av grundform utan to.',
'Mustn’t betyder att det är förbjudet. Don’t have to betyder att det inte är nödvändigt. You mustn’t run här förbjuder springande. You don’t have to run säger att du inte behöver springa. Could kan visa tidigare förmåga eller en artig fråga.'
],[
'''I can ___ English.|speak|speaks~speaking|Can följs av grundformen speak.
She ___ swim very well.|can|cans~is can|Can ändras inte med she.
Can you ___ me?|help|helps~helping|Efter can står grundformen.
He cannot ___ a car yet.|drive|drives~driving|Cannot följs av grundformen.
We can ___ after school.|meet|meets~meeting|Can följs av meet.
They can ___ the piano.|play|plays~played|Can följs av play.''',
'''You should ___ more water.|drink|drinks~to drink|Should följs av grundformen utan to.
We must ___ our tickets.|bring|brings~to bring|Must följs av grundformen bring.
She should ___ a break.|take|takes~to take|Should följs av take.
You must not ___ here.|park|parks~to park|Must not följs av grundformen.
Can he ___ with us?|come|comes~to come|Can följs av come.
You shouldn’t ___ up so late.|stay|stays~to stay|Shouldn’t följs av grundformen.''',
'''The sign says NO ENTRY. You ___ go in.|mustn’t|don’t have to~must|Mustn’t visar ett förbud.
The homework is optional. You ___ do it.|don’t have to|mustn’t~must|Don’t have to betyder att det inte är nödvändigt.
When I was five, I ___ already swim.|could|can~must|Could visar förmåga i dåtid.
___ you help me, please?|Could|Mustn’t~Shouldn’t|Could används i artiga frågor.
Visitors ___ wear safety glasses. It is a strict rule.|must|can~don’t have to|Must visar ett krav.
You ___ bring lunch; the school provides it.|don’t have to|mustn’t~cannot|Det behövs inte: don’t have to.'''
],('At our climbing club, you must {0} (wear) a helmet. You should {1} (listen) to the instructor. You can {2} (ask) for help. You must not {3} (climb) alone. You should {4} (check) your equipment. You don’t have to {5} (bring) your own helmet; we provide one.',['wear','listen','ask','climb','check','bring']),
'can|kan;can’t|kan inte;should|borde;must|måste;mustn’t|får inte;don’t have to|behöver inte',
['Skriv tre saker du kan eller inte kan göra.','Ge en kompis tre råd med should och skriv två regler med must.','Skriv information till en klubb. Skilj mellan krav, förbud och sådant som är frivilligt.'])
T('questions','Questions & word order','Frågeord & ordföljd','Beskriv & bygg','Who, what, where, when, why och how.',[
'Frågeord hjälper dig att välja vilken information du vill ha: who = vem, what = vad, where = var, when = när, why = varför, how = hur. Where are you? What do you like?',
'I frågor med to be byter subjektet och verbet plats: Where is she? Med andra verb används ofta do/does/did: Where does she live? Efter hjälpverbet står huvudverbet i grundform.',
'Om who är subjekt behövs ofta inget do: Who lives here? Jämför Who do you know? där you är subjekt. I indirekta frågor används påståendeordföljd: Do you know where she lives?'
],[
'''___ is your name?|What|Where~When|What frågar efter vad, här ett namn.
___ do you live?|Where|Who~When|Where frågar efter plats.
___ is your birthday?|When|Who~Where|When frågar efter tid.
___ are you tired?|Why|Who~Where|Why frågar efter anledning.
___ is that student?|Who|When~Why|Who frågar efter en person.
___ do you get to school?|How|Who~What time is|How frågar här efter färdsätt.''',
'''Where ___ your sister live?|does|do~is|Your sister är singular, och live kräver does.
What time ___ the lesson start?|does|do~are|The lesson är singular: does.
Why ___ you late yesterday?|were|did~was|Late är adjektiv och yesterday visar dåtid: were.
When did you ___ home?|get|got~gets|Efter did står get i grundform.
How many books ___ you have?|do|does~are|You använder do med have.
Where ___ your bag?|is|do~does|Bag är singular; fråga med to be.''',
'''Who ___ next door?|lives|does lives~live|Who är subjekt: inget do behövs och verbet får -s.
Do you know where she ___?|lives|does live~live|En indirekt fråga använder påståendeordföljd.
Can you tell me what time it ___?|is|does~are|Indirekt fråga: what time it is.
Who ___ you meet yesterday?|did|does~are|You är subjekt; past simple kräver did.
Could you explain why they ___ upset?|are|do~is|Indirekt fråga med plural: why they are upset.
How long ___ you lived here?|have|has~do|Perfektfråga: have you lived.'''
],('Maya meets a new student. “{0} is your name?” she asks. “Alex.” “{1} do you live?” “Near the park.” “{2} do you get here?” “By bus.” “{3} is your birthday?” “In May.” “{4} is your favourite singer?” “A singer from Canada.” “{5} do you like her?” “Her songs tell great stories.”',['What','Where','How','When','Who','Why']),
'who|vem;what|vad;where|var;when|när;why|varför;how|hur',
['Skriv tre frågor till en ny klasskamrat.','Gör en kort intervju med frågor om plats, tid och intressen. Använd be, do och did.','Skriv direkta och indirekta frågor till en resebyrå. Använd Do you know …? och Can you tell me …?'])
T('connectors','Linking words','Binda ihop meningar','Beskriv & bygg','And, but, because, so och although.',[
'And lägger till information. But visar en skillnad eller kontrast. Because förklarar varför. I like music and games. I am tired, but happy. I stayed home because I was ill.',
'So visar ett resultat: It rained, so we stayed inside. Because ger orsaken: We stayed inside because it rained. Then hjälper dig att visa vad som hände sedan.',
'Although betyder även om eller fastän och markerar en kontrast. However betyder däremot eller dock och används ofta i en ny mening. Använd inte både although och but för samma koppling. Sambandsord hjälper läsaren att följa resonemanget.'
],[
'''I like music ___ games.|and|because~although|And lägger till en sak i samma lista.
I stayed home ___ I was ill.|because|and~although|Because ger orsaken till att jag stannade hemma.
I wanted to go out, ___ I was too tired.|but|because~and because|But visar en kontrast.
She likes both art ___ music.|and|but~because|Both … and kopplar ihop två saker.
We wore coats ___ it was cold.|because|although~but|Kylan är orsaken: because.
He is young, ___ he is very experienced.|but|because~so because|But markerar kontrast.''',
'''It was raining, ___ we stayed inside.|so|because~although|So ger följden av regnet.
We stayed inside ___ it was raining.|because|so~although|Because ger orsaken.
I finished my homework. ___ I called my friend.|Then|Because~Although|Then visar nästa händelse.
She was tired, ___ she kept working.|but|because~so because|But visar att hon fortsatte trots tröttheten.
We missed the bus, ___ we walked to school.|so|because~although|So visar följden av att bussen missades.
I practise every day ___ I want to improve.|because|although~but|Because visar anledningen till träningen.''',
'''___ it was cold, we went swimming.|Although|Because~So|Although visar kontrasten mellan kyla och bad.
The film was long. ___, it was interesting.|However|Because~Although|However kan koppla två hela meningar med kontrast.
She studied hard; ___, she passed the test.|therefore|although~because|Therefore visar slutsats eller följd.
I like the book ___ the ending is disappointing.|although|so~because of|Although visar en kontrast och följs av en sats.
___ his illness, he came to school.|Despite|Although~Because|Despite följs här av ett substantiv, inte en hel sats.
I prefer walking, ___ my sister prefers cycling.|whereas|because~so|Whereas jämför två personers olika preferenser.'''
],('I enjoy our game club {0} (because/but) everyone is welcome. We play board games {1} (and/because) card games. Some games are difficult, {2} (but/because) we help each other. Last week it rained, {3} (so/because) more people came. We played a quick game. {4} (Then/Although) we tried a longer one. I stayed late {5} (because/although) I was having fun.',['because','and','but','so','Then','because']),
'and|och;but|men;because|eftersom;so|så / därför;although|även om;however|däremot / dock',
['Skriv tre meningar med and, but och because.','Berätta om en dag. Använd because för orsak, so för följd och then för ordning.','Skriv en kort åsikt om en skolregel. Ge skäl och bemöt en annan åsikt med although eller however.'])
# Correct a distractor that also formed a grammatical question.
for t in TOPICS:
    if t['id']=='do':
        q=next(q for q in t['questions'] if q['prompt']=='___ he swim well?')
        q['options']=['Can','Do','Are']
    if t['id']=='articles':
        for q in t['questions']:
            q['options']=[o for o in q['options'] if ' ' not in o]
            if q['answer'] in ['a','an']:
                q['instruction']='Välj a eller an. Utgå från det första ljudet.'
    for q in t['questions']:
        q['sentence']=q['prompt'].replace('___',q['answer'])
# Text variants allow the normal spelling alternatives taught in Swedish schools.
for t in TOPICS:
    if t['id']=='perfect': t['story']['alternatives']={'4':['learned','learnt']}
# Visual support is attached to the exact question it illustrates.
prepositions=next(t for t in TOPICS if t['id']=='prepositions')
spatial=[
 ('preposition-in','Nycklar ligger inuti en öppen väska.','The keys are ___ the bag.'),
 ('preposition-on','En bok ligger ovanpå ett skrivbord.','The book is lying ___ the desk.'),
 ('preposition-under','Ett par skor står under en säng.','The shoes are ___ the bed.'),
 ('preposition-between','Maya står mellan Leo och Sam.',None),
 ('preposition-next','En busshållplats står bredvid skolan.',None),
 ('preposition-wall','En affisch sitter på en vägg.',None),
]
for q,(asset,alt,prompt) in zip(prepositions['questions'][:6],spatial):
    q['image']={'src':f'assets/{asset}.svg','alt':alt}
    if prompt:q['prompt']=prompt
    q['sentence']=q['prompt'].replace('___',q['answer'])
    q['instruction']='Titta på bilden. Vilket ord eller vilken fras passar i luckan?'
prepositions['questions'][0]['why']='In betyder i. Nycklarna ligger inuti väskan.'
prepositions['questions'][1]['why']='On betyder på. Boken ligger på skrivbordets ovansida.'
prepositions['questions'][2]['why']='Under betyder under. Skorna står under sängen.'
for q,(asset,alt) in zip(prepositions['questions'][12:15],[
 ('preposition-into','En person går från korridoren in genom dörren till ett rum.'),
 ('preposition-across','En person går över en bro från ena sidan till den andra.'),
 ('preposition-through','Ett tåg färdas genom en tunnel.'),
]):q['image']={'src':f'assets/{asset}.svg','alt':alt}
prepositions['visualExamples']=[{'src':f'assets/{name}.svg','alt':alt,'label':label} for (name,alt,label) in [
 ('preposition-in','Nycklar ligger inuti en öppen väska.','in'),
 ('preposition-on','En bok ligger ovanpå ett skrivbord.','on'),
 ('preposition-under','Ett par skor står under en säng.','under'),
]]
mia={'src':'assets/mia-at-desk.png','width':2172,'height':724,'alt':'Mia sitter vid ett skrivbord. Hon ritar i en anteckningsbok och håller en telefon. Det finns böcker, pennor, en lampa och en växt.'}
football={'src':'assets/football-break.png','width':1448,'height':1086,'alt':'Två elever spelar fotboll. En annan elev sitter på en bänk och en flicka står bredvid med ett papper. En väska står vid bänken.'}
room={'src':'assets/study-room.svg','alt':'Ett rum med ett fönster, ett bord, en stol, fyra böcker, en väska och en boll.'}
for id,image,prompts,examples in [
 ('continuous',mia,['Beskriv tre saker som händer i bilden. Börja med She is … .','Beskriv fyra saker i bilden med pågående form. Lägg till en fråga och en nekande mening.','Beskriv vad Mia gör i bilden och föreställ dig vad hon brukar göra efter skolan. Skilj på vad du ser och vad du antar.'],['She is sitting at a desk.','She is drawing in her notebook.','She is holding a phone.']),
 ('be',football,['Beskriv personerna i bilden med tre meningar. Använd She is …, He is … och They are … .','Beskriv var personerna är och hur de ser ut att känna sig. Skriv fyra meningar och en fråga med to be.','Skriv ett meddelande om gruppen på bilden till en ny klasskamrat. Beskriv vad du ser och ställ två frågor med to be.'],['They are outside.','The girl is happy.','The boys are ready to play.']),
 ('pronouns',football,['Beskriv bilden med tre meningar. Använd he, she och they.','Beskriv personerna i bilden med minst fyra meningar. Använd subjektpronomen och ett ägandeord, till exempel her.','Skriv en kort scen inspirerad av bilden. Använd subjekt- och objektpronomen samt minst ett ägandeord. Skilj det du ser från det du hittar på.'],['She is holding a piece of paper.','They are playing football.','Her shoes are white.']),
 ('there',room,['Beskriv tre saker som finns i rummet. Använd There is … och There are … .','Beskriv vad som finns i rummet och ställ två frågor med Is there …? eller Are there …?','Beskriv bilden och föreställ dig hur rummet såg ut tidigare. Använd there is/are och there was/were. Markera vad du hittar på.'],['There is a bag on the table.','There are four books on the shelf.','There is a window.']),
 ('plurals',room,['Skriv tre meningar om sakerna i rummet. Använd både en sak och flera saker.','Beskriv rummet med minst fyra meningar. Använd både singular och plural.','Föreslå vad ett studierum behöver. Utgå från bilden och använd pluralformer samt some information eller some advice.'],['There is one bag.','There are four books.','There is a window.']),
 ('prepositions',mia,['Beskriv var tre saker finns i bilden med in, on eller next to.','Beskriv fem saker i bilden med olika platsord. Skriv också när du brukar göra läxor med in, on eller at.','Skriv ett kort meddelande som beskriver rummet på bilden och när du vill träffa en kompis. Använd både plats- och tidsprepositioner.'],['The phone is in her hand.','The books are on the desk.','The plant is next to the lamp.']),
]:
    t=next(t for t in TOPICS if t['id']==id)
    t['imagePractice']={'image':image,'prompts':prompts,'examples':examples}
continuous=next(t for t in TOPICS if t['id']=='continuous')
for index,prompt,answer,options,why,image in [
 (1,'She ___ drawing in her notebook.','is',['is','am','are'],'She använder is före verb-ing.',mia),
 (2,'The two players ___ playing football.','are',['are','is','am'],'Two players är plural, så använd are.',football),
 (4,'The boy is ___ on the bench.','sitting',['sitting','sit','sits'],'Efter is används verb-ing. Sit dubblerar t: sitting.',football),
]:
    q=continuous['questions'][index];q.update(prompt=prompt,answer=answer,options=options,why=why,image=image,sentence=prompt.replace('___',answer))

from content_banks import enrich
enrich(TOPICS)
assert len(TOPICS)==20
Path('webb/data.js').write_text('window.GRAMMAR = '+json.dumps(TOPICS,ensure_ascii=False)+';\n')
print(f'{len(TOPICS)} topics, {sum(len(t["questions"]) for t in TOPICS)} levelled questions, {sum(len(st["answers"]) for t in TOPICS for st in t["stories"])} text gaps, {sum(len(t["matchBank"]) for t in TOPICS)} memory pairs')
