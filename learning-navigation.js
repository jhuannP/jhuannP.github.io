(function(root){
 const courseId=/^[a-z0-9-]+$/;
 function parse(route){const split=route.indexOf('?');return {path:split<0?route:route.slice(0,split),params:new URLSearchParams(split<0?'':route.slice(split+1))}}
 function step(course,raw){if(!/^[1-9][0-9]*$/.test(raw||''))return null;const index=Number(raw)-1;return Number.isSafeInteger(index)&&course.studyGuide?.[index]?{index,value:course.studyGuide[index]}:null}
 function context(course,lesson,raw){const found=step(course,raw);return found&&found.value.lessons.some(link=>link.id===lesson)?{course,step:found}:null}
 function lessonLink(id,course,index){return '#aula/'+encodeURIComponent(id)+'?'+new URLSearchParams({percurso:course,etapa:String(index+1)})}
 function returnLink(course,index){return '#curso/'+encodeURIComponent(course)+'?'+new URLSearchParams({etapa:String(index+1)})}
 function related(lesson){
  const labels={preparation:'Revisar a base',application:'Aplicar esta ideia'},seen=new Set([lesson.id]);
  return (Array.isArray(lesson.relatedLessons)?lesson.relatedLessons:[]).flatMap(item=>{
   if(!item||typeof item.id!=='string'||!courseId.test(item.id)||seen.has(item.id)||!Object.hasOwn(labels,item.relation)||typeof item.title!=='string'||!item.title.trim()||typeof item.reason!=='string'||!item.reason.trim())return [];
   seen.add(item.id);
   return [{id:item.id,title:item.title,reason:item.reason,label:labels[item.relation],href:'#aula/'+encodeURIComponent(item.id)}];
  });
 }
 const api={parse,step,context,lessonLink,returnLink,related,validCourse:id=>courseId.test(id||'')};
 if(typeof module==='object'&&module.exports)module.exports=api;else root.LearningNavigation=api;
})(typeof window==='undefined'?{}:window);
