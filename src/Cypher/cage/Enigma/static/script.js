const answerbox = document.querySelector(".dialog-box");
const querybutton = document.querySelector("input[type='submit']");
const speed = 60;
let i = 0;
let j = 1;
let txt = "Hell i am testing it right now >>>...."
let count = 0;

function Writer(renderbox, txt) {
   if(i < txt.length) {
     document.querySelector("#" + renderbox).innerHTML += txt.charAt(i);
     i++;
     setTimeout(function(){Writer(renderbox, txt);}, speed);
  }
  else{
    i = 0;
    // querybutton.disabled = false;
  }
}


function interval(){
  let ans = document.querySelector("#info");
  if(ans.innerHTML.length > 1 ){
    console.log(ans.innerHTML);
    dostuff(ans.innerHTML);
  }
  else{
    console.log(1);
    setInterval(interval, 10000);
  }
}


function dostuff(ans){
  // querybutton.disabled = true;
  count += 1;
  answerbox.style.display = 'block';
  let newbox = document.createElement("div");
  newbox.id = 'a' + count;
  // txt = "Hello I am Number" + count;
  answerbox.appendChild(newbox);
  Writer(newbox.id, ans);
}


interval();

querybutton.addEventListener('click', () => {
  // querybutton.disabled = true;
  // count += 1;
  // answerbox.style.display = 'block';
  // let newbox = document.createElement("div");
  // newbox.id = 'a' + count;
  // txt = "Hello I am Number" + count;
  // answerbox.appendChild(newbox);
  // Writer(newbox.id, txt);
});

