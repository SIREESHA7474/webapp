function validatedata(){
    let v1,v2;
    v1=document.querySelector("#t1").value;
    v2=document.querySelector("#t2").value;
    if (v1<0 || v2<0)
        return false;
    else
        return true;      

}