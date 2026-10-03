const fs=require('fs');
const {Document,Packer,Paragraph,TextRun,ImageRun,HeadingLevel,AlignmentType,LevelFormat,BorderStyle}=require('docx');
const RED='862222';
const src=fs.readFileSync('posts.md','utf8').split(/^## /m).filter(s=>s.trim());
function runs(t,base={}){const out=[];const re=/(\*\*[^*]+\*\*|\*[^*]+\*)/g;let last=0,m;
 while((m=re.exec(t))){if(m.index>last)out.push(new TextRun({text:t.slice(last,m.index),...base}));
  const s=m[0];if(s.startsWith('**'))out.push(new TextRun({text:s.slice(2,-2),bold:true,...base}));else out.push(new TextRun({text:s.slice(1,-1),italics:true,...base}));last=m.index+s.length;}
 if(last<t.length)out.push(new TextRun({text:t.slice(last),...base}));return out;}
const logo=fs.readFileSync('img/logo_c_crop.png');
const outDir=process.argv[2];
src.forEach((sec,idx)=>{
 const lines=sec.split('\n');const title=lines[0].trim();
 let img=null,img2=null,cat='',pdfs=[];const body=[];
 for(const l of lines.slice(1)){ if(l.startsWith('@pdf '))pdfs.push(l.slice(5).trim()); else if(l.startsWith('@img2 '))img2=l.slice(6).trim(); else if(l.startsWith('@img '))img=l.slice(5).trim(); else if(l.startsWith('@cat '))cat=l.slice(5).trim(); else body.push(l);}
 const ch=[];
 ch.push(new Paragraph({children:[new ImageRun({type:'png',data:logo,transformation:{width:90,height:70}})]}));
 ch.push(new Paragraph({heading:HeadingLevel.HEADING_1,spacing:{before:200,after:120},children:[new TextRun({text:'Thử thách Flow 7 ngày · '+title,color:RED,bold:true,size:32})]}));
 const m=title.match(/\(([^)]+)\)/);
 ch.push(new Paragraph({children:[new TextRun({text:'Ngày đăng: ',bold:true}),new TextRun(m?m[1]:'')]}));
 ch.push(new Paragraph({children:[new TextRun({text:'Danh mục trên Skool: ',bold:true}),new TextRun(cat)]}));
 const imgs=[img,img2].filter(Boolean);
 if(pdfs.length)ch.push(new Paragraph({children:[new TextRun({text:'File PDF đính kèm: ',bold:true}),new TextRun(pdfs.join(', '))]}));
 ch.push(new Paragraph({spacing:{after:160},border:{bottom:{style:BorderStyle.SINGLE,size:6,color:RED,space:4}},children:[new TextRun({text:'Hình đính kèm: ',bold:true}),new TextRun(imgs.map(i=>'10XHub_Flow7Ngay_'+i+'.png').join(', '))]}));
 for(const i of imgs){const d=fs.readFileSync('docjpg/10XHub_Flow7Ngay_'+i+'.jpg');ch.push(new Paragraph({alignment:AlignmentType.CENTER,spacing:{after:200},children:[new ImageRun({type:'jpg',data:d,transformation:{width:600,height:338}})]}));}
 let inEn=false;
 for(const raw of body){const l=raw.trim(); if(!l)continue;
  if(l==='@en'){inEn=true;ch.push(new Paragraph({heading:HeadingLevel.HEADING_2,spacing:{before:300,after:120},children:[new TextRun({text:'Bản tiếng Anh (English version)',color:RED,bold:true,size:26})]}));continue;}
  if(l.startsWith('- '))ch.push(new Paragraph({numbering:{reference:'b',level:0},spacing:{after:80},children:runs(l.slice(2))}));
  else if(/^\d+\. /.test(l))ch.push(new Paragraph({numbering:{reference:'n'+idx,level:0},spacing:{after:80},children:runs(l.replace(/^\d+\. /,''))}));
  else ch.push(new Paragraph({spacing:{after:160},children:runs(l)}));}
 const doc=new Document({styles:{default:{document:{run:{font:'Arial',size:22}}}},
  numbering:{config:[{reference:'b',levels:[{level:0,format:LevelFormat.BULLET,text:'•',alignment:AlignmentType.LEFT,style:{paragraph:{indent:{left:540,hanging:270}}}}]},{reference:'n'+idx,levels:[{level:0,format:LevelFormat.DECIMAL,text:'%1.',alignment:AlignmentType.LEFT,style:{paragraph:{indent:{left:540,hanging:300}}}}]}]},
  sections:[{properties:{page:{margin:{top:1000,bottom:1000,left:1100,right:1100}}},children:ch}]});
 const name=`10XHub_Flow7Ngay_Bai${idx}_${(img||'').replace(/^\d+_/,'')}.docx`;
 Packer.toBuffer(doc).then(b=>{fs.writeFileSync(outDir+'/'+name,b);console.log(name)});
});
