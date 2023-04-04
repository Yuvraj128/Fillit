var coll=document.getElementsByClassName("collapsible");

for(let i=0;i<coll.length;i++){
     coll[i].addEventListener("click",function(){
          this.classList.toggle("active");
          var content=this.nextElementSibling;
          if(content.style.maxHeight){
               content.style.maxHeight=null;
          }else{
               content.style.maxHeight=content.scrollHeight+"px";
          }
     });
}

function gettime(){
     let today=new Date();
     hours=today.getHours();
     minutes=today.getMinutes();
     if(hours<10){
          hours="0"+hours;
     }
     if(minutes<10){
          minutes="0"+minutes;
     }
     let time=hours+":"+minutes;
     return time;
}

function firstbotmessage(){
     let firstmessage="how it going?"
     document.getElementById("botstartermessage").innerHTML='<p class="bottext"><span>'+firstmessage+'</span></p>';

     let time=gettime();
     $("#chat-timestamp").append(time)
     document.getElementById("userinput").scrollIntoView(false);
}
firstbotmessage();

function gethardresponse(userText){
     let botresponse=getbotresponse(userText);
     let bothtml='<p class="bottext"><span>'+botresponse+'</span></p>';
     $("#chatbox").append(bothtml);

     document.getElementById("chat-bar-bottom").scrollIntoView(true);
}

function getresponse(){
     let usertext=$("#textinput").val();

     if(usertext==""){
          usertext="i love code palace";
     }
     let userhtml='<p class="usertext"><span>'+usertext+'</span></p>';
     $("#textinput").val("");
     $("#chatbox").append(userhtml)
     document.getElementById("chat-bar-bottom").scrollIntoView(true);
     setTimeout(()=>{
          gethardresponse(usertext);
     },1000)
}
function buttonsendtext(sampletext){
     let userhtml='<p class="usertext"><span>'+sampletext+'</span></p>';
     $("#textinput").val("");
     $("#chatbox").append(userhtml)
     document.getElementById("chat-bar-bottom").scrollIntoView(true);
}
function sendbutton(){

     getresponse();
}

function heartbutton(){
buttonsendtext('heart clicked')
}

$("#textinput").keypress(function(e){
     if(e.which==13){
          getresponse();
     }
})