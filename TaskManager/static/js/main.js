document.getElementById('new-task').addEventListener("click",function(){
    document.querySelector("#newtask-section").style.display="flex";
})

document.getElementById("popover-close").addEventListener("click",function(){
    document.querySelector("#newtask-section").style.display="none";
})

// var message_ele = document.getElementById("signup-messages");
// setTimeout(function(){ 
//    message_ele.style.display = "none"; 
// }, 3000);

// document.getElementById('new-task').addEventListener("click",function(){
//     document.querySelector("#task-completion-notify-section").style.display="flex";
// })

// document.getElementById("task-finish-button").addEventListener("click",function(){
//     document.querySelector("#task-completion-notify-section").style.display="none";
// })
