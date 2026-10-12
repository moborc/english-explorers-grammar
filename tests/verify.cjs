const fs=require('fs'),vm=require('vm'),assert=require('assert');
// A small DOM test adapter lets us exercise shipped event handlers without a browser server.
class Element{
 constructor(tag='div',attrs={},parent=null){this.tagName=tag.toUpperCase();this.attributes={...attrs};this.parentNode=parent;this.children=[];this.handlers={};this.value=attrs.value||'';this.disabled='disabled'in attrs;this.checked='checked'in attrs;this._text='';this._html='';this.style={};this.dataset={};for(const [k,v]of Object.entries(attrs))if(k.startsWith('data-'))this.dataset[k.slice(5).replace(/-([a-z])/g,(_,c)=>c.toUpperCase())]=v;this.classList={contains:c=>(this.attributes.class||'').split(/\s+/).includes(c),add:c=>{if(!this.classList.contains(c))this.attributes.class=((this.attributes.class||'')+' '+c).trim();},remove:c=>{this.attributes.class=(this.attributes.class||'').split(/\s+/).filter(x=>x!==c).join(' ');},toggle:(c,force)=>{const on=force===undefined?!this.classList.contains(c):force;on?this.classList.add(c):this.classList.remove(c);return on;}};}
 get id(){return this.attributes.id||'';}
 set id(v){this.attributes.id=v;}
 set innerHTML(html){this._html=html;this.children=[];parse(String(html),this);}
 get innerHTML(){return this._html;}
 set textContent(v){this._text=String(v);this.children=[];}
 get textContent(){return this._text||this.children.map(c=>c.textContent).join('');}
 set className(v){this.attributes.class=v;}get className(){return this.attributes.class||'';}
 setAttribute(k,v){this.attributes[k]=String(v);}
 getAttribute(k){return this.attributes[k];}
 addEventListener(name,fn){(this.handlers[name]??=[]).push(fn);}
 focus(){document.activeElement=this;}
 select(){this.selected=true;}
 showModal(){this.open=true;}close(){this.open=false;for(const f of this.handlers.close||[])f({target:this});}
 append(c){this.children.push(c);c.parentNode=this;}
 remove(){this.parentNode.children=this.parentNode.children.filter(c=>c!==this);}
 click(){emit(this,'click');}
 closest(sel){for(let p=this;p;p=p.parentNode)if(match(p,sel))return p;return null;}
 querySelectorAll(sel){return find(this,sel);}
 querySelector(sel){return find(this,sel)[0]||null;}
}
function match(el,selector){const s=selector.trim();if(s.startsWith('#'))return el.attributes.id===s.slice(1);if(s.startsWith('.'))return el.classList.contains(s.slice(1));if(s.startsWith('[')){const m=s.match(/^\[([^=\]]+)(?:="([^"]*)")?\]$/);return !!m&&(m[2]===undefined?m[1]in el.attributes:el.attributes[m[1]]===m[2]);}return el.tagName.toLowerCase()===s;}
function find(root,sel){const selectors=sel.split(',');const out=[];function visit(p){for(const c of p.children){if(selectors.some(s=>match(c,s)))out.push(c);visit(c);}}visit(root);return out;}
function parse(html,root){const stack=[root],voids=new Set(['input','meta','link','br','hr','img']);for(const token of html.match(/<[^>]+>|[^<]+/g)||[]){if(token.startsWith('<!--')||token.startsWith('<!'))continue;if(token.startsWith('</')){if(stack.length>1)stack.pop();continue;}if(token.startsWith('<')){const m=token.match(/^<([\w-]+)/);if(!m)continue;const attrs={};const part=token.slice(m[0].length,-1);for(const a of part.matchAll(/([\w-]+)(?:="([^"]*)"|='([^']*)'|=([^\s>]+))?/g))attrs[a[1]]=decode(a[2]??a[3]??a[4]??'');const el=new Element(m[1],attrs,stack.at(-1));stack.at(-1).children.push(el);if(!voids.has(m[1])&&!token.endsWith('/>'))stack.push(el);}else{const el=new Element('#text',{},stack.at(-1));el._text=decode(token);stack.at(-1).children.push(el);}}}
function decode(s){return s.replace(/&(?:amp|lt|gt|quot|#39|nbsp);/g,c=>({'&amp;':'&','&lt;':'<','&gt;':'>','&quot;':'"','&#39;':"'",'&nbsp;':' '}[c]));}
function emit(el,name,extra={}){const ev={target:el,key:'',preventDefault(){},...extra};for(let p=el;p;p=p.parentNode)for(const fn of p.handlers[name]||[])fn(ev);}
const document=new Element('document');document.body=new Element('body',{},document);document.children=[document.body];document.createElement=t=>new Element(t);parse(fs.readFileSync('webb/index.html','utf8'),document.body);
const listeners={},storage=new Map();let hash='';const location={get hash(){return hash;},set hash(v){hash=v?'#'+v.replace(/^#/,''):'';for(const f of listeners.hashchange||[])f();}};
const timers=new Map();let timerClock=0,timerSequence=0;
function fakeSetTimeout(fn,delay){const id=++timerSequence;timers.set(id,{fn,due:timerClock+delay});return id;}
function fakeClearTimeout(id){timers.delete(id);}
function advanceTimers(ms){timerClock+=ms;for(const [id,t]of [...timers])if(t.due<=timerClock){timers.delete(id);t.fn();}}
let reduceMotion=false;
const window={matchMedia:()=>({matches:reduceMotion}),addEventListener:(n,f)=>(listeners[n]??=[]).push(f),scrollTo(){},print(){}};const sandbox={window,document,location,sessionStorage:{getItem:k=>storage.get(k)||null,setItem:(k,v)=>storage.set(k,v)},navigator:{clipboard:{writeText:async()=>{}}},console,Blob,URL,setTimeout:fakeSetTimeout,clearTimeout:fakeClearTimeout};
vm.createContext(sandbox);vm.runInContext(fs.readFileSync('webb/data.js','utf8'),sandbox);vm.runInContext(fs.readFileSync('webb/app.js','utf8').replace('window.GrammarChecks={normal,accepts,topicById};','window.GrammarChecks={normal,accepts,topicById}; window.__test={get state(){return state;}};'),sandbox);
const $=s=>document.querySelector(s),click=s=>{assert($(s),'missing control '+s);$(s).click();},topic=id=>location.hash=id+'/0';
const data=window.GRAMMAR;
assert.equal(data.length,20);assert.equal(new Set(data.map(t=>t.id)).size,20);
for(const t of data){assert.equal(t.questions.length,36,t.id);assert.equal(t.rules.length,3);assert.equal(t.pairs.length,6);assert.equal(t.use.length,3);assert.equal(t.story.answers.length,6);for(let level=0;level<3;level++){const qs=t.questions.filter(q=>q.level===level);assert.equal(qs.length,12);for(const q of qs){assert.equal((q.prompt.match(/___/g)||[]).length,1,q.id);assert(q.options.includes(q.answer));assert.equal(new Set(q.options).size,q.options.length);assert(q.why.length>10);assert(!q.sentence.includes('___'));assert(q.options.every(o=>o===q.answer||!window.GrammarChecks.accepts(o,q.answer)));}}
 const placeholders=[...t.story.text.matchAll(/\{(\d+)\}/g)].map(m=>Number(m[1]));assert.equal(placeholders.length,6);assert.equal(new Set(placeholders).size,6);
}
for(const [a,b]of [["isn't",'is not'],["doesn't",'does not'],["can't",'cannot'],[' I am ready! ','i am ready'],["I’m ready.",'I am ready']])assert(window.GrammarChecks.accepts(a,b),a);
// Every topic, level and activity must render actual working controls.
for(const t of data)for(let l=0;l<3;l++)for(const mode of ['choice','gap','builder','fix','text','memory','wordmatch','streak','write']){location.hash=`${t.id}/${l}/${mode}`;assert($('.exercise-panel'),`${t.id} ${l} ${mode}`);assert(!$('#main').innerHTML.includes('undefined'));}
// Complete a multiple-choice pass, deliberately needing a retry on one question.
location.hash='be/0/choice';for(let n=0;n<6;n++){const prompt=$('.question-text').textContent.replace(/\s*\?\s*/, '___');const q=data[0].questions.find(q=>q.level===0&&q.prompt.replace(/\s/g,'')===prompt.replace(/\s/g,''));assert(q,'unknown prompt '+prompt);const buttons=$('#main').querySelectorAll('[data-choice]');if(n===0){const wrong=buttons.find(b=>b.textContent!==q.answer);wrong.click();assert(wrong.disabled);assert($('#feedback').textContent.includes('Prova'));}buttons.find(b=>b.textContent===q.answer).click();click('[data-action="next"]');}
assert($('.result'));assert($('.result-number').textContent.includes('5 / 6'));let stored=JSON.parse(storage.get('ee-grammar-v1'));assert.equal(stored.sessions.length,1);
click('[data-action="retry-misses"]');assert($('#answer'));click('[data-action="show-answer"]');click('[data-action="next"]');assert($('.result'));
// Mixed-review retries must not access a null topic. This path also supports restart.
location.hash='review/2';for(let n=0;n<12;n++){click('[data-action="show-answer"]');click('[data-action="next"]');}click('[data-action="retry-misses"]');assert($('#answer'));click('[data-action="show-answer"]');click('[data-action="next"]');
// Complete a sentence builder from the actual shuffled bank.
location.hash='be/0/builder';const bank=$('#main').querySelectorAll('[data-word]');const words=bank.map(b=>b.textContent);const q=data[0].questions.find(q=>q.level===0&&q.sentence.split(/\s+/).every(w=>words.includes(w)));assert(q);for(const w of q.sentence.split(/\s+/)){const b=$('#main').querySelectorAll('[data-word]').find(b=>!b.disabled&&b.textContent===w);assert(b,w);b.click();}click('[data-action="check"]');assert($('#feedback').textContent.includes('Rätt!'));
// Texts: preserve initial-control score and allow both British and American learned/learnt.
location.hash='perfect/2/text';let st=window.__test.state.session.story;if(!st.alternatives){click('[data-action="restart"]');st=window.__test.state.session.story;}for(const input of $('#main').querySelectorAll('[data-gap]'))input.value=Number(input.dataset.gap)===4?'learnt':st.answers[Number(input.dataset.gap)];click('[data-action="check-text"]');assert($('#feedback').textContent.includes('Texten är klar'));assert($('#main').querySelectorAll('[data-gap]').every(el=>el.disabled));
// Memory: use exposed card contents to find every exact pair; repeated clicks do not duplicate records.
location.hash='be/0/memory';const m=window.__test.state.session.memory;
for(let pair=0;pair<6;pair++){const indices=m.cards.map((c,i)=>c.pair===pair?i:null).filter(i=>i!==null);click(`[data-card="${indices[0]}"]`);click(`[data-card="${indices[1]}"]`);}
assert.equal(m.matched.length,6);assert($('#feedback').textContent.includes('Alla sex par'));assert.equal(m.turns,6);
const beforeMemory=JSON.parse(storage.get('ee-grammar-v1')).sessions.length;
const matchedButton=$('#main').querySelectorAll('[data-card]')[0];assert(matchedButton.disabled);
assert.equal(JSON.parse(storage.get('ee-grammar-v1')).sessions.length,beforeMemory);
// Wrong memory pairs remain visible for exactly two seconds, with further flips blocked.
location.hash='be/0/memory';let activeMemory=window.__test.state.session.memory;
const first=0,second=activeMemory.cards.findIndex(c=>c.pair!==activeMemory.cards[first].pair);
click(`[data-card="${first}"]`);click(`[data-card="${second}"]`);
assert.equal(activeMemory.open.length,2);assert.equal(timers.size,1);assert(! $('[data-action="memory-turn"]'));
assert($('#main').querySelectorAll('[data-card]').every(b=>b.disabled));
advanceTimers(1999);assert.equal(activeMemory.open.length,2);assert($(`[data-card="${first}"]`).classList.contains('open'));
advanceTimers(1);assert.equal(activeMemory.open.length,2);assert($(`[data-card="${first}"]`).classList.contains('turn-closing'));assert($('#main').querySelectorAll('[data-card]').every(b=>b.disabled));
advanceTimers(160);assert.equal(activeMemory.open.length,0);assert($(`[data-card="${first}"]`).classList.contains('turn-opening'));assert($(`[data-card="${first}"]`).classList.contains('face-down'));assert($(`[data-card="${first}"]`).disabled);
advanceTimers(160);assert.equal(timers.size,0);assert(!$(`[data-card="${first}"]`).disabled);assert(!$(`[data-card="${first}"]`).classList.contains('turn-opening'));
// Navigation must cancel pending flips; an old timer must never affect a new game.
click(`[data-card="${first}"]`);click(`[data-card="${second}"]`);assert.equal(timers.size,1);
location.hash='past/0/choice';assert.equal(timers.size,0);advanceTimers(2000);assert($('.choices'));
location.hash='be/0/memory';activeMemory=window.__test.state.session.memory;
const mismatch=activeMemory.cards.findIndex(c=>c.pair!==activeMemory.cards[0].pair);
click('[data-card="0"]');click(`[data-card="${mismatch}"]`);assert.equal(timers.size,1);
location.hash='be/0/memory';assert.equal(timers.size,0);const newMemory=window.__test.state.session.memory;click('[data-card="0"]');advanceTimers(2000);assert.equal(newMemory.open.length,1);
// Cancelling during a flip must not leave a timer or mutate the replacement board.
location.hash='be/0/memory';activeMemory=window.__test.state.session.memory;
const flipMismatch=activeMemory.cards.findIndex(c=>c.pair!==activeMemory.cards[0].pair);
click('[data-card="0"]');click(`[data-card="${flipMismatch}"]`);advanceTimers(2000);assert.equal(activeMemory.turnPhase,'closing');
location.hash='be/0/memory';assert.equal(timers.size,0);advanceTimers(160);assert.equal(window.__test.state.session.memory.turning.length,0);
// Reduced-motion users retain an instant reset after the two-second reading pause.
reduceMotion=true;activeMemory=window.__test.state.session.memory;
const reducedMismatch=activeMemory.cards.findIndex(c=>c.pair!==activeMemory.cards[0].pair);
click('[data-card="0"]');click(`[data-card="${reducedMismatch}"]`);advanceTimers(2000);
assert.equal(activeMemory.open.length,0);assert.equal(activeMemory.turning.length,0);assert.equal(timers.size,0);reduceMotion=false;
// Picture practice is tied to an exact question and uses accessible local assets.
for(const t of data){for(const q of t.questions)if(q.image){assert(fs.existsSync('webb/'+q.image.src));assert(q.image.alt.length>10);}if(t.imagePractice){assert.equal(t.imagePractice.prompts.length,3);assert(fs.existsSync('webb/'+t.imagePractice.image.src));}}
location.hash='prepositions/0';assert($('.visual-examples'));assert($('.visual-examples').querySelector('img').getAttribute('alt').length>10);
location.hash='continuous/0/write';assert($('.exercise-visual'));assert($('#main').innerHTML.includes('mia-at-desk.png'));click('[data-action="model"]');assert($('#writing-model').textContent.includes('She is drawing'));
// Writing is a self-check, not automatic correctness; draft survives navigation.
location.hash='be/0/write';$('#writing-answer').value='I am a student. My friend is kind.';emit($('#writing-answer'),'input');click('[data-action="finish-writing"]');assert($('#feedback').textContent.includes('Gör din egen'));for(const id of ['writing-check1','writing-check2','writing-check3'])$('#'+id).checked=true;click('[data-action="finish-writing"]');assert($('#feedback').textContent.includes('inte rättats automatiskt'));location.hash='past/0';location.hash='be/0/write';assert($('#writing-answer').value.includes('I am a student'));
// New passes must vary selections while retaining the chosen topic/level and six-pair size.
for(const t of data)for(let level=0;level<3;level++){
 for(const mode of ['memory','wordmatch','choice']){
  location.hash=`${t.id}/${level}/${mode}`;let previous=null;
  for(let n=0;n<6;n++){
   const session=window.__test.state.session,items=mode==='choice'?session.questions:session.pairs;
   assert.equal(items.length,6);assert.equal(new Set(items.map(x=>x.id)).size,6);
   if(mode==='choice')assert(items.every(q=>q.level===level));else{
    assert(items.every(p=>p.minLevel<=level));assert.equal(new Set(items.map(p=>p.left.toLowerCase())).size,6);assert.equal(new Set(items.map(p=>p.right.toLowerCase())).size,6);
   }
   const ids=items.map(x=>x.id).sort().join('|');assert.notEqual(ids,previous);previous=ids;click('[data-action="restart"]');
  }
 }
 location.hash=`${t.id}/${level}/text`;const storyId=window.__test.state.session.story.id;click('[data-action="restart"]');assert.notEqual(window.__test.state.session.story.id,storyId);
 for(const story of t.stories){assert.equal(story.answers.length,6);assert.equal(new Set([...story.text.matchAll(/\{(\d+)\}/g)].map(m=>m[1])).size,6);}
}
// Visible matching: wrong pairs do not count; either column can be chosen first.
location.hash='articles/0/wordmatch';const matchSession=window.__test.state.session;
const matchButton=(pair,side)=>$('#main').querySelectorAll('[data-match]').find(b=>Number(b.dataset.match)===pair&&Number(b.dataset.side)===side);
matchButton(0,0).click();matchButton(1,1).click();assert.equal(matchSession.match.matched.length,0);assert($('#feedback').textContent.includes('inte ihop'));
for(let pair=0;pair<6;pair++){matchButton(pair,1).click();assert.equal(matchButton(pair,1).getAttribute('aria-pressed'),'true');matchButton(pair,0).click();assert(matchButton(pair,0).classList.contains('pair-found'));assert(matchButton(pair,0).disabled);}
assert.equal(matchSession.match.matched.length,6);assert.equal(matchSession.match.turns,7);assert($('#feedback').textContent.includes('Alla sex par'));
const matchRecords=JSON.parse(storage.get('ee-grammar-v1')).sessions.length;matchButton(0,0).click();assert.equal(JSON.parse(storage.get('ee-grammar-v1')).sessions.length,matchRecords);
location.hash='past/1/streak';const streakQs=window.__test.state.session.questions;assert.equal(streakQs.length,12);assert.equal(new Set(streakQs.map(q=>q.id)).size,6);
location.hash='plurals/1/gap';assert(window.GrammarChecks.accepts('scarfs',data.find(t=>t.id==='plurals').questions.find(q=>q.answer==='scarves').alternatives));
// Search and focus remain usable without changing the exercise.
location.hash='';$('#search').value='dåtid';emit($('#search'),'input');assert($('#main').innerHTML.includes('Was &amp; were'));click('#focus-toggle');assert(document.body.classList.contains('focus'));click('#focus-toggle');assert(!document.body.classList.contains('focus'));
console.log('PASS: 720 questions, 240 text gaps, 359 match pairs; 540 topic/level/activity renders; random sampling/levels/new texts/Word Match;  grading, retry, mixed review, builder, text variants, memory flip phases/timing/cancellation/reduced motion, local image support, writing drafts, search and focus.');
