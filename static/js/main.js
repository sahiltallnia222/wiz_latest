
document.onclick=function(e){
    if(e.target.id!=='ac-icon'){
        box=document.getElementById('right-menu')
        box.style.display='none'
    }
}


const handle_icon_toggle=(box_id)=>{
    box=document.getElementById(box_id)
    if(box.style.display=='none' || box.style.display==''){
        box.style.display='block'
    }
    else{
        box.style.display='none'
    }
}
